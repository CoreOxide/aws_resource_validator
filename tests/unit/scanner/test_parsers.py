"""Unit tests for Terraform, CloudFormation, and .env parsers."""

from __future__ import annotations

from pathlib import Path

from aws_resource_validator.scanner.parsers import (
    parse_candidates,
    parse_cloudformation,
    parse_env_file,
    parse_terraform,
)
from aws_resource_validator.scanner.rules_map import is_dynamic_expression, is_ignorable_arn


def test_is_dynamic_expression() -> None:
    assert is_dynamic_expression("${var.my_bucket}") is True
    assert is_dynamic_expression("var.bucket_name") is True
    assert is_dynamic_expression("local.my_name") is True
    assert is_dynamic_expression("aws_s3_bucket.main.id") is True
    assert is_dynamic_expression("!Ref MyBucket") is True
    assert is_dynamic_expression("!Sub ${Environment}-bucket") is True
    assert is_dynamic_expression("Fn::Sub: ${AWS::StackName}-queue") is True
    assert is_dynamic_expression("") is True
    assert is_dynamic_expression("   ") is True

    # Pure literals
    assert is_dynamic_expression("my-static-bucket-name") is False
    assert is_dynamic_expression("MyLambdaFunction") is False


def test_is_ignorable_arn() -> None:
    assert is_ignorable_arn("arn:aws:s3:::${var.bucket_name}") is True
    assert is_ignorable_arn("arn:aws:s3:::<bucket_name>") is True
    assert is_ignorable_arn("arn:aws:iam::123456789012:role/*") is True
    assert is_ignorable_arn("arn:aws:sqs:us-east-1:123456789012:my-queue") is False


def test_parse_terraform_resources() -> None:
    hcl = """
    resource "aws_s3_bucket" "good_bucket" {
      bucket = "my-valid-bucket-123"
    }

    resource "aws_s3_bucket" "bad_bucket" {
      bucket = "INVALID_BUCKET_NAME"
    }

    resource "aws_lambda_function" "demo_fn" {
      function_name = "my-function"
    }

    resource "aws_iam_role" "my_role" {
      name = "my-role"
      path = "/service-role/"
    }

    # Interpolated expressions should be skipped
    resource "aws_s3_bucket" "dynamic_bucket" {
      bucket = "${var.env}-bucket"
    }
    """
    candidates = parse_terraform(hcl, Path("main.tf"))
    assert len(candidates) == 5

    names = [c.resource_name for c in candidates]
    assert "good_bucket" in names
    assert "bad_bucket" in names
    assert "demo_fn" in names
    assert "my_role" in names

    bad = next(c for c in candidates if c.resource_name == "bad_bucket")
    assert bad.property_name == "bucket"
    assert bad.value == "INVALID_BUCKET_NAME"
    assert bad.service == "s3"
    assert bad.shape == "BucketName"
    assert bad.line == 7


def test_parse_terraform_inline_directives() -> None:
    hcl = """
    resource "aws_s3_bucket" "ignored_bucket" {
      # arv: ignore
      bucket = "INVALID_UPPERCASE"
    }

    resource "aws_s3_bucket" "inline_ignored" {
      bucket = "ANOTHER_INVALID" # arv: ignore
    }

    # arv: service=s3 shape=BucketName
    custom_bucket_var = "custom-test-bucket"
    """
    candidates = parse_terraform(hcl, Path("main.tf"))
    assert len(candidates) == 1
    assert candidates[0].resource_name == "custom_bucket_var"
    assert candidates[0].value == "custom-test-bucket"
    assert candidates[0].service == "s3"
    assert candidates[0].shape == "BucketName"


def test_parse_terraform_hardcoded_arns() -> None:
    hcl = """
    locals {
      queue_arn = "arn:aws:sqs:us-east-1:123456789012:my-queue"
      bad_arn   = "arn:aws:sqs:bad:arn"
    }
    """
    candidates = parse_terraform(hcl, Path("locals.tf"))
    arns = [c for c in candidates if c.is_arn]
    assert len(arns) == 2
    assert arns[0].value == "arn:aws:sqs:us-east-1:123456789012:my-queue"
    assert arns[1].value == "arn:aws:sqs:bad:arn"


def test_parse_cloudformation_resources() -> None:
    yaml_cfn = """
    AWSTemplateFormatVersion: "2010-09-09"
    Resources:
      MyBucket:
        Type: AWS::S3::Bucket
        Properties:
          BucketName: my-static-bucket

      BadBucket:
        Type: AWS::S3::Bucket
        Properties:
          BucketName: BAD_BUCKET_NAME

      DynamicBucket:
        Type: AWS::S3::Bucket
        Properties:
          BucketName: !Sub "${AWS::StackName}-bucket"

      MyFunction:
        Type: AWS::Lambda::Function
        Properties:
          FunctionName: "ValidFunction"
    """
    candidates = parse_cloudformation(yaml_cfn, Path("template.yaml"))
    assert len(candidates) == 3

    logical_ids = [c.resource_name for c in candidates]
    assert "MyBucket" in logical_ids
    assert "BadBucket" in logical_ids
    assert "MyFunction" in logical_ids

    bad = next(c for c in candidates if c.resource_name == "BadBucket")
    assert bad.value == "BAD_BUCKET_NAME"
    assert bad.service == "s3"
    assert bad.shape == "BucketName"


def test_parse_cloudformation_directives() -> None:
    yaml_cfn = """
    Resources:
      IgnoredBucket:
        Type: AWS::S3::Bucket
        Properties:
          # arv: ignore
          BucketName: INVALID_NAME

      OverrideProp:
        Type: Custom::Resource
        Properties:
          # arv: service=dynamodb shape=TableName
          TableTarget: "valid_table_name"
    """
    candidates = parse_cloudformation(yaml_cfn, Path("template.yaml"))
    assert len(candidates) == 1
    assert candidates[0].value == "valid_table_name"
    assert candidates[0].service == "dynamodb"
    assert candidates[0].shape == "TableName"


def test_parse_env_file() -> None:
    env_content = """
    # Environment variables
    S3_BUCKET="my-production-bucket"
    INVALID_BUCKET_NAME=UPPERCASE_BUCKET
    export DYNAMODB_TABLE=users_table
    UNUSED_SECRET=supersecret123
    MY_QUEUE_ARN=arn:aws:sqs:us-east-1:123456789012:orders-queue

    # arv: ignore
    ANOTHER_BUCKET=UPPERCASE_IGNORED

    # arv: service=lambda shape=FunctionName
    CUSTOM_WORKER=my-worker-fn
    """
    candidates = parse_env_file(env_content, Path(".env"))
    assert len(candidates) == 5

    names = [c.property_name for c in candidates]
    assert "S3_BUCKET" in names
    assert "INVALID_BUCKET_NAME" in names
    assert "DYNAMODB_TABLE" in names
    assert "MY_QUEUE_ARN" in names
    assert "CUSTOM_WORKER" in names
    assert "ANOTHER_BUCKET" not in names


def test_parse_candidates_dispatch() -> None:
    tf_cands = parse_candidates('resource "aws_s3_bucket" "b" { bucket = "val" }', Path("a.tf"))
    assert len(tf_cands) == 1

    cfn_text = "Resources:\n  B:\n    Type: AWS::S3::Bucket\n    Properties:\n      BucketName: v"
    cfn_cands = parse_candidates(cfn_text, Path("a.yaml"))
    assert len(cfn_cands) == 1

    env_cands = parse_candidates("S3_BUCKET=val", Path(".env"))
    assert len(env_cands) == 1

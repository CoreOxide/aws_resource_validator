"""Mapping definitions for IaC resources and helper functions for directive/expression parsing."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Final

# Resource mappings for Terraform resources
TERRAFORM_RESOURCE_MAP: Final[Mapping[str, Mapping[str, tuple[str, str]]]] = {
    "aws_s3_bucket": {
        "bucket": ("s3", "BucketName"),
        "bucket_prefix": ("s3", "BucketPrefix"),
    },
    "aws_s3_bucket_policy": {
        "bucket": ("s3", "BucketName"),
    },
    "aws_lambda_function": {
        "function_name": ("Lambda", "FunctionName"),
    },
    "aws_iam_role": {
        "name": ("Iam", "roleNameType"),
        "path": ("Iam", "pathType"),
        "name_prefix": ("Iam", "roleNameType"),
    },
    "aws_iam_policy": {
        "name": ("Iam", "policyNameType"),
        "path": ("Iam", "pathType"),
        "name_prefix": ("Iam", "policyNameType"),
    },
    "aws_iam_user": {
        "name": ("Iam", "userNameType"),
        "path": ("Iam", "pathType"),
        "name_prefix": ("Iam", "userNameType"),
    },
    "aws_iam_group": {
        "name": ("Iam", "groupNameType"),
        "path": ("Iam", "pathType"),
        "name_prefix": ("Iam", "groupNameType"),
    },
    "aws_iam_instance_profile": {
        "name": ("Iam", "instanceProfileNameType"),
        "path": ("Iam", "pathType"),
        "name_prefix": ("Iam", "instanceProfileNameType"),
    },
    "aws_dynamodb_table": {
        "name": ("dynamodb", "TableName"),
    },
    "aws_sqs_queue": {
        "name": ("sqs", "QueueName"),
        "name_prefix": ("sqs", "QueueName"),
    },
    "aws_sns_topic": {
        "name": ("sns", "TopicName"),
        "name_prefix": ("sns", "TopicName"),
    },
    "aws_kinesis_stream": {
        "name": ("Kinesis", "StreamName"),
    },
    "aws_cloudwatch_log_group": {
        "name": ("Logs", "LogGroupName"),
    },
    "aws_ecr_repository": {
        "name": ("Ecr", "RepositoryName"),
    },
    "aws_eks_cluster": {
        "name": ("Eks", "ClusterName"),
    },
    "aws_cloudwatch_event_rule": {
        "name": ("Events", "RuleName"),
    },
    "aws_kms_alias": {
        "name": ("Kms", "AliasNameType"),
    },
    "aws_ssm_parameter": {
        "name": ("Ssm", "PSParameterName"),
    },
    "aws_secretsmanager_secret": {
        "name": ("Secretsmanager", "SecretName"),
    },
    "aws_db_instance": {
        "identifier": ("rds", "DBInstanceIdentifier"),
        "identifier_prefix": ("rds", "DBInstanceIdentifier"),
    },
    "aws_rds_cluster": {
        "cluster_identifier": ("rds", "DBClusterIdentifier"),
        "cluster_identifier_prefix": ("rds", "DBClusterIdentifier"),
    },
    "aws_sfn_state_machine": {
        "name": ("Stepfunctions", "CharacterRestrictedName"),
    },
    "aws_stepfunctions_state_machine": {
        "name": ("Stepfunctions", "CharacterRestrictedName"),
    },
}

# Resource mappings for CloudFormation / SAM resources
CLOUDFORMATION_RESOURCE_MAP: Final[Mapping[str, Mapping[str, tuple[str, str]]]] = {
    "AWS::S3::Bucket": {
        "BucketName": ("s3", "BucketName"),
    },
    "AWS::Lambda::Function": {
        "FunctionName": ("Lambda", "FunctionName"),
    },
    "AWS::IAM::Role": {
        "RoleName": ("Iam", "roleNameType"),
        "Path": ("Iam", "pathType"),
    },
    "AWS::IAM::ManagedPolicy": {
        "ManagedPolicyName": ("Iam", "policyNameType"),
        "Path": ("Iam", "pathType"),
    },
    "AWS::IAM::User": {
        "UserName": ("Iam", "userNameType"),
        "Path": ("Iam", "pathType"),
    },
    "AWS::IAM::Group": {
        "GroupName": ("Iam", "groupNameType"),
        "Path": ("Iam", "pathType"),
    },
    "AWS::IAM::InstanceProfile": {
        "InstanceProfileName": ("Iam", "instanceProfileNameType"),
        "Path": ("Iam", "pathType"),
    },
    "AWS::DynamoDB::Table": {
        "TableName": ("dynamodb", "TableName"),
    },
    "AWS::SQS::Queue": {
        "QueueName": ("sqs", "QueueName"),
    },
    "AWS::SNS::Topic": {
        "TopicName": ("sns", "TopicName"),
    },
    "AWS::Kinesis::Stream": {
        "Name": ("Kinesis", "StreamName"),
    },
    "AWS::Logs::LogGroup": {
        "LogGroupName": ("Logs", "LogGroupName"),
    },
    "AWS::ECR::Repository": {
        "RepositoryName": ("Ecr", "RepositoryName"),
    },
    "AWS::EKS::Cluster": {
        "Name": ("Eks", "ClusterName"),
    },
    "AWS::Events::Rule": {
        "Name": ("Events", "RuleName"),
    },
    "AWS::KMS::Alias": {
        "AliasName": ("Kms", "AliasNameType"),
    },
    "AWS::SSM::Parameter": {
        "Name": ("Ssm", "PSParameterName"),
    },
    "AWS::SecretsManager::Secret": {
        "Name": ("Secretsmanager", "SecretName"),
    },
    "AWS::RDS::DBInstance": {
        "DBInstanceIdentifier": ("rds", "DBInstanceIdentifier"),
    },
    "AWS::RDS::DBCluster": {
        "DBClusterIdentifier": ("rds", "DBClusterIdentifier"),
    },
    "AWS::StepFunctions::StateMachine": {
        "StateMachineName": ("Stepfunctions", "CharacterRestrictedName"),
    },
}

# Environment variable mappings
ENV_VAR_EXACT_MAP: Final[Mapping[str, tuple[str, str]]] = {
    "S3_BUCKET": ("s3", "BucketName"),
    "AWS_S3_BUCKET": ("s3", "BucketName"),
    "BUCKET_NAME": ("s3", "BucketName"),
    "S3_BUCKET_NAME": ("s3", "BucketName"),
    "LAMBDA_FUNCTION_NAME": ("Lambda", "FunctionName"),
    "FUNCTION_NAME": ("Lambda", "FunctionName"),
    "DYNAMODB_TABLE": ("dynamodb", "TableName"),
    "DYNAMODB_TABLE_NAME": ("dynamodb", "TableName"),
    "TABLE_NAME": ("dynamodb", "TableName"),
    "SQS_QUEUE_NAME": ("sqs", "QueueName"),
    "QUEUE_NAME": ("sqs", "QueueName"),
    "SNS_TOPIC_NAME": ("sns", "TopicName"),
    "TOPIC_NAME": ("sns", "TopicName"),
    "ECR_REPOSITORY": ("Ecr", "RepositoryName"),
    "ECR_REPOSITORY_NAME": ("Ecr", "RepositoryName"),
    "LOG_GROUP_NAME": ("Logs", "LogGroupName"),
}

ENV_VAR_SUFFIX_MAP: Final[tuple[tuple[str, tuple[str, str]], ...]] = (
    ("_BUCKET_NAME", ("s3", "BucketName")),
    ("_BUCKET", ("s3", "BucketName")),
    ("_TABLE_NAME", ("dynamodb", "TableName")),
    ("_TABLE", ("dynamodb", "TableName")),
    ("_QUEUE_NAME", ("sqs", "QueueName")),
    ("_QUEUE", ("sqs", "QueueName")),
    ("_TOPIC_NAME", ("sns", "TopicName")),
    ("_TOPIC", ("sns", "TopicName")),
    ("_FUNCTION_NAME", ("Lambda", "FunctionName")),
)

_INTERPOLATION_PATTERN = re.compile(
    r"(\$\{.*?\})|(%\{.*?\})|(\{\{.*?\}\})|(^!\w+)|(Fn::\w+)|(\bvar\.\w+)|(\blocal\.\w+)|(\bmodule\.\w+)"
)
_ARV_DIRECTIVE_PATTERN = re.compile(
    r"(?:#|//)\s*arv(?:-lint)?:\s*(?:(ignore)|service=([a-zA-Z0-9_-]+)\s+shape=([a-zA-Z0-9_]+))"
)


def is_dynamic_expression(value: str) -> bool:
    """Return True if value represents an IaC variable, function call, or interpolation."""
    v = value.strip()
    if not v:
        return True
    if _INTERPOLATION_PATTERN.search(v):
        return True
    # Reference expressions without quotes in Terraform: var.foo, local.bar, aws_s3_bucket.x.id
    if any(v.startswith(prefix) for prefix in ("var.", "local.", "module.", "data.", "aws_", "each.", "count.")):
        return True
    # CloudFormation intrinsic tags
    intrinsic_tags = ("!Ref", "!Sub", "!GetAtt", "!Join", "!Select", "!FindInMap", "!ImportValue")
    return any(v.startswith(tag) for tag in intrinsic_tags)


def is_ignorable_arn(value: str) -> bool:
    """Return True if an ARN contains unresolved template parameters or wildcard tokens."""
    if is_dynamic_expression(value):
        return True
    # Template tokens like arn:aws:s3:::<bucket_name> or arn:aws:iam::123456789012:role/*
    return "<" in value or ">" in value or "*" in value or "?" in value


def parse_inline_directive(line: str) -> tuple[bool, tuple[str, str] | None]:
    """Parse an inline comment directive.

    Returns:
        (is_ignore, (service, shape) | None)
    """
    m = _ARV_DIRECTIVE_PATTERN.search(line)
    if not m:
        return False, None
    if m.group(1):  # "ignore"
        return True, None
    svc = m.group(2)
    shape = m.group(3)
    if svc and shape:
        return False, (svc, shape)
    return False, None

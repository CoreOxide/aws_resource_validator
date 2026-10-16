"""Unit tests for the scanner engine, report serialization, SARIF, and GitHub annotations."""

from __future__ import annotations

from pathlib import Path

from aws_resource_validator.scanner.engine import scan_file, scan_paths, scan_text


def test_scan_text_valid_and_invalid_terraform() -> None:
    tf_content = """
    resource "aws_s3_bucket" "b1" {
      bucket = "my-valid-bucket-name"
    }

    resource "aws_s3_bucket" "b2" {
      bucket = "INVALID_UPPERCASE"
    }

    resource "aws_s3_bucket" "b3" {
      bucket = "double..dots"
    }
    """
    count, findings = scan_text(tf_content, Path("main.tf"))
    assert count == 3
    assert len(findings) == 2

    # b2 finding: uppercase failure
    f_b2 = next(f for f in findings if f.candidate.resource_name == "b2")
    assert not f_b2.is_valid
    assert any("uppercase" in e.lower() or "regex" in e.lower() for e in f_b2.errors)
    assert f_b2.visual_pointer is not None
    assert f_b2.suggested_fix is not None

    # b3 finding: extra S3 check failure (consecutive dots)
    f_b3 = next(f for f in findings if f.candidate.resource_name == "b3")
    assert not f_b3.is_valid
    assert any("consecutive periods" in e for e in f_b3.errors)


def test_scan_text_arn_validation() -> None:
    content = """
    locals {
      valid_arn = "arn:aws:sqs:us-east-1:123456789012:my-queue"
      bad_arn   = "arn:aws:sqs:12345"
    }
    """
    count, findings = scan_text(content, Path("locals.tf"))
    assert count == 2
    assert len(findings) == 1
    bad = findings[0]
    assert bad.candidate.value == "arn:aws:sqs:12345"
    assert not bad.is_valid
    assert len(bad.errors) > 0


def test_scan_file_and_scan_paths(tmp_path: Path) -> None:
    tf_file = tmp_path / "infra.tf"
    tf_file.write_text(
        """
        resource "aws_dynamodb_table" "t1" {
          name = "valid_table_name"
        }
        resource "aws_dynamodb_table" "t2" {
          name = "ab" # Too short, DynamoDB requires >= 3 chars
        }
        """,
        encoding="utf-8",
    )

    env_file = tmp_path / ".env"
    env_file.write_text(
        """
        S3_BUCKET=good-bucket
        LAMBDA_FUNCTION_NAME=Bad!Function
        """,
        encoding="utf-8",
    )

    ignored_dir = tmp_path / "node_modules"
    ignored_dir.mkdir()
    (ignored_dir / "bad.tf").write_text('resource "aws_s3_bucket" "x" { bucket = "BAD" }', encoding="utf-8")

    report = scan_paths([tmp_path])
    assert report.files_scanned == 2  # node_modules skipped
    assert report.candidates_checked == 4
    assert not report.is_valid
    assert report.error_count == 2  # t2 and LAMBDA_FUNCTION_NAME

    # Test single file scan
    cnt, file_findings = scan_file(tf_file)
    assert cnt == 2
    assert len(file_findings) == 1
    assert file_findings[0].candidate.resource_name == "t2"


def test_scan_report_serialization(tmp_path: Path) -> None:
    bad_file = tmp_path / "main.tf"
    bad_file.write_text('resource "aws_s3_bucket" "b" { bucket = "BAD" }', encoding="utf-8")

    report = scan_paths([bad_file])
    assert not report.is_valid

    # JSON dict
    d = report.to_dict()
    assert d["files_scanned"] == 1
    assert d["error_count"] == 1
    assert len(d["findings"]) == 1
    assert d["findings"][0]["shape"] == "BucketName"

    # SARIF
    sarif = report.to_sarif()
    assert sarif["version"] == "2.1.0"
    assert len(sarif["runs"]) == 1
    assert len(sarif["runs"][0]["results"]) == 1
    res = sarif["runs"][0]["results"][0]
    assert res["ruleId"] == "AWS-NAME-S3-BUCKETNAME"
    assert res["level"] == "error"

    # GitHub annotation
    finding = report.findings[0]
    ann = finding.to_github_annotation()
    assert ann.startswith("::error file=")
    assert "col=" in ann
    assert "Validation Violation" in ann


def test_scan_file_nonexistent(tmp_path: Path) -> None:
    non_existent = tmp_path / "does_not_exist.tf"
    count, findings = scan_file(non_existent)
    assert count == 0
    assert len(findings) == 1
    assert not findings[0].is_valid
    assert "Could not read file" in findings[0].errors[0]

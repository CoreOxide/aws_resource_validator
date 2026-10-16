"""Data models for Infrastructure-as-Code and configuration scanning results."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from aws_resource_validator import __version__


@dataclass(frozen=True, slots=True)
class ScanCandidate:
    """A single resource identifier extracted from an IaC or configuration file."""

    file_path: Path
    line: int
    column: int
    raw_line: str
    resource_type: str
    resource_name: str
    property_name: str
    value: str
    service: str
    shape: str
    is_arn: bool = False

    def to_dict(self) -> dict[str, Any]:
        """Serialize candidate to a dictionary."""
        d = asdict(self)
        d["file_path"] = str(self.file_path)
        return d


@dataclass(frozen=True, slots=True)
class ScanFinding:
    """The validation outcome for a single ScanCandidate."""

    candidate: ScanCandidate
    is_valid: bool
    errors: tuple[str, ...] = field(default_factory=tuple)
    warnings: tuple[str, ...] = field(default_factory=tuple)
    failure_index: int | None = None
    failure_reason: str | None = None
    suggested_fix: str | None = None
    visual_pointer: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize finding to a dictionary for JSON output."""
        return {
            "file": str(self.candidate.file_path),
            "line": self.candidate.line,
            "column": self.candidate.column,
            "resource_type": self.candidate.resource_type,
            "resource_name": self.candidate.resource_name,
            "property_name": self.candidate.property_name,
            "value": self.candidate.value,
            "service": self.candidate.service,
            "shape": self.candidate.shape,
            "is_arn": self.candidate.is_arn,
            "is_valid": self.is_valid,
            "errors": list(self.errors),
            "warnings": list(self.warnings),
            "failure_index": self.failure_index,
            "failure_reason": self.failure_reason,
            "suggested_fix": self.suggested_fix,
            "visual_pointer": self.visual_pointer,
        }

    def to_github_annotation(self) -> str:
        """Format as a GitHub Actions workflow command for PR annotations."""
        level = "error" if self.errors else "warning"
        msg = "; ".join(self.errors or self.warnings)
        if self.suggested_fix:
            msg += f" Suggested fix: {self.suggested_fix}"
        title = f"{self.candidate.service}.{self.candidate.shape} Validation Violation"
        return (
            f"::{level} file={self.candidate.file_path},line={self.candidate.line},"
            f"col={self.candidate.column},title={title}::{msg}"
        )

    def to_sarif_result(self) -> dict[str, Any]:
        """Format as a SARIF v2.1.0 result item."""
        level = "error" if self.errors else "warning"
        msg_text = "; ".join(self.errors or self.warnings)
        if self.suggested_fix:
            msg_text += f" Suggested fix: {self.suggested_fix}"

        rule_id = f"AWS-NAME-{self.candidate.service.upper()}-{self.candidate.shape.upper()}"
        return {
            "ruleId": rule_id,
            "level": level,
            "message": {"text": msg_text},
            "locations": [
                {
                    "physicalLocation": {
                        "artifactLocation": {"uri": str(self.candidate.file_path).replace("\\", "/")},
                        "region": {
                            "startLine": self.candidate.line,
                            "startColumn": self.candidate.column,
                            "endColumn": self.candidate.column + len(self.candidate.value),
                            "snippet": {"text": self.candidate.raw_line.strip()},
                        },
                    }
                }
            ],
        }


@dataclass(frozen=True, slots=True)
class ScanReport:
    """Aggregated scan outcome across files."""

    files_scanned: int
    candidates_checked: int
    findings: tuple[ScanFinding, ...] = field(default_factory=tuple)

    @property
    def is_valid(self) -> bool:
        """True if there are no errors in any finding."""
        return not any(f.errors for f in self.findings)

    @property
    def error_count(self) -> int:
        """Total number of errors across all findings."""
        return sum(len(f.errors) for f in self.findings)

    @property
    def warning_count(self) -> int:
        """Total number of warnings across all findings."""
        return sum(len(f.warnings) for f in self.findings)

    def to_dict(self) -> dict[str, Any]:
        """Serialize report to a dictionary for JSON output."""
        return {
            "files_scanned": self.files_scanned,
            "candidates_checked": self.candidates_checked,
            "is_valid": self.is_valid,
            "error_count": self.error_count,
            "warning_count": self.warning_count,
            "findings": [f.to_dict() for f in self.findings],
        }

    def to_sarif(self) -> dict[str, Any]:
        """Serialize report to a complete SARIF v2.1.0 log object."""
        return {
            "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
            "version": "2.1.0",
            "runs": [
                {
                    "tool": {
                        "driver": {
                            "name": "aws-resource-validator",
                            "semanticVersion": __version__,
                            "informationUri": "https://github.com/CoreOxide/aws_resource_validator",
                            "rules": [
                                {
                                    "id": f.to_sarif_result()["ruleId"],
                                    "shortDescription": {
                                        "text": f"AWS naming violation in {f.candidate.service}.{f.candidate.shape}"
                                    },
                                }
                                for f in self.findings
                            ],
                        }
                    },
                    "results": [f.to_sarif_result() for f in self.findings],
                }
            ],
        }

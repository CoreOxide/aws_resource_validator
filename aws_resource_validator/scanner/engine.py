"""Scanning execution engine for evaluating IaC files against AWS resource constraints."""

from __future__ import annotations

import fnmatch
from collections.abc import Sequence
from pathlib import Path

from aws_resource_validator.core.arn import ARN, ARNParseError
from aws_resource_validator.core.builtin_rules import get_extra_validator
from aws_resource_validator.core.diagnostics import diagnose_validation
from aws_resource_validator.core.resolver import resolve_service, resolve_shape
from aws_resource_validator.scanner.models import ScanCandidate, ScanFinding, ScanReport
from aws_resource_validator.scanner.parsers import parse_candidates

_DEFAULT_EXCLUDES = frozenset(
    {
        ".git",
        ".venv",
        "venv",
        "node_modules",
        ".terraform",
        "__pycache__",
        ".tox",
        "dist",
        "build",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
    }
)

_SUPPORTED_EXTENSIONS = frozenset(
    {
        ".tf",
        ".tfvars",
        ".yaml",
        ".yml",
        ".json",
        ".template",
        ".env",
    }
)


def _should_scan_file(path: Path, exclude_patterns: Sequence[str]) -> bool:
    """Return True if the file matches supported IaC extensions and is not excluded."""
    name = path.name.lower()
    for part in path.parts:
        if part in _DEFAULT_EXCLUDES:
            return False

    str_path = str(path).replace("\\", "/")
    for pattern in exclude_patterns:
        if fnmatch.fnmatch(str_path, pattern) or fnmatch.fnmatch(name, pattern):
            return False

    if name.startswith(".env") or name.endswith(".env"):
        return True

    return path.suffix.lower() in _SUPPORTED_EXTENSIONS


def validate_candidate(candidate: ScanCandidate, *, strict: bool = True) -> ScanFinding:
    """Validate a single candidate against AWS rules or ARN grammar."""
    if candidate.is_arn:
        try:
            arn = ARN.parse(candidate.value)
            arn_errors = list(arn.errors)
            arn_warnings = list(arn.warnings)
            is_valid = arn.is_valid
            visual_pointer = None
            suggested_fix = None
            if not is_valid:
                first_err = arn_errors[0] if arn_errors else "malformed ARN"
                suggested_fix = "Ensure the value follows format 'arn:partition:service:region:account-id:resource'."
                visual_pointer = f"{candidate.value}\n^ character 0: {first_err}"

            return ScanFinding(
                candidate=candidate,
                is_valid=is_valid,
                errors=tuple(arn_errors),
                warnings=tuple(arn_warnings),
                failure_index=0 if not is_valid else None,
                failure_reason=arn_errors[0] if arn_errors else None,
                suggested_fix=suggested_fix,
                visual_pointer=visual_pointer,
            )
        except ARNParseError as exc:
            return ScanFinding(
                candidate=candidate,
                is_valid=False,
                errors=(str(exc),),
                warnings=(),
                failure_index=0,
                failure_reason=str(exc),
                suggested_fix="Ensure value begins with 'arn:' followed by 5 colon-delimited components.",
                visual_pointer=f"{candidate.value}\n^ character 0: {exc}",
            )

    svc, _ = resolve_service(candidate.service)
    if svc is None:
        return ScanFinding(
            candidate=candidate,
            is_valid=True,
            warnings=(f"Unknown AWS service '{candidate.service}'; validation skipped.",),
        )

    obj, _ = resolve_shape(svc, candidate.shape)
    if obj is None:
        return ScanFinding(
            candidate=candidate,
            is_valid=True,
            warnings=(f"Unknown shape '{candidate.shape}' in service '{svc.service_name}'; validation skipped.",),
        )

    result = diagnose_validation(obj, svc.service_name, candidate.value, strict=strict)
    shape_errors = list(result.errors)
    shape_warnings = list(result.warnings)

    # Check supplemental domain validators (e.g. S3 consecutive periods or IP format)
    extra_validator = get_extra_validator(svc.service_name, obj.name)
    if extra_validator is not None:
        extra_errs = extra_validator(candidate.value)
        if extra_errs:
            shape_errors.extend(extra_errs)

    is_valid = len(shape_errors) == 0

    return ScanFinding(
        candidate=candidate,
        is_valid=is_valid,
        errors=tuple(shape_errors),
        warnings=tuple(shape_warnings),
        failure_index=result.failure_index,
        failure_reason=result.failure_reason,
        suggested_fix=result.suggested_fix,
        visual_pointer=result.visual_pointer,
    )


def scan_text(
    content: str,
    file_path: Path | str,
    *,
    strict: bool = True,
) -> tuple[int, list[ScanFinding]]:
    """Scan raw text content and return (candidates_count, findings)."""
    p = Path(file_path)
    candidates = parse_candidates(content, p)
    findings: list[ScanFinding] = []

    for cand in candidates:
        finding = validate_candidate(cand, strict=strict)
        if not finding.is_valid or finding.warnings:
            findings.append(finding)

    return len(candidates), findings


def scan_file(
    file_path: Path | str,
    *,
    strict: bool = True,
) -> tuple[int, list[ScanFinding]]:
    """Scan a single file on disk and return (candidates_count, findings)."""
    p = Path(file_path).resolve()
    try:
        content = p.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        cand = ScanCandidate(
            file_path=p,
            line=1,
            column=1,
            raw_line="",
            resource_type="file",
            resource_name=p.name,
            property_name="",
            value="",
            service="",
            shape="",
        )
        return 0, [
            ScanFinding(
                candidate=cand,
                is_valid=False,
                errors=(f"Could not read file: {exc}",),
            )
        ]

    return scan_text(content, p, strict=strict)


def scan_paths(
    paths: Sequence[Path | str],
    *,
    strict: bool = True,
    exclude: Sequence[str] = (),
) -> ScanReport:
    """Recursively scan files and directories, returning an aggregated ScanReport."""
    target_paths = [Path.cwd()] if not paths else [Path(p) for p in paths]

    files_to_scan: list[Path] = []
    for p in target_paths:
        resolved = p.resolve()
        if resolved.is_file():
            if _should_scan_file(resolved, exclude):
                files_to_scan.append(resolved)
        elif resolved.is_dir():
            for item in resolved.rglob("*"):
                if item.is_file() and _should_scan_file(item, exclude):
                    files_to_scan.append(item)

    # Sort files deterministically
    files_to_scan.sort()

    total_candidates = 0
    all_findings: list[ScanFinding] = []

    for file_path in files_to_scan:
        count, findings = scan_file(file_path, strict=strict)
        total_candidates += count
        all_findings.extend(findings)

    return ScanReport(
        files_scanned=len(files_to_scan),
        candidates_checked=total_candidates,
        findings=tuple(all_findings),
    )

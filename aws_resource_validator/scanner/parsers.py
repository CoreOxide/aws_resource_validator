"""Line-and-column-preserving parsers for Terraform, CloudFormation, and environment files."""

from __future__ import annotations

import re
from pathlib import Path

from aws_resource_validator.scanner.models import ScanCandidate
from aws_resource_validator.scanner.rules_map import (
    CLOUDFORMATION_RESOURCE_MAP,
    ENV_VAR_EXACT_MAP,
    ENV_VAR_SUFFIX_MAP,
    TERRAFORM_RESOURCE_MAP,
    is_dynamic_expression,
    is_ignorable_arn,
    parse_inline_directive,
)

_TF_RESOURCE_BLOCK_RE = re.compile(r'^\s*resource\s+"([^"]+)"\s+"([^"]+)"\s*\{')
_TF_PROPERTY_RE = re.compile(r'(?:^|[\{\s;])\s*([a-zA-Z0-9_-]+)\s*=\s*(["\'])(.*?)\2')
_ARN_LITERAL_RE = re.compile(r'(["\'])(arn:[a-zA-Z0-9_.:/-]+)\1')
_ENV_LINE_RE = re.compile(r'^\s*(?:export\s+)?([a-zA-Z0-9_]+)\s*=\s*(?:(["\'])(.*?)\2|([^#\s\r\n]+))')
_CFN_TYPE_RE = re.compile(r'^\s*Type\s*:\s*(["\']?)([a-zA-Z0-9_:]+)\1')
_CFN_PROP_RE = re.compile(r'^\s*([a-zA-Z0-9_]+)\s*:\s*(["\']?)(.*?)\2\s*(?:#.*)?$')


def _resolve_directives(
    line: str, preceding: tuple[bool, tuple[str, str] | None] | None
) -> tuple[bool, tuple[str, str] | None, tuple[bool, tuple[str, str] | None] | None]:
    """Resolve inline and preceding comment directives for a line."""
    inline_ignore, inline_override = parse_inline_directive(line)
    active_ignore = inline_ignore or (preceding[0] if preceding else False)
    active_override = inline_override or (preceding[1] if preceding else None)

    stripped = line.strip()
    if stripped.startswith(("#", "//")):
        next_preceding = (inline_ignore, inline_override) if (inline_ignore or inline_override) else None
    else:
        next_preceding = None

    return active_ignore, active_override, next_preceding


def _scan_arn_literals(
    line: str,
    line_idx: int,
    file_path: Path,
    resource_type: str,
    resource_name: str,
) -> list[ScanCandidate]:
    """Extract hardcoded ARN literals from a line."""
    arns: list[ScanCandidate] = []
    for m in _ARN_LITERAL_RE.finditer(line):
        arn_val = m.group(2)
        if not is_ignorable_arn(arn_val):
            col = m.start(2) + 1
            arns.append(
                ScanCandidate(
                    file_path=file_path,
                    line=line_idx,
                    column=col,
                    raw_line=line,
                    resource_type=resource_type or "resource",
                    resource_name=resource_name or "arn",
                    property_name="arn",
                    value=arn_val,
                    service="arn",
                    shape="ARN",
                    is_arn=True,
                )
            )
    return arns


def _extract_tf_property(
    line: str,
    line_idx: int,
    file_path: Path,
    current_type: str,
    current_name: str,
    override: tuple[str, str] | None,
) -> ScanCandidate | None:
    """Extract property assignment from a Terraform line if matched by rules."""
    prop_match = _TF_PROPERTY_RE.search(line)
    if not prop_match:
        return None
    prop_name = prop_match.group(1)
    val = prop_match.group(3)
    if is_dynamic_expression(val):
        return None

    svc, shape = override if override else (None, None)
    if not svc and current_type in TERRAFORM_RESOURCE_MAP:
        mapping = TERRAFORM_RESOURCE_MAP[current_type]
        if prop_name in mapping:
            svc, shape = mapping[prop_name]

    if not (svc and shape):
        return None

    col = prop_match.start(3) + 1

    return ScanCandidate(
        file_path=file_path,
        line=line_idx,
        column=col,
        raw_line=line,
        resource_type=current_type or "terraform_variable",
        resource_name=current_name or prop_name,
        property_name=prop_name,
        value=val,
        service=svc,
        shape=shape,
        is_arn=False,
    )


def _extract_cfn_property(
    line: str,
    line_idx: int,
    file_path: Path,
    current_type: str,
    current_logical_id: str,
    override: tuple[str, str] | None,
) -> ScanCandidate | None:
    """Extract CloudFormation property assignment if matching rules."""
    prop_match = _CFN_PROP_RE.match(line)
    if not prop_match:
        return None
    prop_name = prop_match.group(1)
    val = prop_match.group(3).strip()
    if is_dynamic_expression(val):
        return None

    svc, shape = override if override else (None, None)
    if not svc and current_type in CLOUDFORMATION_RESOURCE_MAP:
        mapping = CLOUDFORMATION_RESOURCE_MAP[current_type]
        if prop_name in mapping:
            svc, shape = mapping[prop_name]

    if not (svc and shape):
        return None

    col = prop_match.start(3) + 1

    return ScanCandidate(
        file_path=file_path,
        line=line_idx,
        column=col,
        raw_line=line,
        resource_type=current_type,
        resource_name=current_logical_id,
        property_name=prop_name,
        value=val,
        service=svc,
        shape=shape,
        is_arn=False,
    )


def _extract_env_property(
    line: str,
    line_idx: int,
    file_path: Path,
    override: tuple[str, str] | None,
) -> ScanCandidate | None:
    """Extract environment variable assignment if matching rules or ARN."""
    m = _ENV_LINE_RE.match(line)
    if not m:
        return None
    key = m.group(1)
    raw_val = m.group(3) if m.group(3) is not None else m.group(4)
    if raw_val is None or not raw_val.strip():
        return None
    val = raw_val.strip()
    if is_dynamic_expression(val):
        return None

    val_start = line.find(val)
    col = val_start + 1 if val_start != -1 else 1

    if val.startswith("arn:") and not is_ignorable_arn(val):
        return ScanCandidate(
            file_path=file_path,
            line=line_idx,
            column=col,
            raw_line=line,
            resource_type="env",
            resource_name=key,
            property_name=key,
            value=val,
            service="arn",
            shape="ARN",
            is_arn=True,
        )

    svc, shape = override if override else (None, None)
    if not svc:
        if key in ENV_VAR_EXACT_MAP:
            svc, shape = ENV_VAR_EXACT_MAP[key]
        else:
            for suffix, mapping in ENV_VAR_SUFFIX_MAP:
                if key.endswith(suffix):
                    svc, shape = mapping
                    break

    if not (svc and shape):
        return None

    return ScanCandidate(
        file_path=file_path,
        line=line_idx,
        column=col,
        raw_line=line,
        resource_type="env",
        resource_name=key,
        property_name=key,
        value=val,
        service=svc,
        shape=shape,
        is_arn=False,
    )


def parse_terraform(content: str, file_path: Path) -> list[ScanCandidate]:
    """Extract candidate AWS resource names and ARNs from Terraform files (.tf, .tfvars)."""
    candidates: list[ScanCandidate] = []
    current_resource_type = ""
    current_resource_name = ""
    brace_depth = 0
    resource_block_depth = 0
    preceding_directive: tuple[bool, tuple[str, str] | None] | None = None

    for line_idx, line in enumerate(content.splitlines(), start=1):
        stripped = line.strip()
        active_ignore, active_override, preceding_directive = _resolve_directives(line, preceding_directive)

        if stripped.startswith(("#", "//")):
            continue

        if active_ignore:
            brace_depth += line.count("{") - line.count("}")
            if brace_depth < resource_block_depth:
                current_resource_type, current_resource_name, resource_block_depth = "", "", 0
            continue

        res_match = _TF_RESOURCE_BLOCK_RE.search(line)
        if res_match:
            current_resource_type = res_match.group(1)
            current_resource_name = res_match.group(2)
            open_count = line.count("{")
            close_count = line.count("}")
            brace_depth += open_count - close_count
            resource_block_depth = brace_depth

            if "=" in line:
                cand = _extract_tf_property(
                    line, line_idx, file_path, current_resource_type, current_resource_name, active_override
                )
                if cand is not None:
                    candidates.append(cand)

            if close_count >= open_count:
                current_resource_type, current_resource_name, resource_block_depth = "", "", 0
            continue

        cand = _extract_tf_property(
            line, line_idx, file_path, current_resource_type, current_resource_name, active_override
        )
        if cand is not None:
            candidates.append(cand)

        candidates.extend(
            _scan_arn_literals(line, line_idx, file_path, current_resource_type, current_resource_name)
        )

        brace_depth += line.count("{") - line.count("}")
        if brace_depth < resource_block_depth:
            current_resource_type, current_resource_name, resource_block_depth = "", "", 0

    return candidates


def parse_cloudformation(content: str, file_path: Path) -> list[ScanCandidate]:
    """Extract candidate AWS resource names and ARNs from CloudFormation / SAM templates."""
    candidates: list[ScanCandidate] = []
    in_resources = False
    resources_indent = 0
    current_logical_id = ""
    current_type = ""
    in_properties = False
    properties_indent = 0
    preceding_directive: tuple[bool, tuple[str, str] | None] | None = None
    reserved_cfn_keys = ("properties", "metadata", "dependson", "condition", "deletionpolicy", "updatepolicy")

    for line_idx, line in enumerate(content.splitlines(), start=1):
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        active_ignore, active_override, preceding_directive = _resolve_directives(line, preceding_directive)

        if stripped.startswith("#") or active_ignore:
            continue

        if re.match(r"^Resources\s*:", stripped):
            in_resources, resources_indent = True, indent
            current_logical_id, current_type, in_properties = "", "", False
            continue

        if in_resources:
            if indent <= resources_indent and stripped:
                in_resources, current_logical_id, current_type, in_properties = False, "", "", False
                continue

            if re.match(r"^\s*Properties\s*:", line):
                in_properties, properties_indent = True, indent
                continue

            if in_properties and indent <= properties_indent and stripped:
                in_properties = False

            clean_token = stripped.rstrip(":").strip().lower()
            if (
                indent > resources_indent
                and re.match(r"^[a-zA-Z0-9_]+\s*:\s*$", stripped)
                and clean_token not in reserved_cfn_keys
            ):
                current_logical_id = stripped.rstrip(":").strip()
                current_type, in_properties = "", False
                continue

            type_match = _CFN_TYPE_RE.match(line)
            if type_match and current_logical_id:
                current_type = type_match.group(2)
                continue

            if in_properties and current_type:
                cand = _extract_cfn_property(
                    line, line_idx, file_path, current_type, current_logical_id, active_override
                )
                if cand is not None:
                    candidates.append(cand)

        candidates.extend(_scan_arn_literals(line, line_idx, file_path, current_type, current_logical_id))

    return candidates


def parse_env_file(content: str, file_path: Path) -> list[ScanCandidate]:
    """Extract candidate AWS resource names and ARNs from .env files."""
    candidates: list[ScanCandidate] = []
    preceding_directive: tuple[bool, tuple[str, str] | None] | None = None

    for line_idx, line in enumerate(content.splitlines(), start=1):
        stripped = line.strip()
        active_ignore, active_override, preceding_directive = _resolve_directives(line, preceding_directive)

        if stripped.startswith("#") or active_ignore or not stripped:
            continue

        cand = _extract_env_property(line, line_idx, file_path, active_override)
        if cand is not None:
            candidates.append(cand)

    return candidates


def parse_candidates(content: str, file_path: Path) -> list[ScanCandidate]:
    """Dispatch to appropriate parser based on file extension and naming."""
    name = file_path.name.lower()
    if name.endswith((".tf", ".tfvars")):
        return parse_terraform(content, file_path)
    if name.endswith((".yaml", ".yml", ".json", ".template")):
        return parse_cloudformation(content, file_path)
    if name.startswith(".env") or name.endswith(".env"):
        return parse_env_file(content, file_path)
    return parse_terraform(content, file_path)

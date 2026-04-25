"""Per-service orchestration: stub in, ``ServiceModelIR`` out, files on disk."""

from __future__ import annotations

import ast
from collections.abc import Iterable
from dataclasses import replace
from pathlib import Path

from aws_resource_validator.generator.common.logging import get_logger
from aws_resource_validator.generator.pipeline_b.ast_reader import read_module
from aws_resource_validator.generator.pipeline_b.literal_extractor import extract_literals
from aws_resource_validator.generator.pipeline_b.model_ir import ClassIR, ServiceModelIR, UnionAliasIR
from aws_resource_validator.generator.pipeline_b.python_emitter import EmittedArtifacts, emit_service
from aws_resource_validator.generator.pipeline_b.service_annotator import MethodRole, extract_method_roles
from aws_resource_validator.generator.pipeline_b.stubs_source import StubPackage
from aws_resource_validator.generator.pipeline_b.type_map import build_type_map
from aws_resource_validator.generator.pipeline_b.type_resolver import TypeResolver
from aws_resource_validator.generator.pipeline_b.typeddict_extractor import extract_items

_logger = get_logger(__name__)


def build_service_ir(stub: StubPackage) -> ServiceModelIR:
    """Run every extractor on ``stub`` and return a fully-populated IR."""
    resolver = TypeResolver(context=stub.service)
    type_defs_tree = read_module(stub.type_defs_file)
    literals_tree = _read_optional(stub.literals_file)
    client_tree = _read_optional(stub.client_file)

    type_map = build_type_map(type_defs_tree)
    items = extract_items(type_defs_tree, type_map, resolver)
    literals = extract_literals(literals_tree) if literals_tree is not None else ()
    roles = extract_method_roles(client_tree) if client_tree is not None else {}

    annotated: tuple[ClassIR | UnionAliasIR, ...] = tuple(
        _annotate(item, roles) if isinstance(item, ClassIR) else item for item in items
    )
    return ServiceModelIR(
        service=stub.service,
        items=annotated,
        literals=literals,
    )


def _read_optional(path: Path) -> ast.Module | None:
    """Return the parsed AST of ``path``, or ``None`` if the file is missing."""
    try:
        return read_module(path)
    except FileNotFoundError:
        return None


def _annotate(cls: ClassIR, roles: dict[str, MethodRole]) -> ClassIR:
    role = roles.get(cls.name)
    if role is None:
        return cls
    return replace(cls, role=role.role, role_fn=role.fn_name)


def emit_all(stubs: Iterable[StubPackage], out_dir: Path) -> list[EmittedArtifacts]:
    """Build IR for every stub and write the output tree to ``out_dir``."""
    artifacts: list[EmittedArtifacts] = []
    for stub in stubs:
        try:
            ir = build_service_ir(stub)
        except FileNotFoundError as err:
            _logger.warning("Skipping %s: %s", stub.service, err)
            continue
        artifacts.append(emit_service(ir, out_dir))
    return artifacts

"""Auto-parametrized tests for every generated Pydantic class.

This file does not itself change shape — it consumes one ``_manifest.json``
per service from ``aws_resource_validator/pydantic_models/<service>/`` and
parametrizes over the ``(service, class_name)`` product. That's roughly
100,000 test cases. Run with ``pytest tests/generated -n auto`` for
parallelism.

The test body verifies that each generated class:

1. imports without raising,
2. is a subclass of :class:`~.BaseValidatorModel` (or :class:`~.EventStream`),
3. generates a JSON schema (unless it contains a ``Callable`` field, which
   Pydantic legitimately cannot represent),
4. validates an empty dict either successfully (all fields optional) or with
   a :class:`~pydantic.ValidationError` (required fields present). Any
   other exception means the generated code is broken.
"""

from __future__ import annotations

import importlib
import json
from pathlib import Path
from typing import Any

import pytest
from pydantic import ValidationError
from pydantic.errors import PydanticInvalidForJsonSchema

import aws_resource_validator
from aws_resource_validator.core.base_validator_model import BaseValidatorModel, EventStream

_PYDANTIC_MODELS_DIR = Path(aws_resource_validator.__file__).parent / "pydantic_models"


def _load_manifests() -> list[tuple[str, str]]:
    """Return a flat list of ``(service, class_name)`` across all manifests.

    Manifests are read at collection time (cheap JSON); the generated module
    is only imported inside each test so a failure in one service's module
    doesn't poison collection for the rest.
    """
    cases: list[tuple[str, str]] = []
    for manifest_path in sorted(_PYDANTIC_MODELS_DIR.glob("*/_manifest.json")):
        with manifest_path.open() as fh:
            manifest = json.load(fh)
        for class_name in manifest["classes"]:
            cases.append((manifest["service"], class_name))
    return cases


def _id(case: tuple[str, str] | str) -> str:
    # pytest calls ``ids`` once per individual value rather than per-tuple,
    # so this receives each element (service name, then class name).
    return str(case)


_CASES = _load_manifests()


@pytest.mark.generated
@pytest.mark.parametrize(("service", "class_name"), _CASES, ids=_id)
def test_generated_class_contract(service: str, class_name: str) -> None:
    module = importlib.import_module(f"aws_resource_validator.pydantic_models.{service}.{service}_classes")
    cls = getattr(module, class_name)

    assert issubclass(cls, BaseValidatorModel) or issubclass(cls, EventStream), (
        f"{service}.{class_name} has unexpected base chain: {cls.__mro__}"
    )

    # EventStream classes aren't Pydantic models — they exist only for type hints.
    if not issubclass(cls, BaseValidatorModel):
        return

    _assert_schema_generates(cls, service, class_name)
    _assert_empty_validate(cls, service, class_name)


def _assert_schema_generates(cls: type[BaseValidatorModel], service: str, class_name: str) -> None:
    """Schema generation must either succeed or fail with the single known exception."""
    try:
        cls.model_json_schema()
    except PydanticInvalidForJsonSchema:
        # Pydantic can't schema-generate Callable fields. The models are still
        # usable at runtime; this is a known, intentional limitation.
        pass
    except Exception as err:
        pytest.fail(f"{service}.{class_name}.model_json_schema() raised {type(err).__name__}: {err}")


def _assert_empty_validate(cls: type[BaseValidatorModel], service: str, class_name: str) -> None:
    """``model_validate({})`` must be binary: success or ValidationError."""
    try:
        cls.model_validate({})
    except ValidationError:
        return
    except Exception as err:
        pytest.fail(f"{service}.{class_name}.model_validate({{}}) raised {type(err).__name__}: {err}")


def test_manifests_discovered() -> None:
    """Collection-time sanity: we should have found hundreds of services."""
    assert len(_CASES) > 10_000, f"Expected 10,000+ generated cases, found {len(_CASES)}"


def test_manifest_integrity(pydantic_models_root: Path) -> None:
    """Every manifest references classes that actually exist in its module."""
    # Spot-check: full import verification happens in the parametrized test above.
    sample_manifest = pydantic_models_root / "acm" / "_manifest.json"
    with sample_manifest.open() as fh:
        manifest: dict[str, Any] = json.load(fh)
    module = importlib.import_module(manifest["module"])
    for class_name in manifest["classes"]:
        assert hasattr(module, class_name), f"Manifest names {class_name} but module doesn't export it."

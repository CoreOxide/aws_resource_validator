"""Pipeline B — the Pydantic model generator.

Walks the ``mypy_boto3_*`` stub packages, turns their ``TypedDict``
definitions into Pydantic v2 ``BaseModel``s, and writes them under
:mod:`aws_resource_validator.pydantic_models`.
"""

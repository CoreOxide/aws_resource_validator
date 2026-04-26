"""Build-time code generators.

Nothing in this package is imported at application runtime. It reads AWS
service definitions from outside sources (GitHub, mypy_boto3 stubs) and emits
the files under :mod:`aws_resource_validator.class_definitions` and
:mod:`aws_resource_validator.pydantic_models`.
"""

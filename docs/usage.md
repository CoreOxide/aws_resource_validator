
# Usage

Here's a simple example demonstrating how to use `aws_resource_validator`:

```python
from aws_resource_validator.class_definitions import Acm, class_registry

# Use type hint so that you can use `api_registry` with full class definitions
acm: Acm = class_registry.Acm

print(acm.Arn.pattern)
print(acm.Arn.type)
print(acm.Arn.validate("example-arn"))
print(acm.Arn.generate())
```

## Opt-in pattern validation on generated Pydantic models

Every string field on a generated Pydantic model that is backed by a
botocore shape with a regex carries an opt-in validator. Default
construction does not run it:

```python
from aws_resource_validator.pydantic_models.acm_pca.acm_pca_classes import (
    CreateCertificateAuthorityAuditReportRequestTypeDef as Req,
)

# No pattern check: "not-an-arn" is accepted.
Req.model_validate(
    {
        "CertificateAuthorityArn": "not-an-arn",
        "S3BucketName": "my-bucket",
        "AuditReportResponseFormat": "JSON",
    }
)
```

Activate it per call by passing `context={"aws_validate_patterns": True}`:

```python
from pydantic import ValidationError

try:
    Req.model_validate(
        {
            "CertificateAuthorityArn": "not-an-arn",
            "S3BucketName": "my-bucket",
            "AuditReportResponseFormat": "JSON",
        },
        context={"aws_validate_patterns": True},
    )
except ValidationError as exc:
    for err in exc.errors():
        print(err["loc"], err["type"])  # -> ('CertificateAuthorityArn',) aws_pattern
```

The check delegates to `APIObject.validate(value)` from the resource
validator, so the regex + length bounds are always consistent with
`class_registry`. Coverage is limited to annotations that are exactly
`str`, `Optional[str]`, `List[str]`, or `Optional[List[str]]`; other
shapes (`Dict[str, T]`, `Union[str, int]`, nested containers) pass
through unchanged. Unknown `(service, shape)` pairs resolve to a
permissive no-op so a stale emitter never breaks a caller.

## Parsing, validating, and building ARNs

`ARN` replaces fragile `arn.split(":")` code. It splits on at most five
colons (so S3 keys, alarm names, and Lambda aliases containing `:` stay
intact), validates each segment, and decomposes the resource:

```python
from aws_resource_validator import ARN, ARNParseError

arn = ARN.parse("arn:aws:s3:::my-bucket/logs/2026:10:09.gz")
arn.resource       # 'my-bucket/logs/2026:10:09.gz'
arn.is_valid       # True

ARN.parse("arn:aws:iam::12345:role/x").errors
# ("Account ID '12345' must be exactly 12 digits (got 5 characters), 'aws', or empty.",)

ARN.build(service="iam", account_id="123456789012", resource_type="role", resource_id="MyRole")
# ARN(partition='aws', service='iam', region='', account_id='123456789012', resource='role/MyRole')
```

- `ARN.parse(value)` raises `ARNParseError` only when `value` cannot be split
  into six ARN segments; segment problems are reported via `errors` /
  `is_valid`. Pass `strict=True` to raise on any error.
- `ARN.build(...)` raises on invalid results unless `strict=False`.
- `arn.validate_against(service, shape)` checks a specific botocore `*Arn`
  shape and returns a `ValidationResult`; `arn.matching_shapes()` lists every
  service-specific botocore shape the ARN satisfies. Both load the class
  registry lazily — plain parsing never does.
- `ARN` can be used directly as a Pydantic v2 field type.
- CLI: `arv arn "<arn>" [--json] [--strict] [--no-shapes]`.

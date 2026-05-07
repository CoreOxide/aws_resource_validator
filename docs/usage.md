
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

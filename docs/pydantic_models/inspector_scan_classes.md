# Inspector Scan Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# ScanSbomRequest

### sbom
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### outputFormat
- **Type**: typing.Optional[typing.Literal['CYCLONE_DX_1_5', 'INSPECTOR']]


# ScanSbomResponse

### sbom
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_scan.inspector_scan_classes.ResponseMetadata'>
- **Required**: Yes



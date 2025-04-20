# Marketplace Reporting Marketplace Reporting Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetBuyerDashboardInput

### dashboardIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### embeddingDomains
- **Type**: typing.List[str]
- **Required**: Yes


# GetBuyerDashboardOutput

### embedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### embeddingDomains
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_reporting.marketplace_reporting_classes.ResponseMetadata'>
- **Required**: Yes


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



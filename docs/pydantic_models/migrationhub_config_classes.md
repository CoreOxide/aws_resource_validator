# Migrationhub Config Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateHomeRegionControlRequest

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.Target'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# CreateHomeRegionControlResult

### HomeRegionControl
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.HomeRegionControl'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteHomeRegionControlRequest

### ControlId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHomeRegionControlsRequest

### ControlId
- **Type**: typing.Optional[str]

### HomeRegion
- **Type**: typing.Optional[str]

### Target
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeHomeRegionControlsResult

### HomeRegionControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhub_config_classes.HomeRegionControl]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetHomeRegionResult

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.ResponseMetadata'>
- **Required**: Yes


# HomeRegionControl

### ControlId
- **Type**: typing.Optional[str]

### HomeRegion
- **Type**: typing.Optional[str]

### Target
- **Type**: <class 'NoneType'>

### RequestedTime
- **Type**: typing.Optional[datetime.datetime]


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


# Target

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


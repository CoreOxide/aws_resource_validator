# Migrationhub Config Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateHomeRegionControlRequestTypeDef

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.TargetTypeDef'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# CreateHomeRegionControlResultTypeDef

### HomeRegionControl
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.HomeRegionControlTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteHomeRegionControlRequestTypeDef

### ControlId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHomeRegionControlsRequestTypeDef

### ControlId
- **Type**: typing.Optional[str]

### HomeRegion
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhub_config_classes.TargetTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeHomeRegionControlsResultTypeDef

### HomeRegionControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhub_config_classes.HomeRegionControlTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetHomeRegionResultTypeDef

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhub_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HomeRegionControlTypeDef

### ControlId
- **Type**: typing.Optional[str]

### HomeRegion
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhub_config_classes.TargetTypeDef]

### RequestedTime
- **Type**: typing.Optional[datetime.datetime]


# ResponseMetadataTypeDef

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


# TargetTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


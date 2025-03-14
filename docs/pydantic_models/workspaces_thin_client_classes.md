# Workspaces Thin Client Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEnvironmentRequestTypeDef

### desktopArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### desktopEndpoint
- **Type**: typing.Optional[str]

### softwareSetUpdateSchedule
- **Type**: typing.Optional[typing.Literal['APPLY_IMMEDIATELY', 'USE_MAINTENANCE_WINDOW']]

### maintenanceWindow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.MaintenanceWindowUnionTypeDef]

### softwareSetUpdateMode
- **Type**: typing.Optional[typing.Literal['USE_DESIRED', 'USE_LATEST']]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### deviceCreationTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEnvironmentResponseTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeviceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetDeviceResponseTypeDef

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.DeviceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentResponseTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSoftwareSetResponseTypeDef

### softwareSet
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.SoftwareSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDevicesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.PaginatorConfigTypeDef]


# ListDevicesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDevicesResponseTypeDef

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.DeviceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.PaginatorConfigTypeDef]


# ListEnvironmentsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsResponseTypeDef

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSoftwareSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.PaginatorConfigTypeDef]


# ListSoftwareSetsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSoftwareSetsResponseTypeDef

### softwareSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.SoftwareSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MaintenanceWindowUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# SoftwareSetSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SoftwareSetTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SoftwareTypeDef

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeviceResponseTypeDef

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.DeviceSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentResponseTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



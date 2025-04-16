# Workspaces Thin Client Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEnvironmentRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.MaintenanceWindowUnion]

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


# CreateEnvironmentResponse

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# Device

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeviceSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Environment

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetDeviceResponse

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.Device'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentResponse

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# GetSoftwareSetResponse

### softwareSet
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.SoftwareSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# ListDevicesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDevicesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.PaginatorConfig]


# ListDevicesResponse

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.DeviceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.PaginatorConfig]


# ListEnvironmentsResponse

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSoftwareSetsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSoftwareSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.PaginatorConfig]


# ListSoftwareSetsResponse

### softwareSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.SoftwareSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# MaintenanceWindowUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# Software

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# SoftwareSet

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SoftwareSetSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeviceResponse

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.DeviceSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentResponse

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes



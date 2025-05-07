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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.MaintenanceWindow, aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.MaintenanceWindowOutput, NoneType]

### softwareSetUpdateMode
- **Type**: typing.Optional[typing.Literal['USE_DESIRED', 'USE_LATEST']]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### deviceCreationTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateEnvironmentResponse

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.EnvironmentSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDeviceRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteEnvironmentRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeregisterDeviceRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### targetDeviceStatus
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'DEREGISTERED']]

### clientToken
- **Type**: typing.Optional[str]


# Device

### id
- **Type**: typing.Optional[str]

### serialNumber
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### model
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'DEREGISTERED', 'DEREGISTERING', 'REGISTERED']]

### currentSoftwareSetId
- **Type**: typing.Optional[str]

### currentSoftwareSetVersion
- **Type**: typing.Optional[str]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### pendingSoftwareSetId
- **Type**: typing.Optional[str]

### pendingSoftwareSetVersion
- **Type**: typing.Optional[str]

### softwareSetUpdateSchedule
- **Type**: typing.Optional[typing.Literal['APPLY_IMMEDIATELY', 'USE_MAINTENANCE_WINDOW']]

### softwareSetComplianceStatus
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'NONE', 'NOT_COMPLIANT']]

### softwareSetUpdateStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'IN_PROGRESS', 'UP_TO_DATE']]

### lastConnectedAt
- **Type**: typing.Optional[datetime.datetime]

### lastPostureAt
- **Type**: typing.Optional[datetime.datetime]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### arn
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeviceSummary

### id
- **Type**: typing.Optional[str]

### serialNumber
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### model
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'DEREGISTERED', 'DEREGISTERING', 'REGISTERED']]

### currentSoftwareSetId
- **Type**: typing.Optional[str]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### pendingSoftwareSetId
- **Type**: typing.Optional[str]

### softwareSetUpdateSchedule
- **Type**: typing.Optional[typing.Literal['APPLY_IMMEDIATELY', 'USE_MAINTENANCE_WINDOW']]

### lastConnectedAt
- **Type**: typing.Optional[datetime.datetime]

### lastPostureAt
- **Type**: typing.Optional[datetime.datetime]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### arn
- **Type**: typing.Optional[str]


# Environment

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### desktopArn
- **Type**: typing.Optional[str]

### desktopEndpoint
- **Type**: typing.Optional[str]

### desktopType
- **Type**: typing.Optional[typing.Literal['appstream', 'workspaces', 'workspaces-web']]

### activationCode
- **Type**: typing.Optional[str]

### registeredDevicesCount
- **Type**: typing.Optional[int]

### softwareSetUpdateSchedule
- **Type**: typing.Optional[typing.Literal['APPLY_IMMEDIATELY', 'USE_MAINTENANCE_WINDOW']]

### maintenanceWindow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.MaintenanceWindowOutput]

### softwareSetUpdateMode
- **Type**: typing.Optional[typing.Literal['USE_DESIRED', 'USE_LATEST']]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### pendingSoftwareSetId
- **Type**: typing.Optional[str]

### pendingSoftwareSetVersion
- **Type**: typing.Optional[str]

### softwareSetComplianceStatus
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'NOT_COMPLIANT', 'NO_REGISTERED_DEVICES']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### arn
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### deviceCreationTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EnvironmentSummary

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### desktopArn
- **Type**: typing.Optional[str]

### desktopEndpoint
- **Type**: typing.Optional[str]

### desktopType
- **Type**: typing.Optional[typing.Literal['appstream', 'workspaces', 'workspaces-web']]

### activationCode
- **Type**: typing.Optional[str]

### softwareSetUpdateSchedule
- **Type**: typing.Optional[typing.Literal['APPLY_IMMEDIATELY', 'USE_MAINTENANCE_WINDOW']]

### maintenanceWindow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.MaintenanceWindowOutput]

### softwareSetUpdateMode
- **Type**: typing.Optional[typing.Literal['USE_DESIRED', 'USE_LATEST']]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### pendingSoftwareSetId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### arn
- **Type**: typing.Optional[str]


# GetDeviceRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceResponse

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.Device'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentResponse

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# GetSoftwareSetRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSoftwareSetResponse

### softwareSet
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.SoftwareSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# ListDevicesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDevicesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.PaginatorConfig]


# ListDevicesResponse

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.DeviceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.PaginatorConfig]


# ListEnvironmentsResponse

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.EnvironmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.PaginatorConfig]


# ListSoftwareSetsResponse

### softwareSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.SoftwareSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# MaintenanceWindow

### type
- **Type**: typing.Literal['CUSTOM', 'SYSTEM']
- **Required**: Yes

### startTimeHour
- **Type**: typing.Optional[int]

### startTimeMinute
- **Type**: typing.Optional[int]

### endTimeHour
- **Type**: typing.Optional[int]

### endTimeMinute
- **Type**: typing.Optional[int]

### daysOfTheWeek
- **Type**: typing.Optional[typing.List[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]]

### applyTimeOf
- **Type**: typing.Optional[typing.Literal['DEVICE', 'UTC']]


# MaintenanceWindowOutput

### type
- **Type**: typing.Literal['CUSTOM', 'SYSTEM']
- **Required**: Yes

### startTimeHour
- **Type**: typing.Optional[int]

### startTimeMinute
- **Type**: typing.Optional[int]

### endTimeHour
- **Type**: typing.Optional[int]

### endTimeMinute
- **Type**: typing.Optional[int]

### daysOfTheWeek
- **Type**: typing.Optional[typing.List[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]]

### applyTimeOf
- **Type**: typing.Optional[typing.Literal['DEVICE', 'UTC']]


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

### id
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### releasedAt
- **Type**: typing.Optional[datetime.datetime]

### supportedUntil
- **Type**: typing.Optional[datetime.datetime]

### validationStatus
- **Type**: typing.Optional[typing.Literal['NOT_VALIDATED', 'VALIDATED']]

### software
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.Software]]

### arn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SoftwareSetSummary

### id
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### releasedAt
- **Type**: typing.Optional[datetime.datetime]

### supportedUntil
- **Type**: typing.Optional[datetime.datetime]

### validationStatus
- **Type**: typing.Optional[typing.Literal['NOT_VALIDATED', 'VALIDATED']]

### arn
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDeviceRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### softwareSetUpdateSchedule
- **Type**: typing.Optional[typing.Literal['APPLY_IMMEDIATELY', 'USE_MAINTENANCE_WINDOW']]


# UpdateDeviceResponse

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.DeviceSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### desktopArn
- **Type**: typing.Optional[str]

### desktopEndpoint
- **Type**: typing.Optional[str]

### softwareSetUpdateSchedule
- **Type**: typing.Optional[typing.Literal['APPLY_IMMEDIATELY', 'USE_MAINTENANCE_WINDOW']]

### maintenanceWindow
- **Type**: typing.Union[aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.MaintenanceWindow, aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.MaintenanceWindowOutput, NoneType]

### softwareSetUpdateMode
- **Type**: typing.Optional[typing.Literal['USE_DESIRED', 'USE_LATEST']]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### deviceCreationTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpdateEnvironmentResponse

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.EnvironmentSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSoftwareSetRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### validationStatus
- **Type**: typing.Literal['NOT_VALIDATED', 'VALIDATED']
- **Required**: Yes



# Workspaces Thin Client Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEnvironmentRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.MaintenanceWindowTypeDef]

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


# DeleteDeviceRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteEnvironmentRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeregisterDeviceRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### targetDeviceStatus
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'DEREGISTERED']]

### clientToken
- **Type**: typing.Optional[str]


# DeviceSummaryTypeDef

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


# DeviceTypeDef

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


# EnvironmentSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.MaintenanceWindowOutputTypeDef]

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


# EnvironmentTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.MaintenanceWindowOutputTypeDef]

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


# GetDeviceRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceResponseTypeDef

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.DeviceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentResponseTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSoftwareSetRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSoftwareSetResponseTypeDef

### softwareSet
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.SoftwareSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDevicesRequestListDevicesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.PaginatorConfigTypeDef]


# ListDevicesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDevicesResponseTypeDef

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.DeviceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentsRequestListEnvironmentsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.PaginatorConfigTypeDef]


# ListEnvironmentsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsResponseTypeDef

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSoftwareSetsRequestListSoftwareSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.PaginatorConfigTypeDef]


# ListSoftwareSetsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSoftwareSetsResponseTypeDef

### softwareSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.SoftwareSetSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# MaintenanceWindowExtraOutputTypeDef

### type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'SYSTEM']]

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


# MaintenanceWindowOutputTypeDef

### type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'SYSTEM']]

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


# MaintenanceWindowTypeDef

### type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'SYSTEM']]

### startTimeHour
- **Type**: typing.Optional[int]

### startTimeMinute
- **Type**: typing.Optional[int]

### endTimeHour
- **Type**: typing.Optional[int]

### endTimeMinute
- **Type**: typing.Optional[int]

### daysOfTheWeek
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]]

### applyTimeOf
- **Type**: typing.Optional[typing.Literal['DEVICE', 'UTC']]


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


# SoftwareSetTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.SoftwareTypeDef]]

### arn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SoftwareTypeDef

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeviceRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### softwareSetUpdateSchedule
- **Type**: typing.Optional[typing.Literal['APPLY_IMMEDIATELY', 'USE_MAINTENANCE_WINDOW']]


# UpdateDeviceResponseTypeDef

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.DeviceSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_thin_client_classes.MaintenanceWindowTypeDef]

### softwareSetUpdateMode
- **Type**: typing.Optional[typing.Literal['USE_DESIRED', 'USE_LATEST']]

### desiredSoftwareSetId
- **Type**: typing.Optional[str]

### deviceCreationTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateEnvironmentResponseTypeDef

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.EnvironmentSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_thin_client_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSoftwareSetRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### validationStatus
- **Type**: typing.Literal['NOT_VALIDATED', 'VALIDATED']
- **Required**: Yes



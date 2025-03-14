# Backup Gateway Classes

# AssociateGatewayToServerInputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateGatewayToServerOutputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BandwidthRateLimitIntervalOutputTypeDef

### DaysOfWeek
- **Type**: typing.List[int]
- **Required**: Yes

### EndHourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### EndMinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### StartHourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### StartMinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### AverageUploadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]


# BandwidthRateLimitIntervalTypeDef

### DaysOfWeek
- **Type**: typing.Sequence[int]
- **Required**: Yes

### EndHourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### EndMinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### StartHourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### StartMinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### AverageUploadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]


# BandwidthRateLimitIntervalUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateGatewayInputTypeDef

### ActivationKey
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayType
- **Type**: typing.Literal['BACKUP_VM']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.TagTypeDef]]


# CreateGatewayOutputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGatewayInputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGatewayOutputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteHypervisorInputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHypervisorOutputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateGatewayFromServerInputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateGatewayFromServerOutputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GatewayDetailsTypeDef

### GatewayArn
- **Type**: typing.Optional[str]

### GatewayDisplayName
- **Type**: typing.Optional[str]

### GatewayType
- **Type**: typing.Optional[typing.Literal['BACKUP_VM']]

### HypervisorId
- **Type**: typing.Optional[str]

### LastSeenTime
- **Type**: typing.Optional[datetime.datetime]

### MaintenanceStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_gateway_classes.MaintenanceStartTimeTypeDef]

### NextUpdateAvailabilityTime
- **Type**: typing.Optional[datetime.datetime]

### VpcEndpoint
- **Type**: typing.Optional[str]


# GatewayTypeDef

### GatewayArn
- **Type**: typing.Optional[str]

### GatewayDisplayName
- **Type**: typing.Optional[str]

### GatewayType
- **Type**: typing.Optional[typing.Literal['BACKUP_VM']]

### HypervisorId
- **Type**: typing.Optional[str]

### LastSeenTime
- **Type**: typing.Optional[datetime.datetime]


# GetBandwidthRateLimitScheduleInputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetBandwidthRateLimitScheduleOutputTypeDef

### BandwidthRateLimitIntervals
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.BandwidthRateLimitIntervalOutputTypeDef]
- **Required**: Yes

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGatewayInputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetGatewayOutputTypeDef

### Gateway
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.GatewayDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHypervisorInputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetHypervisorOutputTypeDef

### Hypervisor
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.HypervisorDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHypervisorPropertyMappingsInputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetHypervisorPropertyMappingsOutputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VmwareToAwsTagMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.VmwareToAwsTagMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVirtualMachineInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetVirtualMachineOutputTypeDef

### VirtualMachine
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.VirtualMachineDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HypervisorDetailsTypeDef

### Host
- **Type**: typing.Optional[str]

### HypervisorArn
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### LastSuccessfulMetadataSyncTime
- **Type**: typing.Optional[datetime.datetime]

### LatestMetadataSyncStatus
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'PARTIALLY_FAILED', 'RUNNING', 'SUCCEEDED']]

### LatestMetadataSyncStatusMessage
- **Type**: typing.Optional[str]

### LogGroupArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ERROR', 'OFFLINE', 'ONLINE', 'PENDING']]


# HypervisorTypeDef

### Host
- **Type**: typing.Optional[str]

### HypervisorArn
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ERROR', 'OFFLINE', 'ONLINE', 'PENDING']]


# ImportHypervisorConfigurationInputTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.TagTypeDef]]

### Username
- **Type**: typing.Optional[str]


# ImportHypervisorConfigurationOutputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGatewaysInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_gateway_classes.PaginatorConfigTypeDef]


# ListGatewaysInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGatewaysOutputTypeDef

### Gateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.GatewayTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHypervisorsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_gateway_classes.PaginatorConfigTypeDef]


# ListHypervisorsInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHypervisorsOutputTypeDef

### Hypervisors
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.HypervisorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVirtualMachinesInputPaginateTypeDef

### HypervisorArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_gateway_classes.PaginatorConfigTypeDef]


# ListVirtualMachinesInputTypeDef

### HypervisorArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVirtualMachinesOutputTypeDef

### VirtualMachines
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.VirtualMachineTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MaintenanceStartTimeTypeDef

### HourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### MinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### DayOfMonth
- **Type**: typing.Optional[int]

### DayOfWeek
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutBandwidthRateLimitScheduleInputTypeDef

### BandwidthRateLimitIntervals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.BandwidthRateLimitIntervalUnionTypeDef]
- **Required**: Yes

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutBandwidthRateLimitScheduleOutputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutHypervisorPropertyMappingsInputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VmwareToAwsTagMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.VmwareToAwsTagMappingTypeDef]
- **Required**: Yes


# PutHypervisorPropertyMappingsOutputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutMaintenanceStartTimeInputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### HourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### MinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### DayOfMonth
- **Type**: typing.Optional[int]

### DayOfWeek
- **Type**: typing.Optional[int]


# PutMaintenanceStartTimeOutputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# StartVirtualMachinesMetadataSyncInputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartVirtualMachinesMetadataSyncOutputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.TagTypeDef]
- **Required**: Yes


# TagResourceOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TestHypervisorConfigurationInputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# UntagResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGatewayInformationInputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayDisplayName
- **Type**: typing.Optional[str]


# UpdateGatewayInformationOutputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGatewaySoftwareNowInputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGatewaySoftwareNowOutputTypeDef

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateHypervisorInputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Host
- **Type**: typing.Optional[str]

### LogGroupArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# UpdateHypervisorOutputTypeDef

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VirtualMachineDetailsTypeDef

### HostName
- **Type**: typing.Optional[str]

### HypervisorId
- **Type**: typing.Optional[str]

### LastBackupDate
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### VmwareTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.VmwareTagTypeDef]]


# VirtualMachineTypeDef

### HostName
- **Type**: typing.Optional[str]

### HypervisorId
- **Type**: typing.Optional[str]

### LastBackupDate
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# VmwareTagTypeDef

### VmwareCategory
- **Type**: typing.Optional[str]

### VmwareTagDescription
- **Type**: typing.Optional[str]

### VmwareTagName
- **Type**: typing.Optional[str]


# VmwareToAwsTagMappingTypeDef

### AwsTagKey
- **Type**: <class 'str'>
- **Required**: Yes

### AwsTagValue
- **Type**: <class 'str'>
- **Required**: Yes

### VmwareCategory
- **Type**: <class 'str'>
- **Required**: Yes

### VmwareTagName
- **Type**: <class 'str'>
- **Required**: Yes



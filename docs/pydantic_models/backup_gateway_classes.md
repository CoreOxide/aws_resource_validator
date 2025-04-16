# Backup Gateway Classes

# AssociateGatewayToServerInput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateGatewayToServerOutput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# BandwidthRateLimitInterval

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


# BandwidthRateLimitIntervalOutput

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


# BandwidthRateLimitIntervalUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateGatewayInput

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.Tag]]


# CreateGatewayOutput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGatewayInput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGatewayOutput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteHypervisorInput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHypervisorOutput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateGatewayFromServerInput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateGatewayFromServerOutput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# Gateway

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


# GatewayDetails

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
- **Type**: <class 'NoneType'>

### NextUpdateAvailabilityTime
- **Type**: typing.Optional[datetime.datetime]

### VpcEndpoint
- **Type**: typing.Optional[str]


# GetBandwidthRateLimitScheduleInput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetBandwidthRateLimitScheduleOutput

### BandwidthRateLimitIntervals
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.BandwidthRateLimitIntervalOutput]
- **Required**: Yes

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# GetGatewayInput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetGatewayOutput

### Gateway
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.GatewayDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# GetHypervisorInput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetHypervisorOutput

### Hypervisor
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.HypervisorDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# GetHypervisorPropertyMappingsInput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetHypervisorPropertyMappingsOutput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VmwareToAwsTagMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.VmwareToAwsTagMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# GetVirtualMachineInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetVirtualMachineOutput

### VirtualMachine
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.VirtualMachineDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# Hypervisor

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


# HypervisorDetails

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


# ImportHypervisorConfigurationInput

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.Tag]]

### Username
- **Type**: typing.Optional[str]


# ImportHypervisorConfigurationOutput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListGatewaysInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGatewaysInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_gateway_classes.PaginatorConfig]


# ListGatewaysOutput

### Gateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.Gateway]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHypervisorsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHypervisorsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_gateway_classes.PaginatorConfig]


# ListHypervisorsOutput

### Hypervisors
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.Hypervisor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListVirtualMachinesInput

### HypervisorArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVirtualMachinesInputPaginate

### HypervisorArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_gateway_classes.PaginatorConfig]


# ListVirtualMachinesOutput

### VirtualMachines
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.VirtualMachine]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MaintenanceStartTime

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutBandwidthRateLimitScheduleInput

### BandwidthRateLimitIntervals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.BandwidthRateLimitIntervalUnion]
- **Required**: Yes

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutBandwidthRateLimitScheduleOutput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# PutHypervisorPropertyMappingsInput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VmwareToAwsTagMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.VmwareToAwsTagMapping]
- **Required**: Yes


# PutHypervisorPropertyMappingsOutput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# PutMaintenanceStartTimeInput

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


# PutMaintenanceStartTimeOutput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
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


# StartVirtualMachinesMetadataSyncInput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartVirtualMachinesMetadataSyncOutput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.backup_gateway_classes.Tag]
- **Required**: Yes


# TagResourceOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# TestHypervisorConfigurationInput

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


# UntagResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGatewayInformationInput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayDisplayName
- **Type**: typing.Optional[str]


# UpdateGatewayInformationOutput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGatewaySoftwareNowInput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGatewaySoftwareNowOutput

### GatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateHypervisorInput

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


# UpdateHypervisorOutput

### HypervisorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_gateway_classes.ResponseMetadata'>
- **Required**: Yes


# VirtualMachine

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


# VirtualMachineDetails

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_gateway_classes.VmwareTag]]


# VmwareTag

### VmwareCategory
- **Type**: typing.Optional[str]

### VmwareTagDescription
- **Type**: typing.Optional[str]

### VmwareTagName
- **Type**: typing.Optional[str]


# VmwareToAwsTagMapping

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



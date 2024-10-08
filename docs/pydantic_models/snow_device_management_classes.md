# Pydantic Models in snow_device_management_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTaskInputRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelTaskOutputTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CapacityTypeDef

### available
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### total
- **Type**: typing.Optional[int]

### unit
- **Type**: typing.Optional[str]

### used
- **Type**: typing.Optional[int]


# CommandTypeDef

### reboot
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### unlock
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# CpuOptionsTypeDef

### coreCount
- **Type**: typing.Optional[int]

### threadsPerCore
- **Type**: typing.Optional[int]


# CreateTaskInputRequestTypeDef

### command
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.CommandTypeDef'>
- **Required**: Yes

### targets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTaskOutputTypeDef

### taskArn
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeviceEc2InputRequestTypeDef

### instanceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceEc2OutputTypeDef

### instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management_classes.InstanceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeviceInputRequestTypeDef

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceOutputTypeDef

### associatedWithJob
- **Type**: <class 'str'>
- **Required**: Yes

### deviceCapacities
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management_classes.CapacityTypeDef]
- **Required**: Yes

### deviceState
- **Type**: typing.Literal['LOCKED', 'UNLOCKED', 'UNLOCKING']
- **Required**: Yes

### deviceType
- **Type**: <class 'str'>
- **Required**: Yes

### lastReachedOutAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### managedDeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### physicalNetworkInterfaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management_classes.PhysicalNetworkInterfaceTypeDef]
- **Required**: Yes

### software
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.SoftwareInformationTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExecutionInputRequestTypeDef

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExecutionOutputTypeDef

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTaskInputRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTaskOutputTypeDef

### completedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['CANCELED', 'COMPLETED', 'IN_PROGRESS']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### targets
- **Type**: typing.List[str]
- **Required**: Yes

### taskArn
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceSummaryTypeDef

### associatedWithJob
- **Type**: typing.Optional[str]

### managedDeviceArn
- **Type**: typing.Optional[str]

### managedDeviceId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EbsInstanceBlockDeviceTypeDef

### attachTime
- **Type**: typing.Optional[datetime.datetime]

### deleteOnTermination
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ATTACHED', 'ATTACHING', 'DETACHED', 'DETACHING']]

### volumeId
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecutionSummaryTypeDef

### executionId
- **Type**: typing.Optional[str]

### managedDeviceId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]

### taskId
- **Type**: typing.Optional[str]


# InstanceBlockDeviceMappingTypeDef

### deviceName
- **Type**: typing.Optional[str]

### ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management_classes.EbsInstanceBlockDeviceTypeDef]


# InstanceStateTypeDef

### code
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'SHUTTING_DOWN', 'STOPPED', 'STOPPING', 'TERMINATED']]


# InstanceSummaryTypeDef

### instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management_classes.InstanceTypeDef]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# InstanceTypeDef

### amiLaunchIndex
- **Type**: typing.Optional[int]

### blockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snow_device_management_classes.InstanceBlockDeviceMappingTypeDef]]

### cpuOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management_classes.CpuOptionsTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### imageId
- **Type**: typing.Optional[str]

### instanceId
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### privateIpAddress
- **Type**: typing.Optional[str]

### publicIpAddress
- **Type**: typing.Optional[str]

### rootDeviceName
- **Type**: typing.Optional[str]

### securityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snow_device_management_classes.SecurityGroupIdentifierTypeDef]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management_classes.InstanceStateTypeDef]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# ListDeviceResourcesInputListDeviceResourcesPaginateTypeDef

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management_classes.PaginatorConfigTypeDef]


# ListDeviceResourcesInputRequestTypeDef

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# ListDeviceResourcesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management_classes.ResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDevicesInputListDevicesPaginateTypeDef

### jobId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management_classes.PaginatorConfigTypeDef]


# ListDevicesInputRequestTypeDef

### jobId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDevicesOutputTypeDef

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management_classes.DeviceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExecutionsInputListExecutionsPaginateTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management_classes.PaginatorConfigTypeDef]


# ListExecutionsInputRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]


# ListExecutionsOutputTypeDef

### executions
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management_classes.ExecutionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTasksInputListTasksPaginateTypeDef

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management_classes.PaginatorConfigTypeDef]


# ListTasksInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'IN_PROGRESS']]


# ListTasksOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management_classes.TaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhysicalNetworkInterfaceTypeDef

### defaultGateway
- **Type**: typing.Optional[str]

### ipAddress
- **Type**: typing.Optional[str]

### ipAddressAssignment
- **Type**: typing.Optional[typing.Literal['DHCP', 'STATIC']]

### macAddress
- **Type**: typing.Optional[str]

### netmask
- **Type**: typing.Optional[str]

### physicalConnectorType
- **Type**: typing.Optional[typing.Literal['QSFP', 'RJ45', 'RJ45_2', 'SFP_PLUS', 'WIFI']]

### physicalNetworkInterfaceId
- **Type**: typing.Optional[str]


# ResourceSummaryTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# SecurityGroupIdentifierTypeDef

### groupId
- **Type**: typing.Optional[str]

### groupName
- **Type**: typing.Optional[str]


# SoftwareInformationTypeDef

### installState
- **Type**: typing.Optional[str]

### installedVersion
- **Type**: typing.Optional[str]

### installingVersion
- **Type**: typing.Optional[str]


# TagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TaskSummaryTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'IN_PROGRESS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### taskArn
- **Type**: typing.Optional[str]


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes



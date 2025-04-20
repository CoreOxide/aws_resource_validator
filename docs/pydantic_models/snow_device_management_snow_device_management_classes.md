# Snow Device Management Snow Device Management Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTaskInput

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelTaskOutput

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes


# Capacity

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


# Command

### reboot
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### unlock
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# CpuOptions

### coreCount
- **Type**: typing.Optional[int]

### threadsPerCore
- **Type**: typing.Optional[int]


# CreateTaskInput

### command
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.Command'>
- **Required**: Yes

### targets
- **Type**: typing.List[str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateTaskOutput

### taskArn
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDeviceEc2Input

### instanceIds
- **Type**: typing.List[str]
- **Required**: Yes

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceEc2Output

### instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.InstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDeviceInput

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceOutput

### associatedWithJob
- **Type**: <class 'str'>
- **Required**: Yes

### deviceCapacities
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.Capacity]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.PhysicalNetworkInterface]
- **Required**: Yes

### software
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.SoftwareInformation'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExecutionInput

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExecutionOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTaskInput

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTaskOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes


# DeviceSummary

### associatedWithJob
- **Type**: typing.Optional[str]

### managedDeviceArn
- **Type**: typing.Optional[str]

### managedDeviceId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EbsInstanceBlockDevice

### attachTime
- **Type**: typing.Optional[datetime.datetime]

### deleteOnTermination
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ATTACHED', 'ATTACHING', 'DETACHED', 'DETACHING']]

### volumeId
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes


# ExecutionSummary

### executionId
- **Type**: typing.Optional[str]

### managedDeviceId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]

### taskId
- **Type**: typing.Optional[str]


# Instance

### amiLaunchIndex
- **Type**: typing.Optional[int]

### blockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.InstanceBlockDeviceMapping]]

### cpuOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.CpuOptions]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.SecurityGroupIdentifier]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.InstanceState]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# InstanceBlockDeviceMapping

### deviceName
- **Type**: typing.Optional[str]

### ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.EbsInstanceBlockDevice]


# InstanceState

### code
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'SHUTTING_DOWN', 'STOPPED', 'STOPPING', 'TERMINATED']]


# InstanceSummary

### instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.Instance]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ListDeviceResourcesInput

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# ListDeviceResourcesInputPaginate

### managedDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.PaginatorConfig]


# ListDeviceResourcesOutput

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevicesInput

### jobId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDevicesInputPaginate

### jobId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.PaginatorConfig]


# ListDevicesOutput

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.DeviceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExecutionsInput

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]


# ListExecutionsInputPaginate

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.PaginatorConfig]


# ListExecutionsOutput

### executions
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ExecutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes


# ListTasksInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'IN_PROGRESS']]


# ListTasksInputPaginate

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.PaginatorConfig]


# ListTasksOutput

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.TaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snow_device_management.snow_device_management_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhysicalNetworkInterface

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


# ResourceSummary

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### id
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


# SecurityGroupIdentifier

### groupId
- **Type**: typing.Optional[str]

### groupName
- **Type**: typing.Optional[str]


# SoftwareInformation

### installState
- **Type**: typing.Optional[str]

### installedVersion
- **Type**: typing.Optional[str]

### installingVersion
- **Type**: typing.Optional[str]


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TaskSummary

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'IN_PROGRESS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### taskArn
- **Type**: typing.Optional[str]


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes



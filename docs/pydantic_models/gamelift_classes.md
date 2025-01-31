# gamelift_classes

# AcceptMatchInputRequestTypeDef

### TicketId
- **Type**: <class 'str'>
- **Required**: Yes

### PlayerIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AcceptanceType
- **Type**: typing.Literal['ACCEPT', 'REJECT']
- **Required**: Yes


# AliasTypeDef

### AliasId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### AliasArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoutingStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.RoutingStrategyTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# AnywhereConfigurationTypeDef

### Cost
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeValueOutputTypeDef

### S
- **Type**: typing.Optional[str]

### N
- **Type**: typing.Optional[float]

### SL
- **Type**: typing.Optional[typing.List[str]]

### SDM
- **Type**: typing.Optional[typing.Dict[str, float]]


# AttributeValueTypeDef

### S
- **Type**: typing.Optional[str]

### N
- **Type**: typing.Optional[float]

### SL
- **Type**: typing.Optional[typing.Sequence[str]]

### SDM
- **Type**: typing.Optional[typing.Mapping[str, float]]


# AwsCredentialsTypeDef

### AccessKeyId
- **Type**: typing.Optional[str]

### SecretAccessKey
- **Type**: typing.Optional[str]

### SessionToken
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BuildTypeDef

### BuildId
- **Type**: typing.Optional[str]

### BuildArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'READY']]

### SizeOnDisk
- **Type**: typing.Optional[int]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2023', 'WINDOWS_2012', 'WINDOWS_2016']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ServerSdkVersion
- **Type**: typing.Optional[str]


# CertificateConfigurationTypeDef

### CertificateType
- **Type**: typing.Literal['DISABLED', 'GENERATED']
- **Required**: Yes


# ClaimFilterOptionTypeDef

### InstanceStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'DRAINING']]]


# ClaimGameServerInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerId
- **Type**: typing.Optional[str]

### GameServerData
- **Type**: typing.Optional[str]

### FilterOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ClaimFilterOptionTypeDef]


# ClaimGameServerOutputTypeDef

### GameServer
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ComputeTypeDef

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### ComputeName
- **Type**: typing.Optional[str]

### ComputeArn
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### ComputeStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PENDING', 'TERMINATING']]

### Location
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2023', 'WINDOWS_2012', 'WINDOWS_2016']]

### Type
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### GameLiftServiceSdkEndpoint
- **Type**: typing.Optional[str]

### GameLiftAgentEndpoint
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### ContainerAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerAttributesTypeDef]


# ConnectionPortRangeTypeDef

### FromPort
- **Type**: <class 'int'>
- **Required**: Yes

### ToPort
- **Type**: <class 'int'>
- **Required**: Yes


# ContainerAttributesTypeDef

### ContainerPortMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ContainerPortMappingTypeDef]]


# ContainerDefinitionInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### MemoryLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerMemoryLimitsTypeDef]

### PortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerPortConfigurationTypeDef]

### Cpu
- **Type**: typing.Optional[int]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerHealthCheckTypeDef]

### Command
- **Type**: typing.Optional[typing.Sequence[str]]

### Essential
- **Type**: typing.Optional[bool]

### EntryPoint
- **Type**: typing.Optional[typing.Sequence[str]]

### WorkingDirectory
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.ContainerEnvironmentTypeDef]]

### DependsOn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.ContainerDependencyTypeDef]]


# ContainerDefinitionTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ResolvedImageDigest
- **Type**: typing.Optional[str]

### MemoryLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerMemoryLimitsTypeDef]

### PortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerPortConfigurationOutputTypeDef]

### Cpu
- **Type**: typing.Optional[int]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerHealthCheckOutputTypeDef]

### Command
- **Type**: typing.Optional[typing.List[str]]

### Essential
- **Type**: typing.Optional[bool]

### EntryPoint
- **Type**: typing.Optional[typing.List[str]]

### WorkingDirectory
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ContainerEnvironmentTypeDef]]

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ContainerDependencyTypeDef]]


# ContainerDependencyTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['COMPLETE', 'HEALTHY', 'START', 'SUCCESS']
- **Required**: Yes


# ContainerEnvironmentTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ContainerGroupDefinitionPropertyTypeDef

### SchedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### ContainerGroupDefinitionName
- **Type**: typing.Optional[str]


# ContainerGroupDefinitionTypeDef

### ContainerGroupDefinitionArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX_2023']]

### Name
- **Type**: typing.Optional[str]

### SchedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### TotalMemoryLimit
- **Type**: typing.Optional[int]

### TotalCpuLimit
- **Type**: typing.Optional[int]

### ContainerDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ContainerDefinitionTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['COPYING', 'FAILED', 'READY']]

### StatusReason
- **Type**: typing.Optional[str]


# ContainerGroupsAttributesTypeDef

### ContainerGroupDefinitionProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ContainerGroupDefinitionPropertyTypeDef]]

### ConnectionPortRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ConnectionPortRangeTypeDef]

### ContainerGroupsPerInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerGroupsPerInstanceTypeDef]


# ContainerGroupsConfigurationTypeDef

### ContainerGroupDefinitionNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ConnectionPortRange
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ConnectionPortRangeTypeDef'>
- **Required**: Yes

### DesiredReplicaContainerGroupsPerInstance
- **Type**: typing.Optional[int]


# ContainerGroupsPerInstanceTypeDef

### DesiredReplicaContainerGroupsPerInstance
- **Type**: typing.Optional[int]

### MaxReplicaContainerGroupsPerInstance
- **Type**: typing.Optional[int]


# ContainerHealthCheckOutputTypeDef

### Command
- **Type**: typing.List[str]
- **Required**: Yes

### Interval
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### StartPeriod
- **Type**: typing.Optional[int]


# ContainerHealthCheckTypeDef

### Command
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Interval
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### StartPeriod
- **Type**: typing.Optional[int]


# ContainerMemoryLimitsTypeDef

### SoftLimit
- **Type**: typing.Optional[int]

### HardLimit
- **Type**: typing.Optional[int]


# ContainerPortConfigurationOutputTypeDef

### ContainerPortRanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ContainerPortRangeTypeDef]
- **Required**: Yes


# ContainerPortConfigurationTypeDef

### ContainerPortRanges
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.ContainerPortRangeTypeDef]
- **Required**: Yes


# ContainerPortMappingTypeDef

### ContainerPort
- **Type**: typing.Optional[int]

### ConnectionPort
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]


# ContainerPortRangeTypeDef

### FromPort
- **Type**: <class 'int'>
- **Required**: Yes

### ToPort
- **Type**: <class 'int'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['TCP', 'UDP']
- **Required**: Yes


# CreateAliasInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.RoutingStrategyTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]


# CreateAliasOutputTypeDef

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.AliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBuildInputRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### StorageLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.S3LocationTypeDef]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2023', 'WINDOWS_2012', 'WINDOWS_2016']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]

### ServerSdkVersion
- **Type**: typing.Optional[str]


# CreateBuildOutputTypeDef

### Build
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.BuildTypeDef'>
- **Required**: Yes

### UploadCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### StorageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.S3LocationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContainerGroupDefinitionInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TotalMemoryLimit
- **Type**: <class 'int'>
- **Required**: Yes

### TotalCpuLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ContainerDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.ContainerDefinitionInputTypeDef]
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Literal['AMAZON_LINUX_2023']
- **Required**: Yes

### SchedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]


# CreateContainerGroupDefinitionOutputTypeDef

### ContainerGroupDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ContainerGroupDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFleetInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### BuildId
- **Type**: typing.Optional[str]

### ScriptId
- **Type**: typing.Optional[str]

### ServerLaunchPath
- **Type**: typing.Optional[str]

### ServerLaunchParameters
- **Type**: typing.Optional[str]

### LogPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### EC2InstanceType
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### EC2InboundPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.IpPermissionTypeDef]]

### NewGameSessionProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]

### RuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.RuntimeConfigurationTypeDef]

### ResourceCreationLimitPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ResourceCreationLimitPolicyTypeDef]

### MetricGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### PeerVpcAwsAccountId
- **Type**: typing.Optional[str]

### PeerVpcId
- **Type**: typing.Optional[str]

### FleetType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### InstanceRoleArn
- **Type**: typing.Optional[str]

### CertificateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.CertificateConfigurationTypeDef]

### Locations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.LocationConfigurationTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]

### ComputeType
- **Type**: typing.Optional[typing.Literal['ANYWHERE', 'CONTAINER', 'EC2']]

### AnywhereConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.AnywhereConfigurationTypeDef]

### InstanceRoleCredentialsProvider
- **Type**: typing.Optional[typing.Literal['SHARED_CREDENTIAL_FILE']]

### ContainerGroupsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerGroupsConfigurationTypeDef]


# CreateFleetLocationsInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Locations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.LocationConfigurationTypeDef]
- **Required**: Yes


# CreateFleetLocationsOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.LocationStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFleetOutputTypeDef

### FleetAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.FleetAttributesTypeDef'>
- **Required**: Yes

### LocationStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.LocationStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGameServerGroupInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### MinSize
- **Type**: <class 'int'>
- **Required**: Yes

### MaxSize
- **Type**: <class 'int'>
- **Required**: Yes

### LaunchTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.LaunchTemplateSpecificationTypeDef'>
- **Required**: Yes

### InstanceDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.InstanceDefinitionTypeDef]
- **Required**: Yes

### AutoScalingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.GameServerGroupAutoScalingPolicyTypeDef]

### BalancingStrategy
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_ONLY', 'SPOT_ONLY', 'SPOT_PREFERRED']]

### GameServerProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FULL_PROTECTION', 'NO_PROTECTION']]

### VpcSubnets
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]


# CreateGameServerGroupOutputTypeDef

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGameSessionInputRequestTypeDef

### MaximumPlayerSessionCount
- **Type**: <class 'int'>
- **Required**: Yes

### FleetId
- **Type**: typing.Optional[str]

### AliasId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### GameProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.GamePropertyTypeDef]]

### CreatorId
- **Type**: typing.Optional[str]

### GameSessionId
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]

### GameSessionData
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]


# CreateGameSessionOutputTypeDef

### GameSession
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGameSessionQueueInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### PlayerLatencyPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.PlayerLatencyPolicyTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.GameSessionQueueDestinationTypeDef]]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.FilterConfigurationTypeDef]

### PriorityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PriorityConfigurationTypeDef]

### CustomEventData
- **Type**: typing.Optional[str]

### NotificationTarget
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]


# CreateGameSessionQueueOutputTypeDef

### GameSessionQueue
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameSessionQueueTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationInputRequestTypeDef

### LocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]


# CreateLocationOutputTypeDef

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.LocationModelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMatchmakingConfigurationInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RequestTimeoutSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### AcceptanceRequired
- **Type**: <class 'bool'>
- **Required**: Yes

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### GameSessionQueueArns
- **Type**: typing.Optional[typing.Sequence[str]]

### AcceptanceTimeoutSeconds
- **Type**: typing.Optional[int]

### NotificationTarget
- **Type**: typing.Optional[str]

### AdditionalPlayerCount
- **Type**: typing.Optional[int]

### CustomEventData
- **Type**: typing.Optional[str]

### GameProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.GamePropertyTypeDef]]

### GameSessionData
- **Type**: typing.Optional[str]

### BackfillMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]

### FlexMatchMode
- **Type**: typing.Optional[typing.Literal['STANDALONE', 'WITH_QUEUE']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]


# CreateMatchmakingConfigurationOutputTypeDef

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.MatchmakingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMatchmakingRuleSetInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetBody
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]


# CreateMatchmakingRuleSetOutputTypeDef

### RuleSet
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.MatchmakingRuleSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePlayerSessionInputRequestTypeDef

### GameSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### PlayerId
- **Type**: <class 'str'>
- **Required**: Yes

### PlayerData
- **Type**: typing.Optional[str]


# CreatePlayerSessionOutputTypeDef

### PlayerSession
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.PlayerSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePlayerSessionsInputRequestTypeDef

### GameSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### PlayerIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PlayerDataMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePlayerSessionsOutputTypeDef

### PlayerSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.PlayerSessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateScriptInputRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### StorageLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.S3LocationTypeDef]

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]]


# CreateScriptOutputTypeDef

### Script
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ScriptTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcPeeringAuthorizationInputRequestTypeDef

### GameLiftAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerVpcId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateVpcPeeringAuthorizationOutputTypeDef

### VpcPeeringAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.VpcPeeringAuthorizationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcPeeringConnectionInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerVpcAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerVpcId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAliasInputRequestTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBuildInputRequestTypeDef

### BuildId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerGroupDefinitionInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFleetInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFleetLocationsInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Locations
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteFleetLocationsOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.LocationStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGameServerGroupInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteOption
- **Type**: typing.Optional[typing.Literal['FORCE_DELETE', 'RETAIN', 'SAFE_DELETE']]


# DeleteGameServerGroupOutputTypeDef

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGameSessionQueueInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLocationInputRequestTypeDef

### LocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMatchmakingConfigurationInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMatchmakingRuleSetInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScalingPolicyInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScriptInputRequestTypeDef

### ScriptId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcPeeringAuthorizationInputRequestTypeDef

### GameLiftAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerVpcId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcPeeringConnectionInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcPeeringConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterComputeInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterGameServerInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAliasInputRequestTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAliasOutputTypeDef

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.AliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBuildInputRequestTypeDef

### BuildId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBuildOutputTypeDef

### Build
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.BuildTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeComputeInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeComputeOutputTypeDef

### Compute
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ComputeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeContainerGroupDefinitionInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContainerGroupDefinitionOutputTypeDef

### ContainerGroupDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ContainerGroupDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEC2InstanceLimitsInputRequestTypeDef

### EC2InstanceType
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### Location
- **Type**: typing.Optional[str]


# DescribeEC2InstanceLimitsOutputTypeDef

### EC2InstanceLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.EC2InstanceLimitTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetAttributesInputDescribeFleetAttributesPaginateTypeDef

### FleetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeFleetAttributesInputRequestTypeDef

### FleetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAttributesOutputTypeDef

### FleetAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.FleetAttributesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetCapacityInputDescribeFleetCapacityPaginateTypeDef

### FleetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeFleetCapacityInputRequestTypeDef

### FleetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetCapacityOutputTypeDef

### FleetCapacity
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.FleetCapacityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetEventsInputDescribeFleetEventsPaginateTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeFleetEventsInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetEventsOutputTypeDef

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetLocationAttributesInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Locations
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetLocationAttributesOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.LocationAttributesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetLocationCapacityInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFleetLocationCapacityOutputTypeDef

### FleetCapacity
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.FleetCapacityTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetLocationUtilizationInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFleetLocationUtilizationOutputTypeDef

### FleetUtilization
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.FleetUtilizationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetPortSettingsInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]


# DescribeFleetPortSettingsOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### InboundPermissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.IpPermissionTypeDef]
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Literal['PENDING_UPDATE']
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetUtilizationInputDescribeFleetUtilizationPaginateTypeDef

### FleetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeFleetUtilizationInputRequestTypeDef

### FleetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetUtilizationOutputTypeDef

### FleetUtilization
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.FleetUtilizationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameServerGroupInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGameServerGroupOutputTypeDef

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGameServerInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGameServerInstancesInputDescribeGameServerInstancesPaginateTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeGameServerInstancesInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameServerInstancesOutputTypeDef

### GameServerInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GameServerInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameServerOutputTypeDef

### GameServer
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGameSessionDetailsInputDescribeGameSessionDetailsPaginateTypeDef

### FleetId
- **Type**: typing.Optional[str]

### GameSessionId
- **Type**: typing.Optional[str]

### AliasId
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeGameSessionDetailsInputRequestTypeDef

### FleetId
- **Type**: typing.Optional[str]

### GameSessionId
- **Type**: typing.Optional[str]

### AliasId
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameSessionDetailsOutputTypeDef

### GameSessionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GameSessionDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameSessionPlacementInputRequestTypeDef

### PlacementId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGameSessionPlacementOutputTypeDef

### GameSessionPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameSessionPlacementTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGameSessionQueuesInputDescribeGameSessionQueuesPaginateTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeGameSessionQueuesInputRequestTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameSessionQueuesOutputTypeDef

### GameSessionQueues
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GameSessionQueueTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameSessionsInputDescribeGameSessionsPaginateTypeDef

### FleetId
- **Type**: typing.Optional[str]

### GameSessionId
- **Type**: typing.Optional[str]

### AliasId
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeGameSessionsInputRequestTypeDef

### FleetId
- **Type**: typing.Optional[str]

### GameSessionId
- **Type**: typing.Optional[str]

### AliasId
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameSessionsOutputTypeDef

### GameSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GameSessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancesInputDescribeInstancesPaginateTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeInstancesInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]


# DescribeInstancesOutputTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.InstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMatchmakingConfigurationsInputDescribeMatchmakingConfigurationsPaginateTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### RuleSetName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeMatchmakingConfigurationsInputRequestTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### RuleSetName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMatchmakingConfigurationsOutputTypeDef

### Configurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.MatchmakingConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMatchmakingInputRequestTypeDef

### TicketIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeMatchmakingOutputTypeDef

### TicketList
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.MatchmakingTicketTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMatchmakingRuleSetsInputDescribeMatchmakingRuleSetsPaginateTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeMatchmakingRuleSetsInputRequestTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMatchmakingRuleSetsOutputTypeDef

### RuleSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.MatchmakingRuleSetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePlayerSessionsInputDescribePlayerSessionsPaginateTypeDef

### GameSessionId
- **Type**: typing.Optional[str]

### PlayerId
- **Type**: typing.Optional[str]

### PlayerSessionId
- **Type**: typing.Optional[str]

### PlayerSessionStatusFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribePlayerSessionsInputRequestTypeDef

### GameSessionId
- **Type**: typing.Optional[str]

### PlayerId
- **Type**: typing.Optional[str]

### PlayerSessionId
- **Type**: typing.Optional[str]

### PlayerSessionStatusFilter
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePlayerSessionsOutputTypeDef

### PlayerSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.PlayerSessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRuntimeConfigurationInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRuntimeConfigurationOutputTypeDef

### RuntimeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.RuntimeConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeScalingPoliciesInputDescribeScalingPoliciesPaginateTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### StatusFilter
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'ERROR', 'UPDATE_REQUESTED', 'UPDATING']]

### Location
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# DescribeScalingPoliciesInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### StatusFilter
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'ERROR', 'UPDATE_REQUESTED', 'UPDATING']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]


# DescribeScalingPoliciesOutputTypeDef

### ScalingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ScalingPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScriptInputRequestTypeDef

### ScriptId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScriptOutputTypeDef

### Script
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ScriptTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVpcPeeringAuthorizationsOutputTypeDef

### VpcPeeringAuthorizations
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.VpcPeeringAuthorizationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVpcPeeringConnectionsInputRequestTypeDef

### FleetId
- **Type**: typing.Optional[str]


# DescribeVpcPeeringConnectionsOutputTypeDef

### VpcPeeringConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.VpcPeeringConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DesiredPlayerSessionTypeDef

### PlayerId
- **Type**: typing.Optional[str]

### PlayerData
- **Type**: typing.Optional[str]


# EC2InstanceCountsTypeDef

### DESIRED
- **Type**: typing.Optional[int]

### MINIMUM
- **Type**: typing.Optional[int]

### MAXIMUM
- **Type**: typing.Optional[int]

### PENDING
- **Type**: typing.Optional[int]

### ACTIVE
- **Type**: typing.Optional[int]

### IDLE
- **Type**: typing.Optional[int]

### TERMINATING
- **Type**: typing.Optional[int]


# EC2InstanceLimitTypeDef

### EC2InstanceType
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### CurrentInstances
- **Type**: typing.Optional[int]

### InstanceLimit
- **Type**: typing.Optional[int]

### Location
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventTypeDef

### EventId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### EventCode
- **Type**: typing.Optional[typing.Literal['FLEET_ACTIVATION_FAILED', 'FLEET_ACTIVATION_FAILED_NO_INSTANCES', 'FLEET_BINARY_DOWNLOAD_FAILED', 'FLEET_CREATED', 'FLEET_CREATION_EXTRACTING_BUILD', 'FLEET_CREATION_RUNNING_INSTALLER', 'FLEET_CREATION_VALIDATING_RUNTIME_CONFIG', 'FLEET_DELETED', 'FLEET_INITIALIZATION_FAILED', 'FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED', 'FLEET_SCALING_EVENT', 'FLEET_STATE_ACTIVATING', 'FLEET_STATE_ACTIVE', 'FLEET_STATE_BUILDING', 'FLEET_STATE_DOWNLOADING', 'FLEET_STATE_ERROR', 'FLEET_STATE_VALIDATING', 'FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE', 'FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND', 'FLEET_VALIDATION_TIMED_OUT', 'FLEET_VPC_PEERING_DELETED', 'FLEET_VPC_PEERING_FAILED', 'FLEET_VPC_PEERING_SUCCEEDED', 'GAME_SESSION_ACTIVATION_TIMEOUT', 'GENERIC_EVENT', 'INSTANCE_INTERRUPTED', 'INSTANCE_RECYCLED', 'SERVER_PROCESS_CRASHED', 'SERVER_PROCESS_FORCE_TERMINATED', 'SERVER_PROCESS_INVALID_PATH', 'SERVER_PROCESS_PROCESS_EXIT_TIMEOUT', 'SERVER_PROCESS_PROCESS_READY_TIMEOUT', 'SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT', 'SERVER_PROCESS_TERMINATED_UNHEALTHY']]

### Message
- **Type**: typing.Optional[str]

### EventTime
- **Type**: typing.Optional[datetime.datetime]

### PreSignedLogUrl
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]


# FilterConfigurationExtraOutputTypeDef

### AllowedLocations
- **Type**: typing.Optional[typing.List[str]]


# FilterConfigurationOutputTypeDef

### AllowedLocations
- **Type**: typing.Optional[typing.List[str]]


# FilterConfigurationTypeDef

### AllowedLocations
- **Type**: typing.Optional[typing.Sequence[str]]


# FleetAttributesTypeDef

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### FleetType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### InstanceType
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TerminationTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'BUILDING', 'DELETING', 'DOWNLOADING', 'ERROR', 'NEW', 'NOT_FOUND', 'TERMINATED', 'VALIDATING']]

### BuildId
- **Type**: typing.Optional[str]

### BuildArn
- **Type**: typing.Optional[str]

### ScriptId
- **Type**: typing.Optional[str]

### ScriptArn
- **Type**: typing.Optional[str]

### ServerLaunchPath
- **Type**: typing.Optional[str]

### ServerLaunchParameters
- **Type**: typing.Optional[str]

### LogPaths
- **Type**: typing.Optional[typing.List[str]]

### NewGameSessionProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2023', 'WINDOWS_2012', 'WINDOWS_2016']]

### ResourceCreationLimitPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ResourceCreationLimitPolicyTypeDef]

### MetricGroups
- **Type**: typing.Optional[typing.List[str]]

### StoppedActions
- **Type**: typing.Optional[typing.List[typing.Literal['AUTO_SCALING']]]

### InstanceRoleArn
- **Type**: typing.Optional[str]

### CertificateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.CertificateConfigurationTypeDef]

### ComputeType
- **Type**: typing.Optional[typing.Literal['ANYWHERE', 'CONTAINER', 'EC2']]

### AnywhereConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.AnywhereConfigurationTypeDef]

### InstanceRoleCredentialsProvider
- **Type**: typing.Optional[typing.Literal['SHARED_CREDENTIAL_FILE']]

### ContainerGroupsAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ContainerGroupsAttributesTypeDef]


# FleetCapacityTypeDef

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### InstanceCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.EC2InstanceCountsTypeDef]

### Location
- **Type**: typing.Optional[str]

### ReplicaContainerGroupCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ReplicaContainerGroupCountsTypeDef]


# FleetUtilizationTypeDef

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### ActiveServerProcessCount
- **Type**: typing.Optional[int]

### ActiveGameSessionCount
- **Type**: typing.Optional[int]

### CurrentPlayerSessionCount
- **Type**: typing.Optional[int]

### MaximumPlayerSessionCount
- **Type**: typing.Optional[int]

### Location
- **Type**: typing.Optional[str]


# GamePropertyTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# GameServerGroupAutoScalingPolicyTypeDef

### TargetTrackingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.TargetTrackingConfigurationTypeDef'>
- **Required**: Yes

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]


# GameServerGroupTypeDef

### GameServerGroupName
- **Type**: typing.Optional[str]

### GameServerGroupArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### InstanceDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.InstanceDefinitionTypeDef]]

### BalancingStrategy
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_ONLY', 'SPOT_ONLY', 'SPOT_PREFERRED']]

### GameServerProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FULL_PROTECTION', 'NO_PROTECTION']]

### AutoScalingGroupArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'DELETED', 'DELETE_SCHEDULED', 'DELETING', 'ERROR', 'NEW']]

### StatusReason
- **Type**: typing.Optional[str]

### SuspendedActions
- **Type**: typing.Optional[typing.List[typing.Literal['REPLACE_INSTANCE_TYPES']]]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# GameServerInstanceTypeDef

### GameServerGroupName
- **Type**: typing.Optional[str]

### GameServerGroupArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAINING', 'SPOT_TERMINATING']]


# GameServerTypeDef

### GameServerGroupName
- **Type**: typing.Optional[str]

### GameServerGroupArn
- **Type**: typing.Optional[str]

### GameServerId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### ConnectionInfo
- **Type**: typing.Optional[str]

### GameServerData
- **Type**: typing.Optional[str]

### ClaimStatus
- **Type**: typing.Optional[typing.Literal['CLAIMED']]

### UtilizationStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'UTILIZED']]

### RegistrationTime
- **Type**: typing.Optional[datetime.datetime]

### LastClaimTime
- **Type**: typing.Optional[datetime.datetime]

### LastHealthCheckTime
- **Type**: typing.Optional[datetime.datetime]


# GameSessionConnectionInfoTypeDef

### GameSessionArn
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MatchedPlayerSessions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.MatchedPlayerSessionTypeDef]]


# GameSessionDetailTypeDef

### GameSession
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.GameSessionTypeDef]

### ProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]


# GameSessionPlacementTypeDef

### PlacementId
- **Type**: typing.Optional[str]

### GameSessionQueueName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'FULFILLED', 'PENDING', 'TIMED_OUT']]

### GameProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GamePropertyTypeDef]]

### MaximumPlayerSessionCount
- **Type**: typing.Optional[int]

### GameSessionName
- **Type**: typing.Optional[str]

### GameSessionId
- **Type**: typing.Optional[str]

### GameSessionArn
- **Type**: typing.Optional[str]

### GameSessionRegion
- **Type**: typing.Optional[str]

### PlayerLatencies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.PlayerLatencyTypeDef]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### IpAddress
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### PlacedPlayerSessions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.PlacedPlayerSessionTypeDef]]

### GameSessionData
- **Type**: typing.Optional[str]

### MatchmakerData
- **Type**: typing.Optional[str]


# GameSessionQueueDestinationTypeDef

### DestinationArn
- **Type**: typing.Optional[str]


# GameSessionQueueTypeDef

### Name
- **Type**: typing.Optional[str]

### GameSessionQueueArn
- **Type**: typing.Optional[str]

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### PlayerLatencyPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.PlayerLatencyPolicyTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GameSessionQueueDestinationTypeDef]]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.FilterConfigurationOutputTypeDef]

### PriorityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PriorityConfigurationOutputTypeDef]

### CustomEventData
- **Type**: typing.Optional[str]

### NotificationTarget
- **Type**: typing.Optional[str]


# GameSessionTypeDef

### GameSessionId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TerminationTime
- **Type**: typing.Optional[datetime.datetime]

### CurrentPlayerSessionCount
- **Type**: typing.Optional[int]

### MaximumPlayerSessionCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'ERROR', 'TERMINATED', 'TERMINATING']]

### StatusReason
- **Type**: typing.Optional[typing.Literal['INTERRUPTED']]

### GameProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GamePropertyTypeDef]]

### IpAddress
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### PlayerSessionCreationPolicy
- **Type**: typing.Optional[typing.Literal['ACCEPT_ALL', 'DENY_ALL']]

### CreatorId
- **Type**: typing.Optional[str]

### GameSessionData
- **Type**: typing.Optional[str]

### MatchmakerData
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]


# GetComputeAccessInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetComputeAccessOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComputeAuthTokenInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetComputeAuthTokenOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthToken
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGameSessionLogUrlInputRequestTypeDef

### GameSessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGameSessionLogUrlOutputTypeDef

### PreSignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceAccessInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceAccessOutputTypeDef

### InstanceAccess
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.InstanceAccessTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceAccessTypeDef

### FleetId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2023', 'WINDOWS_2012', 'WINDOWS_2016']]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.InstanceCredentialsTypeDef]


# InstanceCredentialsTypeDef

### UserName
- **Type**: typing.Optional[str]

### Secret
- **Type**: typing.Optional[str]


# InstanceDefinitionTypeDef

### InstanceType
- **Type**: typing.Literal['c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge']
- **Required**: Yes

### WeightedCapacity
- **Type**: typing.Optional[str]


# InstanceTypeDef

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2023', 'WINDOWS_2012', 'WINDOWS_2016']]

### Type
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PENDING', 'TERMINATING']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Location
- **Type**: typing.Optional[str]


# IpPermissionTypeDef

### FromPort
- **Type**: <class 'int'>
- **Required**: Yes

### ToPort
- **Type**: <class 'int'>
- **Required**: Yes

### IpRange
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['TCP', 'UDP']
- **Required**: Yes


# LaunchTemplateSpecificationTypeDef

### LaunchTemplateId
- **Type**: typing.Optional[str]

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# ListAliasesInputListAliasesPaginateTypeDef

### RoutingStrategyType
- **Type**: typing.Optional[typing.Literal['SIMPLE', 'TERMINAL']]

### Name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# ListAliasesInputRequestTypeDef

### RoutingStrategyType
- **Type**: typing.Optional[typing.Literal['SIMPLE', 'TERMINAL']]

### Name
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAliasesOutputTypeDef

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.AliasTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBuildsInputListBuildsPaginateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'READY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# ListBuildsInputRequestTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'READY']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBuildsOutputTypeDef

### Builds
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.BuildTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComputeInputListComputePaginateTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# ListComputeInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListComputeOutputTypeDef

### ComputeList
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ComputeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContainerGroupDefinitionsInputListContainerGroupDefinitionsPaginateTypeDef

### SchedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# ListContainerGroupDefinitionsInputRequestTypeDef

### SchedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListContainerGroupDefinitionsOutputTypeDef

### ContainerGroupDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ContainerGroupDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFleetsInputListFleetsPaginateTypeDef

### BuildId
- **Type**: typing.Optional[str]

### ScriptId
- **Type**: typing.Optional[str]

### ContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# ListFleetsInputRequestTypeDef

### BuildId
- **Type**: typing.Optional[str]

### ScriptId
- **Type**: typing.Optional[str]

### ContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFleetsOutputTypeDef

### FleetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGameServerGroupsInputListGameServerGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# ListGameServerGroupsInputRequestTypeDef

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGameServerGroupsOutputTypeDef

### GameServerGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GameServerGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGameServersInputListGameServersPaginateTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# ListGameServersInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGameServersOutputTypeDef

### GameServers
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GameServerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLocationsInputListLocationsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWS', 'CUSTOM']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# ListLocationsInputRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWS', 'CUSTOM']]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLocationsOutputTypeDef

### Locations
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.LocationModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListScriptsInputListScriptsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# ListScriptsInputRequestTypeDef

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListScriptsOutputTypeDef

### Scripts
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ScriptTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LocationAttributesTypeDef

### LocationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.LocationStateTypeDef]

### StoppedActions
- **Type**: typing.Optional[typing.List[typing.Literal['AUTO_SCALING']]]

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['PENDING_UPDATE']]


# LocationConfigurationTypeDef

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# LocationModelTypeDef

### LocationName
- **Type**: typing.Optional[str]

### LocationArn
- **Type**: typing.Optional[str]


# LocationStateTypeDef

### Location
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'BUILDING', 'DELETING', 'DOWNLOADING', 'ERROR', 'NEW', 'NOT_FOUND', 'TERMINATED', 'VALIDATING']]


# MatchedPlayerSessionTypeDef

### PlayerId
- **Type**: typing.Optional[str]

### PlayerSessionId
- **Type**: typing.Optional[str]


# MatchmakingConfigurationTypeDef

### Name
- **Type**: typing.Optional[str]

### ConfigurationArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### GameSessionQueueArns
- **Type**: typing.Optional[typing.List[str]]

### RequestTimeoutSeconds
- **Type**: typing.Optional[int]

### AcceptanceTimeoutSeconds
- **Type**: typing.Optional[int]

### AcceptanceRequired
- **Type**: typing.Optional[bool]

### RuleSetName
- **Type**: typing.Optional[str]

### RuleSetArn
- **Type**: typing.Optional[str]

### NotificationTarget
- **Type**: typing.Optional[str]

### AdditionalPlayerCount
- **Type**: typing.Optional[int]

### CustomEventData
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### GameProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GamePropertyTypeDef]]

### GameSessionData
- **Type**: typing.Optional[str]

### BackfillMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]

### FlexMatchMode
- **Type**: typing.Optional[typing.Literal['STANDALONE', 'WITH_QUEUE']]


# MatchmakingRuleSetTypeDef

### RuleSetBody
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetName
- **Type**: typing.Optional[str]

### RuleSetArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# MatchmakingTicketTypeDef

### TicketId
- **Type**: typing.Optional[str]

### ConfigurationName
- **Type**: typing.Optional[str]

### ConfigurationArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PLACING', 'QUEUED', 'REQUIRES_ACCEPTANCE', 'SEARCHING', 'TIMED_OUT']]

### StatusReason
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Players
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.PlayerOutputTypeDef]]

### GameSessionConnectionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.GameSessionConnectionInfoTypeDef]

### EstimatedWaitTime
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlacedPlayerSessionTypeDef

### PlayerId
- **Type**: typing.Optional[str]

### PlayerSessionId
- **Type**: typing.Optional[str]


# PlayerLatencyPolicyTypeDef

### MaximumIndividualPlayerLatencyMilliseconds
- **Type**: typing.Optional[int]

### PolicyDurationSeconds
- **Type**: typing.Optional[int]


# PlayerLatencyTypeDef

### PlayerId
- **Type**: typing.Optional[str]

### RegionIdentifier
- **Type**: typing.Optional[str]

### LatencyInMilliseconds
- **Type**: typing.Optional[float]


# PlayerOutputTypeDef

### PlayerId
- **Type**: typing.Optional[str]

### PlayerAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.gamelift_classes.AttributeValueOutputTypeDef]]

### Team
- **Type**: typing.Optional[str]

### LatencyInMs
- **Type**: typing.Optional[typing.Dict[str, int]]


# PlayerSessionTypeDef

### PlayerSessionId
- **Type**: typing.Optional[str]

### PlayerId
- **Type**: typing.Optional[str]

### GameSessionId
- **Type**: typing.Optional[str]

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TerminationTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COMPLETED', 'RESERVED', 'TIMEDOUT']]

### IpAddress
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### PlayerData
- **Type**: typing.Optional[str]


# PlayerTypeDef

### PlayerId
- **Type**: typing.Optional[str]

### PlayerAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.gamelift_classes.AttributeValueTypeDef]]

### Team
- **Type**: typing.Optional[str]

### LatencyInMs
- **Type**: typing.Optional[typing.Mapping[str, int]]


# PriorityConfigurationExtraOutputTypeDef

### PriorityOrder
- **Type**: typing.Optional[typing.List[typing.Literal['COST', 'DESTINATION', 'LATENCY', 'LOCATION']]]

### LocationOrder
- **Type**: typing.Optional[typing.List[str]]


# PriorityConfigurationOutputTypeDef

### PriorityOrder
- **Type**: typing.Optional[typing.List[typing.Literal['COST', 'DESTINATION', 'LATENCY', 'LOCATION']]]

### LocationOrder
- **Type**: typing.Optional[typing.List[str]]


# PriorityConfigurationTypeDef

### PriorityOrder
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COST', 'DESTINATION', 'LATENCY', 'LOCATION']]]

### LocationOrder
- **Type**: typing.Optional[typing.Sequence[str]]


# PutScalingPolicyInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: typing.Literal['ActivatingGameSessions', 'ActiveGameSessions', 'ActiveInstances', 'AvailableGameSessions', 'AvailablePlayerSessions', 'ConcurrentActivatableGameSessions', 'CurrentPlayerSessions', 'IdleInstances', 'PercentAvailableGameSessions', 'PercentIdleInstances', 'QueueDepth', 'WaitTime']
- **Required**: Yes

### ScalingAdjustment
- **Type**: typing.Optional[int]

### ScalingAdjustmentType
- **Type**: typing.Optional[typing.Literal['ChangeInCapacity', 'ExactCapacity', 'PercentChangeInCapacity']]

### Threshold
- **Type**: typing.Optional[float]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### PolicyType
- **Type**: typing.Optional[typing.Literal['RuleBased', 'TargetBased']]

### TargetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.TargetConfigurationTypeDef]


# PutScalingPolicyOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterComputeInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes

### CertificatePath
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]


# RegisterComputeOutputTypeDef

### Compute
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ComputeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterGameServerInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionInfo
- **Type**: typing.Optional[str]

### GameServerData
- **Type**: typing.Optional[str]


# RegisterGameServerOutputTypeDef

### GameServer
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplicaContainerGroupCountsTypeDef

### PENDING
- **Type**: typing.Optional[int]

### ACTIVE
- **Type**: typing.Optional[int]

### IDLE
- **Type**: typing.Optional[int]

### TERMINATING
- **Type**: typing.Optional[int]


# RequestUploadCredentialsInputRequestTypeDef

### BuildId
- **Type**: <class 'str'>
- **Required**: Yes


# RequestUploadCredentialsOutputTypeDef

### UploadCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### StorageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.S3LocationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResolveAliasInputRequestTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# ResolveAliasOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceCreationLimitPolicyTypeDef

### NewGameSessionsPerCreator
- **Type**: typing.Optional[int]

### PolicyPeriodInMinutes
- **Type**: typing.Optional[int]


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


# ResumeGameServerGroupInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResumeActions
- **Type**: typing.Sequence[typing.Literal['REPLACE_INSTANCE_TYPES']]
- **Required**: Yes


# ResumeGameServerGroupOutputTypeDef

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RoutingStrategyTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['SIMPLE', 'TERMINAL']]

### FleetId
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# RuntimeConfigurationOutputTypeDef

### ServerProcesses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift_classes.ServerProcessTypeDef]]

### MaxConcurrentGameSessionActivations
- **Type**: typing.Optional[int]

### GameSessionActivationTimeoutSeconds
- **Type**: typing.Optional[int]


# RuntimeConfigurationTypeDef

### ServerProcesses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.ServerProcessTypeDef]]

### MaxConcurrentGameSessionActivations
- **Type**: typing.Optional[int]

### GameSessionActivationTimeoutSeconds
- **Type**: typing.Optional[int]


# S3LocationTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ObjectVersion
- **Type**: typing.Optional[str]


# ScalingPolicyTypeDef

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'ERROR', 'UPDATE_REQUESTED', 'UPDATING']]

### ScalingAdjustment
- **Type**: typing.Optional[int]

### ScalingAdjustmentType
- **Type**: typing.Optional[typing.Literal['ChangeInCapacity', 'ExactCapacity', 'PercentChangeInCapacity']]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']]

### Threshold
- **Type**: typing.Optional[float]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### MetricName
- **Type**: typing.Optional[typing.Literal['ActivatingGameSessions', 'ActiveGameSessions', 'ActiveInstances', 'AvailableGameSessions', 'AvailablePlayerSessions', 'ConcurrentActivatableGameSessions', 'CurrentPlayerSessions', 'IdleInstances', 'PercentAvailableGameSessions', 'PercentIdleInstances', 'QueueDepth', 'WaitTime']]

### PolicyType
- **Type**: typing.Optional[typing.Literal['RuleBased', 'TargetBased']]

### TargetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.TargetConfigurationTypeDef]

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['PENDING_UPDATE']]

### Location
- **Type**: typing.Optional[str]


# ScriptTypeDef

### ScriptId
- **Type**: typing.Optional[str]

### ScriptArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### SizeOnDisk
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### StorageLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.S3LocationTypeDef]


# SearchGameSessionsInputRequestTypeDef

### FleetId
- **Type**: typing.Optional[str]

### AliasId
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### FilterExpression
- **Type**: typing.Optional[str]

### SortExpression
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchGameSessionsInputSearchGameSessionsPaginateTypeDef

### FleetId
- **Type**: typing.Optional[str]

### AliasId
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### FilterExpression
- **Type**: typing.Optional[str]

### SortExpression
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PaginatorConfigTypeDef]


# SearchGameSessionsOutputTypeDef

### GameSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift_classes.GameSessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ServerProcessTypeDef

### LaunchPath
- **Type**: <class 'str'>
- **Required**: Yes

### ConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[str]


# StartFleetActionsInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[typing.Literal['AUTO_SCALING']]
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]


# StartFleetActionsOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartGameSessionPlacementInputRequestTypeDef

### PlacementId
- **Type**: <class 'str'>
- **Required**: Yes

### GameSessionQueueName
- **Type**: <class 'str'>
- **Required**: Yes

### MaximumPlayerSessionCount
- **Type**: <class 'int'>
- **Required**: Yes

### GameProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.GamePropertyTypeDef]]

### GameSessionName
- **Type**: typing.Optional[str]

### PlayerLatencies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.PlayerLatencyTypeDef]]

### DesiredPlayerSessions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.DesiredPlayerSessionTypeDef]]

### GameSessionData
- **Type**: typing.Optional[str]


# StartGameSessionPlacementOutputTypeDef

### GameSessionPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameSessionPlacementTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMatchBackfillInputRequestTypeDef

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Players
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.gamelift_classes.PlayerTypeDef, aws_resource_validator.pydantic_models.gamelift_classes.PlayerOutputTypeDef]]
- **Required**: Yes

### TicketId
- **Type**: typing.Optional[str]

### GameSessionArn
- **Type**: typing.Optional[str]


# StartMatchBackfillOutputTypeDef

### MatchmakingTicket
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.MatchmakingTicketTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMatchmakingInputRequestTypeDef

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Players
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.gamelift_classes.PlayerTypeDef, aws_resource_validator.pydantic_models.gamelift_classes.PlayerOutputTypeDef]]
- **Required**: Yes

### TicketId
- **Type**: typing.Optional[str]


# StartMatchmakingOutputTypeDef

### MatchmakingTicket
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.MatchmakingTicketTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopFleetActionsInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[typing.Literal['AUTO_SCALING']]
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]


# StopFleetActionsOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopGameSessionPlacementInputRequestTypeDef

### PlacementId
- **Type**: <class 'str'>
- **Required**: Yes


# StopGameSessionPlacementOutputTypeDef

### GameSessionPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameSessionPlacementTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopMatchmakingInputRequestTypeDef

### TicketId
- **Type**: <class 'str'>
- **Required**: Yes


# SuspendGameServerGroupInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SuspendActions
- **Type**: typing.Sequence[typing.Literal['REPLACE_INSTANCE_TYPES']]
- **Required**: Yes


# SuspendGameServerGroupOutputTypeDef

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetConfigurationTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes


# TargetTrackingConfigurationTypeDef

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAliasInputRequestTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoutingStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.RoutingStrategyTypeDef]


# UpdateAliasOutputTypeDef

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.AliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBuildInputRequestTypeDef

### BuildId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# UpdateBuildOutputTypeDef

### Build
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.BuildTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFleetAttributesInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### NewGameSessionProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]

### ResourceCreationLimitPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.ResourceCreationLimitPolicyTypeDef]

### MetricGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### AnywhereConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.AnywhereConfigurationTypeDef]


# UpdateFleetAttributesOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFleetCapacityInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredInstances
- **Type**: typing.Optional[int]

### MinSize
- **Type**: typing.Optional[int]

### MaxSize
- **Type**: typing.Optional[int]

### Location
- **Type**: typing.Optional[str]


# UpdateFleetCapacityOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFleetPortSettingsInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### InboundPermissionAuthorizations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.IpPermissionTypeDef]]

### InboundPermissionRevocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.IpPermissionTypeDef]]


# UpdateFleetPortSettingsOutputTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGameServerGroupInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### InstanceDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.InstanceDefinitionTypeDef]]

### GameServerProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FULL_PROTECTION', 'NO_PROTECTION']]

### BalancingStrategy
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_ONLY', 'SPOT_ONLY', 'SPOT_PREFERRED']]


# UpdateGameServerGroupOutputTypeDef

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGameServerInputRequestTypeDef

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerId
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerData
- **Type**: typing.Optional[str]

### UtilizationStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'UTILIZED']]

### HealthCheck
- **Type**: typing.Optional[typing.Literal['HEALTHY']]


# UpdateGameServerOutputTypeDef

### GameServer
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGameSessionInputRequestTypeDef

### GameSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaximumPlayerSessionCount
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### PlayerSessionCreationPolicy
- **Type**: typing.Optional[typing.Literal['ACCEPT_ALL', 'DENY_ALL']]

### ProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]

### GameProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.GamePropertyTypeDef]]


# UpdateGameSessionOutputTypeDef

### GameSession
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGameSessionQueueInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### PlayerLatencyPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.PlayerLatencyPolicyTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.GameSessionQueueDestinationTypeDef]]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.FilterConfigurationTypeDef]

### PriorityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.PriorityConfigurationTypeDef]

### CustomEventData
- **Type**: typing.Optional[str]

### NotificationTarget
- **Type**: typing.Optional[str]


# UpdateGameSessionQueueOutputTypeDef

### GameSessionQueue
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.GameSessionQueueTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMatchmakingConfigurationInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### GameSessionQueueArns
- **Type**: typing.Optional[typing.Sequence[str]]

### RequestTimeoutSeconds
- **Type**: typing.Optional[int]

### AcceptanceTimeoutSeconds
- **Type**: typing.Optional[int]

### AcceptanceRequired
- **Type**: typing.Optional[bool]

### RuleSetName
- **Type**: typing.Optional[str]

### NotificationTarget
- **Type**: typing.Optional[str]

### AdditionalPlayerCount
- **Type**: typing.Optional[int]

### CustomEventData
- **Type**: typing.Optional[str]

### GameProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.gamelift_classes.GamePropertyTypeDef]]

### GameSessionData
- **Type**: typing.Optional[str]

### BackfillMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]

### FlexMatchMode
- **Type**: typing.Optional[typing.Literal['STANDALONE', 'WITH_QUEUE']]


# UpdateMatchmakingConfigurationOutputTypeDef

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.MatchmakingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRuntimeConfigurationInputRequestTypeDef

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### RuntimeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.RuntimeConfigurationTypeDef'>
- **Required**: Yes


# UpdateRuntimeConfigurationOutputTypeDef

### RuntimeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.RuntimeConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateScriptInputRequestTypeDef

### ScriptId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### StorageLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.S3LocationTypeDef]

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# UpdateScriptOutputTypeDef

### Script
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ScriptTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidateMatchmakingRuleSetInputRequestTypeDef

### RuleSetBody
- **Type**: <class 'str'>
- **Required**: Yes


# ValidateMatchmakingRuleSetOutputTypeDef

### Valid
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcPeeringAuthorizationTypeDef

### GameLiftAwsAccountId
- **Type**: typing.Optional[str]

### PeerVpcAwsAccountId
- **Type**: typing.Optional[str]

### PeerVpcId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTime
- **Type**: typing.Optional[datetime.datetime]


# VpcPeeringConnectionStatusTypeDef

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# VpcPeeringConnectionTypeDef

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### IpV4CidrBlock
- **Type**: typing.Optional[str]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift_classes.VpcPeeringConnectionStatusTypeDef]

### PeerVpcId
- **Type**: typing.Optional[str]

### GameLiftVpcId
- **Type**: typing.Optional[str]



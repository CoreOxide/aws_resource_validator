# Gamelift Classes

# AcceptMatchInput

### TicketId
- **Type**: <class 'str'>
- **Required**: Yes

### PlayerIds
- **Type**: typing.List[str]
- **Required**: Yes

### AcceptanceType
- **Type**: typing.Literal['ACCEPT', 'REJECT']
- **Required**: Yes


# Alias

### AliasId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### AliasArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoutingStrategy
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# AnywhereConfiguration

### Cost
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeValue

### S
- **Type**: typing.Optional[str]

### N
- **Type**: typing.Optional[float]

### SL
- **Type**: typing.Optional[typing.List[str]]

### SDM
- **Type**: typing.Optional[typing.Dict[str, float]]


# AttributeValueOutput

### S
- **Type**: typing.Optional[str]

### N
- **Type**: typing.Optional[float]

### SL
- **Type**: typing.Optional[typing.List[str]]

### SDM
- **Type**: typing.Optional[typing.Dict[str, float]]


# AwsCredentials

### AccessKeyId
- **Type**: typing.Optional[str]

### SecretAccessKey
- **Type**: typing.Optional[str]

### SessionToken
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Build

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


# CertificateConfiguration

### CertificateType
- **Type**: typing.Literal['DISABLED', 'GENERATED']
- **Required**: Yes


# ClaimFilterOption

### InstanceStatuses
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE', 'DRAINING']]]


# ClaimGameServerInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerId
- **Type**: typing.Optional[str]

### GameServerData
- **Type**: typing.Optional[str]

### FilterOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ClaimFilterOption]


# ClaimGameServerOutput

### GameServer
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# Compute

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
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'IMPAIRED', 'PENDING', 'TERMINATING']]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerAttribute]]

### GameServerContainerGroupDefinitionArn
- **Type**: typing.Optional[str]


# ConnectionPortRange

### FromPort
- **Type**: <class 'int'>
- **Required**: Yes

### ToPort
- **Type**: <class 'int'>
- **Required**: Yes


# ContainerAttribute

### ContainerName
- **Type**: typing.Optional[str]

### ContainerRuntimeId
- **Type**: typing.Optional[str]


# ContainerDependency

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['COMPLETE', 'HEALTHY', 'START', 'SUCCESS']
- **Required**: Yes


# ContainerEnvironment

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ContainerFleet

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### FleetRoleArn
- **Type**: typing.Optional[str]

### GameServerContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### GameServerContainerGroupDefinitionArn
- **Type**: typing.Optional[str]

### PerInstanceContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### PerInstanceContainerGroupDefinitionArn
- **Type**: typing.Optional[str]

### InstanceConnectionPortRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ConnectionPortRange]

### InstanceInboundPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.IpPermission]]

### GameServerContainerGroupsPerInstance
- **Type**: typing.Optional[int]

### MaximumGameServerContainerGroupsPerInstance
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[str]

### BillingType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### Description
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### MetricGroups
- **Type**: typing.Optional[typing.List[str]]

### NewGameSessionProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]

### GameSessionCreationLimitPolicy
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'CREATED', 'CREATING', 'DELETING', 'PENDING', 'UPDATING']]

### DeploymentDetails
- **Type**: <class 'NoneType'>

### LogConfiguration
- **Type**: <class 'NoneType'>

### LocationAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerFleetLocationAttributes]]


# ContainerFleetLocationAttributes

### Location
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'CREATED', 'CREATING', 'DELETING', 'PENDING', 'UPDATING']]


# ContainerGroupDefinition

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerGroupDefinitionArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX_2023']]

### ContainerGroupType
- **Type**: typing.Optional[typing.Literal['GAME_SERVER', 'PER_INSTANCE']]

### TotalMemoryLimitMebibytes
- **Type**: typing.Optional[int]

### TotalVcpuLimit
- **Type**: typing.Optional[float]

### GameServerContainerDefinition
- **Type**: <class 'NoneType'>

### SupportContainerDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.SupportContainerDefinition]]

### VersionNumber
- **Type**: typing.Optional[int]

### VersionDescription
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COPYING', 'FAILED', 'READY']]

### StatusReason
- **Type**: typing.Optional[str]


# ContainerHealthCheck

### Command
- **Type**: typing.List[str]
- **Required**: Yes

### Interval
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### StartPeriod
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]


# ContainerHealthCheckOutput

### Command
- **Type**: typing.List[str]
- **Required**: Yes

### Interval
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### StartPeriod
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]


# ContainerIdentifier

### ContainerName
- **Type**: typing.Optional[str]

### ContainerRuntimeId
- **Type**: typing.Optional[str]


# ContainerMountPoint

### InstancePath
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerPath
- **Type**: typing.Optional[str]

### AccessLevel
- **Type**: typing.Optional[typing.Literal['READ_AND_WRITE', 'READ_ONLY']]


# ContainerPortConfiguration

### ContainerPortRanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerPortRange]
- **Required**: Yes


# ContainerPortConfigurationOutput

### ContainerPortRanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerPortRange]
- **Required**: Yes


# ContainerPortRange

### FromPort
- **Type**: <class 'int'>
- **Required**: Yes

### ToPort
- **Type**: <class 'int'>
- **Required**: Yes

### Protocol
- **Type**: typing.Literal['TCP', 'UDP']
- **Required**: Yes


# CreateAliasInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.RoutingStrategy'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]


# CreateAliasOutput

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Alias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBuildInput

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### StorageLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.S3Location]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2023', 'WINDOWS_2012', 'WINDOWS_2016']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]

### ServerSdkVersion
- **Type**: typing.Optional[str]


# CreateBuildOutput

### Build
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Build'>
- **Required**: Yes

### UploadCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.AwsCredentials'>
- **Required**: Yes

### StorageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.S3Location'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContainerFleetInput

### FleetRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### GameServerContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### PerInstanceContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### InstanceConnectionPortRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ConnectionPortRange]

### InstanceInboundPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.IpPermission]]

### GameServerContainerGroupsPerInstance
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[str]

### BillingType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### Locations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationConfiguration]]

### MetricGroups
- **Type**: typing.Optional[typing.List[str]]

### NewGameSessionProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]

### GameSessionCreationLimitPolicy
- **Type**: <class 'NoneType'>

### LogConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]


# CreateContainerFleetOutput

### ContainerFleet
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerFleet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContainerGroupDefinitionInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TotalMemoryLimitMebibytes
- **Type**: <class 'int'>
- **Required**: Yes

### TotalVcpuLimit
- **Type**: <class 'float'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Literal['AMAZON_LINUX_2023']
- **Required**: Yes

### ContainerGroupType
- **Type**: typing.Optional[typing.Literal['GAME_SERVER', 'PER_INSTANCE']]

### GameServerContainerDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerContainerDefinitionInput]

### SupportContainerDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.SupportContainerDefinitionInput]]

### VersionDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]


# CreateContainerGroupDefinitionOutput

### ContainerGroupDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerGroupDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFleetInput

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
- **Type**: typing.Optional[typing.List[str]]

### EC2InstanceType
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### EC2InboundPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.IpPermission]]

### NewGameSessionProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]

### RuntimeConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.RuntimeConfiguration, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.RuntimeConfigurationOutput, NoneType]

### ResourceCreationLimitPolicy
- **Type**: <class 'NoneType'>

### MetricGroups
- **Type**: typing.Optional[typing.List[str]]

### PeerVpcAwsAccountId
- **Type**: typing.Optional[str]

### PeerVpcId
- **Type**: typing.Optional[str]

### FleetType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### InstanceRoleArn
- **Type**: typing.Optional[str]

### CertificateConfiguration
- **Type**: <class 'NoneType'>

### Locations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationConfiguration]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]

### ComputeType
- **Type**: typing.Optional[typing.Literal['ANYWHERE', 'EC2']]

### AnywhereConfiguration
- **Type**: <class 'NoneType'>

### InstanceRoleCredentialsProvider
- **Type**: typing.Optional[typing.Literal['SHARED_CREDENTIAL_FILE']]


# CreateFleetLocationsInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Locations
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationConfiguration]
- **Required**: Yes


# CreateFleetLocationsOutput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFleetOutput

### FleetAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FleetAttributes'>
- **Required**: Yes

### LocationStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGameServerGroupInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LaunchTemplateSpecification'>
- **Required**: Yes

### InstanceDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.InstanceDefinition]
- **Required**: Yes

### AutoScalingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerGroupAutoScalingPolicy]

### BalancingStrategy
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_ONLY', 'SPOT_ONLY', 'SPOT_PREFERRED']]

### GameServerProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FULL_PROTECTION', 'NO_PROTECTION']]

### VpcSubnets
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]


# CreateGameServerGroupOutput

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGameSessionInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameProperty]]

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


# CreateGameSessionOutput

### GameSession
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGameSessionQueueInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### PlayerLatencyPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerLatencyPolicy]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionQueueDestination]]

### FilterConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FilterConfiguration, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FilterConfigurationOutput, NoneType]

### PriorityConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PriorityConfiguration, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PriorityConfigurationOutput, NoneType]

### CustomEventData
- **Type**: typing.Optional[str]

### NotificationTarget
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]


# CreateGameSessionQueueOutput

### GameSessionQueue
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionQueue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationInput

### LocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]


# CreateLocationOutput

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationModel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMatchmakingConfigurationInput

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
- **Type**: typing.Optional[typing.List[str]]

### AcceptanceTimeoutSeconds
- **Type**: typing.Optional[int]

### NotificationTarget
- **Type**: typing.Optional[str]

### AdditionalPlayerCount
- **Type**: typing.Optional[int]

### CustomEventData
- **Type**: typing.Optional[str]

### GameProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameProperty]]

### GameSessionData
- **Type**: typing.Optional[str]

### BackfillMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]

### FlexMatchMode
- **Type**: typing.Optional[typing.Literal['STANDALONE', 'WITH_QUEUE']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]


# CreateMatchmakingConfigurationOutput

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.MatchmakingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMatchmakingRuleSetInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetBody
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]


# CreateMatchmakingRuleSetOutput

### RuleSet
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.MatchmakingRuleSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePlayerSessionInput

### GameSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### PlayerId
- **Type**: <class 'str'>
- **Required**: Yes

### PlayerData
- **Type**: typing.Optional[str]


# CreatePlayerSessionOutput

### PlayerSession
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePlayerSessionsInput

### GameSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### PlayerIds
- **Type**: typing.List[str]
- **Required**: Yes

### PlayerDataMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePlayerSessionsOutput

### PlayerSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerSession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScriptInput

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### StorageLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.S3Location]

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]]


# CreateScriptOutput

### Script
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Script'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcPeeringAuthorizationInput

### GameLiftAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerVpcId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateVpcPeeringAuthorizationOutput

### VpcPeeringAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.VpcPeeringAuthorization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcPeeringConnectionInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerVpcAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerVpcId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAliasInput

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBuildInput

### BuildId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerFleetInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerGroupDefinitionInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]

### VersionCountToRetain
- **Type**: typing.Optional[int]


# DeleteFleetInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFleetLocationsInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Locations
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteFleetLocationsOutput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGameServerGroupInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteOption
- **Type**: typing.Optional[typing.Literal['FORCE_DELETE', 'RETAIN', 'SAFE_DELETE']]


# DeleteGameServerGroupOutput

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGameSessionQueueInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLocationInput

### LocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMatchmakingConfigurationInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMatchmakingRuleSetInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScalingPolicyInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScriptInput

### ScriptId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcPeeringAuthorizationInput

### GameLiftAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PeerVpcId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcPeeringConnectionInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcPeeringConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeploymentConfiguration

### ProtectionStrategy
- **Type**: typing.Optional[typing.Literal['IGNORE_PROTECTION', 'WITH_PROTECTION']]

### MinimumHealthyPercentage
- **Type**: typing.Optional[int]

### ImpairmentStrategy
- **Type**: typing.Optional[typing.Literal['MAINTAIN', 'ROLLBACK']]


# DeploymentDetails

### LatestDeploymentId
- **Type**: typing.Optional[str]


# DeregisterComputeInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterGameServerInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAliasInput

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAliasOutput

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Alias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBuildInput

### BuildId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBuildOutput

### Build
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Build'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeComputeInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeComputeOutput

### Compute
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Compute'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeContainerFleetInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContainerFleetOutput

### ContainerFleet
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerFleet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeContainerGroupDefinitionInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DescribeContainerGroupDefinitionOutput

### ContainerGroupDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerGroupDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEC2InstanceLimitsInput

### EC2InstanceType
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### Location
- **Type**: typing.Optional[str]


# DescribeEC2InstanceLimitsOutput

### EC2InstanceLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.EC2InstanceLimit]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFleetAttributesInput

### FleetIds
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAttributesInputPaginate

### FleetIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeFleetAttributesOutput

### FleetAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FleetAttributes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetCapacityInput

### FleetIds
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetCapacityInputPaginate

### FleetIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeFleetCapacityOutput

### FleetCapacity
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FleetCapacity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetDeploymentInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: typing.Optional[str]


# DescribeFleetDeploymentOutput

### FleetDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FleetDeployment'>
- **Required**: Yes

### LocationalDeployments
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationalDeployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFleetEventsInput

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


# DescribeFleetEventsInputPaginate

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeFleetEventsOutput

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetLocationAttributesInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Locations
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetLocationAttributesOutput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationAttributes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetLocationCapacityInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFleetLocationCapacityOutput

### FleetCapacity
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FleetCapacity'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFleetLocationUtilizationInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFleetLocationUtilizationOutput

### FleetUtilization
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FleetUtilization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFleetPortSettingsInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]


# DescribeFleetPortSettingsOutput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### InboundPermissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.IpPermission]
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Literal['PENDING_UPDATE']
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFleetUtilizationInput

### FleetIds
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetUtilizationInputPaginate

### FleetIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeFleetUtilizationOutput

### FleetUtilization
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FleetUtilization]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameServerGroupInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGameServerGroupOutput

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGameServerInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGameServerInstancesInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameServerInstancesInputPaginate

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeGameServerInstancesOutput

### GameServerInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameServerOutput

### GameServer
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGameSessionDetailsInput

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


# DescribeGameSessionDetailsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeGameSessionDetailsOutput

### GameSessionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameSessionPlacementInput

### PlacementId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGameSessionPlacementOutput

### GameSessionPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionPlacement'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGameSessionQueuesInput

### Names
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameSessionQueuesInputPaginate

### Names
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeGameSessionQueuesOutput

### GameSessionQueues
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionQueue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGameSessionsInput

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


# DescribeGameSessionsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeGameSessionsOutput

### GameSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancesInput

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


# DescribeInstancesInputPaginate

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeInstancesOutput

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Instance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMatchmakingConfigurationsInput

### Names
- **Type**: typing.Optional[typing.List[str]]

### RuleSetName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMatchmakingConfigurationsInputPaginate

### Names
- **Type**: typing.Optional[typing.List[str]]

### RuleSetName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeMatchmakingConfigurationsOutput

### Configurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.MatchmakingConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMatchmakingInput

### TicketIds
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeMatchmakingOutput

### TicketList
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.MatchmakingTicket]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMatchmakingRuleSetsInput

### Names
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMatchmakingRuleSetsInputPaginate

### Names
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeMatchmakingRuleSetsOutput

### RuleSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.MatchmakingRuleSet]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePlayerSessionsInput

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


# DescribePlayerSessionsInputPaginate

### GameSessionId
- **Type**: typing.Optional[str]

### PlayerId
- **Type**: typing.Optional[str]

### PlayerSessionId
- **Type**: typing.Optional[str]

### PlayerSessionStatusFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribePlayerSessionsOutput

### PlayerSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerSession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRuntimeConfigurationInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRuntimeConfigurationOutput

### RuntimeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.RuntimeConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeScalingPoliciesInput

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


# DescribeScalingPoliciesInputPaginate

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### StatusFilter
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETE_REQUESTED', 'DELETING', 'ERROR', 'UPDATE_REQUESTED', 'UPDATING']]

### Location
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# DescribeScalingPoliciesOutput

### ScalingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ScalingPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeScriptInput

### ScriptId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScriptOutput

### Script
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Script'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVpcPeeringAuthorizationsOutput

### VpcPeeringAuthorizations
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.VpcPeeringAuthorization]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVpcPeeringConnectionsInput

### FleetId
- **Type**: typing.Optional[str]


# DescribeVpcPeeringConnectionsOutput

### VpcPeeringConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.VpcPeeringConnection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# DesiredPlayerSession

### PlayerId
- **Type**: typing.Optional[str]

### PlayerData
- **Type**: typing.Optional[str]


# EC2InstanceCounts

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


# EC2InstanceLimit

### EC2InstanceType
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### CurrentInstances
- **Type**: typing.Optional[int]

### InstanceLimit
- **Type**: typing.Optional[int]

### Location
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# Event

### EventId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### EventCode
- **Type**: typing.Optional[typing.Literal['COMPUTE_LOG_UPLOAD_FAILED', 'FLEET_ACTIVATION_FAILED', 'FLEET_ACTIVATION_FAILED_NO_INSTANCES', 'FLEET_BINARY_DOWNLOAD_FAILED', 'FLEET_CREATED', 'FLEET_CREATION_COMPLETED_INSTALLER', 'FLEET_CREATION_EXTRACTING_BUILD', 'FLEET_CREATION_FAILED_INSTALLER', 'FLEET_CREATION_RUNNING_INSTALLER', 'FLEET_CREATION_VALIDATING_RUNTIME_CONFIG', 'FLEET_DELETED', 'FLEET_INITIALIZATION_FAILED', 'FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED', 'FLEET_SCALING_EVENT', 'FLEET_STATE_ACTIVATING', 'FLEET_STATE_ACTIVE', 'FLEET_STATE_BUILDING', 'FLEET_STATE_CREATED', 'FLEET_STATE_CREATING', 'FLEET_STATE_DOWNLOADING', 'FLEET_STATE_ERROR', 'FLEET_STATE_PENDING', 'FLEET_STATE_UPDATING', 'FLEET_STATE_VALIDATING', 'FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE', 'FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND', 'FLEET_VALIDATION_TIMED_OUT', 'FLEET_VPC_PEERING_DELETED', 'FLEET_VPC_PEERING_FAILED', 'FLEET_VPC_PEERING_SUCCEEDED', 'GAME_SERVER_CONTAINER_GROUP_CRASHED', 'GAME_SERVER_CONTAINER_GROUP_REPLACED_UNHEALTHY', 'GAME_SESSION_ACTIVATION_TIMEOUT', 'GENERIC_EVENT', 'INSTANCE_INTERRUPTED', 'INSTANCE_RECYCLED', 'INSTANCE_REPLACED_UNHEALTHY', 'LOCATION_STATE_ACTIVATING', 'LOCATION_STATE_ACTIVE', 'LOCATION_STATE_CREATED', 'LOCATION_STATE_CREATING', 'LOCATION_STATE_DELETED', 'LOCATION_STATE_DELETING', 'LOCATION_STATE_ERROR', 'LOCATION_STATE_PENDING', 'LOCATION_STATE_UPDATING', 'PER_INSTANCE_CONTAINER_GROUP_CRASHED', 'SERVER_PROCESS_CRASHED', 'SERVER_PROCESS_FORCE_TERMINATED', 'SERVER_PROCESS_INVALID_PATH', 'SERVER_PROCESS_MISCONFIGURED_CONTAINER_PORT', 'SERVER_PROCESS_PROCESS_EXIT_TIMEOUT', 'SERVER_PROCESS_PROCESS_READY_TIMEOUT', 'SERVER_PROCESS_SDK_INITIALIZATION_FAILED', 'SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT', 'SERVER_PROCESS_TERMINATED_UNHEALTHY']]

### Message
- **Type**: typing.Optional[str]

### EventTime
- **Type**: typing.Optional[datetime.datetime]

### PreSignedLogUrl
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]


# FilterConfiguration

### AllowedLocations
- **Type**: typing.Optional[typing.List[str]]


# FilterConfigurationOutput

### AllowedLocations
- **Type**: typing.Optional[typing.List[str]]


# FleetAttributes

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
- **Type**: <class 'NoneType'>

### MetricGroups
- **Type**: typing.Optional[typing.List[str]]

### StoppedActions
- **Type**: typing.Optional[typing.List[typing.Literal['AUTO_SCALING']]]

### InstanceRoleArn
- **Type**: typing.Optional[str]

### CertificateConfiguration
- **Type**: <class 'NoneType'>

### ComputeType
- **Type**: typing.Optional[typing.Literal['ANYWHERE', 'EC2']]

### AnywhereConfiguration
- **Type**: <class 'NoneType'>

### InstanceRoleCredentialsProvider
- **Type**: typing.Optional[typing.Literal['SHARED_CREDENTIAL_FILE']]


# FleetCapacity

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c3.large', 'c3.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c5d.12xlarge', 'c5d.18xlarge', 'c5d.24xlarge', 'c5d.2xlarge', 'c5d.4xlarge', 'c5d.9xlarge', 'c5d.large', 'c5d.xlarge', 'c6a.12xlarge', 'c6a.16xlarge', 'c6a.24xlarge', 'c6a.2xlarge', 'c6a.4xlarge', 'c6a.8xlarge', 'c6a.large', 'c6a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'c6gn.12xlarge', 'c6gn.16xlarge', 'c6gn.2xlarge', 'c6gn.4xlarge', 'c6gn.8xlarge', 'c6gn.large', 'c6gn.medium', 'c6gn.xlarge', 'c6i.12xlarge', 'c6i.16xlarge', 'c6i.24xlarge', 'c6i.2xlarge', 'c6i.4xlarge', 'c6i.8xlarge', 'c6i.large', 'c6i.xlarge', 'c7g.12xlarge', 'c7g.16xlarge', 'c7g.2xlarge', 'c7g.4xlarge', 'c7g.8xlarge', 'c7g.large', 'c7g.medium', 'c7g.xlarge', 'g5g.16xlarge', 'g5g.2xlarge', 'g5g.4xlarge', 'g5g.8xlarge', 'g5g.xlarge', 'm3.2xlarge', 'm3.large', 'm3.medium', 'm3.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'm7g.12xlarge', 'm7g.16xlarge', 'm7g.2xlarge', 'm7g.4xlarge', 'm7g.8xlarge', 'm7g.large', 'm7g.medium', 'm7g.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r3.large', 'r3.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r5d.12xlarge', 'r5d.16xlarge', 'r5d.24xlarge', 'r5d.2xlarge', 'r5d.4xlarge', 'r5d.8xlarge', 'r5d.large', 'r5d.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge', 'r7g.12xlarge', 'r7g.16xlarge', 'r7g.2xlarge', 'r7g.4xlarge', 'r7g.8xlarge', 'r7g.large', 'r7g.medium', 'r7g.xlarge', 't2.large', 't2.medium', 't2.micro', 't2.small']]

### InstanceCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.EC2InstanceCounts]

### Location
- **Type**: typing.Optional[str]

### GameServerContainerGroupCounts
- **Type**: <class 'NoneType'>


# FleetDeployment

### DeploymentId
- **Type**: typing.Optional[str]

### FleetId
- **Type**: typing.Optional[str]

### GameServerBinaryArn
- **Type**: typing.Optional[str]

### RollbackGameServerBinaryArn
- **Type**: typing.Optional[str]

### PerInstanceBinaryArn
- **Type**: typing.Optional[str]

### RollbackPerInstanceBinaryArn
- **Type**: typing.Optional[str]

### DeploymentStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETE', 'IMPAIRED', 'IN_PROGRESS', 'PENDING', 'ROLLBACK_COMPLETE', 'ROLLBACK_IN_PROGRESS']]

### DeploymentConfiguration
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# FleetUtilization

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


# GameProperty

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# GameServer

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


# GameServerContainerDefinition

### ContainerName
- **Type**: typing.Optional[str]

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerDependency]]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerMountPoint]]

### EnvironmentOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerEnvironment]]

### ImageUri
- **Type**: typing.Optional[str]

### PortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerPortConfigurationOutput]

### ResolvedImageDigest
- **Type**: typing.Optional[str]

### ServerSdkVersion
- **Type**: typing.Optional[str]


# GameServerContainerDefinitionInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### PortConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerPortConfiguration, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerPortConfigurationOutput]
- **Required**: Yes

### ServerSdkVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerDependency]]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerMountPoint]]

### EnvironmentOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerEnvironment]]


# GameServerContainerGroupCounts

### PENDING
- **Type**: typing.Optional[int]

### ACTIVE
- **Type**: typing.Optional[int]

### IDLE
- **Type**: typing.Optional[int]

### TERMINATING
- **Type**: typing.Optional[int]


# GameServerGroup

### GameServerGroupName
- **Type**: typing.Optional[str]

### GameServerGroupArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### InstanceDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.InstanceDefinition]]

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


# GameServerGroupAutoScalingPolicy

### TargetTrackingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.TargetTrackingConfiguration'>
- **Required**: Yes

### EstimatedInstanceWarmup
- **Type**: typing.Optional[int]


# GameServerInstance

### GameServerGroupName
- **Type**: typing.Optional[str]

### GameServerGroupArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAINING', 'SPOT_TERMINATING']]


# GameSession

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
- **Type**: typing.Optional[typing.Literal['FORCE_TERMINATED', 'INTERRUPTED', 'TRIGGERED_ON_PROCESS_TERMINATE']]

### GameProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameProperty]]

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


# GameSessionConnectionInfo

### GameSessionArn
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MatchedPlayerSessions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.MatchedPlayerSession]]


# GameSessionCreationLimitPolicy

### NewGameSessionsPerCreator
- **Type**: typing.Optional[int]

### PolicyPeriodInMinutes
- **Type**: typing.Optional[int]


# GameSessionDetail

### GameSession
- **Type**: <class 'NoneType'>

### ProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]


# GameSessionPlacement

### PlacementId
- **Type**: typing.Optional[str]

### GameSessionQueueName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'FULFILLED', 'PENDING', 'TIMED_OUT']]

### GameProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameProperty]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerLatency]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlacedPlayerSession]]

### GameSessionData
- **Type**: typing.Optional[str]

### MatchmakerData
- **Type**: typing.Optional[str]

### PriorityConfigurationOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PriorityConfigurationOverrideOutput]


# GameSessionQueue

### Name
- **Type**: typing.Optional[str]

### GameSessionQueueArn
- **Type**: typing.Optional[str]

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### PlayerLatencyPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerLatencyPolicy]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionQueueDestination]]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FilterConfigurationOutput]

### PriorityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PriorityConfigurationOutput]

### CustomEventData
- **Type**: typing.Optional[str]

### NotificationTarget
- **Type**: typing.Optional[str]


# GameSessionQueueDestination

### DestinationArn
- **Type**: typing.Optional[str]


# GetComputeAccessInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetComputeAccessOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.AwsCredentials'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# GetComputeAuthTokenInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetComputeAuthTokenOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# GetGameSessionLogUrlInput

### GameSessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGameSessionLogUrlOutput

### PreSignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceAccessInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceAccessOutput

### InstanceAccess
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.InstanceAccess'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# Instance

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


# InstanceAccess

### FleetId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2023', 'WINDOWS_2012', 'WINDOWS_2016']]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.InstanceCredentials]


# InstanceCredentials

### UserName
- **Type**: typing.Optional[str]

### Secret
- **Type**: typing.Optional[str]


# InstanceDefinition

### InstanceType
- **Type**: typing.Literal['c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'c4.large', 'c4.xlarge', 'c5.12xlarge', 'c5.18xlarge', 'c5.24xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.large', 'c5.xlarge', 'c5a.12xlarge', 'c5a.16xlarge', 'c5a.24xlarge', 'c5a.2xlarge', 'c5a.4xlarge', 'c5a.8xlarge', 'c5a.large', 'c5a.xlarge', 'c6g.12xlarge', 'c6g.16xlarge', 'c6g.2xlarge', 'c6g.4xlarge', 'c6g.8xlarge', 'c6g.large', 'c6g.medium', 'c6g.xlarge', 'm4.10xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.large', 'm4.xlarge', 'm5.12xlarge', 'm5.16xlarge', 'm5.24xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.8xlarge', 'm5.large', 'm5.xlarge', 'm5a.12xlarge', 'm5a.16xlarge', 'm5a.24xlarge', 'm5a.2xlarge', 'm5a.4xlarge', 'm5a.8xlarge', 'm5a.large', 'm5a.xlarge', 'm6g.12xlarge', 'm6g.16xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'm6g.8xlarge', 'm6g.large', 'm6g.medium', 'm6g.xlarge', 'r4.16xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.large', 'r4.xlarge', 'r5.12xlarge', 'r5.16xlarge', 'r5.24xlarge', 'r5.2xlarge', 'r5.4xlarge', 'r5.8xlarge', 'r5.large', 'r5.xlarge', 'r5a.12xlarge', 'r5a.16xlarge', 'r5a.24xlarge', 'r5a.2xlarge', 'r5a.4xlarge', 'r5a.8xlarge', 'r5a.large', 'r5a.xlarge', 'r6g.12xlarge', 'r6g.16xlarge', 'r6g.2xlarge', 'r6g.4xlarge', 'r6g.8xlarge', 'r6g.large', 'r6g.medium', 'r6g.xlarge']
- **Required**: Yes

### WeightedCapacity
- **Type**: typing.Optional[str]


# IpPermission

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


# LaunchTemplateSpecification

### LaunchTemplateId
- **Type**: typing.Optional[str]

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# ListAliasesInput

### RoutingStrategyType
- **Type**: typing.Optional[typing.Literal['SIMPLE', 'TERMINAL']]

### Name
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAliasesInputPaginate

### RoutingStrategyType
- **Type**: typing.Optional[typing.Literal['SIMPLE', 'TERMINAL']]

### Name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListAliasesOutput

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Alias]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBuildsInput

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'READY']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBuildsInputPaginate

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'READY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListBuildsOutput

### Builds
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Build]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComputeInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]

### ContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### ComputeStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'IMPAIRED']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListComputeInputPaginate

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]

### ContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### ComputeStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'IMPAIRED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListComputeOutput

### ComputeList
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Compute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContainerFleetsInput

### ContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListContainerFleetsInputPaginate

### ContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListContainerFleetsOutput

### ContainerFleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerFleet]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContainerGroupDefinitionVersionsInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListContainerGroupDefinitionVersionsInputPaginate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListContainerGroupDefinitionVersionsOutput

### ContainerGroupDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerGroupDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContainerGroupDefinitionsInput

### ContainerGroupType
- **Type**: typing.Optional[typing.Literal['GAME_SERVER', 'PER_INSTANCE']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListContainerGroupDefinitionsInputPaginate

### ContainerGroupType
- **Type**: typing.Optional[typing.Literal['GAME_SERVER', 'PER_INSTANCE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListContainerGroupDefinitionsOutput

### ContainerGroupDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerGroupDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFleetDeploymentsInput

### FleetId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFleetDeploymentsInputPaginate

### FleetId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListFleetDeploymentsOutput

### FleetDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FleetDeployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFleetsInput

### BuildId
- **Type**: typing.Optional[str]

### ScriptId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFleetsInputPaginate

### BuildId
- **Type**: typing.Optional[str]

### ScriptId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListFleetsOutput

### FleetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGameServerGroupsInput

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGameServerGroupsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListGameServerGroupsOutput

### GameServerGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGameServersInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGameServersInputPaginate

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListGameServersOutput

### GameServers
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLocationsInput

### Filters
- **Type**: typing.Optional[typing.List[typing.Literal['AWS', 'CUSTOM']]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLocationsInputPaginate

### Filters
- **Type**: typing.Optional[typing.List[typing.Literal['AWS', 'CUSTOM']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListLocationsOutput

### Locations
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.LocationModel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListScriptsInput

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListScriptsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# ListScriptsOutput

### Scripts
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Script]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# LocationAttributes

### LocationState
- **Type**: <class 'NoneType'>

### StoppedActions
- **Type**: typing.Optional[typing.List[typing.Literal['AUTO_SCALING']]]

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['PENDING_UPDATE']]


# LocationConfiguration

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# LocationModel

### LocationName
- **Type**: typing.Optional[str]

### LocationArn
- **Type**: typing.Optional[str]


# LocationState

### Location
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'BUILDING', 'DELETING', 'DOWNLOADING', 'ERROR', 'NEW', 'NOT_FOUND', 'TERMINATED', 'VALIDATING']]


# LocationalDeployment

### DeploymentStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETE', 'IMPAIRED', 'IN_PROGRESS', 'PENDING', 'ROLLBACK_COMPLETE', 'ROLLBACK_IN_PROGRESS']]


# LogConfiguration

### LogDestination
- **Type**: typing.Optional[typing.Literal['CLOUDWATCH', 'NONE', 'S3']]

### S3BucketName
- **Type**: typing.Optional[str]

### LogGroupArn
- **Type**: typing.Optional[str]


# MatchedPlayerSession

### PlayerId
- **Type**: typing.Optional[str]

### PlayerSessionId
- **Type**: typing.Optional[str]


# MatchmakingConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameProperty]]

### GameSessionData
- **Type**: typing.Optional[str]

### BackfillMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]

### FlexMatchMode
- **Type**: typing.Optional[typing.Literal['STANDALONE', 'WITH_QUEUE']]


# MatchmakingRuleSet

### RuleSetBody
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetName
- **Type**: typing.Optional[str]

### RuleSetArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# MatchmakingTicket

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerOutput]]

### GameSessionConnectionInfo
- **Type**: <class 'NoneType'>

### EstimatedWaitTime
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlacedPlayerSession

### PlayerId
- **Type**: typing.Optional[str]

### PlayerSessionId
- **Type**: typing.Optional[str]


# Player

### PlayerId
- **Type**: typing.Optional[str]

### PlayerAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.AttributeValue, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.AttributeValueOutput]]]

### Team
- **Type**: typing.Optional[str]

### LatencyInMs
- **Type**: typing.Optional[typing.Dict[str, int]]


# PlayerLatency

### PlayerId
- **Type**: typing.Optional[str]

### RegionIdentifier
- **Type**: typing.Optional[str]

### LatencyInMilliseconds
- **Type**: typing.Optional[float]


# PlayerLatencyPolicy

### MaximumIndividualPlayerLatencyMilliseconds
- **Type**: typing.Optional[int]

### PolicyDurationSeconds
- **Type**: typing.Optional[int]


# PlayerOutput

### PlayerId
- **Type**: typing.Optional[str]

### PlayerAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.AttributeValueOutput]]

### Team
- **Type**: typing.Optional[str]

### LatencyInMs
- **Type**: typing.Optional[typing.Dict[str, int]]


# PlayerSession

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


# PriorityConfiguration

### PriorityOrder
- **Type**: typing.Optional[typing.List[typing.Literal['COST', 'DESTINATION', 'LATENCY', 'LOCATION']]]

### LocationOrder
- **Type**: typing.Optional[typing.List[str]]


# PriorityConfigurationOutput

### PriorityOrder
- **Type**: typing.Optional[typing.List[typing.Literal['COST', 'DESTINATION', 'LATENCY', 'LOCATION']]]

### LocationOrder
- **Type**: typing.Optional[typing.List[str]]


# PriorityConfigurationOverride

### LocationOrder
- **Type**: typing.List[str]
- **Required**: Yes

### PlacementFallbackStrategy
- **Type**: typing.Optional[typing.Literal['DEFAULT_AFTER_SINGLE_PASS', 'NONE']]


# PriorityConfigurationOverrideOutput

### LocationOrder
- **Type**: typing.List[str]
- **Required**: Yes

### PlacementFallbackStrategy
- **Type**: typing.Optional[typing.Literal['DEFAULT_AFTER_SINGLE_PASS', 'NONE']]


# PutScalingPolicyInput

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
- **Type**: <class 'NoneType'>


# PutScalingPolicyOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterComputeInput

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


# RegisterComputeOutput

### Compute
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Compute'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterGameServerInput

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


# RegisterGameServerOutput

### GameServer
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# RequestUploadCredentialsInput

### BuildId
- **Type**: <class 'str'>
- **Required**: Yes


# RequestUploadCredentialsOutput

### UploadCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.AwsCredentials'>
- **Required**: Yes

### StorageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.S3Location'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# ResolveAliasInput

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# ResolveAliasOutput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceCreationLimitPolicy

### NewGameSessionsPerCreator
- **Type**: typing.Optional[int]

### PolicyPeriodInMinutes
- **Type**: typing.Optional[int]


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


# ResumeGameServerGroupInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResumeActions
- **Type**: typing.List[typing.Literal['REPLACE_INSTANCE_TYPES']]
- **Required**: Yes


# ResumeGameServerGroupOutput

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# RoutingStrategy

### Type
- **Type**: typing.Optional[typing.Literal['SIMPLE', 'TERMINAL']]

### FleetId
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# RuntimeConfiguration

### ServerProcesses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ServerProcess]]

### MaxConcurrentGameSessionActivations
- **Type**: typing.Optional[int]

### GameSessionActivationTimeoutSeconds
- **Type**: typing.Optional[int]


# RuntimeConfigurationOutput

### ServerProcesses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ServerProcess]]

### MaxConcurrentGameSessionActivations
- **Type**: typing.Optional[int]

### GameSessionActivationTimeoutSeconds
- **Type**: typing.Optional[int]


# S3Location

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ObjectVersion
- **Type**: typing.Optional[str]


# ScalingPolicy

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
- **Type**: <class 'NoneType'>

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['PENDING_UPDATE']]

### Location
- **Type**: typing.Optional[str]


# Script

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.S3Location]


# SearchGameSessionsInput

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


# SearchGameSessionsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PaginatorConfig]


# SearchGameSessionsOutput

### GameSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ServerProcess

### LaunchPath
- **Type**: <class 'str'>
- **Required**: Yes

### ConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[str]


# StartFleetActionsInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.List[typing.Literal['AUTO_SCALING']]
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]


# StartFleetActionsOutput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# StartGameSessionPlacementInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameProperty]]

### GameSessionName
- **Type**: typing.Optional[str]

### PlayerLatencies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerLatency]]

### DesiredPlayerSessions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.DesiredPlayerSession]]

### GameSessionData
- **Type**: typing.Optional[str]

### PriorityConfigurationOverride
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PriorityConfigurationOverride, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PriorityConfigurationOverrideOutput, NoneType]


# StartGameSessionPlacementOutput

### GameSessionPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionPlacement'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# StartMatchBackfillInput

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Players
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Player, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerOutput]]
- **Required**: Yes

### TicketId
- **Type**: typing.Optional[str]

### GameSessionArn
- **Type**: typing.Optional[str]


# StartMatchBackfillOutput

### MatchmakingTicket
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.MatchmakingTicket'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# StartMatchmakingInput

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Players
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Player, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerOutput]]
- **Required**: Yes

### TicketId
- **Type**: typing.Optional[str]


# StartMatchmakingOutput

### MatchmakingTicket
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.MatchmakingTicket'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# StopFleetActionsInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.List[typing.Literal['AUTO_SCALING']]
- **Required**: Yes

### Location
- **Type**: typing.Optional[str]


# StopFleetActionsOutput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# StopGameSessionPlacementInput

### PlacementId
- **Type**: <class 'str'>
- **Required**: Yes


# StopGameSessionPlacementOutput

### GameSessionPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionPlacement'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# StopMatchmakingInput

### TicketId
- **Type**: <class 'str'>
- **Required**: Yes


# SupportContainerDefinition

### ContainerName
- **Type**: typing.Optional[str]

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerDependency]]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerMountPoint]]

### EnvironmentOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerEnvironment]]

### Essential
- **Type**: typing.Optional[bool]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerHealthCheckOutput]

### ImageUri
- **Type**: typing.Optional[str]

### MemoryHardLimitMebibytes
- **Type**: typing.Optional[int]

### PortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerPortConfigurationOutput]

### ResolvedImageDigest
- **Type**: typing.Optional[str]

### Vcpu
- **Type**: typing.Optional[float]


# SupportContainerDefinitionInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerDependency]]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerMountPoint]]

### EnvironmentOverride
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerEnvironment]]

### Essential
- **Type**: typing.Optional[bool]

### HealthCheck
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerHealthCheck, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerHealthCheckOutput, NoneType]

### MemoryHardLimitMebibytes
- **Type**: typing.Optional[int]

### PortConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerPortConfiguration, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerPortConfigurationOutput, NoneType]

### Vcpu
- **Type**: typing.Optional[float]


# SuspendGameServerGroupInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SuspendActions
- **Type**: typing.List[typing.Literal['REPLACE_INSTANCE_TYPES']]
- **Required**: Yes


# SuspendGameServerGroupOutput

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Tag]
- **Required**: Yes


# TargetConfiguration

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes


# TargetTrackingConfiguration

### TargetValue
- **Type**: <class 'float'>
- **Required**: Yes


# TerminateGameSessionInput

### GameSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### TerminationMode
- **Type**: typing.Literal['FORCE_TERMINATE', 'TRIGGER_ON_PROCESS_TERMINATE']
- **Required**: Yes


# TerminateGameSessionOutput

### GameSession
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAliasInput

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoutingStrategy
- **Type**: <class 'NoneType'>


# UpdateAliasOutput

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Alias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBuildInput

### BuildId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# UpdateBuildOutput

### Build
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Build'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateContainerFleetInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### PerInstanceContainerGroupDefinitionName
- **Type**: typing.Optional[str]

### GameServerContainerGroupsPerInstance
- **Type**: typing.Optional[int]

### InstanceConnectionPortRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ConnectionPortRange]

### InstanceInboundPermissionAuthorizations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.IpPermission]]

### InstanceInboundPermissionRevocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.IpPermission]]

### DeploymentConfiguration
- **Type**: <class 'NoneType'>

### Description
- **Type**: typing.Optional[str]

### MetricGroups
- **Type**: typing.Optional[typing.List[str]]

### NewGameSessionProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FullProtection', 'NoProtection']]

### GameSessionCreationLimitPolicy
- **Type**: <class 'NoneType'>

### LogConfiguration
- **Type**: <class 'NoneType'>

### RemoveAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['PER_INSTANCE_CONTAINER_GROUP_DEFINITION']]]


# UpdateContainerFleetOutput

### ContainerFleet
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerFleet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateContainerGroupDefinitionInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### GameServerContainerDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerContainerDefinitionInput]

### SupportContainerDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.SupportContainerDefinitionInput]]

### TotalMemoryLimitMebibytes
- **Type**: typing.Optional[int]

### TotalVcpuLimit
- **Type**: typing.Optional[float]

### VersionDescription
- **Type**: typing.Optional[str]

### SourceVersionNumber
- **Type**: typing.Optional[int]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX_2023']]


# UpdateContainerGroupDefinitionOutput

### ContainerGroupDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ContainerGroupDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFleetAttributesInput

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
- **Type**: <class 'NoneType'>

### MetricGroups
- **Type**: typing.Optional[typing.List[str]]

### AnywhereConfiguration
- **Type**: <class 'NoneType'>


# UpdateFleetAttributesOutput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFleetCapacityInput

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


# UpdateFleetCapacityOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFleetPortSettingsInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### InboundPermissionAuthorizations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.IpPermission]]

### InboundPermissionRevocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.IpPermission]]


# UpdateFleetPortSettingsOutput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### FleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGameServerGroupInput

### GameServerGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### InstanceDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.InstanceDefinition]]

### GameServerProtectionPolicy
- **Type**: typing.Optional[typing.Literal['FULL_PROTECTION', 'NO_PROTECTION']]

### BalancingStrategy
- **Type**: typing.Optional[typing.Literal['ON_DEMAND_ONLY', 'SPOT_ONLY', 'SPOT_PREFERRED']]


# UpdateGameServerGroupOutput

### GameServerGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServerGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGameServerInput

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


# UpdateGameServerOutput

### GameServer
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameServer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGameSessionInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameProperty]]


# UpdateGameSessionOutput

### GameSession
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGameSessionQueueInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TimeoutInSeconds
- **Type**: typing.Optional[int]

### PlayerLatencyPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PlayerLatencyPolicy]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionQueueDestination]]

### FilterConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FilterConfiguration, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.FilterConfigurationOutput, NoneType]

### PriorityConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PriorityConfiguration, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.PriorityConfigurationOutput, NoneType]

### CustomEventData
- **Type**: typing.Optional[str]

### NotificationTarget
- **Type**: typing.Optional[str]


# UpdateGameSessionQueueOutput

### GameSessionQueue
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameSessionQueue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMatchmakingConfigurationInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

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

### NotificationTarget
- **Type**: typing.Optional[str]

### AdditionalPlayerCount
- **Type**: typing.Optional[int]

### CustomEventData
- **Type**: typing.Optional[str]

### GameProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.GameProperty]]

### GameSessionData
- **Type**: typing.Optional[str]

### BackfillMode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]

### FlexMatchMode
- **Type**: typing.Optional[typing.Literal['STANDALONE', 'WITH_QUEUE']]


# UpdateMatchmakingConfigurationOutput

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.MatchmakingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRuntimeConfigurationInput

### FleetId
- **Type**: <class 'str'>
- **Required**: Yes

### RuntimeConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.RuntimeConfiguration, aws_resource_validator.pydantic_models.gamelift.gamelift_classes.RuntimeConfigurationOutput]
- **Required**: Yes


# UpdateRuntimeConfigurationOutput

### RuntimeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.RuntimeConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScriptInput

### ScriptId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### StorageLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.S3Location]

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# UpdateScriptOutput

### Script
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.Script'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# ValidateMatchmakingRuleSetInput

### RuleSetBody
- **Type**: <class 'str'>
- **Required**: Yes


# ValidateMatchmakingRuleSetOutput

### Valid
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.gamelift.gamelift_classes.ResponseMetadata'>
- **Required**: Yes


# VpcPeeringAuthorization

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


# VpcPeeringConnection

### FleetId
- **Type**: typing.Optional[str]

### FleetArn
- **Type**: typing.Optional[str]

### IpV4CidrBlock
- **Type**: typing.Optional[str]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.gamelift.gamelift_classes.VpcPeeringConnectionStatus]

### PeerVpcId
- **Type**: typing.Optional[str]

### GameLiftVpcId
- **Type**: typing.Optional[str]


# VpcPeeringConnectionStatus

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]



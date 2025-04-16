# Elasticache Classes

# AddTagsToResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]
- **Required**: Yes


# AllowedNodeTypeModificationsMessage

### ScaleUpModifications
- **Type**: typing.List[str]
- **Required**: Yes

### ScaleDownModifications
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# Authentication

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuthenticationMode

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuthorizeCacheSecurityGroupIngressMessage

### CacheSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EC2SecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EC2SecurityGroupOwnerId
- **Type**: <class 'str'>
- **Required**: Yes


# AuthorizeCacheSecurityGroupIngressResult

### CacheSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# AvailabilityZone

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchApplyUpdateActionMessage

### ServiceUpdateName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### CacheClusterIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchStopUpdateActionMessage

### ServiceUpdateName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### CacheClusterIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CacheCluster

### CacheClusterId
- **Type**: typing.Optional[str]

### ConfigurationEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Endpoint]

### ClientDownloadLandingPage
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheClusterStatus
- **Type**: typing.Optional[str]

### NumCacheNodes
- **Type**: typing.Optional[int]

### PreferredAvailabilityZone
- **Type**: typing.Optional[str]

### PreferredOutpostArn
- **Type**: typing.Optional[str]

### CacheClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: <class 'NoneType'>

### NotificationConfiguration
- **Type**: <class 'NoneType'>

### CacheSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroupMembership]]

### CacheParameterGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.CacheParameterGroupStatus]

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### CacheNodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheNode]]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.SecurityGroupMembership]]

### ReplicationGroupId
- **Type**: typing.Optional[str]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### SnapshotWindow
- **Type**: typing.Optional[str]

### AuthTokenEnabled
- **Type**: typing.Optional[bool]

### AuthTokenLastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### AtRestEncryptionEnabled
- **Type**: typing.Optional[bool]

### ARN
- **Type**: typing.Optional[str]

### ReplicationGroupLogDeliveryEnabled
- **Type**: typing.Optional[bool]

### LogDeliveryConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfiguration]]

### NetworkType
- **Type**: typing.Optional[typing.Literal['dual_stack', 'ipv4', 'ipv6']]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]


# CacheClusterMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CacheEngineVersion

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheParameterGroupFamily
- **Type**: typing.Optional[str]

### CacheEngineDescription
- **Type**: typing.Optional[str]

### CacheEngineVersionDescription
- **Type**: typing.Optional[str]


# CacheEngineVersionMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheEngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheEngineVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CacheNode

### CacheNodeId
- **Type**: typing.Optional[str]

### CacheNodeStatus
- **Type**: typing.Optional[str]

### CacheNodeCreateTime
- **Type**: typing.Optional[datetime.datetime]

### Endpoint
- **Type**: <class 'NoneType'>

### ParameterGroupStatus
- **Type**: typing.Optional[str]

### SourceCacheNodeId
- **Type**: typing.Optional[str]

### CustomerAvailabilityZone
- **Type**: typing.Optional[str]

### CustomerOutpostArn
- **Type**: typing.Optional[str]


# CacheNodeTypeSpecificParameter

### ParameterName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]

### IsModifiable
- **Type**: typing.Optional[bool]

### MinimumEngineVersion
- **Type**: typing.Optional[str]

### CacheNodeTypeSpecificValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheNodeTypeSpecificValue]]

### ChangeType
- **Type**: typing.Optional[typing.Literal['immediate', 'requires-reboot']]


# CacheNodeTypeSpecificValue

### CacheNodeType
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# CacheNodeUpdateStatus

### CacheNodeId
- **Type**: typing.Optional[str]

### NodeUpdateStatus
- **Type**: typing.Optional[typing.Literal['complete', 'in-progress', 'not-applied', 'stopped', 'stopping', 'waiting-to-start']]

### NodeDeletionDate
- **Type**: typing.Optional[datetime.datetime]

### NodeUpdateStartDate
- **Type**: typing.Optional[datetime.datetime]

### NodeUpdateEndDate
- **Type**: typing.Optional[datetime.datetime]

### NodeUpdateInitiatedBy
- **Type**: typing.Optional[typing.Literal['customer', 'system']]

### NodeUpdateInitiatedDate
- **Type**: typing.Optional[datetime.datetime]

### NodeUpdateStatusModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# CacheParameterGroup

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### CacheParameterGroupFamily
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsGlobal
- **Type**: typing.Optional[bool]

### ARN
- **Type**: typing.Optional[str]


# CacheParameterGroupDetails

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.Parameter]
- **Required**: Yes

### CacheNodeTypeSpecificParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheNodeTypeSpecificParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CacheParameterGroupNameMessage

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CacheParameterGroupStatus

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### CacheNodeIdsToReboot
- **Type**: typing.Optional[typing.List[str]]


# CacheParameterGroupsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheParameterGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CacheSecurityGroup

### OwnerId
- **Type**: typing.Optional[str]

### CacheSecurityGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EC2SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.EC2SecurityGroup]]

### ARN
- **Type**: typing.Optional[str]


# CacheSecurityGroupMembership

### CacheSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# CacheSecurityGroupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheSecurityGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CacheSubnetGroup

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### CacheSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.Subnet]]

### ARN
- **Type**: typing.Optional[str]

### SupportedNetworkTypes
- **Type**: typing.Optional[typing.List[typing.Literal['dual_stack', 'ipv4', 'ipv6']]]


# CacheSubnetGroupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheSubnetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CacheUsageLimits

### DataStorage
- **Type**: <class 'NoneType'>

### ECPUPerSecond
- **Type**: <class 'NoneType'>


# CloudWatchLogsDestinationDetails

### LogGroup
- **Type**: typing.Optional[str]


# CompleteMigrationMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# CompleteMigrationResponse

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigureShard

### NodeGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### NewReplicaCount
- **Type**: <class 'int'>
- **Required**: Yes

### PreferredAvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### PreferredOutpostArns
- **Type**: typing.Optional[typing.Sequence[str]]


# CopyServerlessCacheSnapshotRequest

### SourceServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]


# CopyServerlessCacheSnapshotResponse

### ServerlessCacheSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CopySnapshotMessage

### SourceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetBucket
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]


# CopySnapshotResult

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCacheClusterMessage

### CacheClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupId
- **Type**: typing.Optional[str]

### AZMode
- **Type**: typing.Optional[typing.Literal['cross-az', 'single-az']]

### PreferredAvailabilityZone
- **Type**: typing.Optional[str]

### PreferredAvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### NumCacheNodes
- **Type**: typing.Optional[int]

### CacheNodeType
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### CacheSecurityGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]

### SnapshotArns
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotName
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### NotificationTopicArn
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### SnapshotWindow
- **Type**: typing.Optional[str]

### AuthToken
- **Type**: typing.Optional[str]

### OutpostMode
- **Type**: typing.Optional[typing.Literal['cross-outpost', 'single-outpost']]

### PreferredOutpostArn
- **Type**: typing.Optional[str]

### PreferredOutpostArns
- **Type**: typing.Optional[typing.Sequence[str]]

### LogDeliveryConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationRequest]]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### NetworkType
- **Type**: typing.Optional[typing.Literal['dual_stack', 'ipv4', 'ipv6']]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# CreateCacheClusterResult

### CacheCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCacheParameterGroupMessage

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CacheParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]


# CreateCacheParameterGroupResult

### CacheParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCacheSecurityGroupMessage

### CacheSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]


# CreateCacheSecurityGroupResult

### CacheSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCacheSubnetGroupMessage

### CacheSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CacheSubnetGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]


# CreateCacheSubnetGroupResult

### CacheSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGlobalReplicationGroupMessage

### GlobalReplicationGroupIdSuffix
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalReplicationGroupDescription
- **Type**: typing.Optional[str]


# CreateGlobalReplicationGroupResult

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReplicationGroupMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalReplicationGroupId
- **Type**: typing.Optional[str]

### PrimaryClusterId
- **Type**: typing.Optional[str]

### AutomaticFailoverEnabled
- **Type**: typing.Optional[bool]

### MultiAZEnabled
- **Type**: typing.Optional[bool]

### NumCacheClusters
- **Type**: typing.Optional[int]

### PreferredCacheClusterAZs
- **Type**: typing.Optional[typing.Sequence[str]]

### NumNodeGroups
- **Type**: typing.Optional[int]

### ReplicasPerNodeGroup
- **Type**: typing.Optional[int]

### NodeGroupConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupConfigurationUnion]]

### CacheNodeType
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### CacheSecurityGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]

### SnapshotArns
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotName
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### NotificationTopicArn
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### SnapshotWindow
- **Type**: typing.Optional[str]

### AuthToken
- **Type**: typing.Optional[str]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### AtRestEncryptionEnabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### UserGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### LogDeliveryConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationRequest]]

### DataTieringEnabled
- **Type**: typing.Optional[bool]

### NetworkType
- **Type**: typing.Optional[typing.Literal['dual_stack', 'ipv4', 'ipv6']]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]

### ClusterMode
- **Type**: typing.Optional[typing.Literal['compatible', 'disabled', 'enabled']]

### ServerlessCacheSnapshotName
- **Type**: typing.Optional[str]


# CreateReplicationGroupResult

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServerlessCacheRequest

### ServerlessCacheName
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]

### CacheUsageLimits
- **Type**: <class 'NoneType'>

### KmsKeyId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotArnsToRestore
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]

### UserGroupId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### DailySnapshotTime
- **Type**: typing.Optional[str]


# CreateServerlessCacheResponse

### ServerlessCache
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCache'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServerlessCacheSnapshotRequest

### ServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerlessCacheName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]


# CreateServerlessCacheSnapshotResponse

### ServerlessCacheSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSnapshotMessage

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupId
- **Type**: typing.Optional[str]

### CacheClusterId
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]


# CreateSnapshotResult

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserGroupMessage

### UserGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### UserIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]


# CreateUserMessage

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### AccessString
- **Type**: <class 'str'>
- **Required**: Yes

### Passwords
- **Type**: typing.Optional[typing.Sequence[str]]

### NoPasswordRequired
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]

### AuthenticationMode
- **Type**: <class 'NoneType'>


# CustomerNodeEndpoint

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# DataStorage

### Unit
- **Type**: typing.Literal['GB']
- **Required**: Yes

### Maximum
- **Type**: typing.Optional[int]

### Minimum
- **Type**: typing.Optional[int]


# DecreaseNodeGroupsInGlobalReplicationGroupMessage

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeGroupCount
- **Type**: <class 'int'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### GlobalNodeGroupsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### GlobalNodeGroupsToRetain
- **Type**: typing.Optional[typing.Sequence[str]]


# DecreaseNodeGroupsInGlobalReplicationGroupResult

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DecreaseReplicaCountMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### NewReplicaCount
- **Type**: typing.Optional[int]

### ReplicaConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ConfigureShard]]

### ReplicasToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# DecreaseReplicaCountResult

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCacheClusterMessage

### CacheClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### FinalSnapshotIdentifier
- **Type**: typing.Optional[str]


# DeleteCacheClusterResult

### CacheCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCacheParameterGroupMessage

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCacheSecurityGroupMessage

### CacheSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCacheSubnetGroupMessage

### CacheSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlobalReplicationGroupMessage

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### RetainPrimaryReplicationGroup
- **Type**: <class 'bool'>
- **Required**: Yes


# DeleteGlobalReplicationGroupResult

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteReplicationGroupMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### RetainPrimaryCluster
- **Type**: typing.Optional[bool]

### FinalSnapshotIdentifier
- **Type**: typing.Optional[str]


# DeleteReplicationGroupResult

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServerlessCacheRequest

### ServerlessCacheName
- **Type**: <class 'str'>
- **Required**: Yes

### FinalSnapshotName
- **Type**: typing.Optional[str]


# DeleteServerlessCacheResponse

### ServerlessCache
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCache'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServerlessCacheSnapshotRequest

### ServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServerlessCacheSnapshotResponse

### ServerlessCacheSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSnapshotMessage

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotResult

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUserGroupMessage

### UserGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserMessage

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCacheClustersMessage

### CacheClusterId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### ShowCacheNodeInfo
- **Type**: typing.Optional[bool]

### ShowCacheClustersNotInReplicationGroups
- **Type**: typing.Optional[bool]


# DescribeCacheClustersMessagePaginate

### CacheClusterId
- **Type**: typing.Optional[str]

### ShowCacheNodeInfo
- **Type**: typing.Optional[bool]

### ShowCacheClustersNotInReplicationGroups
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeCacheClustersMessageWait

### CacheClusterId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### ShowCacheNodeInfo
- **Type**: typing.Optional[bool]

### ShowCacheClustersNotInReplicationGroups
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeCacheClustersMessageWaitExtra

### CacheClusterId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### ShowCacheNodeInfo
- **Type**: typing.Optional[bool]

### ShowCacheClustersNotInReplicationGroups
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeCacheEngineVersionsMessage

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheParameterGroupFamily
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### DefaultOnly
- **Type**: typing.Optional[bool]


# DescribeCacheEngineVersionsMessagePaginate

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheParameterGroupFamily
- **Type**: typing.Optional[str]

### DefaultOnly
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeCacheParameterGroupsMessage

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCacheParameterGroupsMessagePaginate

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeCacheParametersMessage

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCacheParametersMessagePaginate

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeCacheSecurityGroupsMessage

### CacheSecurityGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCacheSecurityGroupsMessagePaginate

### CacheSecurityGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeCacheSubnetGroupsMessage

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCacheSubnetGroupsMessagePaginate

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeEngineDefaultParametersMessage

### CacheParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultParametersMessagePaginate

### CacheParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeEngineDefaultParametersResult

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.EngineDefaults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventsMessage

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cache-cluster', 'cache-parameter-group', 'cache-security-group', 'cache-subnet-group', 'replication-group', 'serverless-cache', 'serverless-cache-snapshot', 'user', 'user-group']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Timestamp]

### Duration
- **Type**: typing.Optional[int]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventsMessagePaginate

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cache-cluster', 'cache-parameter-group', 'cache-security-group', 'cache-subnet-group', 'replication-group', 'serverless-cache', 'serverless-cache-snapshot', 'user', 'user-group']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Timestamp]

### Duration
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeGlobalReplicationGroupsMessage

### GlobalReplicationGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### ShowMemberInfo
- **Type**: typing.Optional[bool]


# DescribeGlobalReplicationGroupsMessagePaginate

### GlobalReplicationGroupId
- **Type**: typing.Optional[str]

### ShowMemberInfo
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeGlobalReplicationGroupsResult

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalReplicationGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationGroupsMessage

### ReplicationGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationGroupsMessagePaginate

### ReplicationGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeReplicationGroupsMessageWait

### ReplicationGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeReplicationGroupsMessageWaitExtra

### ReplicationGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeReservedCacheNodesMessage

### ReservedCacheNodeId
- **Type**: typing.Optional[str]

### ReservedCacheNodesOfferingId
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedCacheNodesMessagePaginate

### ReservedCacheNodeId
- **Type**: typing.Optional[str]

### ReservedCacheNodesOfferingId
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeReservedCacheNodesOfferingsMessage

### ReservedCacheNodesOfferingId
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedCacheNodesOfferingsMessagePaginate

### ReservedCacheNodesOfferingId
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeServerlessCacheSnapshotsRequest

### ServerlessCacheName
- **Type**: typing.Optional[str]

### ServerlessCacheSnapshotName
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeServerlessCacheSnapshotsRequestPaginate

### ServerlessCacheName
- **Type**: typing.Optional[str]

### ServerlessCacheSnapshotName
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeServerlessCacheSnapshotsResponse

### ServerlessCacheSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeServerlessCachesRequest

### ServerlessCacheName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeServerlessCachesRequestPaginate

### ServerlessCacheName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeServerlessCachesResponse

### ServerlessCaches
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCache]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeServiceUpdatesMessage

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ServiceUpdateStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['available', 'cancelled', 'expired']]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeServiceUpdatesMessagePaginate

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ServiceUpdateStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['available', 'cancelled', 'expired']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeSnapshotsListMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.Snapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSnapshotsMessage

### ReplicationGroupId
- **Type**: typing.Optional[str]

### CacheClusterId
- **Type**: typing.Optional[str]

### SnapshotName
- **Type**: typing.Optional[str]

### SnapshotSource
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### ShowNodeGroupConfig
- **Type**: typing.Optional[bool]


# DescribeSnapshotsMessagePaginate

### ReplicationGroupId
- **Type**: typing.Optional[str]

### CacheClusterId
- **Type**: typing.Optional[str]

### SnapshotName
- **Type**: typing.Optional[str]

### SnapshotSource
- **Type**: typing.Optional[str]

### ShowNodeGroupConfig
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeUpdateActionsMessage

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ReplicationGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### CacheClusterIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Engine
- **Type**: typing.Optional[str]

### ServiceUpdateStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['available', 'cancelled', 'expired']]]

### ServiceUpdateTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.TimeRangeFilter]

### UpdateActionStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['complete', 'in-progress', 'not-applicable', 'not-applied', 'scheduled', 'scheduling', 'stopped', 'stopping', 'waiting-to-start']]]

### ShowNodeLevelUpdateStatus
- **Type**: typing.Optional[bool]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeUpdateActionsMessagePaginate

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ReplicationGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### CacheClusterIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Engine
- **Type**: typing.Optional[str]

### ServiceUpdateStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['available', 'cancelled', 'expired']]]

### ServiceUpdateTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.TimeRangeFilter]

### UpdateActionStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['complete', 'in-progress', 'not-applicable', 'not-applied', 'scheduled', 'scheduling', 'stopped', 'stopping', 'waiting-to-start']]]

### ShowNodeLevelUpdateStatus
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeUserGroupsMessage

### UserGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeUserGroupsMessagePaginate

### UserGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeUserGroupsResult

### UserGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.UserGroup]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUsersMessage

### Engine
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeUsersMessagePaginate

### Engine
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfig]


# DescribeUsersResult

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.User]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationDetails

### CloudWatchLogsDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.CloudWatchLogsDestinationDetails]

### KinesisFirehoseDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.KinesisFirehoseDestinationDetails]


# DisassociateGlobalReplicationGroupMessage

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateGlobalReplicationGroupResult

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# EC2SecurityGroup

### Status
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# ECPUPerSecond

### Maximum
- **Type**: typing.Optional[int]

### Minimum
- **Type**: typing.Optional[int]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# EngineDefaults

### CacheParameterGroupFamily
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.Parameter]]

### CacheNodeTypeSpecificParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheNodeTypeSpecificParameter]]


# Event

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cache-cluster', 'cache-parameter-group', 'cache-security-group', 'cache-subnet-group', 'replication-group', 'serverless-cache', 'serverless-cache-snapshot', 'user', 'user-group']]

### Message
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[datetime.datetime]


# EventsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ExportServerlessCacheSnapshotRequest

### ServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes


# ExportServerlessCacheSnapshotResponse

### ServerlessCacheSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# FailoverGlobalReplicationGroupMessage

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryRegion
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# FailoverGlobalReplicationGroupResult

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# Filter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GlobalNodeGroup

### GlobalNodeGroupId
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[str]


# GlobalReplicationGroup

### GlobalReplicationGroupId
- **Type**: typing.Optional[str]

### GlobalReplicationGroupDescription
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### Members
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupMember]]

### ClusterEnabled
- **Type**: typing.Optional[bool]

### GlobalNodeGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.GlobalNodeGroup]]

### AuthTokenEnabled
- **Type**: typing.Optional[bool]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### AtRestEncryptionEnabled
- **Type**: typing.Optional[bool]

### ARN
- **Type**: typing.Optional[str]


# GlobalReplicationGroupInfo

### GlobalReplicationGroupId
- **Type**: typing.Optional[str]

### GlobalReplicationGroupMemberRole
- **Type**: typing.Optional[str]


# GlobalReplicationGroupMember

### ReplicationGroupId
- **Type**: typing.Optional[str]

### ReplicationGroupRegion
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### AutomaticFailover
- **Type**: typing.Optional[typing.Literal['disabled', 'disabling', 'enabled', 'enabling']]

### Status
- **Type**: typing.Optional[str]


# IncreaseNodeGroupsInGlobalReplicationGroupMessage

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeGroupCount
- **Type**: <class 'int'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### RegionalConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.RegionalConfiguration]]


# IncreaseNodeGroupsInGlobalReplicationGroupResult

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# IncreaseReplicaCountMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### NewReplicaCount
- **Type**: typing.Optional[int]

### ReplicaConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ConfigureShard]]


# IncreaseReplicaCountResult

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# KinesisFirehoseDestinationDetails

### DeliveryStream
- **Type**: typing.Optional[str]


# ListAllowedNodeTypeModificationsMessage

### CacheClusterId
- **Type**: typing.Optional[str]

### ReplicationGroupId
- **Type**: typing.Optional[str]


# ListTagsForResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# LogDeliveryConfiguration

### LogType
- **Type**: typing.Optional[typing.Literal['engine-log', 'slow-log']]

### DestinationType
- **Type**: typing.Optional[typing.Literal['cloudwatch-logs', 'kinesis-firehose']]

### DestinationDetails
- **Type**: <class 'NoneType'>

### LogFormat
- **Type**: typing.Optional[typing.Literal['json', 'text']]

### Status
- **Type**: typing.Optional[typing.Literal['active', 'disabling', 'enabling', 'error', 'modifying']]

### Message
- **Type**: typing.Optional[str]


# LogDeliveryConfigurationRequest

### LogType
- **Type**: typing.Optional[typing.Literal['engine-log', 'slow-log']]

### DestinationType
- **Type**: typing.Optional[typing.Literal['cloudwatch-logs', 'kinesis-firehose']]

### DestinationDetails
- **Type**: <class 'NoneType'>

### LogFormat
- **Type**: typing.Optional[typing.Literal['json', 'text']]

### Enabled
- **Type**: typing.Optional[bool]


# ModifyCacheClusterMessage

### CacheClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NumCacheNodes
- **Type**: typing.Optional[int]

### CacheNodeIdsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### AZMode
- **Type**: typing.Optional[typing.Literal['cross-az', 'single-az']]

### NewAvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### CacheSecurityGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### NotificationTopicArn
- **Type**: typing.Optional[str]

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### NotificationTopicStatus
- **Type**: typing.Optional[str]

### ApplyImmediately
- **Type**: typing.Optional[bool]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### SnapshotWindow
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### AuthToken
- **Type**: typing.Optional[str]

### AuthTokenUpdateStrategy
- **Type**: typing.Optional[typing.Literal['DELETE', 'ROTATE', 'SET']]

### LogDeliveryConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationRequest]]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# ModifyCacheClusterResult

### CacheCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyCacheParameterGroupMessage

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterNameValues
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ParameterNameValue]
- **Required**: Yes


# ModifyCacheSubnetGroupMessage

### CacheSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CacheSubnetGroupDescription
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyCacheSubnetGroupResult

### CacheSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyGlobalReplicationGroupMessage

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### CacheNodeType
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### GlobalReplicationGroupDescription
- **Type**: typing.Optional[str]

### AutomaticFailoverEnabled
- **Type**: typing.Optional[bool]


# ModifyGlobalReplicationGroupResult

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyReplicationGroupMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupDescription
- **Type**: typing.Optional[str]

### PrimaryClusterId
- **Type**: typing.Optional[str]

### SnapshottingClusterId
- **Type**: typing.Optional[str]

### AutomaticFailoverEnabled
- **Type**: typing.Optional[bool]

### MultiAZEnabled
- **Type**: typing.Optional[bool]

### NodeGroupId
- **Type**: typing.Optional[str]

### CacheSecurityGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### NotificationTopicArn
- **Type**: typing.Optional[str]

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### NotificationTopicStatus
- **Type**: typing.Optional[str]

### ApplyImmediately
- **Type**: typing.Optional[bool]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### SnapshotWindow
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### AuthToken
- **Type**: typing.Optional[str]

### AuthTokenUpdateStrategy
- **Type**: typing.Optional[typing.Literal['DELETE', 'ROTATE', 'SET']]

### UserGroupIdsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### UserGroupIdsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### RemoveUserGroups
- **Type**: typing.Optional[bool]

### LogDeliveryConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationRequest]]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]

### ClusterMode
- **Type**: typing.Optional[typing.Literal['compatible', 'disabled', 'enabled']]


# ModifyReplicationGroupResult

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyReplicationGroupShardConfigurationMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeGroupCount
- **Type**: <class 'int'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### ReshardingConfiguration
- **Type**: typing.Optional[typing.Sequence[NoneType]]

### NodeGroupsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### NodeGroupsToRetain
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyReplicationGroupShardConfigurationResult

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyServerlessCacheRequest

### ServerlessCacheName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CacheUsageLimits
- **Type**: <class 'NoneType'>

### RemoveUserGroup
- **Type**: typing.Optional[bool]

### UserGroupId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### DailySnapshotTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]


# ModifyServerlessCacheResponse

### ServerlessCache
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCache'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyUserGroupMessage

### UserGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserIdsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### UserIdsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### Engine
- **Type**: typing.Optional[str]


# ModifyUserMessage

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessString
- **Type**: typing.Optional[str]

### AppendAccessString
- **Type**: typing.Optional[str]

### Passwords
- **Type**: typing.Optional[typing.Sequence[str]]

### NoPasswordRequired
- **Type**: typing.Optional[bool]

### AuthenticationMode
- **Type**: <class 'NoneType'>

### Engine
- **Type**: typing.Optional[str]


# NodeGroup

### NodeGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### PrimaryEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Endpoint]

### ReaderEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Endpoint]

### Slots
- **Type**: typing.Optional[str]

### NodeGroupMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupMember]]


# NodeGroupConfiguration

### NodeGroupId
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[str]

### ReplicaCount
- **Type**: typing.Optional[int]

### PrimaryAvailabilityZone
- **Type**: typing.Optional[str]

### ReplicaAvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### PrimaryOutpostArn
- **Type**: typing.Optional[str]

### ReplicaOutpostArns
- **Type**: typing.Optional[typing.Sequence[str]]


# NodeGroupConfigurationOutput

### NodeGroupId
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[str]

### ReplicaCount
- **Type**: typing.Optional[int]

### PrimaryAvailabilityZone
- **Type**: typing.Optional[str]

### ReplicaAvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### PrimaryOutpostArn
- **Type**: typing.Optional[str]

### ReplicaOutpostArns
- **Type**: typing.Optional[typing.List[str]]


# NodeGroupConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NodeGroupMember

### CacheClusterId
- **Type**: typing.Optional[str]

### CacheNodeId
- **Type**: typing.Optional[str]

### ReadEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Endpoint]

### PreferredAvailabilityZone
- **Type**: typing.Optional[str]

### PreferredOutpostArn
- **Type**: typing.Optional[str]

### CurrentRole
- **Type**: typing.Optional[str]


# NodeGroupMemberUpdateStatus

### CacheClusterId
- **Type**: typing.Optional[str]

### CacheNodeId
- **Type**: typing.Optional[str]

### NodeUpdateStatus
- **Type**: typing.Optional[typing.Literal['complete', 'in-progress', 'not-applied', 'stopped', 'stopping', 'waiting-to-start']]

### NodeDeletionDate
- **Type**: typing.Optional[datetime.datetime]

### NodeUpdateStartDate
- **Type**: typing.Optional[datetime.datetime]

### NodeUpdateEndDate
- **Type**: typing.Optional[datetime.datetime]

### NodeUpdateInitiatedBy
- **Type**: typing.Optional[typing.Literal['customer', 'system']]

### NodeUpdateInitiatedDate
- **Type**: typing.Optional[datetime.datetime]

### NodeUpdateStatusModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# NodeGroupUpdateStatus

### NodeGroupId
- **Type**: typing.Optional[str]

### NodeGroupMemberUpdateStatus
- **Type**: typing.Optional[typing.List[NoneType]]


# NodeSnapshot

### CacheClusterId
- **Type**: typing.Optional[str]

### NodeGroupId
- **Type**: typing.Optional[str]

### CacheNodeId
- **Type**: typing.Optional[str]

### NodeGroupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupConfigurationOutput]

### CacheSize
- **Type**: typing.Optional[str]

### CacheNodeCreateTime
- **Type**: typing.Optional[datetime.datetime]

### SnapshotCreateTime
- **Type**: typing.Optional[datetime.datetime]


# NotificationConfiguration

### TopicArn
- **Type**: typing.Optional[str]

### TopicStatus
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameter

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]

### IsModifiable
- **Type**: typing.Optional[bool]

### MinimumEngineVersion
- **Type**: typing.Optional[str]

### ChangeType
- **Type**: typing.Optional[typing.Literal['immediate', 'requires-reboot']]


# ParameterNameValue

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]


# PendingLogDeliveryConfiguration

### LogType
- **Type**: typing.Optional[typing.Literal['engine-log', 'slow-log']]

### DestinationType
- **Type**: typing.Optional[typing.Literal['cloudwatch-logs', 'kinesis-firehose']]

### DestinationDetails
- **Type**: <class 'NoneType'>

### LogFormat
- **Type**: typing.Optional[typing.Literal['json', 'text']]


# PendingModifiedValues

### NumCacheNodes
- **Type**: typing.Optional[int]

### CacheNodeIdsToRemove
- **Type**: typing.Optional[typing.List[str]]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### AuthTokenStatus
- **Type**: typing.Optional[typing.Literal['ROTATING', 'SETTING']]

### LogDeliveryConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.PendingLogDeliveryConfiguration]]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]


# ProcessedUpdateAction

### ReplicationGroupId
- **Type**: typing.Optional[str]

### CacheClusterId
- **Type**: typing.Optional[str]

### ServiceUpdateName
- **Type**: typing.Optional[str]

### UpdateActionStatus
- **Type**: typing.Optional[typing.Literal['complete', 'in-progress', 'not-applicable', 'not-applied', 'scheduled', 'scheduling', 'stopped', 'stopping', 'waiting-to-start']]


# PurchaseReservedCacheNodesOfferingMessage

### ReservedCacheNodesOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedCacheNodeId
- **Type**: typing.Optional[str]

### CacheNodeCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.Tag]]


# PurchaseReservedCacheNodesOfferingResult

### ReservedCacheNode
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReservedCacheNode'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# RebalanceSlotsInGlobalReplicationGroupMessage

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes


# RebalanceSlotsInGlobalReplicationGroupResult

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# RebootCacheClusterMessage

### CacheClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### CacheNodeIdsToReboot
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RebootCacheClusterResult

### CacheCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# RecurringCharge

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# RegionalConfiguration

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ReshardingConfiguration
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ReshardingConfiguration]
- **Required**: Yes


# RemoveTagsFromResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReplicationGroup

### ReplicationGroupId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### GlobalReplicationGroupInfo
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupPendingModifiedValues]

### MemberClusters
- **Type**: typing.Optional[typing.List[str]]

### NodeGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroup]]

### SnapshottingClusterId
- **Type**: typing.Optional[str]

### AutomaticFailover
- **Type**: typing.Optional[typing.Literal['disabled', 'disabling', 'enabled', 'enabling']]

### MultiAZ
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### ConfigurationEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Endpoint]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### SnapshotWindow
- **Type**: typing.Optional[str]

### ClusterEnabled
- **Type**: typing.Optional[bool]

### CacheNodeType
- **Type**: typing.Optional[str]

### AuthTokenEnabled
- **Type**: typing.Optional[bool]

### AuthTokenLastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### AtRestEncryptionEnabled
- **Type**: typing.Optional[bool]

### MemberClustersOutpostArns
- **Type**: typing.Optional[typing.List[str]]

### KmsKeyId
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### UserGroupIds
- **Type**: typing.Optional[typing.List[str]]

### LogDeliveryConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfiguration]]

### ReplicationGroupCreateTime
- **Type**: typing.Optional[datetime.datetime]

### DataTiering
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### NetworkType
- **Type**: typing.Optional[typing.Literal['dual_stack', 'ipv4', 'ipv6']]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]

### ClusterMode
- **Type**: typing.Optional[typing.Literal['compatible', 'disabled', 'enabled']]

### Engine
- **Type**: typing.Optional[str]


# ReplicationGroupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ReplicationGroupPendingModifiedValues

### PrimaryClusterId
- **Type**: typing.Optional[str]

### AutomaticFailoverStatus
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### Resharding
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.ReshardingStatus]

### AuthTokenStatus
- **Type**: typing.Optional[typing.Literal['ROTATING', 'SETTING']]

### UserGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.UserGroupsUpdateStatus]

### LogDeliveryConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.PendingLogDeliveryConfiguration]]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]

### ClusterMode
- **Type**: typing.Optional[typing.Literal['compatible', 'disabled', 'enabled']]


# ReservedCacheNode

### ReservedCacheNodeId
- **Type**: typing.Optional[str]

### ReservedCacheNodesOfferingId
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### UsagePrice
- **Type**: typing.Optional[float]

### CacheNodeCount
- **Type**: typing.Optional[int]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.RecurringCharge]]

### ReservationARN
- **Type**: typing.Optional[str]


# ReservedCacheNodeMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedCacheNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ReservedCacheNode]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ReservedCacheNodesOffering

### ReservedCacheNodesOfferingId
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### UsagePrice
- **Type**: typing.Optional[float]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.RecurringCharge]]


# ReservedCacheNodesOfferingMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedCacheNodesOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ReservedCacheNodesOffering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# ResetCacheParameterGroupMessage

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### ParameterNameValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ParameterNameValue]]


# ReshardingConfiguration

### NodeGroupId
- **Type**: typing.Optional[str]

### PreferredAvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]


# ReshardingStatus

### SlotMigration
- **Type**: <class 'NoneType'>


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


# RevokeCacheSecurityGroupIngressMessage

### CacheSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EC2SecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EC2SecurityGroupOwnerId
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeCacheSecurityGroupIngressResult

### CacheSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# SecurityGroupMembership

### SecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ServerlessCache

### ServerlessCacheName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]

### FullEngineVersion
- **Type**: typing.Optional[str]

### CacheUsageLimits
- **Type**: <class 'NoneType'>

### KmsKeyId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Endpoint
- **Type**: <class 'NoneType'>

### ReaderEndpoint
- **Type**: <class 'NoneType'>

### ARN
- **Type**: typing.Optional[str]

### UserGroupId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### DailySnapshotTime
- **Type**: typing.Optional[str]


# ServerlessCacheConfiguration

### ServerlessCacheName
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]


# ServerlessCacheSnapshot

### ServerlessCacheSnapshotName
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### ExpiryTime
- **Type**: typing.Optional[datetime.datetime]

### BytesUsedForCache
- **Type**: typing.Optional[str]

### ServerlessCacheConfiguration
- **Type**: <class 'NoneType'>


# ServiceUpdate

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ServiceUpdateReleaseDate
- **Type**: typing.Optional[datetime.datetime]

### ServiceUpdateEndDate
- **Type**: typing.Optional[datetime.datetime]

### ServiceUpdateSeverity
- **Type**: typing.Optional[typing.Literal['critical', 'important', 'low', 'medium']]

### ServiceUpdateRecommendedApplyByDate
- **Type**: typing.Optional[datetime.datetime]

### ServiceUpdateStatus
- **Type**: typing.Optional[typing.Literal['available', 'cancelled', 'expired']]

### ServiceUpdateDescription
- **Type**: typing.Optional[str]

### ServiceUpdateType
- **Type**: typing.Optional[typing.Literal['security-update']]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### AutoUpdateAfterRecommendedApplyByDate
- **Type**: typing.Optional[bool]

### EstimatedUpdateTime
- **Type**: typing.Optional[str]


# ServiceUpdatesMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ServiceUpdate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# SlotMigration

### ProgressPercentage
- **Type**: typing.Optional[float]


# Snapshot

### SnapshotName
- **Type**: typing.Optional[str]

### ReplicationGroupId
- **Type**: typing.Optional[str]

### ReplicationGroupDescription
- **Type**: typing.Optional[str]

### CacheClusterId
- **Type**: typing.Optional[str]

### SnapshotStatus
- **Type**: typing.Optional[str]

### SnapshotSource
- **Type**: typing.Optional[str]

### CacheNodeType
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### NumCacheNodes
- **Type**: typing.Optional[int]

### PreferredAvailabilityZone
- **Type**: typing.Optional[str]

### PreferredOutpostArn
- **Type**: typing.Optional[str]

### CacheClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### TopicArn
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### SnapshotWindow
- **Type**: typing.Optional[str]

### NumNodeGroups
- **Type**: typing.Optional[int]

### AutomaticFailover
- **Type**: typing.Optional[typing.Literal['disabled', 'disabling', 'enabled', 'enabling']]

### NodeSnapshots
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.NodeSnapshot]]

### KmsKeyId
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### DataTiering
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]


# StartMigrationMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerNodeEndpointList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.CustomerNodeEndpoint]
- **Required**: Yes


# StartMigrationResponse

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# Subnet

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.AvailabilityZone]

### SubnetOutpost
- **Type**: <class 'NoneType'>

### SupportedNetworkTypes
- **Type**: typing.Optional[typing.List[typing.Literal['dual_stack', 'ipv4', 'ipv6']]]


# SubnetOutpost

### SubnetOutpostArn
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagListMessage

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# TestFailoverMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# TestFailoverResult

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# TestMigrationMessage

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerNodeEndpointList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.CustomerNodeEndpoint]
- **Required**: Yes


# TestMigrationResponse

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# TimeRangeFilter

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.Timestamp]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnprocessedUpdateAction

### ReplicationGroupId
- **Type**: typing.Optional[str]

### CacheClusterId
- **Type**: typing.Optional[str]

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UpdateAction

### ReplicationGroupId
- **Type**: typing.Optional[str]

### CacheClusterId
- **Type**: typing.Optional[str]

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ServiceUpdateReleaseDate
- **Type**: typing.Optional[datetime.datetime]

### ServiceUpdateSeverity
- **Type**: typing.Optional[typing.Literal['critical', 'important', 'low', 'medium']]

### ServiceUpdateStatus
- **Type**: typing.Optional[typing.Literal['available', 'cancelled', 'expired']]

### ServiceUpdateRecommendedApplyByDate
- **Type**: typing.Optional[datetime.datetime]

### ServiceUpdateType
- **Type**: typing.Optional[typing.Literal['security-update']]

### UpdateActionAvailableDate
- **Type**: typing.Optional[datetime.datetime]

### UpdateActionStatus
- **Type**: typing.Optional[typing.Literal['complete', 'in-progress', 'not-applicable', 'not-applied', 'scheduled', 'scheduling', 'stopped', 'stopping', 'waiting-to-start']]

### NodesUpdated
- **Type**: typing.Optional[str]

### UpdateActionStatusModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### SlaMet
- **Type**: typing.Optional[typing.Literal['n/a', 'no', 'yes']]

### NodeGroupUpdateStatus
- **Type**: typing.Optional[typing.List[NoneType]]

### CacheNodeUpdateStatus
- **Type**: typing.Optional[typing.List[NoneType]]

### EstimatedUpdateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]


# UpdateActionResultsMessage

### ProcessedUpdateActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ProcessedUpdateAction]
- **Required**: Yes

### UnprocessedUpdateActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.UnprocessedUpdateAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateActionsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.UpdateAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# User

### UserId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### MinimumEngineVersion
- **Type**: typing.Optional[str]

### AccessString
- **Type**: typing.Optional[str]

### UserGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Authentication
- **Type**: <class 'NoneType'>

### ARN
- **Type**: typing.Optional[str]


# UserGroup

### UserGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### UserIds
- **Type**: typing.Optional[typing.List[str]]

### MinimumEngineVersion
- **Type**: typing.Optional[str]

### PendingChanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.UserGroupPendingChanges]

### ReplicationGroups
- **Type**: typing.Optional[typing.List[str]]

### ServerlessCaches
- **Type**: typing.Optional[typing.List[str]]

### ARN
- **Type**: typing.Optional[str]


# UserGroupPendingChanges

### UserIdsToRemove
- **Type**: typing.Optional[typing.List[str]]

### UserIdsToAdd
- **Type**: typing.Optional[typing.List[str]]


# UserGroupResponse

### UserGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### UserIds
- **Type**: typing.List[str]
- **Required**: Yes

### MinimumEngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PendingChanges
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.UserGroupPendingChanges'>
- **Required**: Yes

### ReplicationGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ServerlessCaches
- **Type**: typing.List[str]
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# UserGroupsUpdateStatus

### UserGroupIdsToAdd
- **Type**: typing.Optional[typing.List[str]]

### UserGroupIdsToRemove
- **Type**: typing.Optional[typing.List[str]]


# UserResponse

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### MinimumEngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### AccessString
- **Type**: <class 'str'>
- **Required**: Yes

### UserGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.Authentication'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



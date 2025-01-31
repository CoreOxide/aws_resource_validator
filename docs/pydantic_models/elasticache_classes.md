# elasticache_classes

# AddTagsToResourceMessageRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]
- **Required**: Yes


# AllowedNodeTypeModificationsMessageTypeDef

### ScaleUpModifications
- **Type**: typing.List[str]
- **Required**: Yes

### ScaleDownModifications
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthenticationModeTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['iam', 'no-password-required', 'password']]

### Passwords
- **Type**: typing.Optional[typing.Sequence[str]]


# AuthenticationTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['iam', 'no-password', 'password']]

### PasswordCount
- **Type**: typing.Optional[int]


# AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef

### CacheSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EC2SecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EC2SecurityGroupOwnerId
- **Type**: <class 'str'>
- **Required**: Yes


# AuthorizeCacheSecurityGroupIngressResultTypeDef

### CacheSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AvailabilityZoneTypeDef

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchApplyUpdateActionMessageRequestTypeDef

### ServiceUpdateName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### CacheClusterIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchStopUpdateActionMessageRequestTypeDef

### ServiceUpdateName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### CacheClusterIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CacheClusterMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CacheClusterTypeDef

### CacheClusterId
- **Type**: typing.Optional[str]

### ConfigurationEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.EndpointTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PendingModifiedValuesTypeDef]

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.NotificationConfigurationTypeDef]

### CacheSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroupMembershipTypeDef]]

### CacheParameterGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.CacheParameterGroupStatusTypeDef]

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### CacheNodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheNodeTypeDef]]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.SecurityGroupMembershipTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationTypeDef]]

### NetworkType
- **Type**: typing.Optional[typing.Literal['dual_stack', 'ipv4', 'ipv6']]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]


# CacheEngineVersionMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheEngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheEngineVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CacheEngineVersionTypeDef

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


# CacheNodeTypeDef

### CacheNodeId
- **Type**: typing.Optional[str]

### CacheNodeStatus
- **Type**: typing.Optional[str]

### CacheNodeCreateTime
- **Type**: typing.Optional[datetime.datetime]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.EndpointTypeDef]

### ParameterGroupStatus
- **Type**: typing.Optional[str]

### SourceCacheNodeId
- **Type**: typing.Optional[str]

### CustomerAvailabilityZone
- **Type**: typing.Optional[str]

### CustomerOutpostArn
- **Type**: typing.Optional[str]


# CacheNodeTypeSpecificParameterTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheNodeTypeSpecificValueTypeDef]]

### ChangeType
- **Type**: typing.Optional[typing.Literal['immediate', 'requires-reboot']]


# CacheNodeTypeSpecificValueTypeDef

### CacheNodeType
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# CacheNodeUpdateStatusTypeDef

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


# CacheParameterGroupDetailsTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ParameterTypeDef]
- **Required**: Yes

### CacheNodeTypeSpecificParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheNodeTypeSpecificParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CacheParameterGroupNameMessageTypeDef

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CacheParameterGroupStatusTypeDef

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### CacheNodeIdsToReboot
- **Type**: typing.Optional[typing.List[str]]


# CacheParameterGroupTypeDef

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


# CacheParameterGroupsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheParameterGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CacheSecurityGroupMembershipTypeDef

### CacheSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# CacheSecurityGroupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheSecurityGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CacheSecurityGroupTypeDef

### OwnerId
- **Type**: typing.Optional[str]

### CacheSecurityGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EC2SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.EC2SecurityGroupTypeDef]]

### ARN
- **Type**: typing.Optional[str]


# CacheSubnetGroupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### CacheSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheSubnetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CacheSubnetGroupTypeDef

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### CacheSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.SubnetTypeDef]]

### ARN
- **Type**: typing.Optional[str]

### SupportedNetworkTypes
- **Type**: typing.Optional[typing.List[typing.Literal['dual_stack', 'ipv4', 'ipv6']]]


# CacheUsageLimitsTypeDef

### DataStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.DataStorageTypeDef]

### ECPUPerSecond
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.ECPUPerSecondTypeDef]


# CloudWatchLogsDestinationDetailsTypeDef

### LogGroup
- **Type**: typing.Optional[str]


# CompleteMigrationMessageRequestTypeDef

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# CompleteMigrationResponseTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfigureShardTypeDef

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


# CopyServerlessCacheSnapshotRequestRequestTypeDef

### SourceServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]


# CopyServerlessCacheSnapshotResponseTypeDef

### ServerlessCacheSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopySnapshotMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]


# CopySnapshotResultTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCacheClusterMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationRequestTypeDef]]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### NetworkType
- **Type**: typing.Optional[typing.Literal['dual_stack', 'ipv4', 'ipv6']]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# CreateCacheClusterResultTypeDef

### CacheCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCacheParameterGroupMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]


# CreateCacheParameterGroupResultTypeDef

### CacheParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCacheSecurityGroupMessageRequestTypeDef

### CacheSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]


# CreateCacheSecurityGroupResultTypeDef

### CacheSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCacheSubnetGroupMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]


# CreateCacheSubnetGroupResultTypeDef

### CacheSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGlobalReplicationGroupMessageRequestTypeDef

### GlobalReplicationGroupIdSuffix
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalReplicationGroupDescription
- **Type**: typing.Optional[str]


# CreateGlobalReplicationGroupResultTypeDef

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReplicationGroupMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupConfigurationTypeDef, aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupConfigurationExtraOutputTypeDef]]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationRequestTypeDef]]

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


# CreateReplicationGroupResultTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServerlessCacheRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.CacheUsageLimitsTypeDef]

### KmsKeyId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotArnsToRestore
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]

### UserGroupId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotRetentionLimit
- **Type**: typing.Optional[int]

### DailySnapshotTime
- **Type**: typing.Optional[str]


# CreateServerlessCacheResponseTypeDef

### ServerlessCache
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServerlessCacheSnapshotRequestRequestTypeDef

### ServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerlessCacheName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]


# CreateServerlessCacheSnapshotResponseTypeDef

### ServerlessCacheSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]


# CreateSnapshotResultTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserGroupMessageRequestTypeDef

### UserGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### UserIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]


# CreateUserMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]

### AuthenticationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.AuthenticationModeTypeDef]


# CustomerNodeEndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# DataStorageTypeDef

### Unit
- **Type**: typing.Literal['GB']
- **Required**: Yes

### Maximum
- **Type**: typing.Optional[int]

### Minimum
- **Type**: typing.Optional[int]


# DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef

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


# DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DecreaseReplicaCountMessageRequestTypeDef

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### NewReplicaCount
- **Type**: typing.Optional[int]

### ReplicaConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ConfigureShardTypeDef]]

### ReplicasToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# DecreaseReplicaCountResultTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCacheClusterMessageRequestTypeDef

### CacheClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### FinalSnapshotIdentifier
- **Type**: typing.Optional[str]


# DeleteCacheClusterResultTypeDef

### CacheCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCacheParameterGroupMessageRequestTypeDef

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCacheSecurityGroupMessageRequestTypeDef

### CacheSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCacheSubnetGroupMessageRequestTypeDef

### CacheSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlobalReplicationGroupMessageRequestTypeDef

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### RetainPrimaryReplicationGroup
- **Type**: <class 'bool'>
- **Required**: Yes


# DeleteGlobalReplicationGroupResultTypeDef

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteReplicationGroupMessageRequestTypeDef

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### RetainPrimaryCluster
- **Type**: typing.Optional[bool]

### FinalSnapshotIdentifier
- **Type**: typing.Optional[str]


# DeleteReplicationGroupResultTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServerlessCacheRequestRequestTypeDef

### ServerlessCacheName
- **Type**: <class 'str'>
- **Required**: Yes

### FinalSnapshotName
- **Type**: typing.Optional[str]


# DeleteServerlessCacheResponseTypeDef

### ServerlessCache
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServerlessCacheSnapshotRequestRequestTypeDef

### ServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServerlessCacheSnapshotResponseTypeDef

### ServerlessCacheSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSnapshotMessageRequestTypeDef

### SnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotResultTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUserGroupMessageRequestTypeDef

### UserGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserMessageRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCacheClustersMessageCacheClusterAvailableWaitTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.WaiterConfigTypeDef]


# DescribeCacheClustersMessageCacheClusterDeletedWaitTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.WaiterConfigTypeDef]


# DescribeCacheClustersMessageDescribeCacheClustersPaginateTypeDef

### CacheClusterId
- **Type**: typing.Optional[str]

### ShowCacheNodeInfo
- **Type**: typing.Optional[bool]

### ShowCacheClustersNotInReplicationGroups
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeCacheClustersMessageRequestTypeDef

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


# DescribeCacheEngineVersionsMessageDescribeCacheEngineVersionsPaginateTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheParameterGroupFamily
- **Type**: typing.Optional[str]

### DefaultOnly
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeCacheEngineVersionsMessageRequestTypeDef

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


# DescribeCacheParameterGroupsMessageDescribeCacheParameterGroupsPaginateTypeDef

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeCacheParameterGroupsMessageRequestTypeDef

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCacheParametersMessageDescribeCacheParametersPaginateTypeDef

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeCacheParametersMessageRequestTypeDef

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCacheSecurityGroupsMessageDescribeCacheSecurityGroupsPaginateTypeDef

### CacheSecurityGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeCacheSecurityGroupsMessageRequestTypeDef

### CacheSecurityGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCacheSubnetGroupsMessageDescribeCacheSubnetGroupsPaginateTypeDef

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeCacheSubnetGroupsMessageRequestTypeDef

### CacheSubnetGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef

### CacheParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeEngineDefaultParametersMessageRequestTypeDef

### CacheParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultParametersResultTypeDef

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.EngineDefaultsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventsMessageDescribeEventsPaginateTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cache-cluster', 'cache-parameter-group', 'cache-security-group', 'cache-subnet-group', 'replication-group', 'serverless-cache', 'serverless-cache-snapshot', 'user', 'user-group']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeEventsMessageRequestTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cache-cluster', 'cache-parameter-group', 'cache-security-group', 'cache-subnet-group', 'replication-group', 'serverless-cache', 'serverless-cache-snapshot', 'user', 'user-group']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[int]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeGlobalReplicationGroupsMessageDescribeGlobalReplicationGroupsPaginateTypeDef

### GlobalReplicationGroupId
- **Type**: typing.Optional[str]

### ShowMemberInfo
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeGlobalReplicationGroupsMessageRequestTypeDef

### GlobalReplicationGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### ShowMemberInfo
- **Type**: typing.Optional[bool]


# DescribeGlobalReplicationGroupsResultTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalReplicationGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationGroupsMessageDescribeReplicationGroupsPaginateTypeDef

### ReplicationGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeReplicationGroupsMessageReplicationGroupAvailableWaitTypeDef

### ReplicationGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.WaiterConfigTypeDef]


# DescribeReplicationGroupsMessageReplicationGroupDeletedWaitTypeDef

### ReplicationGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.WaiterConfigTypeDef]


# DescribeReplicationGroupsMessageRequestTypeDef

### ReplicationGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedCacheNodesMessageDescribeReservedCacheNodesPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeReservedCacheNodesMessageRequestTypeDef

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


# DescribeReservedCacheNodesOfferingsMessageDescribeReservedCacheNodesOfferingsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeReservedCacheNodesOfferingsMessageRequestTypeDef

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


# DescribeServerlessCacheSnapshotsRequestDescribeServerlessCacheSnapshotsPaginateTypeDef

### ServerlessCacheName
- **Type**: typing.Optional[str]

### ServerlessCacheSnapshotName
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeServerlessCacheSnapshotsRequestRequestTypeDef

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


# DescribeServerlessCacheSnapshotsResponseTypeDef

### ServerlessCacheSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeServerlessCachesRequestDescribeServerlessCachesPaginateTypeDef

### ServerlessCacheName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeServerlessCachesRequestRequestTypeDef

### ServerlessCacheName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeServerlessCachesResponseTypeDef

### ServerlessCaches
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeServiceUpdatesMessageDescribeServiceUpdatesPaginateTypeDef

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ServiceUpdateStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['available', 'cancelled', 'expired']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeServiceUpdatesMessageRequestTypeDef

### ServiceUpdateName
- **Type**: typing.Optional[str]

### ServiceUpdateStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['available', 'cancelled', 'expired']]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeSnapshotsListMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.SnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSnapshotsMessageDescribeSnapshotsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeSnapshotsMessageRequestTypeDef

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


# DescribeUpdateActionsMessageDescribeUpdateActionsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.TimeRangeFilterTypeDef]

### UpdateActionStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['complete', 'in-progress', 'not-applicable', 'not-applied', 'scheduled', 'scheduling', 'stopped', 'stopping', 'waiting-to-start']]]

### ShowNodeLevelUpdateStatus
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeUpdateActionsMessageRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.TimeRangeFilterTypeDef]

### UpdateActionStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['complete', 'in-progress', 'not-applicable', 'not-applied', 'scheduled', 'scheduling', 'stopped', 'stopping', 'waiting-to-start']]]

### ShowNodeLevelUpdateStatus
- **Type**: typing.Optional[bool]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeUserGroupsMessageDescribeUserGroupsPaginateTypeDef

### UserGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeUserGroupsMessageRequestTypeDef

### UserGroupId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeUserGroupsResultTypeDef

### UserGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.UserGroupTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUsersMessageDescribeUsersPaginateTypeDef

### Engine
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.PaginatorConfigTypeDef]


# DescribeUsersMessageRequestTypeDef

### Engine
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeUsersResultTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.UserTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationDetailsTypeDef

### CloudWatchLogsDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.CloudWatchLogsDestinationDetailsTypeDef]

### KinesisFirehoseDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.KinesisFirehoseDestinationDetailsTypeDef]


# DisassociateGlobalReplicationGroupMessageRequestTypeDef

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateGlobalReplicationGroupResultTypeDef

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EC2SecurityGroupTypeDef

### Status
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# ECPUPerSecondTypeDef

### Maximum
- **Type**: typing.Optional[int]

### Minimum
- **Type**: typing.Optional[int]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# EngineDefaultsTypeDef

### CacheParameterGroupFamily
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ParameterTypeDef]]

### CacheNodeTypeSpecificParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheNodeTypeSpecificParameterTypeDef]]


# EventTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cache-cluster', 'cache-parameter-group', 'cache-security-group', 'cache-subnet-group', 'replication-group', 'serverless-cache', 'serverless-cache-snapshot', 'user', 'user-group']]

### Message
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[datetime.datetime]


# EventsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportServerlessCacheSnapshotRequestRequestTypeDef

### ServerlessCacheSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes


# ExportServerlessCacheSnapshotResponseTypeDef

### ServerlessCacheSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailoverGlobalReplicationGroupMessageRequestTypeDef

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryRegion
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# FailoverGlobalReplicationGroupResultTypeDef

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GlobalNodeGroupTypeDef

### GlobalNodeGroupId
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[str]


# GlobalReplicationGroupInfoTypeDef

### GlobalReplicationGroupId
- **Type**: typing.Optional[str]

### GlobalReplicationGroupMemberRole
- **Type**: typing.Optional[str]


# GlobalReplicationGroupMemberTypeDef

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


# GlobalReplicationGroupTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupMemberTypeDef]]

### ClusterEnabled
- **Type**: typing.Optional[bool]

### GlobalNodeGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.GlobalNodeGroupTypeDef]]

### AuthTokenEnabled
- **Type**: typing.Optional[bool]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### AtRestEncryptionEnabled
- **Type**: typing.Optional[bool]

### ARN
- **Type**: typing.Optional[str]


# IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.RegionalConfigurationTypeDef]]


# IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IncreaseReplicaCountMessageRequestTypeDef

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### NewReplicaCount
- **Type**: typing.Optional[int]

### ReplicaConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ConfigureShardTypeDef]]


# IncreaseReplicaCountResultTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KinesisFirehoseDestinationDetailsTypeDef

### DeliveryStream
- **Type**: typing.Optional[str]


# ListAllowedNodeTypeModificationsMessageRequestTypeDef

### CacheClusterId
- **Type**: typing.Optional[str]

### ReplicationGroupId
- **Type**: typing.Optional[str]


# ListTagsForResourceMessageRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# LogDeliveryConfigurationRequestTypeDef

### LogType
- **Type**: typing.Optional[typing.Literal['engine-log', 'slow-log']]

### DestinationType
- **Type**: typing.Optional[typing.Literal['cloudwatch-logs', 'kinesis-firehose']]

### DestinationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.DestinationDetailsTypeDef]

### LogFormat
- **Type**: typing.Optional[typing.Literal['json', 'text']]

### Enabled
- **Type**: typing.Optional[bool]


# LogDeliveryConfigurationTypeDef

### LogType
- **Type**: typing.Optional[typing.Literal['engine-log', 'slow-log']]

### DestinationType
- **Type**: typing.Optional[typing.Literal['cloudwatch-logs', 'kinesis-firehose']]

### DestinationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.DestinationDetailsTypeDef]

### LogFormat
- **Type**: typing.Optional[typing.Literal['json', 'text']]

### Status
- **Type**: typing.Optional[typing.Literal['active', 'disabling', 'enabling', 'error', 'modifying']]

### Message
- **Type**: typing.Optional[str]


# ModifyCacheClusterMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationRequestTypeDef]]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# ModifyCacheClusterResultTypeDef

### CacheCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyCacheParameterGroupMessageRequestTypeDef

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterNameValues
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ParameterNameValueTypeDef]
- **Required**: Yes


# ModifyCacheSubnetGroupMessageRequestTypeDef

### CacheSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CacheSubnetGroupDescription
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyCacheSubnetGroupResultTypeDef

### CacheSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyGlobalReplicationGroupMessageRequestTypeDef

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### CacheNodeType
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### CacheParameterGroupName
- **Type**: typing.Optional[str]

### GlobalReplicationGroupDescription
- **Type**: typing.Optional[str]

### AutomaticFailoverEnabled
- **Type**: typing.Optional[bool]


# ModifyGlobalReplicationGroupResultTypeDef

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyReplicationGroupMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationRequestTypeDef]]

### IpDiscovery
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]

### ClusterMode
- **Type**: typing.Optional[typing.Literal['compatible', 'disabled', 'enabled']]


# ModifyReplicationGroupResultTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyReplicationGroupShardConfigurationMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ReshardingConfigurationTypeDef]]

### NodeGroupsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### NodeGroupsToRetain
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyReplicationGroupShardConfigurationResultTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyServerlessCacheRequestRequestTypeDef

### ServerlessCacheName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CacheUsageLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.CacheUsageLimitsTypeDef]

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


# ModifyServerlessCacheResponseTypeDef

### ServerlessCache
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyUserGroupMessageRequestTypeDef

### UserGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserIdsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### UserIdsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyUserMessageRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.AuthenticationModeTypeDef]


# NodeGroupConfigurationExtraOutputTypeDef

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


# NodeGroupConfigurationOutputTypeDef

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


# NodeGroupConfigurationTypeDef

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


# NodeGroupMemberTypeDef

### CacheClusterId
- **Type**: typing.Optional[str]

### CacheNodeId
- **Type**: typing.Optional[str]

### ReadEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.EndpointTypeDef]

### PreferredAvailabilityZone
- **Type**: typing.Optional[str]

### PreferredOutpostArn
- **Type**: typing.Optional[str]

### CurrentRole
- **Type**: typing.Optional[str]


# NodeGroupMemberUpdateStatusTypeDef

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


# NodeGroupTypeDef

### NodeGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### PrimaryEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.EndpointTypeDef]

### ReaderEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.EndpointTypeDef]

### Slots
- **Type**: typing.Optional[str]

### NodeGroupMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupMemberTypeDef]]


# NodeGroupUpdateStatusTypeDef

### NodeGroupId
- **Type**: typing.Optional[str]

### NodeGroupMemberUpdateStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupMemberUpdateStatusTypeDef]]


# NodeSnapshotTypeDef

### CacheClusterId
- **Type**: typing.Optional[str]

### NodeGroupId
- **Type**: typing.Optional[str]

### CacheNodeId
- **Type**: typing.Optional[str]

### NodeGroupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupConfigurationOutputTypeDef]

### CacheSize
- **Type**: typing.Optional[str]

### CacheNodeCreateTime
- **Type**: typing.Optional[datetime.datetime]

### SnapshotCreateTime
- **Type**: typing.Optional[datetime.datetime]


# NotificationConfigurationTypeDef

### TopicArn
- **Type**: typing.Optional[str]

### TopicStatus
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterNameValueTypeDef

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]


# ParameterTypeDef

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


# PendingLogDeliveryConfigurationTypeDef

### LogType
- **Type**: typing.Optional[typing.Literal['engine-log', 'slow-log']]

### DestinationType
- **Type**: typing.Optional[typing.Literal['cloudwatch-logs', 'kinesis-firehose']]

### DestinationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.DestinationDetailsTypeDef]

### LogFormat
- **Type**: typing.Optional[typing.Literal['json', 'text']]


# PendingModifiedValuesTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.PendingLogDeliveryConfigurationTypeDef]]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]


# ProcessedUpdateActionTypeDef

### ReplicationGroupId
- **Type**: typing.Optional[str]

### CacheClusterId
- **Type**: typing.Optional[str]

### ServiceUpdateName
- **Type**: typing.Optional[str]

### UpdateActionStatus
- **Type**: typing.Optional[typing.Literal['complete', 'in-progress', 'not-applicable', 'not-applied', 'scheduled', 'scheduling', 'stopped', 'stopping', 'waiting-to-start']]


# PurchaseReservedCacheNodesOfferingMessageRequestTypeDef

### ReservedCacheNodesOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedCacheNodeId
- **Type**: typing.Optional[str]

### CacheNodeCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]]


# PurchaseReservedCacheNodesOfferingResultTypeDef

### ReservedCacheNode
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReservedCacheNodeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef

### GlobalReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes


# RebalanceSlotsInGlobalReplicationGroupResultTypeDef

### GlobalReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RebootCacheClusterMessageRequestTypeDef

### CacheClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### CacheNodeIdsToReboot
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RebootCacheClusterResultTypeDef

### CacheCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecurringChargeTypeDef

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# RegionalConfigurationTypeDef

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroupRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ReshardingConfiguration
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ReshardingConfigurationTypeDef]
- **Required**: Yes


# RemoveTagsFromResourceMessageRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReplicationGroupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplicationGroupPendingModifiedValuesTypeDef

### PrimaryClusterId
- **Type**: typing.Optional[str]

### AutomaticFailoverStatus
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### Resharding
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.ReshardingStatusTypeDef]

### AuthTokenStatus
- **Type**: typing.Optional[typing.Literal['ROTATING', 'SETTING']]

### UserGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.UserGroupsUpdateStatusTypeDef]

### LogDeliveryConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.PendingLogDeliveryConfigurationTypeDef]]

### TransitEncryptionEnabled
- **Type**: typing.Optional[bool]

### TransitEncryptionMode
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]

### ClusterMode
- **Type**: typing.Optional[typing.Literal['compatible', 'disabled', 'enabled']]


# ReplicationGroupTypeDef

### ReplicationGroupId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### GlobalReplicationGroupInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.GlobalReplicationGroupInfoTypeDef]

### Status
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupPendingModifiedValuesTypeDef]

### MemberClusters
- **Type**: typing.Optional[typing.List[str]]

### NodeGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupTypeDef]]

### SnapshottingClusterId
- **Type**: typing.Optional[str]

### AutomaticFailover
- **Type**: typing.Optional[typing.Literal['disabled', 'disabling', 'enabled', 'enabling']]

### MultiAZ
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### ConfigurationEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.EndpointTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.LogDeliveryConfigurationTypeDef]]

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


# ReservedCacheNodeMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedCacheNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ReservedCacheNodeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReservedCacheNodeTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.RecurringChargeTypeDef]]

### ReservationARN
- **Type**: typing.Optional[str]


# ReservedCacheNodesOfferingMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedCacheNodesOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ReservedCacheNodesOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReservedCacheNodesOfferingTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.RecurringChargeTypeDef]]


# ResetCacheParameterGroupMessageRequestTypeDef

### CacheParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### ParameterNameValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.ParameterNameValueTypeDef]]


# ReshardingConfigurationTypeDef

### NodeGroupId
- **Type**: typing.Optional[str]

### PreferredAvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]


# ReshardingStatusTypeDef

### SlotMigration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.SlotMigrationTypeDef]


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


# RevokeCacheSecurityGroupIngressMessageRequestTypeDef

### CacheSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EC2SecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EC2SecurityGroupOwnerId
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeCacheSecurityGroupIngressResultTypeDef

### CacheSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.CacheSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SecurityGroupMembershipTypeDef

### SecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ServerlessCacheConfigurationTypeDef

### ServerlessCacheName
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]


# ServerlessCacheSnapshotTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.ServerlessCacheConfigurationTypeDef]


# ServerlessCacheTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.CacheUsageLimitsTypeDef]

### KmsKeyId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.EndpointTypeDef]

### ReaderEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.EndpointTypeDef]

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


# ServiceUpdateTypeDef

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


# ServiceUpdatesMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ServiceUpdateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SlotMigrationTypeDef

### ProgressPercentage
- **Type**: typing.Optional[float]


# SnapshotTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.NodeSnapshotTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### DataTiering
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]


# StartMigrationMessageRequestTypeDef

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerNodeEndpointList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.CustomerNodeEndpointTypeDef]
- **Required**: Yes


# StartMigrationResponseTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubnetOutpostTypeDef

### SubnetOutpostArn
- **Type**: typing.Optional[str]


# SubnetTypeDef

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.AvailabilityZoneTypeDef]

### SubnetOutpost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.SubnetOutpostTypeDef]

### SupportedNetworkTypes
- **Type**: typing.Optional[typing.List[typing.Literal['dual_stack', 'ipv4', 'ipv6']]]


# TagListMessageTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TestFailoverMessageRequestTypeDef

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# TestFailoverResultTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TestMigrationMessageRequestTypeDef

### ReplicationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerNodeEndpointList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elasticache_classes.CustomerNodeEndpointTypeDef]
- **Required**: Yes


# TestMigrationResponseTypeDef

### ReplicationGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ReplicationGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TimeRangeFilterTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UnprocessedUpdateActionTypeDef

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


# UpdateActionResultsMessageTypeDef

### ProcessedUpdateActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.ProcessedUpdateActionTypeDef]
- **Required**: Yes

### UnprocessedUpdateActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.UnprocessedUpdateActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateActionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.NodeGroupUpdateStatusTypeDef]]

### CacheNodeUpdateStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elasticache_classes.CacheNodeUpdateStatusTypeDef]]

### EstimatedUpdateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]


# UpdateActionsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elasticache_classes.UpdateActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserGroupPendingChangesTypeDef

### UserIdsToRemove
- **Type**: typing.Optional[typing.List[str]]

### UserIdsToAdd
- **Type**: typing.Optional[typing.List[str]]


# UserGroupResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.UserGroupPendingChangesTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserGroupTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.UserGroupPendingChangesTypeDef]

### ReplicationGroups
- **Type**: typing.Optional[typing.List[str]]

### ServerlessCaches
- **Type**: typing.Optional[typing.List[str]]

### ARN
- **Type**: typing.Optional[str]


# UserGroupsUpdateStatusTypeDef

### UserGroupIdsToAdd
- **Type**: typing.Optional[typing.List[str]]

### UserGroupIdsToRemove
- **Type**: typing.Optional[typing.List[str]]


# UserResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.AuthenticationTypeDef'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elasticache_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elasticache_classes.AuthenticationTypeDef]

### ARN
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



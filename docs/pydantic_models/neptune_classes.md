# Neptune Classes

# AddRoleToDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: typing.Optional[str]


# AddSourceIdentifierToSubscriptionMessageRequestTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# AddSourceIdentifierToSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddTagsToResourceMessageRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]
- **Required**: Yes


# ApplyPendingMaintenanceActionMessageRequestTypeDef

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyAction
- **Type**: <class 'str'>
- **Required**: Yes

### OptInType
- **Type**: <class 'str'>
- **Required**: Yes


# ApplyPendingMaintenanceActionResultTypeDef

### ResourcePendingMaintenanceActions
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResourcePendingMaintenanceActionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AvailabilityZoneTypeDef

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CharacterSetTypeDef

### CharacterSetName
- **Type**: typing.Optional[str]

### CharacterSetDescription
- **Type**: typing.Optional[str]


# CloudwatchLogsExportConfigurationTypeDef

### EnableLogTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### DisableLogTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# ClusterPendingModifiedValuesTypeDef

### PendingCloudwatchLogsExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PendingCloudwatchLogsExportsTypeDef]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Iops
- **Type**: typing.Optional[int]


# CopyDBClusterParameterGroupMessageRequestTypeDef

### SourceDBClusterParameterGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDBClusterParameterGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDBClusterParameterGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]


# CopyDBClusterParameterGroupResultTypeDef

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopyDBClusterSnapshotMessageRequestTypeDef

### SourceDBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### PreSignedUrl
- **Type**: typing.Optional[str]

### CopyTags
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]

### SourceRegion
- **Type**: typing.Optional[str]


# CopyDBClusterSnapshotResultTypeDef

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopyDBParameterGroupMessageRequestTypeDef

### SourceDBParameterGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDBParameterGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDBParameterGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]


# CopyDBParameterGroupResultTypeDef

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBClusterEndpointMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: <class 'str'>
- **Required**: Yes

### StaticMembers
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludedMembers
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]


# CreateDBClusterEndpointOutputTypeDef

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterEndpointResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: <class 'str'>
- **Required**: Yes

### CustomEndpointType
- **Type**: <class 'str'>
- **Required**: Yes

### StaticMembers
- **Type**: typing.List[str]
- **Required**: Yes

### ExcludedMembers
- **Type**: typing.List[str]
- **Required**: Yes

### DBClusterEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### CharacterSetName
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### DatabaseName
- **Type**: typing.Optional[str]

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]

### OptionGroupName
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReplicationSourceIdentifier
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### PreSignedUrl
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.ServerlessV2ScalingConfigurationTypeDef]

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### SourceRegion
- **Type**: typing.Optional[str]


# CreateDBClusterParameterGroupMessageRequestTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]


# CreateDBClusterParameterGroupResultTypeDef

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBClusterSnapshotMessageRequestTypeDef

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]


# CreateDBClusterSnapshotResultTypeDef

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBInstanceMessageRequestTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstanceClass
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBName
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]

### DBSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### DBParameterGroupName
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### CharacterSetName
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### TdeCredentialPassword
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]

### Timezone
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]


# CreateDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBParameterGroupMessageRequestTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]


# CreateDBParameterGroupResultTypeDef

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBSubnetGroupMessageRequestTypeDef

### DBSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DBSubnetGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]


# CreateDBSubnetGroupResultTypeDef

### DBSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventSubscriptionMessageRequestTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### SourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]


# CreateEventSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGlobalClusterMessageRequestTypeDef

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDBClusterIdentifier
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### StorageEncrypted
- **Type**: typing.Optional[bool]


# CreateGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterEndpointMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBClusterEndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterEndpointTypeDef

### DBClusterEndpointIdentifier
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterEndpointResourceIdentifier
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[str]

### CustomEndpointType
- **Type**: typing.Optional[str]

### StaticMembers
- **Type**: typing.Optional[typing.List[str]]

### ExcludedMembers
- **Type**: typing.Optional[typing.List[str]]

### DBClusterEndpointArn
- **Type**: typing.Optional[str]


# DBClusterMemberTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### IsClusterWriter
- **Type**: typing.Optional[bool]

### DBClusterParameterGroupStatus
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]


# DBClusterMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterOptionGroupStatusTypeDef

### DBClusterOptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# DBClusterParameterGroupDetailsTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.ParameterTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterParameterGroupNameMessageTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterParameterGroupTypeDef

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DBClusterParameterGroupArn
- **Type**: typing.Optional[str]


# DBClusterParameterGroupsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBClusterParameterGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterRoleTypeDef

### RoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### FeatureName
- **Type**: typing.Optional[str]


# DBClusterSnapshotAttributeTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[str]]


# DBClusterSnapshotAttributesResultTypeDef

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBClusterSnapshotAttributeTypeDef]]


# DBClusterSnapshotMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBClusterSnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterSnapshotTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotCreateTime
- **Type**: typing.Optional[datetime.datetime]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DBClusterSnapshotArn
- **Type**: typing.Optional[str]

### SourceDBClusterSnapshotArn
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### StorageType
- **Type**: typing.Optional[str]


# DBClusterTypeDef

### AllocatedStorage
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### CharacterSetName
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterParameterGroup
- **Type**: typing.Optional[str]

### DBSubnetGroup
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[str]

### EarliestRestorableTime
- **Type**: typing.Optional[datetime.datetime]

### Endpoint
- **Type**: typing.Optional[str]

### ReaderEndpoint
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LatestRestorableTime
- **Type**: typing.Optional[datetime.datetime]

### Port
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### DBClusterOptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBClusterOptionGroupStatusTypeDef]]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReplicationSourceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DBClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBClusterMemberTypeDef]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.VpcSecurityGroupMembershipTypeDef]]

### HostedZoneId
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### DBClusterArn
- **Type**: typing.Optional[str]

### AssociatedRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBClusterRoleTypeDef]]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### CloneGroupId
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### EnabledCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.ClusterPendingModifiedValuesTypeDef]

### DeletionProtection
- **Type**: typing.Optional[bool]

### CrossAccountClone
- **Type**: typing.Optional[bool]

### AutomaticRestartTime
- **Type**: typing.Optional[datetime.datetime]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.ServerlessV2ScalingConfigurationInfoTypeDef]

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### IOOptimizedNextAllowedModificationTime
- **Type**: typing.Optional[datetime.datetime]

### StorageType
- **Type**: typing.Optional[str]


# DBEngineVersionMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBEngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBEngineVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBEngineVersionTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### DBEngineDescription
- **Type**: typing.Optional[str]

### DBEngineVersionDescription
- **Type**: typing.Optional[str]

### DefaultCharacterSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.CharacterSetTypeDef]

### SupportedCharacterSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.CharacterSetTypeDef]]

### ValidUpgradeTarget
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.UpgradeTargetTypeDef]]

### SupportedTimezones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.TimezoneTypeDef]]

### ExportableLogTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportsLogExportsToCloudwatchLogs
- **Type**: typing.Optional[bool]

### SupportsReadReplica
- **Type**: typing.Optional[bool]

### SupportsGlobalDatabases
- **Type**: typing.Optional[bool]


# DBInstanceMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBInstanceStatusInfoTypeDef

### StatusType
- **Type**: typing.Optional[str]

### Normal
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# DBInstanceTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### DBInstanceStatus
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.EndpointTypeDef]

### AllocatedStorage
- **Type**: typing.Optional[int]

### InstanceCreateTime
- **Type**: typing.Optional[datetime.datetime]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DBSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBSecurityGroupMembershipTypeDef]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.VpcSecurityGroupMembershipTypeDef]]

### DBParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBParameterGroupStatusTypeDef]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DBSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.DBSubnetGroupTypeDef]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PendingModifiedValuesTypeDef]

### LatestRestorableTime
- **Type**: typing.Optional[datetime.datetime]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### ReadReplicaSourceDBInstanceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaDBInstanceIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### ReadReplicaDBClusterIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.OptionGroupMembershipTypeDef]]

### CharacterSetName
- **Type**: typing.Optional[str]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBInstanceStatusInfoTypeDef]]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### DbInstancePort
- **Type**: typing.Optional[int]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbiResourceId
- **Type**: typing.Optional[str]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### DomainMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.DomainMembershipTypeDef]]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### EnhancedMonitoringResourceArn
- **Type**: typing.Optional[str]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]

### DBInstanceArn
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### EnabledCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]


# DBParameterGroupDetailsTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.ParameterTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBParameterGroupNameMessageTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBParameterGroupStatusTypeDef

### DBParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]


# DBParameterGroupTypeDef

### DBParameterGroupName
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DBParameterGroupArn
- **Type**: typing.Optional[str]


# DBParameterGroupsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBParameterGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBSecurityGroupMembershipTypeDef

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# DBSubnetGroupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.DBSubnetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBSubnetGroupTypeDef

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### DBSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.SubnetTypeDef]]

### DBSubnetGroupArn
- **Type**: typing.Optional[str]


# DeleteDBClusterEndpointMessageRequestTypeDef

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterEndpointOutputTypeDef

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterEndpointResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: <class 'str'>
- **Required**: Yes

### CustomEndpointType
- **Type**: <class 'str'>
- **Required**: Yes

### StaticMembers
- **Type**: typing.List[str]
- **Required**: Yes

### ExcludedMembers
- **Type**: typing.List[str]
- **Required**: Yes

### DBClusterEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]


# DeleteDBClusterParameterGroupMessageRequestTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBClusterSnapshotMessageRequestTypeDef

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterSnapshotResultTypeDef

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBInstanceMessageRequestTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]


# DeleteDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBParameterGroupMessageRequestTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBSubnetGroupMessageRequestTypeDef

### DBSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionMessageRequestTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGlobalClusterMessageRequestTypeDef

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterEndpointIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBClusterEndpointsMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterEndpointIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBClusterParameterGroupsMessageRequestTypeDef

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBClusterParametersMessageRequestTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterSnapshotAttributesMessageRequestTypeDef

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDBClusterSnapshotAttributesResultTypeDef

### DBClusterSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterSnapshotAttributesResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBClusterSnapshotsMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]


# DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBClustersMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### DefaultOnly
- **Type**: typing.Optional[bool]

### ListSupportedCharacterSets
- **Type**: typing.Optional[bool]

### ListSupportedTimezones
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBEngineVersionsMessageRequestTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### DefaultOnly
- **Type**: typing.Optional[bool]

### ListSupportedCharacterSets
- **Type**: typing.Optional[bool]

### ListSupportedTimezones
- **Type**: typing.Optional[bool]


# DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.WaiterConfigTypeDef]


# DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.WaiterConfigTypeDef]


# DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBInstancesMessageRequestTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateTypeDef

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBParameterGroupsMessageRequestTypeDef

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBParametersMessageDescribeDBParametersPaginateTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBParametersMessageRequestTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeDBSubnetGroupsMessageRequestTypeDef

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultClusterParametersMessageRequestTypeDef

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultClusterParametersResultTypeDef

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.EngineDefaultsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeEngineDefaultParametersMessageRequestTypeDef

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultParametersResultTypeDef

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.EngineDefaultsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventCategoriesMessageRequestTypeDef

### SourceType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]


# DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeEventSubscriptionsMessageRequestTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventsMessageDescribeEventsPaginateTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['db-cluster', 'db-cluster-snapshot', 'db-instance', 'db-parameter-group', 'db-security-group', 'db-snapshot']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeEventsMessageRequestTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['db-cluster', 'db-cluster-snapshot', 'db-instance', 'db-parameter-group', 'db-security-group', 'db-snapshot']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeGlobalClustersMessageRequestTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PaginatorConfigTypeDef]


# DescribeOrderableDBInstanceOptionsMessageRequestTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribePendingMaintenanceActionsMessageRequestTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeValidDBInstanceModificationsMessageRequestTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeValidDBInstanceModificationsResultTypeDef

### ValidDBInstanceModificationsMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ValidDBInstanceModificationsMessageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainMembershipTypeDef

### Domain
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### FQDN
- **Type**: typing.Optional[str]

### IAMRoleName
- **Type**: typing.Optional[str]


# DoubleRangeTypeDef

### From
- **Type**: typing.Optional[float]

### To
- **Type**: typing.Optional[float]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### HostedZoneId
- **Type**: typing.Optional[str]


# EngineDefaultsTypeDef

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.ParameterTypeDef]]


# EventCategoriesMapTypeDef

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]


# EventCategoriesMessageTypeDef

### EventCategoriesMapList
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.EventCategoriesMapTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventSubscriptionTypeDef

### CustomerAwsId
- **Type**: typing.Optional[str]

### CustSubscriptionId
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SubscriptionCreationTime
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### SourceIdsList
- **Type**: typing.Optional[typing.List[str]]

### EventCategoriesList
- **Type**: typing.Optional[typing.List[str]]

### Enabled
- **Type**: typing.Optional[bool]

### EventSubscriptionArn
- **Type**: typing.Optional[str]


# EventSubscriptionsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### EventSubscriptionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.EventSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['db-cluster', 'db-cluster-snapshot', 'db-instance', 'db-parameter-group', 'db-security-group', 'db-snapshot']]

### Message
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]

### Date
- **Type**: typing.Optional[datetime.datetime]

### SourceArn
- **Type**: typing.Optional[str]


# EventsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailoverDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### TargetDBInstanceIdentifier
- **Type**: typing.Optional[str]


# FailoverDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailoverGlobalClusterMessageRequestTypeDef

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDbClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# FailoverGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GlobalClusterMemberTypeDef

### DBClusterArn
- **Type**: typing.Optional[str]

### Readers
- **Type**: typing.Optional[typing.List[str]]

### IsWriter
- **Type**: typing.Optional[bool]


# GlobalClusterTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### GlobalClusterResourceId
- **Type**: typing.Optional[str]

### GlobalClusterArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### DeletionProtection
- **Type**: typing.Optional[bool]

### GlobalClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.GlobalClusterMemberTypeDef]]


# GlobalClustersMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.GlobalClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceMessageRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.FilterTypeDef]]


# ModifyDBClusterEndpointMessageRequestTypeDef

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: typing.Optional[str]

### StaticMembers
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludedMembers
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyDBClusterEndpointOutputTypeDef

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterEndpointResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: <class 'str'>
- **Required**: Yes

### CustomEndpointType
- **Type**: <class 'str'>
- **Required**: Yes

### StaticMembers
- **Type**: typing.List[str]
- **Required**: Yes

### ExcludedMembers
- **Type**: typing.List[str]
- **Required**: Yes

### DBClusterEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NewDBClusterIdentifier
- **Type**: typing.Optional[str]

### ApplyImmediately
- **Type**: typing.Optional[bool]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Port
- **Type**: typing.Optional[int]

### MasterUserPassword
- **Type**: typing.Optional[str]

### OptionGroupName
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### CloudwatchLogsExportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.CloudwatchLogsExportConfigurationTypeDef]

### EngineVersion
- **Type**: typing.Optional[str]

### AllowMajorVersionUpgrade
- **Type**: typing.Optional[bool]

### DBInstanceParameterGroupName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.ServerlessV2ScalingConfigurationTypeDef]

### StorageType
- **Type**: typing.Optional[str]


# ModifyDBClusterParameterGroupMessageRequestTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.ParameterTypeDef]
- **Required**: Yes


# ModifyDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBClusterSnapshotAttributeMessageRequestTypeDef

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ValuesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### ValuesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyDBClusterSnapshotAttributeResultTypeDef

### DBClusterSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterSnapshotAttributesResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBInstanceMessageRequestTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AllocatedStorage
- **Type**: typing.Optional[int]

### DBInstanceClass
- **Type**: typing.Optional[str]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### DBSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ApplyImmediately
- **Type**: typing.Optional[bool]

### MasterUserPassword
- **Type**: typing.Optional[str]

### DBParameterGroupName
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### AllowMajorVersionUpgrade
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### NewDBInstanceIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### TdeCredentialPassword
- **Type**: typing.Optional[str]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### DBPortNumber
- **Type**: typing.Optional[int]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### CloudwatchLogsExportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.CloudwatchLogsExportConfigurationTypeDef]

### DeletionProtection
- **Type**: typing.Optional[bool]


# ModifyDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBParameterGroupMessageRequestTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.ParameterTypeDef]
- **Required**: Yes


# ModifyDBSubnetGroupMessageRequestTypeDef

### DBSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DBSubnetGroupDescription
- **Type**: typing.Optional[str]


# ModifyDBSubnetGroupResultTypeDef

### DBSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyEventSubscriptionMessageRequestTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]


# ModifyEventSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyGlobalClusterMessageRequestTypeDef

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NewGlobalClusterIdentifier
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### AllowMajorVersionUpgrade
- **Type**: typing.Optional[bool]


# ModifyGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OptionGroupMembershipTypeDef

### OptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# OrderableDBInstanceOptionTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.AvailabilityZoneTypeDef]]

### MultiAZCapable
- **Type**: typing.Optional[bool]

### ReadReplicaCapable
- **Type**: typing.Optional[bool]

### Vpc
- **Type**: typing.Optional[bool]

### SupportsStorageEncryption
- **Type**: typing.Optional[bool]

### StorageType
- **Type**: typing.Optional[str]

### SupportsIops
- **Type**: typing.Optional[bool]

### SupportsEnhancedMonitoring
- **Type**: typing.Optional[bool]

### SupportsIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### SupportsPerformanceInsights
- **Type**: typing.Optional[bool]

### MinStorageSize
- **Type**: typing.Optional[int]

### MaxStorageSize
- **Type**: typing.Optional[int]

### MinIopsPerDbInstance
- **Type**: typing.Optional[int]

### MaxIopsPerDbInstance
- **Type**: typing.Optional[int]

### MinIopsPerGib
- **Type**: typing.Optional[float]

### MaxIopsPerGib
- **Type**: typing.Optional[float]

### SupportsGlobalDatabases
- **Type**: typing.Optional[bool]


# OrderableDBInstanceOptionsMessageTypeDef

### OrderableDBInstanceOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.OrderableDBInstanceOptionTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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

### ApplyType
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]

### IsModifiable
- **Type**: typing.Optional[bool]

### MinimumEngineVersion
- **Type**: typing.Optional[str]

### ApplyMethod
- **Type**: typing.Optional[typing.Literal['immediate', 'pending-reboot']]


# PendingCloudwatchLogsExportsTypeDef

### LogTypesToEnable
- **Type**: typing.Optional[typing.List[str]]

### LogTypesToDisable
- **Type**: typing.Optional[typing.List[str]]


# PendingMaintenanceActionTypeDef

### Action
- **Type**: typing.Optional[str]

### AutoAppliedAfterDate
- **Type**: typing.Optional[datetime.datetime]

### ForcedApplyDate
- **Type**: typing.Optional[datetime.datetime]

### OptInStatus
- **Type**: typing.Optional[str]

### CurrentApplyDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]


# PendingMaintenanceActionsMessageTypeDef

### PendingMaintenanceActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.ResourcePendingMaintenanceActionsTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PendingModifiedValuesTypeDef

### DBInstanceClass
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### MasterUserPassword
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### PendingCloudwatchLogsExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.PendingCloudwatchLogsExportsTypeDef]


# PromoteReadReplicaDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PromoteReadReplicaDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RangeTypeDef

### From
- **Type**: typing.Optional[int]

### To
- **Type**: typing.Optional[int]

### Step
- **Type**: typing.Optional[int]


# RebootDBInstanceMessageRequestTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ForceFailover
- **Type**: typing.Optional[bool]


# RebootDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveFromGlobalClusterMessageRequestTypeDef

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DbClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFromGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveRoleFromDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: typing.Optional[str]


# RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveSourceIdentifierFromSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTagsFromResourceMessageRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResetDBClusterParameterGroupMessageRequestTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.ParameterTypeDef]]


# ResetDBParameterGroupMessageRequestTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.ParameterTypeDef]]


# ResourcePendingMaintenanceActionsTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### PendingMaintenanceActionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.PendingMaintenanceActionTypeDef]]


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


# RestoreDBClusterFromSnapshotMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### EngineVersion
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### OptionGroupName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.ServerlessV2ScalingConfigurationTypeDef]

### StorageType
- **Type**: typing.Optional[str]


# RestoreDBClusterFromSnapshotResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreDBClusterToPointInTimeMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreType
- **Type**: typing.Optional[str]

### RestoreToTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### UseLatestRestorableTime
- **Type**: typing.Optional[bool]

### Port
- **Type**: typing.Optional[int]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### OptionGroupName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.ServerlessV2ScalingConfigurationTypeDef]

### StorageType
- **Type**: typing.Optional[str]


# RestoreDBClusterToPointInTimeResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServerlessV2ScalingConfigurationInfoTypeDef

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]


# ServerlessV2ScalingConfigurationTypeDef

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]


# StartDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubnetTypeDef

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_classes.AvailabilityZoneTypeDef]

### SubnetStatus
- **Type**: typing.Optional[str]


# TagListMessageTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TimezoneTypeDef

### TimezoneName
- **Type**: typing.Optional[str]


# UpgradeTargetTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### AutoUpgrade
- **Type**: typing.Optional[bool]

### IsMajorVersionUpgrade
- **Type**: typing.Optional[bool]

### SupportsGlobalDatabases
- **Type**: typing.Optional[bool]


# ValidDBInstanceModificationsMessageTypeDef

### Storage
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.ValidStorageOptionsTypeDef]]


# ValidStorageOptionsTypeDef

### StorageType
- **Type**: typing.Optional[str]

### StorageSize
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.RangeTypeDef]]

### ProvisionedIops
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.RangeTypeDef]]

### IopsToStorageRatio
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_classes.DoubleRangeTypeDef]]


# VpcSecurityGroupMembershipTypeDef

### VpcSecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



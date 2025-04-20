# Neptune Neptune Classes

# AddRoleToDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: typing.Optional[str]


# AddSourceIdentifierToSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# AddSourceIdentifierToSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsToResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]
- **Required**: Yes


# ApplyPendingMaintenanceActionMessage

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyAction
- **Type**: <class 'str'>
- **Required**: Yes

### OptInType
- **Type**: <class 'str'>
- **Required**: Yes


# ApplyPendingMaintenanceActionResult

### ResourcePendingMaintenanceActions
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResourcePendingMaintenanceActions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# AvailabilityZone

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CharacterSet

### CharacterSetName
- **Type**: typing.Optional[str]

### CharacterSetDescription
- **Type**: typing.Optional[str]


# CloudwatchLogsExportConfiguration

### EnableLogTypes
- **Type**: typing.Optional[typing.List[str]]

### DisableLogTypes
- **Type**: typing.Optional[typing.List[str]]


# ClusterPendingModifiedValues

### PendingCloudwatchLogsExports
- **Type**: <class 'NoneType'>

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


# CopyDBClusterParameterGroupMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]


# CopyDBClusterParameterGroupResult

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CopyDBClusterSnapshotMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]

### SourceRegion
- **Type**: typing.Optional[str]


# CopyDBClusterSnapshotResult

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CopyDBParameterGroupMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]


# CopyDBParameterGroupResult

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBClusterEndpointMessage

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
- **Type**: typing.Optional[typing.List[str]]

### ExcludedMembers
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]


# CreateDBClusterEndpointOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### PreSignedUrl
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### ServerlessV2ScalingConfiguration
- **Type**: <class 'NoneType'>

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### SourceRegion
- **Type**: typing.Optional[str]


# CreateDBClusterParameterGroupMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]


# CreateDBClusterParameterGroupResult

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBClusterSnapshotMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]


# CreateDBClusterSnapshotResult

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBInstanceMessage

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
- **Type**: typing.Optional[typing.List[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]

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
- **Type**: typing.Optional[typing.List[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]


# CreateDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBParameterGroupMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]


# CreateDBParameterGroupResult

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBSubnetGroupMessage

### DBSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DBSubnetGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]


# CreateDBSubnetGroupResult

### DBSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]

### SourceIds
- **Type**: typing.Optional[typing.List[str]]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]


# CreateEventSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGlobalClusterMessage

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


# CreateGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBCluster

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterOptionGroupStatus]]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReplicationSourceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DBClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterMember]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.VpcSecurityGroupMembership]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterRole]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.ClusterPendingModifiedValues]

### DeletionProtection
- **Type**: typing.Optional[bool]

### CrossAccountClone
- **Type**: typing.Optional[bool]

### AutomaticRestartTime
- **Type**: typing.Optional[datetime.datetime]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.ServerlessV2ScalingConfigurationInfo]

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### IOOptimizedNextAllowedModificationTime
- **Type**: typing.Optional[datetime.datetime]

### StorageType
- **Type**: typing.Optional[str]


# DBClusterEndpoint

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


# DBClusterEndpointMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterEndpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterMember

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### IsClusterWriter
- **Type**: typing.Optional[bool]

### DBClusterParameterGroupStatus
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]


# DBClusterMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterOptionGroupStatus

### DBClusterOptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# DBClusterParameterGroup

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DBClusterParameterGroupArn
- **Type**: typing.Optional[str]


# DBClusterParameterGroupDetails

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Parameter]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterParameterGroupNameMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterParameterGroupsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterParameterGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterRole

### RoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### FeatureName
- **Type**: typing.Optional[str]


# DBClusterSnapshot

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


# DBClusterSnapshotAttribute

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[str]]


# DBClusterSnapshotAttributesResult

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterSnapshotAttribute]]


# DBClusterSnapshotMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterSnapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBEngineVersion

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.CharacterSet]

### SupportedCharacterSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.CharacterSet]]

### ValidUpgradeTarget
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.UpgradeTarget]]

### SupportedTimezones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Timezone]]

### ExportableLogTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportsLogExportsToCloudwatchLogs
- **Type**: typing.Optional[bool]

### SupportsReadReplica
- **Type**: typing.Optional[bool]

### SupportsGlobalDatabases
- **Type**: typing.Optional[bool]


# DBEngineVersionMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBEngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBEngineVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBInstance

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
- **Type**: <class 'NoneType'>

### AllocatedStorage
- **Type**: typing.Optional[int]

### InstanceCreateTime
- **Type**: typing.Optional[datetime.datetime]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DBSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBSecurityGroupMembership]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.VpcSecurityGroupMembership]]

### DBParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBParameterGroupStatus]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DBSubnetGroup
- **Type**: <class 'NoneType'>

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.OptionGroupMembership]]

### CharacterSetName
- **Type**: typing.Optional[str]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBInstanceStatusInfo]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DomainMembership]]

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


# DBInstanceMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBInstanceStatusInfo

### StatusType
- **Type**: typing.Optional[str]

### Normal
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# DBParameterGroup

### DBParameterGroupName
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DBParameterGroupArn
- **Type**: typing.Optional[str]


# DBParameterGroupDetails

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Parameter]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBParameterGroupNameMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBParameterGroupStatus

### DBParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]


# DBParameterGroupsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBParameterGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DBSecurityGroupMembership

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# DBSubnetGroup

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### DBSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Subnet]]

### DBSubnetGroupArn
- **Type**: typing.Optional[str]


# DBSubnetGroupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DBSubnetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBClusterEndpointMessage

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterEndpointOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]


# DeleteDBClusterParameterGroupMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBClusterSnapshotMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterSnapshotResult

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]


# DeleteDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBParameterGroupMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBSubnetGroupMessage

### DBSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGlobalClusterMessage

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBClusterEndpointsMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterEndpointIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterEndpointsMessagePaginate

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterEndpointIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeDBClusterParameterGroupsMessage

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterParameterGroupsMessagePaginate

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeDBClusterParametersMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterParametersMessagePaginate

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeDBClusterSnapshotAttributesMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDBClusterSnapshotAttributesResult

### DBClusterSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterSnapshotAttributesResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBClusterSnapshotsMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]


# DescribeDBClusterSnapshotsMessagePaginate

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeDBClustersMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClustersMessagePaginate

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeDBEngineVersionsMessage

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

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


# DescribeDBEngineVersionsMessagePaginate

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### DefaultOnly
- **Type**: typing.Optional[bool]

### ListSupportedCharacterSets
- **Type**: typing.Optional[bool]

### ListSupportedTimezones
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeDBInstancesMessage

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBInstancesMessagePaginate

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeDBInstancesMessageWait

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeDBInstancesMessageWaitExtra

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeDBParameterGroupsMessage

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBParameterGroupsMessagePaginate

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeDBParametersMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBParametersMessagePaginate

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeDBSubnetGroupsMessage

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBSubnetGroupsMessagePaginate

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeEngineDefaultClusterParametersMessage

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultClusterParametersResult

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.EngineDefaults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEngineDefaultParametersMessage

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultParametersMessagePaginate

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeEngineDefaultParametersResult

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.EngineDefaults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventCategoriesMessage

### SourceType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]


# DescribeEventSubscriptionsMessage

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventSubscriptionsMessagePaginate

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeEventsMessage

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
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventsMessagePaginate

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
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeGlobalClustersMessage

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeGlobalClustersMessagePaginate

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeOrderableDBInstanceOptionsMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeOrderableDBInstanceOptionsMessagePaginate

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribePendingMaintenanceActionsMessage

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribePendingMaintenanceActionsMessagePaginate

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.PaginatorConfig]


# DescribeValidDBInstanceModificationsMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeValidDBInstanceModificationsResult

### ValidDBInstanceModificationsMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ValidDBInstanceModificationsMessage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# DomainMembership

### Domain
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### FQDN
- **Type**: typing.Optional[str]

### IAMRoleName
- **Type**: typing.Optional[str]


# DoubleRange

### From
- **Type**: typing.Optional[float]

### To
- **Type**: typing.Optional[float]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### HostedZoneId
- **Type**: typing.Optional[str]


# EngineDefaults

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Parameter]]


# Event

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


# EventCategoriesMap

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]


# EventCategoriesMessage

### EventCategoriesMapList
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.EventCategoriesMap]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# EventSubscription

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


# EventSubscriptionsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### EventSubscriptionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.EventSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# EventsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# FailoverDBClusterMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### TargetDBInstanceIdentifier
- **Type**: typing.Optional[str]


# FailoverDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# FailoverGlobalClusterMessage

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDbClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# FailoverGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# Filter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# GlobalCluster

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.GlobalClusterMember]]


# GlobalClusterMember

### DBClusterArn
- **Type**: typing.Optional[str]

### Readers
- **Type**: typing.Optional[typing.List[str]]

### IsWriter
- **Type**: typing.Optional[bool]


# GlobalClustersMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.GlobalCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Filter]]


# ModifyDBClusterEndpointMessage

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: typing.Optional[str]

### StaticMembers
- **Type**: typing.Optional[typing.List[str]]

### ExcludedMembers
- **Type**: typing.Optional[typing.List[str]]


# ModifyDBClusterEndpointOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBClusterMessage

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
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

### StorageType
- **Type**: typing.Optional[str]


# ModifyDBClusterParameterGroupMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Parameter]
- **Required**: Yes


# ModifyDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBClusterSnapshotAttributeMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ValuesToAdd
- **Type**: typing.Optional[typing.List[str]]

### ValuesToRemove
- **Type**: typing.Optional[typing.List[str]]


# ModifyDBClusterSnapshotAttributeResult

### DBClusterSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBClusterSnapshotAttributesResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBInstanceMessage

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
- **Type**: typing.Optional[typing.List[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: <class 'NoneType'>

### DeletionProtection
- **Type**: typing.Optional[bool]


# ModifyDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBParameterGroupMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Parameter]
- **Required**: Yes


# ModifyDBSubnetGroupMessage

### DBSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### DBSubnetGroupDescription
- **Type**: typing.Optional[str]


# ModifyDBSubnetGroupResult

### DBSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyEventSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]

### Enabled
- **Type**: typing.Optional[bool]


# ModifyEventSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyGlobalClusterMessage

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


# ModifyGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# OptionGroupMembership

### OptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# OrderableDBInstanceOption

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.AvailabilityZone]]

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


# OrderableDBInstanceOptionsMessage

### OrderableDBInstanceOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.OrderableDBInstanceOption]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


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


# PendingCloudwatchLogsExports

### LogTypesToEnable
- **Type**: typing.Optional[typing.List[str]]

### LogTypesToDisable
- **Type**: typing.Optional[typing.List[str]]


# PendingMaintenanceAction

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


# PendingMaintenanceActionsMessage

### PendingMaintenanceActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.ResourcePendingMaintenanceActions]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# PendingModifiedValues

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
- **Type**: <class 'NoneType'>


# PromoteReadReplicaDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PromoteReadReplicaDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# Range

### From
- **Type**: typing.Optional[int]

### To
- **Type**: typing.Optional[int]

### Step
- **Type**: typing.Optional[int]


# RebootDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ForceFailover
- **Type**: typing.Optional[bool]


# RebootDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveFromGlobalClusterMessage

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DbClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveFromGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveRoleFromDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: typing.Optional[str]


# RemoveSourceIdentifierFromSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveSourceIdentifierFromSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsFromResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# ResetDBClusterParameterGroupMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Parameter]]


# ResetDBParameterGroupMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Parameter]]


# ResourcePendingMaintenanceActions

### ResourceIdentifier
- **Type**: typing.Optional[str]

### PendingMaintenanceActionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.PendingMaintenanceAction]]


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


# RestoreDBClusterFromSnapshotMessage

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
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### ServerlessV2ScalingConfiguration
- **Type**: <class 'NoneType'>

### StorageType
- **Type**: typing.Optional[str]


# RestoreDBClusterFromSnapshotResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreDBClusterToPointInTimeMessage

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
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### ServerlessV2ScalingConfiguration
- **Type**: <class 'NoneType'>

### StorageType
- **Type**: typing.Optional[str]


# RestoreDBClusterToPointInTimeResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# ServerlessV2ScalingConfiguration

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]


# ServerlessV2ScalingConfigurationInfo

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]


# StartDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# StopDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# Subnet

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune.neptune_classes.AvailabilityZone]

### SubnetStatus
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagListMessage

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune.neptune_classes.ResponseMetadata'>
- **Required**: Yes


# Timezone

### TimezoneName
- **Type**: typing.Optional[str]


# UpgradeTarget

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


# ValidDBInstanceModificationsMessage

### Storage
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.ValidStorageOptions]]


# ValidStorageOptions

### StorageType
- **Type**: typing.Optional[str]

### StorageSize
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Range]]

### ProvisionedIops
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.Range]]

### IopsToStorageRatio
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune.neptune_classes.DoubleRange]]


# VpcSecurityGroupMembership

### VpcSecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



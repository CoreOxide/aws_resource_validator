# Docdb Classes

# AddSourceIdentifierToSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# AddSourceIdentifierToSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsToResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResourcePendingMaintenanceActions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# AvailabilityZone

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Certificate

### CertificateIdentifier
- **Type**: typing.Optional[str]

### CertificateType
- **Type**: typing.Optional[str]

### Thumbprint
- **Type**: typing.Optional[str]

### ValidFrom
- **Type**: typing.Optional[datetime.datetime]

### ValidTill
- **Type**: typing.Optional[datetime.datetime]

### CertificateArn
- **Type**: typing.Optional[str]


# CertificateDetails

### CAIdentifier
- **Type**: typing.Optional[str]

### ValidTill
- **Type**: typing.Optional[datetime.datetime]


# CertificateMessage

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.Certificate]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# CloudwatchLogsExportConfiguration

### EnableLogTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### DisableLogTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# ClusterMasterUserSecret

### SecretArn
- **Type**: typing.Optional[str]

### SecretStatus
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]


# CopyDBClusterParameterGroupResult

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBClusterParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]

### SourceRegion
- **Type**: typing.Optional[str]


# CopyDBClusterSnapshotResult

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBClusterMessage

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

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### PreSignedUrl
- **Type**: typing.Optional[str]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### ManageMasterUserPassword
- **Type**: typing.Optional[bool]

### MasterUserSecretKmsKeyId
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]


# CreateDBClusterParameterGroupResult

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBClusterParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBClusterSnapshotMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]


# CreateDBClusterSnapshotResult

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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

### AvailabilityZone
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### PromotionTier
- **Type**: typing.Optional[int]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### CACertificateIdentifier
- **Type**: typing.Optional[str]


# CreateDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBSubnetGroupMessage

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]


# CreateDBSubnetGroupResult

### DBSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[str]]

### SourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]


# CreateEventSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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

### DatabaseName
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]


# CreateGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DBCluster

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

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

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReplicationSourceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DBClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBClusterMember]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.VpcSecurityGroupMembership]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBClusterRole]]

### CloneGroupId
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### EnabledCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### StorageType
- **Type**: typing.Optional[str]

### MasterUserSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.ClusterMasterUserSecret]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.Parameter]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterParameterGroupNameMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterParameterGroupsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBClusterParameterGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterRole

### RoleArn
- **Type**: typing.Optional[str]

### Status
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBClusterSnapshotAttribute]]


# DBClusterSnapshotMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBClusterSnapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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

### ValidUpgradeTarget
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.UpgradeTarget]]

### ExportableLogTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportsLogExportsToCloudwatchLogs
- **Type**: typing.Optional[bool]

### SupportedCACertificateIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### SupportsCertificateRotationWithoutRestart
- **Type**: typing.Optional[bool]


# DBEngineVersionMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBEngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBEngineVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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

### Endpoint
- **Type**: <class 'NoneType'>

### InstanceCreateTime
- **Type**: typing.Optional[datetime.datetime]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.VpcSecurityGroupMembership]]

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

### EngineVersion
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBInstanceStatusInfo]]

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

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### PromotionTier
- **Type**: typing.Optional[int]

### DBInstanceArn
- **Type**: typing.Optional[str]

### EnabledCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### CertificateDetails
- **Type**: <class 'NoneType'>

### PerformanceInsightsEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]


# DBInstanceMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.Subnet]]

### DBSubnetGroupArn
- **Type**: typing.Optional[str]


# DBSubnetGroupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.DBSubnetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBClusterSnapshotMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterSnapshotResult

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGlobalClusterMessage

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCertificatesMessage

### CertificateIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCertificatesMessagePaginate

### CertificateIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeDBClusterParameterGroupsMessage

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterParameterGroupsMessagePaginate

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeDBClusterParametersMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeDBClusterSnapshotAttributesMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDBClusterSnapshotAttributesResult

### DBClusterSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBClusterSnapshotAttributesResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBClusterSnapshotsMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeDBClustersMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClustersMessagePaginate

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeDBEngineVersionsMessage

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### DefaultOnly
- **Type**: typing.Optional[bool]

### ListSupportedCharacterSets
- **Type**: typing.Optional[bool]

### ListSupportedTimezones
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeDBInstancesMessage

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBInstancesMessagePaginate

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeDBInstancesMessageWait

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeDBSubnetGroupsMessage

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBSubnetGroupsMessagePaginate

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeEngineDefaultClusterParametersMessage

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultClusterParametersResult

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.EngineDefaults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventCategoriesMessage

### SourceType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]


# DescribeEventSubscriptionsMessage

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventSubscriptionsMessagePaginate

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeEventsMessage

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['db-cluster', 'db-cluster-snapshot', 'db-instance', 'db-parameter-group', 'db-security-group', 'db-snapshot']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.Timestamp]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.Timestamp]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribeGlobalClustersMessage

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeGlobalClustersMessagePaginate

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# DescribePendingMaintenanceActionsMessage

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribePendingMaintenanceActionsMessagePaginate

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.PaginatorConfig]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.Parameter]]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.EventCategoriesMap]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.EventSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# EventsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# FailoverDBClusterMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### TargetDBInstanceIdentifier
- **Type**: typing.Optional[str]


# FailoverDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# FailoverGlobalClusterMessage

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDbClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AllowDataLoss
- **Type**: typing.Optional[bool]

### Switchover
- **Type**: typing.Optional[bool]


# FailoverGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# Filter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
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

### DatabaseName
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### DeletionProtection
- **Type**: typing.Optional[bool]

### GlobalClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.GlobalClusterMember]]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.GlobalCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Filter]]


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
- **Type**: typing.Optional[typing.Sequence[str]]

### Port
- **Type**: typing.Optional[int]

### MasterUserPassword
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### CloudwatchLogsExportConfiguration
- **Type**: <class 'NoneType'>

### EngineVersion
- **Type**: typing.Optional[str]

### AllowMajorVersionUpgrade
- **Type**: typing.Optional[bool]

### DeletionProtection
- **Type**: typing.Optional[bool]

### StorageType
- **Type**: typing.Optional[str]

### ManageMasterUserPassword
- **Type**: typing.Optional[bool]

### MasterUserSecretKmsKeyId
- **Type**: typing.Optional[str]

### RotateMasterUserPassword
- **Type**: typing.Optional[bool]


# ModifyDBClusterParameterGroupMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Parameter]
- **Required**: Yes


# ModifyDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBClusterSnapshotAttributeMessage

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


# ModifyDBClusterSnapshotAttributeResult

### DBClusterSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBClusterSnapshotAttributesResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstanceClass
- **Type**: typing.Optional[str]

### ApplyImmediately
- **Type**: typing.Optional[bool]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### NewDBInstanceIdentifier
- **Type**: typing.Optional[str]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### PromotionTier
- **Type**: typing.Optional[int]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### CertificateRotationRestart
- **Type**: typing.Optional[bool]


# ModifyDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBSubnetGroupMessage

### DBSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DBSubnetGroupDescription
- **Type**: typing.Optional[str]


# ModifyDBSubnetGroupResult

### DBSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]


# ModifyEventSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyGlobalClusterMessage

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NewGlobalClusterIdentifier
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]


# ModifyGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.AvailabilityZone]]

### Vpc
- **Type**: typing.Optional[bool]

### StorageType
- **Type**: typing.Optional[str]


# OrderableDBInstanceOptionsMessage

### OrderableDBInstanceOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.OrderableDBInstanceOption]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.ResourcePendingMaintenanceActions]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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


# RebootDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ForceFailover
- **Type**: typing.Optional[bool]


# RebootDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveSourceIdentifierFromSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveSourceIdentifierFromSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsFromResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResetDBClusterParameterGroupMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Parameter]]


# ResourcePendingMaintenanceActions

### ResourceIdentifier
- **Type**: typing.Optional[str]

### PendingMaintenanceActionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_classes.PendingMaintenanceAction]]


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
- **Type**: typing.Optional[typing.Sequence[str]]

### EngineVersion
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]


# RestoreDBClusterFromSnapshotResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.Timestamp]

### UseLatestRestorableTime
- **Type**: typing.Optional[bool]

### Port
- **Type**: typing.Optional[int]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.docdb_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### StorageType
- **Type**: typing.Optional[str]


# RestoreDBClusterToPointInTimeResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# StartDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# StopDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# Subnet

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_classes.AvailabilityZone]

### SubnetStatus
- **Type**: typing.Optional[str]


# SwitchoverGlobalClusterMessage

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDbClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# SwitchoverGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagListMessage

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_classes.ResponseMetadata'>
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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



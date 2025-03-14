# Rds Classes

# AccountAttributesMessageTypeDef

### AccountQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.AccountQuotaTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccountQuotaTypeDef

### AccountQuotaName
- **Type**: typing.Optional[str]

### Used
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# AddRoleToDBClusterMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: typing.Optional[str]


# AddRoleToDBInstanceMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes


# AddSourceIdentifierToSubscriptionMessageTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# AddSourceIdentifierToSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddTagsToResourceMessageTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]
- **Required**: Yes


# ApplyPendingMaintenanceActionMessageTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResourcePendingMaintenanceActionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthorizeDBSecurityGroupIngressMessageTypeDef

### DBSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CIDRIP
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupId
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# AuthorizeDBSecurityGroupIngressResultTypeDef

### DBSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AvailabilityZoneTypeDef

### Name
- **Type**: typing.Optional[str]


# AvailableProcessorFeatureTypeDef

### Name
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]


# BacktrackDBClusterMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BacktrackTo
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]

### UseEarliestTimeOnPointInTimeUnavailable
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlueGreenDeploymentTaskTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# BlueGreenDeploymentTypeDef

### BlueGreenDeploymentIdentifier
- **Type**: typing.Optional[str]

### BlueGreenDeploymentName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### SwitchoverDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.SwitchoverDetailTypeDef]]

### Tasks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.BlueGreenDeploymentTaskTypeDef]]

### Status
- **Type**: typing.Optional[str]

### StatusDetails
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### DeleteTime
- **Type**: typing.Optional[datetime.datetime]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CancelExportTaskMessageTypeDef

### ExportTaskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CertificateDetailsTypeDef

### CAIdentifier
- **Type**: typing.Optional[str]

### ValidTill
- **Type**: typing.Optional[datetime.datetime]


# CertificateMessageTypeDef

### DefaultCertificateForNewLaunches
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.CertificateTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CertificateTypeDef

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

### CustomerOverride
- **Type**: typing.Optional[bool]

### CustomerOverrideValidTill
- **Type**: typing.Optional[datetime.datetime]


# CharacterSetTypeDef

### CharacterSetName
- **Type**: typing.Optional[str]

### CharacterSetDescription
- **Type**: typing.Optional[str]


# ClientGenerateDbAuthTokenRequestTypeDef

### DBHostname
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### DBUsername
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]


# CloudwatchLogsExportConfigurationTypeDef

### EnableLogTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### DisableLogTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# ClusterPendingModifiedValuesTypeDef

### PendingCloudwatchLogsExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PendingCloudwatchLogsExportsTypeDef]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### AllocatedStorage
- **Type**: typing.Optional[int]

### RdsCustomClusterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.RdsCustomClusterConfigurationTypeDef]

### Iops
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[str]

### CertificateDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.CertificateDetailsTypeDef]


# ConnectionPoolConfigurationInfoTypeDef

### MaxConnectionsPercent
- **Type**: typing.Optional[int]

### MaxIdleConnectionsPercent
- **Type**: typing.Optional[int]

### ConnectionBorrowTimeout
- **Type**: typing.Optional[int]

### SessionPinningFilters
- **Type**: typing.Optional[typing.List[str]]

### InitQuery
- **Type**: typing.Optional[str]


# ConnectionPoolConfigurationTypeDef

### MaxConnectionsPercent
- **Type**: typing.Optional[int]

### MaxIdleConnectionsPercent
- **Type**: typing.Optional[int]

### ConnectionBorrowTimeout
- **Type**: typing.Optional[int]

### SessionPinningFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### InitQuery
- **Type**: typing.Optional[str]


# ContextAttributeTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# CopyDBClusterParameterGroupMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CopyDBClusterParameterGroupResultTypeDef

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopyDBClusterSnapshotMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### SourceRegion
- **Type**: typing.Optional[str]


# CopyDBClusterSnapshotResultTypeDef

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopyDBParameterGroupMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CopyDBParameterGroupResultTypeDef

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopyDBSnapshotMessageTypeDef

### SourceDBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### CopyTags
- **Type**: typing.Optional[bool]

### PreSignedUrl
- **Type**: typing.Optional[str]

### OptionGroupName
- **Type**: typing.Optional[str]

### TargetCustomAvailabilityZone
- **Type**: typing.Optional[str]

### CopyOptionGroup
- **Type**: typing.Optional[bool]

### SourceRegion
- **Type**: typing.Optional[str]


# CopyDBSnapshotResultTypeDef

### DBSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopyOptionGroupMessageTypeDef

### SourceOptionGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetOptionGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetOptionGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CopyOptionGroupResultTypeDef

### OptionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.OptionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBlueGreenDeploymentRequestTypeDef

### BlueGreenDeploymentName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### TargetEngineVersion
- **Type**: typing.Optional[str]

### TargetDBParameterGroupName
- **Type**: typing.Optional[str]

### TargetDBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### TargetDBInstanceClass
- **Type**: typing.Optional[str]

### UpgradeTargetStorageConfig
- **Type**: typing.Optional[bool]

### TargetIops
- **Type**: typing.Optional[int]

### TargetStorageType
- **Type**: typing.Optional[str]

### TargetAllocatedStorage
- **Type**: typing.Optional[int]

### TargetStorageThroughput
- **Type**: typing.Optional[int]


# CreateBlueGreenDeploymentResponseTypeDef

### BlueGreenDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.BlueGreenDeploymentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomDBEngineVersionMessageTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseInstallationFilesS3BucketName
- **Type**: typing.Optional[str]

### DatabaseInstallationFilesS3Prefix
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### KMSKeyId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Manifest
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### SourceCustomDbEngineVersionIdentifier
- **Type**: typing.Optional[str]

### UseAwsProvidedLatestImage
- **Type**: typing.Optional[bool]


# CreateDBClusterEndpointMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBClusterMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### PreSignedUrl
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### BacktrackWindow
- **Type**: typing.Optional[int]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### EngineMode
- **Type**: typing.Optional[str]

### ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ScalingConfigurationTypeDef]

### RdsCustomClusterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.RdsCustomClusterConfigurationTypeDef]

### DeletionProtection
- **Type**: typing.Optional[bool]

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### EnableHttpEndpoint
- **Type**: typing.Optional[bool]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### Domain
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### EnableGlobalWriteForwarding
- **Type**: typing.Optional[bool]

### DBClusterInstanceClass
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### DatabaseInsightsMode
- **Type**: typing.Optional[typing.Literal['advanced', 'standard']]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnableLimitlessDatabase
- **Type**: typing.Optional[bool]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ServerlessV2ScalingConfigurationTypeDef]

### NetworkType
- **Type**: typing.Optional[str]

### ClusterScalabilityType
- **Type**: typing.Optional[typing.Literal['limitless', 'standard']]

### DBSystemId
- **Type**: typing.Optional[str]

### ManageMasterUserPassword
- **Type**: typing.Optional[bool]

### MasterUserSecretKmsKeyId
- **Type**: typing.Optional[str]

### EnableLocalWriteForwarding
- **Type**: typing.Optional[bool]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]

### SourceRegion
- **Type**: typing.Optional[str]


# CreateDBClusterParameterGroupMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBClusterParameterGroupResultTypeDef

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBClusterSnapshotMessageTypeDef

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBClusterSnapshotResultTypeDef

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBInstanceMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstanceClass
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
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

### NcharCharacterSetName
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

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

### DomainFqdn
- **Type**: typing.Optional[str]

### DomainOu
- **Type**: typing.Optional[str]

### DomainAuthSecretArn
- **Type**: typing.Optional[str]

### DomainDnsIps
- **Type**: typing.Optional[typing.Sequence[str]]

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

### DatabaseInsightsMode
- **Type**: typing.Optional[typing.Literal['advanced', 'standard']]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ProcessorFeatureTypeDef]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]

### EnableCustomerOwnedIp
- **Type**: typing.Optional[bool]

### CustomIamInstanceProfile
- **Type**: typing.Optional[str]

### BackupTarget
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]

### ManageMasterUserPassword
- **Type**: typing.Optional[bool]

### MasterUserSecretKmsKeyId
- **Type**: typing.Optional[str]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### DBSystemId
- **Type**: typing.Optional[str]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### MultiTenant
- **Type**: typing.Optional[bool]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# CreateDBInstanceReadReplicaMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### DBParameterGroupName
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### StorageType
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### PreSignedUrl
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### DatabaseInsightsMode
- **Type**: typing.Optional[typing.Literal['advanced', 'standard']]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ProcessorFeatureTypeDef]]

### UseDefaultProcessorFeatures
- **Type**: typing.Optional[bool]

### DeletionProtection
- **Type**: typing.Optional[bool]

### Domain
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### DomainFqdn
- **Type**: typing.Optional[str]

### DomainOu
- **Type**: typing.Optional[str]

### DomainAuthSecretArn
- **Type**: typing.Optional[str]

### DomainDnsIps
- **Type**: typing.Optional[typing.Sequence[str]]

### ReplicaMode
- **Type**: typing.Optional[typing.Literal['mounted', 'open-read-only']]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]

### CustomIamInstanceProfile
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]

### EnableCustomerOwnedIp
- **Type**: typing.Optional[bool]

### AllocatedStorage
- **Type**: typing.Optional[int]

### SourceDBClusterIdentifier
- **Type**: typing.Optional[str]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### UpgradeStorageConfig
- **Type**: typing.Optional[bool]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### SourceRegion
- **Type**: typing.Optional[str]


# CreateDBInstanceReadReplicaResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBParameterGroupMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBParameterGroupResultTypeDef

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBProxyEndpointRequestTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### DBProxyEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### TargetRole
- **Type**: typing.Optional[typing.Literal['READ_ONLY', 'READ_WRITE']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBProxyEndpointResponseTypeDef

### DBProxyEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBProxyEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBProxyRequestTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineFamily
- **Type**: typing.Literal['MYSQL', 'POSTGRESQL', 'SQLSERVER']
- **Required**: Yes

### Auth
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.UserAuthConfigTypeDef]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### RequireTLS
- **Type**: typing.Optional[bool]

### IdleClientTimeout
- **Type**: typing.Optional[int]

### DebugLogging
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBProxyResponseTypeDef

### DBProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBProxyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBSecurityGroupMessageTypeDef

### DBSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DBSecurityGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBSecurityGroupResultTypeDef

### DBSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBShardGroupMessageTypeDef

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxACU
- **Type**: <class 'float'>
- **Required**: Yes

### ComputeRedundancy
- **Type**: typing.Optional[int]

### MinACU
- **Type**: typing.Optional[float]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBSnapshotMessageTypeDef

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBSnapshotResultTypeDef

### DBSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBSubnetGroupMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBSubnetGroupResultTypeDef

### DBSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventSubscriptionMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateEventSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGlobalClusterMessageTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### SourceDBClusterIdentifier
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### DatabaseName
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntegrationMessageTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### KMSKeyId
- **Type**: typing.Optional[str]

### AdditionalEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### DataFilter
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# CreateOptionGroupMessageTypeDef

### OptionGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineName
- **Type**: <class 'str'>
- **Required**: Yes

### MajorEngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### OptionGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateOptionGroupResultTypeDef

### OptionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.OptionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTenantDatabaseMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TenantDBName
- **Type**: <class 'str'>
- **Required**: Yes

### MasterUsername
- **Type**: <class 'str'>
- **Required**: Yes

### MasterUserPassword
- **Type**: <class 'str'>
- **Required**: Yes

### CharacterSetName
- **Type**: typing.Optional[str]

### NcharCharacterSetName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateTenantDatabaseResultTypeDef

### TenantDatabase
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.TenantDatabaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomDBEngineVersionAMITypeDef

### ImageId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# DBClusterAutomatedBackupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterAutomatedBackups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterAutomatedBackupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterAutomatedBackupTypeDef

### Engine
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### DBClusterAutomatedBackupsArn
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### RestoreWindow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.RestoreWindowTypeDef]

### MasterUsername
- **Type**: typing.Optional[str]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### ClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### AllocatedStorage
- **Type**: typing.Optional[int]

### EngineVersion
- **Type**: typing.Optional[str]

### DBClusterArn
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### EngineMode
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### Port
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### AwsBackupRecoveryPointArn
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]


# DBClusterBacktrackMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterBacktracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterBacktrackTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterBacktrackResponseTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BacktrackIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BacktrackTo
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BacktrackedFrom
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BacktrackRequestCreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterBacktrackTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### BacktrackIdentifier
- **Type**: typing.Optional[str]

### BacktrackTo
- **Type**: typing.Optional[datetime.datetime]

### BacktrackedFrom
- **Type**: typing.Optional[datetime.datetime]

### BacktrackRequestCreationTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[str]


# DBClusterCapacityInfoTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PendingCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### CurrentCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### SecondsBeforeTimeout
- **Type**: <class 'int'>
- **Required**: Yes

### TimeoutAction
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterEndpointMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterEndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterEndpointResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterOptionGroupStatusTypeDef

### DBClusterOptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# DBClusterParameterGroupDetailsTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.ParameterOutputTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBClusterParameterGroupNameMessageTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterParameterGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterSnapshotAttributeTypeDef]]


# DBClusterSnapshotMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterSnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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

### EngineMode
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

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### DBSystemId
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]


# DBClusterStatusInfoTypeDef

### StatusType
- **Type**: typing.Optional[str]

### Normal
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### Message
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

### AutomaticRestartTime
- **Type**: typing.Optional[datetime.datetime]

### PercentProgress
- **Type**: typing.Optional[str]

### EarliestRestorableTime
- **Type**: typing.Optional[datetime.datetime]

### Endpoint
- **Type**: typing.Optional[str]

### ReaderEndpoint
- **Type**: typing.Optional[str]

### CustomEndpoints
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterOptionGroupStatusTypeDef]]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReplicationSourceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterStatusInfoTypeDef]]

### DBClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterMemberTypeDef]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.VpcSecurityGroupMembershipTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBClusterRoleTypeDef]]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### CloneGroupId
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### EarliestBacktrackTime
- **Type**: typing.Optional[datetime.datetime]

### BacktrackWindow
- **Type**: typing.Optional[int]

### BacktrackConsumedChangeRecords
- **Type**: typing.Optional[int]

### EnabledCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### Capacity
- **Type**: typing.Optional[int]

### EngineMode
- **Type**: typing.Optional[str]

### ScalingConfigurationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ScalingConfigurationInfoTypeDef]

### RdsCustomClusterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.RdsCustomClusterConfigurationTypeDef]

### DeletionProtection
- **Type**: typing.Optional[bool]

### HttpEndpointEnabled
- **Type**: typing.Optional[bool]

### ActivityStreamMode
- **Type**: typing.Optional[typing.Literal['async', 'sync']]

### ActivityStreamStatus
- **Type**: typing.Optional[typing.Literal['started', 'starting', 'stopped', 'stopping']]

### ActivityStreamKmsKeyId
- **Type**: typing.Optional[str]

### ActivityStreamKinesisStreamName
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### CrossAccountClone
- **Type**: typing.Optional[bool]

### DomainMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DomainMembershipTypeDef]]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### GlobalWriteForwardingStatus
- **Type**: typing.Optional[typing.Literal['disabled', 'disabling', 'enabled', 'enabling', 'unknown']]

### GlobalWriteForwardingRequested
- **Type**: typing.Optional[bool]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ClusterPendingModifiedValuesTypeDef]

### DBClusterInstanceClass
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### DatabaseInsightsMode
- **Type**: typing.Optional[typing.Literal['advanced', 'standard']]

### PerformanceInsightsEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ServerlessV2ScalingConfigurationInfoTypeDef]

### NetworkType
- **Type**: typing.Optional[str]

### DBSystemId
- **Type**: typing.Optional[str]

### MasterUserSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.MasterUserSecretTypeDef]

### IOOptimizedNextAllowedModificationTime
- **Type**: typing.Optional[datetime.datetime]

### LocalWriteForwardingStatus
- **Type**: typing.Optional[typing.Literal['disabled', 'disabling', 'enabled', 'enabling', 'requested']]

### AwsBackupRecoveryPointArn
- **Type**: typing.Optional[str]

### LimitlessDatabase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.LimitlessDatabaseTypeDef]

### StorageThroughput
- **Type**: typing.Optional[int]

### ClusterScalabilityType
- **Type**: typing.Optional[typing.Literal['limitless', 'standard']]

### CertificateDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.CertificateDetailsTypeDef]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# DBEngineVersionMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBEngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBEngineVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBEngineVersionResponseTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### DBEngineDescription
- **Type**: <class 'str'>
- **Required**: Yes

### DBEngineVersionDescription
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultCharacterSet
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.CharacterSetTypeDef'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.CustomDBEngineVersionAMITypeDef'>
- **Required**: Yes

### DBEngineMediaType
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedCharacterSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.CharacterSetTypeDef]
- **Required**: Yes

### SupportedNcharCharacterSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.CharacterSetTypeDef]
- **Required**: Yes

### ValidUpgradeTarget
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.UpgradeTargetTypeDef]
- **Required**: Yes

### SupportedTimezones
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.TimezoneTypeDef]
- **Required**: Yes

### ExportableLogTypes
- **Type**: typing.List[str]
- **Required**: Yes

### SupportsLogExportsToCloudwatchLogs
- **Type**: <class 'bool'>
- **Required**: Yes

### SupportsReadReplica
- **Type**: <class 'bool'>
- **Required**: Yes

### SupportedEngineModes
- **Type**: typing.List[str]
- **Required**: Yes

### SupportedFeatureNames
- **Type**: typing.List[str]
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### SupportsParallelQuery
- **Type**: <class 'bool'>
- **Required**: Yes

### SupportsGlobalDatabases
- **Type**: <class 'bool'>
- **Required**: Yes

### MajorEngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseInstallationFilesS3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseInstallationFilesS3Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### DBEngineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]
- **Required**: Yes

### SupportsBabelfish
- **Type**: <class 'bool'>
- **Required**: Yes

### CustomDBEngineVersionManifest
- **Type**: <class 'str'>
- **Required**: Yes

### SupportsLimitlessDatabase
- **Type**: <class 'bool'>
- **Required**: Yes

### SupportsCertificateRotationWithoutRestart
- **Type**: <class 'bool'>
- **Required**: Yes

### SupportedCACertificateIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### SupportsLocalWriteForwarding
- **Type**: <class 'bool'>
- **Required**: Yes

### SupportsIntegrations
- **Type**: <class 'bool'>
- **Required**: Yes

### ServerlessV2FeaturesSupport
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ServerlessV2FeaturesSupportTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.CharacterSetTypeDef]

### Image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.CustomDBEngineVersionAMITypeDef]

### DBEngineMediaType
- **Type**: typing.Optional[str]

### SupportedCharacterSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.CharacterSetTypeDef]]

### SupportedNcharCharacterSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.CharacterSetTypeDef]]

### ValidUpgradeTarget
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.UpgradeTargetTypeDef]]

### SupportedTimezones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TimezoneTypeDef]]

### ExportableLogTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportsLogExportsToCloudwatchLogs
- **Type**: typing.Optional[bool]

### SupportsReadReplica
- **Type**: typing.Optional[bool]

### SupportedEngineModes
- **Type**: typing.Optional[typing.List[str]]

### SupportedFeatureNames
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[str]

### SupportsParallelQuery
- **Type**: typing.Optional[bool]

### SupportsGlobalDatabases
- **Type**: typing.Optional[bool]

### MajorEngineVersion
- **Type**: typing.Optional[str]

### DatabaseInstallationFilesS3BucketName
- **Type**: typing.Optional[str]

### DatabaseInstallationFilesS3Prefix
- **Type**: typing.Optional[str]

### DBEngineVersionArn
- **Type**: typing.Optional[str]

### KMSKeyId
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### SupportsBabelfish
- **Type**: typing.Optional[bool]

### CustomDBEngineVersionManifest
- **Type**: typing.Optional[str]

### SupportsLimitlessDatabase
- **Type**: typing.Optional[bool]

### SupportsCertificateRotationWithoutRestart
- **Type**: typing.Optional[bool]

### SupportedCACertificateIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### SupportsLocalWriteForwarding
- **Type**: typing.Optional[bool]

### SupportsIntegrations
- **Type**: typing.Optional[bool]

### ServerlessV2FeaturesSupport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ServerlessV2FeaturesSupportTypeDef]


# DBInstanceAutomatedBackupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstanceAutomatedBackups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBInstanceAutomatedBackupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBInstanceAutomatedBackupTypeDef

### DBInstanceArn
- **Type**: typing.Optional[str]

### DbiResourceId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### RestoreWindow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.RestoreWindowTypeDef]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### InstanceCreateTime
- **Type**: typing.Optional[datetime.datetime]

### MasterUsername
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### StorageType
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]

### DBInstanceAutomatedBackupsReplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBInstanceAutomatedBackupsReplicationTypeDef]]

### BackupTarget
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]

### AwsBackupRecoveryPointArn
- **Type**: typing.Optional[str]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### MultiTenant
- **Type**: typing.Optional[bool]


# DBInstanceAutomatedBackupsReplicationTypeDef

### DBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]


# DBInstanceMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBInstanceRoleTypeDef

### RoleArn
- **Type**: typing.Optional[str]

### FeatureName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


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

### AutomaticRestartTime
- **Type**: typing.Optional[datetime.datetime]

### MasterUsername
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.EndpointTypeDef]

### AllocatedStorage
- **Type**: typing.Optional[int]

### InstanceCreateTime
- **Type**: typing.Optional[datetime.datetime]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DBSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBSecurityGroupMembershipTypeDef]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.VpcSecurityGroupMembershipTypeDef]]

### DBParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBParameterGroupStatusTypeDef]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DBSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.DBSubnetGroupTypeDef]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PendingModifiedValuesTypeDef]

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

### ReplicaMode
- **Type**: typing.Optional[typing.Literal['mounted', 'open-read-only']]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.OptionGroupMembershipTypeDef]]

### CharacterSetName
- **Type**: typing.Optional[str]

### NcharCharacterSetName
- **Type**: typing.Optional[str]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBInstanceStatusInfoTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DomainMembershipTypeDef]]

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

### DatabaseInsightsMode
- **Type**: typing.Optional[typing.Literal['advanced', 'standard']]

### PerformanceInsightsEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnabledCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.ProcessorFeatureTypeDef]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### AssociatedRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBInstanceRoleTypeDef]]

### ListenerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.EndpointTypeDef]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### DBInstanceAutomatedBackupsReplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBInstanceAutomatedBackupsReplicationTypeDef]]

### CustomerOwnedIpEnabled
- **Type**: typing.Optional[bool]

### AwsBackupRecoveryPointArn
- **Type**: typing.Optional[str]

### ActivityStreamStatus
- **Type**: typing.Optional[typing.Literal['started', 'starting', 'stopped', 'stopping']]

### ActivityStreamKmsKeyId
- **Type**: typing.Optional[str]

### ActivityStreamKinesisStreamName
- **Type**: typing.Optional[str]

### ActivityStreamMode
- **Type**: typing.Optional[typing.Literal['async', 'sync']]

### ActivityStreamEngineNativeAuditFieldsIncluded
- **Type**: typing.Optional[bool]

### AutomationMode
- **Type**: typing.Optional[typing.Literal['all-paused', 'full']]

### ResumeFullAutomationModeTime
- **Type**: typing.Optional[datetime.datetime]

### CustomIamInstanceProfile
- **Type**: typing.Optional[str]

### BackupTarget
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[str]

### ActivityStreamPolicyStatus
- **Type**: typing.Optional[typing.Literal['locked', 'locking-policy', 'unlocked', 'unlocking-policy']]

### StorageThroughput
- **Type**: typing.Optional[int]

### DBSystemId
- **Type**: typing.Optional[str]

### MasterUserSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.MasterUserSecretTypeDef]

### CertificateDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.CertificateDetailsTypeDef]

### ReadReplicaSourceDBClusterIdentifier
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[str]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### IsStorageConfigUpgradeAvailable
- **Type**: typing.Optional[bool]

### MultiTenant
- **Type**: typing.Optional[bool]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# DBParameterGroupDetailsTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.ParameterOutputTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBParameterGroupNameMessageTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBParameterGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBProxyEndpointTypeDef

### DBProxyEndpointName
- **Type**: typing.Optional[str]

### DBProxyEndpointArn
- **Type**: typing.Optional[str]

### DBProxyName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['available', 'creating', 'deleting', 'incompatible-network', 'insufficient-resource-limits', 'modifying']]

### VpcId
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### VpcSubnetIds
- **Type**: typing.Optional[typing.List[str]]

### Endpoint
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### TargetRole
- **Type**: typing.Optional[typing.Literal['READ_ONLY', 'READ_WRITE']]

### IsDefault
- **Type**: typing.Optional[bool]


# DBProxyTargetGroupTypeDef

### DBProxyName
- **Type**: typing.Optional[str]

### TargetGroupName
- **Type**: typing.Optional[str]

### TargetGroupArn
- **Type**: typing.Optional[str]

### IsDefault
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### ConnectionPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ConnectionPoolConfigurationInfoTypeDef]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### UpdatedDate
- **Type**: typing.Optional[datetime.datetime]


# DBProxyTargetTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DBProxyTypeDef

### DBProxyName
- **Type**: typing.Optional[str]

### DBProxyArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['available', 'creating', 'deleting', 'incompatible-network', 'insufficient-resource-limits', 'modifying', 'reactivating', 'suspended', 'suspending']]

### EngineFamily
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### VpcSubnetIds
- **Type**: typing.Optional[typing.List[str]]

### Auth
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.UserAuthConfigInfoTypeDef]]

### RoleArn
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### RequireTLS
- **Type**: typing.Optional[bool]

### IdleClientTimeout
- **Type**: typing.Optional[int]

### DebugLogging
- **Type**: typing.Optional[bool]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### UpdatedDate
- **Type**: typing.Optional[datetime.datetime]


# DBRecommendationMessageTypeDef

### DBRecommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBRecommendationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBRecommendationTypeDef

### RecommendationId
- **Type**: typing.Optional[str]

### TypeId
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### Detection
- **Type**: typing.Optional[str]

### Recommendation
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]

### RecommendedActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.RecommendedActionTypeDef]]

### Category
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### TypeDetection
- **Type**: typing.Optional[str]

### TypeRecommendation
- **Type**: typing.Optional[str]

### Impact
- **Type**: typing.Optional[str]

### AdditionalInfo
- **Type**: typing.Optional[str]

### Links
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DocLinkTypeDef]]

### IssueDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.IssueDetailsTypeDef]


# DBRecommendationsMessageTypeDef

### DBRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBRecommendationTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBSecurityGroupMembershipTypeDef

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# DBSecurityGroupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSecurityGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBSecurityGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBSecurityGroupTypeDef

### OwnerId
- **Type**: typing.Optional[str]

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### DBSecurityGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### EC2SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.EC2SecurityGroupTypeDef]]

### IPRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.IPRangeTypeDef]]

### DBSecurityGroupArn
- **Type**: typing.Optional[str]


# DBShardGroupResponseTypeDef

### DBShardGroupResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxACU
- **Type**: <class 'float'>
- **Required**: Yes

### MinACU
- **Type**: <class 'float'>
- **Required**: Yes

### ComputeRedundancy
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### PubliclyAccessible
- **Type**: <class 'bool'>
- **Required**: Yes

### Endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### DBShardGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBShardGroupTypeDef

### DBShardGroupResourceId
- **Type**: typing.Optional[str]

### DBShardGroupIdentifier
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### MaxACU
- **Type**: typing.Optional[float]

### MinACU
- **Type**: typing.Optional[float]

### ComputeRedundancy
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[str]

### DBShardGroupArn
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# DBSnapshotAttributeTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[str]]


# DBSnapshotAttributesResultTypeDef

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBSnapshotAttributeTypeDef]]


# DBSnapshotMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBSnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBSnapshotTenantDatabaseTypeDef

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DbiResourceId
- **Type**: typing.Optional[str]

### EngineName
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### TenantDatabaseCreateTime
- **Type**: typing.Optional[datetime.datetime]

### TenantDBName
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### TenantDatabaseResourceId
- **Type**: typing.Optional[str]

### CharacterSetName
- **Type**: typing.Optional[str]

### DBSnapshotTenantDatabaseARN
- **Type**: typing.Optional[str]

### NcharCharacterSetName
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# DBSnapshotTenantDatabasesMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSnapshotTenantDatabases
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBSnapshotTenantDatabaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DBSnapshotTypeDef

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
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

### AvailabilityZone
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### InstanceCreateTime
- **Type**: typing.Optional[datetime.datetime]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### SourceRegion
- **Type**: typing.Optional[str]

### SourceDBSnapshotIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DBSnapshotArn
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.ProcessorFeatureTypeDef]]

### DbiResourceId
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### OriginalSnapshotCreateTime
- **Type**: typing.Optional[datetime.datetime]

### SnapshotDatabaseTime
- **Type**: typing.Optional[datetime.datetime]

### SnapshotTarget
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]

### DBSystemId
- **Type**: typing.Optional[str]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### MultiTenant
- **Type**: typing.Optional[bool]


# DBSubnetGroupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBSubnetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.SubnetTypeDef]]

### DBSubnetGroupArn
- **Type**: typing.Optional[str]

### SupportedNetworkTypes
- **Type**: typing.Optional[typing.List[str]]


# DeleteBlueGreenDeploymentRequestTypeDef

### BlueGreenDeploymentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteTarget
- **Type**: typing.Optional[bool]


# DeleteBlueGreenDeploymentResponseTypeDef

### BlueGreenDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.BlueGreenDeploymentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCustomDBEngineVersionMessageTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterAutomatedBackupMessageTypeDef

### DbClusterResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterAutomatedBackupResultTypeDef

### DBClusterAutomatedBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterAutomatedBackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBClusterEndpointMessageTypeDef

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DeleteAutomatedBackups
- **Type**: typing.Optional[bool]


# DeleteDBClusterParameterGroupMessageTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBClusterSnapshotMessageTypeDef

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterSnapshotResultTypeDef

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBInstanceAutomatedBackupMessageTypeDef

### DbiResourceId
- **Type**: typing.Optional[str]

### DBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]


# DeleteDBInstanceAutomatedBackupResultTypeDef

### DBInstanceAutomatedBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceAutomatedBackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBInstanceMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DeleteAutomatedBackups
- **Type**: typing.Optional[bool]


# DeleteDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBParameterGroupMessageTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBProxyEndpointRequestTypeDef

### DBProxyEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBProxyEndpointResponseTypeDef

### DBProxyEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBProxyEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBProxyRequestTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBProxyResponseTypeDef

### DBProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBProxyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBSecurityGroupMessageTypeDef

### DBSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBShardGroupMessageTypeDef

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBSnapshotMessageTypeDef

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBSnapshotResultTypeDef

### DBSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDBSubnetGroupMessageTypeDef

### DBSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionMessageTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGlobalClusterMessageTypeDef

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIntegrationMessageTypeDef

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOptionGroupMessageTypeDef

### OptionGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTenantDatabaseMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TenantDBName
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]


# DeleteTenantDatabaseResultTypeDef

### TenantDatabase
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.TenantDatabaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterDBProxyTargetsRequestTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### DBInstanceIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### DBClusterIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeBlueGreenDeploymentsRequestPaginateTypeDef

### BlueGreenDeploymentIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeBlueGreenDeploymentsRequestTypeDef

### BlueGreenDeploymentIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeBlueGreenDeploymentsResponseTypeDef

### BlueGreenDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.BlueGreenDeploymentTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCertificatesMessagePaginateTypeDef

### CertificateIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeCertificatesMessageTypeDef

### CertificateIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterAutomatedBackupsMessagePaginateTypeDef

### DbClusterResourceId
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterAutomatedBackupsMessageTypeDef

### DbClusterResourceId
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterBacktracksMessagePaginateTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BacktrackIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterBacktracksMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BacktrackIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterEndpointsMessagePaginateTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterEndpointIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterEndpointsMessageTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterEndpointIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterParameterGroupsMessagePaginateTypeDef

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterParameterGroupsMessageTypeDef

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterParametersMessagePaginateTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterParametersMessageTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterSnapshotAttributesMessageTypeDef

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDBClusterSnapshotAttributesResultTypeDef

### DBClusterSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterSnapshotAttributesResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBClusterSnapshotsMessagePaginateTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterSnapshotsMessageTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbClusterResourceId
- **Type**: typing.Optional[str]


# DescribeDBClusterSnapshotsMessageWaitExtraTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeDBClusterSnapshotsMessageWaitTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeDBClustersMessagePaginateTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### IncludeShared
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClustersMessageTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]


# DescribeDBClustersMessageWaitExtraTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeDBClustersMessageWaitTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeDBEngineVersionsMessagePaginateTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### DefaultOnly
- **Type**: typing.Optional[bool]

### ListSupportedCharacterSets
- **Type**: typing.Optional[bool]

### ListSupportedTimezones
- **Type**: typing.Optional[bool]

### IncludeAll
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBEngineVersionsMessageTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

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

### IncludeAll
- **Type**: typing.Optional[bool]


# DescribeDBInstanceAutomatedBackupsMessagePaginateTypeDef

### DbiResourceId
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### DBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBInstanceAutomatedBackupsMessageTypeDef

### DbiResourceId
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### DBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]


# DescribeDBInstancesMessagePaginateTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBInstancesMessageTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBInstancesMessageWaitExtraTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeDBInstancesMessageWaitTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeDBLogFilesDetailsTypeDef

### LogFileName
- **Type**: typing.Optional[str]

### LastWritten
- **Type**: typing.Optional[int]

### Size
- **Type**: typing.Optional[int]


# DescribeDBLogFilesMessagePaginateTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### FilenameContains
- **Type**: typing.Optional[str]

### FileLastWritten
- **Type**: typing.Optional[int]

### FileSize
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBLogFilesMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### FilenameContains
- **Type**: typing.Optional[str]

### FileLastWritten
- **Type**: typing.Optional[int]

### FileSize
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBLogFilesResponseTypeDef

### DescribeDBLogFiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DescribeDBLogFilesDetailsTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBParameterGroupsMessagePaginateTypeDef

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBParameterGroupsMessageTypeDef

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBParametersMessagePaginateTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBParametersMessageTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBProxiesRequestPaginateTypeDef

### DBProxyName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBProxiesRequestTypeDef

### DBProxyName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBProxiesResponseTypeDef

### DBProxies
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBProxyTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBProxyEndpointsRequestPaginateTypeDef

### DBProxyName
- **Type**: typing.Optional[str]

### DBProxyEndpointName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBProxyEndpointsRequestTypeDef

### DBProxyName
- **Type**: typing.Optional[str]

### DBProxyEndpointName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBProxyEndpointsResponseTypeDef

### DBProxyEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBProxyEndpointTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBProxyTargetGroupsRequestPaginateTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBProxyTargetGroupsRequestTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBProxyTargetGroupsResponseTypeDef

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBProxyTargetGroupTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBProxyTargetsRequestPaginateTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBProxyTargetsRequestTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBProxyTargetsResponseTypeDef

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBProxyTargetTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBRecommendationsMessagePaginateTypeDef

### LastUpdatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

### LastUpdatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

### Locale
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBRecommendationsMessageTypeDef

### LastUpdatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

### LastUpdatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

### Locale
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBSecurityGroupsMessagePaginateTypeDef

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBSecurityGroupsMessageTypeDef

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBShardGroupsMessageTypeDef

### DBShardGroupIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBShardGroupsResponseTypeDef

### DBShardGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBShardGroupTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBSnapshotAttributesMessageTypeDef

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDBSnapshotAttributesResultTypeDef

### DBSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSnapshotAttributesResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDBSnapshotTenantDatabasesMessagePaginateTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### DbiResourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBSnapshotTenantDatabasesMessageTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### DbiResourceId
- **Type**: typing.Optional[str]


# DescribeDBSnapshotsMessagePaginateTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbiResourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBSnapshotsMessageTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbiResourceId
- **Type**: typing.Optional[str]


# DescribeDBSnapshotsMessageWaitExtraExtraTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbiResourceId
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeDBSnapshotsMessageWaitExtraTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbiResourceId
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeDBSnapshotsMessageWaitTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbiResourceId
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeDBSubnetGroupsMessagePaginateTypeDef

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBSubnetGroupsMessageTypeDef

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultClusterParametersMessagePaginateTypeDef

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeEngineDefaultClusterParametersMessageTypeDef

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultClusterParametersResultTypeDef

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EngineDefaultsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEngineDefaultParametersMessagePaginateTypeDef

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeEngineDefaultParametersMessageTypeDef

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultParametersResultTypeDef

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EngineDefaultsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventCategoriesMessageTypeDef

### SourceType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]


# DescribeEventSubscriptionsMessagePaginateTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeEventSubscriptionsMessageTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventsMessagePaginateTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['blue-green-deployment', 'custom-engine-version', 'db-cluster', 'db-cluster-snapshot', 'db-instance', 'db-parameter-group', 'db-proxy', 'db-security-group', 'db-snapshot']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeEventsMessageTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['blue-green-deployment', 'custom-engine-version', 'db-cluster', 'db-cluster-snapshot', 'db-instance', 'db-parameter-group', 'db-proxy', 'db-security-group', 'db-snapshot']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeExportTasksMessagePaginateTypeDef

### ExportTaskIdentifier
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'SNAPSHOT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeExportTasksMessageTypeDef

### ExportTaskIdentifier
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'SNAPSHOT']]


# DescribeGlobalClustersMessagePaginateTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeGlobalClustersMessageTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeIntegrationsMessagePaginateTypeDef

### IntegrationIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeIntegrationsMessageTypeDef

### IntegrationIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeIntegrationsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Integrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.IntegrationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOptionGroupOptionsMessagePaginateTypeDef

### EngineName
- **Type**: <class 'str'>
- **Required**: Yes

### MajorEngineVersion
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeOptionGroupOptionsMessageTypeDef

### EngineName
- **Type**: <class 'str'>
- **Required**: Yes

### MajorEngineVersion
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeOptionGroupsMessagePaginateTypeDef

### OptionGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### EngineName
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeOptionGroupsMessageTypeDef

### OptionGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### EngineName
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]


# DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### AvailabilityZoneGroup
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeOrderableDBInstanceOptionsMessageTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### AvailabilityZoneGroup
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribePendingMaintenanceActionsMessagePaginateTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribePendingMaintenanceActionsMessageTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeReservedDBInstancesMessagePaginateTypeDef

### ReservedDBInstanceId
- **Type**: typing.Optional[str]

### ReservedDBInstancesOfferingId
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### LeaseId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeReservedDBInstancesMessageTypeDef

### ReservedDBInstanceId
- **Type**: typing.Optional[str]

### ReservedDBInstancesOfferingId
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### LeaseId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedDBInstancesOfferingsMessagePaginateTypeDef

### ReservedDBInstancesOfferingId
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeReservedDBInstancesOfferingsMessageTypeDef

### ReservedDBInstancesOfferingId
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeTenantDatabasesMessagePaginateTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeTenantDatabasesMessageTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeTenantDatabasesMessageWaitExtraTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeTenantDatabasesMessageWaitTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.WaiterConfigTypeDef]


# DescribeValidDBInstanceModificationsMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeValidDBInstanceModificationsResultTypeDef

### ValidDBInstanceModificationsMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ValidDBInstanceModificationsMessageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableHttpEndpointRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisableHttpEndpointResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpEndpointEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocLinkTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DomainMembershipTypeDef

### Domain
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### FQDN
- **Type**: typing.Optional[str]

### IAMRoleName
- **Type**: typing.Optional[str]

### OU
- **Type**: typing.Optional[str]

### AuthSecretArn
- **Type**: typing.Optional[str]

### DnsIps
- **Type**: typing.Optional[typing.List[str]]


# DoubleRangeTypeDef

### From
- **Type**: typing.Optional[float]

### To
- **Type**: typing.Optional[float]


# DownloadDBLogFilePortionDetailsTypeDef

### LogFileData
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalDataPending
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DownloadDBLogFilePortionMessagePaginateTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### LogFileName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DownloadDBLogFilePortionMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### LogFileName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### NumberOfLines
- **Type**: typing.Optional[int]


# EC2SecurityGroupTypeDef

### Status
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupId
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableHttpEndpointRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# EnableHttpEndpointResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpEndpointEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.ParameterOutputTypeDef]]


# EventCategoriesMapTypeDef

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]


# EventCategoriesMessageTypeDef

### EventCategoriesMapList
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.EventCategoriesMapTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.EventSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['blue-green-deployment', 'custom-engine-version', 'db-cluster', 'db-cluster-snapshot', 'db-instance', 'db-parameter-group', 'db-proxy', 'db-security-group', 'db-snapshot']]

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportTaskResponseTypeDef

### ExportTaskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExportOnly
- **Type**: typing.List[str]
- **Required**: Yes

### SnapshotTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TaskStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TaskEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### PercentProgress
- **Type**: <class 'int'>
- **Required**: Yes

### TotalExtractedDataInGB
- **Type**: <class 'int'>
- **Required**: Yes

### FailureCause
- **Type**: <class 'str'>
- **Required**: Yes

### WarningMessage
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Literal['CLUSTER', 'SNAPSHOT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportTaskTypeDef

### ExportTaskIdentifier
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### ExportOnly
- **Type**: typing.Optional[typing.List[str]]

### SnapshotTime
- **Type**: typing.Optional[datetime.datetime]

### TaskStartTime
- **Type**: typing.Optional[datetime.datetime]

### TaskEndTime
- **Type**: typing.Optional[datetime.datetime]

### S3Bucket
- **Type**: typing.Optional[str]

### S3Prefix
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### TotalExtractedDataInGB
- **Type**: typing.Optional[int]

### FailureCause
- **Type**: typing.Optional[str]

### WarningMessage
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'SNAPSHOT']]


# ExportTasksMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ExportTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.ExportTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailoverDBClusterMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDBInstanceIdentifier
- **Type**: typing.Optional[str]


# FailoverDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailoverGlobalClusterMessageTypeDef

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


# FailoverGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailoverStateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['cancelling', 'failing-over', 'pending']]

### FromDbClusterArn
- **Type**: typing.Optional[str]

### ToDbClusterArn
- **Type**: typing.Optional[str]

### IsDataLossAllowed
- **Type**: typing.Optional[bool]


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

### GlobalWriteForwardingStatus
- **Type**: typing.Optional[typing.Literal['disabled', 'disabling', 'enabled', 'enabling', 'unknown']]

### SynchronizationStatus
- **Type**: typing.Optional[typing.Literal['connected', 'pending-resync']]


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

### EngineLifecycleSupport
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### DeletionProtection
- **Type**: typing.Optional[bool]

### GlobalClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.GlobalClusterMemberTypeDef]]

### Endpoint
- **Type**: typing.Optional[str]

### FailoverState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.FailoverStateTypeDef]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# GlobalClustersMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.GlobalClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IPRangeTypeDef

### Status
- **Type**: typing.Optional[str]

### CIDRIP
- **Type**: typing.Optional[str]


# IntegrationErrorTypeDef

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: typing.Optional[str]


# IntegrationResponseTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalEncryptionContext
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Status
- **Type**: typing.Literal['active', 'creating', 'deleting', 'failed', 'modifying', 'needs_attention', 'syncing']
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.IntegrationErrorTypeDef]
- **Required**: Yes

### DataFilter
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IntegrationTypeDef

### SourceArn
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### IntegrationName
- **Type**: typing.Optional[str]

### IntegrationArn
- **Type**: typing.Optional[str]

### KMSKeyId
- **Type**: typing.Optional[str]

### AdditionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### Status
- **Type**: typing.Optional[typing.Literal['active', 'creating', 'deleting', 'failed', 'modifying', 'needs_attention', 'syncing']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.IntegrationErrorTypeDef]]

### DataFilter
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# IssueDetailsTypeDef

### PerformanceIssueDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PerformanceIssueDetailsTypeDef]


# LimitlessDatabaseTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['active', 'disabled', 'disabling', 'enabled', 'enabling', 'error', 'modifying-max-capacity', 'not-in-use']]

### MinRequiredACU
- **Type**: typing.Optional[float]


# ListTagsForResourceMessageTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]


# MasterUserSecretTypeDef

### SecretArn
- **Type**: typing.Optional[str]

### SecretStatus
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]


# MetricQueryTypeDef

### PerformanceInsightsMetricQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PerformanceInsightsMetricQueryTypeDef]


# MetricReferenceTypeDef

### Name
- **Type**: typing.Optional[str]

### ReferenceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ReferenceDetailsTypeDef]


# MetricTypeDef

### Name
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.MetricReferenceTypeDef]]

### StatisticsDetails
- **Type**: typing.Optional[str]

### MetricQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.MetricQueryTypeDef]


# MinimumEngineVersionPerAllowedValueTypeDef

### AllowedValue
- **Type**: typing.Optional[str]

### MinimumEngineVersion
- **Type**: typing.Optional[str]


# ModifyActivityStreamRequestTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### AuditPolicyState
- **Type**: typing.Optional[typing.Literal['locked', 'unlocked']]


# ModifyActivityStreamResponseTypeDef

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['started', 'starting', 'stopped', 'stopping']
- **Required**: Yes

### Mode
- **Type**: typing.Literal['async', 'sync']
- **Required**: Yes

### EngineNativeAuditFieldsIncluded
- **Type**: <class 'bool'>
- **Required**: Yes

### PolicyStatus
- **Type**: typing.Literal['locked', 'locking-policy', 'unlocked', 'unlocking-policy']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyCertificatesMessageTypeDef

### CertificateIdentifier
- **Type**: typing.Optional[str]

### RemoveCustomerOverride
- **Type**: typing.Optional[bool]


# ModifyCertificatesResultTypeDef

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.CertificateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyCurrentDBClusterCapacityMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Capacity
- **Type**: typing.Optional[int]

### SecondsBeforeTimeout
- **Type**: typing.Optional[int]

### TimeoutAction
- **Type**: typing.Optional[str]


# ModifyCustomDBEngineVersionMessageTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['available', 'inactive', 'inactive-except-restore']]


# ModifyDBClusterEndpointMessageTypeDef

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: typing.Optional[str]

### StaticMembers
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludedMembers
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyDBClusterMessageTypeDef

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

### BacktrackWindow
- **Type**: typing.Optional[int]

### CloudwatchLogsExportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.CloudwatchLogsExportConfigurationTypeDef]

### EngineVersion
- **Type**: typing.Optional[str]

### AllowMajorVersionUpgrade
- **Type**: typing.Optional[bool]

### DBInstanceParameterGroupName
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ScalingConfigurationTypeDef]

### DeletionProtection
- **Type**: typing.Optional[bool]

### EnableHttpEndpoint
- **Type**: typing.Optional[bool]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### EnableGlobalWriteForwarding
- **Type**: typing.Optional[bool]

### DBClusterInstanceClass
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### DatabaseInsightsMode
- **Type**: typing.Optional[typing.Literal['advanced', 'standard']]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ServerlessV2ScalingConfigurationTypeDef]

### NetworkType
- **Type**: typing.Optional[str]

### ManageMasterUserPassword
- **Type**: typing.Optional[bool]

### RotateMasterUserPassword
- **Type**: typing.Optional[bool]

### MasterUserSecretKmsKeyId
- **Type**: typing.Optional[str]

### EngineMode
- **Type**: typing.Optional[str]

### AllowEngineModeChange
- **Type**: typing.Optional[bool]

### EnableLocalWriteForwarding
- **Type**: typing.Optional[bool]

### AwsBackupRecoveryPointArn
- **Type**: typing.Optional[str]

### EnableLimitlessDatabase
- **Type**: typing.Optional[bool]

### CACertificateIdentifier
- **Type**: typing.Optional[str]


# ModifyDBClusterParameterGroupMessageTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ParameterUnionTypeDef]
- **Required**: Yes


# ModifyDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBClusterSnapshotAttributeMessageTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterSnapshotAttributesResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBInstanceMessageTypeDef

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

### DomainFqdn
- **Type**: typing.Optional[str]

### DomainOu
- **Type**: typing.Optional[str]

### DomainAuthSecretArn
- **Type**: typing.Optional[str]

### DomainDnsIps
- **Type**: typing.Optional[typing.Sequence[str]]

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

### DisableDomain
- **Type**: typing.Optional[bool]

### PromotionTier
- **Type**: typing.Optional[int]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### DatabaseInsightsMode
- **Type**: typing.Optional[typing.Literal['advanced', 'standard']]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### CloudwatchLogsExportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.CloudwatchLogsExportConfigurationTypeDef]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ProcessorFeatureTypeDef]]

### UseDefaultProcessorFeatures
- **Type**: typing.Optional[bool]

### DeletionProtection
- **Type**: typing.Optional[bool]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]

### CertificateRotationRestart
- **Type**: typing.Optional[bool]

### ReplicaMode
- **Type**: typing.Optional[typing.Literal['mounted', 'open-read-only']]

### EnableCustomerOwnedIp
- **Type**: typing.Optional[bool]

### AwsBackupRecoveryPointArn
- **Type**: typing.Optional[str]

### AutomationMode
- **Type**: typing.Optional[typing.Literal['all-paused', 'full']]

### ResumeFullAutomationModeMinutes
- **Type**: typing.Optional[int]

### NetworkType
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]

### ManageMasterUserPassword
- **Type**: typing.Optional[bool]

### RotateMasterUserPassword
- **Type**: typing.Optional[bool]

### MasterUserSecretKmsKeyId
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### MultiTenant
- **Type**: typing.Optional[bool]


# ModifyDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBParameterGroupMessageTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ParameterUnionTypeDef]
- **Required**: Yes


# ModifyDBProxyEndpointRequestTypeDef

### DBProxyEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### NewDBProxyEndpointName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyDBProxyEndpointResponseTypeDef

### DBProxyEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBProxyEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBProxyRequestTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### NewDBProxyName
- **Type**: typing.Optional[str]

### Auth
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.UserAuthConfigTypeDef]]

### RequireTLS
- **Type**: typing.Optional[bool]

### IdleClientTimeout
- **Type**: typing.Optional[int]

### DebugLogging
- **Type**: typing.Optional[bool]

### RoleArn
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyDBProxyResponseTypeDef

### DBProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBProxyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBProxyTargetGroupRequestTypeDef

### TargetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ConnectionPoolConfigurationTypeDef]

### NewName
- **Type**: typing.Optional[str]


# ModifyDBProxyTargetGroupResponseTypeDef

### DBProxyTargetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBProxyTargetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBRecommendationMessageTypeDef

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### Locale
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### RecommendedActionUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.RecommendedActionUpdateTypeDef]]


# ModifyDBShardGroupMessageTypeDef

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxACU
- **Type**: typing.Optional[float]

### MinACU
- **Type**: typing.Optional[float]

### ComputeRedundancy
- **Type**: typing.Optional[int]


# ModifyDBSnapshotAttributeMessageTypeDef

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ValuesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### ValuesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyDBSnapshotAttributeResultTypeDef

### DBSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSnapshotAttributesResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBSnapshotMessageTypeDef

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: typing.Optional[str]

### OptionGroupName
- **Type**: typing.Optional[str]


# ModifyDBSnapshotResultTypeDef

### DBSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDBSubnetGroupMessageTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyEventSubscriptionMessageTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyGlobalClusterMessageTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyIntegrationMessageTypeDef

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: typing.Optional[str]

### DataFilter
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ModifyOptionGroupMessageTypeDef

### OptionGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### OptionsToInclude
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.OptionConfigurationTypeDef]]

### OptionsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### ApplyImmediately
- **Type**: typing.Optional[bool]


# ModifyOptionGroupResultTypeDef

### OptionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.OptionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyTenantDatabaseMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TenantDBName
- **Type**: <class 'str'>
- **Required**: Yes

### MasterUserPassword
- **Type**: typing.Optional[str]

### NewTenantDBName
- **Type**: typing.Optional[str]


# ModifyTenantDatabaseResultTypeDef

### TenantDatabase
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.TenantDatabaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OptionConfigurationTypeDef

### OptionName
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: typing.Optional[int]

### OptionVersion
- **Type**: typing.Optional[str]

### DBSecurityGroupMemberships
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcSecurityGroupMemberships
- **Type**: typing.Optional[typing.Sequence[str]]

### OptionSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.OptionSettingTypeDef]]


# OptionGroupMembershipTypeDef

### OptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# OptionGroupOptionSettingTypeDef

### SettingName
- **Type**: typing.Optional[str]

### SettingDescription
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### ApplyType
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]

### IsModifiable
- **Type**: typing.Optional[bool]

### IsRequired
- **Type**: typing.Optional[bool]

### MinimumEngineVersionPerAllowedValue
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.MinimumEngineVersionPerAllowedValueTypeDef]]


# OptionGroupOptionTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EngineName
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]

### MinimumRequiredMinorEngineVersion
- **Type**: typing.Optional[str]

### PortRequired
- **Type**: typing.Optional[bool]

### DefaultPort
- **Type**: typing.Optional[int]

### OptionsDependedOn
- **Type**: typing.Optional[typing.List[str]]

### OptionsConflictsWith
- **Type**: typing.Optional[typing.List[str]]

### Persistent
- **Type**: typing.Optional[bool]

### Permanent
- **Type**: typing.Optional[bool]

### RequiresAutoMinorEngineVersionUpgrade
- **Type**: typing.Optional[bool]

### VpcOnly
- **Type**: typing.Optional[bool]

### SupportsOptionVersionDowngrade
- **Type**: typing.Optional[bool]

### OptionGroupOptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.OptionGroupOptionSettingTypeDef]]

### OptionGroupOptionVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.OptionVersionTypeDef]]

### CopyableCrossAccount
- **Type**: typing.Optional[bool]


# OptionGroupOptionsMessageTypeDef

### OptionGroupOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.OptionGroupOptionTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OptionGroupTypeDef

### OptionGroupName
- **Type**: typing.Optional[str]

### OptionGroupDescription
- **Type**: typing.Optional[str]

### EngineName
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.OptionTypeDef]]

### AllowsVpcAndNonVpcInstanceMemberships
- **Type**: typing.Optional[bool]

### VpcId
- **Type**: typing.Optional[str]

### OptionGroupArn
- **Type**: typing.Optional[str]

### SourceOptionGroup
- **Type**: typing.Optional[str]

### SourceAccountId
- **Type**: typing.Optional[str]

### CopyTimestamp
- **Type**: typing.Optional[datetime.datetime]


# OptionGroupsTypeDef

### OptionGroupsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.OptionGroupTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OptionSettingTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ApplyType
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]

### IsModifiable
- **Type**: typing.Optional[bool]

### IsCollection
- **Type**: typing.Optional[bool]


# OptionTypeDef

### OptionName
- **Type**: typing.Optional[str]

### OptionDescription
- **Type**: typing.Optional[str]

### Persistent
- **Type**: typing.Optional[bool]

### Permanent
- **Type**: typing.Optional[bool]

### Port
- **Type**: typing.Optional[int]

### OptionVersion
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.OptionSettingTypeDef]]

### DBSecurityGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DBSecurityGroupMembershipTypeDef]]

### VpcSecurityGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.VpcSecurityGroupMembershipTypeDef]]


# OptionVersionTypeDef

### Version
- **Type**: typing.Optional[str]

### IsDefault
- **Type**: typing.Optional[bool]


# OrderableDBInstanceOptionTypeDef

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### AvailabilityZoneGroup
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.AvailabilityZoneTypeDef]]

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

### AvailableProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.AvailableProcessorFeatureTypeDef]]

### SupportedEngineModes
- **Type**: typing.Optional[typing.List[str]]

### SupportsStorageAutoscaling
- **Type**: typing.Optional[bool]

### SupportsKerberosAuthentication
- **Type**: typing.Optional[bool]

### OutpostCapable
- **Type**: typing.Optional[bool]

### SupportedActivityStreamModes
- **Type**: typing.Optional[typing.List[str]]

### SupportsGlobalDatabases
- **Type**: typing.Optional[bool]

### SupportsClusters
- **Type**: typing.Optional[bool]

### SupportedNetworkTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportsStorageThroughput
- **Type**: typing.Optional[bool]

### MinStorageThroughputPerDbInstance
- **Type**: typing.Optional[int]

### MaxStorageThroughputPerDbInstance
- **Type**: typing.Optional[int]

### MinStorageThroughputPerIops
- **Type**: typing.Optional[float]

### MaxStorageThroughputPerIops
- **Type**: typing.Optional[float]

### SupportsDedicatedLogVolume
- **Type**: typing.Optional[bool]


# OrderableDBInstanceOptionsMessageTypeDef

### OrderableDBInstanceOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.OrderableDBInstanceOptionTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OutpostTypeDef

### Arn
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterOutputTypeDef

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

### SupportedEngineModes
- **Type**: typing.Optional[typing.List[str]]


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

### SupportedEngineModes
- **Type**: typing.Optional[typing.Sequence[str]]


# ParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.ResourcePendingMaintenanceActionsTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PendingCloudwatchLogsExportsTypeDef]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.ProcessorFeatureTypeDef]]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### AutomationMode
- **Type**: typing.Optional[typing.Literal['all-paused', 'full']]

### ResumeFullAutomationModeTime
- **Type**: typing.Optional[datetime.datetime]

### StorageThroughput
- **Type**: typing.Optional[int]

### Engine
- **Type**: typing.Optional[str]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### MultiTenant
- **Type**: typing.Optional[bool]


# PerformanceInsightsMetricDimensionGroupTypeDef

### Dimensions
- **Type**: typing.Optional[typing.List[str]]

### Group
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# PerformanceInsightsMetricQueryTypeDef

### GroupBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PerformanceInsightsMetricDimensionGroupTypeDef]

### Metric
- **Type**: typing.Optional[str]


# PerformanceIssueDetailsTypeDef

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.MetricTypeDef]]

### Analysis
- **Type**: typing.Optional[str]


# ProcessorFeatureTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# PromoteReadReplicaDBClusterMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PromoteReadReplicaDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PromoteReadReplicaMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### PreferredBackupWindow
- **Type**: typing.Optional[str]


# PromoteReadReplicaResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PurchaseReservedDBInstancesOfferingMessageTypeDef

### ReservedDBInstancesOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedDBInstanceId
- **Type**: typing.Optional[str]

### DBInstanceCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# PurchaseReservedDBInstancesOfferingResultTypeDef

### ReservedDBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ReservedDBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RangeTypeDef

### From
- **Type**: typing.Optional[int]

### To
- **Type**: typing.Optional[int]

### Step
- **Type**: typing.Optional[int]


# RdsCustomClusterConfigurationTypeDef

### InterconnectSubnetId
- **Type**: typing.Optional[str]

### TransitGatewayMulticastDomainId
- **Type**: typing.Optional[str]

### ReplicaMode
- **Type**: typing.Optional[typing.Literal['mounted', 'open-read-only']]


# RebootDBClusterMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RebootDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RebootDBInstanceMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ForceFailover
- **Type**: typing.Optional[bool]


# RebootDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RebootDBShardGroupMessageTypeDef

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RecommendedActionParameterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# RecommendedActionTypeDef

### ActionId
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.RecommendedActionParameterTypeDef]]

### ApplyModes
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[str]

### IssueDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.IssueDetailsTypeDef]

### ContextAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.ContextAttributeTypeDef]]


# RecommendedActionUpdateTypeDef

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes


# RecurringChargeTypeDef

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# ReferenceDetailsTypeDef

### ScalarReferenceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ScalarReferenceDetailsTypeDef]


# RegisterDBProxyTargetsRequestTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### DBInstanceIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### DBClusterIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# RegisterDBProxyTargetsResponseTypeDef

### DBProxyTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.DBProxyTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveFromGlobalClusterMessageTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterIdentifier
- **Type**: typing.Optional[str]


# RemoveFromGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveRoleFromDBClusterMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: typing.Optional[str]


# RemoveRoleFromDBInstanceMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveSourceIdentifierFromSubscriptionMessageTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveSourceIdentifierFromSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTagsFromResourceMessageTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReservedDBInstanceMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedDBInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.ReservedDBInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReservedDBInstanceTypeDef

### ReservedDBInstanceId
- **Type**: typing.Optional[str]

### ReservedDBInstancesOfferingId
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### UsagePrice
- **Type**: typing.Optional[float]

### CurrencyCode
- **Type**: typing.Optional[str]

### DBInstanceCount
- **Type**: typing.Optional[int]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### State
- **Type**: typing.Optional[str]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.RecurringChargeTypeDef]]

### ReservedDBInstanceArn
- **Type**: typing.Optional[str]

### LeaseId
- **Type**: typing.Optional[str]


# ReservedDBInstancesOfferingMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedDBInstancesOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.ReservedDBInstancesOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReservedDBInstancesOfferingTypeDef

### ReservedDBInstancesOfferingId
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### UsagePrice
- **Type**: typing.Optional[float]

### CurrencyCode
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.RecurringChargeTypeDef]]


# ResetDBClusterParameterGroupMessageTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ParameterUnionTypeDef]]


# ResetDBParameterGroupMessageTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ParameterUnionTypeDef]]


# ResourcePendingMaintenanceActionsTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### PendingMaintenanceActionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.PendingMaintenanceActionTypeDef]]


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


# RestoreDBClusterFromS3MessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### MasterUsername
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEngine
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3IngestionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### CharacterSetName
- **Type**: typing.Optional[str]

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

### MasterUserPassword
- **Type**: typing.Optional[str]

### OptionGroupName
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### S3Prefix
- **Type**: typing.Optional[str]

### BacktrackWindow
- **Type**: typing.Optional[int]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### Domain
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ServerlessV2ScalingConfigurationTypeDef]

### NetworkType
- **Type**: typing.Optional[str]

### ManageMasterUserPassword
- **Type**: typing.Optional[bool]

### MasterUserSecretKmsKeyId
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# RestoreDBClusterFromS3ResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreDBClusterFromSnapshotMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### BacktrackWindow
- **Type**: typing.Optional[int]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### EngineMode
- **Type**: typing.Optional[str]

### ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ScalingConfigurationTypeDef]

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### Domain
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### DBClusterInstanceClass
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ServerlessV2ScalingConfigurationTypeDef]

### NetworkType
- **Type**: typing.Optional[str]

### RdsCustomClusterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.RdsCustomClusterConfigurationTypeDef]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# RestoreDBClusterFromSnapshotResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreDBClusterToPointInTimeMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreType
- **Type**: typing.Optional[str]

### SourceDBClusterIdentifier
- **Type**: typing.Optional[str]

### RestoreToTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### BacktrackWindow
- **Type**: typing.Optional[int]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### Domain
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ScalingConfigurationTypeDef]

### EngineMode
- **Type**: typing.Optional[str]

### DBClusterInstanceClass
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Iops
- **Type**: typing.Optional[int]

### ServerlessV2ScalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.ServerlessV2ScalingConfigurationTypeDef]

### NetworkType
- **Type**: typing.Optional[str]

### SourceDbClusterResourceId
- **Type**: typing.Optional[str]

### RdsCustomClusterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.RdsCustomClusterConfigurationTypeDef]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# RestoreDBClusterToPointInTimeResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreDBInstanceFromDBSnapshotMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### LicenseModel
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### TdeCredentialPassword
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Domain
- **Type**: typing.Optional[str]

### DomainFqdn
- **Type**: typing.Optional[str]

### DomainOu
- **Type**: typing.Optional[str]

### DomainAuthSecretArn
- **Type**: typing.Optional[str]

### DomainDnsIps
- **Type**: typing.Optional[typing.Sequence[str]]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ProcessorFeatureTypeDef]]

### UseDefaultProcessorFeatures
- **Type**: typing.Optional[bool]

### DBParameterGroupName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### EnableCustomerOwnedIp
- **Type**: typing.Optional[bool]

### CustomIamInstanceProfile
- **Type**: typing.Optional[str]

### BackupTarget
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# RestoreDBInstanceFromDBSnapshotResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreDBInstanceFromS3MessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstanceClass
- **Type**: <class 'str'>
- **Required**: Yes

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEngine
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3IngestionRoleArn
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

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### StorageType
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### S3Prefix
- **Type**: typing.Optional[str]

### DatabaseInsightsMode
- **Type**: typing.Optional[typing.Literal['advanced', 'standard']]

### EnablePerformanceInsights
- **Type**: typing.Optional[bool]

### PerformanceInsightsKMSKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ProcessorFeatureTypeDef]]

### UseDefaultProcessorFeatures
- **Type**: typing.Optional[bool]

### DeletionProtection
- **Type**: typing.Optional[bool]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]

### NetworkType
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]

### ManageMasterUserPassword
- **Type**: typing.Optional[bool]

### MasterUserSecretKmsKeyId
- **Type**: typing.Optional[str]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# RestoreDBInstanceFromS3ResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreDBInstanceToPointInTimeMessageTypeDef

### TargetDBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDBInstanceIdentifier
- **Type**: typing.Optional[str]

### RestoreTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TimestampTypeDef]

### UseLatestRestorableTime
- **Type**: typing.Optional[bool]

### DBInstanceClass
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### LicenseModel
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### TdeCredentialPassword
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Domain
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### DomainFqdn
- **Type**: typing.Optional[str]

### DomainOu
- **Type**: typing.Optional[str]

### DomainAuthSecretArn
- **Type**: typing.Optional[str]

### DomainDnsIps
- **Type**: typing.Optional[typing.Sequence[str]]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.ProcessorFeatureTypeDef]]

### UseDefaultProcessorFeatures
- **Type**: typing.Optional[bool]

### DBParameterGroupName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### SourceDbiResourceId
- **Type**: typing.Optional[str]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]

### SourceDBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]

### EnableCustomerOwnedIp
- **Type**: typing.Optional[bool]

### CustomIamInstanceProfile
- **Type**: typing.Optional[str]

### BackupTarget
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]

### AllocatedStorage
- **Type**: typing.Optional[int]

### DedicatedLogVolume
- **Type**: typing.Optional[bool]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# RestoreDBInstanceToPointInTimeResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreWindowTypeDef

### EarliestTime
- **Type**: typing.Optional[datetime.datetime]

### LatestTime
- **Type**: typing.Optional[datetime.datetime]


# RevokeDBSecurityGroupIngressMessageTypeDef

### DBSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CIDRIP
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupId
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# RevokeDBSecurityGroupIngressResultTypeDef

### DBSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ScalarReferenceDetailsTypeDef

### Value
- **Type**: typing.Optional[float]


# ScalingConfigurationInfoTypeDef

### MinCapacity
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[int]

### AutoPause
- **Type**: typing.Optional[bool]

### SecondsUntilAutoPause
- **Type**: typing.Optional[int]

### TimeoutAction
- **Type**: typing.Optional[str]

### SecondsBeforeTimeout
- **Type**: typing.Optional[int]


# ScalingConfigurationTypeDef

### MinCapacity
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[int]

### AutoPause
- **Type**: typing.Optional[bool]

### SecondsUntilAutoPause
- **Type**: typing.Optional[int]

### TimeoutAction
- **Type**: typing.Optional[str]

### SecondsBeforeTimeout
- **Type**: typing.Optional[int]


# ServerlessV2FeaturesSupportTypeDef

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]


# ServerlessV2ScalingConfigurationInfoTypeDef

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]

### SecondsUntilAutoPause
- **Type**: typing.Optional[int]


# ServerlessV2ScalingConfigurationTypeDef

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]

### SecondsUntilAutoPause
- **Type**: typing.Optional[int]


# SourceRegionMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### SourceRegions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.SourceRegionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SourceRegionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartActivityStreamRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Literal['async', 'sync']
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: typing.Optional[bool]

### EngineNativeAuditFieldsIncluded
- **Type**: typing.Optional[bool]


# StartActivityStreamResponseTypeDef

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['started', 'starting', 'stopped', 'stopping']
- **Required**: Yes

### Mode
- **Type**: typing.Literal['async', 'sync']
- **Required**: Yes

### ApplyImmediately
- **Type**: <class 'bool'>
- **Required**: Yes

### EngineNativeAuditFieldsIncluded
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDBClusterMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDBInstanceAutomatedBackupsReplicationMessageTypeDef

### SourceDBInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### PreSignedUrl
- **Type**: typing.Optional[str]

### SourceRegion
- **Type**: typing.Optional[str]


# StartDBInstanceAutomatedBackupsReplicationResultTypeDef

### DBInstanceAutomatedBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceAutomatedBackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDBInstanceMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartExportTaskMessageTypeDef

### ExportTaskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: typing.Optional[str]

### ExportOnly
- **Type**: typing.Optional[typing.Sequence[str]]


# StopActivityStreamRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: typing.Optional[bool]


# StopActivityStreamResponseTypeDef

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['started', 'starting', 'stopped', 'stopping']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDBClusterMessageTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDBInstanceAutomatedBackupsReplicationMessageTypeDef

### SourceDBInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopDBInstanceAutomatedBackupsReplicationResultTypeDef

### DBInstanceAutomatedBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceAutomatedBackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDBInstanceMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]


# StopDBInstanceResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubnetTypeDef

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.AvailabilityZoneTypeDef]

### SubnetOutpost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.OutpostTypeDef]

### SubnetStatus
- **Type**: typing.Optional[str]


# SwitchoverBlueGreenDeploymentRequestTypeDef

### BlueGreenDeploymentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SwitchoverTimeout
- **Type**: typing.Optional[int]


# SwitchoverBlueGreenDeploymentResponseTypeDef

### BlueGreenDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.BlueGreenDeploymentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SwitchoverDetailTypeDef

### SourceMember
- **Type**: typing.Optional[str]

### TargetMember
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# SwitchoverGlobalClusterMessageTypeDef

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDbClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# SwitchoverGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SwitchoverReadReplicaMessageTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# SwitchoverReadReplicaResultTypeDef

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagListMessageTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TargetHealthTypeDef

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'REGISTERING', 'UNAVAILABLE']]

### Reason
- **Type**: typing.Optional[typing.Literal['AUTH_FAILURE', 'CONNECTION_FAILED', 'INVALID_REPLICATION_STATE', 'PENDING_PROXY_CAPACITY', 'UNREACHABLE']]

### Description
- **Type**: typing.Optional[str]


# TenantDatabasePendingModifiedValuesTypeDef

### MasterUserPassword
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]


# TenantDatabaseTypeDef

### TenantDatabaseCreateTime
- **Type**: typing.Optional[datetime.datetime]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### DbiResourceId
- **Type**: typing.Optional[str]

### TenantDatabaseResourceId
- **Type**: typing.Optional[str]

### TenantDatabaseARN
- **Type**: typing.Optional[str]

### CharacterSetName
- **Type**: typing.Optional[str]

### NcharCharacterSetName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TenantDatabasePendingModifiedValuesTypeDef]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# TenantDatabasesMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### TenantDatabases
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_classes.TenantDatabaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### SupportedEngineModes
- **Type**: typing.Optional[typing.List[str]]

### SupportsParallelQuery
- **Type**: typing.Optional[bool]

### SupportsGlobalDatabases
- **Type**: typing.Optional[bool]

### SupportsBabelfish
- **Type**: typing.Optional[bool]

### SupportsLimitlessDatabase
- **Type**: typing.Optional[bool]

### SupportsLocalWriteForwarding
- **Type**: typing.Optional[bool]

### SupportsIntegrations
- **Type**: typing.Optional[bool]


# UserAuthConfigInfoTypeDef

### Description
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### AuthScheme
- **Type**: typing.Optional[typing.Literal['SECRETS']]

### SecretArn
- **Type**: typing.Optional[str]

### IAMAuth
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'REQUIRED']]

### ClientPasswordAuthType
- **Type**: typing.Optional[typing.Literal['MYSQL_CACHING_SHA2_PASSWORD', 'MYSQL_NATIVE_PASSWORD', 'POSTGRES_MD5', 'POSTGRES_SCRAM_SHA_256', 'SQL_SERVER_AUTHENTICATION']]


# UserAuthConfigTypeDef

### Description
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### AuthScheme
- **Type**: typing.Optional[typing.Literal['SECRETS']]

### SecretArn
- **Type**: typing.Optional[str]

### IAMAuth
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'REQUIRED']]

### ClientPasswordAuthType
- **Type**: typing.Optional[typing.Literal['MYSQL_CACHING_SHA2_PASSWORD', 'MYSQL_NATIVE_PASSWORD', 'POSTGRES_MD5', 'POSTGRES_SCRAM_SHA_256', 'SQL_SERVER_AUTHENTICATION']]


# ValidDBInstanceModificationsMessageTypeDef

### Storage
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.ValidStorageOptionsTypeDef]]

### ValidProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.AvailableProcessorFeatureTypeDef]]

### SupportsDedicatedLogVolume
- **Type**: typing.Optional[bool]


# ValidStorageOptionsTypeDef

### StorageType
- **Type**: typing.Optional[str]

### StorageSize
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.RangeTypeDef]]

### ProvisionedIops
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.RangeTypeDef]]

### IopsToStorageRatio
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DoubleRangeTypeDef]]

### SupportsStorageAutoscaling
- **Type**: typing.Optional[bool]

### ProvisionedStorageThroughput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.RangeTypeDef]]

### StorageThroughputToIopsRatio
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_classes.DoubleRangeTypeDef]]


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



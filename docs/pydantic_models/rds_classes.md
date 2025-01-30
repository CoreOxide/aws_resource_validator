# rds_classes

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


# AddRoleToDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: typing.Optional[str]


# AddRoleToDBInstanceMessageRequestTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes


# AddSourceIdentifierToSubscriptionMessageRequestTypeDef

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


# AddTagsToResourceMessageRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResourcePendingMaintenanceActionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthorizeDBSecurityGroupIngressMessageRequestTypeDef

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


# BacktrackDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BacktrackTo
- **Type**: typing.Union[datetime.datetime, str]
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


# CancelExportTaskMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CopyDBClusterParameterGroupResultTypeDef

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CopyDBParameterGroupResultTypeDef

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopyDBSnapshotMessageRequestTypeDef

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


# CopyOptionGroupMessageRequestTypeDef

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


# CreateBlueGreenDeploymentRequestRequestTypeDef

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


# CreateBlueGreenDeploymentResponseTypeDef

### BlueGreenDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.BlueGreenDeploymentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomDBEngineVersionMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


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


# CreateDBClusterSnapshotMessageRequestTypeDef

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


# CreateDBInstanceReadReplicaMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBParameterGroupResultTypeDef

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDBProxyEndpointRequestRequestTypeDef

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


# CreateDBProxyRequestRequestTypeDef

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


# CreateDBSecurityGroupMessageRequestTypeDef

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


# CreateDBShardGroupMessageRequestTypeDef

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

### PubliclyAccessible
- **Type**: typing.Optional[bool]


# CreateDBSnapshotMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateDBSubnetGroupResultTypeDef

### DBSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.TagTypeDef]]


# CreateEventSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGlobalClusterMessageRequestTypeDef

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


# CreateGlobalClusterResultTypeDef

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.GlobalClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntegrationMessageRequestTypeDef

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


# CreateOptionGroupMessageRequestTypeDef

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


# CreateTenantDatabaseMessageRequestTypeDef

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

### TargetArn
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### TrackedClusterId
- **Type**: typing.Optional[str]

### RdsResourceId
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[typing.Literal['RDS_INSTANCE', 'RDS_SERVERLESS_ENDPOINT', 'TRACKED_CLUSTER']]

### Role
- **Type**: typing.Optional[typing.Literal['READ_ONLY', 'READ_WRITE', 'UNKNOWN']]

### TargetHealth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.TargetHealthTypeDef]


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

### ComputeRedundancy
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[str]


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


# DeleteBlueGreenDeploymentRequestRequestTypeDef

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


# DeleteCustomDBEngineVersionMessageRequestTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterAutomatedBackupMessageRequestTypeDef

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


# DeleteDBClusterEndpointMessageRequestTypeDef

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DeleteAutomatedBackups
- **Type**: typing.Optional[bool]


# DeleteDBClusterParameterGroupMessageRequestTypeDef

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


# DeleteDBClusterSnapshotMessageRequestTypeDef

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


# DeleteDBInstanceAutomatedBackupMessageRequestTypeDef

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


# DeleteDBInstanceMessageRequestTypeDef

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


# DeleteDBParameterGroupMessageRequestTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBProxyEndpointRequestRequestTypeDef

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


# DeleteDBProxyRequestRequestTypeDef

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


# DeleteDBSecurityGroupMessageRequestTypeDef

### DBSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBShardGroupMessageRequestTypeDef

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBSnapshotMessageRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGlobalClusterMessageRequestTypeDef

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


# DeleteIntegrationMessageRequestTypeDef

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOptionGroupMessageRequestTypeDef

### OptionGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTenantDatabaseMessageRequestTypeDef

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


# DeregisterDBProxyTargetsRequestRequestTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### DBInstanceIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### DBClusterIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeBlueGreenDeploymentsRequestDescribeBlueGreenDeploymentsPaginateTypeDef

### BlueGreenDeploymentIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeBlueGreenDeploymentsRequestRequestTypeDef

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


# DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef

### CertificateIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeCertificatesMessageRequestTypeDef

### CertificateIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterAutomatedBackupsMessageRequestTypeDef

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


# DescribeDBClusterBacktracksMessageDescribeDBClusterBacktracksPaginateTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BacktrackIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterBacktracksMessageRequestTypeDef

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


# DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterEndpointIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterEndpointsMessageRequestTypeDef

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


# DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterParameterGroupsMessageRequestTypeDef

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClusterParametersMessageRequestTypeDef

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


# DescribeDBClusterSnapshotAttributesMessageRequestTypeDef

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


# DescribeDBClusterSnapshotsMessageDBClusterSnapshotAvailableWaitTypeDef

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


# DescribeDBClusterSnapshotsMessageDBClusterSnapshotDeletedWaitTypeDef

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


# DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef

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


# DescribeDBClusterSnapshotsMessageRequestTypeDef

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


# DescribeDBClustersMessageDBClusterAvailableWaitTypeDef

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


# DescribeDBClustersMessageDBClusterDeletedWaitTypeDef

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


# DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### IncludeShared
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBClustersMessageRequestTypeDef

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


# DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef

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


# DescribeDBEngineVersionsMessageRequestTypeDef

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


# DescribeDBInstanceAutomatedBackupsMessageDescribeDBInstanceAutomatedBackupsPaginateTypeDef

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


# DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef

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


# DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef

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


# DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef

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


# DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBInstancesMessageRequestTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBLogFilesDetailsTypeDef

### LogFileName
- **Type**: typing.Optional[str]

### LastWritten
- **Type**: typing.Optional[int]

### Size
- **Type**: typing.Optional[int]


# DescribeDBLogFilesMessageDescribeDBLogFilesPaginateTypeDef

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


# DescribeDBLogFilesMessageRequestTypeDef

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


# DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateTypeDef

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBParameterGroupsMessageRequestTypeDef

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBParametersMessageRequestTypeDef

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


# DescribeDBProxiesRequestDescribeDBProxiesPaginateTypeDef

### DBProxyName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBProxiesRequestRequestTypeDef

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


# DescribeDBProxyEndpointsRequestDescribeDBProxyEndpointsPaginateTypeDef

### DBProxyName
- **Type**: typing.Optional[str]

### DBProxyEndpointName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBProxyEndpointsRequestRequestTypeDef

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


# DescribeDBProxyTargetGroupsRequestDescribeDBProxyTargetGroupsPaginateTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBProxyTargetGroupsRequestRequestTypeDef

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


# DescribeDBProxyTargetsRequestDescribeDBProxyTargetsPaginateTypeDef

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBProxyTargetsRequestRequestTypeDef

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


# DescribeDBRecommendationsMessageDescribeDBRecommendationsPaginateTypeDef

### LastUpdatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastUpdatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Locale
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBRecommendationsMessageRequestTypeDef

### LastUpdatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastUpdatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Locale
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBSecurityGroupsMessageDescribeDBSecurityGroupsPaginateTypeDef

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBSecurityGroupsMessageRequestTypeDef

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBShardGroupsMessageRequestTypeDef

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


# DescribeDBSnapshotAttributesMessageRequestTypeDef

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


# DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef

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


# DescribeDBSnapshotsMessageDBSnapshotAvailableWaitTypeDef

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


# DescribeDBSnapshotsMessageDBSnapshotCompletedWaitTypeDef

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


# DescribeDBSnapshotsMessageDBSnapshotDeletedWaitTypeDef

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


# DescribeDBSnapshotsMessageDescribeDBSnapshotsPaginateTypeDef

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


# DescribeDBSnapshotsMessageRequestTypeDef

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


# DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeDBSubnetGroupsMessageRequestTypeDef

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultClusterParametersMessageDescribeEngineDefaultClusterParametersPaginateTypeDef

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeEngineDefaultClusterParametersMessageRequestTypeDef

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


# DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeEngineDefaultParametersMessageRequestTypeDef

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


# DescribeEventCategoriesMessageRequestTypeDef

### SourceType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]


# DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeEventSubscriptionsMessageRequestTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventsMessageDescribeEventsPaginateTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['blue-green-deployment', 'custom-engine-version', 'db-cluster', 'db-cluster-snapshot', 'db-instance', 'db-parameter-group', 'db-proxy', 'db-security-group', 'db-snapshot']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeEventsMessageRequestTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['blue-green-deployment', 'custom-engine-version', 'db-cluster', 'db-cluster-snapshot', 'db-instance', 'db-parameter-group', 'db-proxy', 'db-security-group', 'db-snapshot']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# DescribeExportTasksMessageDescribeExportTasksPaginateTypeDef

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


# DescribeExportTasksMessageRequestTypeDef

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


# DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeGlobalClustersMessageRequestTypeDef

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeIntegrationsMessageDescribeIntegrationsPaginateTypeDef

### IntegrationIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeIntegrationsMessageRequestTypeDef

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


# DescribeOptionGroupOptionsMessageDescribeOptionGroupOptionsPaginateTypeDef

### EngineName
- **Type**: <class 'str'>
- **Required**: Yes

### MajorEngineVersion
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeOptionGroupOptionsMessageRequestTypeDef

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


# DescribeOptionGroupsMessageDescribeOptionGroupsPaginateTypeDef

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


# DescribeOptionGroupsMessageRequestTypeDef

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

### AvailabilityZoneGroup
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


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


# DescribePendingMaintenanceActionsMessageRequestTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeReservedDBInstancesMessageDescribeReservedDBInstancesPaginateTypeDef

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


# DescribeReservedDBInstancesMessageRequestTypeDef

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


# DescribeReservedDBInstancesOfferingsMessageDescribeReservedDBInstancesOfferingsPaginateTypeDef

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


# DescribeReservedDBInstancesOfferingsMessageRequestTypeDef

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


# DescribeSourceRegionsMessageDescribeSourceRegionsPaginateTypeDef

### RegionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeSourceRegionsMessageRequestTypeDef

### RegionName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]


# DescribeTenantDatabasesMessageDescribeTenantDatabasesPaginateTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DescribeTenantDatabasesMessageRequestTypeDef

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


# DescribeTenantDatabasesMessageTenantDatabaseAvailableWaitTypeDef

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


# DescribeTenantDatabasesMessageTenantDatabaseDeletedWaitTypeDef

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


# DescribeValidDBInstanceModificationsMessageRequestTypeDef

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


# DisableHttpEndpointRequestRequestTypeDef

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

### Text
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


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


# DownloadDBLogFilePortionMessageDownloadDBLogFilePortionPaginateTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### LogFileName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.PaginatorConfigTypeDef]


# DownloadDBLogFilePortionMessageRequestTypeDef

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


# EnableHttpEndpointRequestRequestTypeDef

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


# FailoverDBClusterMessageRequestTypeDef

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


# FailoverGlobalClusterMessageRequestTypeDef

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

### FailoverState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_classes.FailoverStateTypeDef]


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


# ListTagsForResourceMessageRequestTypeDef

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


# ModifyActivityStreamRequestRequestTypeDef

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


# ModifyCertificatesMessageRequestTypeDef

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


# ModifyCurrentDBClusterCapacityMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Capacity
- **Type**: typing.Optional[int]

### SecondsBeforeTimeout
- **Type**: typing.Optional[int]

### TimeoutAction
- **Type**: typing.Optional[str]


# ModifyCustomDBEngineVersionMessageRequestTypeDef

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


# ModifyDBClusterParameterGroupMessageRequestTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.rds_classes.ParameterTypeDef, aws_resource_validator.pydantic_models.rds_classes.ParameterExtraOutputTypeDef]]
- **Required**: Yes


# ModifyDBClusterResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterSnapshotAttributesResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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


# ModifyDBParameterGroupMessageRequestTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.rds_classes.ParameterTypeDef, aws_resource_validator.pydantic_models.rds_classes.ParameterExtraOutputTypeDef]]
- **Required**: Yes


# ModifyDBProxyEndpointRequestRequestTypeDef

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


# ModifyDBProxyRequestRequestTypeDef

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


# ModifyDBProxyTargetGroupRequestRequestTypeDef

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


# ModifyDBRecommendationMessageRequestTypeDef

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### Locale
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### RecommendedActionUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_classes.RecommendedActionUpdateTypeDef]]


# ModifyDBShardGroupMessageRequestTypeDef

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxACU
- **Type**: typing.Optional[float]


# ModifyDBSnapshotAttributeMessageRequestTypeDef

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


# ModifyDBSnapshotMessageRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyGlobalClusterMessageRequestTypeDef

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


# ModifyIntegrationMessageRequestTypeDef

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: typing.Optional[str]

### DataFilter
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ModifyOptionGroupMessageRequestTypeDef

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


# ModifyTenantDatabaseMessageRequestTypeDef

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


# ParameterExtraOutputTypeDef

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


# PromoteReadReplicaDBClusterMessageRequestTypeDef

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


# PromoteReadReplicaMessageRequestTypeDef

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


# PurchaseReservedDBInstancesOfferingMessageRequestTypeDef

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


# RebootDBClusterMessageRequestTypeDef

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


# RebootDBInstanceMessageRequestTypeDef

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


# RebootDBShardGroupMessageRequestTypeDef

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


# RegisterDBProxyTargetsRequestRequestTypeDef

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


# RemoveFromGlobalClusterMessageRequestTypeDef

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


# RemoveRoleFromDBClusterMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: typing.Optional[str]


# RemoveRoleFromDBInstanceMessageRequestTypeDef

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef

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


# RemoveTagsFromResourceMessageRequestTypeDef

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


# ResetDBClusterParameterGroupMessageRequestTypeDef

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.rds_classes.ParameterTypeDef, aws_resource_validator.pydantic_models.rds_classes.ParameterExtraOutputTypeDef]]]


# ResetDBParameterGroupMessageRequestTypeDef

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.rds_classes.ParameterTypeDef, aws_resource_validator.pydantic_models.rds_classes.ParameterExtraOutputTypeDef]]]


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


# RestoreDBClusterFromS3MessageRequestTypeDef

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

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# RestoreDBClusterFromSnapshotResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreDBClusterToPointInTimeMessageRequestTypeDef

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreType
- **Type**: typing.Optional[str]

### SourceDBClusterIdentifier
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

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# RestoreDBClusterToPointInTimeResultTypeDef

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.DBClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef

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


# RestoreDBInstanceFromS3MessageRequestTypeDef

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


# RestoreDBInstanceToPointInTimeMessageRequestTypeDef

### TargetDBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDBInstanceIdentifier
- **Type**: typing.Optional[str]

### RestoreTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# RevokeDBSecurityGroupIngressMessageRequestTypeDef

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

### RegionName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SupportsDBInstanceAutomatedBackupsReplication
- **Type**: typing.Optional[bool]


# StartActivityStreamRequestRequestTypeDef

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


# StartDBClusterMessageRequestTypeDef

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


# StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef

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


# StartDBInstanceMessageRequestTypeDef

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


# StartExportTaskMessageRequestTypeDef

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


# StopActivityStreamRequestRequestTypeDef

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


# StopDBClusterMessageRequestTypeDef

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


# StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef

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


# StopDBInstanceMessageRequestTypeDef

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


# SwitchoverBlueGreenDeploymentRequestRequestTypeDef

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


# SwitchoverGlobalClusterMessageRequestTypeDef

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


# SwitchoverReadReplicaMessageRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['MYSQL_NATIVE_PASSWORD', 'POSTGRES_MD5', 'POSTGRES_SCRAM_SHA_256', 'SQL_SERVER_AUTHENTICATION']]


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
- **Type**: typing.Optional[typing.Literal['MYSQL_NATIVE_PASSWORD', 'POSTGRES_MD5', 'POSTGRES_SCRAM_SHA_256', 'SQL_SERVER_AUTHENTICATION']]


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



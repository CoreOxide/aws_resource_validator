# Rds Classes

# AccountAttributesMessage

### AccountQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.AccountQuota]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# AccountQuota

### AccountQuotaName
- **Type**: typing.Optional[str]

### Used
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# AddRoleToDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: typing.Optional[str]


# AddRoleToDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes


# AddSourceIdentifierToSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# AddSourceIdentifierToSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsToResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResourcePendingMaintenanceActions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# AuthorizeDBSecurityGroupIngressMessage

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


# AuthorizeDBSecurityGroupIngressResult

### DBSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# AvailabilityZone

### Name
- **Type**: typing.Optional[str]


# AvailableProcessorFeature

### Name
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]


# BacktrackDBClusterMessage

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

# BlueGreenDeployment

### BlueGreenDeploymentIdentifier
- **Type**: typing.Optional[str]

### BlueGreenDeploymentName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### SwitchoverDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.SwitchoverDetail]]

### Tasks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.BlueGreenDeploymentTask]]

### Status
- **Type**: typing.Optional[str]

### StatusDetails
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### DeleteTime
- **Type**: typing.Optional[datetime.datetime]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# BlueGreenDeploymentTask

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# CancelExportTaskMessage

### ExportTaskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


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

### CustomerOverride
- **Type**: typing.Optional[bool]

### CustomerOverrideValidTill
- **Type**: typing.Optional[datetime.datetime]


# CertificateDetails

### CAIdentifier
- **Type**: typing.Optional[str]

### ValidTill
- **Type**: typing.Optional[datetime.datetime]


# CertificateMessage

### DefaultCertificateForNewLaunches
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Certificate]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CharacterSet

### CharacterSetName
- **Type**: typing.Optional[str]

### CharacterSetDescription
- **Type**: typing.Optional[str]


# ClientGenerateDbAuthTokenRequest

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
- **Type**: <class 'NoneType'>

### Iops
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[str]

### CertificateDetails
- **Type**: <class 'NoneType'>


# ConnectionPoolConfiguration

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


# ConnectionPoolConfigurationInfo

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


# ContextAttribute

### Key
- **Type**: typing.Optional[str]

### Value
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CopyDBClusterParameterGroupResult

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### SourceRegion
- **Type**: typing.Optional[str]


# CopyDBClusterSnapshotResult

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CopyDBParameterGroupResult

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CopyDBSnapshotMessage

### SourceDBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

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


# CopyDBSnapshotResult

### DBSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CopyOptionGroupMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CopyOptionGroupResult

### OptionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.OptionGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBlueGreenDeploymentRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

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


# CreateBlueGreenDeploymentResponse

### BlueGreenDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.BlueGreenDeployment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomDBEngineVersionMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### SourceCustomDbEngineVersionIdentifier
- **Type**: typing.Optional[str]

### UseAwsProvidedLatestImage
- **Type**: typing.Optional[bool]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

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
- **Type**: typing.Optional[typing.List[str]]

### EngineMode
- **Type**: typing.Optional[str]

### ScalingConfiguration
- **Type**: <class 'NoneType'>

### RdsCustomClusterConfiguration
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateDBClusterParameterGroupResult

### DBClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBClusterSnapshotMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateDBClusterSnapshotResult

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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

### NcharCharacterSetName
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

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
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[typing.List[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ProcessorFeature]]

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


# CreateDBInstanceReadReplicaMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[typing.List[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ProcessorFeature]]

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
- **Type**: typing.Optional[typing.List[str]]

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


# CreateDBInstanceReadReplicaResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateDBParameterGroupResult

### DBParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBProxyEndpointRequest

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### DBProxyEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### TargetRole
- **Type**: typing.Optional[typing.Literal['READ_ONLY', 'READ_WRITE']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateDBProxyEndpointResponse

### DBProxyEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBProxyEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBProxyRequest

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineFamily
- **Type**: typing.Literal['MYSQL', 'POSTGRESQL', 'SQLSERVER']
- **Required**: Yes

### Auth
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.UserAuthConfig]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### RequireTLS
- **Type**: typing.Optional[bool]

### IdleClientTimeout
- **Type**: typing.Optional[int]

### DebugLogging
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateDBProxyResponse

### DBProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBProxy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBSecurityGroupMessage

### DBSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DBSecurityGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateDBSecurityGroupResult

### DBSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDBShardGroupMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateDBSnapshotMessage

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateDBSnapshotResult

### DBSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateDBSubnetGroupResult

### DBSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateEventSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGlobalClusterMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntegrationMessage

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### DataFilter
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# CreateOptionGroupMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateOptionGroupResult

### OptionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.OptionGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTenantDatabaseMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# CreateTenantDatabaseResult

### TenantDatabase
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.TenantDatabase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# CustomDBEngineVersionAMI

### ImageId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterOptionGroupStatus]]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReplicationSourceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterStatusInfo]]

### DBClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterMember]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.VpcSecurityGroupMembership]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterRole]]

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
- **Type**: <class 'NoneType'>

### RdsCustomClusterConfiguration
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DomainMembership]]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### GlobalWriteForwardingStatus
- **Type**: typing.Optional[typing.Literal['disabled', 'disabling', 'enabled', 'enabling', 'unknown']]

### GlobalWriteForwardingRequested
- **Type**: typing.Optional[bool]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.ClusterPendingModifiedValues]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.ServerlessV2ScalingConfigurationInfo]

### NetworkType
- **Type**: typing.Optional[str]

### DBSystemId
- **Type**: typing.Optional[str]

### MasterUserSecret
- **Type**: <class 'NoneType'>

### IOOptimizedNextAllowedModificationTime
- **Type**: typing.Optional[datetime.datetime]

### LocalWriteForwardingStatus
- **Type**: typing.Optional[typing.Literal['disabled', 'disabling', 'enabled', 'enabling', 'requested']]

### AwsBackupRecoveryPointArn
- **Type**: typing.Optional[str]

### LimitlessDatabase
- **Type**: <class 'NoneType'>

### StorageThroughput
- **Type**: typing.Optional[int]

### ClusterScalabilityType
- **Type**: typing.Optional[typing.Literal['limitless', 'standard']]

### CertificateDetails
- **Type**: <class 'NoneType'>

### EngineLifecycleSupport
- **Type**: typing.Optional[str]


# DBClusterAutomatedBackup

### Engine
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### DBClusterAutomatedBackupsArn
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### RestoreWindow
- **Type**: <class 'NoneType'>

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


# DBClusterAutomatedBackupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterAutomatedBackups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterAutomatedBackup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterBacktrack

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


# DBClusterBacktrackMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterBacktracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterBacktrack]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterBacktrackResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterCapacityInfo

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterEndpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterEndpointResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ParameterOutput]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterParameterGroupNameMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterParameterGroupsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterParameterGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### DBSystemId
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### StorageThroughput
- **Type**: typing.Optional[int]


# DBClusterSnapshotAttribute

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[str]]


# DBClusterSnapshotAttributesResult

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterSnapshotAttribute]]


# DBClusterSnapshotMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBClusterSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterSnapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBClusterStatusInfo

### StatusType
- **Type**: typing.Optional[str]

### Normal
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.CharacterSet]

### Image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.CustomDBEngineVersionAMI]

### DBEngineMediaType
- **Type**: typing.Optional[str]

### SupportedCharacterSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.CharacterSet]]

### SupportedNcharCharacterSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.CharacterSet]]

### ValidUpgradeTarget
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.UpgradeTarget]]

### SupportedTimezones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Timezone]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

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
- **Type**: <class 'NoneType'>


# DBEngineVersionMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBEngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBEngineVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBEngineVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.CharacterSet'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.CustomDBEngineVersionAMI'>
- **Required**: Yes

### DBEngineMediaType
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedCharacterSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.CharacterSet]
- **Required**: Yes

### SupportedNcharCharacterSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.CharacterSet]
- **Required**: Yes

### ValidUpgradeTarget
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.UpgradeTarget]
- **Required**: Yes

### SupportedTimezones
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Timezone]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ServerlessV2FeaturesSupport'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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

### AutomaticRestartTime
- **Type**: typing.Optional[datetime.datetime]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBSecurityGroupMembership]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.VpcSecurityGroupMembership]]

### DBParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBParameterGroupStatus]]

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

### ReplicaMode
- **Type**: typing.Optional[typing.Literal['mounted', 'open-read-only']]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.OptionGroupMembership]]

### CharacterSetName
- **Type**: typing.Optional[str]

### NcharCharacterSetName
- **Type**: typing.Optional[str]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBInstanceStatusInfo]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DomainMembership]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ProcessorFeature]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### AssociatedRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBInstanceRole]]

### ListenerEndpoint
- **Type**: <class 'NoneType'>

### MaxAllocatedStorage
- **Type**: typing.Optional[int]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### DBInstanceAutomatedBackupsReplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBInstanceAutomatedBackupsReplication]]

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
- **Type**: <class 'NoneType'>

### CertificateDetails
- **Type**: <class 'NoneType'>

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


# DBInstanceAutomatedBackup

### DBInstanceArn
- **Type**: typing.Optional[str]

### DbiResourceId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### RestoreWindow
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBInstanceAutomatedBackupsReplication]]

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


# DBInstanceAutomatedBackupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstanceAutomatedBackups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBInstanceAutomatedBackup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBInstanceAutomatedBackupsReplication

### DBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]


# DBInstanceMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBInstanceRole

### RoleArn
- **Type**: typing.Optional[str]

### FeatureName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ParameterOutput]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBParameterGroupNameMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBParameterGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBProxy

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.UserAuthConfigInfo]]

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


# DBProxyEndpoint

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


# DBProxyTarget

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
- **Type**: <class 'NoneType'>


# DBProxyTargetGroup

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.ConnectionPoolConfigurationInfo]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### UpdatedDate
- **Type**: typing.Optional[datetime.datetime]


# DBRecommendation

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.RecommendedAction]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DocLink]]

### IssueDetails
- **Type**: <class 'NoneType'>


# DBRecommendationMessage

### DBRecommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBRecommendation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBRecommendationsMessage

### DBRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBRecommendation]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBSecurityGroup

### OwnerId
- **Type**: typing.Optional[str]

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### DBSecurityGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### EC2SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.EC2SecurityGroup]]

### IPRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.IPRange]]

### DBSecurityGroupArn
- **Type**: typing.Optional[str]


# DBSecurityGroupMembership

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# DBSecurityGroupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSecurityGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBSecurityGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBShardGroup

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# DBShardGroupResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBSnapshot

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ProcessorFeature]]

### DbiResourceId
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

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


# DBSnapshotAttribute

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[str]]


# DBSnapshotAttributesResult

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBSnapshotAttribute]]


# DBSnapshotMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBSnapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DBSnapshotTenantDatabase

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# DBSnapshotTenantDatabasesMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSnapshotTenantDatabases
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBSnapshotTenantDatabase]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Subnet]]

### DBSubnetGroupArn
- **Type**: typing.Optional[str]

### SupportedNetworkTypes
- **Type**: typing.Optional[typing.List[str]]


# DBSubnetGroupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DBSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBSubnetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBlueGreenDeploymentRequest

### BlueGreenDeploymentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteTarget
- **Type**: typing.Optional[bool]


# DeleteBlueGreenDeploymentResponse

### BlueGreenDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.BlueGreenDeployment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCustomDBEngineVersionMessage

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterAutomatedBackupMessage

### DbClusterResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterAutomatedBackupResult

### DBClusterAutomatedBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterAutomatedBackup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBClusterEndpointMessage

### DBClusterEndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DeleteAutomatedBackups
- **Type**: typing.Optional[bool]


# DeleteDBClusterParameterGroupMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBClusterSnapshotMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBClusterSnapshotResult

### DBClusterSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBInstanceAutomatedBackupMessage

### DbiResourceId
- **Type**: typing.Optional[str]

### DBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]


# DeleteDBInstanceAutomatedBackupResult

### DBInstanceAutomatedBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstanceAutomatedBackup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalSnapshot
- **Type**: typing.Optional[bool]

### FinalDBSnapshotIdentifier
- **Type**: typing.Optional[str]

### DeleteAutomatedBackups
- **Type**: typing.Optional[bool]


# DeleteDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBParameterGroupMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBProxyEndpointRequest

### DBProxyEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBProxyEndpointResponse

### DBProxyEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBProxyEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBProxyRequest

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBProxyResponse

### DBProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBProxy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDBSecurityGroupMessage

### DBSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBShardGroupMessage

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBSnapshotMessage

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDBSnapshotResult

### DBSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGlobalClusterMessage

### GlobalClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIntegrationMessage

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOptionGroupMessage

### OptionGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTenantDatabaseMessage

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


# DeleteTenantDatabaseResult

### TenantDatabase
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.TenantDatabase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterDBProxyTargetsRequest

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### DBInstanceIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DBClusterIdentifiers
- **Type**: typing.Optional[typing.List[str]]


# DescribeBlueGreenDeploymentsRequest

### BlueGreenDeploymentIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeBlueGreenDeploymentsRequestPaginate

### BlueGreenDeploymentIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeBlueGreenDeploymentsResponse

### BlueGreenDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.BlueGreenDeployment]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCertificatesMessage

### CertificateIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCertificatesMessagePaginate

### CertificateIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBClusterAutomatedBackupsMessage

### DbClusterResourceId
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterAutomatedBackupsMessagePaginate

### DbClusterResourceId
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBClusterBacktracksMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BacktrackIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterBacktracksMessagePaginate

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BacktrackIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBClusterEndpointsMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterEndpointIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBClusterParameterGroupsMessage

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBClusterParameterGroupsMessagePaginate

### DBClusterParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBClusterParametersMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBClusterSnapshotAttributesMessage

### DBClusterSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDBClusterSnapshotAttributesResult

### DBClusterSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterSnapshotAttributesResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBClusterSnapshotsMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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


# DescribeDBClusterSnapshotsMessagePaginate

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBClusterSnapshotsMessageWait

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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
- **Type**: <class 'NoneType'>


# DescribeDBClusterSnapshotsMessageWaitExtra

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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
- **Type**: <class 'NoneType'>


# DescribeDBClustersMessage

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]


# DescribeDBClustersMessagePaginate

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### IncludeShared
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBClustersMessageWait

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeDBClustersMessageWaitExtra

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeDBEngineVersionsMessage

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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


# DescribeDBEngineVersionsMessagePaginate

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DBParameterGroupFamily
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### DefaultOnly
- **Type**: typing.Optional[bool]

### ListSupportedCharacterSets
- **Type**: typing.Optional[bool]

### ListSupportedTimezones
- **Type**: typing.Optional[bool]

### IncludeAll
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBInstanceAutomatedBackupsMessage

### DbiResourceId
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### DBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]


# DescribeDBInstanceAutomatedBackupsMessagePaginate

### DbiResourceId
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### DBInstanceAutomatedBackupsArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBInstancesMessage

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBInstancesMessagePaginate

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBInstancesMessageWait

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeDBLogFilesDetails

### LogFileName
- **Type**: typing.Optional[str]

### LastWritten
- **Type**: typing.Optional[int]

### Size
- **Type**: typing.Optional[int]


# DescribeDBLogFilesMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBLogFilesMessagePaginate

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBLogFilesResponse

### DescribeDBLogFiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DescribeDBLogFilesDetails]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBParameterGroupsMessage

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBParameterGroupsMessagePaginate

### DBParameterGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBParametersMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBProxiesRequest

### DBProxyName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBProxiesRequestPaginate

### DBProxyName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBProxiesResponse

### DBProxies
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBProxy]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBProxyEndpointsRequest

### DBProxyName
- **Type**: typing.Optional[str]

### DBProxyEndpointName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBProxyEndpointsRequestPaginate

### DBProxyName
- **Type**: typing.Optional[str]

### DBProxyEndpointName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBProxyEndpointsResponse

### DBProxyEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBProxyEndpoint]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBProxyTargetGroupsRequest

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBProxyTargetGroupsRequestPaginate

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBProxyTargetGroupsResponse

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBProxyTargetGroup]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBProxyTargetsRequest

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBProxyTargetsRequestPaginate

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBProxyTargetsResponse

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBProxyTarget]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBRecommendationsMessage

### LastUpdatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastUpdatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Locale
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBRecommendationsMessagePaginate

### LastUpdatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastUpdatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Locale
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBSecurityGroupsMessage

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBSecurityGroupsMessagePaginate

### DBSecurityGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBShardGroupsMessage

### DBShardGroupIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeDBShardGroupsResponse

### DBShardGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBShardGroup]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBSnapshotAttributesMessage

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDBSnapshotAttributesResult

### DBSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSnapshotAttributesResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDBSnapshotTenantDatabasesMessage

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### DbiResourceId
- **Type**: typing.Optional[str]


# DescribeDBSnapshotTenantDatabasesMessagePaginate

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### DbiResourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBSnapshotsMessage

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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


# DescribeDBSnapshotsMessagePaginate

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### IncludeShared
- **Type**: typing.Optional[bool]

### IncludePublic
- **Type**: typing.Optional[bool]

### DbiResourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeDBSnapshotsMessageWait

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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
- **Type**: <class 'NoneType'>


# DescribeDBSnapshotsMessageWaitExtra

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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
- **Type**: <class 'NoneType'>


# DescribeDBSnapshotsMessageWaitExtraExtra

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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
- **Type**: <class 'NoneType'>


# DescribeDBSubnetGroupsMessage

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDBSubnetGroupsMessagePaginate

### DBSubnetGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeEngineDefaultClusterParametersMessage

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultClusterParametersMessagePaginate

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeEngineDefaultClusterParametersResult

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.EngineDefaults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEngineDefaultParametersMessage

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineDefaultParametersMessagePaginate

### DBParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeEngineDefaultParametersResult

### EngineDefaults
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.EngineDefaults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventCategoriesMessage

### SourceType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]


# DescribeEventSubscriptionsMessage

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventSubscriptionsMessagePaginate

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeEventsMessage

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
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventsMessagePaginate

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
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeExportTasksMessage

### ExportTaskIdentifier
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'SNAPSHOT']]


# DescribeExportTasksMessagePaginate

### ExportTaskIdentifier
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### SourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'SNAPSHOT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeGlobalClustersMessage

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeGlobalClustersMessagePaginate

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeIntegrationsMessage

### IntegrationIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeIntegrationsMessagePaginate

### IntegrationIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeIntegrationsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Integrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Integration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOptionGroupOptionsMessage

### EngineName
- **Type**: <class 'str'>
- **Required**: Yes

### MajorEngineVersion
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeOptionGroupOptionsMessagePaginate

### EngineName
- **Type**: <class 'str'>
- **Required**: Yes

### MajorEngineVersion
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeOptionGroupsMessage

### OptionGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### EngineName
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]


# DescribeOptionGroupsMessagePaginate

### OptionGroupName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### EngineName
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


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

### AvailabilityZoneGroup
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

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

### AvailabilityZoneGroup
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribePendingMaintenanceActionsMessage

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribePendingMaintenanceActionsMessagePaginate

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeReservedDBInstancesMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedDBInstancesMessagePaginate

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeReservedDBInstancesOfferingsMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedDBInstancesOfferingsMessagePaginate

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeSourceRegionsMessage

### RegionName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]


# DescribeSourceRegionsMessagePaginate

### RegionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeTenantDatabasesMessage

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeTenantDatabasesMessagePaginate

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# DescribeTenantDatabasesMessageWait

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTenantDatabasesMessageWaitExtra

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeValidDBInstanceModificationsMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeValidDBInstanceModificationsResult

### ValidDBInstanceModificationsMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ValidDBInstanceModificationsMessage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DisableHttpEndpointRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisableHttpEndpointResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpEndpointEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DocLink

### Text
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# DomainMembership

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


# DoubleRange

### From
- **Type**: typing.Optional[float]

### To
- **Type**: typing.Optional[float]


# DownloadDBLogFilePortionDetails

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# DownloadDBLogFilePortionMessage

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


# DownloadDBLogFilePortionMessagePaginate

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### LogFileName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PaginatorConfig]


# EC2SecurityGroup

### Status
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupId
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# EnableHttpEndpointRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# EnableHttpEndpointResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpEndpointEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ParameterOutput]]


# Event

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


# EventCategoriesMap

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]


# EventCategoriesMessage

### EventCategoriesMapList
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.EventCategoriesMap]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.EventSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# EventsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ExportTask

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


# ExportTaskResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ExportTasksMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ExportTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ExportTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# FailoverDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDBInstanceIdentifier
- **Type**: typing.Optional[str]


# FailoverDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# FailoverState

### Status
- **Type**: typing.Optional[typing.Literal['cancelling', 'failing-over', 'pending']]

### FromDbClusterArn
- **Type**: typing.Optional[str]

### ToDbClusterArn
- **Type**: typing.Optional[str]

### IsDataLossAllowed
- **Type**: typing.Optional[bool]


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

### EngineLifecycleSupport
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### DeletionProtection
- **Type**: typing.Optional[bool]

### GlobalClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.GlobalClusterMember]]

### Endpoint
- **Type**: typing.Optional[str]

### FailoverState
- **Type**: <class 'NoneType'>

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# GlobalClusterMember

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


# GlobalClustersMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### GlobalClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.GlobalCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# IPRange

### Status
- **Type**: typing.Optional[str]

### CIDRIP
- **Type**: typing.Optional[str]


# Integration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.IntegrationError]]

### DataFilter
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# IntegrationError

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: typing.Optional[str]


# IntegrationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.IntegrationError]
- **Required**: Yes

### DataFilter
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# IssueDetails

### PerformanceIssueDetails
- **Type**: <class 'NoneType'>


# LimitlessDatabase

### Status
- **Type**: typing.Optional[typing.Literal['active', 'disabled', 'disabling', 'enabled', 'enabling', 'error', 'modifying-max-capacity', 'not-in-use']]

### MinRequiredACU
- **Type**: typing.Optional[float]


# ListTagsForResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Filter]]


# MasterUserSecret

### SecretArn
- **Type**: typing.Optional[str]

### SecretStatus
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]


# Metric

### Name
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.MetricReference]]

### StatisticsDetails
- **Type**: typing.Optional[str]

### MetricQuery
- **Type**: <class 'NoneType'>


# MetricQuery

### PerformanceInsightsMetricQuery
- **Type**: <class 'NoneType'>


# MetricReference

### Name
- **Type**: typing.Optional[str]

### ReferenceDetails
- **Type**: <class 'NoneType'>


# MinimumEngineVersionPerAllowedValue

### AllowedValue
- **Type**: typing.Optional[str]

### MinimumEngineVersion
- **Type**: typing.Optional[str]


# ModifyActivityStreamRequest

### ResourceArn
- **Type**: typing.Optional[str]

### AuditPolicyState
- **Type**: typing.Optional[typing.Literal['locked', 'unlocked']]


# ModifyActivityStreamResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyCertificatesMessage

### CertificateIdentifier
- **Type**: typing.Optional[str]

### RemoveCustomerOverride
- **Type**: typing.Optional[bool]


# ModifyCertificatesResult

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.Certificate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyCurrentDBClusterCapacityMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Capacity
- **Type**: typing.Optional[int]

### SecondsBeforeTimeout
- **Type**: typing.Optional[int]

### TimeoutAction
- **Type**: typing.Optional[str]


# ModifyCustomDBEngineVersionMessage

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

### BacktrackWindow
- **Type**: typing.Optional[int]

### CloudwatchLogsExportConfiguration
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

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


# ModifyDBClusterParameterGroupMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.rds.rds_classes.Parameter, aws_resource_validator.pydantic_models.rds.rds_classes.ParameterOutput]]
- **Required**: Yes


# ModifyDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBClusterSnapshotAttributesResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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

### DomainFqdn
- **Type**: typing.Optional[str]

### DomainOu
- **Type**: typing.Optional[str]

### DomainAuthSecretArn
- **Type**: typing.Optional[str]

### DomainDnsIps
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: <class 'NoneType'>

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ProcessorFeature]]

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


# ModifyDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBParameterGroupMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.rds.rds_classes.Parameter, aws_resource_validator.pydantic_models.rds.rds_classes.ParameterOutput]]
- **Required**: Yes


# ModifyDBProxyEndpointRequest

### DBProxyEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### NewDBProxyEndpointName
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# ModifyDBProxyEndpointResponse

### DBProxyEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBProxyEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBProxyRequest

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### NewDBProxyName
- **Type**: typing.Optional[str]

### Auth
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.UserAuthConfig]]

### RequireTLS
- **Type**: typing.Optional[bool]

### IdleClientTimeout
- **Type**: typing.Optional[int]

### DebugLogging
- **Type**: typing.Optional[bool]

### RoleArn
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# ModifyDBProxyResponse

### DBProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBProxy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBProxyTargetGroupRequest

### TargetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.ConnectionPoolConfiguration]

### NewName
- **Type**: typing.Optional[str]


# ModifyDBProxyTargetGroupResponse

### DBProxyTargetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBProxyTargetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBRecommendationMessage

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### Locale
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### RecommendedActionUpdates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.RecommendedActionUpdate]]


# ModifyDBShardGroupMessage

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxACU
- **Type**: typing.Optional[float]

### MinACU
- **Type**: typing.Optional[float]

### ComputeRedundancy
- **Type**: typing.Optional[int]


# ModifyDBSnapshotAttributeMessage

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ValuesToAdd
- **Type**: typing.Optional[typing.List[str]]

### ValuesToRemove
- **Type**: typing.Optional[typing.List[str]]


# ModifyDBSnapshotAttributeResult

### DBSnapshotAttributesResult
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSnapshotAttributesResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDBSnapshotMessage

### DBSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: typing.Optional[str]

### OptionGroupName
- **Type**: typing.Optional[str]


# ModifyDBSnapshotResult

### DBSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyGlobalClusterMessage

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


# ModifyGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyIntegrationMessage

### IntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: typing.Optional[str]

### DataFilter
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ModifyOptionGroupMessage

### OptionGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### OptionsToInclude
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.OptionConfiguration]]

### OptionsToRemove
- **Type**: typing.Optional[typing.List[str]]

### ApplyImmediately
- **Type**: typing.Optional[bool]


# ModifyOptionGroupResult

### OptionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.OptionGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyTenantDatabaseMessage

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


# ModifyTenantDatabaseResult

### TenantDatabase
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.TenantDatabase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# Option

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.OptionSetting]]

### DBSecurityGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBSecurityGroupMembership]]

### VpcSecurityGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.VpcSecurityGroupMembership]]


# OptionConfiguration

### OptionName
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: typing.Optional[int]

### OptionVersion
- **Type**: typing.Optional[str]

### DBSecurityGroupMemberships
- **Type**: typing.Optional[typing.List[str]]

### VpcSecurityGroupMemberships
- **Type**: typing.Optional[typing.List[str]]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.OptionSetting]]


# OptionGroup

### OptionGroupName
- **Type**: typing.Optional[str]

### OptionGroupDescription
- **Type**: typing.Optional[str]

### EngineName
- **Type**: typing.Optional[str]

### MajorEngineVersion
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Option]]

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


# OptionGroupMembership

### OptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# OptionGroupOption

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.OptionGroupOptionSetting]]

### OptionGroupOptionVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.OptionVersion]]

### CopyableCrossAccount
- **Type**: typing.Optional[bool]


# OptionGroupOptionSetting

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
- **Type**: typing.Optional[typing.List[NoneType]]


# OptionGroupOptionsMessage

### OptionGroupOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.OptionGroupOption]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# OptionGroups

### OptionGroupsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.OptionGroup]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# OptionSetting

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


# OptionVersion

### Version
- **Type**: typing.Optional[str]

### IsDefault
- **Type**: typing.Optional[bool]


# OrderableDBInstanceOption

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.AvailabilityZone]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.AvailableProcessorFeature]]

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


# OrderableDBInstanceOptionsMessage

### OrderableDBInstanceOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.OrderableDBInstanceOption]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# Outpost

### Arn
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


# ParameterOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ResourcePendingMaintenanceActions]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ProcessorFeature]]

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


# PerformanceInsightsMetricDimensionGroup

### Dimensions
- **Type**: typing.Optional[typing.List[str]]

### Group
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# PerformanceInsightsMetricQuery

### GroupBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.PerformanceInsightsMetricDimensionGroup]

### Metric
- **Type**: typing.Optional[str]


# PerformanceIssueDetails

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Metric]]

### Analysis
- **Type**: typing.Optional[str]


# ProcessorFeature

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# PromoteReadReplicaDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PromoteReadReplicaDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# PromoteReadReplicaMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### PreferredBackupWindow
- **Type**: typing.Optional[str]


# PromoteReadReplicaResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# PurchaseReservedDBInstancesOfferingMessage

### ReservedDBInstancesOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedDBInstanceId
- **Type**: typing.Optional[str]

### DBInstanceCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# PurchaseReservedDBInstancesOfferingResult

### ReservedDBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ReservedDBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# Range

### From
- **Type**: typing.Optional[int]

### To
- **Type**: typing.Optional[int]

### Step
- **Type**: typing.Optional[int]


# RdsCustomClusterConfiguration

### InterconnectSubnetId
- **Type**: typing.Optional[str]

### TransitGatewayMulticastDomainId
- **Type**: typing.Optional[str]

### ReplicaMode
- **Type**: typing.Optional[typing.Literal['mounted', 'open-read-only']]


# RebootDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RebootDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# RebootDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ForceFailover
- **Type**: typing.Optional[bool]


# RebootDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# RebootDBShardGroupMessage

### DBShardGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RecommendedAction

### ActionId
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.RecommendedActionParameter]]

### ApplyModes
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[str]

### IssueDetails
- **Type**: <class 'NoneType'>

### ContextAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ContextAttribute]]


# RecommendedActionParameter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# RecommendedActionUpdate

### ActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes


# RecurringCharge

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# ReferenceDetails

### ScalarReferenceDetails
- **Type**: <class 'NoneType'>


# RegisterDBProxyTargetsRequest

### DBProxyName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetGroupName
- **Type**: typing.Optional[str]

### DBInstanceIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DBClusterIdentifiers
- **Type**: typing.Optional[typing.List[str]]


# RegisterDBProxyTargetsResponse

### DBProxyTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DBProxyTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveFromGlobalClusterMessage

### GlobalClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterIdentifier
- **Type**: typing.Optional[str]


# RemoveFromGlobalClusterResult

### GlobalCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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


# RemoveRoleFromDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsFromResourceMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# ReservedDBInstance

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.RecurringCharge]]

### ReservedDBInstanceArn
- **Type**: typing.Optional[str]

### LeaseId
- **Type**: typing.Optional[str]


# ReservedDBInstanceMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedDBInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ReservedDBInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ReservedDBInstancesOffering

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.RecurringCharge]]


# ReservedDBInstancesOfferingMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedDBInstancesOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ReservedDBInstancesOffering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ResetDBClusterParameterGroupMessage

### DBClusterParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.rds.rds_classes.Parameter, aws_resource_validator.pydantic_models.rds.rds_classes.ParameterOutput]]]


# ResetDBParameterGroupMessage

### DBParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.rds.rds_classes.Parameter, aws_resource_validator.pydantic_models.rds.rds_classes.ParameterOutput]]]


# ResourcePendingMaintenanceActions

### ResourceIdentifier
- **Type**: typing.Optional[str]

### PendingMaintenanceActionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.PendingMaintenanceAction]]


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


# RestoreDBClusterFromS3Message

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
- **Type**: typing.Optional[typing.List[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### CharacterSetName
- **Type**: typing.Optional[str]

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

### MasterUserPassword
- **Type**: typing.Optional[str]

### OptionGroupName
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

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
- **Type**: typing.Optional[typing.List[str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### Domain
- **Type**: typing.Optional[str]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### ServerlessV2ScalingConfiguration
- **Type**: <class 'NoneType'>

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


# RestoreDBClusterFromS3Result

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### BacktrackWindow
- **Type**: typing.Optional[int]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### EngineMode
- **Type**: typing.Optional[str]

### ScalingConfiguration
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

### NetworkType
- **Type**: typing.Optional[str]

### RdsCustomClusterConfiguration
- **Type**: <class 'NoneType'>

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


# RestoreDBClusterFromSnapshotResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreDBClusterToPointInTimeMessage

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
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### BacktrackWindow
- **Type**: typing.Optional[int]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

### NetworkType
- **Type**: typing.Optional[str]

### SourceDbClusterResourceId
- **Type**: typing.Optional[str]

### RdsCustomClusterConfiguration
- **Type**: <class 'NoneType'>

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


# RestoreDBClusterToPointInTimeResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreDBInstanceFromDBSnapshotMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### TdeCredentialPassword
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Domain
- **Type**: typing.Optional[str]

### DomainFqdn
- **Type**: typing.Optional[str]

### DomainOu
- **Type**: typing.Optional[str]

### DomainAuthSecretArn
- **Type**: typing.Optional[str]

### DomainDnsIps
- **Type**: typing.Optional[typing.List[str]]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### DomainIAMRoleName
- **Type**: typing.Optional[str]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ProcessorFeature]]

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


# RestoreDBInstanceFromDBSnapshotResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreDBInstanceFromS3Message

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

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

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
- **Type**: typing.Optional[typing.List[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ProcessorFeature]]

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


# RestoreDBInstanceFromS3Result

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreDBInstanceToPointInTimeMessage

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### TdeCredentialPassword
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[typing.List[str]]

### EnableIAMDatabaseAuthentication
- **Type**: typing.Optional[bool]

### EnableCloudwatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ProcessorFeature]]

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


# RestoreDBInstanceToPointInTimeResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreWindow

### EarliestTime
- **Type**: typing.Optional[datetime.datetime]

### LatestTime
- **Type**: typing.Optional[datetime.datetime]


# RevokeDBSecurityGroupIngressMessage

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


# RevokeDBSecurityGroupIngressResult

### DBSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# ScalarReferenceDetails

### Value
- **Type**: typing.Optional[float]


# ScalingConfiguration

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


# ScalingConfigurationInfo

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


# ServerlessV2FeaturesSupport

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]


# ServerlessV2ScalingConfiguration

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]

### SecondsUntilAutoPause
- **Type**: typing.Optional[int]


# ServerlessV2ScalingConfigurationInfo

### MinCapacity
- **Type**: typing.Optional[float]

### MaxCapacity
- **Type**: typing.Optional[float]

### SecondsUntilAutoPause
- **Type**: typing.Optional[int]


# SourceRegion

### RegionName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SupportsDBInstanceAutomatedBackupsReplication
- **Type**: typing.Optional[bool]


# SourceRegionMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### SourceRegions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.SourceRegion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# StartActivityStreamRequest

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


# StartActivityStreamResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# StartDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# StartDBInstanceAutomatedBackupsReplicationMessage

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


# StartDBInstanceAutomatedBackupsReplicationResult

### DBInstanceAutomatedBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstanceAutomatedBackup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# StartDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# StartExportTaskMessage

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
- **Type**: typing.Optional[typing.List[str]]


# StopActivityStreamRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyImmediately
- **Type**: typing.Optional[bool]


# StopActivityStreamResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# StopDBClusterMessage

### DBClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopDBClusterResult

### DBCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# StopDBInstanceAutomatedBackupsReplicationMessage

### SourceDBInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopDBInstanceAutomatedBackupsReplicationResult

### DBInstanceAutomatedBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstanceAutomatedBackup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# StopDBInstanceMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DBSnapshotIdentifier
- **Type**: typing.Optional[str]


# StopDBInstanceResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# Subnet

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.AvailabilityZone]

### SubnetOutpost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.Outpost]

### SubnetStatus
- **Type**: typing.Optional[str]


# SwitchoverBlueGreenDeploymentRequest

### BlueGreenDeploymentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SwitchoverTimeout
- **Type**: typing.Optional[int]


# SwitchoverBlueGreenDeploymentResponse

### BlueGreenDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.BlueGreenDeployment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# SwitchoverDetail

### SourceMember
- **Type**: typing.Optional[str]

### TargetMember
- **Type**: typing.Optional[str]

### Status
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.GlobalCluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# SwitchoverReadReplicaMessage

### DBInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# SwitchoverReadReplicaResult

### DBInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.DBInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagListMessage

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
- **Required**: Yes


# TargetHealth

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'REGISTERING', 'UNAVAILABLE']]

### Reason
- **Type**: typing.Optional[typing.Literal['AUTH_FAILURE', 'CONNECTION_FAILED', 'INVALID_REPLICATION_STATE', 'PENDING_PROXY_CAPACITY', 'UNREACHABLE']]

### Description
- **Type**: typing.Optional[str]


# TenantDatabase

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds.rds_classes.TenantDatabasePendingModifiedValues]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Tag]]


# TenantDatabasePendingModifiedValues

### MasterUserPassword
- **Type**: typing.Optional[str]

### TenantDBName
- **Type**: typing.Optional[str]


# TenantDatabasesMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### TenantDatabases
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.TenantDatabase]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds.rds_classes.ResponseMetadata'>
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


# UserAuthConfig

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


# UserAuthConfigInfo

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


# ValidDBInstanceModificationsMessage

### Storage
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.ValidStorageOptions]]

### ValidProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.AvailableProcessorFeature]]

### SupportsDedicatedLogVolume
- **Type**: typing.Optional[bool]


# ValidStorageOptions

### StorageType
- **Type**: typing.Optional[str]

### StorageSize
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Range]]

### ProvisionedIops
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Range]]

### IopsToStorageRatio
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DoubleRange]]

### SupportsStorageAutoscaling
- **Type**: typing.Optional[bool]

### ProvisionedStorageThroughput
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.Range]]

### StorageThroughputToIopsRatio
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds.rds_classes.DoubleRange]]


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



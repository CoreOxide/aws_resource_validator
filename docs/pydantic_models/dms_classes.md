# Dms Classes

# AccountQuota

### AccountQuotaName
- **Type**: typing.Optional[str]

### Used
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# AddTagsToResourceMessage

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]
- **Required**: Yes


# ApplyPendingMaintenanceActionMessage

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyAction
- **Type**: <class 'str'>
- **Required**: Yes

### OptInType
- **Type**: <class 'str'>
- **Required**: Yes


# ApplyPendingMaintenanceActionResponse

### ResourcePendingMaintenanceActions
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResourcePendingMaintenanceActions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# AvailabilityZone

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchStartRecommendationsErrorEntry

### DatabaseId
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]


# BatchStartRecommendationsRequest

### Data
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.StartRecommendationsRequestEntry]]


# BatchStartRecommendationsResponse

### ErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.BatchStartRecommendationsErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelReplicationTaskAssessmentRunMessage

### ReplicationTaskAssessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# CancelReplicationTaskAssessmentRunResponse

### ReplicationTaskAssessmentRun
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# Certificate

### CertificateIdentifier
- **Type**: typing.Optional[str]

### CertificateCreationDate
- **Type**: typing.Optional[datetime.datetime]

### CertificatePem
- **Type**: typing.Optional[str]

### CertificateWallet
- **Type**: typing.Optional[bytes]

### CertificateArn
- **Type**: typing.Optional[str]

### CertificateOwner
- **Type**: typing.Optional[str]

### ValidFromDate
- **Type**: typing.Optional[datetime.datetime]

### ValidToDate
- **Type**: typing.Optional[datetime.datetime]

### SigningAlgorithm
- **Type**: typing.Optional[str]

### KeyLength
- **Type**: typing.Optional[int]


# CollectorHealthCheck

### CollectorStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'UNREGISTERED']]

### LocalCollectorS3Access
- **Type**: typing.Optional[bool]

### WebCollectorS3Access
- **Type**: typing.Optional[bool]

### WebCollectorGrantedRoleBasedAccess
- **Type**: typing.Optional[bool]


# CollectorResponse

### CollectorReferencedId
- **Type**: typing.Optional[str]

### CollectorName
- **Type**: typing.Optional[str]

### CollectorVersion
- **Type**: typing.Optional[str]

### VersionStatus
- **Type**: typing.Optional[typing.Literal['OUTDATED', 'UNSUPPORTED', 'UP_TO_DATE']]

### Description
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### CollectorHealthCheck
- **Type**: <class 'NoneType'>

### LastDataReceived
- **Type**: typing.Optional[str]

### RegisteredDate
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### ModifiedDate
- **Type**: typing.Optional[str]

### InventoryData
- **Type**: <class 'NoneType'>


# CollectorShortInfoResponse

### CollectorReferencedId
- **Type**: typing.Optional[str]

### CollectorName
- **Type**: typing.Optional[str]


# ComputeConfig

### AvailabilityZone
- **Type**: typing.Optional[str]

### DnsNameServers
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### MaxCapacityUnits
- **Type**: typing.Optional[int]

### MinCapacityUnits
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReplicationSubnetGroupId
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ComputeConfigOutput

### AvailabilityZone
- **Type**: typing.Optional[str]

### DnsNameServers
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### MaxCapacityUnits
- **Type**: typing.Optional[int]

### MinCapacityUnits
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReplicationSubnetGroupId
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# ComputeConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Connection

### ReplicationInstanceArn
- **Type**: typing.Optional[str]

### EndpointArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### LastFailureMessage
- **Type**: typing.Optional[str]

### EndpointIdentifier
- **Type**: typing.Optional[str]

### ReplicationInstanceIdentifier
- **Type**: typing.Optional[str]


# CreateDataMigrationMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DataMigrationType
- **Type**: typing.Literal['cdc', 'full-load', 'full-load-and-cdc']
- **Required**: Yes

### ServiceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataMigrationName
- **Type**: typing.Optional[str]

### EnableCloudwatchLogs
- **Type**: typing.Optional[bool]

### SourceDataSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.SourceDataSettingUnion]]

### TargetDataSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TargetDataSetting]]

### NumberOfJobs
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]

### SelectionRules
- **Type**: typing.Optional[str]


# CreateDataMigrationResponse

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataProviderMessage

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataProviderSettings'>
- **Required**: Yes

### DataProviderName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]


# CreateDataProviderResponse

### DataProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataProvider'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEndpointMessage

### EndpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: typing.Literal['source', 'target']
- **Required**: Yes

### EngineName
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### ExtraConnectionAttributes
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]

### CertificateArn
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### ExternalTableDefinition
- **Type**: typing.Optional[str]

### DynamoDbSettings
- **Type**: <class 'NoneType'>

### S3Settings
- **Type**: <class 'NoneType'>

### DmsTransferSettings
- **Type**: <class 'NoneType'>

### MongoDbSettings
- **Type**: <class 'NoneType'>

### KinesisSettings
- **Type**: <class 'NoneType'>

### KafkaSettings
- **Type**: <class 'NoneType'>

### ElasticsearchSettings
- **Type**: <class 'NoneType'>

### NeptuneSettings
- **Type**: <class 'NoneType'>

### RedshiftSettings
- **Type**: <class 'NoneType'>

### PostgreSQLSettings
- **Type**: <class 'NoneType'>

### MySQLSettings
- **Type**: <class 'NoneType'>

### OracleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.OracleSettingsUnion]

### SybaseSettings
- **Type**: <class 'NoneType'>

### MicrosoftSQLServerSettings
- **Type**: <class 'NoneType'>

### IBMDb2Settings
- **Type**: <class 'NoneType'>

### ResourceIdentifier
- **Type**: typing.Optional[str]

### DocDbSettings
- **Type**: <class 'NoneType'>

### RedisSettings
- **Type**: <class 'NoneType'>

### GcpMySQLSettings
- **Type**: <class 'NoneType'>

### TimestreamSettings
- **Type**: <class 'NoneType'>


# CreateEndpointResponse

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.Endpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]


# CreateEventSubscriptionResponse

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFleetAdvisorCollectorRequest

### CollectorName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateFleetAdvisorCollectorResponse

### CollectorReferencedId
- **Type**: <class 'str'>
- **Required**: Yes

### CollectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstanceProfileMessage

### AvailabilityZone
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]

### NetworkType
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SubnetGroupIdentifier
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateInstanceProfileResponse

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMigrationProjectMessage

### SourceDataProviderDescriptors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorDefinition]
- **Required**: Yes

### TargetDataProviderDescriptors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorDefinition]
- **Required**: Yes

### InstanceProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationProjectName
- **Type**: typing.Optional[str]

### TransformationRules
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]

### SchemaConversionApplicationAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SCApplicationAttributes]


# CreateMigrationProjectResponse

### MigrationProject
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.MigrationProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReplicationConfigMessage

### ReplicationConfigIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ComputeConfigUnion'>
- **Required**: Yes

### ReplicationType
- **Type**: typing.Literal['cdc', 'full-load', 'full-load-and-cdc']
- **Required**: Yes

### TableMappings
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationSettings
- **Type**: typing.Optional[str]

### SupplementalSettings
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]


# CreateReplicationConfigResponse

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReplicationInstanceMessage

### ReplicationInstanceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstanceClass
- **Type**: <class 'str'>
- **Required**: Yes

### AllocatedStorage
- **Type**: typing.Optional[int]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ReplicationSubnetGroupIdentifier
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### DnsNameServers
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[str]

### KerberosAuthenticationSettings
- **Type**: <class 'NoneType'>


# CreateReplicationInstanceResponse

### ReplicationInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReplicationSubnetGroupMessage

### ReplicationSubnetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationSubnetGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]


# CreateReplicationSubnetGroupResponse

### ReplicationSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReplicationTaskMessage

### ReplicationTaskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationType
- **Type**: typing.Literal['cdc', 'full-load', 'full-load-and-cdc']
- **Required**: Yes

### TableMappings
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTaskSettings
- **Type**: typing.Optional[str]

### CdcStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]

### TaskData
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]


# CreateReplicationTaskResponse

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DataMigration

### DataMigrationName
- **Type**: typing.Optional[str]

### DataMigrationArn
- **Type**: typing.Optional[str]

### DataMigrationCreateTime
- **Type**: typing.Optional[datetime.datetime]

### DataMigrationStartTime
- **Type**: typing.Optional[datetime.datetime]

### DataMigrationEndTime
- **Type**: typing.Optional[datetime.datetime]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### MigrationProjectArn
- **Type**: typing.Optional[str]

### DataMigrationType
- **Type**: typing.Optional[typing.Literal['cdc', 'full-load', 'full-load-and-cdc']]

### DataMigrationSettings
- **Type**: <class 'NoneType'>

### SourceDataSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.SourceDataSettingOutput]]

### TargetDataSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.TargetDataSetting]]

### DataMigrationStatistics
- **Type**: <class 'NoneType'>

### DataMigrationStatus
- **Type**: typing.Optional[str]

### PublicIpAddresses
- **Type**: typing.Optional[typing.List[str]]

### DataMigrationCidrBlocks
- **Type**: typing.Optional[typing.List[str]]

### LastFailureMessage
- **Type**: typing.Optional[str]

### StopReason
- **Type**: typing.Optional[str]


# DataMigrationSettings

### NumberOfJobs
- **Type**: typing.Optional[int]

### CloudwatchLogsEnabled
- **Type**: typing.Optional[bool]

### SelectionRules
- **Type**: typing.Optional[str]


# DataMigrationStatistics

### TablesLoaded
- **Type**: typing.Optional[int]

### ElapsedTimeMillis
- **Type**: typing.Optional[int]

### TablesLoading
- **Type**: typing.Optional[int]

### FullLoadPercentage
- **Type**: typing.Optional[int]

### CDCLatency
- **Type**: typing.Optional[int]

### TablesQueued
- **Type**: typing.Optional[int]

### TablesErrored
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### StopTime
- **Type**: typing.Optional[datetime.datetime]


# DataProvider

### DataProviderName
- **Type**: typing.Optional[str]

### DataProviderArn
- **Type**: typing.Optional[str]

### DataProviderCreationTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DataProviderSettings]


# DataProviderDescriptor

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### DataProviderName
- **Type**: typing.Optional[str]

### DataProviderArn
- **Type**: typing.Optional[str]


# DataProviderDescriptorDefinition

### DataProviderIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]


# DataProviderSettings

### RedshiftSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RedshiftDataProviderSettings]

### PostgreSqlSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PostgreSqlDataProviderSettings]

### MySqlSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MySqlDataProviderSettings]

### OracleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.OracleDataProviderSettings]

### MicrosoftSqlServerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MicrosoftSqlServerDataProviderSettings]

### DocDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DocDbDataProviderSettings]

### MariaDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MariaDbDataProviderSettings]

### IbmDb2LuwSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.IbmDb2LuwDataProviderSettings]

### IbmDb2zOsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.IbmDb2zOsDataProviderSettings]

### MongoDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MongoDbDataProviderSettings]


# DatabaseInstanceSoftwareDetailsResponse

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EngineEdition
- **Type**: typing.Optional[str]

### ServicePack
- **Type**: typing.Optional[str]

### SupportLevel
- **Type**: typing.Optional[str]

### OsArchitecture
- **Type**: typing.Optional[int]

### Tooltip
- **Type**: typing.Optional[str]


# DatabaseResponse

### DatabaseId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### NumberOfSchemas
- **Type**: typing.Optional[int]

### Server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ServerShortInfoResponse]

### SoftwareDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DatabaseInstanceSoftwareDetailsResponse]

### Collectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.CollectorShortInfoResponse]]


# DatabaseShortInfoResponse

### DatabaseId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### DatabaseIpAddress
- **Type**: typing.Optional[str]

### DatabaseEngine
- **Type**: typing.Optional[str]


# DefaultErrorDetails

### Message
- **Type**: typing.Optional[str]


# DeleteCertificateMessage

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateResponse

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.Certificate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCollectorRequest

### CollectorReferencedId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionMessage

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.Connection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataMigrationMessage

### DataMigrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataMigrationResponse

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataProviderMessage

### DataProviderIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataProviderResponse

### DataProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataProvider'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEndpointMessage

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointResponse

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.Endpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEventSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionResponse

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFleetAdvisorDatabasesRequest

### DatabaseIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteFleetAdvisorDatabasesResponse

### DatabaseIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInstanceProfileMessage

### InstanceProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceProfileResponse

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMigrationProjectMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMigrationProjectResponse

### MigrationProject
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.MigrationProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteReplicationConfigMessage

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationConfigResponse

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteReplicationInstanceMessage

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationInstanceResponse

### ReplicationInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteReplicationSubnetGroupMessage

### ReplicationSubnetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationTaskAssessmentRunMessage

### ReplicationTaskAssessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationTaskAssessmentRunResponse

### ReplicationTaskAssessmentRun
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteReplicationTaskMessage

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationTaskResponse

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccountAttributesResponse

### AccountQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.AccountQuota]
- **Required**: Yes

### UniqueAccountIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicableIndividualAssessmentsMessage

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### ReplicationInstanceArn
- **Type**: typing.Optional[str]

### ReplicationConfigArn
- **Type**: typing.Optional[str]

### SourceEngineName
- **Type**: typing.Optional[str]

### TargetEngineName
- **Type**: typing.Optional[str]

### MigrationType
- **Type**: typing.Optional[typing.Literal['cdc', 'full-load', 'full-load-and-cdc']]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeApplicableIndividualAssessmentsResponse

### IndividualAssessmentNames
- **Type**: typing.List[str]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCertificatesMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCertificatesMessagePaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeCertificatesResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.Certificate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectionsMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeConnectionsMessagePaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeConnectionsMessageWait

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeConnectionsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.Connection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConversionConfigurationMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConversionConfigurationResponse

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ConversionConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataMigrationsMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WithoutStatistics
- **Type**: typing.Optional[bool]


# DescribeDataMigrationsMessagePaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WithoutStatistics
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeDataMigrationsResponse

### DataMigrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.DataMigration]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataProvidersMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDataProvidersResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DataProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.DataProvider]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointSettingsMessage

### EngineName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEndpointSettingsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EndpointSetting]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointTypesMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEndpointTypesMessagePaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeEndpointTypesResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedEndpointTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SupportedEndpointType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointsMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEndpointsMessagePaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeEndpointsMessageWait

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEndpointsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEngineVersionsMessage

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineVersionsResponse

### EngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EngineVersion]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventCategoriesMessage

### SourceType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]


# DescribeEventCategoriesResponse

### EventCategoryGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EventCategoryGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventSubscriptionsMessage

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventSubscriptionsMessagePaginate

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeEventSubscriptionsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### EventSubscriptionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EventSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventsMessage

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['replication-instance']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventsMessagePaginate

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['replication-instance']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeEventsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExtensionPackAssociationsMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeExtensionPackAssociationsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFleetAdvisorCollectorsRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorCollectorsResponse

### Collectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.CollectorResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorDatabasesRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorDatabasesResponse

### Databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.DatabaseResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorLsaAnalysisRequest

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorLsaAnalysisResponse

### Analysis
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.FleetAdvisorLsaAnalysisResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorSchemaObjectSummaryRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorSchemaObjectSummaryResponse

### FleetAdvisorSchemaObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.FleetAdvisorSchemaObjectResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorSchemasRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorSchemasResponse

### FleetAdvisorSchemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceProfilesMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeInstanceProfilesResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.InstanceProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMetadataModelAssessmentsMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelAssessmentsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMetadataModelConversionsMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelConversionsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMetadataModelExportsAsScriptMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelExportsAsScriptResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMetadataModelExportsToTargetMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelExportsToTargetResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMetadataModelImportsMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelImportsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMigrationProjectsMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeMigrationProjectsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationProjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.MigrationProject]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrderableReplicationInstancesMessage

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeOrderableReplicationInstancesMessagePaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeOrderableReplicationInstancesResponse

### OrderableReplicationInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.OrderableReplicationInstance]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePendingMaintenanceActionsMessage

### ReplicationInstanceArn
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribePendingMaintenanceActionsResponse

### PendingMaintenanceActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ResourcePendingMaintenanceActions]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRecommendationLimitationsRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRecommendationLimitationsResponse

### Limitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.Limitation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRecommendationsRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRecommendationsResponse

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.Recommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRefreshSchemasStatusMessage

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRefreshSchemasStatusResponse

### RefreshSchemasStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.RefreshSchemasStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationConfigsMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationConfigsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationInstanceTaskLogsMessage

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationInstanceTaskLogsResponse

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstanceTaskLogs
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationInstanceTaskLog]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationInstancesMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationInstancesMessagePaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeReplicationInstancesMessageWait

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeReplicationInstancesMessageWaitExtra

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeReplicationInstancesResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationSubnetGroupsMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationSubnetGroupsMessagePaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeReplicationSubnetGroupsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationSubnetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationTableStatisticsMessage

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]


# DescribeReplicationTableStatisticsResponse

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTableStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.TableStatistics]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationTaskAssessmentResultsMessage

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationTaskAssessmentResultsMessagePaginate

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeReplicationTaskAssessmentResultsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTaskAssessmentResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationTaskAssessmentRunsMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationTaskAssessmentRunsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTaskAssessmentRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationTaskIndividualAssessmentsMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationTaskIndividualAssessmentsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTaskIndividualAssessments
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskIndividualAssessment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationTasksMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]


# DescribeReplicationTasksMessagePaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### WithoutSettings
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeReplicationTasksMessageWait

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeReplicationTasksMessageWaitExtra

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeReplicationTasksMessageWaitExtraExtra

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeReplicationTasksMessageWaitExtraExtraExtra

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeReplicationTasksResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationsMessage

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Replications
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.Replication]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSchemasMessage

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeSchemasMessagePaginate

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeSchemasResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Schemas
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTableStatisticsMessage

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]


# DescribeTableStatisticsMessagePaginate

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfig]


# DescribeTableStatisticsResponse

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.TableStatistics]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# DmsTransferSettings

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### BucketName
- **Type**: typing.Optional[str]


# DocDbDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]


# DocDbSettings

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### NestingLevel
- **Type**: typing.Optional[typing.Literal['none', 'one']]

### ExtractDocId
- **Type**: typing.Optional[bool]

### DocsToInvestigate
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### UseUpdateLookUp
- **Type**: typing.Optional[bool]

### ReplicateShardCollections
- **Type**: typing.Optional[bool]


# DynamoDbSettings

### ServiceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ElasticsearchSettings

### ServiceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointUri
- **Type**: <class 'str'>
- **Required**: Yes

### FullLoadErrorPercentage
- **Type**: typing.Optional[int]

### ErrorRetryDuration
- **Type**: typing.Optional[int]

### UseNewMappingType
- **Type**: typing.Optional[bool]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### EndpointIdentifier
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[typing.Literal['source', 'target']]

### EngineName
- **Type**: typing.Optional[str]

### EngineDisplayName
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### ExtraConnectionAttributes
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### EndpointArn
- **Type**: typing.Optional[str]

### CertificateArn
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### ExternalTableDefinition
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]

### DynamoDbSettings
- **Type**: <class 'NoneType'>

### S3Settings
- **Type**: <class 'NoneType'>

### DmsTransferSettings
- **Type**: <class 'NoneType'>

### MongoDbSettings
- **Type**: <class 'NoneType'>

### KinesisSettings
- **Type**: <class 'NoneType'>

### KafkaSettings
- **Type**: <class 'NoneType'>

### ElasticsearchSettings
- **Type**: <class 'NoneType'>

### NeptuneSettings
- **Type**: <class 'NoneType'>

### RedshiftSettings
- **Type**: <class 'NoneType'>

### PostgreSQLSettings
- **Type**: <class 'NoneType'>

### MySQLSettings
- **Type**: <class 'NoneType'>

### OracleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.OracleSettingsOutput]

### SybaseSettings
- **Type**: <class 'NoneType'>

### MicrosoftSQLServerSettings
- **Type**: <class 'NoneType'>

### IBMDb2Settings
- **Type**: <class 'NoneType'>

### DocDbSettings
- **Type**: <class 'NoneType'>

### RedisSettings
- **Type**: <class 'NoneType'>

### GcpMySQLSettings
- **Type**: <class 'NoneType'>

### TimestreamSettings
- **Type**: <class 'NoneType'>


# EndpointSetting

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EngineVersion

### Version
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[str]

### ReleaseStatus
- **Type**: typing.Optional[typing.Literal['beta', 'prod']]

### LaunchDate
- **Type**: typing.Optional[datetime.datetime]

### AutoUpgradeDate
- **Type**: typing.Optional[datetime.datetime]

### DeprecationDate
- **Type**: typing.Optional[datetime.datetime]

### ForceUpgradeDate
- **Type**: typing.Optional[datetime.datetime]

### AvailableUpgrades
- **Type**: typing.Optional[typing.List[str]]


# ErrorDetails

### defaultErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DefaultErrorDetails]


# Event

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['replication-instance']]

### Message
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]

### Date
- **Type**: typing.Optional[datetime.datetime]


# EventCategoryGroup

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]


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


# ExportMetadataModelAssessmentMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionRules
- **Type**: <class 'str'>
- **Required**: Yes

### FileName
- **Type**: typing.Optional[str]

### AssessmentReportTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['csv', 'pdf']]]


# ExportMetadataModelAssessmentResponse

### PdfReport
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ExportMetadataModelAssessmentResultEntry'>
- **Required**: Yes

### CsvReport
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ExportMetadataModelAssessmentResultEntry'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ExportMetadataModelAssessmentResultEntry

### S3ObjectKey
- **Type**: typing.Optional[str]

### ObjectURL
- **Type**: typing.Optional[str]


# ExportSqlDetails

### S3ObjectKey
- **Type**: typing.Optional[str]

### ObjectURL
- **Type**: typing.Optional[str]


# Filter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# FleetAdvisorLsaAnalysisResponse

### LsaAnalysisId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# FleetAdvisorSchemaObjectResponse

### SchemaId
- **Type**: typing.Optional[str]

### ObjectType
- **Type**: typing.Optional[str]

### NumberOfObjects
- **Type**: typing.Optional[int]

### CodeLineCount
- **Type**: typing.Optional[int]

### CodeSize
- **Type**: typing.Optional[int]


# GcpMySQLSettings

### AfterConnectScript
- **Type**: typing.Optional[str]

### CleanSourceMetadataOnMismatch
- **Type**: typing.Optional[bool]

### DatabaseName
- **Type**: typing.Optional[str]

### EventsPollInterval
- **Type**: typing.Optional[int]

### TargetDbType
- **Type**: typing.Optional[typing.Literal['multiple-databases', 'specific-database']]

### MaxFileSize
- **Type**: typing.Optional[int]

### ParallelLoadThreads
- **Type**: typing.Optional[int]

### Password
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ServerName
- **Type**: typing.Optional[str]

### ServerTimezone
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]


# IBMDb2Settings

### DatabaseName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ServerName
- **Type**: typing.Optional[str]

### SetDataCaptureChanges
- **Type**: typing.Optional[bool]

### CurrentLsn
- **Type**: typing.Optional[str]

### MaxKBytesPerRead
- **Type**: typing.Optional[int]

### Username
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### LoadTimeout
- **Type**: typing.Optional[int]

### WriteBufferSize
- **Type**: typing.Optional[int]

### MaxFileSize
- **Type**: typing.Optional[int]

### KeepCsvFiles
- **Type**: typing.Optional[bool]


# IbmDb2LuwDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]


# IbmDb2zOsDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]


# ImportCertificateMessage

### CertificateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CertificatePem
- **Type**: typing.Optional[str]

### CertificateWallet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Blob]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]


# ImportCertificateResponse

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.Certificate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# InstanceProfile

### InstanceProfileArn
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### NetworkType
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### InstanceProfileCreationTime
- **Type**: typing.Optional[datetime.datetime]

### SubnetGroupIdentifier
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# InventoryData

### NumberOfDatabases
- **Type**: typing.Optional[int]

### NumberOfSchemas
- **Type**: typing.Optional[int]


# KafkaSettings

### Broker
- **Type**: typing.Optional[str]

### Topic
- **Type**: typing.Optional[str]

### MessageFormat
- **Type**: typing.Optional[typing.Literal['json', 'json-unformatted']]

### IncludeTransactionDetails
- **Type**: typing.Optional[bool]

### IncludePartitionValue
- **Type**: typing.Optional[bool]

### PartitionIncludeSchemaTable
- **Type**: typing.Optional[bool]

### IncludeTableAlterOperations
- **Type**: typing.Optional[bool]

### IncludeControlDetails
- **Type**: typing.Optional[bool]

### MessageMaxBytes
- **Type**: typing.Optional[int]

### IncludeNullAndEmpty
- **Type**: typing.Optional[bool]

### SecurityProtocol
- **Type**: typing.Optional[typing.Literal['plaintext', 'sasl-ssl', 'ssl-authentication', 'ssl-encryption']]

### SslClientCertificateArn
- **Type**: typing.Optional[str]

### SslClientKeyArn
- **Type**: typing.Optional[str]

### SslClientKeyPassword
- **Type**: typing.Optional[str]

### SslCaCertificateArn
- **Type**: typing.Optional[str]

### SaslUsername
- **Type**: typing.Optional[str]

### SaslPassword
- **Type**: typing.Optional[str]

### NoHexPrefix
- **Type**: typing.Optional[bool]

### SaslMechanism
- **Type**: typing.Optional[typing.Literal['plain', 'scram-sha-512']]

### SslEndpointIdentificationAlgorithm
- **Type**: typing.Optional[typing.Literal['https', 'none']]

### UseLargeIntegerValue
- **Type**: typing.Optional[bool]


# KerberosAuthenticationSettings

### KeyCacheSecretId
- **Type**: typing.Optional[str]

### KeyCacheSecretIamArn
- **Type**: typing.Optional[str]

### Krb5FileContents
- **Type**: typing.Optional[str]


# KinesisSettings

### StreamArn
- **Type**: typing.Optional[str]

### MessageFormat
- **Type**: typing.Optional[typing.Literal['json', 'json-unformatted']]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### IncludeTransactionDetails
- **Type**: typing.Optional[bool]

### IncludePartitionValue
- **Type**: typing.Optional[bool]

### PartitionIncludeSchemaTable
- **Type**: typing.Optional[bool]

### IncludeTableAlterOperations
- **Type**: typing.Optional[bool]

### IncludeControlDetails
- **Type**: typing.Optional[bool]

### IncludeNullAndEmpty
- **Type**: typing.Optional[bool]

### NoHexPrefix
- **Type**: typing.Optional[bool]

### UseLargeIntegerValue
- **Type**: typing.Optional[bool]


# Limitation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListTagsForResourceMessage

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceArnList
- **Type**: typing.Optional[typing.Sequence[str]]


# ListTagsForResourceResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# MariaDbDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]


# MicrosoftSQLServerSettings

### Port
- **Type**: typing.Optional[int]

### BcpPacketSize
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### ControlTablesFileGroup
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### QuerySingleAlwaysOnNode
- **Type**: typing.Optional[bool]

### ReadBackupOnly
- **Type**: typing.Optional[bool]

### SafeguardPolicy
- **Type**: typing.Optional[typing.Literal['exclusive-automatic-truncation', 'rely-on-sql-server-replication-agent', 'shared-automatic-truncation']]

### ServerName
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### UseBcpFullLoad
- **Type**: typing.Optional[bool]

### UseThirdPartyBackupDevice
- **Type**: typing.Optional[bool]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### TrimSpaceInChar
- **Type**: typing.Optional[bool]

### TlogAccessMode
- **Type**: typing.Optional[typing.Literal['BackupOnly', 'PreferBackup', 'PreferTlog', 'TlogOnly']]

### ForceLobLookup
- **Type**: typing.Optional[bool]

### AuthenticationMethod
- **Type**: typing.Optional[typing.Literal['kerberos', 'password']]


# MicrosoftSqlServerDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]


# MigrationProject

### MigrationProjectName
- **Type**: typing.Optional[str]

### MigrationProjectArn
- **Type**: typing.Optional[str]

### MigrationProjectCreationTime
- **Type**: typing.Optional[datetime.datetime]

### SourceDataProviderDescriptors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptor]]

### TargetDataProviderDescriptors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptor]]

### InstanceProfileArn
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### TransformationRules
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SchemaConversionApplicationAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SCApplicationAttributes]


# ModifyConversionConfigurationMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ConversionConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyConversionConfigurationResponse

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDataMigrationMessage

### DataMigrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DataMigrationName
- **Type**: typing.Optional[str]

### EnableCloudwatchLogs
- **Type**: typing.Optional[bool]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### DataMigrationType
- **Type**: typing.Optional[typing.Literal['cdc', 'full-load', 'full-load-and-cdc']]

### SourceDataSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.SourceDataSettingUnion]]

### TargetDataSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TargetDataSetting]]

### NumberOfJobs
- **Type**: typing.Optional[int]

### SelectionRules
- **Type**: typing.Optional[str]


# ModifyDataMigrationResponse

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyDataProviderMessage

### DataProviderIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DataProviderName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### ExactSettings
- **Type**: typing.Optional[bool]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DataProviderSettings]


# ModifyDataProviderResponse

### DataProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataProvider'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyEndpointMessage

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointIdentifier
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[typing.Literal['source', 'target']]

### EngineName
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### ExtraConnectionAttributes
- **Type**: typing.Optional[str]

### CertificateArn
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### ExternalTableDefinition
- **Type**: typing.Optional[str]

### DynamoDbSettings
- **Type**: <class 'NoneType'>

### S3Settings
- **Type**: <class 'NoneType'>

### DmsTransferSettings
- **Type**: <class 'NoneType'>

### MongoDbSettings
- **Type**: <class 'NoneType'>

### KinesisSettings
- **Type**: <class 'NoneType'>

### KafkaSettings
- **Type**: <class 'NoneType'>

### ElasticsearchSettings
- **Type**: <class 'NoneType'>

### NeptuneSettings
- **Type**: <class 'NoneType'>

### RedshiftSettings
- **Type**: <class 'NoneType'>

### PostgreSQLSettings
- **Type**: <class 'NoneType'>

### MySQLSettings
- **Type**: <class 'NoneType'>

### OracleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.OracleSettingsUnion]

### SybaseSettings
- **Type**: <class 'NoneType'>

### MicrosoftSQLServerSettings
- **Type**: <class 'NoneType'>

### IBMDb2Settings
- **Type**: <class 'NoneType'>

### DocDbSettings
- **Type**: <class 'NoneType'>

### RedisSettings
- **Type**: <class 'NoneType'>

### ExactSettings
- **Type**: typing.Optional[bool]

### GcpMySQLSettings
- **Type**: <class 'NoneType'>

### TimestreamSettings
- **Type**: <class 'NoneType'>


# ModifyEndpointResponse

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.Endpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
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


# ModifyEventSubscriptionResponse

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyInstanceProfileMessage

### InstanceProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### NetworkType
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SubnetGroupIdentifier
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyInstanceProfileResponse

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyMigrationProjectMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationProjectName
- **Type**: typing.Optional[str]

### SourceDataProviderDescriptors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorDefinition]]

### TargetDataProviderDescriptors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorDefinition]]

### InstanceProfileIdentifier
- **Type**: typing.Optional[str]

### TransformationRules
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SchemaConversionApplicationAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SCApplicationAttributes]


# ModifyMigrationProjectResponse

### MigrationProject
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.MigrationProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyReplicationConfigMessage

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationConfigIdentifier
- **Type**: typing.Optional[str]

### ReplicationType
- **Type**: typing.Optional[typing.Literal['cdc', 'full-load', 'full-load-and-cdc']]

### TableMappings
- **Type**: typing.Optional[str]

### ReplicationSettings
- **Type**: typing.Optional[str]

### SupplementalSettings
- **Type**: typing.Optional[str]

### ComputeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ComputeConfigUnion]

### SourceEndpointArn
- **Type**: typing.Optional[str]

### TargetEndpointArn
- **Type**: typing.Optional[str]


# ModifyReplicationConfigResponse

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyReplicationInstanceMessage

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AllocatedStorage
- **Type**: typing.Optional[int]

### ApplyImmediately
- **Type**: typing.Optional[bool]

### ReplicationInstanceClass
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

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

### ReplicationInstanceIdentifier
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[str]

### KerberosAuthenticationSettings
- **Type**: <class 'NoneType'>


# ModifyReplicationInstanceResponse

### ReplicationInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyReplicationSubnetGroupMessage

### ReplicationSubnetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ReplicationSubnetGroupDescription
- **Type**: typing.Optional[str]


# ModifyReplicationSubnetGroupResponse

### ReplicationSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyReplicationTaskMessage

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTaskIdentifier
- **Type**: typing.Optional[str]

### MigrationType
- **Type**: typing.Optional[typing.Literal['cdc', 'full-load', 'full-load-and-cdc']]

### TableMappings
- **Type**: typing.Optional[str]

### ReplicationTaskSettings
- **Type**: typing.Optional[str]

### CdcStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]

### TaskData
- **Type**: typing.Optional[str]


# ModifyReplicationTaskResponse

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# MongoDbDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]

### AuthType
- **Type**: typing.Optional[typing.Literal['no', 'password']]

### AuthSource
- **Type**: typing.Optional[str]

### AuthMechanism
- **Type**: typing.Optional[typing.Literal['default', 'mongodb_cr', 'scram_sha_1']]


# MongoDbSettings

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### AuthType
- **Type**: typing.Optional[typing.Literal['no', 'password']]

### AuthMechanism
- **Type**: typing.Optional[typing.Literal['default', 'mongodb_cr', 'scram_sha_1']]

### NestingLevel
- **Type**: typing.Optional[typing.Literal['none', 'one']]

### ExtractDocId
- **Type**: typing.Optional[str]

### DocsToInvestigate
- **Type**: typing.Optional[str]

### AuthSource
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### UseUpdateLookUp
- **Type**: typing.Optional[bool]

### ReplicateShardCollections
- **Type**: typing.Optional[bool]


# MoveReplicationTaskMessage

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# MoveReplicationTaskResponse

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# MySQLSettings

### AfterConnectScript
- **Type**: typing.Optional[str]

### CleanSourceMetadataOnMismatch
- **Type**: typing.Optional[bool]

### DatabaseName
- **Type**: typing.Optional[str]

### EventsPollInterval
- **Type**: typing.Optional[int]

### TargetDbType
- **Type**: typing.Optional[typing.Literal['multiple-databases', 'specific-database']]

### MaxFileSize
- **Type**: typing.Optional[int]

### ParallelLoadThreads
- **Type**: typing.Optional[int]

### Password
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ServerName
- **Type**: typing.Optional[str]

### ServerTimezone
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### ExecuteTimeout
- **Type**: typing.Optional[int]


# MySqlDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]


# NeptuneSettings

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketFolder
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### ErrorRetryDuration
- **Type**: typing.Optional[int]

### MaxFileSize
- **Type**: typing.Optional[int]

### MaxRetryCount
- **Type**: typing.Optional[int]

### IamAuthEnabled
- **Type**: typing.Optional[bool]


# OracleDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]

### AsmServer
- **Type**: typing.Optional[str]

### SecretsManagerOracleAsmSecretId
- **Type**: typing.Optional[str]

### SecretsManagerOracleAsmAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecurityDbEncryptionSecretId
- **Type**: typing.Optional[str]

### SecretsManagerSecurityDbEncryptionAccessRoleArn
- **Type**: typing.Optional[str]


# OracleSettings

### AddSupplementalLogging
- **Type**: typing.Optional[bool]

### ArchivedLogDestId
- **Type**: typing.Optional[int]

### AdditionalArchivedLogDestId
- **Type**: typing.Optional[int]

### ExtraArchivedLogDestIds
- **Type**: typing.Optional[typing.Sequence[int]]

### AllowSelectNestedTables
- **Type**: typing.Optional[bool]

### ParallelAsmReadThreads
- **Type**: typing.Optional[int]

### ReadAheadBlocks
- **Type**: typing.Optional[int]

### AccessAlternateDirectly
- **Type**: typing.Optional[bool]

### UseAlternateFolderForOnline
- **Type**: typing.Optional[bool]

### OraclePathPrefix
- **Type**: typing.Optional[str]

### UsePathPrefix
- **Type**: typing.Optional[str]

### ReplacePathPrefix
- **Type**: typing.Optional[bool]

### EnableHomogenousTablespace
- **Type**: typing.Optional[bool]

### DirectPathNoLog
- **Type**: typing.Optional[bool]

### ArchivedLogsOnly
- **Type**: typing.Optional[bool]

### AsmPassword
- **Type**: typing.Optional[str]

### AsmServer
- **Type**: typing.Optional[str]

### AsmUser
- **Type**: typing.Optional[str]

### CharLengthSemantics
- **Type**: typing.Optional[typing.Literal['byte', 'char', 'default']]

### DatabaseName
- **Type**: typing.Optional[str]

### DirectPathParallelLoad
- **Type**: typing.Optional[bool]

### FailTasksOnLobTruncation
- **Type**: typing.Optional[bool]

### NumberDatatypeScale
- **Type**: typing.Optional[int]

### Password
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ReadTableSpaceName
- **Type**: typing.Optional[bool]

### RetryInterval
- **Type**: typing.Optional[int]

### SecurityDbEncryption
- **Type**: typing.Optional[str]

### SecurityDbEncryptionName
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### SpatialDataOptionToGeoJsonFunctionName
- **Type**: typing.Optional[str]

### StandbyDelayTime
- **Type**: typing.Optional[int]

### Username
- **Type**: typing.Optional[str]

### UseBFile
- **Type**: typing.Optional[bool]

### UseDirectPathFullLoad
- **Type**: typing.Optional[bool]

### UseLogminerReader
- **Type**: typing.Optional[bool]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### SecretsManagerOracleAsmAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerOracleAsmSecretId
- **Type**: typing.Optional[str]

### TrimSpaceInChar
- **Type**: typing.Optional[bool]

### ConvertTimestampWithZoneToUTC
- **Type**: typing.Optional[bool]

### OpenTransactionWindow
- **Type**: typing.Optional[int]

### AuthenticationMethod
- **Type**: typing.Optional[typing.Literal['kerberos', 'password']]


# OracleSettingsOutput

### AddSupplementalLogging
- **Type**: typing.Optional[bool]

### ArchivedLogDestId
- **Type**: typing.Optional[int]

### AdditionalArchivedLogDestId
- **Type**: typing.Optional[int]

### ExtraArchivedLogDestIds
- **Type**: typing.Optional[typing.List[int]]

### AllowSelectNestedTables
- **Type**: typing.Optional[bool]

### ParallelAsmReadThreads
- **Type**: typing.Optional[int]

### ReadAheadBlocks
- **Type**: typing.Optional[int]

### AccessAlternateDirectly
- **Type**: typing.Optional[bool]

### UseAlternateFolderForOnline
- **Type**: typing.Optional[bool]

### OraclePathPrefix
- **Type**: typing.Optional[str]

### UsePathPrefix
- **Type**: typing.Optional[str]

### ReplacePathPrefix
- **Type**: typing.Optional[bool]

### EnableHomogenousTablespace
- **Type**: typing.Optional[bool]

### DirectPathNoLog
- **Type**: typing.Optional[bool]

### ArchivedLogsOnly
- **Type**: typing.Optional[bool]

### AsmPassword
- **Type**: typing.Optional[str]

### AsmServer
- **Type**: typing.Optional[str]

### AsmUser
- **Type**: typing.Optional[str]

### CharLengthSemantics
- **Type**: typing.Optional[typing.Literal['byte', 'char', 'default']]

### DatabaseName
- **Type**: typing.Optional[str]

### DirectPathParallelLoad
- **Type**: typing.Optional[bool]

### FailTasksOnLobTruncation
- **Type**: typing.Optional[bool]

### NumberDatatypeScale
- **Type**: typing.Optional[int]

### Password
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ReadTableSpaceName
- **Type**: typing.Optional[bool]

### RetryInterval
- **Type**: typing.Optional[int]

### SecurityDbEncryption
- **Type**: typing.Optional[str]

### SecurityDbEncryptionName
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### SpatialDataOptionToGeoJsonFunctionName
- **Type**: typing.Optional[str]

### StandbyDelayTime
- **Type**: typing.Optional[int]

### Username
- **Type**: typing.Optional[str]

### UseBFile
- **Type**: typing.Optional[bool]

### UseDirectPathFullLoad
- **Type**: typing.Optional[bool]

### UseLogminerReader
- **Type**: typing.Optional[bool]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### SecretsManagerOracleAsmAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerOracleAsmSecretId
- **Type**: typing.Optional[str]

### TrimSpaceInChar
- **Type**: typing.Optional[bool]

### ConvertTimestampWithZoneToUTC
- **Type**: typing.Optional[bool]

### OpenTransactionWindow
- **Type**: typing.Optional[int]

### AuthenticationMethod
- **Type**: typing.Optional[typing.Literal['kerberos', 'password']]


# OracleSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrderableReplicationInstance

### EngineVersion
- **Type**: typing.Optional[str]

### ReplicationInstanceClass
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### MinAllocatedStorage
- **Type**: typing.Optional[int]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]

### DefaultAllocatedStorage
- **Type**: typing.Optional[int]

### IncludedAllocatedStorage
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### ReleaseStatus
- **Type**: typing.Optional[typing.Literal['beta', 'prod']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# PostgreSQLSettings

### AfterConnectScript
- **Type**: typing.Optional[str]

### CaptureDdls
- **Type**: typing.Optional[bool]

### MaxFileSize
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### DdlArtifactsSchema
- **Type**: typing.Optional[str]

### ExecuteTimeout
- **Type**: typing.Optional[int]

### FailTasksOnLobTruncation
- **Type**: typing.Optional[bool]

### HeartbeatEnable
- **Type**: typing.Optional[bool]

### HeartbeatSchema
- **Type**: typing.Optional[str]

### HeartbeatFrequency
- **Type**: typing.Optional[int]

### Password
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ServerName
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### SlotName
- **Type**: typing.Optional[str]

### PluginName
- **Type**: typing.Optional[typing.Literal['no-preference', 'pglogical', 'test-decoding']]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### TrimSpaceInChar
- **Type**: typing.Optional[bool]

### MapBooleanAsBoolean
- **Type**: typing.Optional[bool]

### MapJsonbAsClob
- **Type**: typing.Optional[bool]

### MapLongVarcharAs
- **Type**: typing.Optional[typing.Literal['clob', 'nclob', 'wstring']]

### DatabaseMode
- **Type**: typing.Optional[typing.Literal['babelfish', 'default']]

### BabelfishDatabaseName
- **Type**: typing.Optional[str]

### DisableUnicodeSourceFilter
- **Type**: typing.Optional[bool]


# PostgreSqlDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]


# PremigrationAssessmentStatus

### PremigrationAssessmentRunArn
- **Type**: typing.Optional[str]

### FailOnAssessmentFailure
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### PremigrationAssessmentRunCreationDate
- **Type**: typing.Optional[datetime.datetime]

### AssessmentProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunProgress]

### LastFailureMessage
- **Type**: typing.Optional[str]

### ResultLocationBucket
- **Type**: typing.Optional[str]

### ResultLocationFolder
- **Type**: typing.Optional[str]

### ResultEncryptionMode
- **Type**: typing.Optional[str]

### ResultKmsKeyArn
- **Type**: typing.Optional[str]

### ResultStatistic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunResultStatistic]


# ProvisionData

### ProvisionState
- **Type**: typing.Optional[str]

### ProvisionedCapacityUnits
- **Type**: typing.Optional[int]

### DateProvisioned
- **Type**: typing.Optional[datetime.datetime]

### IsNewProvisioningAvailable
- **Type**: typing.Optional[bool]

### DateNewProvisioningDataAvailable
- **Type**: typing.Optional[datetime.datetime]

### ReasonForNewProvisioningData
- **Type**: typing.Optional[str]


# RdsConfiguration

### EngineEdition
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### InstanceVcpu
- **Type**: typing.Optional[float]

### InstanceMemory
- **Type**: typing.Optional[float]

### StorageType
- **Type**: typing.Optional[str]

### StorageSize
- **Type**: typing.Optional[int]

### StorageIops
- **Type**: typing.Optional[int]

### DeploymentOption
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]


# RdsRecommendation

### RequirementsToTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RdsRequirements]

### TargetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RdsConfiguration]


# RdsRequirements

### EngineEdition
- **Type**: typing.Optional[str]

### InstanceVcpu
- **Type**: typing.Optional[float]

### InstanceMemory
- **Type**: typing.Optional[float]

### StorageSize
- **Type**: typing.Optional[int]

### StorageIops
- **Type**: typing.Optional[int]

### DeploymentOption
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]


# RebootReplicationInstanceMessage

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ForceFailover
- **Type**: typing.Optional[bool]

### ForcePlannedFailover
- **Type**: typing.Optional[bool]


# RebootReplicationInstanceResponse

### ReplicationInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# Recommendation

### DatabaseId
- **Type**: typing.Optional[str]

### EngineName
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Preferred
- **Type**: typing.Optional[bool]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RecommendationSettings]

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RecommendationData]


# RecommendationData

### RdsEngine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RdsRecommendation]


# RecommendationSettings

### InstanceSizingType
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadType
- **Type**: <class 'str'>
- **Required**: Yes


# RedisSettings

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### SslSecurityProtocol
- **Type**: typing.Optional[typing.Literal['plaintext', 'ssl-encryption']]

### AuthType
- **Type**: typing.Optional[typing.Literal['auth-role', 'auth-token', 'none']]

### AuthUserName
- **Type**: typing.Optional[str]

### AuthPassword
- **Type**: typing.Optional[str]

### SslCaCertificateArn
- **Type**: typing.Optional[str]


# RedshiftDataProviderSettings

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]


# RedshiftSettings

### AcceptAnyDate
- **Type**: typing.Optional[bool]

### AfterConnectScript
- **Type**: typing.Optional[str]

### BucketFolder
- **Type**: typing.Optional[str]

### BucketName
- **Type**: typing.Optional[str]

### CaseSensitiveNames
- **Type**: typing.Optional[bool]

### CompUpdate
- **Type**: typing.Optional[bool]

### ConnectionTimeout
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### DateFormat
- **Type**: typing.Optional[str]

### EmptyAsNull
- **Type**: typing.Optional[bool]

### EncryptionMode
- **Type**: typing.Optional[typing.Literal['sse-kms', 'sse-s3']]

### ExplicitIds
- **Type**: typing.Optional[bool]

### FileTransferUploadStreams
- **Type**: typing.Optional[int]

### LoadTimeout
- **Type**: typing.Optional[int]

### MaxFileSize
- **Type**: typing.Optional[int]

### Password
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### RemoveQuotes
- **Type**: typing.Optional[bool]

### ReplaceInvalidChars
- **Type**: typing.Optional[str]

### ReplaceChars
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### ServerSideEncryptionKmsKeyId
- **Type**: typing.Optional[str]

### TimeFormat
- **Type**: typing.Optional[str]

### TrimBlanks
- **Type**: typing.Optional[bool]

### TruncateColumns
- **Type**: typing.Optional[bool]

### Username
- **Type**: typing.Optional[str]

### WriteBufferSize
- **Type**: typing.Optional[int]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### MapBooleanAsBoolean
- **Type**: typing.Optional[bool]


# RefreshSchemasMessage

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RefreshSchemasResponse

### RefreshSchemasStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.RefreshSchemasStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# RefreshSchemasStatus

### EndpointArn
- **Type**: typing.Optional[str]

### ReplicationInstanceArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['failed', 'refreshing', 'successful']]

### LastRefreshDate
- **Type**: typing.Optional[datetime.datetime]

### LastFailureMessage
- **Type**: typing.Optional[str]


# ReloadReplicationTablesMessage

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### TablesToReload
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TableToReload]
- **Required**: Yes

### ReloadOption
- **Type**: typing.Optional[typing.Literal['data-reload', 'validate-only']]


# ReloadReplicationTablesResponse

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# ReloadTablesMessage

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TablesToReload
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TableToReload]
- **Required**: Yes

### ReloadOption
- **Type**: typing.Optional[typing.Literal['data-reload', 'validate-only']]


# ReloadTablesResponse

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsFromResourceMessage

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# Replication

### ReplicationConfigIdentifier
- **Type**: typing.Optional[str]

### ReplicationConfigArn
- **Type**: typing.Optional[str]

### SourceEndpointArn
- **Type**: typing.Optional[str]

### TargetEndpointArn
- **Type**: typing.Optional[str]

### ReplicationType
- **Type**: typing.Optional[typing.Literal['cdc', 'full-load', 'full-load-and-cdc']]

### Status
- **Type**: typing.Optional[str]

### ProvisionData
- **Type**: <class 'NoneType'>

### PremigrationAssessmentStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.PremigrationAssessmentStatus]]

### StopReason
- **Type**: typing.Optional[str]

### FailureMessages
- **Type**: typing.Optional[typing.List[str]]

### ReplicationStats
- **Type**: <class 'NoneType'>

### StartReplicationType
- **Type**: typing.Optional[str]

### CdcStartTime
- **Type**: typing.Optional[datetime.datetime]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]

### RecoveryCheckpoint
- **Type**: typing.Optional[str]

### ReplicationCreateTime
- **Type**: typing.Optional[datetime.datetime]

### ReplicationUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### ReplicationLastStopTime
- **Type**: typing.Optional[datetime.datetime]

### ReplicationDeprovisionTime
- **Type**: typing.Optional[datetime.datetime]


# ReplicationConfig

### ReplicationConfigIdentifier
- **Type**: typing.Optional[str]

### ReplicationConfigArn
- **Type**: typing.Optional[str]

### SourceEndpointArn
- **Type**: typing.Optional[str]

### TargetEndpointArn
- **Type**: typing.Optional[str]

### ReplicationType
- **Type**: typing.Optional[typing.Literal['cdc', 'full-load', 'full-load-and-cdc']]

### ComputeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ComputeConfigOutput]

### ReplicationSettings
- **Type**: typing.Optional[str]

### SupplementalSettings
- **Type**: typing.Optional[str]

### TableMappings
- **Type**: typing.Optional[str]

### ReplicationConfigCreateTime
- **Type**: typing.Optional[datetime.datetime]

### ReplicationConfigUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# ReplicationInstance

### ReplicationInstanceIdentifier
- **Type**: typing.Optional[str]

### ReplicationInstanceClass
- **Type**: typing.Optional[str]

### ReplicationInstanceStatus
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### InstanceCreateTime
- **Type**: typing.Optional[datetime.datetime]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.VpcSecurityGroupMembership]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ReplicationSubnetGroup
- **Type**: <class 'NoneType'>

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationPendingModifiedValues]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### ReplicationInstanceArn
- **Type**: typing.Optional[str]

### ReplicationInstancePublicIpAddress
- **Type**: typing.Optional[str]

### ReplicationInstancePrivateIpAddress
- **Type**: typing.Optional[str]

### ReplicationInstancePublicIpAddresses
- **Type**: typing.Optional[typing.List[str]]

### ReplicationInstancePrivateIpAddresses
- **Type**: typing.Optional[typing.List[str]]

### ReplicationInstanceIpv6Addresses
- **Type**: typing.Optional[typing.List[str]]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### FreeUntil
- **Type**: typing.Optional[datetime.datetime]

### DnsNameServers
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[str]

### KerberosAuthenticationSettings
- **Type**: <class 'NoneType'>


# ReplicationInstanceTaskLog

### ReplicationTaskName
- **Type**: typing.Optional[str]

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### ReplicationInstanceTaskLogSize
- **Type**: typing.Optional[int]


# ReplicationPendingModifiedValues

### ReplicationInstanceClass
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[str]


# ReplicationStats

### FullLoadProgressPercent
- **Type**: typing.Optional[int]

### ElapsedTimeMillis
- **Type**: typing.Optional[int]

### TablesLoaded
- **Type**: typing.Optional[int]

### TablesLoading
- **Type**: typing.Optional[int]

### TablesQueued
- **Type**: typing.Optional[int]

### TablesErrored
- **Type**: typing.Optional[int]

### FreshStartDate
- **Type**: typing.Optional[datetime.datetime]

### StartDate
- **Type**: typing.Optional[datetime.datetime]

### StopDate
- **Type**: typing.Optional[datetime.datetime]

### FullLoadStartDate
- **Type**: typing.Optional[datetime.datetime]

### FullLoadFinishDate
- **Type**: typing.Optional[datetime.datetime]


# ReplicationSubnetGroup

### ReplicationSubnetGroupIdentifier
- **Type**: typing.Optional[str]

### ReplicationSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.Subnet]]

### SupportedNetworkTypes
- **Type**: typing.Optional[typing.List[str]]


# ReplicationTask

### ReplicationTaskIdentifier
- **Type**: typing.Optional[str]

### SourceEndpointArn
- **Type**: typing.Optional[str]

### TargetEndpointArn
- **Type**: typing.Optional[str]

### ReplicationInstanceArn
- **Type**: typing.Optional[str]

### MigrationType
- **Type**: typing.Optional[typing.Literal['cdc', 'full-load', 'full-load-and-cdc']]

### TableMappings
- **Type**: typing.Optional[str]

### ReplicationTaskSettings
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### LastFailureMessage
- **Type**: typing.Optional[str]

### StopReason
- **Type**: typing.Optional[str]

### ReplicationTaskCreationDate
- **Type**: typing.Optional[datetime.datetime]

### ReplicationTaskStartDate
- **Type**: typing.Optional[datetime.datetime]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]

### RecoveryCheckpoint
- **Type**: typing.Optional[str]

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### ReplicationTaskStats
- **Type**: <class 'NoneType'>

### TaskData
- **Type**: typing.Optional[str]

### TargetReplicationInstanceArn
- **Type**: typing.Optional[str]


# ReplicationTaskAssessmentResult

### ReplicationTaskIdentifier
- **Type**: typing.Optional[str]

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### ReplicationTaskLastAssessmentDate
- **Type**: typing.Optional[datetime.datetime]

### AssessmentStatus
- **Type**: typing.Optional[str]

### AssessmentResultsFile
- **Type**: typing.Optional[str]

### AssessmentResults
- **Type**: typing.Optional[str]

### S3ObjectUrl
- **Type**: typing.Optional[str]


# ReplicationTaskAssessmentRun

### ReplicationTaskAssessmentRunArn
- **Type**: typing.Optional[str]

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### ReplicationTaskAssessmentRunCreationDate
- **Type**: typing.Optional[datetime.datetime]

### AssessmentProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunProgress]

### LastFailureMessage
- **Type**: typing.Optional[str]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### ResultLocationBucket
- **Type**: typing.Optional[str]

### ResultLocationFolder
- **Type**: typing.Optional[str]

### ResultEncryptionMode
- **Type**: typing.Optional[str]

### ResultKmsKeyArn
- **Type**: typing.Optional[str]

### AssessmentRunName
- **Type**: typing.Optional[str]

### IsLatestTaskAssessmentRun
- **Type**: typing.Optional[bool]

### ResultStatistic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunResultStatistic]


# ReplicationTaskAssessmentRunProgress

### IndividualAssessmentCount
- **Type**: typing.Optional[int]

### IndividualAssessmentCompletedCount
- **Type**: typing.Optional[int]


# ReplicationTaskAssessmentRunResultStatistic

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReplicationTaskIndividualAssessment

### ReplicationTaskIndividualAssessmentArn
- **Type**: typing.Optional[str]

### ReplicationTaskAssessmentRunArn
- **Type**: typing.Optional[str]

### IndividualAssessmentName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### ReplicationTaskIndividualAssessmentStartDate
- **Type**: typing.Optional[datetime.datetime]


# ReplicationTaskStats

### FullLoadProgressPercent
- **Type**: typing.Optional[int]

### ElapsedTimeMillis
- **Type**: typing.Optional[int]

### TablesLoaded
- **Type**: typing.Optional[int]

### TablesLoading
- **Type**: typing.Optional[int]

### TablesQueued
- **Type**: typing.Optional[int]

### TablesErrored
- **Type**: typing.Optional[int]

### FreshStartDate
- **Type**: typing.Optional[datetime.datetime]

### StartDate
- **Type**: typing.Optional[datetime.datetime]

### StopDate
- **Type**: typing.Optional[datetime.datetime]

### FullLoadStartDate
- **Type**: typing.Optional[datetime.datetime]

### FullLoadFinishDate
- **Type**: typing.Optional[datetime.datetime]


# ResourcePendingMaintenanceActions

### ResourceIdentifier
- **Type**: typing.Optional[str]

### PendingMaintenanceActionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.PendingMaintenanceAction]]


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


# RunFleetAdvisorLsaAnalysisResponse

### LsaAnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# S3Settings

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### ExternalTableDefinition
- **Type**: typing.Optional[str]

### CsvRowDelimiter
- **Type**: typing.Optional[str]

### CsvDelimiter
- **Type**: typing.Optional[str]

### BucketFolder
- **Type**: typing.Optional[str]

### BucketName
- **Type**: typing.Optional[str]

### CompressionType
- **Type**: typing.Optional[typing.Literal['gzip', 'none']]

### EncryptionMode
- **Type**: typing.Optional[typing.Literal['sse-kms', 'sse-s3']]

### ServerSideEncryptionKmsKeyId
- **Type**: typing.Optional[str]

### DataFormat
- **Type**: typing.Optional[typing.Literal['csv', 'parquet']]

### EncodingType
- **Type**: typing.Optional[typing.Literal['plain', 'plain-dictionary', 'rle-dictionary']]

### DictPageSizeLimit
- **Type**: typing.Optional[int]

### RowGroupLength
- **Type**: typing.Optional[int]

### DataPageSize
- **Type**: typing.Optional[int]

### ParquetVersion
- **Type**: typing.Optional[typing.Literal['parquet-1-0', 'parquet-2-0']]

### EnableStatistics
- **Type**: typing.Optional[bool]

### IncludeOpForFullLoad
- **Type**: typing.Optional[bool]

### CdcInsertsOnly
- **Type**: typing.Optional[bool]

### TimestampColumnName
- **Type**: typing.Optional[str]

### ParquetTimestampInMillisecond
- **Type**: typing.Optional[bool]

### CdcInsertsAndUpdates
- **Type**: typing.Optional[bool]

### DatePartitionEnabled
- **Type**: typing.Optional[bool]

### DatePartitionSequence
- **Type**: typing.Optional[typing.Literal['DDMMYYYY', 'MMYYYYDD', 'YYYYMM', 'YYYYMMDD', 'YYYYMMDDHH']]

### DatePartitionDelimiter
- **Type**: typing.Optional[typing.Literal['DASH', 'NONE', 'SLASH', 'UNDERSCORE']]

### UseCsvNoSupValue
- **Type**: typing.Optional[bool]

### CsvNoSupValue
- **Type**: typing.Optional[str]

### PreserveTransactions
- **Type**: typing.Optional[bool]

### CdcPath
- **Type**: typing.Optional[str]

### UseTaskStartTimeForFullLoadTimestamp
- **Type**: typing.Optional[bool]

### CannedAclForObjects
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'none', 'private', 'public-read', 'public-read-write']]

### AddColumnName
- **Type**: typing.Optional[bool]

### CdcMaxBatchInterval
- **Type**: typing.Optional[int]

### CdcMinFileSize
- **Type**: typing.Optional[int]

### CsvNullValue
- **Type**: typing.Optional[str]

### IgnoreHeaderRows
- **Type**: typing.Optional[int]

### MaxFileSize
- **Type**: typing.Optional[int]

### Rfc4180
- **Type**: typing.Optional[bool]

### DatePartitionTimezone
- **Type**: typing.Optional[str]

### AddTrailingPaddingCharacter
- **Type**: typing.Optional[bool]

### ExpectedBucketOwner
- **Type**: typing.Optional[str]

### GlueCatalogGeneration
- **Type**: typing.Optional[bool]


# SCApplicationAttributes

### S3BucketPath
- **Type**: typing.Optional[str]

### S3BucketRoleArn
- **Type**: typing.Optional[str]


# SchemaConversionRequest

### Status
- **Type**: typing.Optional[str]

### RequestIdentifier
- **Type**: typing.Optional[str]

### MigrationProjectArn
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ErrorDetails]

### ExportSqlDetails
- **Type**: <class 'NoneType'>


# SchemaResponse

### CodeLineCount
- **Type**: typing.Optional[int]

### CodeSize
- **Type**: typing.Optional[int]

### Complexity
- **Type**: typing.Optional[str]

### Server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ServerShortInfoResponse]

### DatabaseInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DatabaseShortInfoResponse]

### SchemaId
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### OriginalSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SchemaShortInfoResponse]

### Similarity
- **Type**: typing.Optional[float]


# SchemaShortInfoResponse

### SchemaId
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### DatabaseId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### DatabaseIpAddress
- **Type**: typing.Optional[str]


# ServerShortInfoResponse

### ServerId
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]


# SourceDataSetting

### CDCStartPosition
- **Type**: typing.Optional[str]

### CDCStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### CDCStopTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### SlotName
- **Type**: typing.Optional[str]


# SourceDataSettingOutput

### CDCStartPosition
- **Type**: typing.Optional[str]

### CDCStartTime
- **Type**: typing.Optional[datetime.datetime]

### CDCStopTime
- **Type**: typing.Optional[datetime.datetime]

### SlotName
- **Type**: typing.Optional[str]


# SourceDataSettingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartDataMigrationMessage

### DataMigrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### StartType
- **Type**: typing.Literal['reload-target', 'resume-processing', 'start-replication']
- **Required**: Yes


# StartDataMigrationResponse

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartExtensionPackAssociationMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartExtensionPackAssociationResponse

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartMetadataModelAssessmentMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionRules
- **Type**: <class 'str'>
- **Required**: Yes


# StartMetadataModelAssessmentResponse

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartMetadataModelConversionMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionRules
- **Type**: <class 'str'>
- **Required**: Yes


# StartMetadataModelConversionResponse

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartMetadataModelExportAsScriptMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionRules
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### FileName
- **Type**: typing.Optional[str]


# StartMetadataModelExportAsScriptResponse

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartMetadataModelExportToTargetMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionRules
- **Type**: <class 'str'>
- **Required**: Yes

### OverwriteExtensionPack
- **Type**: typing.Optional[bool]


# StartMetadataModelExportToTargetResponse

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartMetadataModelImportMessage

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionRules
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: typing.Literal['SOURCE', 'TARGET']
- **Required**: Yes

### Refresh
- **Type**: typing.Optional[bool]


# StartMetadataModelImportResponse

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartRecommendationsRequest

### DatabaseId
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.RecommendationSettings'>
- **Required**: Yes


# StartRecommendationsRequestEntry

### DatabaseId
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.RecommendationSettings'>
- **Required**: Yes


# StartReplicationMessage

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### StartReplicationType
- **Type**: <class 'str'>
- **Required**: Yes

### PremigrationAssessmentSettings
- **Type**: typing.Optional[str]

### CdcStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]


# StartReplicationResponse

### Replication
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.Replication'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartReplicationTaskAssessmentMessage

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartReplicationTaskAssessmentResponse

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartReplicationTaskAssessmentRunMessage

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResultLocationBucket
- **Type**: <class 'str'>
- **Required**: Yes

### AssessmentRunName
- **Type**: <class 'str'>
- **Required**: Yes

### ResultLocationFolder
- **Type**: typing.Optional[str]

### ResultEncryptionMode
- **Type**: typing.Optional[str]

### ResultKmsKeyArn
- **Type**: typing.Optional[str]

### IncludeOnly
- **Type**: typing.Optional[typing.Sequence[str]]

### Exclude
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.Tag]]


# StartReplicationTaskAssessmentRunResponse

### ReplicationTaskAssessmentRun
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StartReplicationTaskMessage

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### StartReplicationTaskType
- **Type**: typing.Literal['reload-target', 'resume-processing', 'start-replication']
- **Required**: Yes

### CdcStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.Timestamp]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]


# StartReplicationTaskResponse

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StopDataMigrationMessage

### DataMigrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopDataMigrationResponse

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StopReplicationMessage

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationResponse

### Replication
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.Replication'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# StopReplicationTaskMessage

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationTaskResponse

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# Subnet

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.AvailabilityZone]

### SubnetStatus
- **Type**: typing.Optional[str]


# SupportedEndpointType

### EngineName
- **Type**: typing.Optional[str]

### SupportsCDC
- **Type**: typing.Optional[bool]

### EndpointType
- **Type**: typing.Optional[typing.Literal['source', 'target']]

### ReplicationInstanceEngineMinimumVersion
- **Type**: typing.Optional[str]

### EngineDisplayName
- **Type**: typing.Optional[str]


# SybaseSettings

### DatabaseName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ServerName
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### SecretsManagerSecretId
- **Type**: typing.Optional[str]


# TableStatistics

### SchemaName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Inserts
- **Type**: typing.Optional[int]

### Deletes
- **Type**: typing.Optional[int]

### Updates
- **Type**: typing.Optional[int]

### Ddls
- **Type**: typing.Optional[int]

### AppliedInserts
- **Type**: typing.Optional[int]

### AppliedDeletes
- **Type**: typing.Optional[int]

### AppliedUpdates
- **Type**: typing.Optional[int]

### AppliedDdls
- **Type**: typing.Optional[int]

### FullLoadRows
- **Type**: typing.Optional[int]

### FullLoadCondtnlChkFailedRows
- **Type**: typing.Optional[int]

### FullLoadErrorRows
- **Type**: typing.Optional[int]

### FullLoadStartTime
- **Type**: typing.Optional[datetime.datetime]

### FullLoadEndTime
- **Type**: typing.Optional[datetime.datetime]

### FullLoadReloaded
- **Type**: typing.Optional[bool]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### TableState
- **Type**: typing.Optional[str]

### ValidationPendingRecords
- **Type**: typing.Optional[int]

### ValidationFailedRecords
- **Type**: typing.Optional[int]

### ValidationSuspendedRecords
- **Type**: typing.Optional[int]

### ValidationState
- **Type**: typing.Optional[str]

### ValidationStateDetails
- **Type**: typing.Optional[str]


# TableToReload

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# TargetDataSetting

### TablePreparationMode
- **Type**: typing.Optional[typing.Literal['do-nothing', 'drop-tables-on-target', 'truncate']]


# TestConnectionMessage

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# TestConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.Connection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestreamSettings

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### MemoryDuration
- **Type**: <class 'int'>
- **Required**: Yes

### MagneticDuration
- **Type**: <class 'int'>
- **Required**: Yes

### CdcInsertsAndUpdates
- **Type**: typing.Optional[bool]

### EnableMagneticStoreWrites
- **Type**: typing.Optional[bool]


# UpdateSubscriptionsToEventBridgeMessage

### ForceMove
- **Type**: typing.Optional[bool]


# UpdateSubscriptionsToEventBridgeResponse

### Result
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadata'>
- **Required**: Yes


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



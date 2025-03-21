# Dms Classes

# AccountQuotaTypeDef

### AccountQuotaName
- **Type**: typing.Optional[str]

### Used
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# AddTagsToResourceMessageTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]
- **Required**: Yes


# ApplyPendingMaintenanceActionMessageTypeDef

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApplyAction
- **Type**: <class 'str'>
- **Required**: Yes

### OptInType
- **Type**: <class 'str'>
- **Required**: Yes


# ApplyPendingMaintenanceActionResponseTypeDef

### ResourcePendingMaintenanceActions
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResourcePendingMaintenanceActionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AvailabilityZoneTypeDef

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchStartRecommendationsErrorEntryTypeDef

### DatabaseId
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]


# BatchStartRecommendationsRequestTypeDef

### Data
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.StartRecommendationsRequestEntryTypeDef]]


# BatchStartRecommendationsResponseTypeDef

### ErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.BatchStartRecommendationsErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelReplicationTaskAssessmentRunMessageTypeDef

### ReplicationTaskAssessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# CancelReplicationTaskAssessmentRunResponseTypeDef

### ReplicationTaskAssessmentRun
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CertificateTypeDef

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


# CollectorHealthCheckTypeDef

### CollectorStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'UNREGISTERED']]

### LocalCollectorS3Access
- **Type**: typing.Optional[bool]

### WebCollectorS3Access
- **Type**: typing.Optional[bool]

### WebCollectorGrantedRoleBasedAccess
- **Type**: typing.Optional[bool]


# CollectorResponseTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.CollectorHealthCheckTypeDef]

### LastDataReceived
- **Type**: typing.Optional[str]

### RegisteredDate
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### ModifiedDate
- **Type**: typing.Optional[str]

### InventoryData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.InventoryDataTypeDef]


# CollectorShortInfoResponseTypeDef

### CollectorReferencedId
- **Type**: typing.Optional[str]

### CollectorName
- **Type**: typing.Optional[str]


# ComputeConfigOutputTypeDef

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


# ComputeConfigTypeDef

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


# ComputeConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectionTypeDef

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


# CreateDataMigrationMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.SourceDataSettingUnionTypeDef]]

### TargetDataSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TargetDataSettingTypeDef]]

### NumberOfJobs
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]

### SelectionRules
- **Type**: typing.Optional[str]


# CreateDataMigrationResponseTypeDef

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataProviderMessageTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataProviderSettingsTypeDef'>
- **Required**: Yes

### DataProviderName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]


# CreateDataProviderResponseTypeDef

### DataProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataProviderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEndpointMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]

### CertificateArn
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### ExternalTableDefinition
- **Type**: typing.Optional[str]

### DynamoDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DynamoDbSettingsTypeDef]

### S3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.S3SettingsTypeDef]

### DmsTransferSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DmsTransferSettingsTypeDef]

### MongoDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MongoDbSettingsTypeDef]

### KinesisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.KinesisSettingsTypeDef]

### KafkaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.KafkaSettingsTypeDef]

### ElasticsearchSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ElasticsearchSettingsTypeDef]

### NeptuneSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.NeptuneSettingsTypeDef]

### RedshiftSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RedshiftSettingsTypeDef]

### PostgreSQLSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PostgreSQLSettingsTypeDef]

### MySQLSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MySQLSettingsTypeDef]

### OracleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.OracleSettingsUnionTypeDef]

### SybaseSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SybaseSettingsTypeDef]

### MicrosoftSQLServerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MicrosoftSQLServerSettingsTypeDef]

### IBMDb2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.IBMDb2SettingsTypeDef]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### DocDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DocDbSettingsTypeDef]

### RedisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RedisSettingsTypeDef]

### GcpMySQLSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.GcpMySQLSettingsTypeDef]

### TimestreamSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestreamSettingsTypeDef]


# CreateEndpointResponseTypeDef

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.EndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]


# CreateEventSubscriptionResponseTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFleetAdvisorCollectorRequestTypeDef

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


# CreateFleetAdvisorCollectorResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstanceProfileMessageTypeDef

### AvailabilityZone
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]

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


# CreateInstanceProfileResponseTypeDef

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.InstanceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMigrationProjectMessageTypeDef

### SourceDataProviderDescriptors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorDefinitionTypeDef]
- **Required**: Yes

### TargetDataProviderDescriptors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorDefinitionTypeDef]
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]

### SchemaConversionApplicationAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SCApplicationAttributesTypeDef]


# CreateMigrationProjectResponseTypeDef

### MigrationProject
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.MigrationProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReplicationConfigMessageTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ComputeConfigUnionTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]


# CreateReplicationConfigResponseTypeDef

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReplicationInstanceMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.KerberosAuthenticationSettingsTypeDef]


# CreateReplicationInstanceResponseTypeDef

### ReplicationInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReplicationSubnetGroupMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]


# CreateReplicationSubnetGroupResponseTypeDef

### ReplicationSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReplicationTaskMessageTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]

### TaskData
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]


# CreateReplicationTaskResponseTypeDef

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataMigrationSettingsTypeDef

### NumberOfJobs
- **Type**: typing.Optional[int]

### CloudwatchLogsEnabled
- **Type**: typing.Optional[bool]

### SelectionRules
- **Type**: typing.Optional[str]


# DataMigrationStatisticsTypeDef

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


# DataMigrationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DataMigrationSettingsTypeDef]

### SourceDataSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.SourceDataSettingOutputTypeDef]]

### TargetDataSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.TargetDataSettingTypeDef]]

### DataMigrationStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DataMigrationStatisticsTypeDef]

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


# DataProviderDescriptorDefinitionTypeDef

### DataProviderIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]


# DataProviderDescriptorTypeDef

### SecretsManagerSecretId
- **Type**: typing.Optional[str]

### SecretsManagerAccessRoleArn
- **Type**: typing.Optional[str]

### DataProviderName
- **Type**: typing.Optional[str]

### DataProviderArn
- **Type**: typing.Optional[str]


# DataProviderSettingsTypeDef

### RedshiftSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RedshiftDataProviderSettingsTypeDef]

### PostgreSqlSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PostgreSqlDataProviderSettingsTypeDef]

### MySqlSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MySqlDataProviderSettingsTypeDef]

### OracleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.OracleDataProviderSettingsTypeDef]

### MicrosoftSqlServerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MicrosoftSqlServerDataProviderSettingsTypeDef]

### DocDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DocDbDataProviderSettingsTypeDef]

### MariaDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MariaDbDataProviderSettingsTypeDef]

### IbmDb2LuwSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.IbmDb2LuwDataProviderSettingsTypeDef]

### IbmDb2zOsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.IbmDb2zOsDataProviderSettingsTypeDef]

### MongoDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MongoDbDataProviderSettingsTypeDef]


# DataProviderTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DataProviderSettingsTypeDef]


# DatabaseInstanceSoftwareDetailsResponseTypeDef

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


# DatabaseResponseTypeDef

### DatabaseId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### NumberOfSchemas
- **Type**: typing.Optional[int]

### Server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ServerShortInfoResponseTypeDef]

### SoftwareDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DatabaseInstanceSoftwareDetailsResponseTypeDef]

### Collectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.CollectorShortInfoResponseTypeDef]]


# DatabaseShortInfoResponseTypeDef

### DatabaseId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### DatabaseIpAddress
- **Type**: typing.Optional[str]

### DatabaseEngine
- **Type**: typing.Optional[str]


# DefaultErrorDetailsTypeDef

### Message
- **Type**: typing.Optional[str]


# DeleteCertificateMessageTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateResponseTypeDef

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.CertificateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCollectorRequestTypeDef

### CollectorReferencedId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionMessageTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataMigrationMessageTypeDef

### DataMigrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataMigrationResponseTypeDef

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataProviderMessageTypeDef

### DataProviderIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataProviderResponseTypeDef

### DataProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataProviderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEndpointMessageTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointResponseTypeDef

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.EndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEventSubscriptionMessageTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionResponseTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFleetAdvisorDatabasesRequestTypeDef

### DatabaseIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteFleetAdvisorDatabasesResponseTypeDef

### DatabaseIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInstanceProfileMessageTypeDef

### InstanceProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceProfileResponseTypeDef

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.InstanceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMigrationProjectMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMigrationProjectResponseTypeDef

### MigrationProject
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.MigrationProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteReplicationConfigMessageTypeDef

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationConfigResponseTypeDef

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteReplicationInstanceMessageTypeDef

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationInstanceResponseTypeDef

### ReplicationInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteReplicationSubnetGroupMessageTypeDef

### ReplicationSubnetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationTaskAssessmentRunMessageTypeDef

### ReplicationTaskAssessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationTaskAssessmentRunResponseTypeDef

### ReplicationTaskAssessmentRun
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteReplicationTaskMessageTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationTaskResponseTypeDef

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccountAttributesResponseTypeDef

### AccountQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.AccountQuotaTypeDef]
- **Required**: Yes

### UniqueAccountIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicableIndividualAssessmentsMessageTypeDef

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


# DescribeApplicableIndividualAssessmentsResponseTypeDef

### IndividualAssessmentNames
- **Type**: typing.List[str]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCertificatesMessagePaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeCertificatesMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCertificatesResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.CertificateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectionsMessagePaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeConnectionsMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeConnectionsMessageWaitTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.WaiterConfigTypeDef]


# DescribeConnectionsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConversionConfigurationMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConversionConfigurationResponseTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ConversionConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataMigrationsMessagePaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WithoutStatistics
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeDataMigrationsMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WithoutStatistics
- **Type**: typing.Optional[bool]


# DescribeDataMigrationsResponseTypeDef

### DataMigrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.DataMigrationTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataProvidersMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDataProvidersResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### DataProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.DataProviderTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointSettingsMessageTypeDef

### EngineName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEndpointSettingsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EndpointSettingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointTypesMessagePaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeEndpointTypesMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEndpointTypesResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedEndpointTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SupportedEndpointTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointsMessagePaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeEndpointsMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEndpointsMessageWaitTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.WaiterConfigTypeDef]


# DescribeEndpointsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEngineVersionsMessageTypeDef

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEngineVersionsResponseTypeDef

### EngineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EngineVersionTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventCategoriesMessageTypeDef

### SourceType
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]


# DescribeEventCategoriesResponseTypeDef

### EventCategoryGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EventCategoryGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventSubscriptionsMessagePaginateTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeEventSubscriptionsMessageTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventSubscriptionsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### EventSubscriptionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EventSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventsMessagePaginateTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['replication-instance']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeEventsMessageTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['replication-instance']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExtensionPackAssociationsMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeExtensionPackAssociationsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetAdvisorCollectorsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorCollectorsResponseTypeDef

### Collectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.CollectorResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorDatabasesRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorDatabasesResponseTypeDef

### Databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.DatabaseResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorLsaAnalysisRequestTypeDef

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorLsaAnalysisResponseTypeDef

### Analysis
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.FleetAdvisorLsaAnalysisResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorSchemaObjectSummaryRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef

### FleetAdvisorSchemaObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.FleetAdvisorSchemaObjectResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorSchemasRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFleetAdvisorSchemasResponseTypeDef

### FleetAdvisorSchemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceProfilesMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeInstanceProfilesResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.InstanceProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMetadataModelAssessmentsMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelAssessmentsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMetadataModelConversionsMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelConversionsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMetadataModelExportsAsScriptMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelExportsAsScriptResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMetadataModelExportsToTargetMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelExportsToTargetResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMetadataModelImportsMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeMetadataModelImportsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.SchemaConversionRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMigrationProjectsMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeMigrationProjectsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationProjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.MigrationProjectTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrderableReplicationInstancesMessagePaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeOrderableReplicationInstancesMessageTypeDef

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeOrderableReplicationInstancesResponseTypeDef

### OrderableReplicationInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.OrderableReplicationInstanceTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePendingMaintenanceActionsMessageTypeDef

### ReplicationInstanceArn
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribePendingMaintenanceActionsResponseTypeDef

### PendingMaintenanceActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ResourcePendingMaintenanceActionsTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRecommendationLimitationsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRecommendationLimitationsResponseTypeDef

### Limitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.LimitationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRecommendationsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRecommendationsResponseTypeDef

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.RecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRefreshSchemasStatusMessageTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRefreshSchemasStatusResponseTypeDef

### RefreshSchemasStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.RefreshSchemasStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationConfigsMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationConfigsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationInstanceTaskLogsMessageTypeDef

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationInstanceTaskLogsResponseTypeDef

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstanceTaskLogs
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationInstanceTaskLogTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationInstancesMessagePaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeReplicationInstancesMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationInstancesMessageWaitExtraTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.WaiterConfigTypeDef]


# DescribeReplicationInstancesMessageWaitTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.WaiterConfigTypeDef]


# DescribeReplicationInstancesResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationSubnetGroupsMessagePaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeReplicationSubnetGroupsMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationSubnetGroupsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationSubnetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationTableStatisticsMessageTypeDef

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]


# DescribeReplicationTableStatisticsResponseTypeDef

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTableStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.TableStatisticsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationTaskAssessmentResultsMessagePaginateTypeDef

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeReplicationTaskAssessmentResultsMessageTypeDef

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationTaskAssessmentResultsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTaskAssessmentResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationTaskAssessmentRunsMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationTaskAssessmentRunsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTaskAssessmentRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationTaskIndividualAssessmentsMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationTaskIndividualAssessmentsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTaskIndividualAssessments
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskIndividualAssessmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationTasksMessagePaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### WithoutSettings
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeReplicationTasksMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]


# DescribeReplicationTasksMessageWaitExtraExtraExtraTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.WaiterConfigTypeDef]


# DescribeReplicationTasksMessageWaitExtraExtraTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.WaiterConfigTypeDef]


# DescribeReplicationTasksMessageWaitExtraTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.WaiterConfigTypeDef]


# DescribeReplicationTasksMessageWaitTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### WithoutSettings
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.WaiterConfigTypeDef]


# DescribeReplicationTasksResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationsMessageTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReplicationsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Replications
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.ReplicationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSchemasMessagePaginateTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeSchemasMessageTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeSchemasResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Schemas
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTableStatisticsMessagePaginateTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PaginatorConfigTypeDef]


# DescribeTableStatisticsMessageTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.FilterTypeDef]]


# DescribeTableStatisticsResponseTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TableStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.TableStatisticsTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DmsTransferSettingsTypeDef

### ServiceAccessRoleArn
- **Type**: typing.Optional[str]

### BucketName
- **Type**: typing.Optional[str]


# DocDbDataProviderSettingsTypeDef

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


# DocDbSettingsTypeDef

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


# DynamoDbSettingsTypeDef

### ServiceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ElasticsearchSettingsTypeDef

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


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointSettingTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EndpointTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DynamoDbSettingsTypeDef]

### S3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.S3SettingsTypeDef]

### DmsTransferSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DmsTransferSettingsTypeDef]

### MongoDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MongoDbSettingsTypeDef]

### KinesisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.KinesisSettingsTypeDef]

### KafkaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.KafkaSettingsTypeDef]

### ElasticsearchSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ElasticsearchSettingsTypeDef]

### NeptuneSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.NeptuneSettingsTypeDef]

### RedshiftSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RedshiftSettingsTypeDef]

### PostgreSQLSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PostgreSQLSettingsTypeDef]

### MySQLSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MySQLSettingsTypeDef]

### OracleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.OracleSettingsOutputTypeDef]

### SybaseSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SybaseSettingsTypeDef]

### MicrosoftSQLServerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MicrosoftSQLServerSettingsTypeDef]

### IBMDb2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.IBMDb2SettingsTypeDef]

### DocDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DocDbSettingsTypeDef]

### RedisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RedisSettingsTypeDef]

### GcpMySQLSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.GcpMySQLSettingsTypeDef]

### TimestreamSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestreamSettingsTypeDef]


# EngineVersionTypeDef

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


# ErrorDetailsTypeDef

### defaultErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DefaultErrorDetailsTypeDef]


# EventCategoryGroupTypeDef

### SourceType
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]


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


# EventTypeDef

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


# ExportMetadataModelAssessmentMessageTypeDef

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


# ExportMetadataModelAssessmentResponseTypeDef

### PdfReport
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ExportMetadataModelAssessmentResultEntryTypeDef'>
- **Required**: Yes

### CsvReport
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ExportMetadataModelAssessmentResultEntryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportMetadataModelAssessmentResultEntryTypeDef

### S3ObjectKey
- **Type**: typing.Optional[str]

### ObjectURL
- **Type**: typing.Optional[str]


# ExportSqlDetailsTypeDef

### S3ObjectKey
- **Type**: typing.Optional[str]

### ObjectURL
- **Type**: typing.Optional[str]


# FilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# FleetAdvisorLsaAnalysisResponseTypeDef

### LsaAnalysisId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# FleetAdvisorSchemaObjectResponseTypeDef

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


# GcpMySQLSettingsTypeDef

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


# IBMDb2SettingsTypeDef

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


# IbmDb2LuwDataProviderSettingsTypeDef

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


# IbmDb2zOsDataProviderSettingsTypeDef

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


# ImportCertificateMessageTypeDef

### CertificateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CertificatePem
- **Type**: typing.Optional[str]

### CertificateWallet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.BlobTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]


# ImportCertificateResponseTypeDef

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.CertificateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceProfileTypeDef

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


# InventoryDataTypeDef

### NumberOfDatabases
- **Type**: typing.Optional[int]

### NumberOfSchemas
- **Type**: typing.Optional[int]


# KafkaSettingsTypeDef

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


# KerberosAuthenticationSettingsTypeDef

### KeyCacheSecretId
- **Type**: typing.Optional[str]

### KeyCacheSecretIamArn
- **Type**: typing.Optional[str]

### Krb5FileContents
- **Type**: typing.Optional[str]


# KinesisSettingsTypeDef

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


# LimitationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListTagsForResourceMessageTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceArnList
- **Type**: typing.Optional[typing.Sequence[str]]


# ListTagsForResourceResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MariaDbDataProviderSettingsTypeDef

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]


# MicrosoftSQLServerSettingsTypeDef

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


# MicrosoftSqlServerDataProviderSettingsTypeDef

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


# MigrationProjectTypeDef

### MigrationProjectName
- **Type**: typing.Optional[str]

### MigrationProjectArn
- **Type**: typing.Optional[str]

### MigrationProjectCreationTime
- **Type**: typing.Optional[datetime.datetime]

### SourceDataProviderDescriptors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorTypeDef]]

### TargetDataProviderDescriptors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorTypeDef]]

### InstanceProfileArn
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### TransformationRules
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SchemaConversionApplicationAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SCApplicationAttributesTypeDef]


# ModifyConversionConfigurationMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ConversionConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyConversionConfigurationResponseTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDataMigrationMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.SourceDataSettingUnionTypeDef]]

### TargetDataSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TargetDataSettingTypeDef]]

### NumberOfJobs
- **Type**: typing.Optional[int]

### SelectionRules
- **Type**: typing.Optional[str]


# ModifyDataMigrationResponseTypeDef

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyDataProviderMessageTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DataProviderSettingsTypeDef]


# ModifyDataProviderResponseTypeDef

### DataProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataProviderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyEndpointMessageTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DynamoDbSettingsTypeDef]

### S3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.S3SettingsTypeDef]

### DmsTransferSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DmsTransferSettingsTypeDef]

### MongoDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MongoDbSettingsTypeDef]

### KinesisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.KinesisSettingsTypeDef]

### KafkaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.KafkaSettingsTypeDef]

### ElasticsearchSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ElasticsearchSettingsTypeDef]

### NeptuneSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.NeptuneSettingsTypeDef]

### RedshiftSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RedshiftSettingsTypeDef]

### PostgreSQLSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.PostgreSQLSettingsTypeDef]

### MySQLSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MySQLSettingsTypeDef]

### OracleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.OracleSettingsUnionTypeDef]

### SybaseSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SybaseSettingsTypeDef]

### MicrosoftSQLServerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.MicrosoftSQLServerSettingsTypeDef]

### IBMDb2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.IBMDb2SettingsTypeDef]

### DocDbSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DocDbSettingsTypeDef]

### RedisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RedisSettingsTypeDef]

### ExactSettings
- **Type**: typing.Optional[bool]

### GcpMySQLSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.GcpMySQLSettingsTypeDef]

### TimestreamSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestreamSettingsTypeDef]


# ModifyEndpointResponseTypeDef

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.EndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
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


# ModifyEventSubscriptionResponseTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyInstanceProfileMessageTypeDef

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


# ModifyInstanceProfileResponseTypeDef

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.InstanceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyMigrationProjectMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationProjectName
- **Type**: typing.Optional[str]

### SourceDataProviderDescriptors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorDefinitionTypeDef]]

### TargetDataProviderDescriptors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.DataProviderDescriptorDefinitionTypeDef]]

### InstanceProfileIdentifier
- **Type**: typing.Optional[str]

### TransformationRules
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SchemaConversionApplicationAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SCApplicationAttributesTypeDef]


# ModifyMigrationProjectResponseTypeDef

### MigrationProject
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.MigrationProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyReplicationConfigMessageTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ComputeConfigUnionTypeDef]

### SourceEndpointArn
- **Type**: typing.Optional[str]

### TargetEndpointArn
- **Type**: typing.Optional[str]


# ModifyReplicationConfigResponseTypeDef

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyReplicationInstanceMessageTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.KerberosAuthenticationSettingsTypeDef]


# ModifyReplicationInstanceResponseTypeDef

### ReplicationInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyReplicationSubnetGroupMessageTypeDef

### ReplicationSubnetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ReplicationSubnetGroupDescription
- **Type**: typing.Optional[str]


# ModifyReplicationSubnetGroupResponseTypeDef

### ReplicationSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyReplicationTaskMessageTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]

### TaskData
- **Type**: typing.Optional[str]


# ModifyReplicationTaskResponseTypeDef

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MongoDbDataProviderSettingsTypeDef

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


# MongoDbSettingsTypeDef

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


# MoveReplicationTaskMessageTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# MoveReplicationTaskResponseTypeDef

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MySQLSettingsTypeDef

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


# MySqlDataProviderSettingsTypeDef

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### SslMode
- **Type**: typing.Optional[typing.Literal['none', 'require', 'verify-ca', 'verify-full']]

### CertificateArn
- **Type**: typing.Optional[str]


# NeptuneSettingsTypeDef

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


# OracleDataProviderSettingsTypeDef

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


# OracleSettingsOutputTypeDef

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


# OracleSettingsTypeDef

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


# OracleSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrderableReplicationInstanceTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# PostgreSQLSettingsTypeDef

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


# PostgreSqlDataProviderSettingsTypeDef

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


# PremigrationAssessmentStatusTypeDef

### PremigrationAssessmentRunArn
- **Type**: typing.Optional[str]

### FailOnAssessmentFailure
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### PremigrationAssessmentRunCreationDate
- **Type**: typing.Optional[datetime.datetime]

### AssessmentProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunProgressTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunResultStatisticTypeDef]


# ProvisionDataTypeDef

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


# RdsConfigurationTypeDef

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


# RdsRecommendationTypeDef

### RequirementsToTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RdsRequirementsTypeDef]

### TargetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RdsConfigurationTypeDef]


# RdsRequirementsTypeDef

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


# RebootReplicationInstanceMessageTypeDef

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ForceFailover
- **Type**: typing.Optional[bool]

### ForcePlannedFailover
- **Type**: typing.Optional[bool]


# RebootReplicationInstanceResponseTypeDef

### ReplicationInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecommendationDataTypeDef

### RdsEngine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RdsRecommendationTypeDef]


# RecommendationSettingsTypeDef

### InstanceSizingType
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadType
- **Type**: <class 'str'>
- **Required**: Yes


# RecommendationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RecommendationSettingsTypeDef]

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.RecommendationDataTypeDef]


# RedisSettingsTypeDef

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


# RedshiftDataProviderSettingsTypeDef

### ServerName
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]


# RedshiftSettingsTypeDef

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


# RefreshSchemasMessageTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RefreshSchemasResponseTypeDef

### RefreshSchemasStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.RefreshSchemasStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RefreshSchemasStatusTypeDef

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


# ReloadReplicationTablesMessageTypeDef

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### TablesToReload
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TableToReloadTypeDef]
- **Required**: Yes

### ReloadOption
- **Type**: typing.Optional[typing.Literal['data-reload', 'validate-only']]


# ReloadReplicationTablesResponseTypeDef

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReloadTablesMessageTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TablesToReload
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TableToReloadTypeDef]
- **Required**: Yes

### ReloadOption
- **Type**: typing.Optional[typing.Literal['data-reload', 'validate-only']]


# ReloadTablesResponseTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTagsFromResourceMessageTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReplicationConfigTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ComputeConfigOutputTypeDef]

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


# ReplicationInstanceTaskLogTypeDef

### ReplicationTaskName
- **Type**: typing.Optional[str]

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### ReplicationInstanceTaskLogSize
- **Type**: typing.Optional[int]


# ReplicationInstanceTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.VpcSecurityGroupMembershipTypeDef]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ReplicationSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationSubnetGroupTypeDef]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationPendingModifiedValuesTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.KerberosAuthenticationSettingsTypeDef]


# ReplicationPendingModifiedValuesTypeDef

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


# ReplicationStatsTypeDef

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


# ReplicationSubnetGroupTypeDef

### ReplicationSubnetGroupIdentifier
- **Type**: typing.Optional[str]

### ReplicationSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.SubnetTypeDef]]

### SupportedNetworkTypes
- **Type**: typing.Optional[typing.List[str]]


# ReplicationTaskAssessmentResultTypeDef

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


# ReplicationTaskAssessmentRunProgressTypeDef

### IndividualAssessmentCount
- **Type**: typing.Optional[int]

### IndividualAssessmentCompletedCount
- **Type**: typing.Optional[int]


# ReplicationTaskAssessmentRunResultStatisticTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReplicationTaskAssessmentRunTypeDef

### ReplicationTaskAssessmentRunArn
- **Type**: typing.Optional[str]

### ReplicationTaskArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### ReplicationTaskAssessmentRunCreationDate
- **Type**: typing.Optional[datetime.datetime]

### AssessmentProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunProgressTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunResultStatisticTypeDef]


# ReplicationTaskIndividualAssessmentTypeDef

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


# ReplicationTaskStatsTypeDef

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


# ReplicationTaskTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskStatsTypeDef]

### TaskData
- **Type**: typing.Optional[str]

### TargetReplicationInstanceArn
- **Type**: typing.Optional[str]


# ReplicationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ProvisionDataTypeDef]

### PremigrationAssessmentStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.PremigrationAssessmentStatusTypeDef]]

### StopReason
- **Type**: typing.Optional[str]

### FailureMessages
- **Type**: typing.Optional[typing.List[str]]

### ReplicationStats
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ReplicationStatsTypeDef]

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


# ResourcePendingMaintenanceActionsTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### PendingMaintenanceActionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dms_classes.PendingMaintenanceActionTypeDef]]


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


# RunFleetAdvisorLsaAnalysisResponseTypeDef

### LsaAnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3SettingsTypeDef

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


# SCApplicationAttributesTypeDef

### S3BucketPath
- **Type**: typing.Optional[str]

### S3BucketRoleArn
- **Type**: typing.Optional[str]


# SchemaConversionRequestTypeDef

### Status
- **Type**: typing.Optional[str]

### RequestIdentifier
- **Type**: typing.Optional[str]

### MigrationProjectArn
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ErrorDetailsTypeDef]

### ExportSqlDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ExportSqlDetailsTypeDef]


# SchemaResponseTypeDef

### CodeLineCount
- **Type**: typing.Optional[int]

### CodeSize
- **Type**: typing.Optional[int]

### Complexity
- **Type**: typing.Optional[str]

### Server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.ServerShortInfoResponseTypeDef]

### DatabaseInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.DatabaseShortInfoResponseTypeDef]

### SchemaId
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### OriginalSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.SchemaShortInfoResponseTypeDef]

### Similarity
- **Type**: typing.Optional[float]


# SchemaShortInfoResponseTypeDef

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


# ServerShortInfoResponseTypeDef

### ServerId
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]


# SourceDataSettingOutputTypeDef

### CDCStartPosition
- **Type**: typing.Optional[str]

### CDCStartTime
- **Type**: typing.Optional[datetime.datetime]

### CDCStopTime
- **Type**: typing.Optional[datetime.datetime]

### SlotName
- **Type**: typing.Optional[str]


# SourceDataSettingTypeDef

### CDCStartPosition
- **Type**: typing.Optional[str]

### CDCStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### CDCStopTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### SlotName
- **Type**: typing.Optional[str]


# SourceDataSettingUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartDataMigrationMessageTypeDef

### DataMigrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### StartType
- **Type**: typing.Literal['reload-target', 'resume-processing', 'start-replication']
- **Required**: Yes


# StartDataMigrationResponseTypeDef

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartExtensionPackAssociationMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartExtensionPackAssociationResponseTypeDef

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMetadataModelAssessmentMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionRules
- **Type**: <class 'str'>
- **Required**: Yes


# StartMetadataModelAssessmentResponseTypeDef

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMetadataModelConversionMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionRules
- **Type**: <class 'str'>
- **Required**: Yes


# StartMetadataModelConversionResponseTypeDef

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMetadataModelExportAsScriptMessageTypeDef

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


# StartMetadataModelExportAsScriptResponseTypeDef

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMetadataModelExportToTargetMessageTypeDef

### MigrationProjectIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionRules
- **Type**: <class 'str'>
- **Required**: Yes

### OverwriteExtensionPack
- **Type**: typing.Optional[bool]


# StartMetadataModelExportToTargetResponseTypeDef

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMetadataModelImportMessageTypeDef

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


# StartMetadataModelImportResponseTypeDef

### RequestIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartRecommendationsRequestEntryTypeDef

### DatabaseId
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.RecommendationSettingsTypeDef'>
- **Required**: Yes


# StartRecommendationsRequestTypeDef

### DatabaseId
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.RecommendationSettingsTypeDef'>
- **Required**: Yes


# StartReplicationMessageTypeDef

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### StartReplicationType
- **Type**: <class 'str'>
- **Required**: Yes

### PremigrationAssessmentSettings
- **Type**: typing.Optional[str]

### CdcStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]


# StartReplicationResponseTypeDef

### Replication
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartReplicationTaskAssessmentMessageTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartReplicationTaskAssessmentResponseTypeDef

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartReplicationTaskAssessmentRunMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dms_classes.TagTypeDef]]


# StartReplicationTaskAssessmentRunResponseTypeDef

### ReplicationTaskAssessmentRun
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskAssessmentRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartReplicationTaskMessageTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### StartReplicationTaskType
- **Type**: typing.Literal['reload-target', 'resume-processing', 'start-replication']
- **Required**: Yes

### CdcStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.TimestampTypeDef]

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]


# StartReplicationTaskResponseTypeDef

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDataMigrationMessageTypeDef

### DataMigrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopDataMigrationResponseTypeDef

### DataMigration
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.DataMigrationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopReplicationMessageTypeDef

### ReplicationConfigArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationResponseTypeDef

### Replication
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopReplicationTaskMessageTypeDef

### ReplicationTaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationTaskResponseTypeDef

### ReplicationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ReplicationTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubnetTypeDef

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dms_classes.AvailabilityZoneTypeDef]

### SubnetStatus
- **Type**: typing.Optional[str]


# SupportedEndpointTypeTypeDef

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


# SybaseSettingsTypeDef

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


# TableStatisticsTypeDef

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


# TableToReloadTypeDef

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# TargetDataSettingTypeDef

### TablePreparationMode
- **Type**: typing.Optional[typing.Literal['do-nothing', 'drop-tables-on-target', 'truncate']]


# TestConnectionMessageTypeDef

### ReplicationInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# TestConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestreamSettingsTypeDef

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


# UpdateSubscriptionsToEventBridgeMessageTypeDef

### ForceMove
- **Type**: typing.Optional[bool]


# UpdateSubscriptionsToEventBridgeResponseTypeDef

### Result
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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



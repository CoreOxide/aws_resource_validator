# Firehose Firehose Classes

# AmazonOpenSearchServerlessBufferingHints

### IntervalInSeconds
- **Type**: typing.Optional[int]

### SizeInMBs
- **Type**: typing.Optional[int]


# AmazonOpenSearchServerlessDestinationConfiguration

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration'>
- **Required**: Yes

### CollectionEndpoint
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonOpenSearchServerlessBufferingHints]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonOpenSearchServerlessRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### VpcConfiguration
- **Type**: <class 'NoneType'>


# AmazonOpenSearchServerlessDestinationDescription

### RoleARN
- **Type**: typing.Optional[str]

### CollectionEndpoint
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonOpenSearchServerlessBufferingHints]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonOpenSearchServerlessRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### S3DestinationDescription
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### VpcConfigurationDescription
- **Type**: <class 'NoneType'>


# AmazonOpenSearchServerlessDestinationUpdate

### RoleARN
- **Type**: typing.Optional[str]

### CollectionEndpoint
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonOpenSearchServerlessBufferingHints]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonOpenSearchServerlessRetryOptions]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationUpdate]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>


# AmazonOpenSearchServerlessRetryOptions

### DurationInSeconds
- **Type**: typing.Optional[int]


# AmazonopensearchserviceBufferingHints

### IntervalInSeconds
- **Type**: typing.Optional[int]

### SizeInMBs
- **Type**: typing.Optional[int]


# AmazonopensearchserviceDestinationConfiguration

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration'>
- **Required**: Yes

### DomainARN
- **Type**: typing.Optional[str]

### ClusterEndpoint
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### IndexRotationPeriod
- **Type**: typing.Optional[typing.Literal['NoRotation', 'OneDay', 'OneHour', 'OneMonth', 'OneWeek']]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonopensearchserviceBufferingHints]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonopensearchserviceRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### VpcConfiguration
- **Type**: <class 'NoneType'>

### DocumentIdOptions
- **Type**: <class 'NoneType'>


# AmazonopensearchserviceDestinationDescription

### RoleARN
- **Type**: typing.Optional[str]

### DomainARN
- **Type**: typing.Optional[str]

### ClusterEndpoint
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### IndexRotationPeriod
- **Type**: typing.Optional[typing.Literal['NoRotation', 'OneDay', 'OneHour', 'OneMonth', 'OneWeek']]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonopensearchserviceBufferingHints]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonopensearchserviceRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### S3DestinationDescription
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### VpcConfigurationDescription
- **Type**: <class 'NoneType'>

### DocumentIdOptions
- **Type**: <class 'NoneType'>


# AmazonopensearchserviceDestinationUpdate

### RoleARN
- **Type**: typing.Optional[str]

### DomainARN
- **Type**: typing.Optional[str]

### ClusterEndpoint
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### IndexRotationPeriod
- **Type**: typing.Optional[typing.Literal['NoRotation', 'OneDay', 'OneHour', 'OneMonth', 'OneWeek']]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonopensearchserviceBufferingHints]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.AmazonopensearchserviceRetryOptions]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationUpdate]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### DocumentIdOptions
- **Type**: <class 'NoneType'>


# AmazonopensearchserviceRetryOptions

### DurationInSeconds
- **Type**: typing.Optional[int]


# AuthenticationConfiguration

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### Connectivity
- **Type**: typing.Literal['PRIVATE', 'PUBLIC']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BufferingHints

### SizeInMBs
- **Type**: typing.Optional[int]

### IntervalInSeconds
- **Type**: typing.Optional[int]


# CatalogConfiguration

### CatalogARN
- **Type**: typing.Optional[str]

### WarehouseLocation
- **Type**: typing.Optional[str]


# CloudWatchLoggingOptions

### Enabled
- **Type**: typing.Optional[bool]

### LogGroupName
- **Type**: typing.Optional[str]

### LogStreamName
- **Type**: typing.Optional[str]


# CopyCommand

### DataTableName
- **Type**: <class 'str'>
- **Required**: Yes

### DataTableColumns
- **Type**: typing.Optional[str]

### CopyOptions
- **Type**: typing.Optional[str]


# CreateDeliveryStreamInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamType
- **Type**: typing.Optional[typing.Literal['DatabaseAsSource', 'DirectPut', 'KinesisStreamAsSource', 'MSKAsSource']]

### DirectPutSourceConfiguration
- **Type**: <class 'NoneType'>

### KinesisStreamSourceConfiguration
- **Type**: <class 'NoneType'>

### DeliveryStreamEncryptionConfigurationInput
- **Type**: <class 'NoneType'>

### S3DestinationConfiguration
- **Type**: <class 'NoneType'>

### ExtendedS3DestinationConfiguration
- **Type**: <class 'NoneType'>

### RedshiftDestinationConfiguration
- **Type**: <class 'NoneType'>

### ElasticsearchDestinationConfiguration
- **Type**: <class 'NoneType'>

### AmazonopensearchserviceDestinationConfiguration
- **Type**: <class 'NoneType'>

### SplunkDestinationConfiguration
- **Type**: <class 'NoneType'>

### HttpEndpointDestinationConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.Tag]]

### AmazonOpenSearchServerlessDestinationConfiguration
- **Type**: <class 'NoneType'>

### MSKSourceConfiguration
- **Type**: <class 'NoneType'>

### SnowflakeDestinationConfiguration
- **Type**: <class 'NoneType'>

### IcebergDestinationConfiguration
- **Type**: <class 'NoneType'>

### DatabaseSourceConfiguration
- **Type**: <class 'NoneType'>


# CreateDeliveryStreamOutput

### DeliveryStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.ResponseMetadata'>
- **Required**: Yes


# DataFormatConversionConfiguration

### SchemaConfiguration
- **Type**: <class 'NoneType'>

### InputFormatConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.InputFormatConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.InputFormatConfigurationOutput, NoneType]

### OutputFormatConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.OutputFormatConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.OutputFormatConfigurationOutput, NoneType]

### Enabled
- **Type**: typing.Optional[bool]


# DataFormatConversionConfigurationOutput

### SchemaConfiguration
- **Type**: <class 'NoneType'>

### InputFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.InputFormatConfigurationOutput]

### OutputFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.OutputFormatConfigurationOutput]

### Enabled
- **Type**: typing.Optional[bool]


# DatabaseColumnList

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# DatabaseColumnListOutput

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# DatabaseList

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# DatabaseListOutput

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# DatabaseSnapshotInfo

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### RequestTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RequestedBy
- **Type**: typing.Literal['FIREHOSE', 'USER']
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETE', 'IN_PROGRESS', 'SUSPENDED']
- **Required**: Yes

### FailureDescription
- **Type**: <class 'NoneType'>


# DatabaseSourceAuthenticationConfiguration

### SecretsManagerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.SecretsManagerConfiguration'>
- **Required**: Yes


# DatabaseSourceConfiguration

### Type
- **Type**: typing.Literal['MySQL', 'PostgreSQL']
- **Required**: Yes

### Endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Databases
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseList, aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseListOutput]
- **Required**: Yes

### Tables
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseTableList, aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseTableListOutput]
- **Required**: Yes

### SnapshotWatermarkTable
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseSourceAuthenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseSourceAuthenticationConfiguration'>
- **Required**: Yes

### DatabaseSourceVPCConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseSourceVPCConfiguration'>
- **Required**: Yes

### SSLMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Columns
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseColumnList, aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseColumnListOutput, NoneType]

### SurrogateKeys
- **Type**: typing.Optional[typing.List[str]]


# DatabaseSourceDescription

### Type
- **Type**: typing.Optional[typing.Literal['MySQL', 'PostgreSQL']]

### Endpoint
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### SSLMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Databases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseListOutput]

### Tables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseTableListOutput]

### Columns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseColumnListOutput]

### SurrogateKeys
- **Type**: typing.Optional[typing.List[str]]

### SnapshotWatermarkTable
- **Type**: typing.Optional[str]

### SnapshotInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.DatabaseSnapshotInfo]]

### DatabaseSourceAuthenticationConfiguration
- **Type**: <class 'NoneType'>

### DatabaseSourceVPCConfiguration
- **Type**: <class 'NoneType'>


# DatabaseSourceVPCConfiguration

### VpcEndpointServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# DatabaseTableList

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# DatabaseTableListOutput

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# DeleteDeliveryStreamInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### AllowForceDelete
- **Type**: typing.Optional[bool]


# DeliveryStreamDescription

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATING_FAILED', 'DELETING', 'DELETING_FAILED']
- **Required**: Yes

### DeliveryStreamType
- **Type**: typing.Literal['DatabaseAsSource', 'DirectPut', 'KinesisStreamAsSource', 'MSKAsSource']
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.DestinationDescription]
- **Required**: Yes

### HasMoreDestinations
- **Type**: <class 'bool'>
- **Required**: Yes

### FailureDescription
- **Type**: <class 'NoneType'>

### DeliveryStreamEncryptionConfiguration
- **Type**: <class 'NoneType'>

### CreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SourceDescription]


# DeliveryStreamEncryptionConfiguration

### KeyARN
- **Type**: typing.Optional[str]

### KeyType
- **Type**: typing.Optional[typing.Literal['AWS_OWNED_CMK', 'CUSTOMER_MANAGED_CMK']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'DISABLING_FAILED', 'ENABLED', 'ENABLING', 'ENABLING_FAILED']]

### FailureDescription
- **Type**: <class 'NoneType'>


# DeliveryStreamEncryptionConfigurationInput

### KeyType
- **Type**: typing.Literal['AWS_OWNED_CMK', 'CUSTOMER_MANAGED_CMK']
- **Required**: Yes

### KeyARN
- **Type**: typing.Optional[str]


# DescribeDeliveryStreamInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartDestinationId
- **Type**: typing.Optional[str]


# DescribeDeliveryStreamOutput

### DeliveryStreamDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.DeliveryStreamDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.ResponseMetadata'>
- **Required**: Yes


# Deserializer

### OpenXJsonSerDe
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.OpenXJsonSerDe, aws_resource_validator.pydantic_models.firehose.firehose_classes.OpenXJsonSerDeOutput, NoneType]

### HiveJsonSerDe
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.HiveJsonSerDe, aws_resource_validator.pydantic_models.firehose.firehose_classes.HiveJsonSerDeOutput, NoneType]


# DeserializerOutput

### OpenXJsonSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.OpenXJsonSerDeOutput]

### HiveJsonSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HiveJsonSerDeOutput]


# DestinationDescription

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### S3DestinationDescription
- **Type**: <class 'NoneType'>

### ExtendedS3DestinationDescription
- **Type**: <class 'NoneType'>

### RedshiftDestinationDescription
- **Type**: <class 'NoneType'>

### ElasticsearchDestinationDescription
- **Type**: <class 'NoneType'>

### AmazonopensearchserviceDestinationDescription
- **Type**: <class 'NoneType'>

### SplunkDestinationDescription
- **Type**: <class 'NoneType'>

### HttpEndpointDestinationDescription
- **Type**: <class 'NoneType'>

### SnowflakeDestinationDescription
- **Type**: <class 'NoneType'>

### AmazonOpenSearchServerlessDestinationDescription
- **Type**: <class 'NoneType'>

### IcebergDestinationDescription
- **Type**: <class 'NoneType'>


# DestinationTableConfiguration

### DestinationTableName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### UniqueKeys
- **Type**: typing.Optional[typing.List[str]]

### PartitionSpec
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.PartitionSpec, aws_resource_validator.pydantic_models.firehose.firehose_classes.PartitionSpecOutput, NoneType]

### S3ErrorOutputPrefix
- **Type**: typing.Optional[str]


# DestinationTableConfigurationOutput

### DestinationTableName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### UniqueKeys
- **Type**: typing.Optional[typing.List[str]]

### PartitionSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.PartitionSpecOutput]

### S3ErrorOutputPrefix
- **Type**: typing.Optional[str]


# DirectPutSourceConfiguration

### ThroughputHintInMBs
- **Type**: <class 'int'>
- **Required**: Yes


# DirectPutSourceDescription

### ThroughputHintInMBs
- **Type**: typing.Optional[int]


# DocumentIdOptions

### DefaultDocumentIdFormat
- **Type**: typing.Literal['FIREHOSE_DEFAULT', 'NO_DOCUMENT_ID']
- **Required**: Yes


# DynamicPartitioningConfiguration

### RetryOptions
- **Type**: <class 'NoneType'>

### Enabled
- **Type**: typing.Optional[bool]


# ElasticsearchBufferingHints

### IntervalInSeconds
- **Type**: typing.Optional[int]

### SizeInMBs
- **Type**: typing.Optional[int]


# ElasticsearchDestinationConfiguration

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration'>
- **Required**: Yes

### DomainARN
- **Type**: typing.Optional[str]

### ClusterEndpoint
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### IndexRotationPeriod
- **Type**: typing.Optional[typing.Literal['NoRotation', 'OneDay', 'OneHour', 'OneMonth', 'OneWeek']]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ElasticsearchBufferingHints]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ElasticsearchRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### VpcConfiguration
- **Type**: <class 'NoneType'>

### DocumentIdOptions
- **Type**: <class 'NoneType'>


# ElasticsearchDestinationDescription

### RoleARN
- **Type**: typing.Optional[str]

### DomainARN
- **Type**: typing.Optional[str]

### ClusterEndpoint
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### IndexRotationPeriod
- **Type**: typing.Optional[typing.Literal['NoRotation', 'OneDay', 'OneHour', 'OneMonth', 'OneWeek']]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ElasticsearchBufferingHints]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ElasticsearchRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### S3DestinationDescription
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### VpcConfigurationDescription
- **Type**: <class 'NoneType'>

### DocumentIdOptions
- **Type**: <class 'NoneType'>


# ElasticsearchDestinationUpdate

### RoleARN
- **Type**: typing.Optional[str]

### DomainARN
- **Type**: typing.Optional[str]

### ClusterEndpoint
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### IndexRotationPeriod
- **Type**: typing.Optional[typing.Literal['NoRotation', 'OneDay', 'OneHour', 'OneMonth', 'OneWeek']]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ElasticsearchBufferingHints]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ElasticsearchRetryOptions]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationUpdate]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### DocumentIdOptions
- **Type**: <class 'NoneType'>


# ElasticsearchRetryOptions

### DurationInSeconds
- **Type**: typing.Optional[int]


# EncryptionConfiguration

### NoEncryptionConfig
- **Type**: typing.Optional[typing.Literal['NoEncryption']]

### KMSEncryptionConfig
- **Type**: <class 'NoneType'>


# ExtendedS3DestinationConfiguration

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: <class 'NoneType'>

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration]

### DataFormatConversionConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.DataFormatConversionConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.DataFormatConversionConfigurationOutput, NoneType]

### DynamicPartitioningConfiguration
- **Type**: <class 'NoneType'>

### FileExtension
- **Type**: typing.Optional[str]

### CustomTimeZone
- **Type**: typing.Optional[str]


# ExtendedS3DestinationDescription

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### BufferingHints
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.BufferingHints'>
- **Required**: Yes

### CompressionFormat
- **Type**: typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.EncryptionConfiguration'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationDescription]

### DataFormatConversionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.DataFormatConversionConfigurationOutput]

### DynamicPartitioningConfiguration
- **Type**: <class 'NoneType'>

### FileExtension
- **Type**: typing.Optional[str]

### CustomTimeZone
- **Type**: typing.Optional[str]


# ExtendedS3DestinationUpdate

### RoleARN
- **Type**: typing.Optional[str]

### BucketARN
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: <class 'NoneType'>

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationUpdate]

### DataFormatConversionConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.DataFormatConversionConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.DataFormatConversionConfigurationOutput, NoneType]

### DynamicPartitioningConfiguration
- **Type**: <class 'NoneType'>

### FileExtension
- **Type**: typing.Optional[str]

### CustomTimeZone
- **Type**: typing.Optional[str]


# FailureDescription

### Type
- **Type**: typing.Literal['CREATE_ENI_FAILED', 'CREATE_KMS_GRANT_FAILED', 'DELETE_ENI_FAILED', 'DISABLED_KMS_KEY', 'ENI_ACCESS_DENIED', 'INVALID_KMS_KEY', 'KMS_ACCESS_DENIED', 'KMS_KEY_NOT_FOUND', 'KMS_OPT_IN_REQUIRED', 'RETIRE_KMS_GRANT_FAILED', 'SECURITY_GROUP_ACCESS_DENIED', 'SECURITY_GROUP_NOT_FOUND', 'SUBNET_ACCESS_DENIED', 'SUBNET_NOT_FOUND', 'UNKNOWN_ERROR', 'VPC_ENDPOINT_SERVICE_NAME_NOT_FOUND', 'VPC_INTERFACE_ENDPOINT_SERVICE_ACCESS_DENIED']
- **Required**: Yes

### Details
- **Type**: <class 'str'>
- **Required**: Yes


# HiveJsonSerDe

### TimestampFormats
- **Type**: typing.Optional[typing.List[str]]


# HiveJsonSerDeOutput

### TimestampFormats
- **Type**: typing.Optional[typing.List[str]]


# HttpEndpointBufferingHints

### SizeInMBs
- **Type**: typing.Optional[int]

### IntervalInSeconds
- **Type**: typing.Optional[int]


# HttpEndpointCommonAttribute

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# HttpEndpointConfiguration

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### AccessKey
- **Type**: typing.Optional[str]


# HttpEndpointDescription

### Url
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# HttpEndpointDestinationConfiguration

### EndpointConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointConfiguration'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration'>
- **Required**: Yes

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointBufferingHints]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### RequestConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointRequestConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointRequestConfigurationOutput, NoneType]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>


# HttpEndpointDestinationDescription

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointDescription]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointBufferingHints]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### RequestConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointRequestConfigurationOutput]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### S3DestinationDescription
- **Type**: <class 'NoneType'>

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>


# HttpEndpointDestinationUpdate

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointConfiguration]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointBufferingHints]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### RequestConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointRequestConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointRequestConfigurationOutput, NoneType]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationUpdate]

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>


# HttpEndpointRequestConfiguration

### ContentEncoding
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### CommonAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointCommonAttribute]]


# HttpEndpointRequestConfigurationOutput

### ContentEncoding
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### CommonAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.HttpEndpointCommonAttribute]]


# HttpEndpointRetryOptions

### DurationInSeconds
- **Type**: typing.Optional[int]


# IcebergDestinationConfiguration

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.CatalogConfiguration'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration'>
- **Required**: Yes

### DestinationTableConfigurationList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.DestinationTableConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.DestinationTableConfigurationOutput]]]

### SchemaEvolutionConfiguration
- **Type**: <class 'NoneType'>

### TableCreationConfiguration
- **Type**: <class 'NoneType'>

### BufferingHints
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### RetryOptions
- **Type**: <class 'NoneType'>

### AppendOnly
- **Type**: typing.Optional[bool]


# IcebergDestinationDescription

### DestinationTableConfigurationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.DestinationTableConfigurationOutput]]

### SchemaEvolutionConfiguration
- **Type**: <class 'NoneType'>

### TableCreationConfiguration
- **Type**: <class 'NoneType'>

### BufferingHints
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### RetryOptions
- **Type**: <class 'NoneType'>

### RoleARN
- **Type**: typing.Optional[str]

### AppendOnly
- **Type**: typing.Optional[bool]

### CatalogConfiguration
- **Type**: <class 'NoneType'>

### S3DestinationDescription
- **Type**: <class 'NoneType'>


# IcebergDestinationUpdate

### DestinationTableConfigurationList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.DestinationTableConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.DestinationTableConfigurationOutput]]]

### SchemaEvolutionConfiguration
- **Type**: <class 'NoneType'>

### TableCreationConfiguration
- **Type**: <class 'NoneType'>

### BufferingHints
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### RetryOptions
- **Type**: <class 'NoneType'>

### RoleARN
- **Type**: typing.Optional[str]

### AppendOnly
- **Type**: typing.Optional[bool]

### CatalogConfiguration
- **Type**: <class 'NoneType'>

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration]


# InputFormatConfiguration

### Deserializer
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.Deserializer, aws_resource_validator.pydantic_models.firehose.firehose_classes.DeserializerOutput, NoneType]


# InputFormatConfigurationOutput

### Deserializer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.DeserializerOutput]


# KMSEncryptionConfig

### AWSKMSKeyARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamSourceConfiguration

### KinesisStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamSourceDescription

### KinesisStreamARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### DeliveryStartTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ListDeliveryStreamsInput

### Limit
- **Type**: typing.Optional[int]

### DeliveryStreamType
- **Type**: typing.Optional[typing.Literal['DatabaseAsSource', 'DirectPut', 'KinesisStreamAsSource', 'MSKAsSource']]

### ExclusiveStartDeliveryStreamName
- **Type**: typing.Optional[str]


# ListDeliveryStreamsOutput

### DeliveryStreamNames
- **Type**: typing.List[str]
- **Required**: Yes

### HasMoreDeliveryStreams
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForDeliveryStreamInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### ExclusiveStartTagKey
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTagsForDeliveryStreamOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.Tag]
- **Required**: Yes

### HasMoreTags
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.ResponseMetadata'>
- **Required**: Yes


# MSKSourceConfiguration

### MSKClusterARN
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.AuthenticationConfiguration'>
- **Required**: Yes

### ReadFromTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# MSKSourceDescription

### MSKClusterARN
- **Type**: typing.Optional[str]

### TopicName
- **Type**: typing.Optional[str]

### AuthenticationConfiguration
- **Type**: <class 'NoneType'>

### DeliveryStartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ReadFromTimestamp
- **Type**: typing.Optional[datetime.datetime]


# OpenXJsonSerDe

### ConvertDotsInJsonKeysToUnderscores
- **Type**: typing.Optional[bool]

### CaseInsensitive
- **Type**: typing.Optional[bool]

### ColumnToJsonKeyMappings
- **Type**: typing.Optional[typing.Dict[str, str]]


# OpenXJsonSerDeOutput

### ConvertDotsInJsonKeysToUnderscores
- **Type**: typing.Optional[bool]

### CaseInsensitive
- **Type**: typing.Optional[bool]

### ColumnToJsonKeyMappings
- **Type**: typing.Optional[typing.Dict[str, str]]


# OrcSerDe

### StripeSizeBytes
- **Type**: typing.Optional[int]

### BlockSizeBytes
- **Type**: typing.Optional[int]

### RowIndexStride
- **Type**: typing.Optional[int]

### EnablePadding
- **Type**: typing.Optional[bool]

### PaddingTolerance
- **Type**: typing.Optional[float]

### Compression
- **Type**: typing.Optional[typing.Literal['NONE', 'SNAPPY', 'ZLIB']]

### BloomFilterColumns
- **Type**: typing.Optional[typing.List[str]]

### BloomFilterFalsePositiveProbability
- **Type**: typing.Optional[float]

### DictionaryKeyThreshold
- **Type**: typing.Optional[float]

### FormatVersion
- **Type**: typing.Optional[typing.Literal['V0_11', 'V0_12']]


# OrcSerDeOutput

### StripeSizeBytes
- **Type**: typing.Optional[int]

### BlockSizeBytes
- **Type**: typing.Optional[int]

### RowIndexStride
- **Type**: typing.Optional[int]

### EnablePadding
- **Type**: typing.Optional[bool]

### PaddingTolerance
- **Type**: typing.Optional[float]

### Compression
- **Type**: typing.Optional[typing.Literal['NONE', 'SNAPPY', 'ZLIB']]

### BloomFilterColumns
- **Type**: typing.Optional[typing.List[str]]

### BloomFilterFalsePositiveProbability
- **Type**: typing.Optional[float]

### DictionaryKeyThreshold
- **Type**: typing.Optional[float]

### FormatVersion
- **Type**: typing.Optional[typing.Literal['V0_11', 'V0_12']]


# OutputFormatConfiguration

### Serializer
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.Serializer, aws_resource_validator.pydantic_models.firehose.firehose_classes.SerializerOutput, NoneType]


# OutputFormatConfigurationOutput

### Serializer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SerializerOutput]


# ParquetSerDe

### BlockSizeBytes
- **Type**: typing.Optional[int]

### PageSizeBytes
- **Type**: typing.Optional[int]

### Compression
- **Type**: typing.Optional[typing.Literal['GZIP', 'SNAPPY', 'UNCOMPRESSED']]

### EnableDictionaryCompression
- **Type**: typing.Optional[bool]

### MaxPaddingBytes
- **Type**: typing.Optional[int]

### WriterVersion
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]


# PartitionField

### SourceName
- **Type**: <class 'str'>
- **Required**: Yes


# PartitionSpec

### Identity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.PartitionField]]


# PartitionSpecOutput

### Identity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.PartitionField]]


# ProcessingConfiguration

### Enabled
- **Type**: typing.Optional[bool]

### Processors
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.Processor, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessorOutput]]]


# ProcessingConfigurationOutput

### Enabled
- **Type**: typing.Optional[bool]

### Processors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessorOutput]]


# Processor

### Type
- **Type**: typing.Literal['AppendDelimiterToRecord', 'CloudWatchLogProcessing', 'Decompression', 'Lambda', 'MetadataExtraction', 'RecordDeAggregation']
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessorParameter]]


# ProcessorOutput

### Type
- **Type**: typing.Literal['AppendDelimiterToRecord', 'CloudWatchLogProcessing', 'Decompression', 'Lambda', 'MetadataExtraction', 'RecordDeAggregation']
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessorParameter]]


# ProcessorParameter

### ParameterName
- **Type**: typing.Literal['BufferIntervalInSeconds', 'BufferSizeInMBs', 'CompressionFormat', 'DataMessageExtraction', 'Delimiter', 'JsonParsingEngine', 'LambdaArn', 'MetadataExtractionQuery', 'NumberOfRetries', 'RoleArn', 'SubRecordType']
- **Required**: Yes

### ParameterValue
- **Type**: <class 'str'>
- **Required**: Yes


# PutRecordBatchInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.Record]
- **Required**: Yes


# PutRecordBatchOutput

### FailedPutCount
- **Type**: <class 'int'>
- **Required**: Yes

### Encrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### RequestResponses
- **Type**: typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.PutRecordBatchResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.ResponseMetadata'>
- **Required**: Yes


# PutRecordBatchResponseEntry

### RecordId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# PutRecordInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Record
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.Record'>
- **Required**: Yes


# PutRecordOutput

### RecordId
- **Type**: <class 'str'>
- **Required**: Yes

### Encrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.ResponseMetadata'>
- **Required**: Yes


# Record

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes


# RedshiftDestinationConfiguration

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterJDBCURL
- **Type**: <class 'str'>
- **Required**: Yes

### CopyCommand
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.CopyCommand'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration'>
- **Required**: Yes

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.RedshiftRetryOptions]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>


# RedshiftDestinationDescription

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterJDBCURL
- **Type**: <class 'str'>
- **Required**: Yes

### CopyCommand
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.CopyCommand'>
- **Required**: Yes

### S3DestinationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationDescription'>
- **Required**: Yes

### Username
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.RedshiftRetryOptions]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationDescription]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>


# RedshiftDestinationUpdate

### RoleARN
- **Type**: typing.Optional[str]

### ClusterJDBCURL
- **Type**: typing.Optional[str]

### CopyCommand
- **Type**: <class 'NoneType'>

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.RedshiftRetryOptions]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationUpdate]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationUpdate]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>


# RedshiftRetryOptions

### DurationInSeconds
- **Type**: typing.Optional[int]


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


# RetryOptions

### DurationInSeconds
- **Type**: typing.Optional[int]


# S3DestinationConfiguration

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: <class 'NoneType'>

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>


# S3DestinationDescription

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### BufferingHints
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.BufferingHints'>
- **Required**: Yes

### CompressionFormat
- **Type**: typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.EncryptionConfiguration'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>


# S3DestinationUpdate

### RoleARN
- **Type**: typing.Optional[str]

### BucketARN
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: <class 'NoneType'>

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>


# SchemaConfiguration

### RoleARN
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# SchemaEvolutionConfiguration

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SecretsManagerConfiguration

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SecretARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# Serializer

### ParquetSerDe
- **Type**: <class 'NoneType'>

### OrcSerDe
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.OrcSerDe, aws_resource_validator.pydantic_models.firehose.firehose_classes.OrcSerDeOutput, NoneType]


# SerializerOutput

### ParquetSerDe
- **Type**: <class 'NoneType'>

### OrcSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.OrcSerDeOutput]


# SnowflakeBufferingHints

### SizeInMBs
- **Type**: typing.Optional[int]

### IntervalInSeconds
- **Type**: typing.Optional[int]


# SnowflakeDestinationConfiguration

### AccountUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### Table
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration'>
- **Required**: Yes

### PrivateKey
- **Type**: typing.Optional[str]

### KeyPassphrase
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[str]

### SnowflakeRoleConfiguration
- **Type**: <class 'NoneType'>

### DataLoadingOption
- **Type**: typing.Optional[typing.Literal['JSON_MAPPING', 'VARIANT_CONTENT_AND_METADATA_MAPPING', 'VARIANT_CONTENT_MAPPING']]

### MetaDataColumnName
- **Type**: typing.Optional[str]

### ContentColumnName
- **Type**: typing.Optional[str]

### SnowflakeVpcConfiguration
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SnowflakeRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SnowflakeBufferingHints]


# SnowflakeDestinationDescription

### AccountUrl
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]

### SnowflakeRoleConfiguration
- **Type**: <class 'NoneType'>

### DataLoadingOption
- **Type**: typing.Optional[typing.Literal['JSON_MAPPING', 'VARIANT_CONTENT_AND_METADATA_MAPPING', 'VARIANT_CONTENT_MAPPING']]

### MetaDataColumnName
- **Type**: typing.Optional[str]

### ContentColumnName
- **Type**: typing.Optional[str]

### SnowflakeVpcConfiguration
- **Type**: <class 'NoneType'>

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SnowflakeRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### S3DestinationDescription
- **Type**: <class 'NoneType'>

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SnowflakeBufferingHints]


# SnowflakeDestinationUpdate

### AccountUrl
- **Type**: typing.Optional[str]

### PrivateKey
- **Type**: typing.Optional[str]

### KeyPassphrase
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]

### SnowflakeRoleConfiguration
- **Type**: <class 'NoneType'>

### DataLoadingOption
- **Type**: typing.Optional[typing.Literal['JSON_MAPPING', 'VARIANT_CONTENT_AND_METADATA_MAPPING', 'VARIANT_CONTENT_MAPPING']]

### MetaDataColumnName
- **Type**: typing.Optional[str]

### ContentColumnName
- **Type**: typing.Optional[str]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SnowflakeRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationUpdate]

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SnowflakeBufferingHints]


# SnowflakeRetryOptions

### DurationInSeconds
- **Type**: typing.Optional[int]


# SnowflakeRoleConfiguration

### Enabled
- **Type**: typing.Optional[bool]

### SnowflakeRole
- **Type**: typing.Optional[str]


# SnowflakeVpcConfiguration

### PrivateLinkVpceId
- **Type**: <class 'str'>
- **Required**: Yes


# SourceDescription

### DirectPutSourceDescription
- **Type**: <class 'NoneType'>

### KinesisStreamSourceDescription
- **Type**: <class 'NoneType'>

### MSKSourceDescription
- **Type**: <class 'NoneType'>

### DatabaseSourceDescription
- **Type**: <class 'NoneType'>


# SplunkBufferingHints

### IntervalInSeconds
- **Type**: typing.Optional[int]

### SizeInMBs
- **Type**: typing.Optional[int]


# SplunkDestinationConfiguration

### HECEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### HECEndpointType
- **Type**: typing.Literal['Event', 'Raw']
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationConfiguration'>
- **Required**: Yes

### HECToken
- **Type**: typing.Optional[str]

### HECAcknowledgmentTimeoutInSeconds
- **Type**: typing.Optional[int]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SplunkRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllEvents', 'FailedEventsOnly']]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SplunkBufferingHints]

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>


# SplunkDestinationDescription

### HECEndpoint
- **Type**: typing.Optional[str]

### HECEndpointType
- **Type**: typing.Optional[typing.Literal['Event', 'Raw']]

### HECToken
- **Type**: typing.Optional[str]

### HECAcknowledgmentTimeoutInSeconds
- **Type**: typing.Optional[int]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SplunkRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllEvents', 'FailedEventsOnly']]

### S3DestinationDescription
- **Type**: <class 'NoneType'>

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SplunkBufferingHints]

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>


# SplunkDestinationUpdate

### HECEndpoint
- **Type**: typing.Optional[str]

### HECEndpointType
- **Type**: typing.Optional[typing.Literal['Event', 'Raw']]

### HECToken
- **Type**: typing.Optional[str]

### HECAcknowledgmentTimeoutInSeconds
- **Type**: typing.Optional[int]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SplunkRetryOptions]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllEvents', 'FailedEventsOnly']]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.S3DestinationUpdate]

### ProcessingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfiguration, aws_resource_validator.pydantic_models.firehose.firehose_classes.ProcessingConfigurationOutput, NoneType]

### CloudWatchLoggingOptions
- **Type**: <class 'NoneType'>

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose.firehose_classes.SplunkBufferingHints]

### SecretsManagerConfiguration
- **Type**: <class 'NoneType'>


# SplunkRetryOptions

### DurationInSeconds
- **Type**: typing.Optional[int]


# StartDeliveryStreamEncryptionInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamEncryptionConfigurationInput
- **Type**: <class 'NoneType'>


# StopDeliveryStreamEncryptionInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# TableCreationConfiguration

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagDeliveryStreamInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.firehose.firehose_classes.Tag]
- **Required**: Yes


# UntagDeliveryStreamInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDestinationInput

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentDeliveryStreamVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### S3DestinationUpdate
- **Type**: <class 'NoneType'>

### ExtendedS3DestinationUpdate
- **Type**: <class 'NoneType'>

### RedshiftDestinationUpdate
- **Type**: <class 'NoneType'>

### ElasticsearchDestinationUpdate
- **Type**: <class 'NoneType'>

### AmazonopensearchserviceDestinationUpdate
- **Type**: <class 'NoneType'>

### SplunkDestinationUpdate
- **Type**: <class 'NoneType'>

### HttpEndpointDestinationUpdate
- **Type**: <class 'NoneType'>

### AmazonOpenSearchServerlessDestinationUpdate
- **Type**: <class 'NoneType'>

### SnowflakeDestinationUpdate
- **Type**: <class 'NoneType'>

### IcebergDestinationUpdate
- **Type**: <class 'NoneType'>


# VpcConfiguration

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigurationDescription

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes



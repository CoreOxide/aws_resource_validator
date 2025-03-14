# Firehose Classes

# AmazonOpenSearchServerlessBufferingHintsTypeDef

### IntervalInSeconds
- **Type**: typing.Optional[int]

### SizeInMBs
- **Type**: typing.Optional[int]


# AmazonOpenSearchServerlessDestinationConfigurationTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef'>
- **Required**: Yes

### CollectionEndpoint
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonOpenSearchServerlessBufferingHintsTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonOpenSearchServerlessRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.VpcConfigurationTypeDef]


# AmazonOpenSearchServerlessDestinationDescriptionTypeDef

### RoleARN
- **Type**: typing.Optional[str]

### CollectionEndpoint
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonOpenSearchServerlessBufferingHintsTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonOpenSearchServerlessRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### S3DestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationOutputTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### VpcConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.VpcConfigurationDescriptionTypeDef]


# AmazonOpenSearchServerlessDestinationUpdateTypeDef

### RoleARN
- **Type**: typing.Optional[str]

### CollectionEndpoint
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonOpenSearchServerlessBufferingHintsTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonOpenSearchServerlessRetryOptionsTypeDef]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]


# AmazonOpenSearchServerlessRetryOptionsTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]


# AmazonopensearchserviceBufferingHintsTypeDef

### IntervalInSeconds
- **Type**: typing.Optional[int]

### SizeInMBs
- **Type**: typing.Optional[int]


# AmazonopensearchserviceDestinationConfigurationTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonopensearchserviceBufferingHintsTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonopensearchserviceRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.VpcConfigurationTypeDef]

### DocumentIdOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DocumentIdOptionsTypeDef]


# AmazonopensearchserviceDestinationDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonopensearchserviceBufferingHintsTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonopensearchserviceRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### S3DestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationOutputTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### VpcConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.VpcConfigurationDescriptionTypeDef]

### DocumentIdOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DocumentIdOptionsTypeDef]


# AmazonopensearchserviceDestinationUpdateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonopensearchserviceBufferingHintsTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonopensearchserviceRetryOptionsTypeDef]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### DocumentIdOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DocumentIdOptionsTypeDef]


# AmazonopensearchserviceRetryOptionsTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]


# AuthenticationConfigurationTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### Connectivity
- **Type**: typing.Literal['PRIVATE', 'PUBLIC']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BufferingHintsTypeDef

### SizeInMBs
- **Type**: typing.Optional[int]

### IntervalInSeconds
- **Type**: typing.Optional[int]


# CatalogConfigurationTypeDef

### CatalogARN
- **Type**: typing.Optional[str]

### WarehouseLocation
- **Type**: typing.Optional[str]


# CloudWatchLoggingOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### LogGroupName
- **Type**: typing.Optional[str]

### LogStreamName
- **Type**: typing.Optional[str]


# CopyCommandTypeDef

### DataTableName
- **Type**: <class 'str'>
- **Required**: Yes

### DataTableColumns
- **Type**: typing.Optional[str]

### CopyOptions
- **Type**: typing.Optional[str]


# CreateDeliveryStreamInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamType
- **Type**: typing.Optional[typing.Literal['DatabaseAsSource', 'DirectPut', 'KinesisStreamAsSource', 'MSKAsSource']]

### DirectPutSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DirectPutSourceConfigurationTypeDef]

### KinesisStreamSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.KinesisStreamSourceConfigurationTypeDef]

### DeliveryStreamEncryptionConfigurationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DeliveryStreamEncryptionConfigurationInputTypeDef]

### S3DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef]

### ExtendedS3DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ExtendedS3DestinationConfigurationTypeDef]

### RedshiftDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RedshiftDestinationConfigurationTypeDef]

### ElasticsearchDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ElasticsearchDestinationConfigurationTypeDef]

### AmazonopensearchserviceDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonopensearchserviceDestinationConfigurationTypeDef]

### SplunkDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SplunkDestinationConfigurationTypeDef]

### HttpEndpointDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointDestinationConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.firehose_classes.TagTypeDef]]

### AmazonOpenSearchServerlessDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonOpenSearchServerlessDestinationConfigurationTypeDef]

### MSKSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.MSKSourceConfigurationTypeDef]

### SnowflakeDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeDestinationConfigurationTypeDef]

### IcebergDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.IcebergDestinationConfigurationTypeDef]

### DatabaseSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DatabaseSourceConfigurationTypeDef]


# CreateDeliveryStreamOutputTypeDef

### DeliveryStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataFormatConversionConfigurationOutputTypeDef

### SchemaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SchemaConfigurationTypeDef]

### InputFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.InputFormatConfigurationOutputTypeDef]

### OutputFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.OutputFormatConfigurationOutputTypeDef]

### Enabled
- **Type**: typing.Optional[bool]


# DataFormatConversionConfigurationTypeDef

### SchemaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SchemaConfigurationTypeDef]

### InputFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.InputFormatConfigurationUnionTypeDef]

### OutputFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.OutputFormatConfigurationUnionTypeDef]

### Enabled
- **Type**: typing.Optional[bool]


# DataFormatConversionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatabaseColumnListOutputTypeDef

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# DatabaseColumnListTypeDef

### Include
- **Type**: typing.Optional[typing.Sequence[str]]

### Exclude
- **Type**: typing.Optional[typing.Sequence[str]]


# DatabaseListOutputTypeDef

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# DatabaseListTypeDef

### Include
- **Type**: typing.Optional[typing.Sequence[str]]

### Exclude
- **Type**: typing.Optional[typing.Sequence[str]]


# DatabaseSnapshotInfoTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.FailureDescriptionTypeDef]


# DatabaseSourceAuthenticationConfigurationTypeDef

### SecretsManagerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef'>
- **Required**: Yes


# DatabaseSourceConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatabaseSourceDescriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatabaseSourceVPCConfigurationTypeDef

### VpcEndpointServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# DatabaseTableListOutputTypeDef

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# DatabaseTableListTypeDef

### Include
- **Type**: typing.Optional[typing.Sequence[str]]

### Exclude
- **Type**: typing.Optional[typing.Sequence[str]]


# DeleteDeliveryStreamInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### AllowForceDelete
- **Type**: typing.Optional[bool]


# DeliveryStreamDescriptionTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.firehose_classes.DestinationDescriptionTypeDef]
- **Required**: Yes

### HasMoreDestinations
- **Type**: <class 'bool'>
- **Required**: Yes

### FailureDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.FailureDescriptionTypeDef]

### DeliveryStreamEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DeliveryStreamEncryptionConfigurationTypeDef]

### CreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SourceDescriptionTypeDef]


# DeliveryStreamEncryptionConfigurationInputTypeDef

### KeyType
- **Type**: typing.Literal['AWS_OWNED_CMK', 'CUSTOMER_MANAGED_CMK']
- **Required**: Yes

### KeyARN
- **Type**: typing.Optional[str]


# DeliveryStreamEncryptionConfigurationTypeDef

### KeyARN
- **Type**: typing.Optional[str]

### KeyType
- **Type**: typing.Optional[typing.Literal['AWS_OWNED_CMK', 'CUSTOMER_MANAGED_CMK']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'DISABLING_FAILED', 'ENABLED', 'ENABLING', 'ENABLING_FAILED']]

### FailureDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.FailureDescriptionTypeDef]


# DescribeDeliveryStreamInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartDestinationId
- **Type**: typing.Optional[str]


# DescribeDeliveryStreamOutputTypeDef

### DeliveryStreamDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.DeliveryStreamDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeserializerOutputTypeDef

### OpenXJsonSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.OpenXJsonSerDeOutputTypeDef]

### HiveJsonSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HiveJsonSerDeOutputTypeDef]


# DeserializerTypeDef

### OpenXJsonSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.OpenXJsonSerDeUnionTypeDef]

### HiveJsonSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HiveJsonSerDeUnionTypeDef]


# DeserializerUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DestinationDescriptionTypeDef

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### S3DestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]

### ExtendedS3DestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ExtendedS3DestinationDescriptionTypeDef]

### RedshiftDestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RedshiftDestinationDescriptionTypeDef]

### ElasticsearchDestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ElasticsearchDestinationDescriptionTypeDef]

### AmazonopensearchserviceDestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonopensearchserviceDestinationDescriptionTypeDef]

### SplunkDestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SplunkDestinationDescriptionTypeDef]

### HttpEndpointDestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointDestinationDescriptionTypeDef]

### SnowflakeDestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeDestinationDescriptionTypeDef]

### AmazonOpenSearchServerlessDestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonOpenSearchServerlessDestinationDescriptionTypeDef]

### IcebergDestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.IcebergDestinationDescriptionTypeDef]


# DestinationTableConfigurationOutputTypeDef

### DestinationTableName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### UniqueKeys
- **Type**: typing.Optional[typing.List[str]]

### PartitionSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.PartitionSpecOutputTypeDef]

### S3ErrorOutputPrefix
- **Type**: typing.Optional[str]


# DestinationTableConfigurationTypeDef

### DestinationTableName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### UniqueKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### PartitionSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.PartitionSpecUnionTypeDef]

### S3ErrorOutputPrefix
- **Type**: typing.Optional[str]


# DestinationTableConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DirectPutSourceConfigurationTypeDef

### ThroughputHintInMBs
- **Type**: <class 'int'>
- **Required**: Yes


# DirectPutSourceDescriptionTypeDef

### ThroughputHintInMBs
- **Type**: typing.Optional[int]


# DocumentIdOptionsTypeDef

### DefaultDocumentIdFormat
- **Type**: typing.Literal['FIREHOSE_DEFAULT', 'NO_DOCUMENT_ID']
- **Required**: Yes


# DynamicPartitioningConfigurationTypeDef

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RetryOptionsTypeDef]

### Enabled
- **Type**: typing.Optional[bool]


# ElasticsearchBufferingHintsTypeDef

### IntervalInSeconds
- **Type**: typing.Optional[int]

### SizeInMBs
- **Type**: typing.Optional[int]


# ElasticsearchDestinationConfigurationTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ElasticsearchBufferingHintsTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ElasticsearchRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.VpcConfigurationTypeDef]

### DocumentIdOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DocumentIdOptionsTypeDef]


# ElasticsearchDestinationDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ElasticsearchBufferingHintsTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ElasticsearchRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllDocuments', 'FailedDocumentsOnly']]

### S3DestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationOutputTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### VpcConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.VpcConfigurationDescriptionTypeDef]

### DocumentIdOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DocumentIdOptionsTypeDef]


# ElasticsearchDestinationUpdateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ElasticsearchBufferingHintsTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ElasticsearchRetryOptionsTypeDef]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### DocumentIdOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DocumentIdOptionsTypeDef]


# ElasticsearchRetryOptionsTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]


# EncryptionConfigurationTypeDef

### NoEncryptionConfig
- **Type**: typing.Optional[typing.Literal['NoEncryption']]

### KMSEncryptionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.KMSEncryptionConfigTypeDef]


# ExtendedS3DestinationConfigurationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.BufferingHintsTypeDef]

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.EncryptionConfigurationTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef]

### DataFormatConversionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DataFormatConversionConfigurationUnionTypeDef]

### DynamicPartitioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DynamicPartitioningConfigurationTypeDef]

### FileExtension
- **Type**: typing.Optional[str]

### CustomTimeZone
- **Type**: typing.Optional[str]


# ExtendedS3DestinationDescriptionTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### BufferingHints
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.BufferingHintsTypeDef'>
- **Required**: Yes

### CompressionFormat
- **Type**: typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.EncryptionConfigurationTypeDef'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationOutputTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]

### DataFormatConversionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DataFormatConversionConfigurationOutputTypeDef]

### DynamicPartitioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DynamicPartitioningConfigurationTypeDef]

### FileExtension
- **Type**: typing.Optional[str]

### CustomTimeZone
- **Type**: typing.Optional[str]


# ExtendedS3DestinationUpdateTypeDef

### RoleARN
- **Type**: typing.Optional[str]

### BucketARN
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.BufferingHintsTypeDef]

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.EncryptionConfigurationTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### DataFormatConversionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DataFormatConversionConfigurationUnionTypeDef]

### DynamicPartitioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DynamicPartitioningConfigurationTypeDef]

### FileExtension
- **Type**: typing.Optional[str]

### CustomTimeZone
- **Type**: typing.Optional[str]


# FailureDescriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HiveJsonSerDeOutputTypeDef

### TimestampFormats
- **Type**: typing.Optional[typing.List[str]]


# HiveJsonSerDeTypeDef

### TimestampFormats
- **Type**: typing.Optional[typing.Sequence[str]]


# HiveJsonSerDeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HttpEndpointBufferingHintsTypeDef

### SizeInMBs
- **Type**: typing.Optional[int]

### IntervalInSeconds
- **Type**: typing.Optional[int]


# HttpEndpointCommonAttributeTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# HttpEndpointConfigurationTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### AccessKey
- **Type**: typing.Optional[str]


# HttpEndpointDescriptionTypeDef

### Url
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# HttpEndpointDestinationConfigurationTypeDef

### EndpointConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointConfigurationTypeDef'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef'>
- **Required**: Yes

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointBufferingHintsTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### RequestConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointRequestConfigurationUnionTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]


# HttpEndpointDestinationDescriptionTypeDef

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointDescriptionTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointBufferingHintsTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### RequestConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointRequestConfigurationOutputTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationOutputTypeDef]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### S3DestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]


# HttpEndpointDestinationUpdateTypeDef

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointConfigurationTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointBufferingHintsTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### RequestConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointRequestConfigurationUnionTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]


# HttpEndpointRequestConfigurationOutputTypeDef

### ContentEncoding
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### CommonAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointCommonAttributeTypeDef]]


# HttpEndpointRequestConfigurationTypeDef

### ContentEncoding
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### CommonAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointCommonAttributeTypeDef]]


# HttpEndpointRequestConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HttpEndpointRetryOptionsTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]


# IcebergDestinationConfigurationTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.CatalogConfigurationTypeDef'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef'>
- **Required**: Yes

### DestinationTableConfigurationList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.firehose_classes.DestinationTableConfigurationUnionTypeDef]]

### SchemaEvolutionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SchemaEvolutionConfigurationTypeDef]

### TableCreationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.TableCreationConfigurationTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.BufferingHintsTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RetryOptionsTypeDef]

### AppendOnly
- **Type**: typing.Optional[bool]


# IcebergDestinationDescriptionTypeDef

### DestinationTableConfigurationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose_classes.DestinationTableConfigurationOutputTypeDef]]

### SchemaEvolutionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SchemaEvolutionConfigurationTypeDef]

### TableCreationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.TableCreationConfigurationTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.BufferingHintsTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationOutputTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RetryOptionsTypeDef]

### RoleARN
- **Type**: typing.Optional[str]

### AppendOnly
- **Type**: typing.Optional[bool]

### CatalogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CatalogConfigurationTypeDef]

### S3DestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]


# IcebergDestinationUpdateTypeDef

### DestinationTableConfigurationList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.firehose_classes.DestinationTableConfigurationUnionTypeDef]]

### SchemaEvolutionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SchemaEvolutionConfigurationTypeDef]

### TableCreationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.TableCreationConfigurationTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.BufferingHintsTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RetryOptionsTypeDef]

### RoleARN
- **Type**: typing.Optional[str]

### AppendOnly
- **Type**: typing.Optional[bool]

### CatalogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CatalogConfigurationTypeDef]

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef]


# InputFormatConfigurationOutputTypeDef

### Deserializer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DeserializerOutputTypeDef]


# InputFormatConfigurationTypeDef

### Deserializer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DeserializerUnionTypeDef]


# InputFormatConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KMSEncryptionConfigTypeDef

### AWSKMSKeyARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamSourceConfigurationTypeDef

### KinesisStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamSourceDescriptionTypeDef

### KinesisStreamARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### DeliveryStartTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ListDeliveryStreamsInputTypeDef

### Limit
- **Type**: typing.Optional[int]

### DeliveryStreamType
- **Type**: typing.Optional[typing.Literal['DatabaseAsSource', 'DirectPut', 'KinesisStreamAsSource', 'MSKAsSource']]

### ExclusiveStartDeliveryStreamName
- **Type**: typing.Optional[str]


# ListDeliveryStreamsOutputTypeDef

### DeliveryStreamNames
- **Type**: typing.List[str]
- **Required**: Yes

### HasMoreDeliveryStreams
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForDeliveryStreamInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### ExclusiveStartTagKey
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTagsForDeliveryStreamOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.firehose_classes.TagTypeDef]
- **Required**: Yes

### HasMoreTags
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MSKSourceConfigurationTypeDef

### MSKClusterARN
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.AuthenticationConfigurationTypeDef'>
- **Required**: Yes

### ReadFromTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.TimestampTypeDef]


# MSKSourceDescriptionTypeDef

### MSKClusterARN
- **Type**: typing.Optional[str]

### TopicName
- **Type**: typing.Optional[str]

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AuthenticationConfigurationTypeDef]

### DeliveryStartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ReadFromTimestamp
- **Type**: typing.Optional[datetime.datetime]


# OpenXJsonSerDeOutputTypeDef

### ConvertDotsInJsonKeysToUnderscores
- **Type**: typing.Optional[bool]

### CaseInsensitive
- **Type**: typing.Optional[bool]

### ColumnToJsonKeyMappings
- **Type**: typing.Optional[typing.Dict[str, str]]


# OpenXJsonSerDeTypeDef

### ConvertDotsInJsonKeysToUnderscores
- **Type**: typing.Optional[bool]

### CaseInsensitive
- **Type**: typing.Optional[bool]

### ColumnToJsonKeyMappings
- **Type**: typing.Optional[typing.Mapping[str, str]]


# OpenXJsonSerDeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrcSerDeOutputTypeDef

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


# OrcSerDeTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### BloomFilterFalsePositiveProbability
- **Type**: typing.Optional[float]

### DictionaryKeyThreshold
- **Type**: typing.Optional[float]

### FormatVersion
- **Type**: typing.Optional[typing.Literal['V0_11', 'V0_12']]


# OrcSerDeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OutputFormatConfigurationOutputTypeDef

### Serializer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SerializerOutputTypeDef]


# OutputFormatConfigurationTypeDef

### Serializer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SerializerUnionTypeDef]


# OutputFormatConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParquetSerDeTypeDef

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


# PartitionFieldTypeDef

### SourceName
- **Type**: <class 'str'>
- **Required**: Yes


# PartitionSpecOutputTypeDef

### Identity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose_classes.PartitionFieldTypeDef]]


# PartitionSpecTypeDef

### Identity
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.firehose_classes.PartitionFieldTypeDef]]


# PartitionSpecUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProcessingConfigurationOutputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### Processors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.firehose_classes.ProcessorOutputTypeDef]]


# ProcessingConfigurationTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### Processors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.firehose_classes.ProcessorUnionTypeDef]]


# ProcessingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProcessorOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProcessorParameterTypeDef

### ParameterName
- **Type**: typing.Literal['BufferIntervalInSeconds', 'BufferSizeInMBs', 'CompressionFormat', 'DataMessageExtraction', 'Delimiter', 'JsonParsingEngine', 'LambdaArn', 'MetadataExtractionQuery', 'NumberOfRetries', 'RoleArn', 'SubRecordType']
- **Required**: Yes

### ParameterValue
- **Type**: <class 'str'>
- **Required**: Yes


# ProcessorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutRecordBatchInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Records
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.firehose_classes.RecordTypeDef]
- **Required**: Yes


# PutRecordBatchOutputTypeDef

### FailedPutCount
- **Type**: <class 'int'>
- **Required**: Yes

### Encrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### RequestResponses
- **Type**: typing.List[aws_resource_validator.pydantic_models.firehose_classes.PutRecordBatchResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRecordBatchResponseEntryTypeDef

### RecordId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# PutRecordInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Record
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.RecordTypeDef'>
- **Required**: Yes


# PutRecordOutputTypeDef

### RecordId
- **Type**: <class 'str'>
- **Required**: Yes

### Encrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecordTypeDef

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.BlobTypeDef'>
- **Required**: Yes


# RedshiftDestinationConfigurationTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterJDBCURL
- **Type**: <class 'str'>
- **Required**: Yes

### CopyCommand
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.CopyCommandTypeDef'>
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef'>
- **Required**: Yes

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RedshiftRetryOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]


# RedshiftDestinationDescriptionTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterJDBCURL
- **Type**: <class 'str'>
- **Required**: Yes

### CopyCommand
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.CopyCommandTypeDef'>
- **Required**: Yes

### S3DestinationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef'>
- **Required**: Yes

### Username
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RedshiftRetryOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationOutputTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]


# RedshiftDestinationUpdateTypeDef

### RoleARN
- **Type**: typing.Optional[str]

### ClusterJDBCURL
- **Type**: typing.Optional[str]

### CopyCommand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CopyCommandTypeDef]

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RedshiftRetryOptionsTypeDef]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### S3BackupUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]


# RedshiftRetryOptionsTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]


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


# RetryOptionsTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]


# S3DestinationConfigurationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.BufferingHintsTypeDef]

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.EncryptionConfigurationTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]


# S3DestinationDescriptionTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### BufferingHints
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.BufferingHintsTypeDef'>
- **Required**: Yes

### CompressionFormat
- **Type**: typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.EncryptionConfigurationTypeDef'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]


# S3DestinationUpdateTypeDef

### RoleARN
- **Type**: typing.Optional[str]

### BucketARN
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### ErrorOutputPrefix
- **Type**: typing.Optional[str]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.BufferingHintsTypeDef]

### CompressionFormat
- **Type**: typing.Optional[typing.Literal['GZIP', 'HADOOP_SNAPPY', 'Snappy', 'UNCOMPRESSED', 'ZIP']]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.EncryptionConfigurationTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]


# SchemaConfigurationTypeDef

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


# SchemaEvolutionConfigurationTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SecretsManagerConfigurationTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SecretARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# SerializerOutputTypeDef

### ParquetSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ParquetSerDeTypeDef]

### OrcSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.OrcSerDeOutputTypeDef]


# SerializerTypeDef

### ParquetSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ParquetSerDeTypeDef]

### OrcSerDe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.OrcSerDeUnionTypeDef]


# SerializerUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SnowflakeBufferingHintsTypeDef

### SizeInMBs
- **Type**: typing.Optional[int]

### IntervalInSeconds
- **Type**: typing.Optional[int]


# SnowflakeDestinationConfigurationTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef'>
- **Required**: Yes

### PrivateKey
- **Type**: typing.Optional[str]

### KeyPassphrase
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[str]

### SnowflakeRoleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeRoleConfigurationTypeDef]

### DataLoadingOption
- **Type**: typing.Optional[typing.Literal['JSON_MAPPING', 'VARIANT_CONTENT_AND_METADATA_MAPPING', 'VARIANT_CONTENT_MAPPING']]

### MetaDataColumnName
- **Type**: typing.Optional[str]

### ContentColumnName
- **Type**: typing.Optional[str]

### SnowflakeVpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeVpcConfigurationTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeBufferingHintsTypeDef]


# SnowflakeDestinationDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeRoleConfigurationTypeDef]

### DataLoadingOption
- **Type**: typing.Optional[typing.Literal['JSON_MAPPING', 'VARIANT_CONTENT_AND_METADATA_MAPPING', 'VARIANT_CONTENT_MAPPING']]

### MetaDataColumnName
- **Type**: typing.Optional[str]

### ContentColumnName
- **Type**: typing.Optional[str]

### SnowflakeVpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeVpcConfigurationTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationOutputTypeDef]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### S3DestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeBufferingHintsTypeDef]


# SnowflakeDestinationUpdateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeRoleConfigurationTypeDef]

### DataLoadingOption
- **Type**: typing.Optional[typing.Literal['JSON_MAPPING', 'VARIANT_CONTENT_AND_METADATA_MAPPING', 'VARIANT_CONTENT_MAPPING']]

### MetaDataColumnName
- **Type**: typing.Optional[str]

### ContentColumnName
- **Type**: typing.Optional[str]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### RoleARN
- **Type**: typing.Optional[str]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllData', 'FailedDataOnly']]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeBufferingHintsTypeDef]


# SnowflakeRetryOptionsTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]


# SnowflakeRoleConfigurationTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### SnowflakeRole
- **Type**: typing.Optional[str]


# SnowflakeVpcConfigurationTypeDef

### PrivateLinkVpceId
- **Type**: <class 'str'>
- **Required**: Yes


# SourceDescriptionTypeDef

### DirectPutSourceDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DirectPutSourceDescriptionTypeDef]

### KinesisStreamSourceDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.KinesisStreamSourceDescriptionTypeDef]

### MSKSourceDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.MSKSourceDescriptionTypeDef]

### DatabaseSourceDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DatabaseSourceDescriptionTypeDef]


# SplunkBufferingHintsTypeDef

### IntervalInSeconds
- **Type**: typing.Optional[int]

### SizeInMBs
- **Type**: typing.Optional[int]


# SplunkDestinationConfigurationTypeDef

### HECEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### HECEndpointType
- **Type**: typing.Literal['Event', 'Raw']
- **Required**: Yes

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.firehose_classes.S3DestinationConfigurationTypeDef'>
- **Required**: Yes

### HECToken
- **Type**: typing.Optional[str]

### HECAcknowledgmentTimeoutInSeconds
- **Type**: typing.Optional[int]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SplunkRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllEvents', 'FailedEventsOnly']]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SplunkBufferingHintsTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]


# SplunkDestinationDescriptionTypeDef

### HECEndpoint
- **Type**: typing.Optional[str]

### HECEndpointType
- **Type**: typing.Optional[typing.Literal['Event', 'Raw']]

### HECToken
- **Type**: typing.Optional[str]

### HECAcknowledgmentTimeoutInSeconds
- **Type**: typing.Optional[int]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SplunkRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllEvents', 'FailedEventsOnly']]

### S3DestinationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationDescriptionTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationOutputTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SplunkBufferingHintsTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]


# SplunkDestinationUpdateTypeDef

### HECEndpoint
- **Type**: typing.Optional[str]

### HECEndpointType
- **Type**: typing.Optional[typing.Literal['Event', 'Raw']]

### HECToken
- **Type**: typing.Optional[str]

### HECAcknowledgmentTimeoutInSeconds
- **Type**: typing.Optional[int]

### RetryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SplunkRetryOptionsTypeDef]

### S3BackupMode
- **Type**: typing.Optional[typing.Literal['AllEvents', 'FailedEventsOnly']]

### S3Update
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### ProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ProcessingConfigurationUnionTypeDef]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.CloudWatchLoggingOptionsTypeDef]

### BufferingHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SplunkBufferingHintsTypeDef]

### SecretsManagerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SecretsManagerConfigurationTypeDef]


# SplunkRetryOptionsTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]


# StartDeliveryStreamEncryptionInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamEncryptionConfigurationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.DeliveryStreamEncryptionConfigurationInputTypeDef]


# StopDeliveryStreamEncryptionInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# TableCreationConfigurationTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# TagDeliveryStreamInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.firehose_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagDeliveryStreamInputTypeDef

### DeliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDestinationInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.S3DestinationUpdateTypeDef]

### ExtendedS3DestinationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ExtendedS3DestinationUpdateTypeDef]

### RedshiftDestinationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.RedshiftDestinationUpdateTypeDef]

### ElasticsearchDestinationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.ElasticsearchDestinationUpdateTypeDef]

### AmazonopensearchserviceDestinationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonopensearchserviceDestinationUpdateTypeDef]

### SplunkDestinationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SplunkDestinationUpdateTypeDef]

### HttpEndpointDestinationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.HttpEndpointDestinationUpdateTypeDef]

### AmazonOpenSearchServerlessDestinationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.AmazonOpenSearchServerlessDestinationUpdateTypeDef]

### SnowflakeDestinationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.SnowflakeDestinationUpdateTypeDef]

### IcebergDestinationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.firehose_classes.IcebergDestinationUpdateTypeDef]


# VpcConfigurationDescriptionTypeDef

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


# VpcConfigurationTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes



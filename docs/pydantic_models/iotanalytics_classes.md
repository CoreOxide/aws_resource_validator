# Iotanalytics Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchPutMessageErrorEntryTypeDef

### messageId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchPutMessageRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.MessageTypeDef]
- **Required**: Yes


# BatchPutMessageResponseTypeDef

### batchPutMessageErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.BatchPutMessageErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelPipelineReprocessingRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### reprocessingId
- **Type**: <class 'str'>
- **Required**: Yes


# ChannelMessagesTypeDef

### s3Paths
- **Type**: typing.Optional[typing.Sequence[str]]


# ChannelStatisticsTypeDef

### size
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.EstimatedResourceSizeTypeDef]


# ChannelStorageOutputTypeDef

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.CustomerManagedChannelS3StorageTypeDef]


# ChannelStorageSummaryTypeDef

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.CustomerManagedChannelS3StorageSummaryTypeDef]


# ChannelStorageTypeDef

### serviceManagedS3
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.CustomerManagedChannelS3StorageTypeDef]


# ChannelStorageUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelSummaryTypeDef

### channelName
- **Type**: typing.Optional[str]

### channelStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelStorageSummaryTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### lastMessageArrivalTime
- **Type**: typing.Optional[datetime.datetime]


# ChannelTypeDef

### name
- **Type**: typing.Optional[str]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelStorageOutputTypeDef]

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### lastMessageArrivalTime
- **Type**: typing.Optional[datetime.datetime]


# ColumnTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerDatasetActionOutputTypeDef

### image
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResourceConfigurationTypeDef'>
- **Required**: Yes

### variables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.VariableTypeDef]]


# ContainerDatasetActionTypeDef

### image
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResourceConfigurationTypeDef'>
- **Required**: Yes

### variables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.VariableTypeDef]]


# ContainerDatasetActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateChannelRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### channelStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelStorageUnionTypeDef]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.TagTypeDef]]


# CreateChannelResponseTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetContentRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# CreateDatasetContentResponseTypeDef

### versionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetActionUnionTypeDef]
- **Required**: Yes

### triggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetTriggerTypeDef]]

### contentDeliveryRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetContentDeliveryRuleTypeDef]]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### versioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.VersioningConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.TagTypeDef]]

### lateDataRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.LateDataRuleTypeDef]]


# CreateDatasetResponseTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatastoreRequestTypeDef

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreStorageUnionTypeDef]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.TagTypeDef]]

### fileFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.FileFormatConfigurationUnionTypeDef]

### datastorePartitions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionsUnionTypeDef]


# CreateDatastoreResponseTypeDef

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePipelineRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineActivities
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineActivityUnionTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.TagTypeDef]]


# CreatePipelineResponseTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerManagedChannelS3StorageSummaryTypeDef

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# CustomerManagedChannelS3StorageTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# CustomerManagedDatastoreS3StorageSummaryTypeDef

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# CustomerManagedDatastoreS3StorageTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# DatasetActionOutputTypeDef

### actionName
- **Type**: typing.Optional[str]

### queryAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.SqlQueryDatasetActionOutputTypeDef]

### containerAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ContainerDatasetActionOutputTypeDef]


# DatasetActionSummaryTypeDef

### actionName
- **Type**: typing.Optional[str]

### actionType
- **Type**: typing.Optional[typing.Literal['CONTAINER', 'QUERY']]


# DatasetActionTypeDef

### actionName
- **Type**: typing.Optional[str]

### queryAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.SqlQueryDatasetActionUnionTypeDef]

### containerAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ContainerDatasetActionUnionTypeDef]


# DatasetActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatasetContentDeliveryDestinationTypeDef

### iotEventsDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.IotEventsDestinationConfigurationTypeDef]

### s3DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.S3DestinationConfigurationTypeDef]


# DatasetContentDeliveryRuleTypeDef

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetContentDeliveryDestinationTypeDef'>
- **Required**: Yes

### entryName
- **Type**: typing.Optional[str]


# DatasetContentStatusTypeDef

### state
- **Type**: typing.Optional[typing.Literal['CREATING', 'FAILED', 'SUCCEEDED']]

### reason
- **Type**: typing.Optional[str]


# DatasetContentSummaryTypeDef

### version
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetContentStatusTypeDef]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### scheduleTime
- **Type**: typing.Optional[datetime.datetime]

### completionTime
- **Type**: typing.Optional[datetime.datetime]


# DatasetContentVersionValueTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DatasetEntryTypeDef

### entryName
- **Type**: typing.Optional[str]

### dataURI
- **Type**: typing.Optional[str]


# DatasetSummaryTypeDef

### datasetName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetTriggerTypeDef]]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetActionSummaryTypeDef]]


# DatasetTriggerTypeDef

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ScheduleTypeDef]

### dataset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TriggeringDatasetTypeDef]


# DatasetTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetActionOutputTypeDef]]

### triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetTriggerTypeDef]]

### contentDeliveryRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetContentDeliveryRuleTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### versioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.VersioningConfigurationTypeDef]

### lateDataRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.LateDataRuleTypeDef]]


# DatastoreActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes


# DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef

### customerManagedS3Storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef]


# DatastoreIotSiteWiseMultiLayerStorageTypeDef

### customerManagedS3Storage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef'>
- **Required**: Yes


# DatastorePartitionTypeDef

### attributePartition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PartitionTypeDef]

### timestampPartition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TimestampPartitionTypeDef]


# DatastorePartitionsOutputTypeDef

### partitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionTypeDef]]


# DatastorePartitionsTypeDef

### partitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionTypeDef]]


# DatastorePartitionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatastoreStatisticsTypeDef

### size
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.EstimatedResourceSizeTypeDef]


# DatastoreStorageOutputTypeDef

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.CustomerManagedDatastoreS3StorageTypeDef]

### iotSiteWiseMultiLayerStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreIotSiteWiseMultiLayerStorageTypeDef]


# DatastoreStorageSummaryTypeDef

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.CustomerManagedDatastoreS3StorageSummaryTypeDef]

### iotSiteWiseMultiLayerStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef]


# DatastoreStorageTypeDef

### serviceManagedS3
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.CustomerManagedDatastoreS3StorageTypeDef]

### iotSiteWiseMultiLayerStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreIotSiteWiseMultiLayerStorageTypeDef]


# DatastoreStorageUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatastoreSummaryTypeDef

### datastoreName
- **Type**: typing.Optional[str]

### datastoreStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreStorageSummaryTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### lastMessageArrivalTime
- **Type**: typing.Optional[datetime.datetime]

### fileFormatType
- **Type**: typing.Optional[typing.Literal['JSON', 'PARQUET']]

### datastorePartitions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionsOutputTypeDef]


# DatastoreTypeDef

### name
- **Type**: typing.Optional[str]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreStorageOutputTypeDef]

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### lastMessageArrivalTime
- **Type**: typing.Optional[datetime.datetime]

### fileFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.FileFormatConfigurationOutputTypeDef]

### datastorePartitions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionsOutputTypeDef]


# DeleteChannelRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetContentRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# DeleteDatasetRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatastoreRequestTypeDef

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipelineRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# DeltaTimeSessionWindowConfigurationTypeDef

### timeoutInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# DeltaTimeTypeDef

### offsetSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### timeExpression
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### includeStatistics
- **Type**: typing.Optional[bool]


# DescribeChannelResponseTypeDef

### channel
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelTypeDef'>
- **Required**: Yes

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponseTypeDef

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatastoreRequestTypeDef

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### includeStatistics
- **Type**: typing.Optional[bool]


# DescribeDatastoreResponseTypeDef

### datastore
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreTypeDef'>
- **Required**: Yes

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoggingOptionsResponseTypeDef

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.LoggingOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePipelineRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipelineResponseTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EstimatedResourceSizeTypeDef

### estimatedSizeInBytes
- **Type**: typing.Optional[float]

### estimatedOn
- **Type**: typing.Optional[datetime.datetime]


# FileFormatConfigurationOutputTypeDef

### jsonConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### parquetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ParquetConfigurationOutputTypeDef]


# FileFormatConfigurationTypeDef

### jsonConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### parquetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ParquetConfigurationTypeDef]


# FileFormatConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetDatasetContentRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# GetDatasetContentResponseTypeDef

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetEntryTypeDef]
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetContentStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlueConfigurationTypeDef

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# IotEventsDestinationConfigurationTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]


# IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# LateDataRuleConfigurationTypeDef

### deltaTimeSessionWindowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DeltaTimeSessionWindowConfigurationTypeDef]


# LateDataRuleTypeDef

### ruleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.LateDataRuleConfigurationTypeDef'>
- **Required**: Yes

### ruleName
- **Type**: typing.Optional[str]


# ListChannelsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListChannelsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListChannelsResponseTypeDef

### channelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetContentsRequestPaginateTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### scheduledOnOrAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TimestampTypeDef]

### scheduledBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListDatasetContentsRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### scheduledOnOrAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TimestampTypeDef]

### scheduledBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TimestampTypeDef]


# ListDatasetContentsResponseTypeDef

### datasetContentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetContentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListDatasetsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponseTypeDef

### datasetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatastoresRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListDatastoresRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatastoresResponseTypeDef

### datastoreSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPipelinesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListPipelinesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPipelinesResponseTypeDef

### pipelineSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingOptionsTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### level
- **Type**: typing.Literal['ERROR']
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# MessageTypeDef

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.BlobTypeDef'>
- **Required**: Yes


# OutputFileUriValueTypeDef

### fileName
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParquetConfigurationOutputTypeDef

### schemaDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.SchemaDefinitionOutputTypeDef]


# ParquetConfigurationTypeDef

### schemaDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.SchemaDefinitionTypeDef]


# PartitionTypeDef

### attributeName
- **Type**: <class 'str'>
- **Required**: Yes


# PipelineActivityOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineActivityUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineSummaryTypeDef

### pipelineName
- **Type**: typing.Optional[str]

### reprocessingSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.ReprocessingSummaryTypeDef]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# PipelineTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### activities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineActivityOutputTypeDef]]

### reprocessingSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.ReprocessingSummaryTypeDef]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# PutLoggingOptionsRequestTypeDef

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.LoggingOptionsTypeDef'>
- **Required**: Yes


# QueryFilterTypeDef

### deltaTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DeltaTimeTypeDef]


# ReprocessingSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceConfigurationTypeDef

### computeType
- **Type**: typing.Literal['ACU_1', 'ACU_2']
- **Required**: Yes

### volumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes


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


# RetentionPeriodTypeDef

### unlimited
- **Type**: typing.Optional[bool]

### numberOfDays
- **Type**: typing.Optional[int]


# RunPipelineActivityRequestTypeDef

### pipelineActivity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineActivityUnionTypeDef'>
- **Required**: Yes

### payloads
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.BlobTypeDef]
- **Required**: Yes


# RunPipelineActivityResponseTypeDef

### payloads
- **Type**: typing.List[bytes]
- **Required**: Yes

### logResult
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3DestinationConfigurationTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### glueConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.GlueConfigurationTypeDef]


# SampleChannelDataRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### maxMessages
- **Type**: typing.Optional[int]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TimestampTypeDef]


# SampleChannelDataResponseTypeDef

### payloads
- **Type**: typing.List[bytes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ScheduleTypeDef

### expression
- **Type**: typing.Optional[str]


# SchemaDefinitionOutputTypeDef

### columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.ColumnTypeDef]]


# SchemaDefinitionTypeDef

### columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.ColumnTypeDef]]


# SqlQueryDatasetActionOutputTypeDef

### sqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.QueryFilterTypeDef]]


# SqlQueryDatasetActionTypeDef

### sqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.QueryFilterTypeDef]]


# SqlQueryDatasetActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartPipelineReprocessingRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.TimestampTypeDef]

### channelMessages
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelMessagesTypeDef]


# StartPipelineReprocessingResponseTypeDef

### reprocessingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampPartitionTypeDef

### attributeName
- **Type**: <class 'str'>
- **Required**: Yes

### timestampFormat
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TriggeringDatasetTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### channelStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelStorageUnionTypeDef]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]


# UpdateDatasetRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetActionUnionTypeDef]
- **Required**: Yes

### triggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetTriggerTypeDef]]

### contentDeliveryRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetContentDeliveryRuleTypeDef]]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### versioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.VersioningConfigurationTypeDef]

### lateDataRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.LateDataRuleTypeDef]]


# UpdateDatastoreRequestTypeDef

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### datastoreStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreStorageUnionTypeDef]

### fileFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.FileFormatConfigurationUnionTypeDef]


# UpdatePipelineRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineActivities
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineActivityUnionTypeDef]
- **Required**: Yes


# VariableTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stringValue
- **Type**: typing.Optional[str]

### doubleValue
- **Type**: typing.Optional[float]

### datasetContentVersionValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetContentVersionValueTypeDef]

### outputFileUriValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.OutputFileUriValueTypeDef]


# VersioningConfigurationTypeDef

### unlimited
- **Type**: typing.Optional[bool]

### maxVersions
- **Type**: typing.Optional[int]



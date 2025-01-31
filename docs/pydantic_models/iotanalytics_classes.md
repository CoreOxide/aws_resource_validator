# Iotanalytics Classes

# AddAttributesActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


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


# BatchPutMessageRequestRequestTypeDef

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


# CancelPipelineReprocessingRequestRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### reprocessingId
- **Type**: <class 'str'>
- **Required**: Yes


# ChannelActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# ChannelMessagesTypeDef

### s3Paths
- **Type**: typing.Optional[typing.Sequence[str]]


# ChannelStatisticsTypeDef

### size
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.EstimatedResourceSizeTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelStorageTypeDef]

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

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes


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


# CreateChannelRequestRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### channelStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelStorageTypeDef]

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


# CreateDatasetContentRequestRequestTypeDef

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


# CreateDatasetRequestRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetActionTypeDef]
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


# CreateDatastoreRequestRequestTypeDef

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreStorageTypeDef]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.TagTypeDef]]

### fileFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.FileFormatConfigurationTypeDef]

### datastorePartitions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionsTypeDef]


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


# CreatePipelineRequestRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineActivities
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineActivityTypeDef]
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


# DatasetActionSummaryTypeDef

### actionName
- **Type**: typing.Optional[str]

### actionType
- **Type**: typing.Optional[typing.Literal['CONTAINER', 'QUERY']]


# DatasetActionTypeDef

### actionName
- **Type**: typing.Optional[str]

### queryAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.SqlQueryDatasetActionTypeDef]

### containerAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ContainerDatasetActionTypeDef]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetActionTypeDef]]

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


# DatastorePartitionsPaginatorTypeDef

### partitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionTypeDef]]


# DatastorePartitionsTypeDef

### partitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionTypeDef]]


# DatastoreStatisticsTypeDef

### size
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.EstimatedResourceSizeTypeDef]


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


# DatastoreSummaryPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionsPaginatorTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionsTypeDef]


# DatastoreTypeDef

### name
- **Type**: typing.Optional[str]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreStorageTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.FileFormatConfigurationTypeDef]

### datastorePartitions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastorePartitionsTypeDef]


# DeleteChannelRequestRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetContentRequestRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# DeleteDatasetRequestRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatastoreRequestRequestTypeDef

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipelineRequestRequestTypeDef

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


# DescribeChannelRequestRequestTypeDef

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


# DescribeDatasetRequestRequestTypeDef

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


# DescribeDatastoreRequestRequestTypeDef

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


# DescribePipelineRequestRequestTypeDef

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


# DeviceRegistryEnrichActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attribute
- **Type**: <class 'str'>
- **Required**: Yes

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# DeviceShadowEnrichActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attribute
- **Type**: <class 'str'>
- **Required**: Yes

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EstimatedResourceSizeTypeDef

### estimatedSizeInBytes
- **Type**: typing.Optional[float]

### estimatedOn
- **Type**: typing.Optional[datetime.datetime]


# FileFormatConfigurationTypeDef

### jsonConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### parquetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ParquetConfigurationTypeDef]


# FilterActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: <class 'str'>
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# GetDatasetContentRequestRequestTypeDef

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


# LambdaActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### lambdaName
- **Type**: <class 'str'>
- **Required**: Yes

### batchSize
- **Type**: <class 'int'>
- **Required**: Yes

### next
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


# ListChannelsRequestListChannelsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListChannelsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListChannelsResponseTypeDef

### channelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetContentsRequestListDatasetContentsPaginateTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### scheduledOnOrAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### scheduledBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListDatasetContentsRequestRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### scheduledOnOrAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### scheduledBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListDatasetContentsResponseTypeDef

### datasetContentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetContentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetsRequestListDatasetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListDatasetsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponseTypeDef

### datasetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatastoresRequestListDatastoresPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListDatastoresRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatastoresResponsePaginatorTypeDef

### datastoreSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreSummaryPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatastoresResponseTypeDef

### datastoreSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPipelinesRequestListPipelinesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.PaginatorConfigTypeDef]


# ListPipelinesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPipelinesResponseTypeDef

### pipelineSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# MathActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attribute
- **Type**: <class 'str'>
- **Required**: Yes

### math
- **Type**: <class 'str'>
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# MessageTypeDef

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# ParquetConfigurationTypeDef

### schemaDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.SchemaDefinitionTypeDef]


# PartitionTypeDef

### attributeName
- **Type**: <class 'str'>
- **Required**: Yes


# PipelineActivityTypeDef

### channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelActivityTypeDef]

### datastore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreActivityTypeDef]

### addAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.AddAttributesActivityTypeDef]

### removeAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RemoveAttributesActivityTypeDef]

### selectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.SelectAttributesActivityTypeDef]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.FilterActivityTypeDef]

### math
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.MathActivityTypeDef]

### deviceRegistryEnrich
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DeviceRegistryEnrichActivityTypeDef]

### deviceShadowEnrich
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DeviceShadowEnrichActivityTypeDef]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineActivityTypeDef]]

### reprocessingSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics_classes.ReprocessingSummaryTypeDef]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# PutLoggingOptionsRequestRequestTypeDef

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.LoggingOptionsTypeDef'>
- **Required**: Yes


# QueryFilterTypeDef

### deltaTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DeltaTimeTypeDef]


# RemoveAttributesActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# ReprocessingSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'RUNNING', 'SUCCEEDED']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]


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

### HostId
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


# RetentionPeriodTypeDef

### unlimited
- **Type**: typing.Optional[bool]

### numberOfDays
- **Type**: typing.Optional[int]


# RunPipelineActivityRequestRequestTypeDef

### pipelineActivity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineActivityTypeDef'>
- **Required**: Yes

### payloads
- **Type**: typing.Sequence[typing.Union[str, bytes, typing.IO[typing.Any]]]
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


# SampleChannelDataRequestRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### maxMessages
- **Type**: typing.Optional[int]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# SchemaDefinitionTypeDef

### columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.ColumnTypeDef]]


# SelectAttributesActivityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# SqlQueryDatasetActionTypeDef

### sqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.QueryFilterTypeDef]]


# StartPipelineReprocessingRequestRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### channelMessages
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelMessagesTypeDef]


# StartPipelineReprocessingResponseTypeDef

### reprocessingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

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


# TriggeringDatasetTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelRequestRequestTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### channelStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.ChannelStorageTypeDef]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]


# UpdateDatasetRequestRequestTypeDef

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.DatasetActionTypeDef]
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


# UpdateDatastoreRequestRequestTypeDef

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.RetentionPeriodTypeDef]

### datastoreStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.DatastoreStorageTypeDef]

### fileFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics_classes.FileFormatConfigurationTypeDef]


# UpdatePipelineRequestRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineActivities
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotanalytics_classes.PipelineActivityTypeDef]
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



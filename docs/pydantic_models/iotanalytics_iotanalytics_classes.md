# Iotanalytics Iotanalytics Classes

# AddAttributesActivity

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# AddAttributesActivityOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchPutMessageErrorEntry

### messageId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchPutMessageRequest

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Message]
- **Required**: Yes


# BatchPutMessageResponse

### batchPutMessageErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.BatchPutMessageErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# CancelPipelineReprocessingRequest

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### reprocessingId
- **Type**: <class 'str'>
- **Required**: Yes


# Channel

### name
- **Type**: typing.Optional[str]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelStorageOutput]

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### lastMessageArrivalTime
- **Type**: typing.Optional[datetime.datetime]


# ChannelActivity

### name
- **Type**: <class 'str'>
- **Required**: Yes

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# ChannelMessages

### s3Paths
- **Type**: typing.Optional[typing.List[str]]


# ChannelStatistics

### size
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.EstimatedResourceSize]


# ChannelStorage

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.CustomerManagedChannelS3Storage]


# ChannelStorageOutput

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.CustomerManagedChannelS3Storage]


# ChannelStorageSummary

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.CustomerManagedChannelS3StorageSummary]


# ChannelSummary

### channelName
- **Type**: typing.Optional[str]

### channelStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelStorageSummary]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### lastMessageArrivalTime
- **Type**: typing.Optional[datetime.datetime]


# Column

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes


# ContainerDatasetAction

### image
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResourceConfiguration'>
- **Required**: Yes

### variables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Variable]]


# ContainerDatasetActionOutput

### image
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResourceConfiguration'>
- **Required**: Yes

### variables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Variable]]


# CreateChannelRequest

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### channelStorage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelStorage, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelStorageOutput, NoneType]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Tag]]


# CreateChannelResponse

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetContentRequest

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# CreateDatasetContentResponse

### versionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetRequest

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetAction, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetActionOutput]]
- **Required**: Yes

### triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetTrigger]]

### contentDeliveryRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetContentDeliveryRule]]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod]

### versioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.VersioningConfiguration]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Tag]]

### lateDataRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.LateDataRule]]


# CreateDatasetResponse

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatastoreRequest

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreStorage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreStorage, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreStorageOutput, NoneType]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Tag]]

### fileFormatConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.FileFormatConfiguration, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.FileFormatConfigurationOutput, NoneType]

### datastorePartitions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastorePartitions, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastorePartitionsOutput, NoneType]


# CreateDatastoreResponse

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePipelineRequest

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineActivities
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PipelineActivity, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PipelineActivityOutput]]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Tag]]


# CreatePipelineResponse

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerManagedChannelS3Storage

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# CustomerManagedChannelS3StorageSummary

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# CustomerManagedDatastoreS3Storage

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# CustomerManagedDatastoreS3StorageSummary

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# Dataset

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetActionOutput]]

### triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetTrigger]]

### contentDeliveryRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetContentDeliveryRule]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod]

### versioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.VersioningConfiguration]

### lateDataRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.LateDataRule]]


# DatasetAction

### actionName
- **Type**: typing.Optional[str]

### queryAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.SqlQueryDatasetAction, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.SqlQueryDatasetActionOutput, NoneType]

### containerAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ContainerDatasetAction, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ContainerDatasetActionOutput, NoneType]


# DatasetActionOutput

### actionName
- **Type**: typing.Optional[str]

### queryAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.SqlQueryDatasetActionOutput]

### containerAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ContainerDatasetActionOutput]


# DatasetActionSummary

### actionName
- **Type**: typing.Optional[str]

### actionType
- **Type**: typing.Optional[typing.Literal['CONTAINER', 'QUERY']]


# DatasetContentDeliveryDestination

### iotEventsDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.IotEventsDestinationConfiguration]

### s3DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.S3DestinationConfiguration]


# DatasetContentDeliveryRule

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetContentDeliveryDestination'>
- **Required**: Yes

### entryName
- **Type**: typing.Optional[str]


# DatasetContentStatus

### state
- **Type**: typing.Optional[typing.Literal['CREATING', 'FAILED', 'SUCCEEDED']]

### reason
- **Type**: typing.Optional[str]


# DatasetContentSummary

### version
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetContentStatus]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### scheduleTime
- **Type**: typing.Optional[datetime.datetime]

### completionTime
- **Type**: typing.Optional[datetime.datetime]


# DatasetContentVersionValue

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DatasetEntry

### entryName
- **Type**: typing.Optional[str]

### dataURI
- **Type**: typing.Optional[str]


# DatasetSummary

### datasetName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetTrigger]]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetActionSummary]]


# DatasetTrigger

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Schedule]

### dataset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.TriggeringDataset]


# Datastore

### name
- **Type**: typing.Optional[str]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreStorageOutput]

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### lastMessageArrivalTime
- **Type**: typing.Optional[datetime.datetime]

### fileFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.FileFormatConfigurationOutput]

### datastorePartitions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastorePartitionsOutput]


# DatastoreActivity

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes


# DatastoreIotSiteWiseMultiLayerStorage

### customerManagedS3Storage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.IotSiteWiseCustomerManagedDatastoreS3Storage'>
- **Required**: Yes


# DatastoreIotSiteWiseMultiLayerStorageSummary

### customerManagedS3Storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.IotSiteWiseCustomerManagedDatastoreS3StorageSummary]


# DatastorePartition

### attributePartition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Partition]

### timestampPartition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.TimestampPartition]


# DatastorePartitions

### partitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastorePartition]]


# DatastorePartitionsOutput

### partitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastorePartition]]


# DatastoreStatistics

### size
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.EstimatedResourceSize]


# DatastoreStorage

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.CustomerManagedDatastoreS3Storage]

### iotSiteWiseMultiLayerStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreIotSiteWiseMultiLayerStorage]


# DatastoreStorageOutput

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.CustomerManagedDatastoreS3Storage]

### iotSiteWiseMultiLayerStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreIotSiteWiseMultiLayerStorage]


# DatastoreStorageSummary

### serviceManagedS3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### customerManagedS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.CustomerManagedDatastoreS3StorageSummary]

### iotSiteWiseMultiLayerStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreIotSiteWiseMultiLayerStorageSummary]


# DatastoreSummary

### datastoreName
- **Type**: typing.Optional[str]

### datastoreStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreStorageSummary]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastorePartitionsOutput]


# DeleteChannelRequest

### channelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetContentRequest

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# DeleteDatasetRequest

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatastoreRequest

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipelineRequest

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# DeltaTime

### offsetSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### timeExpression
- **Type**: <class 'str'>
- **Required**: Yes


# DeltaTimeSessionWindowConfiguration

### timeoutInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeChannelRequest

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### includeStatistics
- **Type**: typing.Optional[bool]


# DescribeChannelResponse

### channel
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Channel'>
- **Required**: Yes

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetRequest

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Dataset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatastoreRequest

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### includeStatistics
- **Type**: typing.Optional[bool]


# DescribeDatastoreResponse

### datastore
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Datastore'>
- **Required**: Yes

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoggingOptionsResponse

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.LoggingOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePipelineRequest

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipelineResponse

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Pipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# DeviceRegistryEnrichActivity

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


# DeviceShadowEnrichActivity

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# EstimatedResourceSize

### estimatedSizeInBytes
- **Type**: typing.Optional[float]

### estimatedOn
- **Type**: typing.Optional[datetime.datetime]


# FileFormatConfiguration

### jsonConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### parquetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ParquetConfiguration]


# FileFormatConfigurationOutput

### jsonConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### parquetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ParquetConfigurationOutput]


# FilterActivity

### name
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: <class 'str'>
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# GetDatasetContentRequest

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# GetDatasetContentResponse

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetEntry]
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetContentStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# GlueConfiguration

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# IotEventsDestinationConfiguration

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# IotSiteWiseCustomerManagedDatastoreS3Storage

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# IotSiteWiseCustomerManagedDatastoreS3StorageSummary

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]


# LambdaActivity

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


# LateDataRule

### ruleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.LateDataRuleConfiguration'>
- **Required**: Yes

### ruleName
- **Type**: typing.Optional[str]


# LateDataRuleConfiguration

### deltaTimeSessionWindowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DeltaTimeSessionWindowConfiguration]


# ListChannelsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListChannelsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PaginatorConfig]


# ListChannelsResponse

### channelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetContentsRequest

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


# ListDatasetContentsRequestPaginate

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### scheduledOnOrAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### scheduledBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PaginatorConfig]


# ListDatasetContentsResponse

### datasetContentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetContentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PaginatorConfig]


# ListDatasetsResponse

### datasetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatastoresRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatastoresRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PaginatorConfig]


# ListDatastoresResponse

### datastoreSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPipelinesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPipelinesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PaginatorConfig]


# ListPipelinesResponse

### pipelineSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PipelineSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingOptions

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### level
- **Type**: typing.Literal['ERROR']
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# MathActivity

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


# Message

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes


# OutputFileUriValue

### fileName
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParquetConfiguration

### schemaDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.SchemaDefinition]


# ParquetConfigurationOutput

### schemaDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.SchemaDefinitionOutput]


# Partition

### attributeName
- **Type**: <class 'str'>
- **Required**: Yes


# Pipeline

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### activities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PipelineActivityOutput]]

### reprocessingSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ReprocessingSummary]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# PipelineActivity

### channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelActivity]

### lambda_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.LambdaActivity]

### datastore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreActivity]

### addAttributes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.AddAttributesActivity, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.AddAttributesActivityOutput, NoneType]

### removeAttributes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RemoveAttributesActivity, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RemoveAttributesActivityOutput, NoneType]

### selectAttributes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.SelectAttributesActivity, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.SelectAttributesActivityOutput, NoneType]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.FilterActivity]

### math
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.MathActivity]

### deviceRegistryEnrich
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DeviceRegistryEnrichActivity]

### deviceShadowEnrich
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DeviceShadowEnrichActivity]


# PipelineActivityOutput

### channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelActivity]

### lambda_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.LambdaActivity]

### datastore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreActivity]

### addAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.AddAttributesActivityOutput]

### removeAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RemoveAttributesActivityOutput]

### selectAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.SelectAttributesActivityOutput]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.FilterActivity]

### math
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.MathActivity]

### deviceRegistryEnrich
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DeviceRegistryEnrichActivity]

### deviceShadowEnrich
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DeviceShadowEnrichActivity]


# PipelineSummary

### pipelineName
- **Type**: typing.Optional[str]

### reprocessingSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ReprocessingSummary]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# PutLoggingOptionsRequest

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.LoggingOptions'>
- **Required**: Yes


# QueryFilter

### deltaTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DeltaTime]


# RemoveAttributesActivity

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# RemoveAttributesActivityOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# ReprocessingSummary

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'RUNNING', 'SUCCEEDED']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]


# ResourceConfiguration

### computeType
- **Type**: typing.Literal['ACU_1', 'ACU_2']
- **Required**: Yes

### volumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes


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


# RetentionPeriod

### unlimited
- **Type**: typing.Optional[bool]

### numberOfDays
- **Type**: typing.Optional[int]


# RunPipelineActivityRequest

### pipelineActivity
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PipelineActivity, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PipelineActivityOutput]
- **Required**: Yes

### payloads
- **Type**: typing.List[typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]]
- **Required**: Yes


# RunPipelineActivityResponse

### payloads
- **Type**: typing.List[bytes]
- **Required**: Yes

### logResult
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# S3DestinationConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.GlueConfiguration]


# SampleChannelDataRequest

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### maxMessages
- **Type**: typing.Optional[int]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# SampleChannelDataResponse

### payloads
- **Type**: typing.List[bytes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# Schedule

### expression
- **Type**: typing.Optional[str]


# SchemaDefinition

### columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Column]]


# SchemaDefinitionOutput

### columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Column]]


# SelectAttributesActivity

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# SelectAttributesActivityOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.Optional[str]


# SqlQueryDatasetAction

### sqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.QueryFilter]]


# SqlQueryDatasetActionOutput

### sqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.QueryFilter]]


# StartPipelineReprocessingRequest

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### channelMessages
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelMessages]


# StartPipelineReprocessingResponse

### reprocessingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.Tag]
- **Required**: Yes


# TimestampPartition

### attributeName
- **Type**: <class 'str'>
- **Required**: Yes

### timestampFormat
- **Type**: typing.Optional[str]


# TriggeringDataset

### name
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateChannelRequest

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### channelStorage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelStorage, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.ChannelStorageOutput, NoneType]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod]


# UpdateDatasetRequest

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetAction, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetActionOutput]]
- **Required**: Yes

### triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetTrigger]]

### contentDeliveryRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetContentDeliveryRule]]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod]

### versioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.VersioningConfiguration]

### lateDataRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.LateDataRule]]


# UpdateDatastoreRequest

### datastoreName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.RetentionPeriod]

### datastoreStorage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreStorage, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatastoreStorageOutput, NoneType]

### fileFormatConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.FileFormatConfiguration, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.FileFormatConfigurationOutput, NoneType]


# UpdatePipelineRequest

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineActivities
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PipelineActivity, aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.PipelineActivityOutput]]
- **Required**: Yes


# Variable

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stringValue
- **Type**: typing.Optional[str]

### doubleValue
- **Type**: typing.Optional[float]

### datasetContentVersionValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.DatasetContentVersionValue]

### outputFileUriValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotanalytics.iotanalytics_classes.OutputFileUriValue]


# VersioningConfiguration

### unlimited
- **Type**: typing.Optional[bool]

### maxVersions
- **Type**: typing.Optional[int]



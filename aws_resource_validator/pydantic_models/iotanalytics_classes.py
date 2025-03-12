from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.iotanalytics_constants import *

class BatchPutMessageErrorEntryTypeDef(BaseValidatorModel):
    messageId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelPipelineReprocessingRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    reprocessingId: str


class ChannelMessagesTypeDef(BaseValidatorModel):
    s3Paths: Optional[Sequence[str]] = None


class EstimatedResourceSizeTypeDef(BaseValidatorModel):
    estimatedSizeInBytes: Optional[float] = None
    estimatedOn: Optional[datetime] = None


class CustomerManagedChannelS3StorageTypeDef(BaseValidatorModel):
    bucket: str
    roleArn: str
    keyPrefix: Optional[str] = None


class CustomerManagedChannelS3StorageSummaryTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None
    roleArn: Optional[str] = None


class RetentionPeriodTypeDef(BaseValidatorModel):
    unlimited: Optional[bool] = None
    numberOfDays: Optional[int] = None


class ResourceConfigurationTypeDef(BaseValidatorModel):
    computeType: ComputeTypeType
    volumeSizeInGB: int


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class CreateDatasetContentRequestTypeDef(BaseValidatorModel):
    datasetName: str
    versionId: Optional[str] = None


class VersioningConfigurationTypeDef(BaseValidatorModel):
    unlimited: Optional[bool] = None
    maxVersions: Optional[int] = None


class CustomerManagedDatastoreS3StorageSummaryTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None
    roleArn: Optional[str] = None


class CustomerManagedDatastoreS3StorageTypeDef(BaseValidatorModel):
    bucket: str
    roleArn: str
    keyPrefix: Optional[str] = None


class DatasetActionSummaryTypeDef(BaseValidatorModel):
    actionName: Optional[str] = None
    actionType: Optional[DatasetActionTypeType] = None


class IotEventsDestinationConfigurationTypeDef(BaseValidatorModel):
    inputName: str
    roleArn: str


class DatasetContentStatusTypeDef(BaseValidatorModel):
    state: Optional[DatasetContentStateType] = None
    reason: Optional[str] = None


class DatasetContentVersionValueTypeDef(BaseValidatorModel):
    datasetName: str


class DatasetEntryTypeDef(BaseValidatorModel):
    entryName: Optional[str] = None
    dataURI: Optional[str] = None


class ScheduleTypeDef(BaseValidatorModel):
    expression: Optional[str] = None


class TriggeringDatasetTypeDef(BaseValidatorModel):
    name: str


class DatastoreActivityTypeDef(BaseValidatorModel):
    name: str
    datastoreName: str


class IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None


class IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef(BaseValidatorModel):
    bucket: str
    keyPrefix: Optional[str] = None


class PartitionTypeDef(BaseValidatorModel):
    attributeName: str


class TimestampPartitionTypeDef(BaseValidatorModel):
    attributeName: str
    timestampFormat: Optional[str] = None


class DeleteChannelRequestTypeDef(BaseValidatorModel):
    channelName: str


class DeleteDatasetContentRequestTypeDef(BaseValidatorModel):
    datasetName: str
    versionId: Optional[str] = None


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    datasetName: str


class DeleteDatastoreRequestTypeDef(BaseValidatorModel):
    datastoreName: str


class DeletePipelineRequestTypeDef(BaseValidatorModel):
    pipelineName: str


class DeltaTimeSessionWindowConfigurationTypeDef(BaseValidatorModel):
    timeoutInMinutes: int


class DeltaTimeTypeDef(BaseValidatorModel):
    offsetSeconds: int
    timeExpression: str


class DescribeChannelRequestTypeDef(BaseValidatorModel):
    channelName: str
    includeStatistics: Optional[bool] = None


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    datasetName: str


class DescribeDatastoreRequestTypeDef(BaseValidatorModel):
    datastoreName: str
    includeStatistics: Optional[bool] = None


class LoggingOptionsTypeDef(BaseValidatorModel):
    roleArn: str
    level: Literal["ERROR"]
    enabled: bool


class DescribePipelineRequestTypeDef(BaseValidatorModel):
    pipelineName: str


class GetDatasetContentRequestTypeDef(BaseValidatorModel):
    datasetName: str
    versionId: Optional[str] = None


class GlueConfigurationTypeDef(BaseValidatorModel):
    tableName: str
    databaseName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChannelsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatastoresRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPipelinesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class OutputFileUriValueTypeDef(BaseValidatorModel):
    fileName: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class BatchPutMessageResponseTypeDef(BaseValidatorModel):
    batchPutMessageErrorEntries: List[BatchPutMessageErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetContentResponseTypeDef(BaseValidatorModel):
    versionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePipelineResponseTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class RunPipelineActivityResponseTypeDef(BaseValidatorModel):
    payloads: List[bytes]
    logResult: str
    ResponseMetadata: ResponseMetadataTypeDef


class SampleChannelDataResponseTypeDef(BaseValidatorModel):
    payloads: List[bytes]
    ResponseMetadata: ResponseMetadataTypeDef


class StartPipelineReprocessingResponseTypeDef(BaseValidatorModel):
    reprocessingId: str
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class MessageTypeDef(BaseValidatorModel):
    messageId: str
    payload: BlobTypeDef


class ChannelStatisticsTypeDef(BaseValidatorModel):
    size: Optional[EstimatedResourceSizeTypeDef] = None


class DatastoreStatisticsTypeDef(BaseValidatorModel):
    size: Optional[EstimatedResourceSizeTypeDef] = None


class ChannelStorageOutputTypeDef(BaseValidatorModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3StorageTypeDef] = None


class ChannelStorageTypeDef(BaseValidatorModel):
    serviceManagedS3: Optional[Mapping[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3StorageTypeDef] = None


class ChannelStorageSummaryTypeDef(BaseValidatorModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3StorageSummaryTypeDef] = None


class CreateChannelResponseTypeDef(BaseValidatorModel):
    channelName: str
    channelArn: str
    retentionPeriod: RetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetResponseTypeDef(BaseValidatorModel):
    datasetName: str
    datasetArn: str
    retentionPeriod: RetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatastoreResponseTypeDef(BaseValidatorModel):
    datastoreName: str
    datastoreArn: str
    retentionPeriod: RetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ColumnTypeDef(BaseValidatorModel):
    pass


class SchemaDefinitionOutputTypeDef(BaseValidatorModel):
    columns: Optional[List[ColumnTypeDef]] = None


class SchemaDefinitionTypeDef(BaseValidatorModel):
    columns: Optional[Sequence[ColumnTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class DatasetContentSummaryTypeDef(BaseValidatorModel):
    version: Optional[str] = None
    status: Optional[DatasetContentStatusTypeDef] = None
    creationTime: Optional[datetime] = None
    scheduleTime: Optional[datetime] = None
    completionTime: Optional[datetime] = None


class GetDatasetContentResponseTypeDef(BaseValidatorModel):
    entries: List[DatasetEntryTypeDef]
    timestamp: datetime
    status: DatasetContentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DatasetTriggerTypeDef(BaseValidatorModel):
    schedule: Optional[ScheduleTypeDef] = None
    dataset: Optional[TriggeringDatasetTypeDef] = None


class DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef(BaseValidatorModel):
    customerManagedS3Storage: Optional[ IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef ] = None


class DatastoreIotSiteWiseMultiLayerStorageTypeDef(BaseValidatorModel):
    customerManagedS3Storage: IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef


class DatastorePartitionTypeDef(BaseValidatorModel):
    attributePartition: Optional[PartitionTypeDef] = None
    timestampPartition: Optional[TimestampPartitionTypeDef] = None


class LateDataRuleConfigurationTypeDef(BaseValidatorModel):
    deltaTimeSessionWindowConfiguration: Optional[DeltaTimeSessionWindowConfigurationTypeDef] = None


class QueryFilterTypeDef(BaseValidatorModel):
    deltaTime: Optional[DeltaTimeTypeDef] = None


class DescribeLoggingOptionsResponseTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutLoggingOptionsRequestTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef


class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    bucket: str
    key: str
    roleArn: str
    glueConfiguration: Optional[GlueConfigurationTypeDef] = None


class ListChannelsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatastoresRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPipelinesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListDatasetContentsRequestPaginateTypeDef(BaseValidatorModel):
    datasetName: str
    scheduledOnOrAfter: Optional[TimestampTypeDef] = None
    scheduledBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetContentsRequestTypeDef(BaseValidatorModel):
    datasetName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    scheduledOnOrAfter: Optional[TimestampTypeDef] = None
    scheduledBefore: Optional[TimestampTypeDef] = None


class SampleChannelDataRequestTypeDef(BaseValidatorModel):
    channelName: str
    maxMessages: Optional[int] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None


class StartPipelineReprocessingRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    channelMessages: Optional[ChannelMessagesTypeDef] = None


class VariableTypeDef(BaseValidatorModel):
    name: str
    stringValue: Optional[str] = None
    doubleValue: Optional[float] = None
    datasetContentVersionValue: Optional[DatasetContentVersionValueTypeDef] = None
    outputFileUriValue: Optional[OutputFileUriValueTypeDef] = None


class ReprocessingSummaryTypeDef(BaseValidatorModel):
    pass


class PipelineSummaryTypeDef(BaseValidatorModel):
    pipelineName: Optional[str] = None
    reprocessingSummaries: Optional[List[ReprocessingSummaryTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None


class BatchPutMessageRequestTypeDef(BaseValidatorModel):
    channelName: str
    messages: Sequence[MessageTypeDef]


class ChannelTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    storage: Optional[ChannelStorageOutputTypeDef] = None
    arn: Optional[str] = None
    status: Optional[ChannelStatusType] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None


class ChannelSummaryTypeDef(BaseValidatorModel):
    channelName: Optional[str] = None
    channelStorage: Optional[ChannelStorageSummaryTypeDef] = None
    status: Optional[ChannelStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None


class ParquetConfigurationOutputTypeDef(BaseValidatorModel):
    schemaDefinition: Optional[SchemaDefinitionOutputTypeDef] = None


class ParquetConfigurationTypeDef(BaseValidatorModel):
    schemaDefinition: Optional[SchemaDefinitionTypeDef] = None


class ListDatasetContentsResponseTypeDef(BaseValidatorModel):
    datasetContentSummaries: List[DatasetContentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DatasetSummaryTypeDef(BaseValidatorModel):
    datasetName: Optional[str] = None
    status: Optional[DatasetStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    triggers: Optional[List[DatasetTriggerTypeDef]] = None
    actions: Optional[List[DatasetActionSummaryTypeDef]] = None


class DatastoreStorageSummaryTypeDef(BaseValidatorModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedDatastoreS3StorageSummaryTypeDef] = None
    iotSiteWiseMultiLayerStorage: Optional[DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef] = None


class DatastoreStorageOutputTypeDef(BaseValidatorModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedDatastoreS3StorageTypeDef] = None
    iotSiteWiseMultiLayerStorage: Optional[DatastoreIotSiteWiseMultiLayerStorageTypeDef] = None


class DatastoreStorageTypeDef(BaseValidatorModel):
    serviceManagedS3: Optional[Mapping[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedDatastoreS3StorageTypeDef] = None
    iotSiteWiseMultiLayerStorage: Optional[DatastoreIotSiteWiseMultiLayerStorageTypeDef] = None


class DatastorePartitionsOutputTypeDef(BaseValidatorModel):
    partitions: Optional[List[DatastorePartitionTypeDef]] = None


class DatastorePartitionsTypeDef(BaseValidatorModel):
    partitions: Optional[Sequence[DatastorePartitionTypeDef]] = None


class LateDataRuleTypeDef(BaseValidatorModel):
    ruleConfiguration: LateDataRuleConfigurationTypeDef
    ruleName: Optional[str] = None


class SqlQueryDatasetActionOutputTypeDef(BaseValidatorModel):
    sqlQuery: str
    filters: Optional[List[QueryFilterTypeDef]] = None


class SqlQueryDatasetActionTypeDef(BaseValidatorModel):
    sqlQuery: str
    filters: Optional[Sequence[QueryFilterTypeDef]] = None


class DatasetContentDeliveryDestinationTypeDef(BaseValidatorModel):
    iotEventsDestinationConfiguration: Optional[IotEventsDestinationConfigurationTypeDef] = None
    s3DestinationConfiguration: Optional[S3DestinationConfigurationTypeDef] = None


class ContainerDatasetActionOutputTypeDef(BaseValidatorModel):
    image: str
    executionRoleArn: str
    resourceConfiguration: ResourceConfigurationTypeDef
    variables: Optional[List[VariableTypeDef]] = None


class ContainerDatasetActionTypeDef(BaseValidatorModel):
    image: str
    executionRoleArn: str
    resourceConfiguration: ResourceConfigurationTypeDef
    variables: Optional[Sequence[VariableTypeDef]] = None


class PipelineActivityOutputTypeDef(BaseValidatorModel):
    pass


class PipelineTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    activities: Optional[List[PipelineActivityOutputTypeDef]] = None
    reprocessingSummaries: Optional[List[ReprocessingSummaryTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None


class ListPipelinesResponseTypeDef(BaseValidatorModel):
    pipelineSummaries: List[PipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeChannelResponseTypeDef(BaseValidatorModel):
    channel: ChannelTypeDef
    statistics: ChannelStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ChannelStorageUnionTypeDef(BaseValidatorModel):
    pass


class CreateChannelRequestTypeDef(BaseValidatorModel):
    channelName: str
    channelStorage: Optional[ChannelStorageUnionTypeDef] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateChannelRequestTypeDef(BaseValidatorModel):
    channelName: str
    channelStorage: Optional[ChannelStorageUnionTypeDef] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None


class ListChannelsResponseTypeDef(BaseValidatorModel):
    channelSummaries: List[ChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FileFormatConfigurationOutputTypeDef(BaseValidatorModel):
    jsonConfiguration: Optional[Dict[str, Any]] = None
    parquetConfiguration: Optional[ParquetConfigurationOutputTypeDef] = None


class FileFormatConfigurationTypeDef(BaseValidatorModel):
    jsonConfiguration: Optional[Mapping[str, Any]] = None
    parquetConfiguration: Optional[ParquetConfigurationTypeDef] = None


class ListDatasetsResponseTypeDef(BaseValidatorModel):
    datasetSummaries: List[DatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DatastoreSummaryTypeDef(BaseValidatorModel):
    datastoreName: Optional[str] = None
    datastoreStorage: Optional[DatastoreStorageSummaryTypeDef] = None
    status: Optional[DatastoreStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None
    fileFormatType: Optional[FileFormatTypeType] = None
    datastorePartitions: Optional[DatastorePartitionsOutputTypeDef] = None


class DatasetContentDeliveryRuleTypeDef(BaseValidatorModel):
    destination: DatasetContentDeliveryDestinationTypeDef
    entryName: Optional[str] = None


class DatasetActionOutputTypeDef(BaseValidatorModel):
    actionName: Optional[str] = None
    queryAction: Optional[SqlQueryDatasetActionOutputTypeDef] = None
    containerAction: Optional[ContainerDatasetActionOutputTypeDef] = None


class DescribePipelineResponseTypeDef(BaseValidatorModel):
    pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DatastoreTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    storage: Optional[DatastoreStorageOutputTypeDef] = None
    arn: Optional[str] = None
    status: Optional[DatastoreStatusType] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationOutputTypeDef] = None
    datastorePartitions: Optional[DatastorePartitionsOutputTypeDef] = None


class ListDatastoresResponseTypeDef(BaseValidatorModel):
    datastoreSummaries: List[DatastoreSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DatasetTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    actions: Optional[List[DatasetActionOutputTypeDef]] = None
    triggers: Optional[List[DatasetTriggerTypeDef]] = None
    contentDeliveryRules: Optional[List[DatasetContentDeliveryRuleTypeDef]] = None
    status: Optional[DatasetStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    versioningConfiguration: Optional[VersioningConfigurationTypeDef] = None
    lateDataRules: Optional[List[LateDataRuleTypeDef]] = None


class SqlQueryDatasetActionUnionTypeDef(BaseValidatorModel):
    pass


class ContainerDatasetActionUnionTypeDef(BaseValidatorModel):
    pass


class DatasetActionTypeDef(BaseValidatorModel):
    actionName: Optional[str] = None
    queryAction: Optional[SqlQueryDatasetActionUnionTypeDef] = None
    containerAction: Optional[ContainerDatasetActionUnionTypeDef] = None


class PipelineActivityUnionTypeDef(BaseValidatorModel):
    pass


class CreatePipelineRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityUnionTypeDef]
    tags: Optional[Sequence[TagTypeDef]] = None


class RunPipelineActivityRequestTypeDef(BaseValidatorModel):
    pipelineActivity: PipelineActivityUnionTypeDef
    payloads: Sequence[BlobTypeDef]


class UpdatePipelineRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityUnionTypeDef]


class DescribeDatastoreResponseTypeDef(BaseValidatorModel):
    datastore: DatastoreTypeDef
    statistics: DatastoreStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FileFormatConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class DatastorePartitionsUnionTypeDef(BaseValidatorModel):
    pass


class DatastoreStorageUnionTypeDef(BaseValidatorModel):
    pass


class CreateDatastoreRequestTypeDef(BaseValidatorModel):
    datastoreName: str
    datastoreStorage: Optional[DatastoreStorageUnionTypeDef] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationUnionTypeDef] = None
    datastorePartitions: Optional[DatastorePartitionsUnionTypeDef] = None


class UpdateDatastoreRequestTypeDef(BaseValidatorModel):
    datastoreName: str
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    datastoreStorage: Optional[DatastoreStorageUnionTypeDef] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationUnionTypeDef] = None


class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DatasetActionUnionTypeDef(BaseValidatorModel):
    pass


class CreateDatasetRequestTypeDef(BaseValidatorModel):
    datasetName: str
    actions: Sequence[DatasetActionUnionTypeDef]
    triggers: Optional[Sequence[DatasetTriggerTypeDef]] = None
    contentDeliveryRules: Optional[Sequence[DatasetContentDeliveryRuleTypeDef]] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    versioningConfiguration: Optional[VersioningConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    lateDataRules: Optional[Sequence[LateDataRuleTypeDef]] = None


class UpdateDatasetRequestTypeDef(BaseValidatorModel):
    datasetName: str
    actions: Sequence[DatasetActionUnionTypeDef]
    triggers: Optional[Sequence[DatasetTriggerTypeDef]] = None
    contentDeliveryRules: Optional[Sequence[DatasetContentDeliveryRuleTypeDef]] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    versioningConfiguration: Optional[VersioningConfigurationTypeDef] = None
    lateDataRules: Optional[Sequence[LateDataRuleTypeDef]] = None



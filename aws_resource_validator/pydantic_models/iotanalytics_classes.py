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

class BatchPutMessageErrorEntry(BaseValidatorModel):
    messageId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelPipelineReprocessingRequest(BaseValidatorModel):
    pipelineName: str
    reprocessingId: str


class ChannelMessages(BaseValidatorModel):
    s3Paths: Optional[Sequence[str]] = None


class EstimatedResourceSize(BaseValidatorModel):
    estimatedSizeInBytes: Optional[float] = None
    estimatedOn: Optional[datetime] = None


class CustomerManagedChannelS3Storage(BaseValidatorModel):
    bucket: str
    roleArn: str
    keyPrefix: Optional[str] = None


class CustomerManagedChannelS3StorageSummary(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None
    roleArn: Optional[str] = None


class RetentionPeriod(BaseValidatorModel):
    unlimited: Optional[bool] = None
    numberOfDays: Optional[int] = None


class ResourceConfiguration(BaseValidatorModel):
    computeType: ComputeTypeType
    volumeSizeInGB: int


class Tag(BaseValidatorModel):
    key: str
    value: str


class CreateDatasetContentRequest(BaseValidatorModel):
    datasetName: str
    versionId: Optional[str] = None


class VersioningConfiguration(BaseValidatorModel):
    unlimited: Optional[bool] = None
    maxVersions: Optional[int] = None


class CustomerManagedDatastoreS3StorageSummary(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None
    roleArn: Optional[str] = None


class CustomerManagedDatastoreS3Storage(BaseValidatorModel):
    bucket: str
    roleArn: str
    keyPrefix: Optional[str] = None


class DatasetActionSummary(BaseValidatorModel):
    actionName: Optional[str] = None
    actionType: Optional[DatasetActionTypeType] = None


class IotEventsDestinationConfiguration(BaseValidatorModel):
    inputName: str
    roleArn: str


class DatasetContentStatus(BaseValidatorModel):
    state: Optional[DatasetContentStateType] = None
    reason: Optional[str] = None


class DatasetContentVersionValue(BaseValidatorModel):
    datasetName: str


class DatasetEntry(BaseValidatorModel):
    entryName: Optional[str] = None
    dataURI: Optional[str] = None


class Schedule(BaseValidatorModel):
    expression: Optional[str] = None


class TriggeringDataset(BaseValidatorModel):
    name: str


class DatastoreActivity(BaseValidatorModel):
    name: str
    datastoreName: str


class IotSiteWiseCustomerManagedDatastoreS3StorageSummary(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None


class IotSiteWiseCustomerManagedDatastoreS3Storage(BaseValidatorModel):
    bucket: str
    keyPrefix: Optional[str] = None


class Partition(BaseValidatorModel):
    attributeName: str


class TimestampPartition(BaseValidatorModel):
    attributeName: str
    timestampFormat: Optional[str] = None


class DeleteChannelRequest(BaseValidatorModel):
    channelName: str


class DeleteDatasetContentRequest(BaseValidatorModel):
    datasetName: str
    versionId: Optional[str] = None


class DeleteDatasetRequest(BaseValidatorModel):
    datasetName: str


class DeleteDatastoreRequest(BaseValidatorModel):
    datastoreName: str


class DeletePipelineRequest(BaseValidatorModel):
    pipelineName: str


class DeltaTimeSessionWindowConfiguration(BaseValidatorModel):
    timeoutInMinutes: int


class DeltaTime(BaseValidatorModel):
    offsetSeconds: int
    timeExpression: str


class DescribeChannelRequest(BaseValidatorModel):
    channelName: str
    includeStatistics: Optional[bool] = None


class DescribeDatasetRequest(BaseValidatorModel):
    datasetName: str


class DescribeDatastoreRequest(BaseValidatorModel):
    datastoreName: str
    includeStatistics: Optional[bool] = None


class LoggingOptions(BaseValidatorModel):
    roleArn: str
    level: Literal["ERROR"]
    enabled: bool


class DescribePipelineRequest(BaseValidatorModel):
    pipelineName: str


class GetDatasetContentRequest(BaseValidatorModel):
    datasetName: str
    versionId: Optional[str] = None


class GlueConfiguration(BaseValidatorModel):
    tableName: str
    databaseName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChannelsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatastoresRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPipelinesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class OutputFileUriValue(BaseValidatorModel):
    fileName: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class BatchPutMessageResponse(BaseValidatorModel):
    batchPutMessageErrorEntries: List[BatchPutMessageErrorEntry]
    ResponseMetadata: ResponseMetadata


class CreateDatasetContentResponse(BaseValidatorModel):
    versionId: str
    ResponseMetadata: ResponseMetadata


class CreatePipelineResponse(BaseValidatorModel):
    pipelineName: str
    pipelineArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class RunPipelineActivityResponse(BaseValidatorModel):
    payloads: List[bytes]
    logResult: str
    ResponseMetadata: ResponseMetadata


class SampleChannelDataResponse(BaseValidatorModel):
    payloads: List[bytes]
    ResponseMetadata: ResponseMetadata


class StartPipelineReprocessingResponse(BaseValidatorModel):
    reprocessingId: str
    ResponseMetadata: ResponseMetadata


class Blob(BaseValidatorModel):
    pass


class Message(BaseValidatorModel):
    messageId: str
    payload: Blob


class ChannelStatistics(BaseValidatorModel):
    size: Optional[EstimatedResourceSize] = None


class DatastoreStatistics(BaseValidatorModel):
    size: Optional[EstimatedResourceSize] = None


class ChannelStorageOutput(BaseValidatorModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3Storage] = None


class ChannelStorage(BaseValidatorModel):
    serviceManagedS3: Optional[Mapping[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3Storage] = None


class ChannelStorageSummary(BaseValidatorModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3StorageSummary] = None


class CreateChannelResponse(BaseValidatorModel):
    channelName: str
    channelArn: str
    retentionPeriod: RetentionPeriod
    ResponseMetadata: ResponseMetadata


class CreateDatasetResponse(BaseValidatorModel):
    datasetName: str
    datasetArn: str
    retentionPeriod: RetentionPeriod
    ResponseMetadata: ResponseMetadata


class CreateDatastoreResponse(BaseValidatorModel):
    datastoreName: str
    datastoreArn: str
    retentionPeriod: RetentionPeriod
    ResponseMetadata: ResponseMetadata


class Column(BaseValidatorModel):
    pass


class SchemaDefinitionOutput(BaseValidatorModel):
    columns: Optional[List[Column]] = None


class SchemaDefinition(BaseValidatorModel):
    columns: Optional[Sequence[Column]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[Tag]


class DatasetContentSummary(BaseValidatorModel):
    version: Optional[str] = None
    status: Optional[DatasetContentStatus] = None
    creationTime: Optional[datetime] = None
    scheduleTime: Optional[datetime] = None
    completionTime: Optional[datetime] = None


class GetDatasetContentResponse(BaseValidatorModel):
    entries: List[DatasetEntry]
    timestamp: datetime
    status: DatasetContentStatus
    ResponseMetadata: ResponseMetadata


class DatasetTrigger(BaseValidatorModel):
    schedule: Optional[Schedule] = None
    dataset: Optional[TriggeringDataset] = None


class DatastoreIotSiteWiseMultiLayerStorageSummary(BaseValidatorModel):
    customerManagedS3Storage: Optional[ IotSiteWiseCustomerManagedDatastoreS3StorageSummary ] = None


class DatastoreIotSiteWiseMultiLayerStorage(BaseValidatorModel):
    customerManagedS3Storage: IotSiteWiseCustomerManagedDatastoreS3Storage


class DatastorePartition(BaseValidatorModel):
    attributePartition: Optional[Partition] = None
    timestampPartition: Optional[TimestampPartition] = None


class LateDataRuleConfiguration(BaseValidatorModel):
    deltaTimeSessionWindowConfiguration: Optional[DeltaTimeSessionWindowConfiguration] = None


class QueryFilter(BaseValidatorModel):
    deltaTime: Optional[DeltaTime] = None


class DescribeLoggingOptionsResponse(BaseValidatorModel):
    loggingOptions: LoggingOptions
    ResponseMetadata: ResponseMetadata


class PutLoggingOptionsRequest(BaseValidatorModel):
    loggingOptions: LoggingOptions


class S3DestinationConfiguration(BaseValidatorModel):
    bucket: str
    key: str
    roleArn: str
    glueConfiguration: Optional[GlueConfiguration] = None


class ListChannelsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatastoresRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipelinesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class ListDatasetContentsRequestPaginate(BaseValidatorModel):
    datasetName: str
    scheduledOnOrAfter: Optional[Timestamp] = None
    scheduledBefore: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetContentsRequest(BaseValidatorModel):
    datasetName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    scheduledOnOrAfter: Optional[Timestamp] = None
    scheduledBefore: Optional[Timestamp] = None


class SampleChannelDataRequest(BaseValidatorModel):
    channelName: str
    maxMessages: Optional[int] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None


class StartPipelineReprocessingRequest(BaseValidatorModel):
    pipelineName: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    channelMessages: Optional[ChannelMessages] = None


class Variable(BaseValidatorModel):
    name: str
    stringValue: Optional[str] = None
    doubleValue: Optional[float] = None
    datasetContentVersionValue: Optional[DatasetContentVersionValue] = None
    outputFileUriValue: Optional[OutputFileUriValue] = None


class ReprocessingSummary(BaseValidatorModel):
    pass


class PipelineSummary(BaseValidatorModel):
    pipelineName: Optional[str] = None
    reprocessingSummaries: Optional[List[ReprocessingSummary]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None


class BatchPutMessageRequest(BaseValidatorModel):
    channelName: str
    messages: Sequence[Message]


class Channel(BaseValidatorModel):
    name: Optional[str] = None
    storage: Optional[ChannelStorageOutput] = None
    arn: Optional[str] = None
    status: Optional[ChannelStatusType] = None
    retentionPeriod: Optional[RetentionPeriod] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None


class ChannelSummary(BaseValidatorModel):
    channelName: Optional[str] = None
    channelStorage: Optional[ChannelStorageSummary] = None
    status: Optional[ChannelStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None


class ParquetConfigurationOutput(BaseValidatorModel):
    schemaDefinition: Optional[SchemaDefinitionOutput] = None


class ParquetConfiguration(BaseValidatorModel):
    schemaDefinition: Optional[SchemaDefinition] = None


class ListDatasetContentsResponse(BaseValidatorModel):
    datasetContentSummaries: List[DatasetContentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DatasetSummary(BaseValidatorModel):
    datasetName: Optional[str] = None
    status: Optional[DatasetStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    triggers: Optional[List[DatasetTrigger]] = None
    actions: Optional[List[DatasetActionSummary]] = None


class DatastoreStorageSummary(BaseValidatorModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedDatastoreS3StorageSummary] = None
    iotSiteWiseMultiLayerStorage: Optional[DatastoreIotSiteWiseMultiLayerStorageSummary] = None


class DatastoreStorageOutput(BaseValidatorModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedDatastoreS3Storage] = None
    iotSiteWiseMultiLayerStorage: Optional[DatastoreIotSiteWiseMultiLayerStorage] = None


class DatastoreStorage(BaseValidatorModel):
    serviceManagedS3: Optional[Mapping[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedDatastoreS3Storage] = None
    iotSiteWiseMultiLayerStorage: Optional[DatastoreIotSiteWiseMultiLayerStorage] = None


class DatastorePartitionsOutput(BaseValidatorModel):
    partitions: Optional[List[DatastorePartition]] = None


class DatastorePartitions(BaseValidatorModel):
    partitions: Optional[Sequence[DatastorePartition]] = None


class LateDataRule(BaseValidatorModel):
    ruleConfiguration: LateDataRuleConfiguration
    ruleName: Optional[str] = None


class SqlQueryDatasetActionOutput(BaseValidatorModel):
    sqlQuery: str
    filters: Optional[List[QueryFilter]] = None


class SqlQueryDatasetAction(BaseValidatorModel):
    sqlQuery: str
    filters: Optional[Sequence[QueryFilter]] = None


class DatasetContentDeliveryDestination(BaseValidatorModel):
    iotEventsDestinationConfiguration: Optional[IotEventsDestinationConfiguration] = None
    s3DestinationConfiguration: Optional[S3DestinationConfiguration] = None


class ContainerDatasetActionOutput(BaseValidatorModel):
    image: str
    executionRoleArn: str
    resourceConfiguration: ResourceConfiguration
    variables: Optional[List[Variable]] = None


class ContainerDatasetAction(BaseValidatorModel):
    image: str
    executionRoleArn: str
    resourceConfiguration: ResourceConfiguration
    variables: Optional[Sequence[Variable]] = None


class PipelineActivityOutput(BaseValidatorModel):
    pass


class Pipeline(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    activities: Optional[List[PipelineActivityOutput]] = None
    reprocessingSummaries: Optional[List[ReprocessingSummary]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None


class ListPipelinesResponse(BaseValidatorModel):
    pipelineSummaries: List[PipelineSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeChannelResponse(BaseValidatorModel):
    channel: Channel
    statistics: ChannelStatistics
    ResponseMetadata: ResponseMetadata


class ChannelStorageUnion(BaseValidatorModel):
    pass


class CreateChannelRequest(BaseValidatorModel):
    channelName: str
    channelStorage: Optional[ChannelStorageUnion] = None
    retentionPeriod: Optional[RetentionPeriod] = None
    tags: Optional[Sequence[Tag]] = None


class UpdateChannelRequest(BaseValidatorModel):
    channelName: str
    channelStorage: Optional[ChannelStorageUnion] = None
    retentionPeriod: Optional[RetentionPeriod] = None


class ListChannelsResponse(BaseValidatorModel):
    channelSummaries: List[ChannelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FileFormatConfigurationOutput(BaseValidatorModel):
    jsonConfiguration: Optional[Dict[str, Any]] = None
    parquetConfiguration: Optional[ParquetConfigurationOutput] = None


class FileFormatConfiguration(BaseValidatorModel):
    jsonConfiguration: Optional[Mapping[str, Any]] = None
    parquetConfiguration: Optional[ParquetConfiguration] = None


class ListDatasetsResponse(BaseValidatorModel):
    datasetSummaries: List[DatasetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DatastoreSummary(BaseValidatorModel):
    datastoreName: Optional[str] = None
    datastoreStorage: Optional[DatastoreStorageSummary] = None
    status: Optional[DatastoreStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None
    fileFormatType: Optional[FileFormatTypeType] = None
    datastorePartitions: Optional[DatastorePartitionsOutput] = None


class DatasetContentDeliveryRule(BaseValidatorModel):
    destination: DatasetContentDeliveryDestination
    entryName: Optional[str] = None


class DatasetActionOutput(BaseValidatorModel):
    actionName: Optional[str] = None
    queryAction: Optional[SqlQueryDatasetActionOutput] = None
    containerAction: Optional[ContainerDatasetActionOutput] = None


class DescribePipelineResponse(BaseValidatorModel):
    pipeline: Pipeline
    ResponseMetadata: ResponseMetadata


class Datastore(BaseValidatorModel):
    name: Optional[str] = None
    storage: Optional[DatastoreStorageOutput] = None
    arn: Optional[str] = None
    status: Optional[DatastoreStatusType] = None
    retentionPeriod: Optional[RetentionPeriod] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationOutput] = None
    datastorePartitions: Optional[DatastorePartitionsOutput] = None


class ListDatastoresResponse(BaseValidatorModel):
    datastoreSummaries: List[DatastoreSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Dataset(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    actions: Optional[List[DatasetActionOutput]] = None
    triggers: Optional[List[DatasetTrigger]] = None
    contentDeliveryRules: Optional[List[DatasetContentDeliveryRule]] = None
    status: Optional[DatasetStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    retentionPeriod: Optional[RetentionPeriod] = None
    versioningConfiguration: Optional[VersioningConfiguration] = None
    lateDataRules: Optional[List[LateDataRule]] = None


class SqlQueryDatasetActionUnion(BaseValidatorModel):
    pass


class ContainerDatasetActionUnion(BaseValidatorModel):
    pass


class DatasetAction(BaseValidatorModel):
    actionName: Optional[str] = None
    queryAction: Optional[SqlQueryDatasetActionUnion] = None
    containerAction: Optional[ContainerDatasetActionUnion] = None


class PipelineActivityUnion(BaseValidatorModel):
    pass


class CreatePipelineRequest(BaseValidatorModel):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityUnion]
    tags: Optional[Sequence[Tag]] = None


class RunPipelineActivityRequest(BaseValidatorModel):
    pipelineActivity: PipelineActivityUnion
    payloads: Sequence[Blob]


class UpdatePipelineRequest(BaseValidatorModel):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityUnion]


class DescribeDatastoreResponse(BaseValidatorModel):
    datastore: Datastore
    statistics: DatastoreStatistics
    ResponseMetadata: ResponseMetadata


class FileFormatConfigurationUnion(BaseValidatorModel):
    pass


class DatastorePartitionsUnion(BaseValidatorModel):
    pass


class DatastoreStorageUnion(BaseValidatorModel):
    pass


class CreateDatastoreRequest(BaseValidatorModel):
    datastoreName: str
    datastoreStorage: Optional[DatastoreStorageUnion] = None
    retentionPeriod: Optional[RetentionPeriod] = None
    tags: Optional[Sequence[Tag]] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationUnion] = None
    datastorePartitions: Optional[DatastorePartitionsUnion] = None


class UpdateDatastoreRequest(BaseValidatorModel):
    datastoreName: str
    retentionPeriod: Optional[RetentionPeriod] = None
    datastoreStorage: Optional[DatastoreStorageUnion] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationUnion] = None


class DescribeDatasetResponse(BaseValidatorModel):
    dataset: Dataset
    ResponseMetadata: ResponseMetadata


class DatasetActionUnion(BaseValidatorModel):
    pass


class CreateDatasetRequest(BaseValidatorModel):
    datasetName: str
    actions: Sequence[DatasetActionUnion]
    triggers: Optional[Sequence[DatasetTrigger]] = None
    contentDeliveryRules: Optional[Sequence[DatasetContentDeliveryRule]] = None
    retentionPeriod: Optional[RetentionPeriod] = None
    versioningConfiguration: Optional[VersioningConfiguration] = None
    tags: Optional[Sequence[Tag]] = None
    lateDataRules: Optional[Sequence[LateDataRule]] = None


class UpdateDatasetRequest(BaseValidatorModel):
    datasetName: str
    actions: Sequence[DatasetActionUnion]
    triggers: Optional[Sequence[DatasetTrigger]] = None
    contentDeliveryRules: Optional[Sequence[DatasetContentDeliveryRule]] = None
    retentionPeriod: Optional[RetentionPeriod] = None
    versioningConfiguration: Optional[VersioningConfiguration] = None
    lateDataRules: Optional[Sequence[LateDataRule]] = None



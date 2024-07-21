from datetime import datetime
from pydantic import BaseModel
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

class AddAttributesActivityTypeDef(BaseModel):
    name: str
    attributes: Mapping[str, str]
    next: Optional[str] = None

class BatchPutMessageErrorEntryTypeDef(BaseModel):
    messageId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CancelPipelineReprocessingRequestRequestTypeDef(BaseModel):
    pipelineName: str
    reprocessingId: str

class ChannelActivityTypeDef(BaseModel):
    name: str
    channelName: str
    next: Optional[str] = None

class ChannelMessagesTypeDef(BaseModel):
    s3Paths: Optional[Sequence[str]] = None

class EstimatedResourceSizeTypeDef(BaseModel):
    estimatedSizeInBytes: Optional[float] = None
    estimatedOn: Optional[datetime] = None

class CustomerManagedChannelS3StorageSummaryTypeDef(BaseModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None
    roleArn: Optional[str] = None

class CustomerManagedChannelS3StorageTypeDef(BaseModel):
    bucket: str
    roleArn: str
    keyPrefix: Optional[str] = None

class RetentionPeriodTypeDef(BaseModel):
    unlimited: Optional[bool] = None
    numberOfDays: Optional[int] = None

class ColumnTypeDef(BaseModel):
    name: str
    type: str

class ResourceConfigurationTypeDef(BaseModel):
    computeType: ComputeTypeType
    volumeSizeInGB: int

class TagTypeDef(BaseModel):
    key: str
    value: str

class CreateDatasetContentRequestRequestTypeDef(BaseModel):
    datasetName: str
    versionId: Optional[str] = None

class VersioningConfigurationTypeDef(BaseModel):
    unlimited: Optional[bool] = None
    maxVersions: Optional[int] = None

class CustomerManagedDatastoreS3StorageSummaryTypeDef(BaseModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None
    roleArn: Optional[str] = None

class CustomerManagedDatastoreS3StorageTypeDef(BaseModel):
    bucket: str
    roleArn: str
    keyPrefix: Optional[str] = None

class DatasetActionSummaryTypeDef(BaseModel):
    actionName: Optional[str] = None
    actionType: Optional[DatasetActionTypeType] = None

class IotEventsDestinationConfigurationTypeDef(BaseModel):
    inputName: str
    roleArn: str

class DatasetContentStatusTypeDef(BaseModel):
    state: Optional[DatasetContentStateType] = None
    reason: Optional[str] = None

class DatasetContentVersionValueTypeDef(BaseModel):
    datasetName: str

class DatasetEntryTypeDef(BaseModel):
    entryName: Optional[str] = None
    dataURI: Optional[str] = None

class ScheduleTypeDef(BaseModel):
    expression: Optional[str] = None

class TriggeringDatasetTypeDef(BaseModel):
    name: str

class DatastoreActivityTypeDef(BaseModel):
    name: str
    datastoreName: str

class IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef(BaseModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None

class IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef(BaseModel):
    bucket: str
    keyPrefix: Optional[str] = None

class PartitionTypeDef(BaseModel):
    attributeName: str

class TimestampPartitionTypeDef(BaseModel):
    attributeName: str
    timestampFormat: Optional[str] = None

class DeleteChannelRequestRequestTypeDef(BaseModel):
    channelName: str

class DeleteDatasetContentRequestRequestTypeDef(BaseModel):
    datasetName: str
    versionId: Optional[str] = None

class DeleteDatasetRequestRequestTypeDef(BaseModel):
    datasetName: str

class DeleteDatastoreRequestRequestTypeDef(BaseModel):
    datastoreName: str

class DeletePipelineRequestRequestTypeDef(BaseModel):
    pipelineName: str

class DeltaTimeSessionWindowConfigurationTypeDef(BaseModel):
    timeoutInMinutes: int

class DeltaTimeTypeDef(BaseModel):
    offsetSeconds: int
    timeExpression: str

class DescribeChannelRequestRequestTypeDef(BaseModel):
    channelName: str
    includeStatistics: Optional[bool] = None

class DescribeDatasetRequestRequestTypeDef(BaseModel):
    datasetName: str

class DescribeDatastoreRequestRequestTypeDef(BaseModel):
    datastoreName: str
    includeStatistics: Optional[bool] = None

class LoggingOptionsTypeDef(BaseModel):
    roleArn: str
    level: Literal["ERROR"]
    enabled: bool

class DescribePipelineRequestRequestTypeDef(BaseModel):
    pipelineName: str

class DeviceRegistryEnrichActivityTypeDef(BaseModel):
    name: str
    attribute: str
    thingName: str
    roleArn: str
    next: Optional[str] = None

class DeviceShadowEnrichActivityTypeDef(BaseModel):
    name: str
    attribute: str
    thingName: str
    roleArn: str
    next: Optional[str] = None

class FilterActivityTypeDef(BaseModel):
    name: str
    filter: str
    next: Optional[str] = None

class GetDatasetContentRequestRequestTypeDef(BaseModel):
    datasetName: str
    versionId: Optional[str] = None

class GlueConfigurationTypeDef(BaseModel):
    tableName: str
    databaseName: str

class LambdaActivityTypeDef(BaseModel):
    name: str
    lambdaName: str
    batchSize: int
    next: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatasetsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatastoresRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPipelinesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class MathActivityTypeDef(BaseModel):
    name: str
    attribute: str
    math: str
    next: Optional[str] = None

class OutputFileUriValueTypeDef(BaseModel):
    fileName: str

class RemoveAttributesActivityTypeDef(BaseModel):
    name: str
    attributes: Sequence[str]
    next: Optional[str] = None

class SelectAttributesActivityTypeDef(BaseModel):
    name: str
    attributes: Sequence[str]
    next: Optional[str] = None

class ReprocessingSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    status: Optional[ReprocessingStatusType] = None
    creationTime: Optional[datetime] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchPutMessageResponseTypeDef(BaseModel):
    batchPutMessageErrorEntries: List[BatchPutMessageErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetContentResponseTypeDef(BaseModel):
    versionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePipelineResponseTypeDef(BaseModel):
    pipelineName: str
    pipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class RunPipelineActivityResponseTypeDef(BaseModel):
    payloads: List[bytes]
    logResult: str
    ResponseMetadata: ResponseMetadataTypeDef

class SampleChannelDataResponseTypeDef(BaseModel):
    payloads: List[bytes]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipelineReprocessingResponseTypeDef(BaseModel):
    reprocessingId: str
    ResponseMetadata: ResponseMetadataTypeDef

class MessageTypeDef(BaseModel):
    messageId: str
    payload: BlobTypeDef

class ChannelStatisticsTypeDef(BaseModel):
    size: Optional[EstimatedResourceSizeTypeDef] = None

class DatastoreStatisticsTypeDef(BaseModel):
    size: Optional[EstimatedResourceSizeTypeDef] = None

class ChannelStorageSummaryTypeDef(BaseModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3StorageSummaryTypeDef] = None

class ChannelStorageTypeDef(BaseModel):
    serviceManagedS3: Optional[Mapping[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3StorageTypeDef] = None

class CreateChannelResponseTypeDef(BaseModel):
    channelName: str
    channelArn: str
    retentionPeriod: RetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(BaseModel):
    datasetName: str
    datasetArn: str
    retentionPeriod: RetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatastoreResponseTypeDef(BaseModel):
    datastoreName: str
    datastoreArn: str
    retentionPeriod: RetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SchemaDefinitionTypeDef(BaseModel):
    columns: Optional[Sequence[ColumnTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class DatasetContentSummaryTypeDef(BaseModel):
    version: Optional[str] = None
    status: Optional[DatasetContentStatusTypeDef] = None
    creationTime: Optional[datetime] = None
    scheduleTime: Optional[datetime] = None
    completionTime: Optional[datetime] = None

class GetDatasetContentResponseTypeDef(BaseModel):
    entries: List[DatasetEntryTypeDef]
    timestamp: datetime
    status: DatasetContentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetTriggerTypeDef(BaseModel):
    schedule: Optional[ScheduleTypeDef] = None
    dataset: Optional[TriggeringDatasetTypeDef] = None

class DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef(BaseModel):
    customerManagedS3Storage: Optional[       IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef     ] = None

class DatastoreIotSiteWiseMultiLayerStorageTypeDef(BaseModel):
    customerManagedS3Storage: IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef

class DatastorePartitionTypeDef(BaseModel):
    attributePartition: Optional[PartitionTypeDef] = None
    timestampPartition: Optional[TimestampPartitionTypeDef] = None

class LateDataRuleConfigurationTypeDef(BaseModel):
    deltaTimeSessionWindowConfiguration: Optional[       DeltaTimeSessionWindowConfigurationTypeDef     ] = None

class QueryFilterTypeDef(BaseModel):
    deltaTime: Optional[DeltaTimeTypeDef] = None

class DescribeLoggingOptionsResponseTypeDef(BaseModel):
    loggingOptions: LoggingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestRequestTypeDef(BaseModel):
    loggingOptions: LoggingOptionsTypeDef

class S3DestinationConfigurationTypeDef(BaseModel):
    bucket: str
    key: str
    roleArn: str
    glueConfiguration: Optional[GlueConfigurationTypeDef] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetsRequestListDatasetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatastoresRequestListDatastoresPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesRequestListPipelinesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetContentsRequestListDatasetContentsPaginateTypeDef(BaseModel):
    datasetName: str
    scheduledOnOrAfter: Optional[TimestampTypeDef] = None
    scheduledBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetContentsRequestRequestTypeDef(BaseModel):
    datasetName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    scheduledOnOrAfter: Optional[TimestampTypeDef] = None
    scheduledBefore: Optional[TimestampTypeDef] = None

class SampleChannelDataRequestRequestTypeDef(BaseModel):
    channelName: str
    maxMessages: Optional[int] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None

class StartPipelineReprocessingRequestRequestTypeDef(BaseModel):
    pipelineName: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    channelMessages: Optional[ChannelMessagesTypeDef] = None

class VariableTypeDef(BaseModel):
    name: str
    stringValue: Optional[str] = None
    doubleValue: Optional[float] = None
    datasetContentVersionValue: Optional[DatasetContentVersionValueTypeDef] = None
    outputFileUriValue: Optional[OutputFileUriValueTypeDef] = None

class PipelineActivityTypeDef(BaseModel):
    channel: Optional[ChannelActivityTypeDef] = None
    lambda: Optional[LambdaActivityTypeDef] = None
    datastore: Optional[DatastoreActivityTypeDef] = None
    addAttributes: Optional[AddAttributesActivityTypeDef] = None
    removeAttributes: Optional[RemoveAttributesActivityTypeDef] = None
    selectAttributes: Optional[SelectAttributesActivityTypeDef] = None
    filter: Optional[FilterActivityTypeDef] = None
    math: Optional[MathActivityTypeDef] = None
    deviceRegistryEnrich: Optional[DeviceRegistryEnrichActivityTypeDef] = None
    deviceShadowEnrich: Optional[DeviceShadowEnrichActivityTypeDef] = None

class PipelineSummaryTypeDef(BaseModel):
    pipelineName: Optional[str] = None
    reprocessingSummaries: Optional[List[ReprocessingSummaryTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class BatchPutMessageRequestRequestTypeDef(BaseModel):
    channelName: str
    messages: Sequence[MessageTypeDef]

class ChannelSummaryTypeDef(BaseModel):
    channelName: Optional[str] = None
    channelStorage: Optional[ChannelStorageSummaryTypeDef] = None
    status: Optional[ChannelStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None

class ChannelTypeDef(BaseModel):
    name: Optional[str] = None
    storage: Optional[ChannelStorageTypeDef] = None
    arn: Optional[str] = None
    status: Optional[ChannelStatusType] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None

class CreateChannelRequestRequestTypeDef(BaseModel):
    channelName: str
    channelStorage: Optional[ChannelStorageTypeDef] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateChannelRequestRequestTypeDef(BaseModel):
    channelName: str
    channelStorage: Optional[ChannelStorageTypeDef] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None

class ParquetConfigurationTypeDef(BaseModel):
    schemaDefinition: Optional[SchemaDefinitionTypeDef] = None

class ListDatasetContentsResponseTypeDef(BaseModel):
    datasetContentSummaries: List[DatasetContentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetSummaryTypeDef(BaseModel):
    datasetName: Optional[str] = None
    status: Optional[DatasetStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    triggers: Optional[List[DatasetTriggerTypeDef]] = None
    actions: Optional[List[DatasetActionSummaryTypeDef]] = None

class DatastoreStorageSummaryTypeDef(BaseModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedDatastoreS3StorageSummaryTypeDef] = None
    iotSiteWiseMultiLayerStorage: Optional[       DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef     ] = None

class DatastoreStorageTypeDef(BaseModel):
    serviceManagedS3: Optional[Mapping[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedDatastoreS3StorageTypeDef] = None
    iotSiteWiseMultiLayerStorage: Optional[DatastoreIotSiteWiseMultiLayerStorageTypeDef] = None

class DatastorePartitionsPaginatorTypeDef(BaseModel):
    partitions: Optional[List[DatastorePartitionTypeDef]] = None

class DatastorePartitionsTypeDef(BaseModel):
    partitions: Optional[Sequence[DatastorePartitionTypeDef]] = None

class LateDataRuleTypeDef(BaseModel):
    ruleConfiguration: LateDataRuleConfigurationTypeDef
    ruleName: Optional[str] = None

class SqlQueryDatasetActionTypeDef(BaseModel):
    sqlQuery: str
    filters: Optional[Sequence[QueryFilterTypeDef]] = None

class DatasetContentDeliveryDestinationTypeDef(BaseModel):
    iotEventsDestinationConfiguration: Optional[IotEventsDestinationConfigurationTypeDef] = None
    s3DestinationConfiguration: Optional[S3DestinationConfigurationTypeDef] = None

class ContainerDatasetActionTypeDef(BaseModel):
    image: str
    executionRoleArn: str
    resourceConfiguration: ResourceConfigurationTypeDef
    variables: Optional[Sequence[VariableTypeDef]] = None

class CreatePipelineRequestRequestTypeDef(BaseModel):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityTypeDef]
    tags: Optional[Sequence[TagTypeDef]] = None

class PipelineTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    activities: Optional[List[PipelineActivityTypeDef]] = None
    reprocessingSummaries: Optional[List[ReprocessingSummaryTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class RunPipelineActivityRequestRequestTypeDef(BaseModel):
    pipelineActivity: PipelineActivityTypeDef
    payloads: Sequence[BlobTypeDef]

class UpdatePipelineRequestRequestTypeDef(BaseModel):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityTypeDef]

class ListPipelinesResponseTypeDef(BaseModel):
    pipelineSummaries: List[PipelineSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsResponseTypeDef(BaseModel):
    channelSummaries: List[ChannelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseModel):
    channel: ChannelTypeDef
    statistics: ChannelStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FileFormatConfigurationTypeDef(BaseModel):
    jsonConfiguration: Optional[Mapping[str, Any]] = None
    parquetConfiguration: Optional[ParquetConfigurationTypeDef] = None

class ListDatasetsResponseTypeDef(BaseModel):
    datasetSummaries: List[DatasetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatastoreSummaryPaginatorTypeDef(BaseModel):
    datastoreName: Optional[str] = None
    datastoreStorage: Optional[DatastoreStorageSummaryTypeDef] = None
    status: Optional[DatastoreStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None
    fileFormatType: Optional[FileFormatTypeType] = None
    datastorePartitions: Optional[DatastorePartitionsPaginatorTypeDef] = None

class DatastoreSummaryTypeDef(BaseModel):
    datastoreName: Optional[str] = None
    datastoreStorage: Optional[DatastoreStorageSummaryTypeDef] = None
    status: Optional[DatastoreStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None
    fileFormatType: Optional[FileFormatTypeType] = None
    datastorePartitions: Optional[DatastorePartitionsTypeDef] = None

class DatasetContentDeliveryRuleTypeDef(BaseModel):
    destination: DatasetContentDeliveryDestinationTypeDef
    entryName: Optional[str] = None

class DatasetActionTypeDef(BaseModel):
    actionName: Optional[str] = None
    queryAction: Optional[SqlQueryDatasetActionTypeDef] = None
    containerAction: Optional[ContainerDatasetActionTypeDef] = None

class DescribePipelineResponseTypeDef(BaseModel):
    pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatastoreRequestRequestTypeDef(BaseModel):
    datastoreName: str
    datastoreStorage: Optional[DatastoreStorageTypeDef] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationTypeDef] = None
    datastorePartitions: Optional[DatastorePartitionsTypeDef] = None

class DatastoreTypeDef(BaseModel):
    name: Optional[str] = None
    storage: Optional[DatastoreStorageTypeDef] = None
    arn: Optional[str] = None
    status: Optional[DatastoreStatusType] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationTypeDef] = None
    datastorePartitions: Optional[DatastorePartitionsTypeDef] = None

class UpdateDatastoreRequestRequestTypeDef(BaseModel):
    datastoreName: str
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    datastoreStorage: Optional[DatastoreStorageTypeDef] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationTypeDef] = None

class ListDatastoresResponsePaginatorTypeDef(BaseModel):
    datastoreSummaries: List[DatastoreSummaryPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatastoresResponseTypeDef(BaseModel):
    datastoreSummaries: List[DatastoreSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetRequestRequestTypeDef(BaseModel):
    datasetName: str
    actions: Sequence[DatasetActionTypeDef]
    triggers: Optional[Sequence[DatasetTriggerTypeDef]] = None
    contentDeliveryRules: Optional[Sequence[DatasetContentDeliveryRuleTypeDef]] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    versioningConfiguration: Optional[VersioningConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    lateDataRules: Optional[Sequence[LateDataRuleTypeDef]] = None

class DatasetTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    actions: Optional[List[DatasetActionTypeDef]] = None
    triggers: Optional[List[DatasetTriggerTypeDef]] = None
    contentDeliveryRules: Optional[List[DatasetContentDeliveryRuleTypeDef]] = None
    status: Optional[DatasetStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    versioningConfiguration: Optional[VersioningConfigurationTypeDef] = None
    lateDataRules: Optional[List[LateDataRuleTypeDef]] = None

class UpdateDatasetRequestRequestTypeDef(BaseModel):
    datasetName: str
    actions: Sequence[DatasetActionTypeDef]
    triggers: Optional[Sequence[DatasetTriggerTypeDef]] = None
    contentDeliveryRules: Optional[Sequence[DatasetContentDeliveryRuleTypeDef]] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    versioningConfiguration: Optional[VersioningConfigurationTypeDef] = None
    lateDataRules: Optional[Sequence[LateDataRuleTypeDef]] = None

class DescribeDatastoreResponseTypeDef(BaseModel):
    datastore: DatastoreTypeDef
    statistics: DatastoreStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetResponseTypeDef(BaseModel):
    dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


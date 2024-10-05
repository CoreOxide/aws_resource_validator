from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AddAttributesActivityTypeDef(BaseValidatorModel):
    name: str
    attributes: Mapping[str, str]
    next: Optional[str] = None

class BatchPutMessageErrorEntryTypeDef(BaseValidatorModel):
    messageId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CancelPipelineReprocessingRequestRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    reprocessingId: str

class ChannelActivityTypeDef(BaseValidatorModel):
    name: str
    channelName: str
    next: Optional[str] = None

class ChannelMessagesTypeDef(BaseValidatorModel):
    s3Paths: Optional[Sequence[str]] = None

class EstimatedResourceSizeTypeDef(BaseValidatorModel):
    estimatedSizeInBytes: Optional[float] = None
    estimatedOn: Optional[datetime] = None

class CustomerManagedChannelS3StorageSummaryTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None
    roleArn: Optional[str] = None

class CustomerManagedChannelS3StorageTypeDef(BaseValidatorModel):
    bucket: str
    roleArn: str
    keyPrefix: Optional[str] = None

class RetentionPeriodTypeDef(BaseValidatorModel):
    unlimited: Optional[bool] = None
    numberOfDays: Optional[int] = None

class ColumnTypeDef(BaseValidatorModel):
    name: str
    type: str

class ResourceConfigurationTypeDef(BaseValidatorModel):
    computeType: ComputeTypeType
    volumeSizeInGB: int

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class CreateDatasetContentRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteChannelRequestRequestTypeDef(BaseValidatorModel):
    channelName: str

class DeleteDatasetContentRequestRequestTypeDef(BaseValidatorModel):
    datasetName: str
    versionId: Optional[str] = None

class DeleteDatasetRequestRequestTypeDef(BaseValidatorModel):
    datasetName: str

class DeleteDatastoreRequestRequestTypeDef(BaseValidatorModel):
    datastoreName: str

class DeletePipelineRequestRequestTypeDef(BaseValidatorModel):
    pipelineName: str

class DeltaTimeSessionWindowConfigurationTypeDef(BaseValidatorModel):
    timeoutInMinutes: int

class DeltaTimeTypeDef(BaseValidatorModel):
    offsetSeconds: int
    timeExpression: str

class DescribeChannelRequestRequestTypeDef(BaseValidatorModel):
    channelName: str
    includeStatistics: Optional[bool] = None

class DescribeDatasetRequestRequestTypeDef(BaseValidatorModel):
    datasetName: str

class DescribeDatastoreRequestRequestTypeDef(BaseValidatorModel):
    datastoreName: str
    includeStatistics: Optional[bool] = None

class LoggingOptionsTypeDef(BaseValidatorModel):
    roleArn: str
    level: Literal["ERROR"]
    enabled: bool

class DescribePipelineRequestRequestTypeDef(BaseValidatorModel):
    pipelineName: str

class DeviceRegistryEnrichActivityTypeDef(BaseValidatorModel):
    name: str
    attribute: str
    thingName: str
    roleArn: str
    next: Optional[str] = None

class DeviceShadowEnrichActivityTypeDef(BaseValidatorModel):
    name: str
    attribute: str
    thingName: str
    roleArn: str
    next: Optional[str] = None

class FilterActivityTypeDef(BaseValidatorModel):
    name: str
    filter: str
    next: Optional[str] = None

class GetDatasetContentRequestRequestTypeDef(BaseValidatorModel):
    datasetName: str
    versionId: Optional[str] = None

class GlueConfigurationTypeDef(BaseValidatorModel):
    tableName: str
    databaseName: str

class LambdaActivityTypeDef(BaseValidatorModel):
    name: str
    lambdaName: str
    batchSize: int
    next: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatasetsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatastoresRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPipelinesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class MathActivityTypeDef(BaseValidatorModel):
    name: str
    attribute: str
    math: str
    next: Optional[str] = None

class OutputFileUriValueTypeDef(BaseValidatorModel):
    fileName: str

class RemoveAttributesActivityTypeDef(BaseValidatorModel):
    name: str
    attributes: Sequence[str]
    next: Optional[str] = None

class SelectAttributesActivityTypeDef(BaseValidatorModel):
    name: str
    attributes: Sequence[str]
    next: Optional[str] = None

class ReprocessingSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    status: Optional[ReprocessingStatusType] = None
    creationTime: Optional[datetime] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
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

class MessageTypeDef(BaseValidatorModel):
    messageId: str
    payload: BlobTypeDef

class ChannelStatisticsTypeDef(BaseValidatorModel):
    size: Optional[EstimatedResourceSizeTypeDef] = None

class DatastoreStatisticsTypeDef(BaseValidatorModel):
    size: Optional[EstimatedResourceSizeTypeDef] = None

class ChannelStorageSummaryTypeDef(BaseValidatorModel):
    serviceManagedS3: Optional[Dict[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3StorageSummaryTypeDef] = None

class ChannelStorageTypeDef(BaseValidatorModel):
    serviceManagedS3: Optional[Mapping[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedChannelS3StorageTypeDef] = None

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

class SchemaDefinitionTypeDef(BaseValidatorModel):
    columns: Optional[Sequence[ColumnTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    customerManagedS3Storage: Optional[       IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef     ] = None

class DatastoreIotSiteWiseMultiLayerStorageTypeDef(BaseValidatorModel):
    customerManagedS3Storage: IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef

class DatastorePartitionTypeDef(BaseValidatorModel):
    attributePartition: Optional[PartitionTypeDef] = None
    timestampPartition: Optional[TimestampPartitionTypeDef] = None

class LateDataRuleConfigurationTypeDef(BaseValidatorModel):
    deltaTimeSessionWindowConfiguration: Optional[       DeltaTimeSessionWindowConfigurationTypeDef     ] = None

class QueryFilterTypeDef(BaseValidatorModel):
    deltaTime: Optional[DeltaTimeTypeDef] = None

class DescribeLoggingOptionsResponseTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestRequestTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef

class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    bucket: str
    key: str
    roleArn: str
    glueConfiguration: Optional[GlueConfigurationTypeDef] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetsRequestListDatasetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatastoresRequestListDatastoresPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesRequestListPipelinesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetContentsRequestListDatasetContentsPaginateTypeDef(BaseValidatorModel):
    datasetName: str
    scheduledOnOrAfter: Optional[TimestampTypeDef] = None
    scheduledBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetContentsRequestRequestTypeDef(BaseValidatorModel):
    datasetName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    scheduledOnOrAfter: Optional[TimestampTypeDef] = None
    scheduledBefore: Optional[TimestampTypeDef] = None

class SampleChannelDataRequestRequestTypeDef(BaseValidatorModel):
    channelName: str
    maxMessages: Optional[int] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None

class StartPipelineReprocessingRequestRequestTypeDef(BaseValidatorModel):
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

class PipelineActivityTypeDef(BaseValidatorModel):
    channel: Optional[ChannelActivityTypeDef] = None
    _lambda: Optional[LambdaActivityTypeDef] = None
    datastore: Optional[DatastoreActivityTypeDef] = None
    addAttributes: Optional[AddAttributesActivityTypeDef] = None
    removeAttributes: Optional[RemoveAttributesActivityTypeDef] = None
    selectAttributes: Optional[SelectAttributesActivityTypeDef] = None
    filter: Optional[FilterActivityTypeDef] = None
    math: Optional[MathActivityTypeDef] = None
    deviceRegistryEnrich: Optional[DeviceRegistryEnrichActivityTypeDef] = None
    deviceShadowEnrich: Optional[DeviceShadowEnrichActivityTypeDef] = None

class PipelineSummaryTypeDef(BaseValidatorModel):
    pipelineName: Optional[str] = None
    reprocessingSummaries: Optional[List[ReprocessingSummaryTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class BatchPutMessageRequestRequestTypeDef(BaseValidatorModel):
    channelName: str
    messages: Sequence[MessageTypeDef]

class ChannelSummaryTypeDef(BaseValidatorModel):
    channelName: Optional[str] = None
    channelStorage: Optional[ChannelStorageSummaryTypeDef] = None
    status: Optional[ChannelStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None

class ChannelTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    storage: Optional[ChannelStorageTypeDef] = None
    arn: Optional[str] = None
    status: Optional[ChannelStatusType] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None

class CreateChannelRequestRequestTypeDef(BaseValidatorModel):
    channelName: str
    channelStorage: Optional[ChannelStorageTypeDef] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateChannelRequestRequestTypeDef(BaseValidatorModel):
    channelName: str
    channelStorage: Optional[ChannelStorageTypeDef] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None

class ParquetConfigurationTypeDef(BaseValidatorModel):
    schemaDefinition: Optional[SchemaDefinitionTypeDef] = None

class ListDatasetContentsResponseTypeDef(BaseValidatorModel):
    datasetContentSummaries: List[DatasetContentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    iotSiteWiseMultiLayerStorage: Optional[       DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef     ] = None

class DatastoreStorageTypeDef(BaseValidatorModel):
    serviceManagedS3: Optional[Mapping[str, Any]] = None
    customerManagedS3: Optional[CustomerManagedDatastoreS3StorageTypeDef] = None
    iotSiteWiseMultiLayerStorage: Optional[DatastoreIotSiteWiseMultiLayerStorageTypeDef] = None

class DatastorePartitionsPaginatorTypeDef(BaseValidatorModel):
    partitions: Optional[List[DatastorePartitionTypeDef]] = None

class DatastorePartitionsTypeDef(BaseValidatorModel):
    partitions: Optional[Sequence[DatastorePartitionTypeDef]] = None

class LateDataRuleTypeDef(BaseValidatorModel):
    ruleConfiguration: LateDataRuleConfigurationTypeDef
    ruleName: Optional[str] = None

class SqlQueryDatasetActionTypeDef(BaseValidatorModel):
    sqlQuery: str
    filters: Optional[Sequence[QueryFilterTypeDef]] = None

class DatasetContentDeliveryDestinationTypeDef(BaseValidatorModel):
    iotEventsDestinationConfiguration: Optional[IotEventsDestinationConfigurationTypeDef] = None
    s3DestinationConfiguration: Optional[S3DestinationConfigurationTypeDef] = None

class ContainerDatasetActionTypeDef(BaseValidatorModel):
    image: str
    executionRoleArn: str
    resourceConfiguration: ResourceConfigurationTypeDef
    variables: Optional[Sequence[VariableTypeDef]] = None

class CreatePipelineRequestRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityTypeDef]
    tags: Optional[Sequence[TagTypeDef]] = None

class PipelineTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    activities: Optional[List[PipelineActivityTypeDef]] = None
    reprocessingSummaries: Optional[List[ReprocessingSummaryTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class RunPipelineActivityRequestRequestTypeDef(BaseValidatorModel):
    pipelineActivity: PipelineActivityTypeDef
    payloads: Sequence[BlobTypeDef]

class UpdatePipelineRequestRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityTypeDef]

class ListPipelinesResponseTypeDef(BaseValidatorModel):
    pipelineSummaries: List[PipelineSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsResponseTypeDef(BaseValidatorModel):
    channelSummaries: List[ChannelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseValidatorModel):
    channel: ChannelTypeDef
    statistics: ChannelStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FileFormatConfigurationTypeDef(BaseValidatorModel):
    jsonConfiguration: Optional[Mapping[str, Any]] = None
    parquetConfiguration: Optional[ParquetConfigurationTypeDef] = None

class ListDatasetsResponseTypeDef(BaseValidatorModel):
    datasetSummaries: List[DatasetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatastoreSummaryPaginatorTypeDef(BaseValidatorModel):
    datastoreName: Optional[str] = None
    datastoreStorage: Optional[DatastoreStorageSummaryTypeDef] = None
    status: Optional[DatastoreStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None
    fileFormatType: Optional[FileFormatTypeType] = None
    datastorePartitions: Optional[DatastorePartitionsPaginatorTypeDef] = None

class DatastoreSummaryTypeDef(BaseValidatorModel):
    datastoreName: Optional[str] = None
    datastoreStorage: Optional[DatastoreStorageSummaryTypeDef] = None
    status: Optional[DatastoreStatusType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    lastMessageArrivalTime: Optional[datetime] = None
    fileFormatType: Optional[FileFormatTypeType] = None
    datastorePartitions: Optional[DatastorePartitionsTypeDef] = None

class DatasetContentDeliveryRuleTypeDef(BaseValidatorModel):
    destination: DatasetContentDeliveryDestinationTypeDef
    entryName: Optional[str] = None

class DatasetActionTypeDef(BaseValidatorModel):
    actionName: Optional[str] = None
    queryAction: Optional[SqlQueryDatasetActionTypeDef] = None
    containerAction: Optional[ContainerDatasetActionTypeDef] = None

class DescribePipelineResponseTypeDef(BaseValidatorModel):
    pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatastoreRequestRequestTypeDef(BaseValidatorModel):
    datastoreName: str
    datastoreStorage: Optional[DatastoreStorageTypeDef] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationTypeDef] = None
    datastorePartitions: Optional[DatastorePartitionsTypeDef] = None

class DatastoreTypeDef(BaseValidatorModel):
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

class UpdateDatastoreRequestRequestTypeDef(BaseValidatorModel):
    datastoreName: str
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    datastoreStorage: Optional[DatastoreStorageTypeDef] = None
    fileFormatConfiguration: Optional[FileFormatConfigurationTypeDef] = None

class ListDatastoresResponsePaginatorTypeDef(BaseValidatorModel):
    datastoreSummaries: List[DatastoreSummaryPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatastoresResponseTypeDef(BaseValidatorModel):
    datastoreSummaries: List[DatastoreSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetRequestRequestTypeDef(BaseValidatorModel):
    datasetName: str
    actions: Sequence[DatasetActionTypeDef]
    triggers: Optional[Sequence[DatasetTriggerTypeDef]] = None
    contentDeliveryRules: Optional[Sequence[DatasetContentDeliveryRuleTypeDef]] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    versioningConfiguration: Optional[VersioningConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    lateDataRules: Optional[Sequence[LateDataRuleTypeDef]] = None

class DatasetTypeDef(BaseValidatorModel):
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

class UpdateDatasetRequestRequestTypeDef(BaseValidatorModel):
    datasetName: str
    actions: Sequence[DatasetActionTypeDef]
    triggers: Optional[Sequence[DatasetTriggerTypeDef]] = None
    contentDeliveryRules: Optional[Sequence[DatasetContentDeliveryRuleTypeDef]] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    versioningConfiguration: Optional[VersioningConfigurationTypeDef] = None
    lateDataRules: Optional[Sequence[LateDataRuleTypeDef]] = None

class DescribeDatastoreResponseTypeDef(BaseValidatorModel):
    datastore: DatastoreTypeDef
    statistics: DatastoreStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


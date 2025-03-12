from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.eventstream import EventStream
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
from aws_resource_validator.pydantic_models.iotsitewise_constants import *

class AccessDeniedExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class ActionDefinitionTypeDef(BaseValidatorModel):
    actionDefinitionId: str
    actionName: str
    actionType: str


class ActionPayloadTypeDef(BaseValidatorModel):
    stringValue: str


class TargetResourceTypeDef(BaseValidatorModel):
    assetId: str


class AlarmsTypeDef(BaseValidatorModel):
    alarmRoleArn: str
    notificationLambdaArn: Optional[str] = None


class AssetErrorDetailsTypeDef(BaseValidatorModel):
    assetId: str
    code: Literal["INTERNAL_FAILURE"]
    message: str


class AssetHierarchyInfoTypeDef(BaseValidatorModel):
    parentAssetId: Optional[str] = None
    childAssetId: Optional[str] = None


class PropertyNotificationTypeDef(BaseValidatorModel):
    topic: str
    state: PropertyNotificationStateType


class TimeInNanosTypeDef(BaseValidatorModel):
    timeInSeconds: int
    offsetInNanos: Optional[int] = None


class AssociateAssetsRequestTypeDef(BaseValidatorModel):
    assetId: str
    hierarchyId: str
    childAssetId: str
    clientToken: Optional[str] = None


class AssociateTimeSeriesToAssetPropertyRequestTypeDef(BaseValidatorModel):
    alias: str
    assetId: str
    propertyId: str
    clientToken: Optional[str] = None


class AttributeTypeDef(BaseValidatorModel):
    defaultValue: Optional[str] = None


class BatchAssociateProjectAssetsRequestTypeDef(BaseValidatorModel):
    projectId: str
    assetIds: Sequence[str]
    clientToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDisassociateProjectAssetsRequestTypeDef(BaseValidatorModel):
    projectId: str
    assetIds: Sequence[str]
    clientToken: Optional[str] = None


class BatchGetAssetPropertyAggregatesErrorEntryTypeDef(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyAggregatesErrorCodeType
    errorMessage: str
    entryId: str


class BatchGetAssetPropertyAggregatesErrorInfoTypeDef(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyAggregatesErrorCodeType
    errorTimestamp: datetime


class BatchGetAssetPropertyValueEntryTypeDef(BaseValidatorModel):
    entryId: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


class BatchGetAssetPropertyValueErrorEntryTypeDef(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyValueErrorCodeType
    errorMessage: str
    entryId: str


class BatchGetAssetPropertyValueErrorInfoTypeDef(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyValueErrorCodeType
    errorTimestamp: datetime


class BatchGetAssetPropertyValueHistoryErrorEntryTypeDef(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyValueHistoryErrorCodeType
    errorMessage: str
    entryId: str


class BatchGetAssetPropertyValueHistoryErrorInfoTypeDef(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyValueHistoryErrorCodeType
    errorTimestamp: datetime


class ContentTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class ColumnTypeTypeDef(BaseValidatorModel):
    scalarType: Optional[ScalarTypeType] = None


class CompositionRelationshipSummaryTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelType: str


class ConfigurationErrorDetailsTypeDef(BaseValidatorModel):
    code: ErrorCodeType
    message: str


class ConflictingOperationExceptionTypeDef(BaseValidatorModel):
    message: str
    resourceId: str
    resourceArn: str


class CreateAssetRequestTypeDef(BaseValidatorModel):
    assetName: str
    assetModelId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    assetDescription: Optional[str] = None
    assetId: Optional[str] = None
    assetExternalId: Optional[str] = None


class ErrorReportLocationTypeDef(BaseValidatorModel):
    bucket: str
    prefix: str


class FileTypeDef(BaseValidatorModel):
    bucket: str
    key: str
    versionId: Optional[str] = None


class CreateDashboardRequestTypeDef(BaseValidatorModel):
    projectId: str
    dashboardName: str
    dashboardDefinition: str
    dashboardDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateProjectRequestTypeDef(BaseValidatorModel):
    portalId: str
    projectName: str
    projectDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CsvOutputTypeDef(BaseValidatorModel):
    columnNames: List[ColumnNameType]


class CsvTypeDef(BaseValidatorModel):
    columnNames: Sequence[ColumnNameType]


class CustomerManagedS3StorageTypeDef(BaseValidatorModel):
    s3ResourceArn: str
    roleArn: str


class DatumPaginatorTypeDef(BaseValidatorModel):
    scalarValue: Optional[str] = None
    arrayValue: Optional[List[Dict[str, Any]]] = None
    rowValue: Optional[Dict[str, Any]] = None
    nullValue: Optional[bool] = None


class DatumTypeDef(BaseValidatorModel):
    scalarValue: Optional[str] = None
    arrayValue: Optional[List[Dict[str, Any]]] = None
    rowValue: Optional[Dict[str, Any]] = None
    nullValue: Optional[bool] = None


class DatumWaiterTypeDef(BaseValidatorModel):
    scalarValue: Optional[str] = None
    arrayValue: Optional[List[Dict[str, Any]]] = None
    rowValue: Optional[Dict[str, Any]] = None
    nullValue: Optional[bool] = None


class DeleteAccessPolicyRequestTypeDef(BaseValidatorModel):
    accessPolicyId: str
    clientToken: Optional[str] = None


class DeleteAssetModelCompositeModelRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    clientToken: Optional[str] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None


class DeleteAssetModelRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    clientToken: Optional[str] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None


class DeleteAssetRequestTypeDef(BaseValidatorModel):
    assetId: str
    clientToken: Optional[str] = None


class DeleteDashboardRequestTypeDef(BaseValidatorModel):
    dashboardId: str
    clientToken: Optional[str] = None


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    datasetId: str
    clientToken: Optional[str] = None


class DeleteGatewayRequestTypeDef(BaseValidatorModel):
    gatewayId: str


class DeletePortalRequestTypeDef(BaseValidatorModel):
    portalId: str
    clientToken: Optional[str] = None


class DeleteProjectRequestTypeDef(BaseValidatorModel):
    projectId: str
    clientToken: Optional[str] = None


class DeleteTimeSeriesRequestTypeDef(BaseValidatorModel):
    alias: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    clientToken: Optional[str] = None


class DescribeAccessPolicyRequestTypeDef(BaseValidatorModel):
    accessPolicyId: str


class DescribeActionRequestTypeDef(BaseValidatorModel):
    actionId: str


class DescribeAssetCompositeModelRequestTypeDef(BaseValidatorModel):
    assetId: str
    assetCompositeModelId: str


class DescribeAssetModelCompositeModelRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelVersion: Optional[str] = None


class DescribeAssetModelRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    assetModelVersion: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeAssetPropertyRequestTypeDef(BaseValidatorModel):
    assetId: str
    propertyId: str


class DescribeAssetRequestTypeDef(BaseValidatorModel):
    assetId: str
    excludeProperties: Optional[bool] = None


class DescribeBulkImportJobRequestTypeDef(BaseValidatorModel):
    jobId: str


class DescribeDashboardRequestTypeDef(BaseValidatorModel):
    dashboardId: str


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    datasetId: str


class DescribeGatewayCapabilityConfigurationRequestTypeDef(BaseValidatorModel):
    gatewayId: str
    capabilityNamespace: str


class DescribeGatewayRequestTypeDef(BaseValidatorModel):
    gatewayId: str


class GatewayCapabilitySummaryTypeDef(BaseValidatorModel):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatusType


class LoggingOptionsTypeDef(BaseValidatorModel):
    level: LoggingLevelType


class DescribePortalRequestTypeDef(BaseValidatorModel):
    portalId: str


class PortalTypeEntryOutputTypeDef(BaseValidatorModel):
    portalTools: Optional[List[str]] = None


class DescribeProjectRequestTypeDef(BaseValidatorModel):
    projectId: str


class RetentionPeriodTypeDef(BaseValidatorModel):
    numberOfDays: Optional[int] = None
    unlimited: Optional[bool] = None


class WarmTierRetentionPeriodTypeDef(BaseValidatorModel):
    numberOfDays: Optional[int] = None
    unlimited: Optional[bool] = None


class DescribeTimeSeriesRequestTypeDef(BaseValidatorModel):
    alias: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None


class DetailedErrorTypeDef(BaseValidatorModel):
    code: DetailedErrorCodeType
    message: str


class DisassociateAssetsRequestTypeDef(BaseValidatorModel):
    assetId: str
    hierarchyId: str
    childAssetId: str
    clientToken: Optional[str] = None


class DisassociateTimeSeriesFromAssetPropertyRequestTypeDef(BaseValidatorModel):
    alias: str
    assetId: str
    propertyId: str
    clientToken: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ExecuteQueryRequestTypeDef(BaseValidatorModel):
    queryStatement: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    clientToken: Optional[str] = None


class ForwardingConfigTypeDef(BaseValidatorModel):
    state: ForwardingConfigStateType


class GreengrassTypeDef(BaseValidatorModel):
    groupArn: str


class GreengrassV2TypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    coreDeviceOperatingSystem: Optional[CoreDeviceOperatingSystemType] = None


class SiemensIETypeDef(BaseValidatorModel):
    iotCoreThingName: str


class GetAssetPropertyValueRequestTypeDef(BaseValidatorModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


class IAMRoleIdentityTypeDef(BaseValidatorModel):
    arn: str


class IAMUserIdentityTypeDef(BaseValidatorModel):
    arn: str


class InternalFailureExceptionTypeDef(BaseValidatorModel):
    message: str


class InvalidRequestExceptionTypeDef(BaseValidatorModel):
    message: str


class InvokeAssistantRequestTypeDef(BaseValidatorModel):
    message: str
    conversationId: Optional[str] = None
    enableTrace: Optional[bool] = None


class KendraSourceDetailTypeDef(BaseValidatorModel):
    knowledgeBaseArn: str
    roleArn: str


class LimitExceededExceptionTypeDef(BaseValidatorModel):
    message: str


class ListAccessPoliciesRequestTypeDef(BaseValidatorModel):
    identityType: Optional[IdentityTypeType] = None
    identityId: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    iamArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListActionsRequestTypeDef(BaseValidatorModel):
    targetResourceType: Literal["ASSET"]
    targetResourceId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssetModelCompositeModelsRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetModelVersion: Optional[str] = None


class ListAssetModelsRequestTypeDef(BaseValidatorModel):
    assetModelTypes: Optional[Sequence[AssetModelTypeType]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetModelVersion: Optional[str] = None


class ListAssetRelationshipsRequestTypeDef(BaseValidatorModel):
    assetId: str
    traversalType: Literal["PATH_TO_ROOT"]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssociatedAssetsRequestTypeDef(BaseValidatorModel):
    assetId: str
    hierarchyId: Optional[str] = None
    traversalDirection: Optional[TraversalDirectionType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCompositionRelationshipsRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDashboardsRequestTypeDef(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetsRequestTypeDef(BaseValidatorModel):
    sourceType: Literal["KENDRA"]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListGatewaysRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPortalsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListProjectAssetsRequestTypeDef(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListProjectsRequestTypeDef(BaseValidatorModel):
    portalId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTimeSeriesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetId: Optional[str] = None
    aliasPrefix: Optional[str] = None
    timeSeriesType: Optional[ListTimeSeriesTypeType] = None


class TimeSeriesSummaryTypeDef(BaseValidatorModel):
    timeSeriesId: str
    dataType: PropertyDataTypeType
    timeSeriesCreationDate: datetime
    timeSeriesLastUpdateDate: datetime
    timeSeriesArn: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    alias: Optional[str] = None
    dataTypeSpec: Optional[str] = None


class LocationTypeDef(BaseValidatorModel):
    uri: Optional[str] = None


class MetricProcessingConfigTypeDef(BaseValidatorModel):
    computeLocation: ComputeLocationType


class TumblingWindowTypeDef(BaseValidatorModel):
    interval: str
    offset: Optional[str] = None


class MonitorErrorDetailsTypeDef(BaseValidatorModel):
    code: Optional[MonitorErrorCodeType] = None
    message: Optional[str] = None


class PortalTypeEntryTypeDef(BaseValidatorModel):
    portalTools: Optional[Sequence[str]] = None


class PropertyValueNullValueTypeDef(BaseValidatorModel):
    valueType: RawValueTypeType


class PutDefaultEncryptionConfigurationRequestTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyId: Optional[str] = None


class ResourceNotFoundExceptionTypeDef(BaseValidatorModel):
    message: str


class ThrottlingExceptionTypeDef(BaseValidatorModel):
    message: str


class TraceTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAssetPropertyRequestTypeDef(BaseValidatorModel):
    assetId: str
    propertyId: str
    propertyAlias: Optional[str] = None
    propertyNotificationState: Optional[PropertyNotificationStateType] = None
    clientToken: Optional[str] = None
    propertyUnit: Optional[str] = None


class UpdateAssetRequestTypeDef(BaseValidatorModel):
    assetId: str
    assetName: str
    clientToken: Optional[str] = None
    assetDescription: Optional[str] = None
    assetExternalId: Optional[str] = None


class UpdateDashboardRequestTypeDef(BaseValidatorModel):
    dashboardId: str
    dashboardName: str
    dashboardDefinition: str
    dashboardDescription: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateGatewayCapabilityConfigurationRequestTypeDef(BaseValidatorModel):
    gatewayId: str
    capabilityNamespace: str
    capabilityConfiguration: str


class UpdateGatewayRequestTypeDef(BaseValidatorModel):
    gatewayId: str
    gatewayName: str


class UpdateProjectRequestTypeDef(BaseValidatorModel):
    projectId: str
    projectName: str
    projectDescription: Optional[str] = None
    clientToken: Optional[str] = None


class ActionSummaryTypeDef(BaseValidatorModel):
    actionId: Optional[str] = None
    actionDefinitionId: Optional[str] = None
    targetResource: Optional[TargetResourceTypeDef] = None


class ExecuteActionRequestTypeDef(BaseValidatorModel):
    targetResource: TargetResourceTypeDef
    actionDefinitionId: str
    actionPayload: ActionPayloadTypeDef
    clientToken: Optional[str] = None


class AggregatesTypeDef(BaseValidatorModel):
    pass


class AggregatedValueTypeDef(BaseValidatorModel):
    timestamp: datetime
    value: AggregatesTypeDef
    quality: Optional[QualityType] = None


class AssetRelationshipSummaryTypeDef(BaseValidatorModel):
    relationshipType: Literal["HIERARCHY"]
    hierarchyInfo: Optional[AssetHierarchyInfoTypeDef] = None


class AssetModelPropertyPathSegmentTypeDef(BaseValidatorModel):
    pass


class VariableValueOutputTypeDef(BaseValidatorModel):
    propertyId: Optional[str] = None
    hierarchyId: Optional[str] = None
    propertyPath: Optional[List[AssetModelPropertyPathSegmentTypeDef]] = None


class VariableValueTypeDef(BaseValidatorModel):
    propertyId: Optional[str] = None
    hierarchyId: Optional[str] = None
    propertyPath: Optional[Sequence[AssetModelPropertyPathSegmentTypeDef]] = None


class BatchPutAssetPropertyErrorTypeDef(BaseValidatorModel):
    errorCode: BatchPutAssetPropertyValueErrorCodeType
    errorMessage: str
    timestamps: List[TimeInNanosTypeDef]


class BatchAssociateProjectAssetsResponseTypeDef(BaseValidatorModel):
    errors: List[AssetErrorDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDisassociateProjectAssetsResponseTypeDef(BaseValidatorModel):
    errors: List[AssetErrorDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAccessPolicyResponseTypeDef(BaseValidatorModel):
    accessPolicyId: str
    accessPolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBulkImportJobResponseTypeDef(BaseValidatorModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDashboardResponseTypeDef(BaseValidatorModel):
    dashboardId: str
    dashboardArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGatewayResponseTypeDef(BaseValidatorModel):
    gatewayId: str
    gatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProjectResponseTypeDef(BaseValidatorModel):
    projectId: str
    projectArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeActionResponseTypeDef(BaseValidatorModel):
    actionId: str
    targetResource: TargetResourceTypeDef
    actionDefinitionId: str
    actionPayload: ActionPayloadTypeDef
    executionTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDashboardResponseTypeDef(BaseValidatorModel):
    dashboardId: str
    dashboardArn: str
    dashboardName: str
    projectId: str
    dashboardDescription: str
    dashboardDefinition: str
    dashboardCreationDate: datetime
    dashboardLastUpdateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeGatewayCapabilityConfigurationResponseTypeDef(BaseValidatorModel):
    gatewayId: str
    capabilityNamespace: str
    capabilityConfiguration: str
    capabilitySyncStatus: CapabilitySyncStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeProjectResponseTypeDef(BaseValidatorModel):
    projectId: str
    projectArn: str
    projectName: str
    portalId: str
    projectDescription: str
    projectCreationDate: datetime
    projectLastUpdateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTimeSeriesResponseTypeDef(BaseValidatorModel):
    assetId: str
    propertyId: str
    alias: str
    timeSeriesId: str
    dataType: PropertyDataTypeType
    dataTypeSpec: str
    timeSeriesCreationDate: datetime
    timeSeriesLastUpdateDate: datetime
    timeSeriesArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ExecuteActionResponseTypeDef(BaseValidatorModel):
    actionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListProjectAssetsResponseTypeDef(BaseValidatorModel):
    assetIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGatewayCapabilityConfigurationResponseTypeDef(BaseValidatorModel):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class BatchGetAssetPropertyAggregatesEntryTypeDef(BaseValidatorModel):
    entryId: str
    aggregateTypes: Sequence[AggregateTypeType]
    resolution: str
    startDate: TimestampTypeDef
    endDate: TimestampTypeDef
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None


class BatchGetAssetPropertyValueHistoryEntryTypeDef(BaseValidatorModel):
    entryId: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None


class GetAssetPropertyAggregatesRequestTypeDef(BaseValidatorModel):
    aggregateTypes: Sequence[AggregateTypeType]
    resolution: str
    startDate: TimestampTypeDef
    endDate: TimestampTypeDef
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetAssetPropertyValueHistoryRequestTypeDef(BaseValidatorModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class BatchGetAssetPropertyAggregatesSkippedEntryTypeDef(BaseValidatorModel):
    entryId: str
    completionStatus: BatchEntryCompletionStatusType
    errorInfo: Optional[BatchGetAssetPropertyAggregatesErrorInfoTypeDef] = None


class BatchGetAssetPropertyValueRequestTypeDef(BaseValidatorModel):
    entries: Sequence[BatchGetAssetPropertyValueEntryTypeDef]
    nextToken: Optional[str] = None


class BatchGetAssetPropertyValueSkippedEntryTypeDef(BaseValidatorModel):
    entryId: str
    completionStatus: BatchEntryCompletionStatusType
    errorInfo: Optional[BatchGetAssetPropertyValueErrorInfoTypeDef] = None


class BatchGetAssetPropertyValueHistorySkippedEntryTypeDef(BaseValidatorModel):
    entryId: str
    completionStatus: BatchEntryCompletionStatusType
    errorInfo: Optional[BatchGetAssetPropertyValueHistoryErrorInfoTypeDef] = None


class CompositionRelationshipItemTypeDef(BaseValidatorModel):
    pass


class CompositionDetailsTypeDef(BaseValidatorModel):
    compositionRelationship: Optional[List[CompositionRelationshipItemTypeDef]] = None


class ListCompositionRelationshipsResponseTypeDef(BaseValidatorModel):
    compositionRelationshipSummaries: List[CompositionRelationshipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConfigurationStatusTypeDef(BaseValidatorModel):
    state: ConfigurationStateType
    error: Optional[ConfigurationErrorDetailsTypeDef] = None


class FileFormatOutputTypeDef(BaseValidatorModel):
    csv: Optional[CsvOutputTypeDef] = None
    parquet: Optional[Dict[str, Any]] = None


class FileFormatTypeDef(BaseValidatorModel):
    csv: Optional[CsvTypeDef] = None
    parquet: Optional[Mapping[str, Any]] = None


class MultiLayerStorageTypeDef(BaseValidatorModel):
    customerManagedS3Storage: CustomerManagedS3StorageTypeDef


class DashboardSummaryTypeDef(BaseValidatorModel):
    pass


class ListDashboardsResponseTypeDef(BaseValidatorModel):
    dashboardSummaries: List[DashboardSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RowPaginatorTypeDef(BaseValidatorModel):
    data: List[DatumPaginatorTypeDef]


class RowTypeDef(BaseValidatorModel):
    data: List[DatumTypeDef]


class RowWaiterTypeDef(BaseValidatorModel):
    data: List[DatumWaiterTypeDef]


class DescribeAssetModelRequestWaitExtraTypeDef(BaseValidatorModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    assetModelVersion: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeAssetModelRequestWaitTypeDef(BaseValidatorModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    assetModelVersion: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeAssetRequestWaitExtraTypeDef(BaseValidatorModel):
    assetId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeAssetRequestWaitTypeDef(BaseValidatorModel):
    assetId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribePortalRequestWaitExtraTypeDef(BaseValidatorModel):
    portalId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribePortalRequestWaitTypeDef(BaseValidatorModel):
    portalId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeLoggingOptionsResponseTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutLoggingOptionsRequestTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef


class ErrorDetailsTypeDef(BaseValidatorModel):
    code: ErrorCodeType
    message: str
    details: Optional[List[DetailedErrorTypeDef]] = None


class ExecuteQueryRequestPaginateTypeDef(BaseValidatorModel):
    queryStatement: str
    clientToken: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetAssetPropertyAggregatesRequestPaginateTypeDef(BaseValidatorModel):
    aggregateTypes: Sequence[AggregateTypeType]
    resolution: str
    startDate: TimestampTypeDef
    endDate: TimestampTypeDef
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetAssetPropertyValueHistoryRequestPaginateTypeDef(BaseValidatorModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccessPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    identityType: Optional[IdentityTypeType] = None
    identityId: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    iamArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListActionsRequestPaginateTypeDef(BaseValidatorModel):
    targetResourceType: Literal["ASSET"]
    targetResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssetModelCompositeModelsRequestPaginateTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssetModelsRequestPaginateTypeDef(BaseValidatorModel):
    assetModelTypes: Optional[Sequence[AssetModelTypeType]] = None
    assetModelVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssetRelationshipsRequestPaginateTypeDef(BaseValidatorModel):
    assetId: str
    traversalType: Literal["PATH_TO_ROOT"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssociatedAssetsRequestPaginateTypeDef(BaseValidatorModel):
    assetId: str
    hierarchyId: Optional[str] = None
    traversalDirection: Optional[TraversalDirectionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCompositionRelationshipsRequestPaginateTypeDef(BaseValidatorModel):
    assetModelId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDashboardsRequestPaginateTypeDef(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetsRequestPaginateTypeDef(BaseValidatorModel):
    sourceType: Literal["KENDRA"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGatewaysRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPortalsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectAssetsRequestPaginateTypeDef(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsRequestPaginateTypeDef(BaseValidatorModel):
    portalId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTimeSeriesRequestPaginateTypeDef(BaseValidatorModel):
    assetId: Optional[str] = None
    aliasPrefix: Optional[str] = None
    timeSeriesType: Optional[ListTimeSeriesTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class MeasurementProcessingConfigTypeDef(BaseValidatorModel):
    forwardingConfig: ForwardingConfigTypeDef


class TransformProcessingConfigTypeDef(BaseValidatorModel):
    computeLocation: ComputeLocationType
    forwardingConfig: Optional[ForwardingConfigTypeDef] = None


class GatewayPlatformTypeDef(BaseValidatorModel):
    greengrass: Optional[GreengrassTypeDef] = None
    greengrassV2: Optional[GreengrassV2TypeDef] = None
    siemensIE: Optional[SiemensIETypeDef] = None


class GroupIdentityTypeDef(BaseValidatorModel):
    pass


class UserIdentityTypeDef(BaseValidatorModel):
    pass


class IdentityTypeDef(BaseValidatorModel):
    user: Optional[UserIdentityTypeDef] = None
    group: Optional[GroupIdentityTypeDef] = None
    iamUser: Optional[IAMUserIdentityTypeDef] = None
    iamRole: Optional[IAMRoleIdentityTypeDef] = None


class JobSummaryTypeDef(BaseValidatorModel):
    pass


class ListBulkImportJobsResponseTypeDef(BaseValidatorModel):
    jobSummaries: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SourceDetailTypeDef(BaseValidatorModel):
    kendra: Optional[KendraSourceDetailTypeDef] = None


class ProjectSummaryTypeDef(BaseValidatorModel):
    pass


class ListProjectsResponseTypeDef(BaseValidatorModel):
    projectSummaries: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTimeSeriesResponseTypeDef(BaseValidatorModel):
    TimeSeriesSummaries: List[TimeSeriesSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SourceTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    location: Optional[LocationTypeDef] = None


class MetricWindowTypeDef(BaseValidatorModel):
    tumbling: Optional[TumblingWindowTypeDef] = None


class PortalStatusTypeDef(BaseValidatorModel):
    state: PortalStateType
    error: Optional[MonitorErrorDetailsTypeDef] = None


class ProjectResourceTypeDef(BaseValidatorModel):
    pass


class PortalResourceTypeDef(BaseValidatorModel):
    pass


class ResourceTypeDef(BaseValidatorModel):
    portal: Optional[PortalResourceTypeDef] = None
    project: Optional[ProjectResourceTypeDef] = None


class VariantTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    integerValue: Optional[int] = None
    doubleValue: Optional[float] = None
    booleanValue: Optional[bool] = None
    nullValue: Optional[PropertyValueNullValueTypeDef] = None


class ListActionsResponseTypeDef(BaseValidatorModel):
    actionSummaries: List[ActionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetAssetPropertyAggregatesSuccessEntryTypeDef(BaseValidatorModel):
    entryId: str
    aggregatedValues: List[AggregatedValueTypeDef]


class GetAssetPropertyAggregatesResponseTypeDef(BaseValidatorModel):
    aggregatedValues: List[AggregatedValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAssetRelationshipsResponseTypeDef(BaseValidatorModel):
    assetRelationshipSummaries: List[AssetRelationshipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssetModelCompositeModelSummaryTypeDef(BaseValidatorModel):
    pass


class ListAssetModelCompositeModelsResponseTypeDef(BaseValidatorModel):
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ExpressionVariableOutputTypeDef(BaseValidatorModel):
    name: str
    value: VariableValueOutputTypeDef


class AssetPropertySummaryTypeDef(BaseValidatorModel):
    pass


class ListAssetPropertiesResponseTypeDef(BaseValidatorModel):
    assetPropertySummaries: List[AssetPropertySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssetPropertyTypeDef(BaseValidatorModel):
    pass


class AssetCompositeModelSummaryTypeDef(BaseValidatorModel):
    pass


class AssetCompositeModelPathSegmentTypeDef(BaseValidatorModel):
    pass


class DescribeAssetCompositeModelResponseTypeDef(BaseValidatorModel):
    assetId: str
    assetCompositeModelId: str
    assetCompositeModelExternalId: str
    assetCompositeModelPath: List[AssetCompositeModelPathSegmentTypeDef]
    assetCompositeModelName: str
    assetCompositeModelDescription: str
    assetCompositeModelType: str
    assetCompositeModelProperties: List[AssetPropertyTypeDef]
    assetCompositeModelSummaries: List[AssetCompositeModelSummaryTypeDef]
    actionDefinitions: List[ActionDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchPutAssetPropertyErrorEntryTypeDef(BaseValidatorModel):
    entryId: str
    errors: List[BatchPutAssetPropertyErrorTypeDef]


class BatchGetAssetPropertyAggregatesRequestTypeDef(BaseValidatorModel):
    entries: Sequence[BatchGetAssetPropertyAggregatesEntryTypeDef]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class BatchGetAssetPropertyValueHistoryRequestTypeDef(BaseValidatorModel):
    entries: Sequence[BatchGetAssetPropertyValueHistoryEntryTypeDef]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeDefaultEncryptionConfigurationResponseTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    configurationStatus: ConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutDefaultEncryptionConfigurationResponseTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    configurationStatus: ConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JobConfigurationOutputTypeDef(BaseValidatorModel):
    fileFormat: FileFormatOutputTypeDef


class JobConfigurationTypeDef(BaseValidatorModel):
    fileFormat: FileFormatTypeDef


class DescribeStorageConfigurationResponseTypeDef(BaseValidatorModel):
    storageType: StorageTypeType
    multiLayerStorage: MultiLayerStorageTypeDef
    disassociatedDataStorage: DisassociatedDataStorageStateType
    retentionPeriod: RetentionPeriodTypeDef
    configurationStatus: ConfigurationStatusTypeDef
    lastUpdateDate: datetime
    warmTier: WarmTierStateType
    warmTierRetentionPeriod: WarmTierRetentionPeriodTypeDef
    disallowIngestNullNaN: bool
    ResponseMetadata: ResponseMetadataTypeDef


class PutStorageConfigurationRequestTypeDef(BaseValidatorModel):
    storageType: StorageTypeType
    multiLayerStorage: Optional[MultiLayerStorageTypeDef] = None
    disassociatedDataStorage: Optional[DisassociatedDataStorageStateType] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    warmTier: Optional[WarmTierStateType] = None
    warmTierRetentionPeriod: Optional[WarmTierRetentionPeriodTypeDef] = None
    disallowIngestNullNaN: Optional[bool] = None


class PutStorageConfigurationResponseTypeDef(BaseValidatorModel):
    storageType: StorageTypeType
    multiLayerStorage: MultiLayerStorageTypeDef
    disassociatedDataStorage: DisassociatedDataStorageStateType
    retentionPeriod: RetentionPeriodTypeDef
    configurationStatus: ConfigurationStatusTypeDef
    warmTier: WarmTierStateType
    warmTierRetentionPeriod: WarmTierRetentionPeriodTypeDef
    disallowIngestNullNaN: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ColumnInfoTypeDef(BaseValidatorModel):
    pass


class ExecuteQueryResponsePaginatorTypeDef(BaseValidatorModel):
    columns: List[ColumnInfoTypeDef]
    rows: List[RowPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ExecuteQueryResponseTypeDef(BaseValidatorModel):
    columns: List[ColumnInfoTypeDef]
    rows: List[RowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ExecuteQueryResponseWaiterTypeDef(BaseValidatorModel):
    columns: List[ColumnInfoTypeDef]
    rows: List[RowWaiterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssetModelStatusTypeDef(BaseValidatorModel):
    state: AssetModelStateType
    error: Optional[ErrorDetailsTypeDef] = None


class AssetStatusTypeDef(BaseValidatorModel):
    state: AssetStateType
    error: Optional[ErrorDetailsTypeDef] = None


class DatasetStatusTypeDef(BaseValidatorModel):
    state: DatasetStateType
    error: Optional[ErrorDetailsTypeDef] = None


class MeasurementTypeDef(BaseValidatorModel):
    processingConfig: Optional[MeasurementProcessingConfigTypeDef] = None


class CreateGatewayRequestTypeDef(BaseValidatorModel):
    gatewayName: str
    gatewayPlatform: GatewayPlatformTypeDef
    gatewayVersion: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DescribeGatewayResponseTypeDef(BaseValidatorModel):
    gatewayId: str
    gatewayName: str
    gatewayArn: str
    gatewayPlatform: GatewayPlatformTypeDef
    gatewayVersion: str
    gatewayCapabilitySummaries: List[GatewayCapabilitySummaryTypeDef]
    creationDate: datetime
    lastUpdateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GatewaySummaryTypeDef(BaseValidatorModel):
    gatewayId: str
    gatewayName: str
    creationDate: datetime
    lastUpdateDate: datetime
    gatewayPlatform: Optional[GatewayPlatformTypeDef] = None
    gatewayVersion: Optional[str] = None
    gatewayCapabilitySummaries: Optional[List[GatewayCapabilitySummaryTypeDef]] = None


class DatasetSourceTypeDef(BaseValidatorModel):
    sourceType: Literal["KENDRA"]
    sourceFormat: Literal["KNOWLEDGE_BASE"]
    sourceDetail: Optional[SourceDetailTypeDef] = None


class DataSetReferenceTypeDef(BaseValidatorModel):
    datasetArn: Optional[str] = None
    source: Optional[SourceTypeDef] = None


class CreatePortalResponseTypeDef(BaseValidatorModel):
    portalId: str
    portalArn: str
    portalStartUrl: str
    portalStatus: PortalStatusTypeDef
    ssoApplicationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePortalResponseTypeDef(BaseValidatorModel):
    portalStatus: PortalStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ImageLocationTypeDef(BaseValidatorModel):
    pass


class DescribePortalResponseTypeDef(BaseValidatorModel):
    portalId: str
    portalArn: str
    portalName: str
    portalDescription: str
    portalClientId: str
    portalStartUrl: str
    portalContactEmail: str
    portalStatus: PortalStatusTypeDef
    portalCreationDate: datetime
    portalLastUpdateDate: datetime
    portalLogoImageLocation: ImageLocationTypeDef
    roleArn: str
    portalAuthMode: AuthModeType
    notificationSenderEmail: str
    alarms: AlarmsTypeDef
    portalType: PortalTypeType
    portalTypeConfiguration: Dict[str, PortalTypeEntryOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePortalResponseTypeDef(BaseValidatorModel):
    portalStatus: PortalStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PortalTypeEntryUnionTypeDef(BaseValidatorModel):
    pass


class ImageFileTypeDef(BaseValidatorModel):
    pass


class CreatePortalRequestTypeDef(BaseValidatorModel):
    portalName: str
    portalContactEmail: str
    roleArn: str
    portalDescription: Optional[str] = None
    clientToken: Optional[str] = None
    portalLogoImageFile: Optional[ImageFileTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    portalAuthMode: Optional[AuthModeType] = None
    notificationSenderEmail: Optional[str] = None
    alarms: Optional[AlarmsTypeDef] = None
    portalType: Optional[PortalTypeType] = None
    portalTypeConfiguration: Optional[Mapping[str, PortalTypeEntryUnionTypeDef]] = None


class CreateAccessPolicyRequestTypeDef(BaseValidatorModel):
    accessPolicyIdentity: IdentityTypeDef
    accessPolicyResource: ResourceTypeDef
    accessPolicyPermission: PermissionType
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DescribeAccessPolicyResponseTypeDef(BaseValidatorModel):
    accessPolicyId: str
    accessPolicyArn: str
    accessPolicyIdentity: IdentityTypeDef
    accessPolicyResource: ResourceTypeDef
    accessPolicyPermission: PermissionType
    accessPolicyCreationDate: datetime
    accessPolicyLastUpdateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAccessPolicyRequestTypeDef(BaseValidatorModel):
    accessPolicyId: str
    accessPolicyIdentity: IdentityTypeDef
    accessPolicyResource: ResourceTypeDef
    accessPolicyPermission: PermissionType
    clientToken: Optional[str] = None


class AssetPropertyValueTypeDef(BaseValidatorModel):
    value: VariantTypeDef
    timestamp: TimeInNanosTypeDef
    quality: Optional[QualityType] = None


class InterpolatedAssetPropertyValueTypeDef(BaseValidatorModel):
    timestamp: TimeInNanosTypeDef
    value: VariantTypeDef


class BatchGetAssetPropertyAggregatesResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchGetAssetPropertyAggregatesErrorEntryTypeDef]
    successEntries: List[BatchGetAssetPropertyAggregatesSuccessEntryTypeDef]
    skippedEntries: List[BatchGetAssetPropertyAggregatesSkippedEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MetricOutputTypeDef(BaseValidatorModel):
    expression: str
    variables: List[ExpressionVariableOutputTypeDef]
    window: MetricWindowTypeDef
    processingConfig: Optional[MetricProcessingConfigTypeDef] = None


class TransformOutputTypeDef(BaseValidatorModel):
    expression: str
    variables: List[ExpressionVariableOutputTypeDef]
    processingConfig: Optional[TransformProcessingConfigTypeDef] = None


class VariableValueUnionTypeDef(BaseValidatorModel):
    pass


class ExpressionVariableTypeDef(BaseValidatorModel):
    name: str
    value: VariableValueUnionTypeDef


class BatchPutAssetPropertyValueResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchPutAssetPropertyErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ImageTypeDef(BaseValidatorModel):
    pass


class UpdatePortalRequestTypeDef(BaseValidatorModel):
    portalId: str
    portalName: str
    portalContactEmail: str
    roleArn: str
    portalDescription: Optional[str] = None
    portalLogoImage: Optional[ImageTypeDef] = None
    clientToken: Optional[str] = None
    notificationSenderEmail: Optional[str] = None
    alarms: Optional[AlarmsTypeDef] = None
    portalType: Optional[PortalTypeType] = None
    portalTypeConfiguration: Optional[Mapping[str, PortalTypeEntryUnionTypeDef]] = None


class DescribeBulkImportJobResponseTypeDef(BaseValidatorModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    jobRoleArn: str
    files: List[FileTypeDef]
    errorReportLocation: ErrorReportLocationTypeDef
    jobConfiguration: JobConfigurationOutputTypeDef
    jobCreationDate: datetime
    jobLastUpdateDate: datetime
    adaptiveIngestion: bool
    deleteFilesAfterImport: bool
    ResponseMetadata: ResponseMetadataTypeDef


class AssetModelCompositeModelPathSegmentTypeDef(BaseValidatorModel):
    pass


class CreateAssetModelCompositeModelResponseTypeDef(BaseValidatorModel):
    assetModelCompositeModelId: str
    assetModelCompositeModelPath: List[AssetModelCompositeModelPathSegmentTypeDef]
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAssetModelResponseTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelArn: str
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAssetModelCompositeModelResponseTypeDef(BaseValidatorModel):
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAssetModelResponseTypeDef(BaseValidatorModel):
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAssetModelCompositeModelResponseTypeDef(BaseValidatorModel):
    assetModelCompositeModelPath: List[AssetModelCompositeModelPathSegmentTypeDef]
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAssetModelResponseTypeDef(BaseValidatorModel):
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAssetResponseTypeDef(BaseValidatorModel):
    assetId: str
    assetArn: str
    assetStatus: AssetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAssetResponseTypeDef(BaseValidatorModel):
    assetStatus: AssetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssetHierarchyTypeDef(BaseValidatorModel):
    pass


class AssetCompositeModelTypeDef(BaseValidatorModel):
    pass


class DescribeAssetResponseTypeDef(BaseValidatorModel):
    assetId: str
    assetArn: str
    assetName: str
    assetModelId: str
    assetProperties: List[AssetPropertyTypeDef]
    assetHierarchies: List[AssetHierarchyTypeDef]
    assetCompositeModels: List[AssetCompositeModelTypeDef]
    assetCreationDate: datetime
    assetLastUpdateDate: datetime
    assetStatus: AssetStatusTypeDef
    assetDescription: str
    assetCompositeModelSummaries: List[AssetCompositeModelSummaryTypeDef]
    assetExternalId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAssetResponseTypeDef(BaseValidatorModel):
    assetStatus: AssetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetResponseTypeDef(BaseValidatorModel):
    datasetId: str
    datasetArn: str
    datasetStatus: DatasetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDatasetResponseTypeDef(BaseValidatorModel):
    datasetStatus: DatasetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDatasetResponseTypeDef(BaseValidatorModel):
    datasetId: str
    datasetArn: str
    datasetStatus: DatasetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListGatewaysResponseTypeDef(BaseValidatorModel):
    gatewaySummaries: List[GatewaySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateDatasetRequestTypeDef(BaseValidatorModel):
    datasetName: str
    datasetSource: DatasetSourceTypeDef
    datasetId: Optional[str] = None
    datasetDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    datasetId: str
    datasetArn: str
    datasetName: str
    datasetDescription: str
    datasetSource: DatasetSourceTypeDef
    datasetStatus: DatasetStatusTypeDef
    datasetCreationDate: datetime
    datasetLastUpdateDate: datetime
    datasetVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDatasetRequestTypeDef(BaseValidatorModel):
    datasetId: str
    datasetName: str
    datasetSource: DatasetSourceTypeDef
    datasetDescription: Optional[str] = None
    clientToken: Optional[str] = None


class ReferenceTypeDef(BaseValidatorModel):
    dataset: Optional[DataSetReferenceTypeDef] = None


class PortalSummaryTypeDef(BaseValidatorModel):
    pass


class ListPortalsResponseTypeDef(BaseValidatorModel):
    portalSummaries: List[PortalSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AccessPolicySummaryTypeDef(BaseValidatorModel):
    pass


class ListAccessPoliciesResponseTypeDef(BaseValidatorModel):
    accessPolicySummaries: List[AccessPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchGetAssetPropertyValueHistorySuccessEntryTypeDef(BaseValidatorModel):
    entryId: str
    assetPropertyValueHistory: List[AssetPropertyValueTypeDef]


class BatchGetAssetPropertyValueSuccessEntryTypeDef(BaseValidatorModel):
    entryId: str
    assetPropertyValue: Optional[AssetPropertyValueTypeDef] = None


class GetAssetPropertyValueHistoryResponseTypeDef(BaseValidatorModel):
    assetPropertyValueHistory: List[AssetPropertyValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetAssetPropertyValueResponseTypeDef(BaseValidatorModel):
    propertyValue: AssetPropertyValueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutAssetPropertyValueEntryTypeDef(BaseValidatorModel):
    entryId: str
    propertyValues: Sequence[AssetPropertyValueTypeDef]
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


class GetInterpolatedAssetPropertyValuesResponseTypeDef(BaseValidatorModel):
    interpolatedAssetPropertyValues: List[InterpolatedAssetPropertyValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PropertyTypeOutputTypeDef(BaseValidatorModel):
    attribute: Optional[AttributeTypeDef] = None
    measurement: Optional[MeasurementTypeDef] = None
    transform: Optional[TransformOutputTypeDef] = None
    metric: Optional[MetricOutputTypeDef] = None


class JobConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateBulkImportJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    jobRoleArn: str
    files: Sequence[FileTypeDef]
    errorReportLocation: ErrorReportLocationTypeDef
    jobConfiguration: JobConfigurationUnionTypeDef
    adaptiveIngestion: Optional[bool] = None
    deleteFilesAfterImport: Optional[bool] = None


class AssetModelSummaryTypeDef(BaseValidatorModel):
    pass


class ListAssetModelsResponseTypeDef(BaseValidatorModel):
    assetModelSummaries: List[AssetModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssetSummaryTypeDef(BaseValidatorModel):
    pass


class ListAssetsResponseTypeDef(BaseValidatorModel):
    assetSummaries: List[AssetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssociatedAssetsSummaryTypeDef(BaseValidatorModel):
    pass


class ListAssociatedAssetsResponseTypeDef(BaseValidatorModel):
    assetSummaries: List[AssociatedAssetsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DatasetSummaryTypeDef(BaseValidatorModel):
    pass


class ListDatasetsResponseTypeDef(BaseValidatorModel):
    datasetSummaries: List[DatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CitationTypeDef(BaseValidatorModel):
    reference: Optional[ReferenceTypeDef] = None
    content: Optional[ContentTypeDef] = None


class BatchGetAssetPropertyValueHistoryResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchGetAssetPropertyValueHistoryErrorEntryTypeDef]
    successEntries: List[BatchGetAssetPropertyValueHistorySuccessEntryTypeDef]
    skippedEntries: List[BatchGetAssetPropertyValueHistorySkippedEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchGetAssetPropertyValueResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchGetAssetPropertyValueErrorEntryTypeDef]
    successEntries: List[BatchGetAssetPropertyValueSuccessEntryTypeDef]
    skippedEntries: List[BatchGetAssetPropertyValueSkippedEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchPutAssetPropertyValueRequestTypeDef(BaseValidatorModel):
    entries: Sequence[PutAssetPropertyValueEntryTypeDef]
    enablePartialEntryProcessing: Optional[bool] = None


class ExpressionVariableUnionTypeDef(BaseValidatorModel):
    pass


class MetricTypeDef(BaseValidatorModel):
    expression: str
    variables: Sequence[ExpressionVariableUnionTypeDef]
    window: MetricWindowTypeDef
    processingConfig: Optional[MetricProcessingConfigTypeDef] = None


class TransformTypeDef(BaseValidatorModel):
    expression: str
    variables: Sequence[ExpressionVariableUnionTypeDef]
    processingConfig: Optional[TransformProcessingConfigTypeDef] = None


class InvocationOutputTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    citations: Optional[List[CitationTypeDef]] = None


class AssetModelPropertyOutputTypeDef(BaseValidatorModel):
    pass


class DescribeAssetModelCompositeModelResponseTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelExternalId: str
    assetModelCompositeModelPath: List[AssetModelCompositeModelPathSegmentTypeDef]
    assetModelCompositeModelName: str
    assetModelCompositeModelDescription: str
    assetModelCompositeModelType: str
    assetModelCompositeModelProperties: List[AssetModelPropertyOutputTypeDef]
    compositionDetails: CompositionDetailsTypeDef
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummaryTypeDef]
    actionDefinitions: List[ActionDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AssetModelPropertySummaryTypeDef(BaseValidatorModel):
    pass


class ListAssetModelPropertiesResponseTypeDef(BaseValidatorModel):
    assetModelPropertySummaries: List[AssetModelPropertySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ResponseStreamTypeDef(BaseValidatorModel):
    trace: Optional[TraceTypeDef] = None
    output: Optional[InvocationOutputTypeDef] = None
    accessDeniedException: Optional[AccessDeniedExceptionTypeDef] = None
    conflictingOperationException: Optional[ConflictingOperationExceptionTypeDef] = None
    internalFailureException: Optional[InternalFailureExceptionTypeDef] = None
    invalidRequestException: Optional[InvalidRequestExceptionTypeDef] = None
    limitExceededException: Optional[LimitExceededExceptionTypeDef] = None
    resourceNotFoundException: Optional[ResourceNotFoundExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None


class AssetModelCompositeModelOutputTypeDef(BaseValidatorModel):
    pass


class AssetModelHierarchyTypeDef(BaseValidatorModel):
    pass


class DescribeAssetModelResponseTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelExternalId: str
    assetModelArn: str
    assetModelName: str
    assetModelType: AssetModelTypeType
    assetModelDescription: str
    assetModelProperties: List[AssetModelPropertyOutputTypeDef]
    assetModelHierarchies: List[AssetModelHierarchyTypeDef]
    assetModelCompositeModels: List[AssetModelCompositeModelOutputTypeDef]
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummaryTypeDef]
    assetModelCreationDate: datetime
    assetModelLastUpdateDate: datetime
    assetModelStatus: AssetModelStatusTypeDef
    assetModelVersion: str
    eTag: str
    ResponseMetadata: ResponseMetadataTypeDef


class PropertyTypeDef(BaseValidatorModel):
    pass


class CompositeModelPropertyTypeDef(BaseValidatorModel):
    pass


class DescribeAssetPropertyResponseTypeDef(BaseValidatorModel):
    assetId: str
    assetName: str
    assetModelId: str
    assetProperty: PropertyTypeDef
    compositeModel: CompositeModelPropertyTypeDef
    assetExternalId: str
    ResponseMetadata: ResponseMetadataTypeDef


class TransformUnionTypeDef(BaseValidatorModel):
    pass


class MetricUnionTypeDef(BaseValidatorModel):
    pass


class PropertyTypeTypeDef(BaseValidatorModel):
    attribute: Optional[AttributeTypeDef] = None
    measurement: Optional[MeasurementTypeDef] = None
    transform: Optional[TransformUnionTypeDef] = None
    metric: Optional[MetricUnionTypeDef] = None


class InvokeAssistantResponseTypeDef(BaseValidatorModel):
    body: EventStream[ResponseStreamTypeDef]
    conversationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssetModelPropertyDefinitionTypeDef(BaseValidatorModel):
    pass


class CreateAssetModelCompositeModelRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelName: str
    assetModelCompositeModelType: str
    assetModelCompositeModelExternalId: Optional[str] = None
    parentAssetModelCompositeModelId: Optional[str] = None
    assetModelCompositeModelId: Optional[str] = None
    assetModelCompositeModelDescription: Optional[str] = None
    clientToken: Optional[str] = None
    composedAssetModelId: Optional[str] = None
    assetModelCompositeModelProperties: Optional[Sequence[AssetModelPropertyDefinitionTypeDef]] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None


class AssetModelHierarchyDefinitionTypeDef(BaseValidatorModel):
    pass


class AssetModelCompositeModelDefinitionTypeDef(BaseValidatorModel):
    pass


class CreateAssetModelRequestTypeDef(BaseValidatorModel):
    assetModelName: str
    assetModelType: Optional[AssetModelTypeType] = None
    assetModelId: Optional[str] = None
    assetModelExternalId: Optional[str] = None
    assetModelDescription: Optional[str] = None
    assetModelProperties: Optional[Sequence[AssetModelPropertyDefinitionTypeDef]] = None
    assetModelHierarchies: Optional[Sequence[AssetModelHierarchyDefinitionTypeDef]] = None
    assetModelCompositeModels: Optional[Sequence[AssetModelCompositeModelDefinitionTypeDef]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class AssetModelPropertyUnionTypeDef(BaseValidatorModel):
    pass


class UpdateAssetModelCompositeModelRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelName: str
    assetModelCompositeModelExternalId: Optional[str] = None
    assetModelCompositeModelDescription: Optional[str] = None
    clientToken: Optional[str] = None
    assetModelCompositeModelProperties: Optional[Sequence[AssetModelPropertyUnionTypeDef]] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None


class AssetModelCompositeModelUnionTypeDef(BaseValidatorModel):
    pass


class UpdateAssetModelRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelName: str
    assetModelExternalId: Optional[str] = None
    assetModelDescription: Optional[str] = None
    assetModelProperties: Optional[Sequence[AssetModelPropertyUnionTypeDef]] = None
    assetModelHierarchies: Optional[Sequence[AssetModelHierarchyTypeDef]] = None
    assetModelCompositeModels: Optional[Sequence[AssetModelCompositeModelUnionTypeDef]] = None
    clientToken: Optional[str] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None



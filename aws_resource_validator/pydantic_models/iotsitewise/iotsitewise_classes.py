from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessDeniedException(BaseValidatorModel):
    message: Optional[str] = None


class ActionDefinition(BaseValidatorModel):
    actionDefinitionId: str
    actionName: str
    actionType: str


class ActionPayload(BaseValidatorModel):
    stringValue: str


class TargetResource(BaseValidatorModel):
    assetId: str


class Aggregates(BaseValidatorModel):
    average: Optional[float] = None
    count: Optional[float] = None
    maximum: Optional[float] = None
    minimum: Optional[float] = None
    sum: Optional[float] = None
    standardDeviation: Optional[float] = None


class Alarms(BaseValidatorModel):
    alarmRoleArn: str
    notificationLambdaArn: Optional[str] = None


class AssetCompositeModelPathSegment(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None


class AssetErrorDetails(BaseValidatorModel):
    assetId: str
    code: Literal['INTERNAL_FAILURE']
    message: str


class AssetHierarchyInfo(BaseValidatorModel):
    parentAssetId: Optional[str] = None
    childAssetId: Optional[str] = None


class AssetHierarchy(BaseValidatorModel):
    name: str
    id: Optional[str] = None
    externalId: Optional[str] = None


class AssetModelCompositeModelPathSegment(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None


class AssetModelHierarchyDefinition(BaseValidatorModel):
    name: str
    childAssetModelId: str
    id: Optional[str] = None
    externalId: Optional[str] = None


class AssetModelHierarchy(BaseValidatorModel):
    name: str
    childAssetModelId: str
    id: Optional[str] = None
    externalId: Optional[str] = None


class AssetModelPropertyPathSegment(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None


class AssetPropertyPathSegment(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None


class PropertyNotification(BaseValidatorModel):
    topic: str
    state: PropertyNotificationStateType


class TimeInNanos(BaseValidatorModel):
    timeInSeconds: int
    offsetInNanos: Optional[int] = None


class AssociateAssetsRequest(BaseValidatorModel):
    assetId: str
    hierarchyId: str
    childAssetId: str
    clientToken: Optional[str] = None


class AssociateTimeSeriesToAssetPropertyRequest(BaseValidatorModel):
    alias: str
    assetId: str
    propertyId: str
    clientToken: Optional[str] = None


class Attribute(BaseValidatorModel):
    defaultValue: Optional[str] = None


class BatchAssociateProjectAssetsRequest(BaseValidatorModel):
    projectId: str
    assetIds: List[str]
    clientToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDisassociateProjectAssetsRequest(BaseValidatorModel):
    projectId: str
    assetIds: List[str]
    clientToken: Optional[str] = None

Timestamp = Union[datetime, str]


class BatchGetAssetPropertyAggregatesErrorEntry(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyAggregatesErrorCodeType
    errorMessage: str
    entryId: str


class BatchGetAssetPropertyAggregatesErrorInfo(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyAggregatesErrorCodeType
    errorTimestamp: datetime


class BatchGetAssetPropertyValueEntry(BaseValidatorModel):
    entryId: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


class BatchGetAssetPropertyValueErrorEntry(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyValueErrorCodeType
    errorMessage: str
    entryId: str


class BatchGetAssetPropertyValueErrorInfo(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyValueErrorCodeType
    errorTimestamp: datetime


class BatchGetAssetPropertyValueHistoryErrorEntry(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyValueHistoryErrorCodeType
    errorMessage: str
    entryId: str


class BatchGetAssetPropertyValueHistoryErrorInfo(BaseValidatorModel):
    errorCode: BatchGetAssetPropertyValueHistoryErrorCodeType
    errorTimestamp: datetime

Blob = Union[str, bytes, IO[Any], StreamingBody]


class Content(BaseValidatorModel):
    text: Optional[str] = None


class ColumnType(BaseValidatorModel):
    scalarType: Optional[ScalarTypeType] = None


class CompositionRelationshipItem(BaseValidatorModel):
    id: Optional[str] = None


class CompositionRelationshipSummary(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelType: str


class ConfigurationErrorDetails(BaseValidatorModel):
    code: ErrorCodeType
    message: str


class ConflictingOperationException(BaseValidatorModel):
    message: str
    resourceId: str
    resourceArn: str


class CreateAssetRequest(BaseValidatorModel):
    assetName: str
    assetModelId: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    assetDescription: Optional[str] = None
    assetId: Optional[str] = None
    assetExternalId: Optional[str] = None


class ErrorReportLocation(BaseValidatorModel):
    bucket: str
    prefix: str


class File(BaseValidatorModel):
    bucket: str
    key: str
    versionId: Optional[str] = None


class CreateDashboardRequest(BaseValidatorModel):
    projectId: str
    dashboardName: str
    dashboardDefinition: str
    dashboardDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateProjectRequest(BaseValidatorModel):
    portalId: str
    projectName: str
    projectDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CsvOutput(BaseValidatorModel):
    columnNames: List[ColumnNameType]


class Csv(BaseValidatorModel):
    columnNames: List[ColumnNameType]


class CustomerManagedS3Storage(BaseValidatorModel):
    s3ResourceArn: str
    roleArn: str


class DashboardSummary(BaseValidatorModel):
    id: str
    name: str
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None


class DatumPaginator(BaseValidatorModel):
    scalarValue: Optional[str] = None
    arrayValue: Optional[List[Dict[str, Any]]] = None
    rowValue: Optional[Dict[str, Any]] = None
    nullValue: Optional[bool] = None


class Datum(BaseValidatorModel):
    scalarValue: Optional[str] = None
    arrayValue: Optional[List[Dict[str, Any]]] = None
    rowValue: Optional[Dict[str, Any]] = None
    nullValue: Optional[bool] = None


class DatumWaiter(BaseValidatorModel):
    scalarValue: Optional[str] = None
    arrayValue: Optional[List[Dict[str, Any]]] = None
    rowValue: Optional[Dict[str, Any]] = None
    nullValue: Optional[bool] = None


class DeleteAccessPolicyRequest(BaseValidatorModel):
    accessPolicyId: str
    clientToken: Optional[str] = None


class DeleteAssetModelCompositeModelRequest(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    clientToken: Optional[str] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None


class DeleteAssetModelRequest(BaseValidatorModel):
    assetModelId: str
    clientToken: Optional[str] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None


class DeleteAssetRequest(BaseValidatorModel):
    assetId: str
    clientToken: Optional[str] = None


class DeleteDashboardRequest(BaseValidatorModel):
    dashboardId: str
    clientToken: Optional[str] = None


class DeleteDatasetRequest(BaseValidatorModel):
    datasetId: str
    clientToken: Optional[str] = None


class DeleteGatewayRequest(BaseValidatorModel):
    gatewayId: str


class DeletePortalRequest(BaseValidatorModel):
    portalId: str
    clientToken: Optional[str] = None


class DeleteProjectRequest(BaseValidatorModel):
    projectId: str
    clientToken: Optional[str] = None


class DeleteTimeSeriesRequest(BaseValidatorModel):
    alias: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    clientToken: Optional[str] = None


class DescribeAccessPolicyRequest(BaseValidatorModel):
    accessPolicyId: str


class DescribeActionRequest(BaseValidatorModel):
    actionId: str


class DescribeAssetCompositeModelRequest(BaseValidatorModel):
    assetId: str
    assetCompositeModelId: str


class DescribeAssetModelCompositeModelRequest(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelVersion: Optional[str] = None


class DescribeAssetModelRequest(BaseValidatorModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    assetModelVersion: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeAssetPropertyRequest(BaseValidatorModel):
    assetId: str
    propertyId: str


class DescribeAssetRequest(BaseValidatorModel):
    assetId: str
    excludeProperties: Optional[bool] = None


class DescribeBulkImportJobRequest(BaseValidatorModel):
    jobId: str


class DescribeDashboardRequest(BaseValidatorModel):
    dashboardId: str


class DescribeDatasetRequest(BaseValidatorModel):
    datasetId: str


class DescribeGatewayCapabilityConfigurationRequest(BaseValidatorModel):
    gatewayId: str
    capabilityNamespace: str


class DescribeGatewayRequest(BaseValidatorModel):
    gatewayId: str


class GatewayCapabilitySummary(BaseValidatorModel):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatusType


class LoggingOptions(BaseValidatorModel):
    level: LoggingLevelType


class DescribePortalRequest(BaseValidatorModel):
    portalId: str


class ImageLocation(BaseValidatorModel):
    id: str
    url: str


class PortalTypeEntryOutput(BaseValidatorModel):
    portalTools: Optional[List[str]] = None


class DescribeProjectRequest(BaseValidatorModel):
    projectId: str


class RetentionPeriod(BaseValidatorModel):
    numberOfDays: Optional[int] = None
    unlimited: Optional[bool] = None


class WarmTierRetentionPeriod(BaseValidatorModel):
    numberOfDays: Optional[int] = None
    unlimited: Optional[bool] = None


class DescribeTimeSeriesRequest(BaseValidatorModel):
    alias: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None


class DetailedError(BaseValidatorModel):
    code: DetailedErrorCodeType
    message: str


class DisassociateAssetsRequest(BaseValidatorModel):
    assetId: str
    hierarchyId: str
    childAssetId: str
    clientToken: Optional[str] = None


class DisassociateTimeSeriesFromAssetPropertyRequest(BaseValidatorModel):
    alias: str
    assetId: str
    propertyId: str
    clientToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ExecuteQueryRequest(BaseValidatorModel):
    queryStatement: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    clientToken: Optional[str] = None


class ForwardingConfig(BaseValidatorModel):
    state: ForwardingConfigStateType


class Greengrass(BaseValidatorModel):
    groupArn: str


class GreengrassV2(BaseValidatorModel):
    coreDeviceThingName: str
    coreDeviceOperatingSystem: Optional[CoreDeviceOperatingSystemType] = None


class SiemensIE(BaseValidatorModel):
    iotCoreThingName: str


class GetAssetPropertyValueRequest(BaseValidatorModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


class GetInterpolatedAssetPropertyValuesRequest(BaseValidatorModel):
    startTimeInSeconds: int
    endTimeInSeconds: int
    quality: QualityType
    intervalInSeconds: int
    type: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startTimeOffsetInNanos: Optional[int] = None
    endTimeOffsetInNanos: Optional[int] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    intervalWindowInSeconds: Optional[int] = None


class GroupIdentity(BaseValidatorModel):
    id: str


class IAMRoleIdentity(BaseValidatorModel):
    arn: str


class IAMUserIdentity(BaseValidatorModel):
    arn: str


class UserIdentity(BaseValidatorModel):
    id: str


class InternalFailureException(BaseValidatorModel):
    message: str


class InvalidRequestException(BaseValidatorModel):
    message: str


class InvokeAssistantRequest(BaseValidatorModel):
    message: str
    conversationId: Optional[str] = None
    enableTrace: Optional[bool] = None


class JobSummary(BaseValidatorModel):
    id: str
    name: str
    status: JobStatusType


class KendraSourceDetail(BaseValidatorModel):
    knowledgeBaseArn: str
    roleArn: str


class LimitExceededException(BaseValidatorModel):
    message: str


class ListAccessPoliciesRequest(BaseValidatorModel):
    identityType: Optional[IdentityTypeType] = None
    identityId: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    iamArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListActionsRequest(BaseValidatorModel):
    targetResourceType: Literal['ASSET']
    targetResourceId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssetModelCompositeModelsRequest(BaseValidatorModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetModelVersion: Optional[str] = None


class ListAssetModelPropertiesRequest(BaseValidatorModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListAssetModelPropertiesFilterType] = None
    assetModelVersion: Optional[str] = None


class ListAssetModelsRequest(BaseValidatorModel):
    assetModelTypes: Optional[List[AssetModelTypeType]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetModelVersion: Optional[str] = None


class ListAssetPropertiesRequest(BaseValidatorModel):
    assetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListAssetPropertiesFilterType] = None


class ListAssetRelationshipsRequest(BaseValidatorModel):
    assetId: str
    traversalType: Literal['PATH_TO_ROOT']
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssetsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetModelId: Optional[str] = None
    filter: Optional[ListAssetsFilterType] = None


class ListAssociatedAssetsRequest(BaseValidatorModel):
    assetId: str
    hierarchyId: Optional[str] = None
    traversalDirection: Optional[TraversalDirectionType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBulkImportJobsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListBulkImportJobsFilterType] = None


class ListCompositionRelationshipsRequest(BaseValidatorModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDashboardsRequest(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetsRequest(BaseValidatorModel):
    sourceType: Literal['KENDRA']
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListGatewaysRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPortalsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListProjectAssetsRequest(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListProjectsRequest(BaseValidatorModel):
    portalId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ProjectSummary(BaseValidatorModel):
    id: str
    name: str
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListTimeSeriesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetId: Optional[str] = None
    aliasPrefix: Optional[str] = None
    timeSeriesType: Optional[ListTimeSeriesTypeType] = None


class TimeSeriesSummary(BaseValidatorModel):
    timeSeriesId: str
    dataType: PropertyDataTypeType
    timeSeriesCreationDate: datetime
    timeSeriesLastUpdateDate: datetime
    timeSeriesArn: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    alias: Optional[str] = None
    dataTypeSpec: Optional[str] = None


class Location(BaseValidatorModel):
    uri: Optional[str] = None


class MetricProcessingConfig(BaseValidatorModel):
    computeLocation: ComputeLocationType


class TumblingWindow(BaseValidatorModel):
    interval: str
    offset: Optional[str] = None


class MonitorErrorDetails(BaseValidatorModel):
    code: Optional[MonitorErrorCodeType] = None
    message: Optional[str] = None


class PortalResource(BaseValidatorModel):
    id: str


class PortalTypeEntry(BaseValidatorModel):
    portalTools: Optional[List[str]] = None


class ProjectResource(BaseValidatorModel):
    id: str


class PropertyValueNullValue(BaseValidatorModel):
    valueType: RawValueTypeType


class PutDefaultEncryptionConfigurationRequest(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyId: Optional[str] = None


class ResourceNotFoundException(BaseValidatorModel):
    message: str


class ThrottlingException(BaseValidatorModel):
    message: str


class Trace(BaseValidatorModel):
    text: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateAssetPropertyRequest(BaseValidatorModel):
    assetId: str
    propertyId: str
    propertyAlias: Optional[str] = None
    propertyNotificationState: Optional[PropertyNotificationStateType] = None
    clientToken: Optional[str] = None
    propertyUnit: Optional[str] = None


class UpdateAssetRequest(BaseValidatorModel):
    assetId: str
    assetName: str
    clientToken: Optional[str] = None
    assetDescription: Optional[str] = None
    assetExternalId: Optional[str] = None


class UpdateDashboardRequest(BaseValidatorModel):
    dashboardId: str
    dashboardName: str
    dashboardDefinition: str
    dashboardDescription: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateGatewayCapabilityConfigurationRequest(BaseValidatorModel):
    gatewayId: str
    capabilityNamespace: str
    capabilityConfiguration: str


class UpdateGatewayRequest(BaseValidatorModel):
    gatewayId: str
    gatewayName: str


class UpdateProjectRequest(BaseValidatorModel):
    projectId: str
    projectName: str
    projectDescription: Optional[str] = None
    clientToken: Optional[str] = None


class ActionSummary(BaseValidatorModel):
    actionId: Optional[str] = None
    actionDefinitionId: Optional[str] = None
    targetResource: Optional[TargetResource] = None


class ExecuteActionRequest(BaseValidatorModel):
    targetResource: TargetResource
    actionDefinitionId: str
    actionPayload: ActionPayload
    clientToken: Optional[str] = None


class AggregatedValue(BaseValidatorModel):
    timestamp: datetime
    value: Aggregates
    quality: Optional[QualityType] = None


class AssetCompositeModelSummary(BaseValidatorModel):
    id: str
    name: str
    type: str
    description: str
    path: List[AssetCompositeModelPathSegment]
    externalId: Optional[str] = None


class AssetRelationshipSummary(BaseValidatorModel):
    relationshipType: Literal['HIERARCHY']
    hierarchyInfo: Optional[AssetHierarchyInfo] = None


class AssetModelCompositeModelSummary(BaseValidatorModel):
    id: str
    name: str
    type: str
    externalId: Optional[str] = None
    description: Optional[str] = None
    path: Optional[List[AssetModelCompositeModelPathSegment]] = None


class VariableValueOutput(BaseValidatorModel):
    propertyId: Optional[str] = None
    hierarchyId: Optional[str] = None
    propertyPath: Optional[List[AssetModelPropertyPathSegment]] = None


class VariableValue(BaseValidatorModel):
    propertyId: Optional[str] = None
    hierarchyId: Optional[str] = None
    propertyPath: Optional[List[AssetModelPropertyPathSegment]] = None


class AssetPropertySummary(BaseValidatorModel):
    id: str
    alias: Optional[str] = None
    unit: Optional[str] = None
    notification: Optional[PropertyNotification] = None
    assetCompositeModelId: Optional[str] = None
    path: Optional[List[AssetPropertyPathSegment]] = None
    externalId: Optional[str] = None


class AssetProperty(BaseValidatorModel):
    id: str
    name: str
    dataType: PropertyDataTypeType
    alias: Optional[str] = None
    notification: Optional[PropertyNotification] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    path: Optional[List[AssetPropertyPathSegment]] = None
    externalId: Optional[str] = None


class BatchPutAssetPropertyError(BaseValidatorModel):
    errorCode: BatchPutAssetPropertyValueErrorCodeType
    errorMessage: str
    timestamps: List[TimeInNanos]


class BatchAssociateProjectAssetsResponse(BaseValidatorModel):
    errors: List[AssetErrorDetails]
    ResponseMetadata: ResponseMetadata


class BatchDisassociateProjectAssetsResponse(BaseValidatorModel):
    errors: List[AssetErrorDetails]
    ResponseMetadata: ResponseMetadata


class CreateAccessPolicyResponse(BaseValidatorModel):
    accessPolicyId: str
    accessPolicyArn: str
    ResponseMetadata: ResponseMetadata


class CreateBulkImportJobResponse(BaseValidatorModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class CreateDashboardResponse(BaseValidatorModel):
    dashboardId: str
    dashboardArn: str
    ResponseMetadata: ResponseMetadata


class CreateGatewayResponse(BaseValidatorModel):
    gatewayId: str
    gatewayArn: str
    ResponseMetadata: ResponseMetadata


class CreateProjectResponse(BaseValidatorModel):
    projectId: str
    projectArn: str
    ResponseMetadata: ResponseMetadata


class DescribeActionResponse(BaseValidatorModel):
    actionId: str
    targetResource: TargetResource
    actionDefinitionId: str
    actionPayload: ActionPayload
    executionTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeDashboardResponse(BaseValidatorModel):
    dashboardId: str
    dashboardArn: str
    dashboardName: str
    projectId: str
    dashboardDescription: str
    dashboardDefinition: str
    dashboardCreationDate: datetime
    dashboardLastUpdateDate: datetime
    ResponseMetadata: ResponseMetadata


class DescribeGatewayCapabilityConfigurationResponse(BaseValidatorModel):
    gatewayId: str
    capabilityNamespace: str
    capabilityConfiguration: str
    capabilitySyncStatus: CapabilitySyncStatusType
    ResponseMetadata: ResponseMetadata


class DescribeProjectResponse(BaseValidatorModel):
    projectId: str
    projectArn: str
    projectName: str
    portalId: str
    projectDescription: str
    projectCreationDate: datetime
    projectLastUpdateDate: datetime
    ResponseMetadata: ResponseMetadata


class DescribeTimeSeriesResponse(BaseValidatorModel):
    assetId: str
    propertyId: str
    alias: str
    timeSeriesId: str
    dataType: PropertyDataTypeType
    dataTypeSpec: str
    timeSeriesCreationDate: datetime
    timeSeriesLastUpdateDate: datetime
    timeSeriesArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExecuteActionResponse(BaseValidatorModel):
    actionId: str
    ResponseMetadata: ResponseMetadata


class ListProjectAssetsResponse(BaseValidatorModel):
    assetIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateGatewayCapabilityConfigurationResponse(BaseValidatorModel):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatusType
    ResponseMetadata: ResponseMetadata


class BatchGetAssetPropertyAggregatesEntry(BaseValidatorModel):
    entryId: str
    aggregateTypes: List[AggregateTypeType]
    resolution: str
    startDate: Timestamp
    endDate: Timestamp
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    qualities: Optional[List[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None


class BatchGetAssetPropertyValueHistoryEntry(BaseValidatorModel):
    entryId: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[Timestamp] = None
    endDate: Optional[Timestamp] = None
    qualities: Optional[List[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None


class GetAssetPropertyAggregatesRequest(BaseValidatorModel):
    aggregateTypes: List[AggregateTypeType]
    resolution: str
    startDate: Timestamp
    endDate: Timestamp
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    qualities: Optional[List[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetAssetPropertyValueHistoryRequest(BaseValidatorModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[Timestamp] = None
    endDate: Optional[Timestamp] = None
    qualities: Optional[List[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class BatchGetAssetPropertyAggregatesSkippedEntry(BaseValidatorModel):
    entryId: str
    completionStatus: BatchEntryCompletionStatusType
    errorInfo: Optional[BatchGetAssetPropertyAggregatesErrorInfo] = None


class BatchGetAssetPropertyValueRequest(BaseValidatorModel):
    entries: List[BatchGetAssetPropertyValueEntry]
    nextToken: Optional[str] = None


class BatchGetAssetPropertyValueSkippedEntry(BaseValidatorModel):
    entryId: str
    completionStatus: BatchEntryCompletionStatusType
    errorInfo: Optional[BatchGetAssetPropertyValueErrorInfo] = None


class BatchGetAssetPropertyValueHistorySkippedEntry(BaseValidatorModel):
    entryId: str
    completionStatus: BatchEntryCompletionStatusType
    errorInfo: Optional[BatchGetAssetPropertyValueHistoryErrorInfo] = None


class ImageFile(BaseValidatorModel):
    data: Blob
    type: Literal['PNG']


class ColumnInfo(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[ColumnType] = None


class CompositionDetails(BaseValidatorModel):
    compositionRelationship: Optional[List[CompositionRelationshipItem]] = None


class ListCompositionRelationshipsResponse(BaseValidatorModel):
    compositionRelationshipSummaries: List[CompositionRelationshipSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConfigurationStatus(BaseValidatorModel):
    state: ConfigurationStateType
    error: Optional[ConfigurationErrorDetails] = None


class FileFormatOutput(BaseValidatorModel):
    csv: Optional[CsvOutput] = None
    parquet: Optional[Dict[str, Any]] = None


class FileFormat(BaseValidatorModel):
    csv: Optional[Csv] = None
    parquet: Optional[Dict[str, Any]] = None


class MultiLayerStorage(BaseValidatorModel):
    customerManagedS3Storage: CustomerManagedS3Storage


class ListDashboardsResponse(BaseValidatorModel):
    dashboardSummaries: List[DashboardSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RowPaginator(BaseValidatorModel):
    data: List[DatumPaginator]


class Row(BaseValidatorModel):
    data: List[Datum]


class RowWaiter(BaseValidatorModel):
    data: List[DatumWaiter]


class DescribeAssetModelRequestWaitExtra(BaseValidatorModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    assetModelVersion: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeAssetModelRequestWait(BaseValidatorModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    assetModelVersion: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeAssetRequestWaitExtra(BaseValidatorModel):
    assetId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeAssetRequestWait(BaseValidatorModel):
    assetId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribePortalRequestWaitExtra(BaseValidatorModel):
    portalId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribePortalRequestWait(BaseValidatorModel):
    portalId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeLoggingOptionsResponse(BaseValidatorModel):
    loggingOptions: LoggingOptions
    ResponseMetadata: ResponseMetadata


class PutLoggingOptionsRequest(BaseValidatorModel):
    loggingOptions: LoggingOptions


class ErrorDetails(BaseValidatorModel):
    code: ErrorCodeType
    message: str
    details: Optional[List[DetailedError]] = None


class ExecuteQueryRequestPaginate(BaseValidatorModel):
    queryStatement: str
    clientToken: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAssetPropertyAggregatesRequestPaginate(BaseValidatorModel):
    aggregateTypes: List[AggregateTypeType]
    resolution: str
    startDate: Timestamp
    endDate: Timestamp
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    qualities: Optional[List[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAssetPropertyValueHistoryRequestPaginate(BaseValidatorModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[Timestamp] = None
    endDate: Optional[Timestamp] = None
    qualities: Optional[List[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetInterpolatedAssetPropertyValuesRequestPaginate(BaseValidatorModel):
    startTimeInSeconds: int
    endTimeInSeconds: int
    quality: QualityType
    intervalInSeconds: int
    type: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startTimeOffsetInNanos: Optional[int] = None
    endTimeOffsetInNanos: Optional[int] = None
    intervalWindowInSeconds: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccessPoliciesRequestPaginate(BaseValidatorModel):
    identityType: Optional[IdentityTypeType] = None
    identityId: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    iamArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListActionsRequestPaginate(BaseValidatorModel):
    targetResourceType: Literal['ASSET']
    targetResourceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetModelCompositeModelsRequestPaginate(BaseValidatorModel):
    assetModelId: str
    assetModelVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetModelPropertiesRequestPaginate(BaseValidatorModel):
    assetModelId: str
    filter: Optional[ListAssetModelPropertiesFilterType] = None
    assetModelVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetModelsRequestPaginate(BaseValidatorModel):
    assetModelTypes: Optional[List[AssetModelTypeType]] = None
    assetModelVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetPropertiesRequestPaginate(BaseValidatorModel):
    assetId: str
    filter: Optional[ListAssetPropertiesFilterType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetRelationshipsRequestPaginate(BaseValidatorModel):
    assetId: str
    traversalType: Literal['PATH_TO_ROOT']
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetsRequestPaginate(BaseValidatorModel):
    assetModelId: Optional[str] = None
    filter: Optional[ListAssetsFilterType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociatedAssetsRequestPaginate(BaseValidatorModel):
    assetId: str
    hierarchyId: Optional[str] = None
    traversalDirection: Optional[TraversalDirectionType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBulkImportJobsRequestPaginate(BaseValidatorModel):
    filter: Optional[ListBulkImportJobsFilterType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCompositionRelationshipsRequestPaginate(BaseValidatorModel):
    assetModelId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDashboardsRequestPaginate(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetsRequestPaginate(BaseValidatorModel):
    sourceType: Literal['KENDRA']
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGatewaysRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPortalsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectAssetsRequestPaginate(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsRequestPaginate(BaseValidatorModel):
    portalId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTimeSeriesRequestPaginate(BaseValidatorModel):
    assetId: Optional[str] = None
    aliasPrefix: Optional[str] = None
    timeSeriesType: Optional[ListTimeSeriesTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class MeasurementProcessingConfig(BaseValidatorModel):
    forwardingConfig: ForwardingConfig


class TransformProcessingConfig(BaseValidatorModel):
    computeLocation: ComputeLocationType
    forwardingConfig: Optional[ForwardingConfig] = None


class GatewayPlatform(BaseValidatorModel):
    greengrass: Optional[Greengrass] = None
    greengrassV2: Optional[GreengrassV2] = None
    siemensIE: Optional[SiemensIE] = None


class Identity(BaseValidatorModel):
    user: Optional[UserIdentity] = None
    group: Optional[GroupIdentity] = None
    iamUser: Optional[IAMUserIdentity] = None
    iamRole: Optional[IAMRoleIdentity] = None


class ListBulkImportJobsResponse(BaseValidatorModel):
    jobSummaries: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SourceDetail(BaseValidatorModel):
    kendra: Optional[KendraSourceDetail] = None


class ListProjectsResponse(BaseValidatorModel):
    projectSummaries: List[ProjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTimeSeriesResponse(BaseValidatorModel):
    TimeSeriesSummaries: List[TimeSeriesSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Source(BaseValidatorModel):
    arn: Optional[str] = None
    location: Optional[Location] = None


class MetricWindow(BaseValidatorModel):
    tumbling: Optional[TumblingWindow] = None


class PortalStatus(BaseValidatorModel):
    state: PortalStateType
    error: Optional[MonitorErrorDetails] = None

PortalTypeEntryUnion = Union[PortalTypeEntry, PortalTypeEntryOutput]


class Resource(BaseValidatorModel):
    portal: Optional[PortalResource] = None
    project: Optional[ProjectResource] = None


class Variant(BaseValidatorModel):
    stringValue: Optional[str] = None
    integerValue: Optional[int] = None
    doubleValue: Optional[float] = None
    booleanValue: Optional[bool] = None
    nullValue: Optional[PropertyValueNullValue] = None


class ListActionsResponse(BaseValidatorModel):
    actionSummaries: List[ActionSummary]
    nextToken: str
    ResponseMetadata: ResponseMetadata


class BatchGetAssetPropertyAggregatesSuccessEntry(BaseValidatorModel):
    entryId: str
    aggregatedValues: List[AggregatedValue]


class GetAssetPropertyAggregatesResponse(BaseValidatorModel):
    aggregatedValues: List[AggregatedValue]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssetRelationshipsResponse(BaseValidatorModel):
    assetRelationshipSummaries: List[AssetRelationshipSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssetModelCompositeModelsResponse(BaseValidatorModel):
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ExpressionVariableOutput(BaseValidatorModel):
    name: str
    value: VariableValueOutput

VariableValueUnion = Union[VariableValue, VariableValueOutput]


class ListAssetPropertiesResponse(BaseValidatorModel):
    assetPropertySummaries: List[AssetPropertySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssetCompositeModel(BaseValidatorModel):
    name: str
    type: str
    properties: List[AssetProperty]
    description: Optional[str] = None
    id: Optional[str] = None
    externalId: Optional[str] = None


class DescribeAssetCompositeModelResponse(BaseValidatorModel):
    assetId: str
    assetCompositeModelId: str
    assetCompositeModelExternalId: str
    assetCompositeModelPath: List[AssetCompositeModelPathSegment]
    assetCompositeModelName: str
    assetCompositeModelDescription: str
    assetCompositeModelType: str
    assetCompositeModelProperties: List[AssetProperty]
    assetCompositeModelSummaries: List[AssetCompositeModelSummary]
    actionDefinitions: List[ActionDefinition]
    ResponseMetadata: ResponseMetadata


class BatchPutAssetPropertyErrorEntry(BaseValidatorModel):
    entryId: str
    errors: List[BatchPutAssetPropertyError]


class BatchGetAssetPropertyAggregatesRequest(BaseValidatorModel):
    entries: List[BatchGetAssetPropertyAggregatesEntry]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class BatchGetAssetPropertyValueHistoryRequest(BaseValidatorModel):
    entries: List[BatchGetAssetPropertyValueHistoryEntry]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class Image(BaseValidatorModel):
    id: Optional[str] = None
    file: Optional[ImageFile] = None


class DescribeDefaultEncryptionConfigurationResponse(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    configurationStatus: ConfigurationStatus
    ResponseMetadata: ResponseMetadata


class PutDefaultEncryptionConfigurationResponse(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    configurationStatus: ConfigurationStatus
    ResponseMetadata: ResponseMetadata


class JobConfigurationOutput(BaseValidatorModel):
    fileFormat: FileFormatOutput


class JobConfiguration(BaseValidatorModel):
    fileFormat: FileFormat


class DescribeStorageConfigurationResponse(BaseValidatorModel):
    storageType: StorageTypeType
    multiLayerStorage: MultiLayerStorage
    disassociatedDataStorage: DisassociatedDataStorageStateType
    retentionPeriod: RetentionPeriod
    configurationStatus: ConfigurationStatus
    lastUpdateDate: datetime
    warmTier: WarmTierStateType
    warmTierRetentionPeriod: WarmTierRetentionPeriod
    disallowIngestNullNaN: bool
    ResponseMetadata: ResponseMetadata


class PutStorageConfigurationRequest(BaseValidatorModel):
    storageType: StorageTypeType
    multiLayerStorage: Optional[MultiLayerStorage] = None
    disassociatedDataStorage: Optional[DisassociatedDataStorageStateType] = None
    retentionPeriod: Optional[RetentionPeriod] = None
    warmTier: Optional[WarmTierStateType] = None
    warmTierRetentionPeriod: Optional[WarmTierRetentionPeriod] = None
    disallowIngestNullNaN: Optional[bool] = None


class PutStorageConfigurationResponse(BaseValidatorModel):
    storageType: StorageTypeType
    multiLayerStorage: MultiLayerStorage
    disassociatedDataStorage: DisassociatedDataStorageStateType
    retentionPeriod: RetentionPeriod
    configurationStatus: ConfigurationStatus
    warmTier: WarmTierStateType
    warmTierRetentionPeriod: WarmTierRetentionPeriod
    disallowIngestNullNaN: bool
    ResponseMetadata: ResponseMetadata


class ExecuteQueryResponsePaginator(BaseValidatorModel):
    columns: List[ColumnInfo]
    rows: List[RowPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ExecuteQueryResponse(BaseValidatorModel):
    columns: List[ColumnInfo]
    rows: List[Row]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ExecuteQueryResponseWaiter(BaseValidatorModel):
    columns: List[ColumnInfo]
    rows: List[RowWaiter]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssetModelStatus(BaseValidatorModel):
    state: AssetModelStateType
    error: Optional[ErrorDetails] = None


class AssetStatus(BaseValidatorModel):
    state: AssetStateType
    error: Optional[ErrorDetails] = None


class DatasetStatus(BaseValidatorModel):
    state: DatasetStateType
    error: Optional[ErrorDetails] = None


class Measurement(BaseValidatorModel):
    processingConfig: Optional[MeasurementProcessingConfig] = None


class CreateGatewayRequest(BaseValidatorModel):
    gatewayName: str
    gatewayPlatform: GatewayPlatform
    gatewayVersion: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DescribeGatewayResponse(BaseValidatorModel):
    gatewayId: str
    gatewayName: str
    gatewayArn: str
    gatewayPlatform: GatewayPlatform
    gatewayVersion: str
    gatewayCapabilitySummaries: List[GatewayCapabilitySummary]
    creationDate: datetime
    lastUpdateDate: datetime
    ResponseMetadata: ResponseMetadata


class GatewaySummary(BaseValidatorModel):
    gatewayId: str
    gatewayName: str
    creationDate: datetime
    lastUpdateDate: datetime
    gatewayPlatform: Optional[GatewayPlatform] = None
    gatewayVersion: Optional[str] = None
    gatewayCapabilitySummaries: Optional[List[GatewayCapabilitySummary]] = None


class DatasetSource(BaseValidatorModel):
    sourceType: Literal['KENDRA']
    sourceFormat: Literal['KNOWLEDGE_BASE']
    sourceDetail: Optional[SourceDetail] = None


class DataSetReference(BaseValidatorModel):
    datasetArn: Optional[str] = None
    source: Optional[Source] = None


class CreatePortalResponse(BaseValidatorModel):
    portalId: str
    portalArn: str
    portalStartUrl: str
    portalStatus: PortalStatus
    ssoApplicationId: str
    ResponseMetadata: ResponseMetadata


class DeletePortalResponse(BaseValidatorModel):
    portalStatus: PortalStatus
    ResponseMetadata: ResponseMetadata


class DescribePortalResponse(BaseValidatorModel):
    portalId: str
    portalArn: str
    portalName: str
    portalDescription: str
    portalClientId: str
    portalStartUrl: str
    portalContactEmail: str
    portalStatus: PortalStatus
    portalCreationDate: datetime
    portalLastUpdateDate: datetime
    portalLogoImageLocation: ImageLocation
    roleArn: str
    portalAuthMode: AuthModeType
    notificationSenderEmail: str
    alarms: Alarms
    portalType: PortalTypeType
    portalTypeConfiguration: Dict[str, PortalTypeEntryOutput]
    ResponseMetadata: ResponseMetadata


class PortalSummary(BaseValidatorModel):
    id: str
    name: str
    startUrl: str
    status: PortalStatus
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None
    roleArn: Optional[str] = None
    portalType: Optional[PortalTypeType] = None


class UpdatePortalResponse(BaseValidatorModel):
    portalStatus: PortalStatus
    ResponseMetadata: ResponseMetadata


class CreatePortalRequest(BaseValidatorModel):
    portalName: str
    portalContactEmail: str
    roleArn: str
    portalDescription: Optional[str] = None
    clientToken: Optional[str] = None
    portalLogoImageFile: Optional[ImageFile] = None
    tags: Optional[Dict[str, str]] = None
    portalAuthMode: Optional[AuthModeType] = None
    notificationSenderEmail: Optional[str] = None
    alarms: Optional[Alarms] = None
    portalType: Optional[PortalTypeType] = None
    portalTypeConfiguration: Optional[Dict[str, PortalTypeEntryUnion]] = None


class AccessPolicySummary(BaseValidatorModel):
    id: str
    identity: Identity
    resource: Resource
    permission: PermissionType
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None


class CreateAccessPolicyRequest(BaseValidatorModel):
    accessPolicyIdentity: Identity
    accessPolicyResource: Resource
    accessPolicyPermission: PermissionType
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DescribeAccessPolicyResponse(BaseValidatorModel):
    accessPolicyId: str
    accessPolicyArn: str
    accessPolicyIdentity: Identity
    accessPolicyResource: Resource
    accessPolicyPermission: PermissionType
    accessPolicyCreationDate: datetime
    accessPolicyLastUpdateDate: datetime
    ResponseMetadata: ResponseMetadata


class UpdateAccessPolicyRequest(BaseValidatorModel):
    accessPolicyId: str
    accessPolicyIdentity: Identity
    accessPolicyResource: Resource
    accessPolicyPermission: PermissionType
    clientToken: Optional[str] = None


class AssetPropertyValue(BaseValidatorModel):
    value: Variant
    timestamp: TimeInNanos
    quality: Optional[QualityType] = None


class InterpolatedAssetPropertyValue(BaseValidatorModel):
    timestamp: TimeInNanos
    value: Variant


class BatchGetAssetPropertyAggregatesResponse(BaseValidatorModel):
    errorEntries: List[BatchGetAssetPropertyAggregatesErrorEntry]
    successEntries: List[BatchGetAssetPropertyAggregatesSuccessEntry]
    skippedEntries: List[BatchGetAssetPropertyAggregatesSkippedEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MetricOutput(BaseValidatorModel):
    expression: str
    variables: List[ExpressionVariableOutput]
    window: MetricWindow
    processingConfig: Optional[MetricProcessingConfig] = None


class TransformOutput(BaseValidatorModel):
    expression: str
    variables: List[ExpressionVariableOutput]
    processingConfig: Optional[TransformProcessingConfig] = None


class ExpressionVariable(BaseValidatorModel):
    name: str
    value: VariableValueUnion


class BatchPutAssetPropertyValueResponse(BaseValidatorModel):
    errorEntries: List[BatchPutAssetPropertyErrorEntry]
    ResponseMetadata: ResponseMetadata


class UpdatePortalRequest(BaseValidatorModel):
    portalId: str
    portalName: str
    portalContactEmail: str
    roleArn: str
    portalDescription: Optional[str] = None
    portalLogoImage: Optional[Image] = None
    clientToken: Optional[str] = None
    notificationSenderEmail: Optional[str] = None
    alarms: Optional[Alarms] = None
    portalType: Optional[PortalTypeType] = None
    portalTypeConfiguration: Optional[Dict[str, PortalTypeEntryUnion]] = None


class DescribeBulkImportJobResponse(BaseValidatorModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    jobRoleArn: str
    files: List[File]
    errorReportLocation: ErrorReportLocation
    jobConfiguration: JobConfigurationOutput
    jobCreationDate: datetime
    jobLastUpdateDate: datetime
    adaptiveIngestion: bool
    deleteFilesAfterImport: bool
    ResponseMetadata: ResponseMetadata

JobConfigurationUnion = Union[JobConfiguration, JobConfigurationOutput]


class AssetModelSummary(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    creationDate: datetime
    lastUpdateDate: datetime
    status: AssetModelStatus
    externalId: Optional[str] = None
    assetModelType: Optional[AssetModelTypeType] = None
    version: Optional[str] = None


class CreateAssetModelCompositeModelResponse(BaseValidatorModel):
    assetModelCompositeModelId: str
    assetModelCompositeModelPath: List[AssetModelCompositeModelPathSegment]
    assetModelStatus: AssetModelStatus
    ResponseMetadata: ResponseMetadata


class CreateAssetModelResponse(BaseValidatorModel):
    assetModelId: str
    assetModelArn: str
    assetModelStatus: AssetModelStatus
    ResponseMetadata: ResponseMetadata


class DeleteAssetModelCompositeModelResponse(BaseValidatorModel):
    assetModelStatus: AssetModelStatus
    ResponseMetadata: ResponseMetadata


class DeleteAssetModelResponse(BaseValidatorModel):
    assetModelStatus: AssetModelStatus
    ResponseMetadata: ResponseMetadata


class UpdateAssetModelCompositeModelResponse(BaseValidatorModel):
    assetModelCompositeModelPath: List[AssetModelCompositeModelPathSegment]
    assetModelStatus: AssetModelStatus
    ResponseMetadata: ResponseMetadata


class UpdateAssetModelResponse(BaseValidatorModel):
    assetModelStatus: AssetModelStatus
    ResponseMetadata: ResponseMetadata


class AssetSummary(BaseValidatorModel):
    id: str
    arn: str
    name: str
    assetModelId: str
    creationDate: datetime
    lastUpdateDate: datetime
    status: AssetStatus
    hierarchies: List[AssetHierarchy]
    description: Optional[str] = None
    externalId: Optional[str] = None


class AssociatedAssetsSummary(BaseValidatorModel):
    id: str
    arn: str
    name: str
    assetModelId: str
    creationDate: datetime
    lastUpdateDate: datetime
    status: AssetStatus
    hierarchies: List[AssetHierarchy]
    description: Optional[str] = None
    externalId: Optional[str] = None


class CreateAssetResponse(BaseValidatorModel):
    assetId: str
    assetArn: str
    assetStatus: AssetStatus
    ResponseMetadata: ResponseMetadata


class DeleteAssetResponse(BaseValidatorModel):
    assetStatus: AssetStatus
    ResponseMetadata: ResponseMetadata


class DescribeAssetResponse(BaseValidatorModel):
    assetId: str
    assetArn: str
    assetName: str
    assetModelId: str
    assetProperties: List[AssetProperty]
    assetHierarchies: List[AssetHierarchy]
    assetCompositeModels: List[AssetCompositeModel]
    assetCreationDate: datetime
    assetLastUpdateDate: datetime
    assetStatus: AssetStatus
    assetDescription: str
    assetCompositeModelSummaries: List[AssetCompositeModelSummary]
    assetExternalId: str
    ResponseMetadata: ResponseMetadata


class UpdateAssetResponse(BaseValidatorModel):
    assetStatus: AssetStatus
    ResponseMetadata: ResponseMetadata


class CreateDatasetResponse(BaseValidatorModel):
    datasetId: str
    datasetArn: str
    datasetStatus: DatasetStatus
    ResponseMetadata: ResponseMetadata


class DatasetSummary(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    creationDate: datetime
    lastUpdateDate: datetime
    status: DatasetStatus


class DeleteDatasetResponse(BaseValidatorModel):
    datasetStatus: DatasetStatus
    ResponseMetadata: ResponseMetadata


class UpdateDatasetResponse(BaseValidatorModel):
    datasetId: str
    datasetArn: str
    datasetStatus: DatasetStatus
    ResponseMetadata: ResponseMetadata


class ListGatewaysResponse(BaseValidatorModel):
    gatewaySummaries: List[GatewaySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateDatasetRequest(BaseValidatorModel):
    datasetName: str
    datasetSource: DatasetSource
    datasetId: Optional[str] = None
    datasetDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DescribeDatasetResponse(BaseValidatorModel):
    datasetId: str
    datasetArn: str
    datasetName: str
    datasetDescription: str
    datasetSource: DatasetSource
    datasetStatus: DatasetStatus
    datasetCreationDate: datetime
    datasetLastUpdateDate: datetime
    datasetVersion: str
    ResponseMetadata: ResponseMetadata


class UpdateDatasetRequest(BaseValidatorModel):
    datasetId: str
    datasetName: str
    datasetSource: DatasetSource
    datasetDescription: Optional[str] = None
    clientToken: Optional[str] = None


class Reference(BaseValidatorModel):
    dataset: Optional[DataSetReference] = None


class ListPortalsResponse(BaseValidatorModel):
    portalSummaries: List[PortalSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAccessPoliciesResponse(BaseValidatorModel):
    accessPolicySummaries: List[AccessPolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchGetAssetPropertyValueHistorySuccessEntry(BaseValidatorModel):
    entryId: str
    assetPropertyValueHistory: List[AssetPropertyValue]


class BatchGetAssetPropertyValueSuccessEntry(BaseValidatorModel):
    entryId: str
    assetPropertyValue: Optional[AssetPropertyValue] = None


class GetAssetPropertyValueHistoryResponse(BaseValidatorModel):
    assetPropertyValueHistory: List[AssetPropertyValue]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetAssetPropertyValueResponse(BaseValidatorModel):
    propertyValue: AssetPropertyValue
    ResponseMetadata: ResponseMetadata


class PutAssetPropertyValueEntry(BaseValidatorModel):
    entryId: str
    propertyValues: List[AssetPropertyValue]
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


class GetInterpolatedAssetPropertyValuesResponse(BaseValidatorModel):
    interpolatedAssetPropertyValues: List[InterpolatedAssetPropertyValue]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PropertyTypeOutput(BaseValidatorModel):
    attribute: Optional[Attribute] = None
    measurement: Optional[Measurement] = None
    transform: Optional[TransformOutput] = None
    metric: Optional[MetricOutput] = None

ExpressionVariableUnion = Union[ExpressionVariable, ExpressionVariableOutput]


class CreateBulkImportJobRequest(BaseValidatorModel):
    jobName: str
    jobRoleArn: str
    files: List[File]
    errorReportLocation: ErrorReportLocation
    jobConfiguration: JobConfigurationUnion
    adaptiveIngestion: Optional[bool] = None
    deleteFilesAfterImport: Optional[bool] = None


class ListAssetModelsResponse(BaseValidatorModel):
    assetModelSummaries: List[AssetModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssetsResponse(BaseValidatorModel):
    assetSummaries: List[AssetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssociatedAssetsResponse(BaseValidatorModel):
    assetSummaries: List[AssociatedAssetsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDatasetsResponse(BaseValidatorModel):
    datasetSummaries: List[DatasetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Citation(BaseValidatorModel):
    reference: Optional[Reference] = None
    content: Optional[Content] = None


class BatchGetAssetPropertyValueHistoryResponse(BaseValidatorModel):
    errorEntries: List[BatchGetAssetPropertyValueHistoryErrorEntry]
    successEntries: List[BatchGetAssetPropertyValueHistorySuccessEntry]
    skippedEntries: List[BatchGetAssetPropertyValueHistorySkippedEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchGetAssetPropertyValueResponse(BaseValidatorModel):
    errorEntries: List[BatchGetAssetPropertyValueErrorEntry]
    successEntries: List[BatchGetAssetPropertyValueSuccessEntry]
    skippedEntries: List[BatchGetAssetPropertyValueSkippedEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchPutAssetPropertyValueRequest(BaseValidatorModel):
    entries: List[PutAssetPropertyValueEntry]
    enablePartialEntryProcessing: Optional[bool] = None


class AssetModelPropertyOutput(BaseValidatorModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeOutput
    id: Optional[str] = None
    externalId: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    path: Optional[List[AssetModelPropertyPathSegment]] = None


class AssetModelPropertySummary(BaseValidatorModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeOutput
    id: Optional[str] = None
    externalId: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    assetModelCompositeModelId: Optional[str] = None
    path: Optional[List[AssetModelPropertyPathSegment]] = None


class Property(BaseValidatorModel):
    id: str
    name: str
    dataType: PropertyDataTypeType
    alias: Optional[str] = None
    notification: Optional[PropertyNotification] = None
    unit: Optional[str] = None
    type: Optional[PropertyTypeOutput] = None
    path: Optional[List[AssetPropertyPathSegment]] = None
    externalId: Optional[str] = None


class Metric(BaseValidatorModel):
    expression: str
    variables: List[ExpressionVariableUnion]
    window: MetricWindow
    processingConfig: Optional[MetricProcessingConfig] = None


class Transform(BaseValidatorModel):
    expression: str
    variables: List[ExpressionVariableUnion]
    processingConfig: Optional[TransformProcessingConfig] = None


class InvocationOutput(BaseValidatorModel):
    message: Optional[str] = None
    citations: Optional[List[Citation]] = None


class AssetModelCompositeModelOutput(BaseValidatorModel):
    name: str
    type: str
    description: Optional[str] = None
    properties: Optional[List[AssetModelPropertyOutput]] = None
    id: Optional[str] = None
    externalId: Optional[str] = None


class DescribeAssetModelCompositeModelResponse(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelExternalId: str
    assetModelCompositeModelPath: List[AssetModelCompositeModelPathSegment]
    assetModelCompositeModelName: str
    assetModelCompositeModelDescription: str
    assetModelCompositeModelType: str
    assetModelCompositeModelProperties: List[AssetModelPropertyOutput]
    compositionDetails: CompositionDetails
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummary]
    actionDefinitions: List[ActionDefinition]
    ResponseMetadata: ResponseMetadata


class ListAssetModelPropertiesResponse(BaseValidatorModel):
    assetModelPropertySummaries: List[AssetModelPropertySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CompositeModelProperty(BaseValidatorModel):
    name: str
    type: str
    assetProperty: Property
    id: Optional[str] = None
    externalId: Optional[str] = None

MetricUnion = Union[Metric, MetricOutput]

TransformUnion = Union[Transform, TransformOutput]


class ResponseStream(BaseValidatorModel):
    trace: Optional[Trace] = None
    output: Optional[InvocationOutput] = None
    accessDeniedException: Optional[AccessDeniedException] = None
    conflictingOperationException: Optional[ConflictingOperationException] = None
    internalFailureException: Optional[InternalFailureException] = None
    invalidRequestException: Optional[InvalidRequestException] = None
    limitExceededException: Optional[LimitExceededException] = None
    resourceNotFoundException: Optional[ResourceNotFoundException] = None
    throttlingException: Optional[ThrottlingException] = None


class DescribeAssetModelResponse(BaseValidatorModel):
    assetModelId: str
    assetModelExternalId: str
    assetModelArn: str
    assetModelName: str
    assetModelType: AssetModelTypeType
    assetModelDescription: str
    assetModelProperties: List[AssetModelPropertyOutput]
    assetModelHierarchies: List[AssetModelHierarchy]
    assetModelCompositeModels: List[AssetModelCompositeModelOutput]
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummary]
    assetModelCreationDate: datetime
    assetModelLastUpdateDate: datetime
    assetModelStatus: AssetModelStatus
    assetModelVersion: str
    eTag: str
    ResponseMetadata: ResponseMetadata


class DescribeAssetPropertyResponse(BaseValidatorModel):
    assetId: str
    assetName: str
    assetModelId: str
    assetProperty: Property
    compositeModel: CompositeModelProperty
    assetExternalId: str
    ResponseMetadata: ResponseMetadata


class PropertyType(BaseValidatorModel):
    attribute: Optional[Attribute] = None
    measurement: Optional[Measurement] = None
    transform: Optional[TransformUnion] = None
    metric: Optional[MetricUnion] = None


class InvokeAssistantResponse(BaseValidatorModel):
    body: EventStream[ResponseStream]
    conversationId: str
    ResponseMetadata: ResponseMetadata

PropertyTypeUnion = Union[PropertyType, PropertyTypeOutput]


class AssetModelPropertyDefinition(BaseValidatorModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeUnion
    id: Optional[str] = None
    externalId: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None


class AssetModelProperty(BaseValidatorModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeUnion
    id: Optional[str] = None
    externalId: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    path: Optional[List[AssetModelPropertyPathSegment]] = None


class AssetModelCompositeModelDefinition(BaseValidatorModel):
    name: str
    type: str
    id: Optional[str] = None
    externalId: Optional[str] = None
    description: Optional[str] = None
    properties: Optional[List[AssetModelPropertyDefinition]] = None


class CreateAssetModelCompositeModelRequest(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelName: str
    assetModelCompositeModelType: str
    assetModelCompositeModelExternalId: Optional[str] = None
    parentAssetModelCompositeModelId: Optional[str] = None
    assetModelCompositeModelId: Optional[str] = None
    assetModelCompositeModelDescription: Optional[str] = None
    clientToken: Optional[str] = None
    composedAssetModelId: Optional[str] = None
    assetModelCompositeModelProperties: Optional[List[AssetModelPropertyDefinition]] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None

AssetModelPropertyUnion = Union[AssetModelProperty, AssetModelPropertyOutput]


class CreateAssetModelRequest(BaseValidatorModel):
    assetModelName: str
    assetModelType: Optional[AssetModelTypeType] = None
    assetModelId: Optional[str] = None
    assetModelExternalId: Optional[str] = None
    assetModelDescription: Optional[str] = None
    assetModelProperties: Optional[List[AssetModelPropertyDefinition]] = None
    assetModelHierarchies: Optional[List[AssetModelHierarchyDefinition]] = None
    assetModelCompositeModels: Optional[List[AssetModelCompositeModelDefinition]] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class AssetModelCompositeModel(BaseValidatorModel):
    name: str
    type: str
    description: Optional[str] = None
    properties: Optional[List[AssetModelPropertyUnion]] = None
    id: Optional[str] = None
    externalId: Optional[str] = None


class UpdateAssetModelCompositeModelRequest(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelName: str
    assetModelCompositeModelExternalId: Optional[str] = None
    assetModelCompositeModelDescription: Optional[str] = None
    clientToken: Optional[str] = None
    assetModelCompositeModelProperties: Optional[List[AssetModelPropertyUnion]] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None

AssetModelCompositeModelUnion = Union[AssetModelCompositeModel, AssetModelCompositeModelOutput]


class UpdateAssetModelRequest(BaseValidatorModel):
    assetModelId: str
    assetModelName: str
    assetModelExternalId: Optional[str] = None
    assetModelDescription: Optional[str] = None
    assetModelProperties: Optional[List[AssetModelPropertyUnion]] = None
    assetModelHierarchies: Optional[List[AssetModelHierarchy]] = None
    assetModelCompositeModels: Optional[List[AssetModelCompositeModelUnion]] = None
    clientToken: Optional[str] = None
    ifMatch: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    matchForVersionType: Optional[AssetModelVersionTypeType] = None
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
from aws_resource_validator.pydantic_models.iotsitewise_constants import *

class ActionDefinitionTypeDef(BaseModel):
    actionDefinitionId: str
    actionName: str
    actionType: str

class ActionPayloadTypeDef(BaseModel):
    stringValue: str

class TargetResourceTypeDef(BaseModel):
    assetId: str

class AggregatesTypeDef(BaseModel):
    average: Optional[float] = None
    count: Optional[float] = None
    maximum: Optional[float] = None
    minimum: Optional[float] = None
    sum: Optional[float] = None
    standardDeviation: Optional[float] = None

class AlarmsTypeDef(BaseModel):
    alarmRoleArn: str
    notificationLambdaArn: Optional[str] = None

class AssetCompositeModelPathSegmentTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class AssetErrorDetailsTypeDef(BaseModel):
    assetId: str
    code: Literal["INTERNAL_FAILURE"]
    message: str

class AssetHierarchyInfoTypeDef(BaseModel):
    parentAssetId: Optional[str] = None
    childAssetId: Optional[str] = None

class AssetHierarchyTypeDef(BaseModel):
    name: str
    id: Optional[str] = None
    externalId: Optional[str] = None

class AssetModelCompositeModelPathSegmentTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class AssetModelHierarchyDefinitionTypeDef(BaseModel):
    name: str
    childAssetModelId: str
    id: Optional[str] = None
    externalId: Optional[str] = None

class AssetModelHierarchyTypeDef(BaseModel):
    name: str
    childAssetModelId: str
    id: Optional[str] = None
    externalId: Optional[str] = None

class AssetModelPropertyPathSegmentTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class AssetPropertyPathSegmentTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class PropertyNotificationTypeDef(BaseModel):
    topic: str
    state: PropertyNotificationStateType

class TimeInNanosTypeDef(BaseModel):
    timeInSeconds: int
    offsetInNanos: Optional[int] = None

class VariantTypeDef(BaseModel):
    stringValue: Optional[str] = None
    integerValue: Optional[int] = None
    doubleValue: Optional[float] = None
    booleanValue: Optional[bool] = None

class AssociateAssetsRequestRequestTypeDef(BaseModel):
    assetId: str
    hierarchyId: str
    childAssetId: str
    clientToken: Optional[str] = None

class AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef(BaseModel):
    alias: str
    assetId: str
    propertyId: str
    clientToken: Optional[str] = None

class AttributeTypeDef(BaseModel):
    defaultValue: Optional[str] = None

class BatchAssociateProjectAssetsRequestRequestTypeDef(BaseModel):
    projectId: str
    assetIds: Sequence[str]
    clientToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDisassociateProjectAssetsRequestRequestTypeDef(BaseModel):
    projectId: str
    assetIds: Sequence[str]
    clientToken: Optional[str] = None

class BatchGetAssetPropertyAggregatesErrorEntryTypeDef(BaseModel):
    errorCode: BatchGetAssetPropertyAggregatesErrorCodeType
    errorMessage: str
    entryId: str

class BatchGetAssetPropertyAggregatesErrorInfoTypeDef(BaseModel):
    errorCode: BatchGetAssetPropertyAggregatesErrorCodeType
    errorTimestamp: datetime

class BatchGetAssetPropertyValueEntryTypeDef(BaseModel):
    entryId: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None

class BatchGetAssetPropertyValueErrorEntryTypeDef(BaseModel):
    errorCode: BatchGetAssetPropertyValueErrorCodeType
    errorMessage: str
    entryId: str

class BatchGetAssetPropertyValueErrorInfoTypeDef(BaseModel):
    errorCode: BatchGetAssetPropertyValueErrorCodeType
    errorTimestamp: datetime

class BatchGetAssetPropertyValueHistoryErrorEntryTypeDef(BaseModel):
    errorCode: BatchGetAssetPropertyValueHistoryErrorCodeType
    errorMessage: str
    entryId: str

class BatchGetAssetPropertyValueHistoryErrorInfoTypeDef(BaseModel):
    errorCode: BatchGetAssetPropertyValueHistoryErrorCodeType
    errorTimestamp: datetime

class ColumnTypeTypeDef(BaseModel):
    scalarType: Optional[ScalarTypeType] = None

class CompositionRelationshipItemTypeDef(BaseModel):
    id: Optional[str] = None

class CompositionRelationshipSummaryTypeDef(BaseModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelType: str

class ConfigurationErrorDetailsTypeDef(BaseModel):
    code: ErrorCodeType
    message: str

class CreateAssetRequestRequestTypeDef(BaseModel):
    assetName: str
    assetModelId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    assetDescription: Optional[str] = None
    assetId: Optional[str] = None
    assetExternalId: Optional[str] = None

class ErrorReportLocationTypeDef(BaseModel):
    bucket: str
    prefix: str

class FileTypeDef(BaseModel):
    bucket: str
    key: str
    versionId: Optional[str] = None

class CreateDashboardRequestRequestTypeDef(BaseModel):
    projectId: str
    dashboardName: str
    dashboardDefinition: str
    dashboardDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateProjectRequestRequestTypeDef(BaseModel):
    portalId: str
    projectName: str
    projectDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CsvTypeDef(BaseModel):
    columnNames: Sequence[ColumnNameType]

class CustomerManagedS3StorageTypeDef(BaseModel):
    s3ResourceArn: str
    roleArn: str

class DashboardSummaryTypeDef(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None

class RowTypeDef(BaseModel):
    data: List["DatumTypeDef"]

class DeleteAccessPolicyRequestRequestTypeDef(BaseModel):
    accessPolicyId: str
    clientToken: Optional[str] = None

class DeleteAssetModelCompositeModelRequestRequestTypeDef(BaseModel):
    assetModelId: str
    assetModelCompositeModelId: str
    clientToken: Optional[str] = None

class DeleteAssetModelRequestRequestTypeDef(BaseModel):
    assetModelId: str
    clientToken: Optional[str] = None

class DeleteAssetRequestRequestTypeDef(BaseModel):
    assetId: str
    clientToken: Optional[str] = None

class DeleteDashboardRequestRequestTypeDef(BaseModel):
    dashboardId: str
    clientToken: Optional[str] = None

class DeleteGatewayRequestRequestTypeDef(BaseModel):
    gatewayId: str

class DeletePortalRequestRequestTypeDef(BaseModel):
    portalId: str
    clientToken: Optional[str] = None

class DeleteProjectRequestRequestTypeDef(BaseModel):
    projectId: str
    clientToken: Optional[str] = None

class DeleteTimeSeriesRequestRequestTypeDef(BaseModel):
    alias: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    clientToken: Optional[str] = None

class DescribeAccessPolicyRequestRequestTypeDef(BaseModel):
    accessPolicyId: str

class DescribeActionRequestRequestTypeDef(BaseModel):
    actionId: str

class DescribeAssetCompositeModelRequestRequestTypeDef(BaseModel):
    assetId: str
    assetCompositeModelId: str

class DescribeAssetModelCompositeModelRequestRequestTypeDef(BaseModel):
    assetModelId: str
    assetModelCompositeModelId: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeAssetModelRequestRequestTypeDef(BaseModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None

class DescribeAssetPropertyRequestRequestTypeDef(BaseModel):
    assetId: str
    propertyId: str

class DescribeAssetRequestRequestTypeDef(BaseModel):
    assetId: str
    excludeProperties: Optional[bool] = None

class DescribeBulkImportJobRequestRequestTypeDef(BaseModel):
    jobId: str

class DescribeDashboardRequestRequestTypeDef(BaseModel):
    dashboardId: str

class DescribeGatewayCapabilityConfigurationRequestRequestTypeDef(BaseModel):
    gatewayId: str
    capabilityNamespace: str

class DescribeGatewayRequestRequestTypeDef(BaseModel):
    gatewayId: str

class GatewayCapabilitySummaryTypeDef(BaseModel):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatusType

class LoggingOptionsTypeDef(BaseModel):
    level: LoggingLevelType

class DescribePortalRequestRequestTypeDef(BaseModel):
    portalId: str

class ImageLocationTypeDef(BaseModel):
    id: str
    url: str

class DescribeProjectRequestRequestTypeDef(BaseModel):
    projectId: str

class RetentionPeriodTypeDef(BaseModel):
    numberOfDays: Optional[int] = None
    unlimited: Optional[bool] = None

class WarmTierRetentionPeriodTypeDef(BaseModel):
    numberOfDays: Optional[int] = None
    unlimited: Optional[bool] = None

class DescribeTimeSeriesRequestRequestTypeDef(BaseModel):
    alias: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None

class DetailedErrorTypeDef(BaseModel):
    code: DetailedErrorCodeType
    message: str

class DisassociateAssetsRequestRequestTypeDef(BaseModel):
    assetId: str
    hierarchyId: str
    childAssetId: str
    clientToken: Optional[str] = None

class DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef(BaseModel):
    alias: str
    assetId: str
    propertyId: str
    clientToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ExecuteQueryRequestRequestTypeDef(BaseModel):
    queryStatement: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ForwardingConfigTypeDef(BaseModel):
    state: ForwardingConfigStateType

class GreengrassTypeDef(BaseModel):
    groupArn: str

class GreengrassV2TypeDef(BaseModel):
    coreDeviceThingName: str

class GetAssetPropertyValueRequestRequestTypeDef(BaseModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None

class GetInterpolatedAssetPropertyValuesRequestRequestTypeDef(BaseModel):
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

class GroupIdentityTypeDef(BaseModel):
    id: str

class IAMRoleIdentityTypeDef(BaseModel):
    arn: str

class IAMUserIdentityTypeDef(BaseModel):
    arn: str

class UserIdentityTypeDef(BaseModel):
    id: str

class JobSummaryTypeDef(BaseModel):
    id: str
    name: str
    status: JobStatusType

class ListAccessPoliciesRequestRequestTypeDef(BaseModel):
    identityType: Optional[IdentityTypeType] = None
    identityId: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    iamArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListActionsRequestRequestTypeDef(BaseModel):
    targetResourceType: Literal["ASSET"]
    targetResourceId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssetModelCompositeModelsRequestRequestTypeDef(BaseModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssetModelPropertiesRequestRequestTypeDef(BaseModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListAssetModelPropertiesFilterType] = None

class ListAssetModelsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetModelTypes: Optional[Sequence[AssetModelTypeType]] = None

class ListAssetPropertiesRequestRequestTypeDef(BaseModel):
    assetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListAssetPropertiesFilterType] = None

class ListAssetRelationshipsRequestRequestTypeDef(BaseModel):
    assetId: str
    traversalType: Literal["PATH_TO_ROOT"]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssetsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetModelId: Optional[str] = None
    filter: Optional[ListAssetsFilterType] = None

class ListAssociatedAssetsRequestRequestTypeDef(BaseModel):
    assetId: str
    hierarchyId: Optional[str] = None
    traversalDirection: Optional[TraversalDirectionType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListBulkImportJobsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListBulkImportJobsFilterType] = None

class ListCompositionRelationshipsRequestRequestTypeDef(BaseModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDashboardsRequestRequestTypeDef(BaseModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListGatewaysRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPortalsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListProjectAssetsRequestRequestTypeDef(BaseModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListProjectsRequestRequestTypeDef(BaseModel):
    portalId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProjectSummaryTypeDef(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTimeSeriesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetId: Optional[str] = None
    aliasPrefix: Optional[str] = None
    timeSeriesType: Optional[ListTimeSeriesTypeType] = None

class TimeSeriesSummaryTypeDef(BaseModel):
    timeSeriesId: str
    dataType: PropertyDataTypeType
    timeSeriesCreationDate: datetime
    timeSeriesLastUpdateDate: datetime
    timeSeriesArn: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    alias: Optional[str] = None
    dataTypeSpec: Optional[str] = None

class MetricProcessingConfigTypeDef(BaseModel):
    computeLocation: ComputeLocationType

class TumblingWindowTypeDef(BaseModel):
    interval: str
    offset: Optional[str] = None

class MonitorErrorDetailsTypeDef(BaseModel):
    code: Optional[MonitorErrorCodeType] = None
    message: Optional[str] = None

class PortalResourceTypeDef(BaseModel):
    id: str

class ProjectResourceTypeDef(BaseModel):
    id: str

class PutDefaultEncryptionConfigurationRequestRequestTypeDef(BaseModel):
    encryptionType: EncryptionTypeType
    kmsKeyId: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAssetPropertyRequestRequestTypeDef(BaseModel):
    assetId: str
    propertyId: str
    propertyAlias: Optional[str] = None
    propertyNotificationState: Optional[PropertyNotificationStateType] = None
    clientToken: Optional[str] = None
    propertyUnit: Optional[str] = None

class UpdateAssetRequestRequestTypeDef(BaseModel):
    assetId: str
    assetName: str
    clientToken: Optional[str] = None
    assetDescription: Optional[str] = None
    assetExternalId: Optional[str] = None

class UpdateDashboardRequestRequestTypeDef(BaseModel):
    dashboardId: str
    dashboardName: str
    dashboardDefinition: str
    dashboardDescription: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateGatewayCapabilityConfigurationRequestRequestTypeDef(BaseModel):
    gatewayId: str
    capabilityNamespace: str
    capabilityConfiguration: str

class UpdateGatewayRequestRequestTypeDef(BaseModel):
    gatewayId: str
    gatewayName: str

class UpdateProjectRequestRequestTypeDef(BaseModel):
    projectId: str
    projectName: str
    projectDescription: Optional[str] = None
    clientToken: Optional[str] = None

class ActionSummaryTypeDef(BaseModel):
    actionId: Optional[str] = None
    actionDefinitionId: Optional[str] = None
    targetResource: Optional[TargetResourceTypeDef] = None

class ExecuteActionRequestRequestTypeDef(BaseModel):
    targetResource: TargetResourceTypeDef
    actionDefinitionId: str
    actionPayload: ActionPayloadTypeDef
    clientToken: Optional[str] = None

class AggregatedValueTypeDef(BaseModel):
    timestamp: datetime
    value: AggregatesTypeDef
    quality: Optional[QualityType] = None

class AssetCompositeModelSummaryTypeDef(BaseModel):
    id: str
    name: str
    type: str
    description: str
    path: List[AssetCompositeModelPathSegmentTypeDef]
    externalId: Optional[str] = None

class AssetRelationshipSummaryTypeDef(BaseModel):
    relationshipType: Literal["HIERARCHY"]
    hierarchyInfo: Optional[AssetHierarchyInfoTypeDef] = None

class AssetModelCompositeModelSummaryTypeDef(BaseModel):
    id: str
    name: str
    type: str
    externalId: Optional[str] = None
    description: Optional[str] = None
    path: Optional[List[AssetModelCompositeModelPathSegmentTypeDef]] = None

class VariableValuePaginatorTypeDef(BaseModel):
    propertyId: Optional[str] = None
    hierarchyId: Optional[str] = None
    propertyPath: Optional[List[AssetModelPropertyPathSegmentTypeDef]] = None

class VariableValueTypeDef(BaseModel):
    propertyId: Optional[str] = None
    hierarchyId: Optional[str] = None
    propertyPath: Optional[Sequence[AssetModelPropertyPathSegmentTypeDef]] = None

class AssetPropertySummaryTypeDef(BaseModel):
    id: str
    alias: Optional[str] = None
    unit: Optional[str] = None
    notification: Optional[PropertyNotificationTypeDef] = None
    assetCompositeModelId: Optional[str] = None
    path: Optional[List[AssetPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class AssetPropertyTypeDef(BaseModel):
    id: str
    name: str
    dataType: PropertyDataTypeType
    alias: Optional[str] = None
    notification: Optional[PropertyNotificationTypeDef] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    path: Optional[List[AssetPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class BatchPutAssetPropertyErrorTypeDef(BaseModel):
    errorCode: BatchPutAssetPropertyValueErrorCodeType
    errorMessage: str
    timestamps: List[TimeInNanosTypeDef]

class AssetPropertyValueTypeDef(BaseModel):
    value: VariantTypeDef
    timestamp: TimeInNanosTypeDef
    quality: Optional[QualityType] = None

class InterpolatedAssetPropertyValueTypeDef(BaseModel):
    timestamp: TimeInNanosTypeDef
    value: VariantTypeDef

class BatchAssociateProjectAssetsResponseTypeDef(BaseModel):
    errors: List[AssetErrorDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateProjectAssetsResponseTypeDef(BaseModel):
    errors: List[AssetErrorDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPolicyResponseTypeDef(BaseModel):
    accessPolicyId: str
    accessPolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBulkImportJobResponseTypeDef(BaseModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDashboardResponseTypeDef(BaseModel):
    dashboardId: str
    dashboardArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGatewayResponseTypeDef(BaseModel):
    gatewayId: str
    gatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResponseTypeDef(BaseModel):
    projectId: str
    projectArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActionResponseTypeDef(BaseModel):
    actionId: str
    targetResource: TargetResourceTypeDef
    actionDefinitionId: str
    actionPayload: ActionPayloadTypeDef
    executionTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDashboardResponseTypeDef(BaseModel):
    dashboardId: str
    dashboardArn: str
    dashboardName: str
    projectId: str
    dashboardDescription: str
    dashboardDefinition: str
    dashboardCreationDate: datetime
    dashboardLastUpdateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayCapabilityConfigurationResponseTypeDef(BaseModel):
    gatewayId: str
    capabilityNamespace: str
    capabilityConfiguration: str
    capabilitySyncStatus: CapabilitySyncStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProjectResponseTypeDef(BaseModel):
    projectId: str
    projectArn: str
    projectName: str
    portalId: str
    projectDescription: str
    projectCreationDate: datetime
    projectLastUpdateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTimeSeriesResponseTypeDef(BaseModel):
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

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteActionResponseTypeDef(BaseModel):
    actionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectAssetsResponseTypeDef(BaseModel):
    assetIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayCapabilityConfigurationResponseTypeDef(BaseModel):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAssetPropertyAggregatesEntryTypeDef(BaseModel):
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

class BatchGetAssetPropertyValueHistoryEntryTypeDef(BaseModel):
    entryId: str
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None

class GetAssetPropertyAggregatesRequestRequestTypeDef(BaseModel):
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

class GetAssetPropertyValueHistoryRequestRequestTypeDef(BaseModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class BatchGetAssetPropertyAggregatesSkippedEntryTypeDef(BaseModel):
    entryId: str
    completionStatus: BatchEntryCompletionStatusType
    errorInfo: Optional[BatchGetAssetPropertyAggregatesErrorInfoTypeDef] = None

class BatchGetAssetPropertyValueRequestRequestTypeDef(BaseModel):
    entries: Sequence[BatchGetAssetPropertyValueEntryTypeDef]
    nextToken: Optional[str] = None

class BatchGetAssetPropertyValueSkippedEntryTypeDef(BaseModel):
    entryId: str
    completionStatus: BatchEntryCompletionStatusType
    errorInfo: Optional[BatchGetAssetPropertyValueErrorInfoTypeDef] = None

class BatchGetAssetPropertyValueHistorySkippedEntryTypeDef(BaseModel):
    entryId: str
    completionStatus: BatchEntryCompletionStatusType
    errorInfo: Optional[BatchGetAssetPropertyValueHistoryErrorInfoTypeDef] = None

class ImageFileTypeDef(BaseModel):
    data: BlobTypeDef
    type: Literal["PNG"]

class ColumnInfoTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[ColumnTypeTypeDef] = None

class CompositionDetailsTypeDef(BaseModel):
    compositionRelationship: Optional[List[CompositionRelationshipItemTypeDef]] = None

class ListCompositionRelationshipsResponseTypeDef(BaseModel):
    compositionRelationshipSummaries: List[CompositionRelationshipSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationStatusTypeDef(BaseModel):
    state: ConfigurationStateType
    error: Optional[ConfigurationErrorDetailsTypeDef] = None

class FileFormatTypeDef(BaseModel):
    csv: Optional[CsvTypeDef] = None
    parquet: Optional[Mapping[str, Any]] = None

class MultiLayerStorageTypeDef(BaseModel):
    customerManagedS3Storage: CustomerManagedS3StorageTypeDef

class ListDashboardsResponseTypeDef(BaseModel):
    dashboardSummaries: List[DashboardSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatumTypeDef(BaseModel):
    scalarValue: Optional[str] = None
    arrayValue: Optional[List[Dict[str, Any]]] = None
    rowValue: Optional[Dict[str, Any]] = None
    nullValue: Optional[bool] = None

class DescribeAssetModelRequestAssetModelActiveWaitTypeDef(BaseModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAssetModelRequestAssetModelNotExistsWaitTypeDef(BaseModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAssetRequestAssetActiveWaitTypeDef(BaseModel):
    assetId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAssetRequestAssetNotExistsWaitTypeDef(BaseModel):
    assetId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribePortalRequestPortalActiveWaitTypeDef(BaseModel):
    portalId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribePortalRequestPortalNotExistsWaitTypeDef(BaseModel):
    portalId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeLoggingOptionsResponseTypeDef(BaseModel):
    loggingOptions: LoggingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestRequestTypeDef(BaseModel):
    loggingOptions: LoggingOptionsTypeDef

class ErrorDetailsTypeDef(BaseModel):
    code: ErrorCodeType
    message: str
    details: Optional[List[DetailedErrorTypeDef]] = None

class ExecuteQueryRequestExecuteQueryPaginateTypeDef(BaseModel):
    queryStatement: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAssetPropertyAggregatesRequestGetAssetPropertyAggregatesPaginateTypeDef(BaseModel):
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

class GetAssetPropertyValueHistoryRequestGetAssetPropertyValueHistoryPaginateTypeDef(BaseModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetInterpolatedAssetPropertyValuesRequestGetInterpolatedAssetPropertyValuesPaginateTypeDef(BaseModel):
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
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef(BaseModel):
    identityType: Optional[IdentityTypeType] = None
    identityId: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    iamArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListActionsRequestListActionsPaginateTypeDef(BaseModel):
    targetResourceType: Literal["ASSET"]
    targetResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetModelCompositeModelsRequestListAssetModelCompositeModelsPaginateTypeDef(BaseModel):
    assetModelId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetModelPropertiesRequestListAssetModelPropertiesPaginateTypeDef(BaseModel):
    assetModelId: str
    filter: Optional[ListAssetModelPropertiesFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetModelsRequestListAssetModelsPaginateTypeDef(BaseModel):
    assetModelTypes: Optional[Sequence[AssetModelTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetPropertiesRequestListAssetPropertiesPaginateTypeDef(BaseModel):
    assetId: str
    filter: Optional[ListAssetPropertiesFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetRelationshipsRequestListAssetRelationshipsPaginateTypeDef(BaseModel):
    assetId: str
    traversalType: Literal["PATH_TO_ROOT"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetsRequestListAssetsPaginateTypeDef(BaseModel):
    assetModelId: Optional[str] = None
    filter: Optional[ListAssetsFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedAssetsRequestListAssociatedAssetsPaginateTypeDef(BaseModel):
    assetId: str
    hierarchyId: Optional[str] = None
    traversalDirection: Optional[TraversalDirectionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBulkImportJobsRequestListBulkImportJobsPaginateTypeDef(BaseModel):
    filter: Optional[ListBulkImportJobsFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCompositionRelationshipsRequestListCompositionRelationshipsPaginateTypeDef(BaseModel):
    assetModelId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDashboardsRequestListDashboardsPaginateTypeDef(BaseModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGatewaysRequestListGatewaysPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPortalsRequestListPortalsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectAssetsRequestListProjectAssetsPaginateTypeDef(BaseModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseModel):
    portalId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTimeSeriesRequestListTimeSeriesPaginateTypeDef(BaseModel):
    assetId: Optional[str] = None
    aliasPrefix: Optional[str] = None
    timeSeriesType: Optional[ListTimeSeriesTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class MeasurementProcessingConfigTypeDef(BaseModel):
    forwardingConfig: ForwardingConfigTypeDef

class TransformProcessingConfigTypeDef(BaseModel):
    computeLocation: ComputeLocationType
    forwardingConfig: Optional[ForwardingConfigTypeDef] = None

class GatewayPlatformTypeDef(BaseModel):
    greengrass: Optional[GreengrassTypeDef] = None
    greengrassV2: Optional[GreengrassV2TypeDef] = None

class IdentityTypeDef(BaseModel):
    user: Optional[UserIdentityTypeDef] = None
    group: Optional[GroupIdentityTypeDef] = None
    iamUser: Optional[IAMUserIdentityTypeDef] = None
    iamRole: Optional[IAMRoleIdentityTypeDef] = None

class ListBulkImportJobsResponseTypeDef(BaseModel):
    jobSummaries: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResponseTypeDef(BaseModel):
    projectSummaries: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTimeSeriesResponseTypeDef(BaseModel):
    TimeSeriesSummaries: List[TimeSeriesSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricWindowTypeDef(BaseModel):
    tumbling: Optional[TumblingWindowTypeDef] = None

class PortalStatusTypeDef(BaseModel):
    state: PortalStateType
    error: Optional[MonitorErrorDetailsTypeDef] = None

class ResourceTypeDef(BaseModel):
    portal: Optional[PortalResourceTypeDef] = None
    project: Optional[ProjectResourceTypeDef] = None

class ListActionsResponseTypeDef(BaseModel):
    actionSummaries: List[ActionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAssetPropertyAggregatesSuccessEntryTypeDef(BaseModel):
    entryId: str
    aggregatedValues: List[AggregatedValueTypeDef]

class GetAssetPropertyAggregatesResponseTypeDef(BaseModel):
    aggregatedValues: List[AggregatedValueTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetRelationshipsResponseTypeDef(BaseModel):
    assetRelationshipSummaries: List[AssetRelationshipSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetModelCompositeModelsResponseTypeDef(BaseModel):
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExpressionVariablePaginatorTypeDef(BaseModel):
    name: str
    value: VariableValuePaginatorTypeDef

class ExpressionVariableTypeDef(BaseModel):
    name: str
    value: VariableValueTypeDef

class ListAssetPropertiesResponseTypeDef(BaseModel):
    assetPropertySummaries: List[AssetPropertySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetCompositeModelTypeDef(BaseModel):
    name: str
    type: str
    properties: List[AssetPropertyTypeDef]
    description: Optional[str] = None
    id: Optional[str] = None
    externalId: Optional[str] = None

class DescribeAssetCompositeModelResponseTypeDef(BaseModel):
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

class BatchPutAssetPropertyErrorEntryTypeDef(BaseModel):
    entryId: str
    errors: List[BatchPutAssetPropertyErrorTypeDef]

class BatchGetAssetPropertyValueHistorySuccessEntryTypeDef(BaseModel):
    entryId: str
    assetPropertyValueHistory: List[AssetPropertyValueTypeDef]

class BatchGetAssetPropertyValueSuccessEntryTypeDef(BaseModel):
    entryId: str
    assetPropertyValue: Optional[AssetPropertyValueTypeDef] = None

class GetAssetPropertyValueHistoryResponseTypeDef(BaseModel):
    assetPropertyValueHistory: List[AssetPropertyValueTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssetPropertyValueResponseTypeDef(BaseModel):
    propertyValue: AssetPropertyValueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAssetPropertyValueEntryTypeDef(BaseModel):
    entryId: str
    propertyValues: Sequence[AssetPropertyValueTypeDef]
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None

class GetInterpolatedAssetPropertyValuesResponseTypeDef(BaseModel):
    interpolatedAssetPropertyValues: List[InterpolatedAssetPropertyValueTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAssetPropertyAggregatesRequestRequestTypeDef(BaseModel):
    entries: Sequence[BatchGetAssetPropertyAggregatesEntryTypeDef]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class BatchGetAssetPropertyValueHistoryRequestRequestTypeDef(BaseModel):
    entries: Sequence[BatchGetAssetPropertyValueHistoryEntryTypeDef]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class CreatePortalRequestRequestTypeDef(BaseModel):
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

class ImageTypeDef(BaseModel):
    id: Optional[str] = None
    file: Optional[ImageFileTypeDef] = None

class ExecuteQueryResponseTypeDef(BaseModel):
    columns: List[ColumnInfoTypeDef]
    rows: List[RowTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDefaultEncryptionConfigurationResponseTypeDef(BaseModel):
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    configurationStatus: ConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDefaultEncryptionConfigurationResponseTypeDef(BaseModel):
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    configurationStatus: ConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobConfigurationTypeDef(BaseModel):
    fileFormat: FileFormatTypeDef

class DescribeStorageConfigurationResponseTypeDef(BaseModel):
    storageType: StorageTypeType
    multiLayerStorage: MultiLayerStorageTypeDef
    disassociatedDataStorage: DisassociatedDataStorageStateType
    retentionPeriod: RetentionPeriodTypeDef
    configurationStatus: ConfigurationStatusTypeDef
    lastUpdateDate: datetime
    warmTier: WarmTierStateType
    warmTierRetentionPeriod: WarmTierRetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutStorageConfigurationRequestRequestTypeDef(BaseModel):
    storageType: StorageTypeType
    multiLayerStorage: Optional[MultiLayerStorageTypeDef] = None
    disassociatedDataStorage: Optional[DisassociatedDataStorageStateType] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    warmTier: Optional[WarmTierStateType] = None
    warmTierRetentionPeriod: Optional[WarmTierRetentionPeriodTypeDef] = None

class PutStorageConfigurationResponseTypeDef(BaseModel):
    storageType: StorageTypeType
    multiLayerStorage: MultiLayerStorageTypeDef
    disassociatedDataStorage: DisassociatedDataStorageStateType
    retentionPeriod: RetentionPeriodTypeDef
    configurationStatus: ConfigurationStatusTypeDef
    warmTier: WarmTierStateType
    warmTierRetentionPeriod: WarmTierRetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssetModelStatusTypeDef(BaseModel):
    state: AssetModelStateType
    error: Optional[ErrorDetailsTypeDef] = None

class AssetStatusTypeDef(BaseModel):
    state: AssetStateType
    error: Optional[ErrorDetailsTypeDef] = None

class MeasurementTypeDef(BaseModel):
    processingConfig: Optional[MeasurementProcessingConfigTypeDef] = None

class CreateGatewayRequestRequestTypeDef(BaseModel):
    gatewayName: str
    gatewayPlatform: GatewayPlatformTypeDef
    tags: Optional[Mapping[str, str]] = None

class DescribeGatewayResponseTypeDef(BaseModel):
    gatewayId: str
    gatewayName: str
    gatewayArn: str
    gatewayPlatform: GatewayPlatformTypeDef
    gatewayCapabilitySummaries: List[GatewayCapabilitySummaryTypeDef]
    creationDate: datetime
    lastUpdateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GatewaySummaryTypeDef(BaseModel):
    gatewayId: str
    gatewayName: str
    creationDate: datetime
    lastUpdateDate: datetime
    gatewayPlatform: Optional[GatewayPlatformTypeDef] = None
    gatewayCapabilitySummaries: Optional[List[GatewayCapabilitySummaryTypeDef]] = None

class CreatePortalResponseTypeDef(BaseModel):
    portalId: str
    portalArn: str
    portalStartUrl: str
    portalStatus: PortalStatusTypeDef
    ssoApplicationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePortalResponseTypeDef(BaseModel):
    portalStatus: PortalStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePortalResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class PortalSummaryTypeDef(BaseModel):
    id: str
    name: str
    startUrl: str
    status: PortalStatusTypeDef
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None
    roleArn: Optional[str] = None

class UpdatePortalResponseTypeDef(BaseModel):
    portalStatus: PortalStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccessPolicySummaryTypeDef(BaseModel):
    id: str
    identity: IdentityTypeDef
    resource: ResourceTypeDef
    permission: PermissionType
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None

class CreateAccessPolicyRequestRequestTypeDef(BaseModel):
    accessPolicyIdentity: IdentityTypeDef
    accessPolicyResource: ResourceTypeDef
    accessPolicyPermission: PermissionType
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DescribeAccessPolicyResponseTypeDef(BaseModel):
    accessPolicyId: str
    accessPolicyArn: str
    accessPolicyIdentity: IdentityTypeDef
    accessPolicyResource: ResourceTypeDef
    accessPolicyPermission: PermissionType
    accessPolicyCreationDate: datetime
    accessPolicyLastUpdateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessPolicyRequestRequestTypeDef(BaseModel):
    accessPolicyId: str
    accessPolicyIdentity: IdentityTypeDef
    accessPolicyResource: ResourceTypeDef
    accessPolicyPermission: PermissionType
    clientToken: Optional[str] = None

class BatchGetAssetPropertyAggregatesResponseTypeDef(BaseModel):
    errorEntries: List[BatchGetAssetPropertyAggregatesErrorEntryTypeDef]
    successEntries: List[BatchGetAssetPropertyAggregatesSuccessEntryTypeDef]
    skippedEntries: List[BatchGetAssetPropertyAggregatesSkippedEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricPaginatorTypeDef(BaseModel):
    expression: str
    variables: List[ExpressionVariablePaginatorTypeDef]
    window: MetricWindowTypeDef
    processingConfig: Optional[MetricProcessingConfigTypeDef] = None

class TransformPaginatorTypeDef(BaseModel):
    expression: str
    variables: List[ExpressionVariablePaginatorTypeDef]
    processingConfig: Optional[TransformProcessingConfigTypeDef] = None

class MetricTypeDef(BaseModel):
    expression: str
    variables: Sequence[ExpressionVariableTypeDef]
    window: MetricWindowTypeDef
    processingConfig: Optional[MetricProcessingConfigTypeDef] = None

class TransformTypeDef(BaseModel):
    expression: str
    variables: Sequence[ExpressionVariableTypeDef]
    processingConfig: Optional[TransformProcessingConfigTypeDef] = None

class BatchPutAssetPropertyValueResponseTypeDef(BaseModel):
    errorEntries: List[BatchPutAssetPropertyErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAssetPropertyValueHistoryResponseTypeDef(BaseModel):
    errorEntries: List[BatchGetAssetPropertyValueHistoryErrorEntryTypeDef]
    successEntries: List[BatchGetAssetPropertyValueHistorySuccessEntryTypeDef]
    skippedEntries: List[BatchGetAssetPropertyValueHistorySkippedEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAssetPropertyValueResponseTypeDef(BaseModel):
    errorEntries: List[BatchGetAssetPropertyValueErrorEntryTypeDef]
    successEntries: List[BatchGetAssetPropertyValueSuccessEntryTypeDef]
    skippedEntries: List[BatchGetAssetPropertyValueSkippedEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutAssetPropertyValueRequestRequestTypeDef(BaseModel):
    entries: Sequence[PutAssetPropertyValueEntryTypeDef]

class UpdatePortalRequestRequestTypeDef(BaseModel):
    portalId: str
    portalName: str
    portalContactEmail: str
    roleArn: str
    portalDescription: Optional[str] = None
    portalLogoImage: Optional[ImageTypeDef] = None
    clientToken: Optional[str] = None
    notificationSenderEmail: Optional[str] = None
    alarms: Optional[AlarmsTypeDef] = None

class CreateBulkImportJobRequestRequestTypeDef(BaseModel):
    jobName: str
    jobRoleArn: str
    files: Sequence[FileTypeDef]
    errorReportLocation: ErrorReportLocationTypeDef
    jobConfiguration: JobConfigurationTypeDef
    adaptiveIngestion: Optional[bool] = None
    deleteFilesAfterImport: Optional[bool] = None

class DescribeBulkImportJobResponseTypeDef(BaseModel):
    jobId: str
    jobName: str
    jobStatus: JobStatusType
    jobRoleArn: str
    files: List[FileTypeDef]
    errorReportLocation: ErrorReportLocationTypeDef
    jobConfiguration: JobConfigurationTypeDef
    jobCreationDate: datetime
    jobLastUpdateDate: datetime
    adaptiveIngestion: bool
    deleteFilesAfterImport: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AssetModelSummaryTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    creationDate: datetime
    lastUpdateDate: datetime
    status: AssetModelStatusTypeDef
    assetModelType: Optional[AssetModelTypeType] = None
    externalId: Optional[str] = None

class CreateAssetModelCompositeModelResponseTypeDef(BaseModel):
    assetModelCompositeModelId: str
    assetModelCompositeModelPath: List[AssetModelCompositeModelPathSegmentTypeDef]
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssetModelResponseTypeDef(BaseModel):
    assetModelId: str
    assetModelArn: str
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAssetModelCompositeModelResponseTypeDef(BaseModel):
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAssetModelResponseTypeDef(BaseModel):
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssetModelCompositeModelResponseTypeDef(BaseModel):
    assetModelCompositeModelPath: List[AssetModelCompositeModelPathSegmentTypeDef]
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssetModelResponseTypeDef(BaseModel):
    assetModelStatus: AssetModelStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssetSummaryTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    assetModelId: str
    creationDate: datetime
    lastUpdateDate: datetime
    status: AssetStatusTypeDef
    hierarchies: List[AssetHierarchyTypeDef]
    description: Optional[str] = None
    externalId: Optional[str] = None

class AssociatedAssetsSummaryTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    assetModelId: str
    creationDate: datetime
    lastUpdateDate: datetime
    status: AssetStatusTypeDef
    hierarchies: List[AssetHierarchyTypeDef]
    description: Optional[str] = None
    externalId: Optional[str] = None

class CreateAssetResponseTypeDef(BaseModel):
    assetId: str
    assetArn: str
    assetStatus: AssetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAssetResponseTypeDef(BaseModel):
    assetStatus: AssetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAssetResponseTypeDef(BaseModel):
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

class UpdateAssetResponseTypeDef(BaseModel):
    assetStatus: AssetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGatewaysResponseTypeDef(BaseModel):
    gatewaySummaries: List[GatewaySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPortalsResponseTypeDef(BaseModel):
    portalSummaries: List[PortalSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessPoliciesResponseTypeDef(BaseModel):
    accessPolicySummaries: List[AccessPolicySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PropertyTypePaginatorTypeDef(BaseModel):
    attribute: Optional[AttributeTypeDef] = None
    measurement: Optional[MeasurementTypeDef] = None
    transform: Optional[TransformPaginatorTypeDef] = None
    metric: Optional[MetricPaginatorTypeDef] = None

class PropertyTypeTypeDef(BaseModel):
    attribute: Optional[AttributeTypeDef] = None
    measurement: Optional[MeasurementTypeDef] = None
    transform: Optional[TransformTypeDef] = None
    metric: Optional[MetricTypeDef] = None

class ListAssetModelsResponseTypeDef(BaseModel):
    assetModelSummaries: List[AssetModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetsResponseTypeDef(BaseModel):
    assetSummaries: List[AssetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedAssetsResponseTypeDef(BaseModel):
    assetSummaries: List[AssociatedAssetsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetModelPropertySummaryPaginatorTypeDef(BaseModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypePaginatorTypeDef
    id: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    assetModelCompositeModelId: Optional[str] = None
    path: Optional[List[AssetModelPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class AssetModelPropertyDefinitionTypeDef(BaseModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeTypeDef
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[str] = None
    externalId: Optional[str] = None

class AssetModelPropertySummaryTypeDef(BaseModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeTypeDef
    id: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    assetModelCompositeModelId: Optional[str] = None
    path: Optional[List[AssetModelPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class AssetModelPropertyTypeDef(BaseModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeTypeDef
    id: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    path: Optional[List[AssetModelPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class PropertyTypeDef(BaseModel):
    id: str
    name: str
    dataType: PropertyDataTypeType
    alias: Optional[str] = None
    notification: Optional[PropertyNotificationTypeDef] = None
    unit: Optional[str] = None
    type: Optional[PropertyTypeTypeDef] = None
    path: Optional[List[AssetPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class ListAssetModelPropertiesResponsePaginatorTypeDef(BaseModel):
    assetModelPropertySummaries: List[AssetModelPropertySummaryPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetModelCompositeModelDefinitionTypeDef(BaseModel):
    name: str
    type: str
    description: Optional[str] = None
    properties: Optional[Sequence[AssetModelPropertyDefinitionTypeDef]] = None
    id: Optional[str] = None
    externalId: Optional[str] = None

class CreateAssetModelCompositeModelRequestRequestTypeDef(BaseModel):
    assetModelId: str
    assetModelCompositeModelName: str
    assetModelCompositeModelType: str
    parentAssetModelCompositeModelId: Optional[str] = None
    assetModelCompositeModelExternalId: Optional[str] = None
    assetModelCompositeModelId: Optional[str] = None
    assetModelCompositeModelDescription: Optional[str] = None
    clientToken: Optional[str] = None
    composedAssetModelId: Optional[str] = None
    assetModelCompositeModelProperties: Optional[       Sequence[AssetModelPropertyDefinitionTypeDef]     ] = None

class ListAssetModelPropertiesResponseTypeDef(BaseModel):
    assetModelPropertySummaries: List[AssetModelPropertySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetModelCompositeModelTypeDef(BaseModel):
    name: str
    type: str
    description: Optional[str] = None
    properties: Optional[List[AssetModelPropertyTypeDef]] = None
    id: Optional[str] = None
    externalId: Optional[str] = None

class DescribeAssetModelCompositeModelResponseTypeDef(BaseModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelExternalId: str
    assetModelCompositeModelPath: List[AssetModelCompositeModelPathSegmentTypeDef]
    assetModelCompositeModelName: str
    assetModelCompositeModelDescription: str
    assetModelCompositeModelType: str
    assetModelCompositeModelProperties: List[AssetModelPropertyTypeDef]
    compositionDetails: CompositionDetailsTypeDef
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummaryTypeDef]
    actionDefinitions: List[ActionDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssetModelCompositeModelRequestRequestTypeDef(BaseModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelName: str
    assetModelCompositeModelExternalId: Optional[str] = None
    assetModelCompositeModelDescription: Optional[str] = None
    clientToken: Optional[str] = None
    assetModelCompositeModelProperties: Optional[Sequence[AssetModelPropertyTypeDef]] = None

class CompositeModelPropertyTypeDef(BaseModel):
    name: str
    type: str
    assetProperty: PropertyTypeDef
    id: Optional[str] = None
    externalId: Optional[str] = None

class CreateAssetModelRequestRequestTypeDef(BaseModel):
    assetModelName: str
    assetModelDescription: Optional[str] = None
    assetModelProperties: Optional[Sequence[AssetModelPropertyDefinitionTypeDef]] = None
    assetModelHierarchies: Optional[Sequence[AssetModelHierarchyDefinitionTypeDef]] = None
    assetModelCompositeModels: Optional[       Sequence[AssetModelCompositeModelDefinitionTypeDef]     ] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    assetModelId: Optional[str] = None
    assetModelExternalId: Optional[str] = None
    assetModelType: Optional[AssetModelTypeType] = None

class DescribeAssetModelResponseTypeDef(BaseModel):
    assetModelId: str
    assetModelArn: str
    assetModelName: str
    assetModelDescription: str
    assetModelProperties: List[AssetModelPropertyTypeDef]
    assetModelHierarchies: List[AssetModelHierarchyTypeDef]
    assetModelCompositeModels: List[AssetModelCompositeModelTypeDef]
    assetModelCreationDate: datetime
    assetModelLastUpdateDate: datetime
    assetModelStatus: AssetModelStatusTypeDef
    assetModelType: AssetModelTypeType
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummaryTypeDef]
    assetModelExternalId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssetModelRequestRequestTypeDef(BaseModel):
    assetModelId: str
    assetModelName: str
    assetModelDescription: Optional[str] = None
    assetModelProperties: Optional[Sequence[AssetModelPropertyTypeDef]] = None
    assetModelHierarchies: Optional[Sequence[AssetModelHierarchyTypeDef]] = None
    assetModelCompositeModels: Optional[Sequence[AssetModelCompositeModelTypeDef]] = None
    clientToken: Optional[str] = None
    assetModelExternalId: Optional[str] = None

class DescribeAssetPropertyResponseTypeDef(BaseModel):
    assetId: str
    assetName: str
    assetModelId: str
    assetProperty: PropertyTypeDef
    compositeModel: CompositeModelPropertyTypeDef
    assetExternalId: str
    ResponseMetadata: ResponseMetadataTypeDef


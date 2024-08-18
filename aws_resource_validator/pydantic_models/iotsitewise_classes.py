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
from aws_resource_validator.pydantic_models.iotsitewise_constants import *

class ActionDefinitionTypeDef(BaseValidatorModel):
    actionDefinitionId: str
    actionName: str
    actionType: str

class ActionPayloadTypeDef(BaseValidatorModel):
    stringValue: str

class TargetResourceTypeDef(BaseValidatorModel):
    assetId: str

class AggregatesTypeDef(BaseValidatorModel):
    average: Optional[float] = None
    count: Optional[float] = None
    maximum: Optional[float] = None
    minimum: Optional[float] = None
    sum: Optional[float] = None
    standardDeviation: Optional[float] = None

class AlarmsTypeDef(BaseValidatorModel):
    alarmRoleArn: str
    notificationLambdaArn: Optional[str] = None

class AssetCompositeModelPathSegmentTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None

class AssetErrorDetailsTypeDef(BaseValidatorModel):
    assetId: str
    code: Literal["INTERNAL_FAILURE"]
    message: str

class AssetHierarchyInfoTypeDef(BaseValidatorModel):
    parentAssetId: Optional[str] = None
    childAssetId: Optional[str] = None

class AssetHierarchyTypeDef(BaseValidatorModel):
    name: str
    id: Optional[str] = None
    externalId: Optional[str] = None

class AssetModelCompositeModelPathSegmentTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None

class AssetModelHierarchyDefinitionTypeDef(BaseValidatorModel):
    name: str
    childAssetModelId: str
    id: Optional[str] = None
    externalId: Optional[str] = None

class AssetModelHierarchyTypeDef(BaseValidatorModel):
    name: str
    childAssetModelId: str
    id: Optional[str] = None
    externalId: Optional[str] = None

class AssetModelPropertyPathSegmentTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None

class AssetPropertyPathSegmentTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None

class PropertyNotificationTypeDef(BaseValidatorModel):
    topic: str
    state: PropertyNotificationStateType

class TimeInNanosTypeDef(BaseValidatorModel):
    timeInSeconds: int
    offsetInNanos: Optional[int] = None

class VariantTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    integerValue: Optional[int] = None
    doubleValue: Optional[float] = None
    booleanValue: Optional[bool] = None

class AssociateAssetsRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    hierarchyId: str
    childAssetId: str
    clientToken: Optional[str] = None

class AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef(BaseValidatorModel):
    alias: str
    assetId: str
    propertyId: str
    clientToken: Optional[str] = None

class AttributeTypeDef(BaseValidatorModel):
    defaultValue: Optional[str] = None

class BatchAssociateProjectAssetsRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    assetIds: Sequence[str]
    clientToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDisassociateProjectAssetsRequestRequestTypeDef(BaseValidatorModel):
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

class ColumnTypeTypeDef(BaseValidatorModel):
    scalarType: Optional[ScalarTypeType] = None

class CompositionRelationshipItemTypeDef(BaseValidatorModel):
    id: Optional[str] = None

class CompositionRelationshipSummaryTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelType: str

class ConfigurationErrorDetailsTypeDef(BaseValidatorModel):
    code: ErrorCodeType
    message: str

class CreateAssetRequestRequestTypeDef(BaseValidatorModel):
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

class CreateDashboardRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    dashboardName: str
    dashboardDefinition: str
    dashboardDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateProjectRequestRequestTypeDef(BaseValidatorModel):
    portalId: str
    projectName: str
    projectDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CsvTypeDef(BaseValidatorModel):
    columnNames: Sequence[ColumnNameType]

class CustomerManagedS3StorageTypeDef(BaseValidatorModel):
    s3ResourceArn: str
    roleArn: str

class DashboardSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None

class RowTypeDef(BaseValidatorModel):
    data: List["DatumTypeDef"]

class DeleteAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
    accessPolicyId: str
    clientToken: Optional[str] = None

class DeleteAssetModelCompositeModelRequestRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    clientToken: Optional[str] = None

class DeleteAssetModelRequestRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    clientToken: Optional[str] = None

class DeleteAssetRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    clientToken: Optional[str] = None

class DeleteDashboardRequestRequestTypeDef(BaseValidatorModel):
    dashboardId: str
    clientToken: Optional[str] = None

class DeleteGatewayRequestRequestTypeDef(BaseValidatorModel):
    gatewayId: str

class DeletePortalRequestRequestTypeDef(BaseValidatorModel):
    portalId: str
    clientToken: Optional[str] = None

class DeleteProjectRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    clientToken: Optional[str] = None

class DeleteTimeSeriesRequestRequestTypeDef(BaseValidatorModel):
    alias: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    clientToken: Optional[str] = None

class DescribeAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
    accessPolicyId: str

class DescribeActionRequestRequestTypeDef(BaseValidatorModel):
    actionId: str

class DescribeAssetCompositeModelRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    assetCompositeModelId: str

class DescribeAssetModelCompositeModelRequestRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeAssetModelRequestRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None

class DescribeAssetPropertyRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    propertyId: str

class DescribeAssetRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    excludeProperties: Optional[bool] = None

class DescribeBulkImportJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class DescribeDashboardRequestRequestTypeDef(BaseValidatorModel):
    dashboardId: str

class DescribeGatewayCapabilityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    gatewayId: str
    capabilityNamespace: str

class DescribeGatewayRequestRequestTypeDef(BaseValidatorModel):
    gatewayId: str

class GatewayCapabilitySummaryTypeDef(BaseValidatorModel):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatusType

class LoggingOptionsTypeDef(BaseValidatorModel):
    level: LoggingLevelType

class DescribePortalRequestRequestTypeDef(BaseValidatorModel):
    portalId: str

class ImageLocationTypeDef(BaseValidatorModel):
    id: str
    url: str

class DescribeProjectRequestRequestTypeDef(BaseValidatorModel):
    projectId: str

class RetentionPeriodTypeDef(BaseValidatorModel):
    numberOfDays: Optional[int] = None
    unlimited: Optional[bool] = None

class WarmTierRetentionPeriodTypeDef(BaseValidatorModel):
    numberOfDays: Optional[int] = None
    unlimited: Optional[bool] = None

class DescribeTimeSeriesRequestRequestTypeDef(BaseValidatorModel):
    alias: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None

class DetailedErrorTypeDef(BaseValidatorModel):
    code: DetailedErrorCodeType
    message: str

class DisassociateAssetsRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    hierarchyId: str
    childAssetId: str
    clientToken: Optional[str] = None

class DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef(BaseValidatorModel):
    alias: str
    assetId: str
    propertyId: str
    clientToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ExecuteQueryRequestRequestTypeDef(BaseValidatorModel):
    queryStatement: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ForwardingConfigTypeDef(BaseValidatorModel):
    state: ForwardingConfigStateType

class GreengrassTypeDef(BaseValidatorModel):
    groupArn: str

class GreengrassV2TypeDef(BaseValidatorModel):
    coreDeviceThingName: str

class GetAssetPropertyValueRequestRequestTypeDef(BaseValidatorModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None

class GetInterpolatedAssetPropertyValuesRequestRequestTypeDef(BaseValidatorModel):
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

class GroupIdentityTypeDef(BaseValidatorModel):
    id: str

class IAMRoleIdentityTypeDef(BaseValidatorModel):
    arn: str

class IAMUserIdentityTypeDef(BaseValidatorModel):
    arn: str

class UserIdentityTypeDef(BaseValidatorModel):
    id: str

class JobSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    status: JobStatusType

class ListAccessPoliciesRequestRequestTypeDef(BaseValidatorModel):
    identityType: Optional[IdentityTypeType] = None
    identityId: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    iamArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListActionsRequestRequestTypeDef(BaseValidatorModel):
    targetResourceType: Literal["ASSET"]
    targetResourceId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssetModelCompositeModelsRequestRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssetModelPropertiesRequestRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListAssetModelPropertiesFilterType] = None

class ListAssetModelsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetModelTypes: Optional[Sequence[AssetModelTypeType]] = None

class ListAssetPropertiesRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListAssetPropertiesFilterType] = None

class ListAssetRelationshipsRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    traversalType: Literal["PATH_TO_ROOT"]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssetsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    assetModelId: Optional[str] = None
    filter: Optional[ListAssetsFilterType] = None

class ListAssociatedAssetsRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    hierarchyId: Optional[str] = None
    traversalDirection: Optional[TraversalDirectionType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListBulkImportJobsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListBulkImportJobsFilterType] = None

class ListCompositionRelationshipsRequestRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDashboardsRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListGatewaysRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPortalsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListProjectAssetsRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListProjectsRequestRequestTypeDef(BaseValidatorModel):
    portalId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProjectSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTimeSeriesRequestRequestTypeDef(BaseValidatorModel):
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

class MetricProcessingConfigTypeDef(BaseValidatorModel):
    computeLocation: ComputeLocationType

class TumblingWindowTypeDef(BaseValidatorModel):
    interval: str
    offset: Optional[str] = None

class MonitorErrorDetailsTypeDef(BaseValidatorModel):
    code: Optional[MonitorErrorCodeType] = None
    message: Optional[str] = None

class PortalResourceTypeDef(BaseValidatorModel):
    id: str

class ProjectResourceTypeDef(BaseValidatorModel):
    id: str

class PutDefaultEncryptionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyId: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAssetPropertyRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    propertyId: str
    propertyAlias: Optional[str] = None
    propertyNotificationState: Optional[PropertyNotificationStateType] = None
    clientToken: Optional[str] = None
    propertyUnit: Optional[str] = None

class UpdateAssetRequestRequestTypeDef(BaseValidatorModel):
    assetId: str
    assetName: str
    clientToken: Optional[str] = None
    assetDescription: Optional[str] = None
    assetExternalId: Optional[str] = None

class UpdateDashboardRequestRequestTypeDef(BaseValidatorModel):
    dashboardId: str
    dashboardName: str
    dashboardDefinition: str
    dashboardDescription: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateGatewayCapabilityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    gatewayId: str
    capabilityNamespace: str
    capabilityConfiguration: str

class UpdateGatewayRequestRequestTypeDef(BaseValidatorModel):
    gatewayId: str
    gatewayName: str

class UpdateProjectRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    projectName: str
    projectDescription: Optional[str] = None
    clientToken: Optional[str] = None

class ActionSummaryTypeDef(BaseValidatorModel):
    actionId: Optional[str] = None
    actionDefinitionId: Optional[str] = None
    targetResource: Optional[TargetResourceTypeDef] = None

class ExecuteActionRequestRequestTypeDef(BaseValidatorModel):
    targetResource: TargetResourceTypeDef
    actionDefinitionId: str
    actionPayload: ActionPayloadTypeDef
    clientToken: Optional[str] = None

class AggregatedValueTypeDef(BaseValidatorModel):
    timestamp: datetime
    value: AggregatesTypeDef
    quality: Optional[QualityType] = None

class AssetCompositeModelSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    type: str
    description: str
    path: List[AssetCompositeModelPathSegmentTypeDef]
    externalId: Optional[str] = None

class AssetRelationshipSummaryTypeDef(BaseValidatorModel):
    relationshipType: Literal["HIERARCHY"]
    hierarchyInfo: Optional[AssetHierarchyInfoTypeDef] = None

class AssetModelCompositeModelSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    type: str
    externalId: Optional[str] = None
    description: Optional[str] = None
    path: Optional[List[AssetModelCompositeModelPathSegmentTypeDef]] = None

class VariableValuePaginatorTypeDef(BaseValidatorModel):
    propertyId: Optional[str] = None
    hierarchyId: Optional[str] = None
    propertyPath: Optional[List[AssetModelPropertyPathSegmentTypeDef]] = None

class VariableValueTypeDef(BaseValidatorModel):
    propertyId: Optional[str] = None
    hierarchyId: Optional[str] = None
    propertyPath: Optional[Sequence[AssetModelPropertyPathSegmentTypeDef]] = None

class AssetPropertySummaryTypeDef(BaseValidatorModel):
    id: str
    alias: Optional[str] = None
    unit: Optional[str] = None
    notification: Optional[PropertyNotificationTypeDef] = None
    assetCompositeModelId: Optional[str] = None
    path: Optional[List[AssetPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class AssetPropertyTypeDef(BaseValidatorModel):
    id: str
    name: str
    dataType: PropertyDataTypeType
    alias: Optional[str] = None
    notification: Optional[PropertyNotificationTypeDef] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    path: Optional[List[AssetPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class BatchPutAssetPropertyErrorTypeDef(BaseValidatorModel):
    errorCode: BatchPutAssetPropertyValueErrorCodeType
    errorMessage: str
    timestamps: List[TimeInNanosTypeDef]

class AssetPropertyValueTypeDef(BaseValidatorModel):
    value: VariantTypeDef
    timestamp: TimeInNanosTypeDef
    quality: Optional[QualityType] = None

class InterpolatedAssetPropertyValueTypeDef(BaseValidatorModel):
    timestamp: TimeInNanosTypeDef
    value: VariantTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayCapabilityConfigurationResponseTypeDef(BaseValidatorModel):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatusType
    ResponseMetadata: ResponseMetadataTypeDef

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

class GetAssetPropertyAggregatesRequestRequestTypeDef(BaseValidatorModel):
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

class GetAssetPropertyValueHistoryRequestRequestTypeDef(BaseValidatorModel):
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

class BatchGetAssetPropertyValueRequestRequestTypeDef(BaseValidatorModel):
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

class ImageFileTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    type: Literal["PNG"]

class ColumnInfoTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[ColumnTypeTypeDef] = None

class CompositionDetailsTypeDef(BaseValidatorModel):
    compositionRelationship: Optional[List[CompositionRelationshipItemTypeDef]] = None

class ListCompositionRelationshipsResponseTypeDef(BaseValidatorModel):
    compositionRelationshipSummaries: List[CompositionRelationshipSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationStatusTypeDef(BaseValidatorModel):
    state: ConfigurationStateType
    error: Optional[ConfigurationErrorDetailsTypeDef] = None

class FileFormatTypeDef(BaseValidatorModel):
    csv: Optional[CsvTypeDef] = None
    parquet: Optional[Mapping[str, Any]] = None

class MultiLayerStorageTypeDef(BaseValidatorModel):
    customerManagedS3Storage: CustomerManagedS3StorageTypeDef

class ListDashboardsResponseTypeDef(BaseValidatorModel):
    dashboardSummaries: List[DashboardSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatumTypeDef(BaseValidatorModel):
    scalarValue: Optional[str] = None
    arrayValue: Optional[List[Dict[str, Any]]] = None
    rowValue: Optional[Dict[str, Any]] = None
    nullValue: Optional[bool] = None

class DescribeAssetModelRequestAssetModelActiveWaitTypeDef(BaseValidatorModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAssetModelRequestAssetModelNotExistsWaitTypeDef(BaseValidatorModel):
    assetModelId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAssetRequestAssetActiveWaitTypeDef(BaseValidatorModel):
    assetId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAssetRequestAssetNotExistsWaitTypeDef(BaseValidatorModel):
    assetId: str
    excludeProperties: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribePortalRequestPortalActiveWaitTypeDef(BaseValidatorModel):
    portalId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribePortalRequestPortalNotExistsWaitTypeDef(BaseValidatorModel):
    portalId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeLoggingOptionsResponseTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestRequestTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef

class ErrorDetailsTypeDef(BaseValidatorModel):
    code: ErrorCodeType
    message: str
    details: Optional[List[DetailedErrorTypeDef]] = None

class ExecuteQueryRequestExecuteQueryPaginateTypeDef(BaseValidatorModel):
    queryStatement: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAssetPropertyAggregatesRequestGetAssetPropertyAggregatesPaginateTypeDef(BaseValidatorModel):
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

class GetAssetPropertyValueHistoryRequestGetAssetPropertyValueHistoryPaginateTypeDef(BaseValidatorModel):
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    startDate: Optional[TimestampTypeDef] = None
    endDate: Optional[TimestampTypeDef] = None
    qualities: Optional[Sequence[QualityType]] = None
    timeOrdering: Optional[TimeOrderingType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetInterpolatedAssetPropertyValuesRequestGetInterpolatedAssetPropertyValuesPaginateTypeDef(BaseValidatorModel):
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

class ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef(BaseValidatorModel):
    identityType: Optional[IdentityTypeType] = None
    identityId: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    iamArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListActionsRequestListActionsPaginateTypeDef(BaseValidatorModel):
    targetResourceType: Literal["ASSET"]
    targetResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetModelCompositeModelsRequestListAssetModelCompositeModelsPaginateTypeDef(BaseValidatorModel):
    assetModelId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetModelPropertiesRequestListAssetModelPropertiesPaginateTypeDef(BaseValidatorModel):
    assetModelId: str
    filter: Optional[ListAssetModelPropertiesFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetModelsRequestListAssetModelsPaginateTypeDef(BaseValidatorModel):
    assetModelTypes: Optional[Sequence[AssetModelTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetPropertiesRequestListAssetPropertiesPaginateTypeDef(BaseValidatorModel):
    assetId: str
    filter: Optional[ListAssetPropertiesFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetRelationshipsRequestListAssetRelationshipsPaginateTypeDef(BaseValidatorModel):
    assetId: str
    traversalType: Literal["PATH_TO_ROOT"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetsRequestListAssetsPaginateTypeDef(BaseValidatorModel):
    assetModelId: Optional[str] = None
    filter: Optional[ListAssetsFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedAssetsRequestListAssociatedAssetsPaginateTypeDef(BaseValidatorModel):
    assetId: str
    hierarchyId: Optional[str] = None
    traversalDirection: Optional[TraversalDirectionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBulkImportJobsRequestListBulkImportJobsPaginateTypeDef(BaseValidatorModel):
    filter: Optional[ListBulkImportJobsFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCompositionRelationshipsRequestListCompositionRelationshipsPaginateTypeDef(BaseValidatorModel):
    assetModelId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDashboardsRequestListDashboardsPaginateTypeDef(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGatewaysRequestListGatewaysPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPortalsRequestListPortalsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectAssetsRequestListProjectAssetsPaginateTypeDef(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseValidatorModel):
    portalId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTimeSeriesRequestListTimeSeriesPaginateTypeDef(BaseValidatorModel):
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

class IdentityTypeDef(BaseValidatorModel):
    user: Optional[UserIdentityTypeDef] = None
    group: Optional[GroupIdentityTypeDef] = None
    iamUser: Optional[IAMUserIdentityTypeDef] = None
    iamRole: Optional[IAMRoleIdentityTypeDef] = None

class ListBulkImportJobsResponseTypeDef(BaseValidatorModel):
    jobSummaries: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResponseTypeDef(BaseValidatorModel):
    projectSummaries: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTimeSeriesResponseTypeDef(BaseValidatorModel):
    TimeSeriesSummaries: List[TimeSeriesSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricWindowTypeDef(BaseValidatorModel):
    tumbling: Optional[TumblingWindowTypeDef] = None

class PortalStatusTypeDef(BaseValidatorModel):
    state: PortalStateType
    error: Optional[MonitorErrorDetailsTypeDef] = None

class ResourceTypeDef(BaseValidatorModel):
    portal: Optional[PortalResourceTypeDef] = None
    project: Optional[ProjectResourceTypeDef] = None

class ListActionsResponseTypeDef(BaseValidatorModel):
    actionSummaries: List[ActionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAssetPropertyAggregatesSuccessEntryTypeDef(BaseValidatorModel):
    entryId: str
    aggregatedValues: List[AggregatedValueTypeDef]

class GetAssetPropertyAggregatesResponseTypeDef(BaseValidatorModel):
    aggregatedValues: List[AggregatedValueTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetRelationshipsResponseTypeDef(BaseValidatorModel):
    assetRelationshipSummaries: List[AssetRelationshipSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetModelCompositeModelsResponseTypeDef(BaseValidatorModel):
    assetModelCompositeModelSummaries: List[AssetModelCompositeModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExpressionVariablePaginatorTypeDef(BaseValidatorModel):
    name: str
    value: VariableValuePaginatorTypeDef

class ExpressionVariableTypeDef(BaseValidatorModel):
    name: str
    value: VariableValueTypeDef

class ListAssetPropertiesResponseTypeDef(BaseValidatorModel):
    assetPropertySummaries: List[AssetPropertySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetCompositeModelTypeDef(BaseValidatorModel):
    name: str
    type: str
    properties: List[AssetPropertyTypeDef]
    description: Optional[str] = None
    id: Optional[str] = None
    externalId: Optional[str] = None

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

class BatchGetAssetPropertyValueHistorySuccessEntryTypeDef(BaseValidatorModel):
    entryId: str
    assetPropertyValueHistory: List[AssetPropertyValueTypeDef]

class BatchGetAssetPropertyValueSuccessEntryTypeDef(BaseValidatorModel):
    entryId: str
    assetPropertyValue: Optional[AssetPropertyValueTypeDef] = None

class GetAssetPropertyValueHistoryResponseTypeDef(BaseValidatorModel):
    assetPropertyValueHistory: List[AssetPropertyValueTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAssetPropertyAggregatesRequestRequestTypeDef(BaseValidatorModel):
    entries: Sequence[BatchGetAssetPropertyAggregatesEntryTypeDef]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class BatchGetAssetPropertyValueHistoryRequestRequestTypeDef(BaseValidatorModel):
    entries: Sequence[BatchGetAssetPropertyValueHistoryEntryTypeDef]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class CreatePortalRequestRequestTypeDef(BaseValidatorModel):
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

class ImageTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    file: Optional[ImageFileTypeDef] = None

class ExecuteQueryResponseTypeDef(BaseValidatorModel):
    columns: List[ColumnInfoTypeDef]
    rows: List[RowTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    ResponseMetadata: ResponseMetadataTypeDef

class PutStorageConfigurationRequestRequestTypeDef(BaseValidatorModel):
    storageType: StorageTypeType
    multiLayerStorage: Optional[MultiLayerStorageTypeDef] = None
    disassociatedDataStorage: Optional[DisassociatedDataStorageStateType] = None
    retentionPeriod: Optional[RetentionPeriodTypeDef] = None
    warmTier: Optional[WarmTierStateType] = None
    warmTierRetentionPeriod: Optional[WarmTierRetentionPeriodTypeDef] = None

class PutStorageConfigurationResponseTypeDef(BaseValidatorModel):
    storageType: StorageTypeType
    multiLayerStorage: MultiLayerStorageTypeDef
    disassociatedDataStorage: DisassociatedDataStorageStateType
    retentionPeriod: RetentionPeriodTypeDef
    configurationStatus: ConfigurationStatusTypeDef
    warmTier: WarmTierStateType
    warmTierRetentionPeriod: WarmTierRetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssetModelStatusTypeDef(BaseValidatorModel):
    state: AssetModelStateType
    error: Optional[ErrorDetailsTypeDef] = None

class AssetStatusTypeDef(BaseValidatorModel):
    state: AssetStateType
    error: Optional[ErrorDetailsTypeDef] = None

class MeasurementTypeDef(BaseValidatorModel):
    processingConfig: Optional[MeasurementProcessingConfigTypeDef] = None

class CreateGatewayRequestRequestTypeDef(BaseValidatorModel):
    gatewayName: str
    gatewayPlatform: GatewayPlatformTypeDef
    tags: Optional[Mapping[str, str]] = None

class DescribeGatewayResponseTypeDef(BaseValidatorModel):
    gatewayId: str
    gatewayName: str
    gatewayArn: str
    gatewayPlatform: GatewayPlatformTypeDef
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
    gatewayCapabilitySummaries: Optional[List[GatewayCapabilitySummaryTypeDef]] = None

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
    ResponseMetadata: ResponseMetadataTypeDef

class PortalSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    startUrl: str
    status: PortalStatusTypeDef
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None
    roleArn: Optional[str] = None

class UpdatePortalResponseTypeDef(BaseValidatorModel):
    portalStatus: PortalStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccessPolicySummaryTypeDef(BaseValidatorModel):
    id: str
    identity: IdentityTypeDef
    resource: ResourceTypeDef
    permission: PermissionType
    creationDate: Optional[datetime] = None
    lastUpdateDate: Optional[datetime] = None

class CreateAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
    accessPolicyId: str
    accessPolicyIdentity: IdentityTypeDef
    accessPolicyResource: ResourceTypeDef
    accessPolicyPermission: PermissionType
    clientToken: Optional[str] = None

class BatchGetAssetPropertyAggregatesResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchGetAssetPropertyAggregatesErrorEntryTypeDef]
    successEntries: List[BatchGetAssetPropertyAggregatesSuccessEntryTypeDef]
    skippedEntries: List[BatchGetAssetPropertyAggregatesSkippedEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricPaginatorTypeDef(BaseValidatorModel):
    expression: str
    variables: List[ExpressionVariablePaginatorTypeDef]
    window: MetricWindowTypeDef
    processingConfig: Optional[MetricProcessingConfigTypeDef] = None

class TransformPaginatorTypeDef(BaseValidatorModel):
    expression: str
    variables: List[ExpressionVariablePaginatorTypeDef]
    processingConfig: Optional[TransformProcessingConfigTypeDef] = None

class MetricTypeDef(BaseValidatorModel):
    expression: str
    variables: Sequence[ExpressionVariableTypeDef]
    window: MetricWindowTypeDef
    processingConfig: Optional[MetricProcessingConfigTypeDef] = None

class TransformTypeDef(BaseValidatorModel):
    expression: str
    variables: Sequence[ExpressionVariableTypeDef]
    processingConfig: Optional[TransformProcessingConfigTypeDef] = None

class BatchPutAssetPropertyValueResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchPutAssetPropertyErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAssetPropertyValueHistoryResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchGetAssetPropertyValueHistoryErrorEntryTypeDef]
    successEntries: List[BatchGetAssetPropertyValueHistorySuccessEntryTypeDef]
    skippedEntries: List[BatchGetAssetPropertyValueHistorySkippedEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAssetPropertyValueResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchGetAssetPropertyValueErrorEntryTypeDef]
    successEntries: List[BatchGetAssetPropertyValueSuccessEntryTypeDef]
    skippedEntries: List[BatchGetAssetPropertyValueSkippedEntryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutAssetPropertyValueRequestRequestTypeDef(BaseValidatorModel):
    entries: Sequence[PutAssetPropertyValueEntryTypeDef]

class UpdatePortalRequestRequestTypeDef(BaseValidatorModel):
    portalId: str
    portalName: str
    portalContactEmail: str
    roleArn: str
    portalDescription: Optional[str] = None
    portalLogoImage: Optional[ImageTypeDef] = None
    clientToken: Optional[str] = None
    notificationSenderEmail: Optional[str] = None
    alarms: Optional[AlarmsTypeDef] = None

class CreateBulkImportJobRequestRequestTypeDef(BaseValidatorModel):
    jobName: str
    jobRoleArn: str
    files: Sequence[FileTypeDef]
    errorReportLocation: ErrorReportLocationTypeDef
    jobConfiguration: JobConfigurationTypeDef
    adaptiveIngestion: Optional[bool] = None
    deleteFilesAfterImport: Optional[bool] = None

class DescribeBulkImportJobResponseTypeDef(BaseValidatorModel):
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

class AssetModelSummaryTypeDef(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    creationDate: datetime
    lastUpdateDate: datetime
    status: AssetModelStatusTypeDef
    assetModelType: Optional[AssetModelTypeType] = None
    externalId: Optional[str] = None

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

class AssetSummaryTypeDef(BaseValidatorModel):
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

class AssociatedAssetsSummaryTypeDef(BaseValidatorModel):
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

class CreateAssetResponseTypeDef(BaseValidatorModel):
    assetId: str
    assetArn: str
    assetStatus: AssetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAssetResponseTypeDef(BaseValidatorModel):
    assetStatus: AssetStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListGatewaysResponseTypeDef(BaseValidatorModel):
    gatewaySummaries: List[GatewaySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPortalsResponseTypeDef(BaseValidatorModel):
    portalSummaries: List[PortalSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessPoliciesResponseTypeDef(BaseValidatorModel):
    accessPolicySummaries: List[AccessPolicySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PropertyTypePaginatorTypeDef(BaseValidatorModel):
    attribute: Optional[AttributeTypeDef] = None
    measurement: Optional[MeasurementTypeDef] = None
    transform: Optional[TransformPaginatorTypeDef] = None
    metric: Optional[MetricPaginatorTypeDef] = None

class PropertyTypeTypeDef(BaseValidatorModel):
    attribute: Optional[AttributeTypeDef] = None
    measurement: Optional[MeasurementTypeDef] = None
    transform: Optional[TransformTypeDef] = None
    metric: Optional[MetricTypeDef] = None

class ListAssetModelsResponseTypeDef(BaseValidatorModel):
    assetModelSummaries: List[AssetModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetsResponseTypeDef(BaseValidatorModel):
    assetSummaries: List[AssetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedAssetsResponseTypeDef(BaseValidatorModel):
    assetSummaries: List[AssociatedAssetsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetModelPropertySummaryPaginatorTypeDef(BaseValidatorModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypePaginatorTypeDef
    id: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    assetModelCompositeModelId: Optional[str] = None
    path: Optional[List[AssetModelPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class AssetModelPropertyDefinitionTypeDef(BaseValidatorModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeTypeDef
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[str] = None
    externalId: Optional[str] = None

class AssetModelPropertySummaryTypeDef(BaseValidatorModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeTypeDef
    id: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    assetModelCompositeModelId: Optional[str] = None
    path: Optional[List[AssetModelPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class AssetModelPropertyTypeDef(BaseValidatorModel):
    name: str
    dataType: PropertyDataTypeType
    type: PropertyTypeTypeDef
    id: Optional[str] = None
    dataTypeSpec: Optional[str] = None
    unit: Optional[str] = None
    path: Optional[List[AssetModelPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class PropertyTypeDef(BaseValidatorModel):
    id: str
    name: str
    dataType: PropertyDataTypeType
    alias: Optional[str] = None
    notification: Optional[PropertyNotificationTypeDef] = None
    unit: Optional[str] = None
    type: Optional[PropertyTypeTypeDef] = None
    path: Optional[List[AssetPropertyPathSegmentTypeDef]] = None
    externalId: Optional[str] = None

class ListAssetModelPropertiesResponsePaginatorTypeDef(BaseValidatorModel):
    assetModelPropertySummaries: List[AssetModelPropertySummaryPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetModelCompositeModelDefinitionTypeDef(BaseValidatorModel):
    name: str
    type: str
    description: Optional[str] = None
    properties: Optional[Sequence[AssetModelPropertyDefinitionTypeDef]] = None
    id: Optional[str] = None
    externalId: Optional[str] = None

class CreateAssetModelCompositeModelRequestRequestTypeDef(BaseValidatorModel):
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

class ListAssetModelPropertiesResponseTypeDef(BaseValidatorModel):
    assetModelPropertySummaries: List[AssetModelPropertySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetModelCompositeModelTypeDef(BaseValidatorModel):
    name: str
    type: str
    description: Optional[str] = None
    properties: Optional[List[AssetModelPropertyTypeDef]] = None
    id: Optional[str] = None
    externalId: Optional[str] = None

class DescribeAssetModelCompositeModelResponseTypeDef(BaseValidatorModel):
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

class UpdateAssetModelCompositeModelRequestRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelCompositeModelId: str
    assetModelCompositeModelName: str
    assetModelCompositeModelExternalId: Optional[str] = None
    assetModelCompositeModelDescription: Optional[str] = None
    clientToken: Optional[str] = None
    assetModelCompositeModelProperties: Optional[Sequence[AssetModelPropertyTypeDef]] = None

class CompositeModelPropertyTypeDef(BaseValidatorModel):
    name: str
    type: str
    assetProperty: PropertyTypeDef
    id: Optional[str] = None
    externalId: Optional[str] = None

class CreateAssetModelRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeAssetModelResponseTypeDef(BaseValidatorModel):
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

class UpdateAssetModelRequestRequestTypeDef(BaseValidatorModel):
    assetModelId: str
    assetModelName: str
    assetModelDescription: Optional[str] = None
    assetModelProperties: Optional[Sequence[AssetModelPropertyTypeDef]] = None
    assetModelHierarchies: Optional[Sequence[AssetModelHierarchyTypeDef]] = None
    assetModelCompositeModels: Optional[Sequence[AssetModelCompositeModelTypeDef]] = None
    clientToken: Optional[str] = None
    assetModelExternalId: Optional[str] = None

class DescribeAssetPropertyResponseTypeDef(BaseValidatorModel):
    assetId: str
    assetName: str
    assetModelId: str
    assetProperty: PropertyTypeDef
    compositeModel: CompositeModelPropertyTypeDef
    assetExternalId: str
    ResponseMetadata: ResponseMetadataTypeDef


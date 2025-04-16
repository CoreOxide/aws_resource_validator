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
from aws_resource_validator.pydantic_models.iottwinmaker_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BundleInformation(BaseValidatorModel):
    bundleNames: List[str]
    pricingTier: Optional[PricingTierType] = None


class CancelMetadataTransferJobRequest(BaseValidatorModel):
    metadataTransferJobId: str


class MetadataTransferJobProgress(BaseValidatorModel):
    totalCount: Optional[int] = None
    succeededCount: Optional[int] = None
    skippedCount: Optional[int] = None
    failedCount: Optional[int] = None


class ComponentPropertyGroupRequest(BaseValidatorModel):
    groupType: Optional[Literal["TABULAR"]] = None
    propertyNames: Optional[Sequence[str]] = None
    updateType: Optional[PropertyGroupUpdateTypeType] = None


class ComponentPropertyGroupResponse(BaseValidatorModel):
    groupType: Literal["TABULAR"]
    propertyNames: List[str]
    isInherited: bool


class CompositeComponentTypeRequest(BaseValidatorModel):
    componentTypeId: Optional[str] = None


class CompositeComponentTypeResponse(BaseValidatorModel):
    componentTypeId: Optional[str] = None
    isInherited: Optional[bool] = None


class PropertyGroupRequest(BaseValidatorModel):
    groupType: Optional[Literal["TABULAR"]] = None
    propertyNames: Optional[Sequence[str]] = None


class CreateSceneRequest(BaseValidatorModel):
    workspaceId: str
    sceneId: str
    contentLocation: str
    description: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None
    sceneMetadata: Optional[Mapping[str, str]] = None


class CreateSyncJobRequest(BaseValidatorModel):
    workspaceId: str
    syncSource: str
    syncRole: str
    tags: Optional[Mapping[str, str]] = None


class CreateWorkspaceRequest(BaseValidatorModel):
    workspaceId: str
    description: Optional[str] = None
    s3Location: Optional[str] = None
    role: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class LambdaFunction(BaseValidatorModel):
    arn: str


class Relationship(BaseValidatorModel):
    targetComponentTypeId: Optional[str] = None
    relationshipType: Optional[str] = None


class RelationshipValue(BaseValidatorModel):
    targetEntityId: Optional[str] = None
    targetComponentName: Optional[str] = None


class DeleteComponentTypeRequest(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str


class DeleteEntityRequest(BaseValidatorModel):
    workspaceId: str
    entityId: str
    isRecursive: Optional[bool] = None


class DeleteSceneRequest(BaseValidatorModel):
    workspaceId: str
    sceneId: str


class DeleteSyncJobRequest(BaseValidatorModel):
    workspaceId: str
    syncSource: str


class DeleteWorkspaceRequest(BaseValidatorModel):
    workspaceId: str


class IotTwinMakerDestinationConfiguration(BaseValidatorModel):
    workspace: str


class S3DestinationConfiguration(BaseValidatorModel):
    location: str


class EntityPropertyReferenceOutput(BaseValidatorModel):
    propertyName: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    externalIdProperty: Optional[Dict[str, str]] = None
    entityId: Optional[str] = None


class EntityPropertyReference(BaseValidatorModel):
    propertyName: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    externalIdProperty: Optional[Mapping[str, str]] = None
    entityId: Optional[str] = None


class ErrorDetails(BaseValidatorModel):
    code: Optional[ErrorCodeType] = None
    message: Optional[str] = None


class ExecuteQueryRequest(BaseValidatorModel):
    workspaceId: str
    queryStatement: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class Row(BaseValidatorModel):
    rowData: Optional[List[Dict[str, Any]]] = None


class FilterByAssetModel(BaseValidatorModel):
    assetModelId: Optional[str] = None
    assetModelExternalId: Optional[str] = None
    includeOffspring: Optional[bool] = None
    includeAssets: Optional[bool] = None


class FilterByAsset(BaseValidatorModel):
    assetId: Optional[str] = None
    assetExternalId: Optional[str] = None
    includeOffspring: Optional[bool] = None
    includeAssetModel: Optional[bool] = None


class FilterByComponentType(BaseValidatorModel):
    componentTypeId: str


class FilterByEntity(BaseValidatorModel):
    entityId: str


class GetComponentTypeRequest(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str


class PropertyGroupResponse(BaseValidatorModel):
    groupType: Literal["TABULAR"]
    propertyNames: List[str]
    isInherited: bool


class GetEntityRequest(BaseValidatorModel):
    workspaceId: str
    entityId: str


class GetMetadataTransferJobRequest(BaseValidatorModel):
    metadataTransferJobId: str


class InterpolationParameters(BaseValidatorModel):
    interpolationType: Optional[Literal["LINEAR"]] = None
    intervalInSeconds: Optional[int] = None


class GetSceneRequest(BaseValidatorModel):
    workspaceId: str
    sceneId: str


class SceneError(BaseValidatorModel):
    code: Optional[Literal["MATTERPORT_ERROR"]] = None
    message: Optional[str] = None


class GetSyncJobRequest(BaseValidatorModel):
    syncSource: str
    workspaceId: Optional[str] = None


class GetWorkspaceRequest(BaseValidatorModel):
    workspaceId: str


class ListComponentTypesFilter(BaseValidatorModel):
    extendsFrom: Optional[str] = None
    namespace: Optional[str] = None
    isAbstract: Optional[bool] = None


class ListComponentsRequest(BaseValidatorModel):
    workspaceId: str
    entityId: str
    componentPath: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEntitiesFilter(BaseValidatorModel):
    parentEntityId: Optional[str] = None
    componentTypeId: Optional[str] = None
    externalId: Optional[str] = None


class ListMetadataTransferJobsFilter(BaseValidatorModel):
    workspaceId: Optional[str] = None
    state: Optional[MetadataTransferJobStateType] = None


class ListPropertiesRequest(BaseValidatorModel):
    workspaceId: str
    entityId: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListScenesRequest(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SceneSummary(BaseValidatorModel):
    sceneId: str
    contentLocation: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: Optional[str] = None


class ListSyncJobsRequest(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SyncResourceFilter(BaseValidatorModel):
    state: Optional[SyncResourceStateType] = None
    resourceType: Optional[SyncResourceTypeType] = None
    resourceId: Optional[str] = None
    externalId: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkspacesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkspaceSummary(BaseValidatorModel):
    workspaceId: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: Optional[str] = None
    linkedServices: Optional[List[str]] = None


class OrderBy(BaseValidatorModel):
    propertyName: str
    order: Optional[OrderType] = None


class ParentEntityUpdateRequest(BaseValidatorModel):
    updateType: ParentEntityUpdateTypeType
    parentEntityId: Optional[str] = None


class S3SourceConfiguration(BaseValidatorModel):
    location: str


class TagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class UpdatePricingPlanRequest(BaseValidatorModel):
    pricingMode: PricingModeType
    bundleNames: Optional[Sequence[str]] = None


class UpdateSceneRequest(BaseValidatorModel):
    workspaceId: str
    sceneId: str
    contentLocation: Optional[str] = None
    description: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    sceneMetadata: Optional[Mapping[str, str]] = None


class UpdateWorkspaceRequest(BaseValidatorModel):
    workspaceId: str
    description: Optional[str] = None
    role: Optional[str] = None
    s3Location: Optional[str] = None


class CreateComponentTypeResponse(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadata


class CreateEntityResponse(BaseValidatorModel):
    entityId: str
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadata


class CreateSceneResponse(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateSyncJobResponse(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadata


class CreateWorkspaceResponse(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadata


class DeleteComponentTypeResponse(BaseValidatorModel):
    state: StateType
    ResponseMetadata: ResponseMetadata


class DeleteEntityResponse(BaseValidatorModel):
    state: StateType
    ResponseMetadata: ResponseMetadata


class DeleteSyncJobResponse(BaseValidatorModel):
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadata


class DeleteWorkspaceResponse(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


class GetWorkspaceResponse(BaseValidatorModel):
    workspaceId: str
    arn: str
    description: str
    linkedServices: List[str]
    s3Location: str
    role: str
    creationDateTime: datetime
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateComponentTypeResponse(BaseValidatorModel):
    workspaceId: str
    arn: str
    componentTypeId: str
    state: StateType
    ResponseMetadata: ResponseMetadata


class UpdateEntityResponse(BaseValidatorModel):
    updateDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadata


class UpdateSceneResponse(BaseValidatorModel):
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateWorkspaceResponse(BaseValidatorModel):
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadata


class PricingPlan(BaseValidatorModel):
    effectiveDateTime: datetime
    pricingMode: PricingModeType
    updateDateTime: datetime
    updateReason: UpdateReasonType
    billableEntityCount: Optional[int] = None
    bundleInformation: Optional[BundleInformation] = None


class DataValueOutput(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    integerValue: Optional[int] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None
    listValue: Optional[List[Dict[str, Any]]] = None
    mapValue: Optional[Dict[str, Dict[str, Any]]] = None
    relationshipValue: Optional[RelationshipValue] = None
    expression: Optional[str] = None


class DataValue(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    integerValue: Optional[int] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None
    listValue: Optional[Sequence[Mapping[str, Any]]] = None
    mapValue: Optional[Mapping[str, Mapping[str, Any]]] = None
    relationshipValue: Optional[RelationshipValue] = None
    expression: Optional[str] = None


class MetadataTransferJobStatus(BaseValidatorModel):
    state: Optional[MetadataTransferJobStateType] = None
    error: Optional[ErrorDetails] = None
    queuedPosition: Optional[int] = None


class Status(BaseValidatorModel):
    state: Optional[StateType] = None
    error: Optional[ErrorDetails] = None


class SyncJobStatus(BaseValidatorModel):
    state: Optional[SyncJobStateType] = None
    error: Optional[ErrorDetails] = None


class SyncResourceStatus(BaseValidatorModel):
    state: Optional[SyncResourceStateType] = None
    error: Optional[ErrorDetails] = None


class ColumnDescription(BaseValidatorModel):
    pass


class ExecuteQueryResponse(BaseValidatorModel):
    columnDescriptions: List[ColumnDescription]
    rows: List[Row]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IotSiteWiseSourceConfigurationFilter(BaseValidatorModel):
    filterByAssetModel: Optional[FilterByAssetModel] = None
    filterByAsset: Optional[FilterByAsset] = None


class IotTwinMakerSourceConfigurationFilter(BaseValidatorModel):
    filterByComponentType: Optional[FilterByComponentType] = None
    filterByEntity: Optional[FilterByEntity] = None


class GetSceneResponse(BaseValidatorModel):
    workspaceId: str
    sceneId: str
    contentLocation: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: str
    capabilities: List[str]
    sceneMetadata: Dict[str, str]
    generatedSceneMetadata: Dict[str, str]
    error: SceneError
    ResponseMetadata: ResponseMetadata


class ListComponentTypesRequest(BaseValidatorModel):
    workspaceId: str
    filters: Optional[Sequence[ListComponentTypesFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListEntitiesRequest(BaseValidatorModel):
    workspaceId: str
    filters: Optional[Sequence[ListEntitiesFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListMetadataTransferJobsRequest(BaseValidatorModel):
    sourceType: SourceTypeType
    destinationType: DestinationTypeType
    filters: Optional[Sequence[ListMetadataTransferJobsFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListScenesResponse(BaseValidatorModel):
    sceneSummaries: List[SceneSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSyncResourcesRequest(BaseValidatorModel):
    workspaceId: str
    syncSource: str
    filters: Optional[Sequence[SyncResourceFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkspacesResponse(BaseValidatorModel):
    workspaceSummaries: List[WorkspaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetPricingPlanResponse(BaseValidatorModel):
    currentPricingPlan: PricingPlan
    pendingPricingPlan: PricingPlan
    ResponseMetadata: ResponseMetadata


class UpdatePricingPlanResponse(BaseValidatorModel):
    currentPricingPlan: PricingPlan
    pendingPricingPlan: PricingPlan
    ResponseMetadata: ResponseMetadata


class DataConnector(BaseValidatorModel):
    pass


class FunctionRequest(BaseValidatorModel):
    requiredProperties: Optional[Sequence[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnector] = None


class FunctionResponse(BaseValidatorModel):
    requiredProperties: Optional[List[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnector] = None
    isInherited: Optional[bool] = None


class PropertyLatestValue(BaseValidatorModel):
    propertyReference: EntityPropertyReferenceOutput
    propertyValue: Optional[DataValueOutput] = None


class PropertyValueOutput(BaseValidatorModel):
    value: DataValueOutput
    timestamp: Optional[datetime] = None
    time: Optional[str] = None


class CancelMetadataTransferJobResponse(BaseValidatorModel):
    metadataTransferJobId: str
    arn: str
    updateDateTime: datetime
    status: MetadataTransferJobStatus
    progress: MetadataTransferJobProgress
    ResponseMetadata: ResponseMetadata


class CreateMetadataTransferJobResponse(BaseValidatorModel):
    metadataTransferJobId: str
    arn: str
    creationDateTime: datetime
    status: MetadataTransferJobStatus
    ResponseMetadata: ResponseMetadata


class MetadataTransferJobSummary(BaseValidatorModel):
    metadataTransferJobId: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    status: MetadataTransferJobStatus
    progress: Optional[MetadataTransferJobProgress] = None


class ComponentSummary(BaseValidatorModel):
    componentName: str
    componentTypeId: str
    status: Status
    definedIn: Optional[str] = None
    description: Optional[str] = None
    propertyGroups: Optional[Dict[str, ComponentPropertyGroupResponse]] = None
    syncSource: Optional[str] = None
    componentPath: Optional[str] = None


class ComponentTypeSummary(BaseValidatorModel):
    arn: str
    componentTypeId: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: Optional[str] = None
    status: Optional[Status] = None
    componentTypeName: Optional[str] = None


class EntitySummary(BaseValidatorModel):
    entityId: str
    entityName: str
    arn: str
    status: Status
    creationDateTime: datetime
    updateDateTime: datetime
    parentEntityId: Optional[str] = None
    description: Optional[str] = None
    hasChildEntities: Optional[bool] = None


class GetSyncJobResponse(BaseValidatorModel):
    arn: str
    workspaceId: str
    syncSource: str
    syncRole: str
    status: SyncJobStatus
    creationDateTime: datetime
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadata


class SyncJobSummary(BaseValidatorModel):
    arn: Optional[str] = None
    workspaceId: Optional[str] = None
    syncSource: Optional[str] = None
    status: Optional[SyncJobStatus] = None
    creationDateTime: Optional[datetime] = None
    updateDateTime: Optional[datetime] = None


class SyncResourceSummary(BaseValidatorModel):
    resourceType: Optional[SyncResourceTypeType] = None
    externalId: Optional[str] = None
    resourceId: Optional[str] = None
    status: Optional[SyncResourceStatus] = None
    updateDateTime: Optional[datetime] = None


class IotSiteWiseSourceConfigurationOutput(BaseValidatorModel):
    filters: Optional[List[IotSiteWiseSourceConfigurationFilter]] = None


class IotSiteWiseSourceConfiguration(BaseValidatorModel):
    filters: Optional[Sequence[IotSiteWiseSourceConfigurationFilter]] = None


class IotTwinMakerSourceConfigurationOutput(BaseValidatorModel):
    workspace: str
    filters: Optional[List[IotTwinMakerSourceConfigurationFilter]] = None


class IotTwinMakerSourceConfiguration(BaseValidatorModel):
    workspace: str
    filters: Optional[Sequence[IotTwinMakerSourceConfigurationFilter]] = None


class DataTypeOutput(BaseValidatorModel):
    pass


class PropertyDefinitionResponse(BaseValidatorModel):
    dataType: DataTypeOutput
    isTimeSeries: bool
    isRequiredInEntity: bool
    isExternalId: bool
    isStoredExternally: bool
    isImported: bool
    isFinal: bool
    isInherited: bool
    defaultValue: Optional[DataValueOutput] = None
    configuration: Optional[Dict[str, str]] = None
    displayName: Optional[str] = None


class GetPropertyValueResponse(BaseValidatorModel):
    propertyValues: Dict[str, PropertyLatestValue]
    tabularPropertyValues: List[List[Dict[str, DataValueOutput]]]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PropertyValueEntryOutput(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceOutput
    propertyValues: Optional[List[PropertyValueOutput]] = None


class PropertyValueHistory(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceOutput
    values: Optional[List[PropertyValueOutput]] = None


class Timestamp(BaseValidatorModel):
    pass


class DataValueUnion(BaseValidatorModel):
    pass


class PropertyValue(BaseValidatorModel):
    value: DataValueUnion
    timestamp: Optional[Timestamp] = None
    time: Optional[str] = None


class ListMetadataTransferJobsResponse(BaseValidatorModel):
    metadataTransferJobSummaries: List[MetadataTransferJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListComponentsResponse(BaseValidatorModel):
    componentSummaries: List[ComponentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListComponentTypesResponse(BaseValidatorModel):
    workspaceId: str
    componentTypeSummaries: List[ComponentTypeSummary]
    maxResults: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEntitiesResponse(BaseValidatorModel):
    entitySummaries: List[EntitySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSyncJobsResponse(BaseValidatorModel):
    syncJobSummaries: List[SyncJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSyncResourcesResponse(BaseValidatorModel):
    syncResources: List[SyncResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetComponentTypeResponse(BaseValidatorModel):
    workspaceId: str
    isSingleton: bool
    componentTypeId: str
    description: str
    propertyDefinitions: Dict[str, PropertyDefinitionResponse]
    extendsFrom: List[str]
    functions: Dict[str, FunctionResponse]
    creationDateTime: datetime
    updateDateTime: datetime
    arn: str
    isAbstract: bool
    isSchemaInitialized: bool
    status: Status
    propertyGroups: Dict[str, PropertyGroupResponse]
    syncSource: str
    componentTypeName: str
    compositeComponentTypes: Dict[str, CompositeComponentTypeResponse]
    ResponseMetadata: ResponseMetadata


class PropertyResponse(BaseValidatorModel):
    definition: Optional[PropertyDefinitionResponse] = None
    value: Optional[DataValueOutput] = None
    areAllPropertyValuesReturned: Optional[bool] = None


class PropertySummary(BaseValidatorModel):
    propertyName: str
    definition: Optional[PropertyDefinitionResponse] = None
    value: Optional[DataValueOutput] = None
    areAllPropertyValuesReturned: Optional[bool] = None


class BatchPutPropertyError(BaseValidatorModel):
    errorCode: str
    errorMessage: str
    entry: PropertyValueEntryOutput


class GetPropertyValueHistoryResponse(BaseValidatorModel):
    propertyValues: List[PropertyValueHistory]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PropertyFilter(BaseValidatorModel):
    pass


class GetPropertyValueHistoryRequest(BaseValidatorModel):
    workspaceId: str
    selectedProperties: Sequence[str]
    entityId: Optional[str] = None
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    componentTypeId: Optional[str] = None
    propertyFilters: Optional[Sequence[PropertyFilter]] = None
    startDateTime: Optional[Timestamp] = None
    endDateTime: Optional[Timestamp] = None
    interpolation: Optional[InterpolationParameters] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    orderByTime: Optional[OrderByTimeType] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None


class TabularConditions(BaseValidatorModel):
    orderBy: Optional[Sequence[OrderBy]] = None
    propertyFilters: Optional[Sequence[PropertyFilter]] = None


class SourceConfigurationOutput(BaseValidatorModel):
    pass


class DestinationConfiguration(BaseValidatorModel):
    pass


class GetMetadataTransferJobResponse(BaseValidatorModel):
    metadataTransferJobId: str
    arn: str
    description: str
    sources: List[SourceConfigurationOutput]
    destination: DestinationConfiguration
    metadataTransferJobRole: str
    reportUrl: str
    creationDateTime: datetime
    updateDateTime: datetime
    status: MetadataTransferJobStatus
    progress: MetadataTransferJobProgress
    ResponseMetadata: ResponseMetadata


class ComponentResponse(BaseValidatorModel):
    componentName: Optional[str] = None
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    status: Optional[Status] = None
    definedIn: Optional[str] = None
    properties: Optional[Dict[str, PropertyResponse]] = None
    propertyGroups: Optional[Dict[str, ComponentPropertyGroupResponse]] = None
    syncSource: Optional[str] = None
    areAllPropertiesReturned: Optional[bool] = None
    compositeComponents: Optional[Dict[str, ComponentSummary]] = None
    areAllCompositeComponentsReturned: Optional[bool] = None


class ListPropertiesResponse(BaseValidatorModel):
    propertySummaries: List[PropertySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchPutPropertyErrorEntry(BaseValidatorModel):
    errors: List[BatchPutPropertyError]


class DataTypeUnion(BaseValidatorModel):
    pass


class PropertyDefinitionRequest(BaseValidatorModel):
    dataType: Optional[DataTypeUnion] = None
    isRequiredInEntity: Optional[bool] = None
    isExternalId: Optional[bool] = None
    isStoredExternally: Optional[bool] = None
    isTimeSeries: Optional[bool] = None
    defaultValue: Optional[DataValueUnion] = None
    configuration: Optional[Mapping[str, str]] = None
    displayName: Optional[str] = None


class GetPropertyValueRequest(BaseValidatorModel):
    selectedProperties: Sequence[str]
    workspaceId: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    componentTypeId: Optional[str] = None
    entityId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    propertyGroupName: Optional[str] = None
    tabularConditions: Optional[TabularConditions] = None


class EntityPropertyReferenceUnion(BaseValidatorModel):
    pass


class PropertyValueUnion(BaseValidatorModel):
    pass


class PropertyValueEntry(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceUnion
    propertyValues: Optional[Sequence[PropertyValueUnion]] = None


class GetEntityResponse(BaseValidatorModel):
    entityId: str
    entityName: str
    arn: str
    status: Status
    workspaceId: str
    description: str
    components: Dict[str, ComponentResponse]
    parentEntityId: str
    hasChildEntities: bool
    creationDateTime: datetime
    updateDateTime: datetime
    syncSource: str
    areAllComponentsReturned: bool
    ResponseMetadata: ResponseMetadata


class BatchPutPropertyValuesResponse(BaseValidatorModel):
    errorEntries: List[BatchPutPropertyErrorEntry]
    ResponseMetadata: ResponseMetadata


class CreateComponentTypeRequest(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str
    isSingleton: Optional[bool] = None
    description: Optional[str] = None
    propertyDefinitions: Optional[Mapping[str, PropertyDefinitionRequest]] = None
    extendsFrom: Optional[Sequence[str]] = None
    functions: Optional[Mapping[str, FunctionRequest]] = None
    tags: Optional[Mapping[str, str]] = None
    propertyGroups: Optional[Mapping[str, PropertyGroupRequest]] = None
    componentTypeName: Optional[str] = None
    compositeComponentTypes: Optional[Mapping[str, CompositeComponentTypeRequest]] = None


class PropertyRequest(BaseValidatorModel):
    definition: Optional[PropertyDefinitionRequest] = None
    value: Optional[DataValueUnion] = None
    updateType: Optional[PropertyUpdateTypeType] = None


class UpdateComponentTypeRequest(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str
    isSingleton: Optional[bool] = None
    description: Optional[str] = None
    propertyDefinitions: Optional[Mapping[str, PropertyDefinitionRequest]] = None
    extendsFrom: Optional[Sequence[str]] = None
    functions: Optional[Mapping[str, FunctionRequest]] = None
    propertyGroups: Optional[Mapping[str, PropertyGroupRequest]] = None
    componentTypeName: Optional[str] = None
    compositeComponentTypes: Optional[Mapping[str, CompositeComponentTypeRequest]] = None


class SourceConfigurationUnion(BaseValidatorModel):
    pass


class CreateMetadataTransferJobRequest(BaseValidatorModel):
    sources: Sequence[SourceConfigurationUnion]
    destination: DestinationConfiguration
    metadataTransferJobId: Optional[str] = None
    description: Optional[str] = None


class ComponentRequest(BaseValidatorModel):
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    properties: Optional[Mapping[str, PropertyRequest]] = None
    propertyGroups: Optional[Mapping[str, ComponentPropertyGroupRequest]] = None


class ComponentUpdateRequest(BaseValidatorModel):
    updateType: Optional[ComponentUpdateTypeType] = None
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    propertyUpdates: Optional[Mapping[str, PropertyRequest]] = None
    propertyGroupUpdates: Optional[Mapping[str, ComponentPropertyGroupRequest]] = None


class CompositeComponentRequest(BaseValidatorModel):
    description: Optional[str] = None
    properties: Optional[Mapping[str, PropertyRequest]] = None
    propertyGroups: Optional[Mapping[str, ComponentPropertyGroupRequest]] = None


class CompositeComponentUpdateRequest(BaseValidatorModel):
    updateType: Optional[ComponentUpdateTypeType] = None
    description: Optional[str] = None
    propertyUpdates: Optional[Mapping[str, PropertyRequest]] = None
    propertyGroupUpdates: Optional[Mapping[str, ComponentPropertyGroupRequest]] = None


class PropertyValueEntryUnion(BaseValidatorModel):
    pass


class BatchPutPropertyValuesRequest(BaseValidatorModel):
    workspaceId: str
    entries: Sequence[PropertyValueEntryUnion]


class CreateEntityRequest(BaseValidatorModel):
    workspaceId: str
    entityName: str
    entityId: Optional[str] = None
    description: Optional[str] = None
    components: Optional[Mapping[str, ComponentRequest]] = None
    compositeComponents: Optional[Mapping[str, CompositeComponentRequest]] = None
    parentEntityId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateEntityRequest(BaseValidatorModel):
    workspaceId: str
    entityId: str
    entityName: Optional[str] = None
    description: Optional[str] = None
    componentUpdates: Optional[Mapping[str, ComponentUpdateRequest]] = None
    compositeComponentUpdates: Optional[Mapping[str, CompositeComponentUpdateRequest]] = None
    parentEntityUpdate: Optional[ParentEntityUpdateRequest] = None



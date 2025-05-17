from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iottwinmaker.iottwinmaker_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BundleInformation(BaseValidatorModel):
    bundleNames: List[str]
    pricingTier: Optional[PricingTierType] = None


# This class is the input for the 'cancel_metadata_transfer_job' function.
class CancelMetadataTransferJobRequest(BaseValidatorModel):
    metadataTransferJobId: str


class MetadataTransferJobProgress(BaseValidatorModel):
    totalCount: Optional[int] = None
    succeededCount: Optional[int] = None
    skippedCount: Optional[int] = None
    failedCount: Optional[int] = None


class ColumnDescription(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[ColumnTypeType] = None


class ComponentPropertyGroupRequest(BaseValidatorModel):
    groupType: Optional[Literal['TABULAR']] = None
    propertyNames: Optional[List[str]] = None
    updateType: Optional[PropertyGroupUpdateTypeType] = None


class ComponentPropertyGroupResponse(BaseValidatorModel):
    groupType: Literal['TABULAR']
    propertyNames: List[str]
    isInherited: bool


class CompositeComponentTypeRequest(BaseValidatorModel):
    componentTypeId: Optional[str] = None


class CompositeComponentTypeResponse(BaseValidatorModel):
    componentTypeId: Optional[str] = None
    isInherited: Optional[bool] = None


class PropertyGroupRequest(BaseValidatorModel):
    groupType: Optional[Literal['TABULAR']] = None
    propertyNames: Optional[List[str]] = None


# This class is the input for the 'create_scene' function.
class CreateSceneRequest(BaseValidatorModel):
    workspaceId: str
    sceneId: str
    contentLocation: str
    description: Optional[str] = None
    capabilities: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None
    sceneMetadata: Optional[Dict[str, str]] = None


# This class is the input for the 'create_sync_job' function.
class CreateSyncJobRequest(BaseValidatorModel):
    workspaceId: str
    syncSource: str
    syncRole: str
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_workspace' function.
class CreateWorkspaceRequest(BaseValidatorModel):
    workspaceId: str
    description: Optional[str] = None
    s3Location: Optional[str] = None
    role: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class LambdaFunction(BaseValidatorModel):
    arn: str


class Relationship(BaseValidatorModel):
    targetComponentTypeId: Optional[str] = None
    relationshipType: Optional[str] = None


class RelationshipValue(BaseValidatorModel):
    targetEntityId: Optional[str] = None
    targetComponentName: Optional[str] = None


# This class is the input for the 'delete_component_type' function.
class DeleteComponentTypeRequest(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str


# This class is the input for the 'delete_entity' function.
class DeleteEntityRequest(BaseValidatorModel):
    workspaceId: str
    entityId: str
    isRecursive: Optional[bool] = None


class DeleteSceneRequest(BaseValidatorModel):
    workspaceId: str
    sceneId: str


# This class is the input for the 'delete_sync_job' function.
class DeleteSyncJobRequest(BaseValidatorModel):
    workspaceId: str
    syncSource: str


# This class is the input for the 'delete_workspace' function.
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
    externalIdProperty: Optional[Dict[str, str]] = None
    entityId: Optional[str] = None


class ErrorDetails(BaseValidatorModel):
    code: Optional[ErrorCodeType] = None
    message: Optional[str] = None


# This class is the input for the 'execute_query' function.
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


# This class is the input for the 'get_component_type' function.
class GetComponentTypeRequest(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str


class PropertyGroupResponse(BaseValidatorModel):
    groupType: Literal['TABULAR']
    propertyNames: List[str]
    isInherited: bool


# This class is the input for the 'get_entity' function.
class GetEntityRequest(BaseValidatorModel):
    workspaceId: str
    entityId: str


# This class is the input for the 'get_metadata_transfer_job' function.
class GetMetadataTransferJobRequest(BaseValidatorModel):
    metadataTransferJobId: str


class InterpolationParameters(BaseValidatorModel):
    interpolationType: Optional[Literal['LINEAR']] = None
    intervalInSeconds: Optional[int] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'get_scene' function.
class GetSceneRequest(BaseValidatorModel):
    workspaceId: str
    sceneId: str


class SceneError(BaseValidatorModel):
    code: Optional[Literal['MATTERPORT_ERROR']] = None
    message: Optional[str] = None


# This class is the input for the 'get_sync_job' function.
class GetSyncJobRequest(BaseValidatorModel):
    syncSource: str
    workspaceId: Optional[str] = None


# This class is the input for the 'get_workspace' function.
class GetWorkspaceRequest(BaseValidatorModel):
    workspaceId: str


class ListComponentTypesFilter(BaseValidatorModel):
    extendsFrom: Optional[str] = None
    namespace: Optional[str] = None
    isAbstract: Optional[bool] = None


# This class is the input for the 'list_components' function.
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


# This class is the input for the 'list_properties' function.
class ListPropertiesRequest(BaseValidatorModel):
    workspaceId: str
    entityId: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_scenes' function.
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


# This class is the input for the 'list_sync_jobs' function.
class ListSyncJobsRequest(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SyncResourceFilter(BaseValidatorModel):
    state: Optional[SyncResourceStateType] = None
    resourceType: Optional[SyncResourceTypeType] = None
    resourceId: Optional[str] = None
    externalId: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_workspaces' function.
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
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: List[str]


# This class is the input for the 'update_pricing_plan' function.
class UpdatePricingPlanRequest(BaseValidatorModel):
    pricingMode: PricingModeType
    bundleNames: Optional[List[str]] = None


# This class is the input for the 'update_scene' function.
class UpdateSceneRequest(BaseValidatorModel):
    workspaceId: str
    sceneId: str
    contentLocation: Optional[str] = None
    description: Optional[str] = None
    capabilities: Optional[List[str]] = None
    sceneMetadata: Optional[Dict[str, str]] = None


# This class is the input for the 'update_workspace' function.
class UpdateWorkspaceRequest(BaseValidatorModel):
    workspaceId: str
    description: Optional[str] = None
    role: Optional[str] = None
    s3Location: Optional[str] = None


# This class is the output for the 'create_component_type' function.
class CreateComponentTypeResponse(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_entity' function.
class CreateEntityResponse(BaseValidatorModel):
    entityId: str
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_scene' function.
class CreateSceneResponse(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_sync_job' function.
class CreateSyncJobResponse(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_workspace' function.
class CreateWorkspaceResponse(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_component_type' function.
class DeleteComponentTypeResponse(BaseValidatorModel):
    state: StateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_entity' function.
class DeleteEntityResponse(BaseValidatorModel):
    state: StateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_sync_job' function.
class DeleteSyncJobResponse(BaseValidatorModel):
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_workspace' function.
class DeleteWorkspaceResponse(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_workspace' function.
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


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_component_type' function.
class UpdateComponentTypeResponse(BaseValidatorModel):
    workspaceId: str
    arn: str
    componentTypeId: str
    state: StateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_entity' function.
class UpdateEntityResponse(BaseValidatorModel):
    updateDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_scene' function.
class UpdateSceneResponse(BaseValidatorModel):
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_workspace' function.
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


class DataConnector(BaseValidatorModel):
    lambda_:Optional[LambdaFunction] = None
    isNative: Optional[bool] = None


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
    listValue: Optional[List[Dict[str, Any]]] = None
    mapValue: Optional[Dict[str, Dict[str, Any]]] = None
    relationshipValue: Optional[RelationshipValue] = None
    expression: Optional[str] = None


class DestinationConfiguration(BaseValidatorModel):
    type: DestinationTypeType
    s3Configuration: Optional[S3DestinationConfiguration] = None
    iotTwinMakerConfiguration: Optional[IotTwinMakerDestinationConfiguration] = None

EntityPropertyReferenceUnion = Union[EntityPropertyReference, EntityPropertyReferenceOutput]


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


# This class is the output for the 'execute_query' function.
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


# This class is the output for the 'get_scene' function.
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


# This class is the input for the 'list_component_types' function.
class ListComponentTypesRequest(BaseValidatorModel):
    workspaceId: str
    filters: Optional[List[ListComponentTypesFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_entities' function.
class ListEntitiesRequest(BaseValidatorModel):
    workspaceId: str
    filters: Optional[List[ListEntitiesFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_metadata_transfer_jobs' function.
class ListMetadataTransferJobsRequest(BaseValidatorModel):
    sourceType: SourceTypeType
    destinationType: DestinationTypeType
    filters: Optional[List[ListMetadataTransferJobsFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'list_scenes' function.
class ListScenesResponse(BaseValidatorModel):
    sceneSummaries: List[SceneSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'list_sync_resources' function.
class ListSyncResourcesRequest(BaseValidatorModel):
    workspaceId: str
    syncSource: str
    filters: Optional[List[SyncResourceFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_workspaces' function.
class ListWorkspacesResponse(BaseValidatorModel):
    workspaceSummaries: List[WorkspaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetPricingPlanResponse(BaseValidatorModel):
    currentPricingPlan: PricingPlan
    pendingPricingPlan: PricingPlan
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pricing_plan' function.
class UpdatePricingPlanResponse(BaseValidatorModel):
    currentPricingPlan: PricingPlan
    pendingPricingPlan: PricingPlan
    ResponseMetadata: ResponseMetadata


class FunctionRequest(BaseValidatorModel):
    requiredProperties: Optional[List[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnector] = None


class FunctionResponse(BaseValidatorModel):
    requiredProperties: Optional[List[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnector] = None
    isInherited: Optional[bool] = None


class DataTypeOutput(BaseValidatorModel):
    type: TypeType
    nestedType: Optional[Dict[str, Any]] = None
    allowedValues: Optional[List[DataValueOutput]] = None
    unitOfMeasure: Optional[str] = None
    relationship: Optional[Relationship] = None


class PropertyLatestValue(BaseValidatorModel):
    propertyReference: EntityPropertyReferenceOutput
    propertyValue: Optional[DataValueOutput] = None


class PropertyValueOutput(BaseValidatorModel):
    value: DataValueOutput
    timestamp: Optional[datetime] = None
    time: Optional[str] = None

DataValueUnion = Union[DataValue, DataValueOutput]


# This class is the output for the 'cancel_metadata_transfer_job' function.
class CancelMetadataTransferJobResponse(BaseValidatorModel):
    metadataTransferJobId: str
    arn: str
    updateDateTime: datetime
    status: MetadataTransferJobStatus
    progress: MetadataTransferJobProgress
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_metadata_transfer_job' function.
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


# This class is the output for the 'get_sync_job' function.
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
    filters: Optional[List[IotSiteWiseSourceConfigurationFilter]] = None


class IotTwinMakerSourceConfigurationOutput(BaseValidatorModel):
    workspace: str
    filters: Optional[List[IotTwinMakerSourceConfigurationFilter]] = None


class IotTwinMakerSourceConfiguration(BaseValidatorModel):
    workspace: str
    filters: Optional[List[IotTwinMakerSourceConfigurationFilter]] = None


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


# This class is the output for the 'get_property_value' function.
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


class DataType(BaseValidatorModel):
    type: TypeType
    nestedType: Optional[Dict[str, Any]] = None
    allowedValues: Optional[List[DataValueUnion]] = None
    unitOfMeasure: Optional[str] = None
    relationship: Optional[Relationship] = None


class PropertyFilter(BaseValidatorModel):
    propertyName: Optional[str] = None
    operator: Optional[str] = None
    value: Optional[DataValueUnion] = None


class PropertyValue(BaseValidatorModel):
    value: DataValueUnion
    timestamp: Optional[Timestamp] = None
    time: Optional[str] = None


# This class is the output for the 'list_metadata_transfer_jobs' function.
class ListMetadataTransferJobsResponse(BaseValidatorModel):
    metadataTransferJobSummaries: List[MetadataTransferJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_components' function.
class ListComponentsResponse(BaseValidatorModel):
    componentSummaries: List[ComponentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_component_types' function.
class ListComponentTypesResponse(BaseValidatorModel):
    workspaceId: str
    componentTypeSummaries: List[ComponentTypeSummary]
    maxResults: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_entities' function.
class ListEntitiesResponse(BaseValidatorModel):
    entitySummaries: List[EntitySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sync_jobs' function.
class ListSyncJobsResponse(BaseValidatorModel):
    syncJobSummaries: List[SyncJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sync_resources' function.
class ListSyncResourcesResponse(BaseValidatorModel):
    syncResources: List[SyncResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

IotSiteWiseSourceConfigurationUnion = Union[IotSiteWiseSourceConfiguration, IotSiteWiseSourceConfigurationOutput]


class SourceConfigurationOutput(BaseValidatorModel):
    type: SourceTypeType
    s3Configuration: Optional[S3SourceConfiguration] = None
    iotSiteWiseConfiguration: Optional[IotSiteWiseSourceConfigurationOutput] = None
    iotTwinMakerConfiguration: Optional[IotTwinMakerSourceConfigurationOutput] = None

IotTwinMakerSourceConfigurationUnion = Union[IotTwinMakerSourceConfiguration, IotTwinMakerSourceConfigurationOutput]


# This class is the output for the 'get_component_type' function.
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


# This class is the output for the 'get_property_value_history' function.
class GetPropertyValueHistoryResponse(BaseValidatorModel):
    propertyValues: List[PropertyValueHistory]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

DataTypeUnion = Union[DataType, DataTypeOutput]


# This class is the input for the 'get_property_value_history' function.
class GetPropertyValueHistoryRequest(BaseValidatorModel):
    workspaceId: str
    selectedProperties: List[str]
    entityId: Optional[str] = None
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    componentTypeId: Optional[str] = None
    propertyFilters: Optional[List[PropertyFilter]] = None
    startDateTime: Optional[Timestamp] = None
    endDateTime: Optional[Timestamp] = None
    interpolation: Optional[InterpolationParameters] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    orderByTime: Optional[OrderByTimeType] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None


class TabularConditions(BaseValidatorModel):
    orderBy: Optional[List[OrderBy]] = None
    propertyFilters: Optional[List[PropertyFilter]] = None

PropertyValueUnion = Union[PropertyValue, PropertyValueOutput]


# This class is the output for the 'get_metadata_transfer_job' function.
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


class SourceConfiguration(BaseValidatorModel):
    type: SourceTypeType
    s3Configuration: Optional[S3SourceConfiguration] = None
    iotSiteWiseConfiguration: Optional[IotSiteWiseSourceConfigurationUnion] = None
    iotTwinMakerConfiguration: Optional[IotTwinMakerSourceConfigurationUnion] = None


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


# This class is the output for the 'list_properties' function.
class ListPropertiesResponse(BaseValidatorModel):
    propertySummaries: List[PropertySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchPutPropertyErrorEntry(BaseValidatorModel):
    errors: List[BatchPutPropertyError]


class PropertyDefinitionRequest(BaseValidatorModel):
    dataType: Optional[DataTypeUnion] = None
    isRequiredInEntity: Optional[bool] = None
    isExternalId: Optional[bool] = None
    isStoredExternally: Optional[bool] = None
    isTimeSeries: Optional[bool] = None
    defaultValue: Optional[DataValueUnion] = None
    configuration: Optional[Dict[str, str]] = None
    displayName: Optional[str] = None


# This class is the input for the 'get_property_value' function.
class GetPropertyValueRequest(BaseValidatorModel):
    selectedProperties: List[str]
    workspaceId: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    componentTypeId: Optional[str] = None
    entityId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    propertyGroupName: Optional[str] = None
    tabularConditions: Optional[TabularConditions] = None


class PropertyValueEntry(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceUnion
    propertyValues: Optional[List[PropertyValueUnion]] = None

SourceConfigurationUnion = Union[SourceConfiguration, SourceConfigurationOutput]


# This class is the output for the 'get_entity' function.
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


# This class is the output for the 'batch_put_property_values' function.
class BatchPutPropertyValuesResponse(BaseValidatorModel):
    errorEntries: List[BatchPutPropertyErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_component_type' function.
class CreateComponentTypeRequest(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str
    isSingleton: Optional[bool] = None
    description: Optional[str] = None
    propertyDefinitions: Optional[Dict[str, PropertyDefinitionRequest]] = None
    extendsFrom: Optional[List[str]] = None
    functions: Optional[Dict[str, FunctionRequest]] = None
    tags: Optional[Dict[str, str]] = None
    propertyGroups: Optional[Dict[str, PropertyGroupRequest]] = None
    componentTypeName: Optional[str] = None
    compositeComponentTypes: Optional[Dict[str, CompositeComponentTypeRequest]] = None


class PropertyRequest(BaseValidatorModel):
    definition: Optional[PropertyDefinitionRequest] = None
    value: Optional[DataValueUnion] = None
    updateType: Optional[PropertyUpdateTypeType] = None


# This class is the input for the 'update_component_type' function.
class UpdateComponentTypeRequest(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str
    isSingleton: Optional[bool] = None
    description: Optional[str] = None
    propertyDefinitions: Optional[Dict[str, PropertyDefinitionRequest]] = None
    extendsFrom: Optional[List[str]] = None
    functions: Optional[Dict[str, FunctionRequest]] = None
    propertyGroups: Optional[Dict[str, PropertyGroupRequest]] = None
    componentTypeName: Optional[str] = None
    compositeComponentTypes: Optional[Dict[str, CompositeComponentTypeRequest]] = None

PropertyValueEntryUnion = Union[PropertyValueEntry, PropertyValueEntryOutput]


# This class is the input for the 'create_metadata_transfer_job' function.
class CreateMetadataTransferJobRequest(BaseValidatorModel):
    sources: List[SourceConfigurationUnion]
    destination: DestinationConfiguration
    metadataTransferJobId: Optional[str] = None
    description: Optional[str] = None


class ComponentRequest(BaseValidatorModel):
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    properties: Optional[Dict[str, PropertyRequest]] = None
    propertyGroups: Optional[Dict[str, ComponentPropertyGroupRequest]] = None


class ComponentUpdateRequest(BaseValidatorModel):
    updateType: Optional[ComponentUpdateTypeType] = None
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    propertyUpdates: Optional[Dict[str, PropertyRequest]] = None
    propertyGroupUpdates: Optional[Dict[str, ComponentPropertyGroupRequest]] = None


class CompositeComponentRequest(BaseValidatorModel):
    description: Optional[str] = None
    properties: Optional[Dict[str, PropertyRequest]] = None
    propertyGroups: Optional[Dict[str, ComponentPropertyGroupRequest]] = None


class CompositeComponentUpdateRequest(BaseValidatorModel):
    updateType: Optional[ComponentUpdateTypeType] = None
    description: Optional[str] = None
    propertyUpdates: Optional[Dict[str, PropertyRequest]] = None
    propertyGroupUpdates: Optional[Dict[str, ComponentPropertyGroupRequest]] = None


# This class is the input for the 'batch_put_property_values' function.
class BatchPutPropertyValuesRequest(BaseValidatorModel):
    workspaceId: str
    entries: List[PropertyValueEntryUnion]


# This class is the input for the 'create_entity' function.
class CreateEntityRequest(BaseValidatorModel):
    workspaceId: str
    entityName: str
    entityId: Optional[str] = None
    description: Optional[str] = None
    components: Optional[Dict[str, ComponentRequest]] = None
    compositeComponents: Optional[Dict[str, CompositeComponentRequest]] = None
    parentEntityId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_entity' function.
class UpdateEntityRequest(BaseValidatorModel):
    workspaceId: str
    entityId: str
    entityName: Optional[str] = None
    description: Optional[str] = None
    componentUpdates: Optional[Dict[str, ComponentUpdateRequest]] = None
    compositeComponentUpdates: Optional[Dict[str, CompositeComponentUpdateRequest]] = None
    parentEntityUpdate: Optional[ParentEntityUpdateRequest] = None
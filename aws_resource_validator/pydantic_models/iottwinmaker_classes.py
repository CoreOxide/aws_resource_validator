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
from aws_resource_validator.pydantic_models.iottwinmaker_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BundleInformationTypeDef(BaseModel):
    bundleNames: List[str]
    pricingTier: Optional[PricingTierType] = None

class CancelMetadataTransferJobRequestRequestTypeDef(BaseModel):
    metadataTransferJobId: str

class MetadataTransferJobProgressTypeDef(BaseModel):
    totalCount: Optional[int] = None
    succeededCount: Optional[int] = None
    skippedCount: Optional[int] = None
    failedCount: Optional[int] = None

class ColumnDescriptionTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[ColumnTypeType] = None

class ComponentPropertyGroupRequestTypeDef(BaseModel):
    groupType: Optional[Literal["TABULAR"]] = None
    propertyNames: Optional[Sequence[str]] = None
    updateType: Optional[PropertyGroupUpdateTypeType] = None

class ComponentPropertyGroupResponseTypeDef(BaseModel):
    groupType: Literal["TABULAR"]
    propertyNames: List[str]
    isInherited: bool

class CompositeComponentTypeRequestTypeDef(BaseModel):
    componentTypeId: Optional[str] = None

class CompositeComponentTypeResponseTypeDef(BaseModel):
    componentTypeId: Optional[str] = None
    isInherited: Optional[bool] = None

class PropertyDefinitionRequestTypeDef(BaseModel):
    dataType: Optional["DataTypeTypeDef"] = None
    isRequiredInEntity: Optional[bool] = None
    isExternalId: Optional[bool] = None
    isStoredExternally: Optional[bool] = None
    isTimeSeries: Optional[bool] = None
    defaultValue: Optional["DataValueTypeDef"] = None
    configuration: Optional[Mapping[str, str]] = None
    displayName: Optional[str] = None

class PropertyGroupRequestTypeDef(BaseModel):
    groupType: Optional[Literal["TABULAR"]] = None
    propertyNames: Optional[Sequence[str]] = None

class CreateSceneRequestRequestTypeDef(BaseModel):
    workspaceId: str
    sceneId: str
    contentLocation: str
    description: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None
    sceneMetadata: Optional[Mapping[str, str]] = None

class CreateSyncJobRequestRequestTypeDef(BaseModel):
    workspaceId: str
    syncSource: str
    syncRole: str
    tags: Optional[Mapping[str, str]] = None

class CreateWorkspaceRequestRequestTypeDef(BaseModel):
    workspaceId: str
    description: Optional[str] = None
    s3Location: Optional[str] = None
    role: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class LambdaFunctionTypeDef(BaseModel):
    arn: str

class RelationshipTypeDef(BaseModel):
    targetComponentTypeId: Optional[str] = None
    relationshipType: Optional[str] = None

class RelationshipValueTypeDef(BaseModel):
    targetEntityId: Optional[str] = None
    targetComponentName: Optional[str] = None

class DeleteComponentTypeRequestRequestTypeDef(BaseModel):
    workspaceId: str
    componentTypeId: str

class DeleteEntityRequestRequestTypeDef(BaseModel):
    workspaceId: str
    entityId: str
    isRecursive: Optional[bool] = None

class DeleteSceneRequestRequestTypeDef(BaseModel):
    workspaceId: str
    sceneId: str

class DeleteSyncJobRequestRequestTypeDef(BaseModel):
    workspaceId: str
    syncSource: str

class DeleteWorkspaceRequestRequestTypeDef(BaseModel):
    workspaceId: str

class IotTwinMakerDestinationConfigurationTypeDef(BaseModel):
    workspace: str

class S3DestinationConfigurationTypeDef(BaseModel):
    location: str

class EntityPropertyReferenceOutputTypeDef(BaseModel):
    propertyName: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    externalIdProperty: Optional[Dict[str, str]] = None
    entityId: Optional[str] = None

class EntityPropertyReferenceTypeDef(BaseModel):
    propertyName: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    externalIdProperty: Optional[Mapping[str, str]] = None
    entityId: Optional[str] = None

class ErrorDetailsTypeDef(BaseModel):
    code: Optional[ErrorCodeType] = None
    message: Optional[str] = None

class ExecuteQueryRequestRequestTypeDef(BaseModel):
    workspaceId: str
    queryStatement: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RowTypeDef(BaseModel):
    rowData: Optional[List[Dict[str, Any]]] = None

class FilterByAssetModelTypeDef(BaseModel):
    assetModelId: Optional[str] = None
    assetModelExternalId: Optional[str] = None
    includeOffspring: Optional[bool] = None
    includeAssets: Optional[bool] = None

class FilterByAssetTypeDef(BaseModel):
    assetId: Optional[str] = None
    assetExternalId: Optional[str] = None
    includeOffspring: Optional[bool] = None
    includeAssetModel: Optional[bool] = None

class FilterByComponentTypeTypeDef(BaseModel):
    componentTypeId: str

class FilterByEntityTypeDef(BaseModel):
    entityId: str

class GetComponentTypeRequestRequestTypeDef(BaseModel):
    workspaceId: str
    componentTypeId: str

class PropertyDefinitionResponseTypeDef(BaseModel):
    dataType: "DataTypeOutputTypeDef"
    isTimeSeries: bool
    isRequiredInEntity: bool
    isExternalId: bool
    isStoredExternally: bool
    isImported: bool
    isFinal: bool
    isInherited: bool
    defaultValue: Optional["DataValueOutputTypeDef"] = None
    configuration: Optional[Dict[str, str]] = None
    displayName: Optional[str] = None

class PropertyGroupResponseTypeDef(BaseModel):
    groupType: Literal["TABULAR"]
    propertyNames: List[str]
    isInherited: bool

class GetEntityRequestRequestTypeDef(BaseModel):
    workspaceId: str
    entityId: str

class GetMetadataTransferJobRequestRequestTypeDef(BaseModel):
    metadataTransferJobId: str

class InterpolationParametersTypeDef(BaseModel):
    interpolationType: Optional[Literal["LINEAR"]] = None
    intervalInSeconds: Optional[int] = None

class PropertyFilterTypeDef(BaseModel):
    propertyName: Optional[str] = None
    operator: Optional[str] = None
    value: Optional["DataValueTypeDef"] = None

class GetSceneRequestRequestTypeDef(BaseModel):
    workspaceId: str
    sceneId: str

class SceneErrorTypeDef(BaseModel):
    code: Optional[Literal["MATTERPORT_ERROR"]] = None
    message: Optional[str] = None

class GetSyncJobRequestRequestTypeDef(BaseModel):
    syncSource: str
    workspaceId: Optional[str] = None

class GetWorkspaceRequestRequestTypeDef(BaseModel):
    workspaceId: str

class ListComponentTypesFilterTypeDef(BaseModel):
    extendsFrom: Optional[str] = None
    namespace: Optional[str] = None
    isAbstract: Optional[bool] = None

class ListComponentsRequestRequestTypeDef(BaseModel):
    workspaceId: str
    entityId: str
    componentPath: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEntitiesFilterTypeDef(BaseModel):
    parentEntityId: Optional[str] = None
    componentTypeId: Optional[str] = None
    externalId: Optional[str] = None

class ListMetadataTransferJobsFilterTypeDef(BaseModel):
    workspaceId: Optional[str] = None
    state: Optional[MetadataTransferJobStateType] = None

class ListPropertiesRequestRequestTypeDef(BaseModel):
    workspaceId: str
    entityId: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListScenesRequestRequestTypeDef(BaseModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SceneSummaryTypeDef(BaseModel):
    sceneId: str
    contentLocation: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: Optional[str] = None

class ListSyncJobsRequestRequestTypeDef(BaseModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SyncResourceFilterTypeDef(BaseModel):
    state: Optional[SyncResourceStateType] = None
    resourceType: Optional[SyncResourceTypeType] = None
    resourceId: Optional[str] = None
    externalId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkspacesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkspaceSummaryTypeDef(BaseModel):
    workspaceId: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: Optional[str] = None
    linkedServices: Optional[List[str]] = None

class OrderByTypeDef(BaseModel):
    propertyName: str
    order: Optional[OrderType] = None

class ParentEntityUpdateRequestTypeDef(BaseModel):
    updateType: ParentEntityUpdateTypeType
    parentEntityId: Optional[str] = None

class PropertyValueOutputTypeDef(BaseModel):
    value: "DataValueOutputTypeDef"
    timestamp: Optional[datetime] = None
    time: Optional[str] = None

class S3SourceConfigurationTypeDef(BaseModel):
    location: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdatePricingPlanRequestRequestTypeDef(BaseModel):
    pricingMode: PricingModeType
    bundleNames: Optional[Sequence[str]] = None

class UpdateSceneRequestRequestTypeDef(BaseModel):
    workspaceId: str
    sceneId: str
    contentLocation: Optional[str] = None
    description: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    sceneMetadata: Optional[Mapping[str, str]] = None

class UpdateWorkspaceRequestRequestTypeDef(BaseModel):
    workspaceId: str
    description: Optional[str] = None
    role: Optional[str] = None
    s3Location: Optional[str] = None

class CreateComponentTypeResponseTypeDef(BaseModel):
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntityResponseTypeDef(BaseModel):
    entityId: str
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSceneResponseTypeDef(BaseModel):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSyncJobResponseTypeDef(BaseModel):
    arn: str
    creationDateTime: datetime
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(BaseModel):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteComponentTypeResponseTypeDef(BaseModel):
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEntityResponseTypeDef(BaseModel):
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSyncJobResponseTypeDef(BaseModel):
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceResponseTypeDef(BaseModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkspaceResponseTypeDef(BaseModel):
    workspaceId: str
    arn: str
    description: str
    linkedServices: List[str]
    s3Location: str
    role: str
    creationDateTime: datetime
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateComponentTypeResponseTypeDef(BaseModel):
    workspaceId: str
    arn: str
    componentTypeId: str
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEntityResponseTypeDef(BaseModel):
    updateDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSceneResponseTypeDef(BaseModel):
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceResponseTypeDef(BaseModel):
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PricingPlanTypeDef(BaseModel):
    effectiveDateTime: datetime
    pricingMode: PricingModeType
    updateDateTime: datetime
    updateReason: UpdateReasonType
    billableEntityCount: Optional[int] = None
    bundleInformation: Optional[BundleInformationTypeDef] = None

class PropertyRequestTypeDef(BaseModel):
    definition: Optional[PropertyDefinitionRequestTypeDef] = None
    value: Optional["DataValueTypeDef"] = None
    updateType: Optional[PropertyUpdateTypeType] = None

class DataConnectorTypeDef(BaseModel):
    lambda: Optional[LambdaFunctionTypeDef] = None
    isNative: Optional[bool] = None

class DataTypeOutputTypeDef(BaseModel):
    type: TypeType
    nestedType: Optional[Dict[str, Any]] = None
    allowedValues: Optional[List["DataValueOutputTypeDef"]] = None
    unitOfMeasure: Optional[str] = None
    relationship: Optional[RelationshipTypeDef] = None

class DataTypeTypeDef(BaseModel):
    type: TypeType
    nestedType: Optional[Dict[str, Any]] = None
    allowedValues: Optional[Sequence["DataValueTypeDef"]] = None
    unitOfMeasure: Optional[str] = None
    relationship: Optional[RelationshipTypeDef] = None

class DataValueOutputTypeDef(BaseModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    integerValue: Optional[int] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None
    listValue: Optional[List[Dict[str, Any]]] = None
    mapValue: Optional[Dict[str, Dict[str, Any]]] = None
    relationshipValue: Optional[RelationshipValueTypeDef] = None
    expression: Optional[str] = None

class DataValueTypeDef(BaseModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    integerValue: Optional[int] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None
    listValue: Optional[Sequence[Dict[str, Any]]] = None
    mapValue: Optional[Mapping[str, Dict[str, Any]]] = None
    relationshipValue: Optional[RelationshipValueTypeDef] = None
    expression: Optional[str] = None

class DestinationConfigurationTypeDef(BaseModel):
    type: DestinationTypeType
    s3Configuration: Optional[S3DestinationConfigurationTypeDef] = None
    iotTwinMakerConfiguration: Optional[IotTwinMakerDestinationConfigurationTypeDef] = None

class PropertyLatestValueTypeDef(BaseModel):
    propertyReference: EntityPropertyReferenceOutputTypeDef
    propertyValue: Optional["DataValueOutputTypeDef"] = None

class MetadataTransferJobStatusTypeDef(BaseModel):
    state: Optional[MetadataTransferJobStateType] = None
    error: Optional[ErrorDetailsTypeDef] = None
    queuedPosition: Optional[int] = None

class StatusTypeDef(BaseModel):
    state: Optional[StateType] = None
    error: Optional[ErrorDetailsTypeDef] = None

class SyncJobStatusTypeDef(BaseModel):
    state: Optional[SyncJobStateType] = None
    error: Optional[ErrorDetailsTypeDef] = None

class SyncResourceStatusTypeDef(BaseModel):
    state: Optional[SyncResourceStateType] = None
    error: Optional[ErrorDetailsTypeDef] = None

class ExecuteQueryResponseTypeDef(BaseModel):
    columnDescriptions: List[ColumnDescriptionTypeDef]
    rows: List[RowTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IotSiteWiseSourceConfigurationFilterTypeDef(BaseModel):
    filterByAssetModel: Optional[FilterByAssetModelTypeDef] = None
    filterByAsset: Optional[FilterByAssetTypeDef] = None

class IotTwinMakerSourceConfigurationFilterTypeDef(BaseModel):
    filterByComponentType: Optional[FilterByComponentTypeTypeDef] = None
    filterByEntity: Optional[FilterByEntityTypeDef] = None

class PropertyResponseTypeDef(BaseModel):
    definition: Optional[PropertyDefinitionResponseTypeDef] = None
    value: Optional["DataValueOutputTypeDef"] = None
    areAllPropertyValuesReturned: Optional[bool] = None

class PropertySummaryTypeDef(BaseModel):
    propertyName: str
    definition: Optional[PropertyDefinitionResponseTypeDef] = None
    value: Optional["DataValueOutputTypeDef"] = None
    areAllPropertyValuesReturned: Optional[bool] = None

class GetPropertyValueHistoryRequestRequestTypeDef(BaseModel):
    workspaceId: str
    selectedProperties: Sequence[str]
    entityId: Optional[str] = None
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    componentTypeId: Optional[str] = None
    propertyFilters: Optional[Sequence[PropertyFilterTypeDef]] = None
    startDateTime: Optional[TimestampTypeDef] = None
    endDateTime: Optional[TimestampTypeDef] = None
    interpolation: Optional[InterpolationParametersTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    orderByTime: Optional[OrderByTimeType] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None

class PropertyValueTypeDef(BaseModel):
    value: "DataValueTypeDef"
    timestamp: Optional[TimestampTypeDef] = None
    time: Optional[str] = None

class GetSceneResponseTypeDef(BaseModel):
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
    error: SceneErrorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListComponentTypesRequestRequestTypeDef(BaseModel):
    workspaceId: str
    filters: Optional[Sequence[ListComponentTypesFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListEntitiesRequestRequestTypeDef(BaseModel):
    workspaceId: str
    filters: Optional[Sequence[ListEntitiesFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMetadataTransferJobsRequestRequestTypeDef(BaseModel):
    sourceType: SourceTypeType
    destinationType: DestinationTypeType
    filters: Optional[Sequence[ListMetadataTransferJobsFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListScenesResponseTypeDef(BaseModel):
    sceneSummaries: List[SceneSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSyncResourcesRequestRequestTypeDef(BaseModel):
    workspaceId: str
    syncSource: str
    filters: Optional[Sequence[SyncResourceFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkspacesResponseTypeDef(BaseModel):
    workspaceSummaries: List[WorkspaceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TabularConditionsTypeDef(BaseModel):
    orderBy: Optional[Sequence[OrderByTypeDef]] = None
    propertyFilters: Optional[Sequence[PropertyFilterTypeDef]] = None

class PropertyValueEntryOutputTypeDef(BaseModel):
    entityPropertyReference: EntityPropertyReferenceOutputTypeDef
    propertyValues: Optional[List[PropertyValueOutputTypeDef]] = None

class PropertyValueHistoryTypeDef(BaseModel):
    entityPropertyReference: EntityPropertyReferenceOutputTypeDef
    values: Optional[List[PropertyValueOutputTypeDef]] = None

class GetPricingPlanResponseTypeDef(BaseModel):
    currentPricingPlan: PricingPlanTypeDef
    pendingPricingPlan: PricingPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePricingPlanResponseTypeDef(BaseModel):
    currentPricingPlan: PricingPlanTypeDef
    pendingPricingPlan: PricingPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentRequestTypeDef(BaseModel):
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    properties: Optional[Mapping[str, PropertyRequestTypeDef]] = None
    propertyGroups: Optional[Mapping[str, ComponentPropertyGroupRequestTypeDef]] = None

class ComponentUpdateRequestTypeDef(BaseModel):
    updateType: Optional[ComponentUpdateTypeType] = None
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    propertyUpdates: Optional[Mapping[str, PropertyRequestTypeDef]] = None
    propertyGroupUpdates: Optional[Mapping[str, ComponentPropertyGroupRequestTypeDef]] = None

class CompositeComponentRequestTypeDef(BaseModel):
    description: Optional[str] = None
    properties: Optional[Mapping[str, PropertyRequestTypeDef]] = None
    propertyGroups: Optional[Mapping[str, ComponentPropertyGroupRequestTypeDef]] = None

class CompositeComponentUpdateRequestTypeDef(BaseModel):
    updateType: Optional[ComponentUpdateTypeType] = None
    description: Optional[str] = None
    propertyUpdates: Optional[Mapping[str, PropertyRequestTypeDef]] = None
    propertyGroupUpdates: Optional[Mapping[str, ComponentPropertyGroupRequestTypeDef]] = None

class FunctionRequestTypeDef(BaseModel):
    requiredProperties: Optional[Sequence[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnectorTypeDef] = None

class FunctionResponseTypeDef(BaseModel):
    requiredProperties: Optional[List[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnectorTypeDef] = None
    isInherited: Optional[bool] = None

class GetPropertyValueResponseTypeDef(BaseModel):
    propertyValues: Dict[str, PropertyLatestValueTypeDef]
    nextToken: str
    tabularPropertyValues: List[List[Dict[str, "DataValueOutputTypeDef"]]]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMetadataTransferJobResponseTypeDef(BaseModel):
    metadataTransferJobId: str
    arn: str
    updateDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    progress: MetadataTransferJobProgressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMetadataTransferJobResponseTypeDef(BaseModel):
    metadataTransferJobId: str
    arn: str
    creationDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MetadataTransferJobSummaryTypeDef(BaseModel):
    metadataTransferJobId: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    progress: Optional[MetadataTransferJobProgressTypeDef] = None

class ComponentSummaryTypeDef(BaseModel):
    componentName: str
    componentTypeId: str
    status: StatusTypeDef
    definedIn: Optional[str] = None
    description: Optional[str] = None
    propertyGroups: Optional[Dict[str, ComponentPropertyGroupResponseTypeDef]] = None
    syncSource: Optional[str] = None
    componentPath: Optional[str] = None

class ComponentTypeSummaryTypeDef(BaseModel):
    arn: str
    componentTypeId: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: Optional[str] = None
    status: Optional[StatusTypeDef] = None
    componentTypeName: Optional[str] = None

class EntitySummaryTypeDef(BaseModel):
    entityId: str
    entityName: str
    arn: str
    status: StatusTypeDef
    creationDateTime: datetime
    updateDateTime: datetime
    parentEntityId: Optional[str] = None
    description: Optional[str] = None
    hasChildEntities: Optional[bool] = None

class GetSyncJobResponseTypeDef(BaseModel):
    arn: str
    workspaceId: str
    syncSource: str
    syncRole: str
    status: SyncJobStatusTypeDef
    creationDateTime: datetime
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SyncJobSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    workspaceId: Optional[str] = None
    syncSource: Optional[str] = None
    status: Optional[SyncJobStatusTypeDef] = None
    creationDateTime: Optional[datetime] = None
    updateDateTime: Optional[datetime] = None

class SyncResourceSummaryTypeDef(BaseModel):
    resourceType: Optional[SyncResourceTypeType] = None
    externalId: Optional[str] = None
    resourceId: Optional[str] = None
    status: Optional[SyncResourceStatusTypeDef] = None
    updateDateTime: Optional[datetime] = None

class IotSiteWiseSourceConfigurationOutputTypeDef(BaseModel):
    filters: Optional[List[IotSiteWiseSourceConfigurationFilterTypeDef]] = None

class IotSiteWiseSourceConfigurationTypeDef(BaseModel):
    filters: Optional[Sequence[IotSiteWiseSourceConfigurationFilterTypeDef]] = None

class IotTwinMakerSourceConfigurationOutputTypeDef(BaseModel):
    workspace: str
    filters: Optional[List[IotTwinMakerSourceConfigurationFilterTypeDef]] = None

class IotTwinMakerSourceConfigurationTypeDef(BaseModel):
    workspace: str
    filters: Optional[Sequence[IotTwinMakerSourceConfigurationFilterTypeDef]] = None

class ListPropertiesResponseTypeDef(BaseModel):
    propertySummaries: List[PropertySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PropertyValueEntryTypeDef(BaseModel):
    entityPropertyReference: EntityPropertyReferenceTypeDef
    propertyValues: Optional[Sequence[PropertyValueTypeDef]] = None

class GetPropertyValueRequestRequestTypeDef(BaseModel):
    selectedProperties: Sequence[str]
    workspaceId: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    componentTypeId: Optional[str] = None
    entityId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    propertyGroupName: Optional[str] = None
    tabularConditions: Optional[TabularConditionsTypeDef] = None

class BatchPutPropertyErrorTypeDef(BaseModel):
    errorCode: str
    errorMessage: str
    entry: PropertyValueEntryOutputTypeDef

class GetPropertyValueHistoryResponseTypeDef(BaseModel):
    propertyValues: List[PropertyValueHistoryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntityRequestRequestTypeDef(BaseModel):
    workspaceId: str
    entityName: str
    entityId: Optional[str] = None
    description: Optional[str] = None
    components: Optional[Mapping[str, ComponentRequestTypeDef]] = None
    compositeComponents: Optional[Mapping[str, CompositeComponentRequestTypeDef]] = None
    parentEntityId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateEntityRequestRequestTypeDef(BaseModel):
    workspaceId: str
    entityId: str
    entityName: Optional[str] = None
    description: Optional[str] = None
    componentUpdates: Optional[Mapping[str, ComponentUpdateRequestTypeDef]] = None
    compositeComponentUpdates: Optional[       Mapping[str, CompositeComponentUpdateRequestTypeDef] = None
    parentEntityUpdate: Optional[ParentEntityUpdateRequestTypeDef] = None

class CreateComponentTypeRequestRequestTypeDef(BaseModel):
    workspaceId: str
    componentTypeId: str
    isSingleton: Optional[bool] = None
    description: Optional[str] = None
    propertyDefinitions: Optional[Mapping[str, PropertyDefinitionRequestTypeDef]] = None
    extendsFrom: Optional[Sequence[str]] = None
    functions: Optional[Mapping[str, FunctionRequestTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    propertyGroups: Optional[Mapping[str, PropertyGroupRequestTypeDef]] = None
    componentTypeName: Optional[str] = None
    compositeComponentTypes: Optional[Mapping[str, CompositeComponentTypeRequestTypeDef]] = None

class UpdateComponentTypeRequestRequestTypeDef(BaseModel):
    workspaceId: str
    componentTypeId: str
    isSingleton: Optional[bool] = None
    description: Optional[str] = None
    propertyDefinitions: Optional[Mapping[str, PropertyDefinitionRequestTypeDef]] = None
    extendsFrom: Optional[Sequence[str]] = None
    functions: Optional[Mapping[str, FunctionRequestTypeDef]] = None
    propertyGroups: Optional[Mapping[str, PropertyGroupRequestTypeDef]] = None
    componentTypeName: Optional[str] = None
    compositeComponentTypes: Optional[Mapping[str, CompositeComponentTypeRequestTypeDef]] = None

class GetComponentTypeResponseTypeDef(BaseModel):
    workspaceId: str
    isSingleton: bool
    componentTypeId: str
    description: str
    propertyDefinitions: Dict[str, PropertyDefinitionResponseTypeDef]
    extendsFrom: List[str]
    functions: Dict[str, FunctionResponseTypeDef]
    creationDateTime: datetime
    updateDateTime: datetime
    arn: str
    isAbstract: bool
    isSchemaInitialized: bool
    status: StatusTypeDef
    propertyGroups: Dict[str, PropertyGroupResponseTypeDef]
    syncSource: str
    componentTypeName: str
    compositeComponentTypes: Dict[str, CompositeComponentTypeResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMetadataTransferJobsResponseTypeDef(BaseModel):
    metadataTransferJobSummaries: List[MetadataTransferJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentResponseTypeDef(BaseModel):
    componentName: Optional[str] = None
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    status: Optional[StatusTypeDef] = None
    definedIn: Optional[str] = None
    properties: Optional[Dict[str, PropertyResponseTypeDef]] = None
    propertyGroups: Optional[Dict[str, ComponentPropertyGroupResponseTypeDef]] = None
    syncSource: Optional[str] = None
    areAllPropertiesReturned: Optional[bool] = None
    compositeComponents: Optional[Dict[str, ComponentSummaryTypeDef]] = None
    areAllCompositeComponentsReturned: Optional[bool] = None

class ListComponentsResponseTypeDef(BaseModel):
    componentSummaries: List[ComponentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListComponentTypesResponseTypeDef(BaseModel):
    workspaceId: str
    componentTypeSummaries: List[ComponentTypeSummaryTypeDef]
    nextToken: str
    maxResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesResponseTypeDef(BaseModel):
    entitySummaries: List[EntitySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSyncJobsResponseTypeDef(BaseModel):
    syncJobSummaries: List[SyncJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSyncResourcesResponseTypeDef(BaseModel):
    syncResources: List[SyncResourceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SourceConfigurationOutputTypeDef(BaseModel):
    type: SourceTypeType
    s3Configuration: Optional[S3SourceConfigurationTypeDef] = None
    iotSiteWiseConfiguration: Optional[IotSiteWiseSourceConfigurationOutputTypeDef] = None
    iotTwinMakerConfiguration: Optional[IotTwinMakerSourceConfigurationOutputTypeDef] = None

class SourceConfigurationTypeDef(BaseModel):
    type: SourceTypeType
    s3Configuration: Optional[S3SourceConfigurationTypeDef] = None
    iotSiteWiseConfiguration: Optional[IotSiteWiseSourceConfigurationTypeDef] = None
    iotTwinMakerConfiguration: Optional[IotTwinMakerSourceConfigurationTypeDef] = None

class BatchPutPropertyErrorEntryTypeDef(BaseModel):
    errors: List[BatchPutPropertyErrorTypeDef]

class GetEntityResponseTypeDef(BaseModel):
    entityId: str
    entityName: str
    arn: str
    status: StatusTypeDef
    workspaceId: str
    description: str
    components: Dict[str, ComponentResponseTypeDef]
    parentEntityId: str
    hasChildEntities: bool
    creationDateTime: datetime
    updateDateTime: datetime
    syncSource: str
    areAllComponentsReturned: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetMetadataTransferJobResponseTypeDef(BaseModel):
    metadataTransferJobId: str
    arn: str
    description: str
    sources: List[SourceConfigurationOutputTypeDef]
    destination: DestinationConfigurationTypeDef
    metadataTransferJobRole: str
    reportUrl: str
    creationDateTime: datetime
    updateDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    progress: MetadataTransferJobProgressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutPropertyValuesRequestRequestTypeDef(BaseModel):
    workspaceId: str
    entries: Sequence[PropertyValueEntryUnionTypeDef]

class BatchPutPropertyValuesResponseTypeDef(BaseModel):
    errorEntries: List[BatchPutPropertyErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMetadataTransferJobRequestRequestTypeDef(BaseModel):
    sources: Sequence[SourceConfigurationUnionTypeDef]
    destination: DestinationConfigurationTypeDef
    metadataTransferJobId: Optional[str] = None
    description: Optional[str] = None


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
from aws_resource_validator.pydantic_models.iottwinmaker_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BundleInformationTypeDef(BaseValidatorModel):
    bundleNames: List[str]
    pricingTier: Optional[PricingTierType] = None

class CancelMetadataTransferJobRequestRequestTypeDef(BaseValidatorModel):
    metadataTransferJobId: str

class MetadataTransferJobProgressTypeDef(BaseValidatorModel):
    totalCount: Optional[int] = None
    succeededCount: Optional[int] = None
    skippedCount: Optional[int] = None
    failedCount: Optional[int] = None

class ColumnDescriptionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[ColumnTypeType] = None

class ComponentPropertyGroupRequestTypeDef(BaseValidatorModel):
    groupType: Optional[Literal["TABULAR"]] = None
    propertyNames: Optional[Sequence[str]] = None
    updateType: Optional[PropertyGroupUpdateTypeType] = None

class ComponentPropertyGroupResponseTypeDef(BaseValidatorModel):
    groupType: Literal["TABULAR"]
    propertyNames: List[str]
    isInherited: bool

class CompositeComponentTypeRequestTypeDef(BaseValidatorModel):
    componentTypeId: Optional[str] = None

class CompositeComponentTypeResponseTypeDef(BaseValidatorModel):
    componentTypeId: Optional[str] = None
    isInherited: Optional[bool] = None

class PropertyDefinitionRequestTypeDef(BaseValidatorModel):
    dataType: Optional["DataTypeTypeDef"] = None
    isRequiredInEntity: Optional[bool] = None
    isExternalId: Optional[bool] = None
    isStoredExternally: Optional[bool] = None
    isTimeSeries: Optional[bool] = None
    defaultValue: Optional["DataValueTypeDef"] = None
    configuration: Optional[Mapping[str, str]] = None
    displayName: Optional[str] = None

class PropertyGroupRequestTypeDef(BaseValidatorModel):
    groupType: Optional[Literal["TABULAR"]] = None
    propertyNames: Optional[Sequence[str]] = None

class CreateSceneRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    sceneId: str
    contentLocation: str
    description: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None
    sceneMetadata: Optional[Mapping[str, str]] = None

class CreateSyncJobRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    syncSource: str
    syncRole: str
    tags: Optional[Mapping[str, str]] = None

class CreateWorkspaceRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    description: Optional[str] = None
    s3Location: Optional[str] = None
    role: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class LambdaFunctionTypeDef(BaseValidatorModel):
    arn: str

class RelationshipTypeDef(BaseValidatorModel):
    targetComponentTypeId: Optional[str] = None
    relationshipType: Optional[str] = None

class RelationshipValueTypeDef(BaseValidatorModel):
    targetEntityId: Optional[str] = None
    targetComponentName: Optional[str] = None

class DeleteComponentTypeRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str

class DeleteEntityRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityId: str
    isRecursive: Optional[bool] = None

class DeleteSceneRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    sceneId: str

class DeleteSyncJobRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    syncSource: str

class DeleteWorkspaceRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str

class IotTwinMakerDestinationConfigurationTypeDef(BaseValidatorModel):
    workspace: str

class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    location: str

class EntityPropertyReferenceOutputTypeDef(BaseValidatorModel):
    propertyName: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    externalIdProperty: Optional[Dict[str, str]] = None
    entityId: Optional[str] = None

class EntityPropertyReferenceTypeDef(BaseValidatorModel):
    propertyName: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    externalIdProperty: Optional[Mapping[str, str]] = None
    entityId: Optional[str] = None

class ErrorDetailsTypeDef(BaseValidatorModel):
    code: Optional[ErrorCodeType] = None
    message: Optional[str] = None

class ExecuteQueryRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    queryStatement: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RowTypeDef(BaseValidatorModel):
    rowData: Optional[List[Dict[str, Any]]] = None

class FilterByAssetModelTypeDef(BaseValidatorModel):
    assetModelId: Optional[str] = None
    assetModelExternalId: Optional[str] = None
    includeOffspring: Optional[bool] = None
    includeAssets: Optional[bool] = None

class FilterByAssetTypeDef(BaseValidatorModel):
    assetId: Optional[str] = None
    assetExternalId: Optional[str] = None
    includeOffspring: Optional[bool] = None
    includeAssetModel: Optional[bool] = None

class FilterByComponentTypeTypeDef(BaseValidatorModel):
    componentTypeId: str

class FilterByEntityTypeDef(BaseValidatorModel):
    entityId: str

class GetComponentTypeRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str

class PropertyDefinitionResponseTypeDef(BaseValidatorModel):
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

class PropertyGroupResponseTypeDef(BaseValidatorModel):
    groupType: Literal["TABULAR"]
    propertyNames: List[str]
    isInherited: bool

class GetEntityRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityId: str

class GetMetadataTransferJobRequestRequestTypeDef(BaseValidatorModel):
    metadataTransferJobId: str

class InterpolationParametersTypeDef(BaseValidatorModel):
    interpolationType: Optional[Literal["LINEAR"]] = None
    intervalInSeconds: Optional[int] = None

class PropertyFilterTypeDef(BaseValidatorModel):
    propertyName: Optional[str] = None
    operator: Optional[str] = None
    value: Optional["DataValueTypeDef"] = None

class GetSceneRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    sceneId: str

class SceneErrorTypeDef(BaseValidatorModel):
    code: Optional[Literal["MATTERPORT_ERROR"]] = None
    message: Optional[str] = None

class GetSyncJobRequestRequestTypeDef(BaseValidatorModel):
    syncSource: str
    workspaceId: Optional[str] = None

class GetWorkspaceRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str

class ListComponentTypesFilterTypeDef(BaseValidatorModel):
    extendsFrom: Optional[str] = None
    namespace: Optional[str] = None
    isAbstract: Optional[bool] = None

class ListComponentsRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityId: str
    componentPath: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEntitiesFilterTypeDef(BaseValidatorModel):
    parentEntityId: Optional[str] = None
    componentTypeId: Optional[str] = None
    externalId: Optional[str] = None

class ListMetadataTransferJobsFilterTypeDef(BaseValidatorModel):
    workspaceId: Optional[str] = None
    state: Optional[MetadataTransferJobStateType] = None

class ListPropertiesRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityId: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListScenesRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SceneSummaryTypeDef(BaseValidatorModel):
    sceneId: str
    contentLocation: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: Optional[str] = None

class ListSyncJobsRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SyncResourceFilterTypeDef(BaseValidatorModel):
    state: Optional[SyncResourceStateType] = None
    resourceType: Optional[SyncResourceTypeType] = None
    resourceId: Optional[str] = None
    externalId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkspacesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkspaceSummaryTypeDef(BaseValidatorModel):
    workspaceId: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: Optional[str] = None
    linkedServices: Optional[List[str]] = None

class OrderByTypeDef(BaseValidatorModel):
    propertyName: str
    order: Optional[OrderType] = None

class ParentEntityUpdateRequestTypeDef(BaseValidatorModel):
    updateType: ParentEntityUpdateTypeType
    parentEntityId: Optional[str] = None

class PropertyValueOutputTypeDef(BaseValidatorModel):
    value: "DataValueOutputTypeDef"
    timestamp: Optional[datetime] = None
    time: Optional[str] = None

class S3SourceConfigurationTypeDef(BaseValidatorModel):
    location: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdatePricingPlanRequestRequestTypeDef(BaseValidatorModel):
    pricingMode: PricingModeType
    bundleNames: Optional[Sequence[str]] = None

class UpdateSceneRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    sceneId: str
    contentLocation: Optional[str] = None
    description: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    sceneMetadata: Optional[Mapping[str, str]] = None

class UpdateWorkspaceRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    description: Optional[str] = None
    role: Optional[str] = None
    s3Location: Optional[str] = None

class CreateComponentTypeResponseTypeDef(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntityResponseTypeDef(BaseValidatorModel):
    entityId: str
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSceneResponseTypeDef(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSyncJobResponseTypeDef(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(BaseValidatorModel):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteComponentTypeResponseTypeDef(BaseValidatorModel):
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEntityResponseTypeDef(BaseValidatorModel):
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSyncJobResponseTypeDef(BaseValidatorModel):
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceResponseTypeDef(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkspaceResponseTypeDef(BaseValidatorModel):
    workspaceId: str
    arn: str
    description: str
    linkedServices: List[str]
    s3Location: str
    role: str
    creationDateTime: datetime
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateComponentTypeResponseTypeDef(BaseValidatorModel):
    workspaceId: str
    arn: str
    componentTypeId: str
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEntityResponseTypeDef(BaseValidatorModel):
    updateDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSceneResponseTypeDef(BaseValidatorModel):
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceResponseTypeDef(BaseValidatorModel):
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PricingPlanTypeDef(BaseValidatorModel):
    effectiveDateTime: datetime
    pricingMode: PricingModeType
    updateDateTime: datetime
    updateReason: UpdateReasonType
    billableEntityCount: Optional[int] = None
    bundleInformation: Optional[BundleInformationTypeDef] = None

class PropertyRequestTypeDef(BaseValidatorModel):
    definition: Optional[PropertyDefinitionRequestTypeDef] = None
    value: Optional["DataValueTypeDef"] = None
    updateType: Optional[PropertyUpdateTypeType] = None

class DataConnectorTypeDef(BaseValidatorModel):
    _lambda: Optional[LambdaFunctionTypeDef] = None
    isNative: Optional[bool] = None

class DataTypeOutputTypeDef(BaseValidatorModel):
    type: TypeType
    nestedType: Optional[Dict[str, Any]] = None
    allowedValues: Optional[List["DataValueOutputTypeDef"]] = None
    unitOfMeasure: Optional[str] = None
    relationship: Optional[RelationshipTypeDef] = None

class DataTypeTypeDef(BaseValidatorModel):
    type: TypeType
    nestedType: Optional[Dict[str, Any]] = None
    allowedValues: Optional[Sequence["DataValueTypeDef"]] = None
    unitOfMeasure: Optional[str] = None
    relationship: Optional[RelationshipTypeDef] = None

class DataValueOutputTypeDef(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    integerValue: Optional[int] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None
    listValue: Optional[List[Dict[str, Any]]] = None
    mapValue: Optional[Dict[str, Dict[str, Any]]] = None
    relationshipValue: Optional[RelationshipValueTypeDef] = None
    expression: Optional[str] = None

class DataValueTypeDef(BaseValidatorModel):
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    integerValue: Optional[int] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None
    listValue: Optional[Sequence[Dict[str, Any]]] = None
    mapValue: Optional[Mapping[str, Dict[str, Any]]] = None
    relationshipValue: Optional[RelationshipValueTypeDef] = None
    expression: Optional[str] = None

class DestinationConfigurationTypeDef(BaseValidatorModel):
    type: DestinationTypeType
    s3Configuration: Optional[S3DestinationConfigurationTypeDef] = None
    iotTwinMakerConfiguration: Optional[IotTwinMakerDestinationConfigurationTypeDef] = None

class PropertyLatestValueTypeDef(BaseValidatorModel):
    propertyReference: EntityPropertyReferenceOutputTypeDef
    propertyValue: Optional["DataValueOutputTypeDef"] = None

class MetadataTransferJobStatusTypeDef(BaseValidatorModel):
    state: Optional[MetadataTransferJobStateType] = None
    error: Optional[ErrorDetailsTypeDef] = None
    queuedPosition: Optional[int] = None

class StatusTypeDef(BaseValidatorModel):
    state: Optional[StateType] = None
    error: Optional[ErrorDetailsTypeDef] = None

class SyncJobStatusTypeDef(BaseValidatorModel):
    state: Optional[SyncJobStateType] = None
    error: Optional[ErrorDetailsTypeDef] = None

class SyncResourceStatusTypeDef(BaseValidatorModel):
    state: Optional[SyncResourceStateType] = None
    error: Optional[ErrorDetailsTypeDef] = None

class ExecuteQueryResponseTypeDef(BaseValidatorModel):
    columnDescriptions: List[ColumnDescriptionTypeDef]
    rows: List[RowTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IotSiteWiseSourceConfigurationFilterTypeDef(BaseValidatorModel):
    filterByAssetModel: Optional[FilterByAssetModelTypeDef] = None
    filterByAsset: Optional[FilterByAssetTypeDef] = None

class IotTwinMakerSourceConfigurationFilterTypeDef(BaseValidatorModel):
    filterByComponentType: Optional[FilterByComponentTypeTypeDef] = None
    filterByEntity: Optional[FilterByEntityTypeDef] = None

class PropertyResponseTypeDef(BaseValidatorModel):
    definition: Optional[PropertyDefinitionResponseTypeDef] = None
    value: Optional["DataValueOutputTypeDef"] = None
    areAllPropertyValuesReturned: Optional[bool] = None

class PropertySummaryTypeDef(BaseValidatorModel):
    propertyName: str
    definition: Optional[PropertyDefinitionResponseTypeDef] = None
    value: Optional["DataValueOutputTypeDef"] = None
    areAllPropertyValuesReturned: Optional[bool] = None

class GetPropertyValueHistoryRequestRequestTypeDef(BaseValidatorModel):
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

class PropertyValueTypeDef(BaseValidatorModel):
    value: "DataValueTypeDef"
    timestamp: Optional[TimestampTypeDef] = None
    time: Optional[str] = None

class GetSceneResponseTypeDef(BaseValidatorModel):
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

class ListComponentTypesRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    filters: Optional[Sequence[ListComponentTypesFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListEntitiesRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    filters: Optional[Sequence[ListEntitiesFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMetadataTransferJobsRequestRequestTypeDef(BaseValidatorModel):
    sourceType: SourceTypeType
    destinationType: DestinationTypeType
    filters: Optional[Sequence[ListMetadataTransferJobsFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListScenesResponseTypeDef(BaseValidatorModel):
    sceneSummaries: List[SceneSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSyncResourcesRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    syncSource: str
    filters: Optional[Sequence[SyncResourceFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkspacesResponseTypeDef(BaseValidatorModel):
    workspaceSummaries: List[WorkspaceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TabularConditionsTypeDef(BaseValidatorModel):
    orderBy: Optional[Sequence[OrderByTypeDef]] = None
    propertyFilters: Optional[Sequence[PropertyFilterTypeDef]] = None

class PropertyValueEntryOutputTypeDef(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceOutputTypeDef
    propertyValues: Optional[List[PropertyValueOutputTypeDef]] = None

class PropertyValueHistoryTypeDef(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceOutputTypeDef
    values: Optional[List[PropertyValueOutputTypeDef]] = None

class GetPricingPlanResponseTypeDef(BaseValidatorModel):
    currentPricingPlan: PricingPlanTypeDef
    pendingPricingPlan: PricingPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePricingPlanResponseTypeDef(BaseValidatorModel):
    currentPricingPlan: PricingPlanTypeDef
    pendingPricingPlan: PricingPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentRequestTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    properties: Optional[Mapping[str, PropertyRequestTypeDef]] = None
    propertyGroups: Optional[Mapping[str, ComponentPropertyGroupRequestTypeDef]] = None

class ComponentUpdateRequestTypeDef(BaseValidatorModel):
    updateType: Optional[ComponentUpdateTypeType] = None
    description: Optional[str] = None
    componentTypeId: Optional[str] = None
    propertyUpdates: Optional[Mapping[str, PropertyRequestTypeDef]] = None
    propertyGroupUpdates: Optional[Mapping[str, ComponentPropertyGroupRequestTypeDef]] = None

class CompositeComponentRequestTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    properties: Optional[Mapping[str, PropertyRequestTypeDef]] = None
    propertyGroups: Optional[Mapping[str, ComponentPropertyGroupRequestTypeDef]] = None

class CompositeComponentUpdateRequestTypeDef(BaseValidatorModel):
    updateType: Optional[ComponentUpdateTypeType] = None
    description: Optional[str] = None
    propertyUpdates: Optional[Mapping[str, PropertyRequestTypeDef]] = None
    propertyGroupUpdates: Optional[Mapping[str, ComponentPropertyGroupRequestTypeDef]] = None

class FunctionRequestTypeDef(BaseValidatorModel):
    requiredProperties: Optional[Sequence[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnectorTypeDef] = None

class FunctionResponseTypeDef(BaseValidatorModel):
    requiredProperties: Optional[List[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnectorTypeDef] = None
    isInherited: Optional[bool] = None

class GetPropertyValueResponseTypeDef(BaseValidatorModel):
    propertyValues: Dict[str, PropertyLatestValueTypeDef]
    nextToken: str
    tabularPropertyValues: List[List[Dict[str, "DataValueOutputTypeDef"]]]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMetadataTransferJobResponseTypeDef(BaseValidatorModel):
    metadataTransferJobId: str
    arn: str
    updateDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    progress: MetadataTransferJobProgressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMetadataTransferJobResponseTypeDef(BaseValidatorModel):
    metadataTransferJobId: str
    arn: str
    creationDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MetadataTransferJobSummaryTypeDef(BaseValidatorModel):
    metadataTransferJobId: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    progress: Optional[MetadataTransferJobProgressTypeDef] = None

class ComponentSummaryTypeDef(BaseValidatorModel):
    componentName: str
    componentTypeId: str
    status: StatusTypeDef
    definedIn: Optional[str] = None
    description: Optional[str] = None
    propertyGroups: Optional[Dict[str, ComponentPropertyGroupResponseTypeDef]] = None
    syncSource: Optional[str] = None
    componentPath: Optional[str] = None

class ComponentTypeSummaryTypeDef(BaseValidatorModel):
    arn: str
    componentTypeId: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: Optional[str] = None
    status: Optional[StatusTypeDef] = None
    componentTypeName: Optional[str] = None

class EntitySummaryTypeDef(BaseValidatorModel):
    entityId: str
    entityName: str
    arn: str
    status: StatusTypeDef
    creationDateTime: datetime
    updateDateTime: datetime
    parentEntityId: Optional[str] = None
    description: Optional[str] = None
    hasChildEntities: Optional[bool] = None

class GetSyncJobResponseTypeDef(BaseValidatorModel):
    arn: str
    workspaceId: str
    syncSource: str
    syncRole: str
    status: SyncJobStatusTypeDef
    creationDateTime: datetime
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SyncJobSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    workspaceId: Optional[str] = None
    syncSource: Optional[str] = None
    status: Optional[SyncJobStatusTypeDef] = None
    creationDateTime: Optional[datetime] = None
    updateDateTime: Optional[datetime] = None

class SyncResourceSummaryTypeDef(BaseValidatorModel):
    resourceType: Optional[SyncResourceTypeType] = None
    externalId: Optional[str] = None
    resourceId: Optional[str] = None
    status: Optional[SyncResourceStatusTypeDef] = None
    updateDateTime: Optional[datetime] = None

class IotSiteWiseSourceConfigurationOutputTypeDef(BaseValidatorModel):
    filters: Optional[List[IotSiteWiseSourceConfigurationFilterTypeDef]] = None

class IotSiteWiseSourceConfigurationTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[IotSiteWiseSourceConfigurationFilterTypeDef]] = None

class IotTwinMakerSourceConfigurationOutputTypeDef(BaseValidatorModel):
    workspace: str
    filters: Optional[List[IotTwinMakerSourceConfigurationFilterTypeDef]] = None

class IotTwinMakerSourceConfigurationTypeDef(BaseValidatorModel):
    workspace: str
    filters: Optional[Sequence[IotTwinMakerSourceConfigurationFilterTypeDef]] = None

class ListPropertiesResponseTypeDef(BaseValidatorModel):
    propertySummaries: List[PropertySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PropertyValueEntryTypeDef(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceTypeDef
    propertyValues: Optional[Sequence[PropertyValueTypeDef]] = None

class GetPropertyValueRequestRequestTypeDef(BaseValidatorModel):
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

class BatchPutPropertyErrorTypeDef(BaseValidatorModel):
    errorCode: str
    errorMessage: str
    entry: PropertyValueEntryOutputTypeDef

class GetPropertyValueHistoryResponseTypeDef(BaseValidatorModel):
    propertyValues: List[PropertyValueHistoryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntityRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityName: str
    entityId: Optional[str] = None
    description: Optional[str] = None
    components: Optional[Mapping[str, ComponentRequestTypeDef]] = None
    compositeComponents: Optional[Mapping[str, CompositeComponentRequestTypeDef]] = None
    parentEntityId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateEntityRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityId: str
    entityName: Optional[str] = None
    description: Optional[str] = None
    componentUpdates: Optional[Mapping[str, ComponentUpdateRequestTypeDef]] = None
    compositeComponentUpdates: Optional[       Mapping[str, CompositeComponentUpdateRequestTypeDef]] = None
    parentEntityUpdate: Optional[ParentEntityUpdateRequestTypeDef] = None

class CreateComponentTypeRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateComponentTypeRequestRequestTypeDef(BaseValidatorModel):
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

class GetComponentTypeResponseTypeDef(BaseValidatorModel):
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

class ListMetadataTransferJobsResponseTypeDef(BaseValidatorModel):
    metadataTransferJobSummaries: List[MetadataTransferJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentResponseTypeDef(BaseValidatorModel):
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

class ListComponentsResponseTypeDef(BaseValidatorModel):
    componentSummaries: List[ComponentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListComponentTypesResponseTypeDef(BaseValidatorModel):
    workspaceId: str
    componentTypeSummaries: List[ComponentTypeSummaryTypeDef]
    nextToken: str
    maxResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesResponseTypeDef(BaseValidatorModel):
    entitySummaries: List[EntitySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSyncJobsResponseTypeDef(BaseValidatorModel):
    syncJobSummaries: List[SyncJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSyncResourcesResponseTypeDef(BaseValidatorModel):
    syncResources: List[SyncResourceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SourceConfigurationOutputTypeDef(BaseValidatorModel):
    type: SourceTypeType
    s3Configuration: Optional[S3SourceConfigurationTypeDef] = None
    iotSiteWiseConfiguration: Optional[IotSiteWiseSourceConfigurationOutputTypeDef] = None
    iotTwinMakerConfiguration: Optional[IotTwinMakerSourceConfigurationOutputTypeDef] = None

class SourceConfigurationTypeDef(BaseValidatorModel):
    type: SourceTypeType
    s3Configuration: Optional[S3SourceConfigurationTypeDef] = None
    iotSiteWiseConfiguration: Optional[IotSiteWiseSourceConfigurationTypeDef] = None
    iotTwinMakerConfiguration: Optional[IotTwinMakerSourceConfigurationTypeDef] = None

class BatchPutPropertyErrorEntryTypeDef(BaseValidatorModel):
    errors: List[BatchPutPropertyErrorTypeDef]

class GetEntityResponseTypeDef(BaseValidatorModel):
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

class GetMetadataTransferJobResponseTypeDef(BaseValidatorModel):
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

class BatchPutPropertyValuesRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entries: Sequence[PropertyValueEntryUnionTypeDef]

class BatchPutPropertyValuesResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchPutPropertyErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMetadataTransferJobRequestRequestTypeDef(BaseValidatorModel):
    sources: Sequence[SourceConfigurationUnionTypeDef]
    destination: DestinationConfigurationTypeDef
    metadataTransferJobId: Optional[str] = None
    description: Optional[str] = None


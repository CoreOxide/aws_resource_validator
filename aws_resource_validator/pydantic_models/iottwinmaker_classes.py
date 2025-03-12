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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BundleInformationTypeDef(BaseValidatorModel):
    bundleNames: List[str]
    pricingTier: Optional[PricingTierType] = None


class CancelMetadataTransferJobRequestTypeDef(BaseValidatorModel):
    metadataTransferJobId: str


class MetadataTransferJobProgressTypeDef(BaseValidatorModel):
    totalCount: Optional[int] = None
    succeededCount: Optional[int] = None
    skippedCount: Optional[int] = None
    failedCount: Optional[int] = None


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


class PropertyGroupRequestTypeDef(BaseValidatorModel):
    groupType: Optional[Literal["TABULAR"]] = None
    propertyNames: Optional[Sequence[str]] = None


class CreateSceneRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    sceneId: str
    contentLocation: str
    description: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None
    sceneMetadata: Optional[Mapping[str, str]] = None


class CreateSyncJobRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    syncSource: str
    syncRole: str
    tags: Optional[Mapping[str, str]] = None


class CreateWorkspaceRequestTypeDef(BaseValidatorModel):
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


class DeleteComponentTypeRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str


class DeleteEntityRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityId: str
    isRecursive: Optional[bool] = None


class DeleteSceneRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    sceneId: str


class DeleteSyncJobRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    syncSource: str


class DeleteWorkspaceRequestTypeDef(BaseValidatorModel):
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


class ExecuteQueryRequestTypeDef(BaseValidatorModel):
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


class GetComponentTypeRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    componentTypeId: str


class PropertyGroupResponseTypeDef(BaseValidatorModel):
    groupType: Literal["TABULAR"]
    propertyNames: List[str]
    isInherited: bool


class GetEntityRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityId: str


class GetMetadataTransferJobRequestTypeDef(BaseValidatorModel):
    metadataTransferJobId: str


class InterpolationParametersTypeDef(BaseValidatorModel):
    interpolationType: Optional[Literal["LINEAR"]] = None
    intervalInSeconds: Optional[int] = None


class GetSceneRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    sceneId: str


class SceneErrorTypeDef(BaseValidatorModel):
    code: Optional[Literal["MATTERPORT_ERROR"]] = None
    message: Optional[str] = None


class GetSyncJobRequestTypeDef(BaseValidatorModel):
    syncSource: str
    workspaceId: Optional[str] = None


class GetWorkspaceRequestTypeDef(BaseValidatorModel):
    workspaceId: str


class ListComponentTypesFilterTypeDef(BaseValidatorModel):
    extendsFrom: Optional[str] = None
    namespace: Optional[str] = None
    isAbstract: Optional[bool] = None


class ListComponentsRequestTypeDef(BaseValidatorModel):
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


class ListPropertiesRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityId: str
    componentName: Optional[str] = None
    componentPath: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListScenesRequestTypeDef(BaseValidatorModel):
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


class ListSyncJobsRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SyncResourceFilterTypeDef(BaseValidatorModel):
    state: Optional[SyncResourceStateType] = None
    resourceType: Optional[SyncResourceTypeType] = None
    resourceId: Optional[str] = None
    externalId: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkspacesRequestTypeDef(BaseValidatorModel):
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


class S3SourceConfigurationTypeDef(BaseValidatorModel):
    location: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class UpdatePricingPlanRequestTypeDef(BaseValidatorModel):
    pricingMode: PricingModeType
    bundleNames: Optional[Sequence[str]] = None


class UpdateSceneRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    sceneId: str
    contentLocation: Optional[str] = None
    description: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    sceneMetadata: Optional[Mapping[str, str]] = None


class UpdateWorkspaceRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    listValue: Optional[Sequence[Mapping[str, Any]]] = None
    mapValue: Optional[Mapping[str, Mapping[str, Any]]] = None
    relationshipValue: Optional[RelationshipValueTypeDef] = None
    expression: Optional[str] = None


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


class ColumnDescriptionTypeDef(BaseValidatorModel):
    pass


class ExecuteQueryResponseTypeDef(BaseValidatorModel):
    columnDescriptions: List[ColumnDescriptionTypeDef]
    rows: List[RowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class IotSiteWiseSourceConfigurationFilterTypeDef(BaseValidatorModel):
    filterByAssetModel: Optional[FilterByAssetModelTypeDef] = None
    filterByAsset: Optional[FilterByAssetTypeDef] = None


class IotTwinMakerSourceConfigurationFilterTypeDef(BaseValidatorModel):
    filterByComponentType: Optional[FilterByComponentTypeTypeDef] = None
    filterByEntity: Optional[FilterByEntityTypeDef] = None


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


class ListComponentTypesRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    filters: Optional[Sequence[ListComponentTypesFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListEntitiesRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    filters: Optional[Sequence[ListEntitiesFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListMetadataTransferJobsRequestTypeDef(BaseValidatorModel):
    sourceType: SourceTypeType
    destinationType: DestinationTypeType
    filters: Optional[Sequence[ListMetadataTransferJobsFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListScenesResponseTypeDef(BaseValidatorModel):
    sceneSummaries: List[SceneSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSyncResourcesRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    syncSource: str
    filters: Optional[Sequence[SyncResourceFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkspacesResponseTypeDef(BaseValidatorModel):
    workspaceSummaries: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetPricingPlanResponseTypeDef(BaseValidatorModel):
    currentPricingPlan: PricingPlanTypeDef
    pendingPricingPlan: PricingPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePricingPlanResponseTypeDef(BaseValidatorModel):
    currentPricingPlan: PricingPlanTypeDef
    pendingPricingPlan: PricingPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DataConnectorTypeDef(BaseValidatorModel):
    pass


class FunctionRequestTypeDef(BaseValidatorModel):
    requiredProperties: Optional[Sequence[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnectorTypeDef] = None


class FunctionResponseTypeDef(BaseValidatorModel):
    requiredProperties: Optional[List[str]] = None
    scope: Optional[ScopeType] = None
    implementedBy: Optional[DataConnectorTypeDef] = None
    isInherited: Optional[bool] = None


class PropertyLatestValueTypeDef(BaseValidatorModel):
    propertyReference: EntityPropertyReferenceOutputTypeDef
    propertyValue: Optional[DataValueOutputTypeDef] = None


class PropertyValueOutputTypeDef(BaseValidatorModel):
    value: DataValueOutputTypeDef
    timestamp: Optional[datetime] = None
    time: Optional[str] = None


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


class DataTypeOutputTypeDef(BaseValidatorModel):
    pass


class PropertyDefinitionResponseTypeDef(BaseValidatorModel):
    dataType: DataTypeOutputTypeDef
    isTimeSeries: bool
    isRequiredInEntity: bool
    isExternalId: bool
    isStoredExternally: bool
    isImported: bool
    isFinal: bool
    isInherited: bool
    defaultValue: Optional[DataValueOutputTypeDef] = None
    configuration: Optional[Dict[str, str]] = None
    displayName: Optional[str] = None


class GetPropertyValueResponseTypeDef(BaseValidatorModel):
    propertyValues: Dict[str, PropertyLatestValueTypeDef]
    tabularPropertyValues: List[List[Dict[str, DataValueOutputTypeDef]]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PropertyValueEntryOutputTypeDef(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceOutputTypeDef
    propertyValues: Optional[List[PropertyValueOutputTypeDef]] = None


class PropertyValueHistoryTypeDef(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceOutputTypeDef
    values: Optional[List[PropertyValueOutputTypeDef]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DataValueUnionTypeDef(BaseValidatorModel):
    pass


class PropertyValueTypeDef(BaseValidatorModel):
    value: DataValueUnionTypeDef
    timestamp: Optional[TimestampTypeDef] = None
    time: Optional[str] = None


class ListMetadataTransferJobsResponseTypeDef(BaseValidatorModel):
    metadataTransferJobSummaries: List[MetadataTransferJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListComponentsResponseTypeDef(BaseValidatorModel):
    componentSummaries: List[ComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListComponentTypesResponseTypeDef(BaseValidatorModel):
    workspaceId: str
    componentTypeSummaries: List[ComponentTypeSummaryTypeDef]
    maxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListEntitiesResponseTypeDef(BaseValidatorModel):
    entitySummaries: List[EntitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSyncJobsResponseTypeDef(BaseValidatorModel):
    syncJobSummaries: List[SyncJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSyncResourcesResponseTypeDef(BaseValidatorModel):
    syncResources: List[SyncResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class PropertyResponseTypeDef(BaseValidatorModel):
    definition: Optional[PropertyDefinitionResponseTypeDef] = None
    value: Optional[DataValueOutputTypeDef] = None
    areAllPropertyValuesReturned: Optional[bool] = None


class PropertySummaryTypeDef(BaseValidatorModel):
    propertyName: str
    definition: Optional[PropertyDefinitionResponseTypeDef] = None
    value: Optional[DataValueOutputTypeDef] = None
    areAllPropertyValuesReturned: Optional[bool] = None


class BatchPutPropertyErrorTypeDef(BaseValidatorModel):
    errorCode: str
    errorMessage: str
    entry: PropertyValueEntryOutputTypeDef


class GetPropertyValueHistoryResponseTypeDef(BaseValidatorModel):
    propertyValues: List[PropertyValueHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PropertyFilterTypeDef(BaseValidatorModel):
    pass


class GetPropertyValueHistoryRequestTypeDef(BaseValidatorModel):
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


class TabularConditionsTypeDef(BaseValidatorModel):
    orderBy: Optional[Sequence[OrderByTypeDef]] = None
    propertyFilters: Optional[Sequence[PropertyFilterTypeDef]] = None


class SourceConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class DestinationConfigurationTypeDef(BaseValidatorModel):
    pass


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


class ListPropertiesResponseTypeDef(BaseValidatorModel):
    propertySummaries: List[PropertySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchPutPropertyErrorEntryTypeDef(BaseValidatorModel):
    errors: List[BatchPutPropertyErrorTypeDef]


class DataTypeUnionTypeDef(BaseValidatorModel):
    pass


class PropertyDefinitionRequestTypeDef(BaseValidatorModel):
    dataType: Optional[DataTypeUnionTypeDef] = None
    isRequiredInEntity: Optional[bool] = None
    isExternalId: Optional[bool] = None
    isStoredExternally: Optional[bool] = None
    isTimeSeries: Optional[bool] = None
    defaultValue: Optional[DataValueUnionTypeDef] = None
    configuration: Optional[Mapping[str, str]] = None
    displayName: Optional[str] = None


class GetPropertyValueRequestTypeDef(BaseValidatorModel):
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


class EntityPropertyReferenceUnionTypeDef(BaseValidatorModel):
    pass


class PropertyValueUnionTypeDef(BaseValidatorModel):
    pass


class PropertyValueEntryTypeDef(BaseValidatorModel):
    entityPropertyReference: EntityPropertyReferenceUnionTypeDef
    propertyValues: Optional[Sequence[PropertyValueUnionTypeDef]] = None


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


class BatchPutPropertyValuesResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchPutPropertyErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateComponentTypeRequestTypeDef(BaseValidatorModel):
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


class PropertyRequestTypeDef(BaseValidatorModel):
    definition: Optional[PropertyDefinitionRequestTypeDef] = None
    value: Optional[DataValueUnionTypeDef] = None
    updateType: Optional[PropertyUpdateTypeType] = None


class UpdateComponentTypeRequestTypeDef(BaseValidatorModel):
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


class SourceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateMetadataTransferJobRequestTypeDef(BaseValidatorModel):
    sources: Sequence[SourceConfigurationUnionTypeDef]
    destination: DestinationConfigurationTypeDef
    metadataTransferJobId: Optional[str] = None
    description: Optional[str] = None


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


class PropertyValueEntryUnionTypeDef(BaseValidatorModel):
    pass


class BatchPutPropertyValuesRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entries: Sequence[PropertyValueEntryUnionTypeDef]


class CreateEntityRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityName: str
    entityId: Optional[str] = None
    description: Optional[str] = None
    components: Optional[Mapping[str, ComponentRequestTypeDef]] = None
    compositeComponents: Optional[Mapping[str, CompositeComponentRequestTypeDef]] = None
    parentEntityId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateEntityRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    entityId: str
    entityName: Optional[str] = None
    description: Optional[str] = None
    componentUpdates: Optional[Mapping[str, ComponentUpdateRequestTypeDef]] = None
    compositeComponentUpdates: Optional[Mapping[str, CompositeComponentUpdateRequestTypeDef]] = None
    parentEntityUpdate: Optional[ParentEntityUpdateRequestTypeDef] = None



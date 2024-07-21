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
from aws_resource_validator.pydantic_models.iotthingsgraph_constants import *

class AssociateEntityToThingRequestRequestTypeDef(BaseModel):
    thingName: str
    entityId: str
    namespaceVersion: Optional[int] = None

class DefinitionDocumentTypeDef(BaseModel):
    language: Literal["GRAPHQL"]
    text: str

class FlowTemplateSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    revisionNumber: Optional[int] = None
    createdAt: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class MetricsConfigurationTypeDef(BaseModel):
    cloudMetricEnabled: Optional[bool] = None
    metricRuleRoleArn: Optional[str] = None

class TagTypeDef(BaseModel):
    key: str
    value: str

class SystemInstanceSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[SystemInstanceDeploymentStatusType] = None
    target: Optional[DeploymentTargetType] = None
    greengrassGroupName: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    greengrassGroupId: Optional[str] = None
    greengrassGroupVersionId: Optional[str] = None

class SystemTemplateSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    revisionNumber: Optional[int] = None
    createdAt: Optional[datetime] = None

class DeleteFlowTemplateRequestRequestTypeDef(BaseModel):
    id: str

class DeleteSystemInstanceRequestRequestTypeDef(BaseModel):
    id: Optional[str] = None

class DeleteSystemTemplateRequestRequestTypeDef(BaseModel):
    id: str

class DependencyRevisionTypeDef(BaseModel):
    id: Optional[str] = None
    revisionNumber: Optional[int] = None

class DeploySystemInstanceRequestRequestTypeDef(BaseModel):
    id: Optional[str] = None

class DeprecateFlowTemplateRequestRequestTypeDef(BaseModel):
    id: str

class DeprecateSystemTemplateRequestRequestTypeDef(BaseModel):
    id: str

class DescribeNamespaceRequestRequestTypeDef(BaseModel):
    namespaceName: Optional[str] = None

class DissociateEntityFromThingRequestRequestTypeDef(BaseModel):
    thingName: str
    entityType: EntityTypeType

class EntityFilterTypeDef(BaseModel):
    name: Optional[EntityFilterNameType] = None
    value: Optional[Sequence[str]] = None

class FlowExecutionMessageTypeDef(BaseModel):
    messageId: Optional[str] = None
    eventType: Optional[FlowExecutionEventTypeType] = None
    timestamp: Optional[datetime] = None
    payload: Optional[str] = None

class FlowExecutionSummaryTypeDef(BaseModel):
    flowExecutionId: Optional[str] = None
    status: Optional[FlowExecutionStatusType] = None
    systemInstanceId: Optional[str] = None
    flowTemplateId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class FlowTemplateFilterTypeDef(BaseModel):
    name: Literal["DEVICE_MODEL_ID"]
    value: Sequence[str]

class GetEntitiesRequestRequestTypeDef(BaseModel):
    ids: Sequence[str]
    namespaceVersion: Optional[int] = None

class GetFlowTemplateRequestRequestTypeDef(BaseModel):
    id: str
    revisionNumber: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetFlowTemplateRevisionsRequestRequestTypeDef(BaseModel):
    id: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetSystemInstanceRequestRequestTypeDef(BaseModel):
    id: str

class GetSystemTemplateRequestRequestTypeDef(BaseModel):
    id: str
    revisionNumber: Optional[int] = None

class GetSystemTemplateRevisionsRequestRequestTypeDef(BaseModel):
    id: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetUploadStatusRequestRequestTypeDef(BaseModel):
    uploadId: str

class ListFlowExecutionMessagesRequestRequestTypeDef(BaseModel):
    flowExecutionId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SystemInstanceFilterTypeDef(BaseModel):
    name: Optional[SystemInstanceFilterNameType] = None
    value: Optional[Sequence[str]] = None

class SystemTemplateFilterTypeDef(BaseModel):
    name: Literal["FLOW_TEMPLATE_ID"]
    value: Sequence[str]

class SearchThingsRequestRequestTypeDef(BaseModel):
    entityId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None

class ThingTypeDef(BaseModel):
    thingArn: Optional[str] = None
    thingName: Optional[str] = None

class UndeploySystemInstanceRequestRequestTypeDef(BaseModel):
    id: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateFlowTemplateRequestRequestTypeDef(BaseModel):
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None

class CreateSystemTemplateRequestRequestTypeDef(BaseModel):
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None

class EntityDescriptionTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    type: Optional[EntityTypeType] = None
    createdAt: Optional[datetime] = None
    definition: Optional[DefinitionDocumentTypeDef] = None

class UpdateFlowTemplateRequestRequestTypeDef(BaseModel):
    id: str
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None

class UpdateSystemTemplateRequestRequestTypeDef(BaseModel):
    id: str
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None

class UploadEntityDefinitionsRequestRequestTypeDef(BaseModel):
    document: Optional[DefinitionDocumentTypeDef] = None
    syncWithPublicNamespace: Optional[bool] = None
    deprecateExistingEntities: Optional[bool] = None

class FlowTemplateDescriptionTypeDef(BaseModel):
    summary: Optional[FlowTemplateSummaryTypeDef] = None
    definition: Optional[DefinitionDocumentTypeDef] = None
    validatedNamespaceVersion: Optional[int] = None

class CreateFlowTemplateResponseTypeDef(BaseModel):
    summary: FlowTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNamespaceResponseTypeDef(BaseModel):
    namespaceArn: str
    namespaceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNamespaceResponseTypeDef(BaseModel):
    namespaceArn: str
    namespaceName: str
    trackingNamespaceName: str
    trackingNamespaceVersion: int
    namespaceVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowTemplateRevisionsResponseTypeDef(BaseModel):
    summaries: List[FlowTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamespaceDeletionStatusResponseTypeDef(BaseModel):
    namespaceArn: str
    namespaceName: str
    status: NamespaceDeletionStatusType
    errorCode: Literal["VALIDATION_FAILED"]
    errorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUploadStatusResponseTypeDef(BaseModel):
    uploadId: str
    uploadStatus: UploadStatusType
    namespaceArn: str
    namespaceName: str
    namespaceVersion: int
    failureReason: List[str]
    createdDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFlowTemplatesResponseTypeDef(BaseModel):
    summaries: List[FlowTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowTemplateResponseTypeDef(BaseModel):
    summary: FlowTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UploadEntityDefinitionsResponseTypeDef(BaseModel):
    uploadId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSystemInstanceRequestRequestTypeDef(BaseModel):
    definition: DefinitionDocumentTypeDef
    target: DeploymentTargetType
    tags: Optional[Sequence[TagTypeDef]] = None
    greengrassGroupName: Optional[str] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfigurationTypeDef] = None
    flowActionsRoleArn: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateSystemInstanceResponseTypeDef(BaseModel):
    summary: SystemInstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploySystemInstanceResponseTypeDef(BaseModel):
    summary: SystemInstanceSummaryTypeDef
    greengrassDeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSystemInstancesResponseTypeDef(BaseModel):
    summaries: List[SystemInstanceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UndeploySystemInstanceResponseTypeDef(BaseModel):
    summary: SystemInstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSystemTemplateResponseTypeDef(BaseModel):
    summary: SystemTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSystemTemplateRevisionsResponseTypeDef(BaseModel):
    summaries: List[SystemTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSystemTemplatesResponseTypeDef(BaseModel):
    summaries: List[SystemTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SystemTemplateDescriptionTypeDef(BaseModel):
    summary: Optional[SystemTemplateSummaryTypeDef] = None
    definition: Optional[DefinitionDocumentTypeDef] = None
    validatedNamespaceVersion: Optional[int] = None

class UpdateSystemTemplateResponseTypeDef(BaseModel):
    summary: SystemTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SystemInstanceDescriptionTypeDef(BaseModel):
    summary: Optional[SystemInstanceSummaryTypeDef] = None
    definition: Optional[DefinitionDocumentTypeDef] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfigurationTypeDef] = None
    validatedNamespaceVersion: Optional[int] = None
    validatedDependencyRevisions: Optional[List[DependencyRevisionTypeDef]] = None
    flowActionsRoleArn: Optional[str] = None

class SearchEntitiesRequestRequestTypeDef(BaseModel):
    entityTypes: Sequence[EntityTypeType]
    filters: Optional[Sequence[EntityFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None

class ListFlowExecutionMessagesResponseTypeDef(BaseModel):
    messages: List[FlowExecutionMessageTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFlowExecutionsResponseTypeDef(BaseModel):
    summaries: List[FlowExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFlowTemplatesRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[FlowTemplateFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetFlowTemplateRevisionsRequestGetFlowTemplateRevisionsPaginateTypeDef(BaseModel):
    id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSystemTemplateRevisionsRequestGetSystemTemplateRevisionsPaginateTypeDef(BaseModel):
    id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowExecutionMessagesRequestListFlowExecutionMessagesPaginateTypeDef(BaseModel):
    flowExecutionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchEntitiesRequestSearchEntitiesPaginateTypeDef(BaseModel):
    entityTypes: Sequence[EntityTypeType]
    filters: Optional[Sequence[EntityFilterTypeDef]] = None
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchFlowTemplatesRequestSearchFlowTemplatesPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FlowTemplateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchThingsRequestSearchThingsPaginateTypeDef(BaseModel):
    entityId: str
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchFlowExecutionsRequestRequestTypeDef(BaseModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SearchFlowExecutionsRequestSearchFlowExecutionsPaginateTypeDef(BaseModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSystemInstancesRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[SystemInstanceFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SearchSystemInstancesRequestSearchSystemInstancesPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[SystemInstanceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSystemTemplatesRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[SystemTemplateFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SearchSystemTemplatesRequestSearchSystemTemplatesPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[SystemTemplateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchThingsResponseTypeDef(BaseModel):
    things: List[ThingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEntitiesResponseTypeDef(BaseModel):
    descriptions: List[EntityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchEntitiesResponseTypeDef(BaseModel):
    descriptions: List[EntityDescriptionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowTemplateResponseTypeDef(BaseModel):
    description: FlowTemplateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSystemTemplateResponseTypeDef(BaseModel):
    description: SystemTemplateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSystemInstanceResponseTypeDef(BaseModel):
    description: SystemInstanceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


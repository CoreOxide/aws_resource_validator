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
from aws_resource_validator.pydantic_models.iotthingsgraph_constants import *

class AssociateEntityToThingRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    entityId: str
    namespaceVersion: Optional[int] = None

class DefinitionDocumentTypeDef(BaseValidatorModel):
    language: Literal["GRAPHQL"]
    text: str

class FlowTemplateSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    revisionNumber: Optional[int] = None
    createdAt: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class MetricsConfigurationTypeDef(BaseValidatorModel):
    cloudMetricEnabled: Optional[bool] = None
    metricRuleRoleArn: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class SystemInstanceSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[SystemInstanceDeploymentStatusType] = None
    target: Optional[DeploymentTargetType] = None
    greengrassGroupName: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    greengrassGroupId: Optional[str] = None
    greengrassGroupVersionId: Optional[str] = None

class SystemTemplateSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    revisionNumber: Optional[int] = None
    createdAt: Optional[datetime] = None

class DeleteFlowTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteSystemInstanceRequestRequestTypeDef(BaseValidatorModel):
    id: Optional[str] = None

class DeleteSystemTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DependencyRevisionTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    revisionNumber: Optional[int] = None

class DeploySystemInstanceRequestRequestTypeDef(BaseValidatorModel):
    id: Optional[str] = None

class DeprecateFlowTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeprecateSystemTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DescribeNamespaceRequestRequestTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None

class DissociateEntityFromThingRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    entityType: EntityTypeType

class EntityFilterTypeDef(BaseValidatorModel):
    name: Optional[EntityFilterNameType] = None
    value: Optional[Sequence[str]] = None

class FlowExecutionMessageTypeDef(BaseValidatorModel):
    messageId: Optional[str] = None
    eventType: Optional[FlowExecutionEventTypeType] = None
    timestamp: Optional[datetime] = None
    payload: Optional[str] = None

class FlowExecutionSummaryTypeDef(BaseValidatorModel):
    flowExecutionId: Optional[str] = None
    status: Optional[FlowExecutionStatusType] = None
    systemInstanceId: Optional[str] = None
    flowTemplateId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class FlowTemplateFilterTypeDef(BaseValidatorModel):
    name: Literal["DEVICE_MODEL_ID"]
    value: Sequence[str]

class GetEntitiesRequestRequestTypeDef(BaseValidatorModel):
    ids: Sequence[str]
    namespaceVersion: Optional[int] = None

class GetFlowTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str
    revisionNumber: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetFlowTemplateRevisionsRequestRequestTypeDef(BaseValidatorModel):
    id: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetSystemInstanceRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetSystemTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str
    revisionNumber: Optional[int] = None

class GetSystemTemplateRevisionsRequestRequestTypeDef(BaseValidatorModel):
    id: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetUploadStatusRequestRequestTypeDef(BaseValidatorModel):
    uploadId: str

class ListFlowExecutionMessagesRequestRequestTypeDef(BaseValidatorModel):
    flowExecutionId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SystemInstanceFilterTypeDef(BaseValidatorModel):
    name: Optional[SystemInstanceFilterNameType] = None
    value: Optional[Sequence[str]] = None

class SystemTemplateFilterTypeDef(BaseValidatorModel):
    name: Literal["FLOW_TEMPLATE_ID"]
    value: Sequence[str]

class SearchThingsRequestRequestTypeDef(BaseValidatorModel):
    entityId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None

class ThingTypeDef(BaseValidatorModel):
    thingArn: Optional[str] = None
    thingName: Optional[str] = None

class UndeploySystemInstanceRequestRequestTypeDef(BaseValidatorModel):
    id: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateFlowTemplateRequestRequestTypeDef(BaseValidatorModel):
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None

class CreateSystemTemplateRequestRequestTypeDef(BaseValidatorModel):
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None

class EntityDescriptionTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    type: Optional[EntityTypeType] = None
    createdAt: Optional[datetime] = None
    definition: Optional[DefinitionDocumentTypeDef] = None

class UpdateFlowTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None

class UpdateSystemTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None

class UploadEntityDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    document: Optional[DefinitionDocumentTypeDef] = None
    syncWithPublicNamespace: Optional[bool] = None
    deprecateExistingEntities: Optional[bool] = None

class FlowTemplateDescriptionTypeDef(BaseValidatorModel):
    summary: Optional[FlowTemplateSummaryTypeDef] = None
    definition: Optional[DefinitionDocumentTypeDef] = None
    validatedNamespaceVersion: Optional[int] = None

class CreateFlowTemplateResponseTypeDef(BaseValidatorModel):
    summary: FlowTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNamespaceResponseTypeDef(BaseValidatorModel):
    namespaceArn: str
    namespaceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNamespaceResponseTypeDef(BaseValidatorModel):
    namespaceArn: str
    namespaceName: str
    trackingNamespaceName: str
    trackingNamespaceVersion: int
    namespaceVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowTemplateRevisionsResponseTypeDef(BaseValidatorModel):
    summaries: List[FlowTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamespaceDeletionStatusResponseTypeDef(BaseValidatorModel):
    namespaceArn: str
    namespaceName: str
    status: NamespaceDeletionStatusType
    errorCode: Literal["VALIDATION_FAILED"]
    errorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUploadStatusResponseTypeDef(BaseValidatorModel):
    uploadId: str
    uploadStatus: UploadStatusType
    namespaceArn: str
    namespaceName: str
    namespaceVersion: int
    failureReason: List[str]
    createdDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFlowTemplatesResponseTypeDef(BaseValidatorModel):
    summaries: List[FlowTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowTemplateResponseTypeDef(BaseValidatorModel):
    summary: FlowTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UploadEntityDefinitionsResponseTypeDef(BaseValidatorModel):
    uploadId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSystemInstanceRequestRequestTypeDef(BaseValidatorModel):
    definition: DefinitionDocumentTypeDef
    target: DeploymentTargetType
    tags: Optional[Sequence[TagTypeDef]] = None
    greengrassGroupName: Optional[str] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfigurationTypeDef] = None
    flowActionsRoleArn: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateSystemInstanceResponseTypeDef(BaseValidatorModel):
    summary: SystemInstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploySystemInstanceResponseTypeDef(BaseValidatorModel):
    summary: SystemInstanceSummaryTypeDef
    greengrassDeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSystemInstancesResponseTypeDef(BaseValidatorModel):
    summaries: List[SystemInstanceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UndeploySystemInstanceResponseTypeDef(BaseValidatorModel):
    summary: SystemInstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSystemTemplateResponseTypeDef(BaseValidatorModel):
    summary: SystemTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSystemTemplateRevisionsResponseTypeDef(BaseValidatorModel):
    summaries: List[SystemTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSystemTemplatesResponseTypeDef(BaseValidatorModel):
    summaries: List[SystemTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SystemTemplateDescriptionTypeDef(BaseValidatorModel):
    summary: Optional[SystemTemplateSummaryTypeDef] = None
    definition: Optional[DefinitionDocumentTypeDef] = None
    validatedNamespaceVersion: Optional[int] = None

class UpdateSystemTemplateResponseTypeDef(BaseValidatorModel):
    summary: SystemTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SystemInstanceDescriptionTypeDef(BaseValidatorModel):
    summary: Optional[SystemInstanceSummaryTypeDef] = None
    definition: Optional[DefinitionDocumentTypeDef] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfigurationTypeDef] = None
    validatedNamespaceVersion: Optional[int] = None
    validatedDependencyRevisions: Optional[List[DependencyRevisionTypeDef]] = None
    flowActionsRoleArn: Optional[str] = None

class SearchEntitiesRequestRequestTypeDef(BaseValidatorModel):
    entityTypes: Sequence[EntityTypeType]
    filters: Optional[Sequence[EntityFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None

class ListFlowExecutionMessagesResponseTypeDef(BaseValidatorModel):
    messages: List[FlowExecutionMessageTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFlowExecutionsResponseTypeDef(BaseValidatorModel):
    summaries: List[FlowExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFlowTemplatesRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FlowTemplateFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetFlowTemplateRevisionsRequestGetFlowTemplateRevisionsPaginateTypeDef(BaseValidatorModel):
    id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSystemTemplateRevisionsRequestGetSystemTemplateRevisionsPaginateTypeDef(BaseValidatorModel):
    id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowExecutionMessagesRequestListFlowExecutionMessagesPaginateTypeDef(BaseValidatorModel):
    flowExecutionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchEntitiesRequestSearchEntitiesPaginateTypeDef(BaseValidatorModel):
    entityTypes: Sequence[EntityTypeType]
    filters: Optional[Sequence[EntityFilterTypeDef]] = None
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchFlowTemplatesRequestSearchFlowTemplatesPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FlowTemplateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchThingsRequestSearchThingsPaginateTypeDef(BaseValidatorModel):
    entityId: str
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchFlowExecutionsRequestRequestTypeDef(BaseValidatorModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SearchFlowExecutionsRequestSearchFlowExecutionsPaginateTypeDef(BaseValidatorModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSystemInstancesRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[SystemInstanceFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SearchSystemInstancesRequestSearchSystemInstancesPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[SystemInstanceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSystemTemplatesRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[SystemTemplateFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SearchSystemTemplatesRequestSearchSystemTemplatesPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[SystemTemplateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchThingsResponseTypeDef(BaseValidatorModel):
    things: List[ThingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEntitiesResponseTypeDef(BaseValidatorModel):
    descriptions: List[EntityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchEntitiesResponseTypeDef(BaseValidatorModel):
    descriptions: List[EntityDescriptionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowTemplateResponseTypeDef(BaseValidatorModel):
    description: FlowTemplateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSystemTemplateResponseTypeDef(BaseValidatorModel):
    description: SystemTemplateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSystemInstanceResponseTypeDef(BaseValidatorModel):
    description: SystemInstanceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


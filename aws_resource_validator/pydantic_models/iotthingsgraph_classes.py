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
from aws_resource_validator.pydantic_models.iotthingsgraph_constants import *

class AssociateEntityToThingRequestTypeDef(BaseValidatorModel):
    thingName: str
    entityId: str
    namespaceVersion: Optional[int] = None


class DefinitionDocumentTypeDef(BaseValidatorModel):
    language: Literal["GRAPHQL"]
    text: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MetricsConfigurationTypeDef(BaseValidatorModel):
    cloudMetricEnabled: Optional[bool] = None
    metricRuleRoleArn: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class DescribeNamespaceRequestTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None


class DissociateEntityFromThingRequestTypeDef(BaseValidatorModel):
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


class GetEntitiesRequestTypeDef(BaseValidatorModel):
    ids: Sequence[str]
    namespaceVersion: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetUploadStatusRequestTypeDef(BaseValidatorModel):
    uploadId: str


class ListFlowExecutionMessagesRequestTypeDef(BaseValidatorModel):
    flowExecutionId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SystemInstanceFilterTypeDef(BaseValidatorModel):
    name: Optional[SystemInstanceFilterNameType] = None
    value: Optional[Sequence[str]] = None


class SystemTemplateFilterTypeDef(BaseValidatorModel):
    name: Literal["FLOW_TEMPLATE_ID"]
    value: Sequence[str]


class SearchThingsRequestTypeDef(BaseValidatorModel):
    entityId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None


class ThingTypeDef(BaseValidatorModel):
    thingArn: Optional[str] = None
    thingName: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateFlowTemplateRequestTypeDef(BaseValidatorModel):
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None


class CreateSystemTemplateRequestTypeDef(BaseValidatorModel):
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: Optional[int] = None


class UploadEntityDefinitionsRequestTypeDef(BaseValidatorModel):
    document: Optional[DefinitionDocumentTypeDef] = None
    syncWithPublicNamespace: Optional[bool] = None
    deprecateExistingEntities: Optional[bool] = None


class FlowTemplateSummaryTypeDef(BaseValidatorModel):
    pass


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateFlowTemplateResponseTypeDef(BaseValidatorModel):
    summary: FlowTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UploadEntityDefinitionsResponseTypeDef(BaseValidatorModel):
    uploadId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSystemInstanceRequestTypeDef(BaseValidatorModel):
    definition: DefinitionDocumentTypeDef
    target: DeploymentTargetType
    tags: Optional[Sequence[TagTypeDef]] = None
    greengrassGroupName: Optional[str] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfigurationTypeDef] = None
    flowActionsRoleArn: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class SystemInstanceSummaryTypeDef(BaseValidatorModel):
    pass


class CreateSystemInstanceResponseTypeDef(BaseValidatorModel):
    summary: SystemInstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeploySystemInstanceResponseTypeDef(BaseValidatorModel):
    summary: SystemInstanceSummaryTypeDef
    greengrassDeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SearchSystemInstancesResponseTypeDef(BaseValidatorModel):
    summaries: List[SystemInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UndeploySystemInstanceResponseTypeDef(BaseValidatorModel):
    summary: SystemInstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SystemTemplateSummaryTypeDef(BaseValidatorModel):
    pass


class CreateSystemTemplateResponseTypeDef(BaseValidatorModel):
    summary: SystemTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSystemTemplateRevisionsResponseTypeDef(BaseValidatorModel):
    summaries: List[SystemTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchSystemTemplatesResponseTypeDef(BaseValidatorModel):
    summaries: List[SystemTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SystemTemplateDescriptionTypeDef(BaseValidatorModel):
    summary: Optional[SystemTemplateSummaryTypeDef] = None
    definition: Optional[DefinitionDocumentTypeDef] = None
    validatedNamespaceVersion: Optional[int] = None


class UpdateSystemTemplateResponseTypeDef(BaseValidatorModel):
    summary: SystemTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DependencyRevisionTypeDef(BaseValidatorModel):
    pass


class SystemInstanceDescriptionTypeDef(BaseValidatorModel):
    summary: Optional[SystemInstanceSummaryTypeDef] = None
    definition: Optional[DefinitionDocumentTypeDef] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfigurationTypeDef] = None
    validatedNamespaceVersion: Optional[int] = None
    validatedDependencyRevisions: Optional[List[DependencyRevisionTypeDef]] = None
    flowActionsRoleArn: Optional[str] = None


class SearchEntitiesRequestTypeDef(BaseValidatorModel):
    entityTypes: Sequence[EntityTypeType]
    filters: Optional[Sequence[EntityFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None


class ListFlowExecutionMessagesResponseTypeDef(BaseValidatorModel):
    messages: List[FlowExecutionMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchFlowExecutionsResponseTypeDef(BaseValidatorModel):
    summaries: List[FlowExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchFlowTemplatesRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FlowTemplateFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFlowExecutionMessagesRequestPaginateTypeDef(BaseValidatorModel):
    flowExecutionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchEntitiesRequestPaginateTypeDef(BaseValidatorModel):
    entityTypes: Sequence[EntityTypeType]
    filters: Optional[Sequence[EntityFilterTypeDef]] = None
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchFlowTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FlowTemplateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchThingsRequestPaginateTypeDef(BaseValidatorModel):
    entityId: str
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class SearchFlowExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchFlowExecutionsRequestTypeDef(BaseValidatorModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SearchSystemInstancesRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[SystemInstanceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchSystemInstancesRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[SystemInstanceFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SearchSystemTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[SystemTemplateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchSystemTemplatesRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[SystemTemplateFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SearchThingsResponseTypeDef(BaseValidatorModel):
    things: List[ThingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EntityDescriptionTypeDef(BaseValidatorModel):
    pass


class GetEntitiesResponseTypeDef(BaseValidatorModel):
    descriptions: List[EntityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SearchEntitiesResponseTypeDef(BaseValidatorModel):
    descriptions: List[EntityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetFlowTemplateResponseTypeDef(BaseValidatorModel):
    description: FlowTemplateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSystemTemplateResponseTypeDef(BaseValidatorModel):
    description: SystemTemplateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSystemInstanceResponseTypeDef(BaseValidatorModel):
    description: SystemInstanceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



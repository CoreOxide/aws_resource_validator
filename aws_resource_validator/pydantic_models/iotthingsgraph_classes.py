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

class AssociateEntityToThingRequest(BaseValidatorModel):
    thingName: str
    entityId: str
    namespaceVersion: Optional[int] = None


class DefinitionDocument(BaseValidatorModel):
    language: Literal["GRAPHQL"]
    text: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MetricsConfiguration(BaseValidatorModel):
    cloudMetricEnabled: Optional[bool] = None
    metricRuleRoleArn: Optional[str] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class DescribeNamespaceRequest(BaseValidatorModel):
    namespaceName: Optional[str] = None


class DissociateEntityFromThingRequest(BaseValidatorModel):
    thingName: str
    entityType: EntityTypeType


class EntityFilter(BaseValidatorModel):
    name: Optional[EntityFilterNameType] = None
    value: Optional[Sequence[str]] = None


class FlowExecutionMessage(BaseValidatorModel):
    messageId: Optional[str] = None
    eventType: Optional[FlowExecutionEventTypeType] = None
    timestamp: Optional[datetime] = None
    payload: Optional[str] = None


class FlowExecutionSummary(BaseValidatorModel):
    flowExecutionId: Optional[str] = None
    status: Optional[FlowExecutionStatusType] = None
    systemInstanceId: Optional[str] = None
    flowTemplateId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class FlowTemplateFilter(BaseValidatorModel):
    name: Literal["DEVICE_MODEL_ID"]
    value: Sequence[str]


class GetEntitiesRequest(BaseValidatorModel):
    ids: Sequence[str]
    namespaceVersion: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetUploadStatusRequest(BaseValidatorModel):
    uploadId: str


class ListFlowExecutionMessagesRequest(BaseValidatorModel):
    flowExecutionId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SystemInstanceFilter(BaseValidatorModel):
    name: Optional[SystemInstanceFilterNameType] = None
    value: Optional[Sequence[str]] = None


class SystemTemplateFilter(BaseValidatorModel):
    name: Literal["FLOW_TEMPLATE_ID"]
    value: Sequence[str]


class SearchThingsRequest(BaseValidatorModel):
    entityId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None


class Thing(BaseValidatorModel):
    thingArn: Optional[str] = None
    thingName: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateFlowTemplateRequest(BaseValidatorModel):
    definition: DefinitionDocument
    compatibleNamespaceVersion: Optional[int] = None


class CreateSystemTemplateRequest(BaseValidatorModel):
    definition: DefinitionDocument
    compatibleNamespaceVersion: Optional[int] = None


class UploadEntityDefinitionsRequest(BaseValidatorModel):
    document: Optional[DefinitionDocument] = None
    syncWithPublicNamespace: Optional[bool] = None
    deprecateExistingEntities: Optional[bool] = None


class FlowTemplateSummary(BaseValidatorModel):
    pass


class FlowTemplateDescription(BaseValidatorModel):
    summary: Optional[FlowTemplateSummary] = None
    definition: Optional[DefinitionDocument] = None
    validatedNamespaceVersion: Optional[int] = None


class CreateFlowTemplateResponse(BaseValidatorModel):
    summary: FlowTemplateSummary
    ResponseMetadata: ResponseMetadata


class DeleteNamespaceResponse(BaseValidatorModel):
    namespaceArn: str
    namespaceName: str
    ResponseMetadata: ResponseMetadata


class DescribeNamespaceResponse(BaseValidatorModel):
    namespaceArn: str
    namespaceName: str
    trackingNamespaceName: str
    trackingNamespaceVersion: int
    namespaceVersion: int
    ResponseMetadata: ResponseMetadata


class GetFlowTemplateRevisionsResponse(BaseValidatorModel):
    summaries: List[FlowTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetNamespaceDeletionStatusResponse(BaseValidatorModel):
    namespaceArn: str
    namespaceName: str
    status: NamespaceDeletionStatusType
    errorCode: Literal["VALIDATION_FAILED"]
    errorMessage: str
    ResponseMetadata: ResponseMetadata


class GetUploadStatusResponse(BaseValidatorModel):
    uploadId: str
    uploadStatus: UploadStatusType
    namespaceArn: str
    namespaceName: str
    namespaceVersion: int
    failureReason: List[str]
    createdDate: datetime
    ResponseMetadata: ResponseMetadata


class SearchFlowTemplatesResponse(BaseValidatorModel):
    summaries: List[FlowTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateFlowTemplateResponse(BaseValidatorModel):
    summary: FlowTemplateSummary
    ResponseMetadata: ResponseMetadata


class UploadEntityDefinitionsResponse(BaseValidatorModel):
    uploadId: str
    ResponseMetadata: ResponseMetadata


class CreateSystemInstanceRequest(BaseValidatorModel):
    definition: DefinitionDocument
    target: DeploymentTargetType
    tags: Optional[Sequence[Tag]] = None
    greengrassGroupName: Optional[str] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfiguration] = None
    flowActionsRoleArn: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[Tag]


class SystemInstanceSummary(BaseValidatorModel):
    pass


class CreateSystemInstanceResponse(BaseValidatorModel):
    summary: SystemInstanceSummary
    ResponseMetadata: ResponseMetadata


class DeploySystemInstanceResponse(BaseValidatorModel):
    summary: SystemInstanceSummary
    greengrassDeploymentId: str
    ResponseMetadata: ResponseMetadata


class SearchSystemInstancesResponse(BaseValidatorModel):
    summaries: List[SystemInstanceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UndeploySystemInstanceResponse(BaseValidatorModel):
    summary: SystemInstanceSummary
    ResponseMetadata: ResponseMetadata


class SystemTemplateSummary(BaseValidatorModel):
    pass


class CreateSystemTemplateResponse(BaseValidatorModel):
    summary: SystemTemplateSummary
    ResponseMetadata: ResponseMetadata


class GetSystemTemplateRevisionsResponse(BaseValidatorModel):
    summaries: List[SystemTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchSystemTemplatesResponse(BaseValidatorModel):
    summaries: List[SystemTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SystemTemplateDescription(BaseValidatorModel):
    summary: Optional[SystemTemplateSummary] = None
    definition: Optional[DefinitionDocument] = None
    validatedNamespaceVersion: Optional[int] = None


class UpdateSystemTemplateResponse(BaseValidatorModel):
    summary: SystemTemplateSummary
    ResponseMetadata: ResponseMetadata


class DependencyRevision(BaseValidatorModel):
    pass


class SystemInstanceDescription(BaseValidatorModel):
    summary: Optional[SystemInstanceSummary] = None
    definition: Optional[DefinitionDocument] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfiguration] = None
    validatedNamespaceVersion: Optional[int] = None
    validatedDependencyRevisions: Optional[List[DependencyRevision]] = None
    flowActionsRoleArn: Optional[str] = None


class SearchEntitiesRequest(BaseValidatorModel):
    entityTypes: Sequence[EntityTypeType]
    filters: Optional[Sequence[EntityFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None


class ListFlowExecutionMessagesResponse(BaseValidatorModel):
    messages: List[FlowExecutionMessage]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchFlowExecutionsResponse(BaseValidatorModel):
    summaries: List[FlowExecutionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchFlowTemplatesRequest(BaseValidatorModel):
    filters: Optional[Sequence[FlowTemplateFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFlowExecutionMessagesRequestPaginate(BaseValidatorModel):
    flowExecutionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchEntitiesRequestPaginate(BaseValidatorModel):
    entityTypes: Sequence[EntityTypeType]
    filters: Optional[Sequence[EntityFilter]] = None
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchFlowTemplatesRequestPaginate(BaseValidatorModel):
    filters: Optional[Sequence[FlowTemplateFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchThingsRequestPaginate(BaseValidatorModel):
    entityId: str
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class SearchFlowExecutionsRequestPaginate(BaseValidatorModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchFlowExecutionsRequest(BaseValidatorModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SearchSystemInstancesRequestPaginate(BaseValidatorModel):
    filters: Optional[Sequence[SystemInstanceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchSystemInstancesRequest(BaseValidatorModel):
    filters: Optional[Sequence[SystemInstanceFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SearchSystemTemplatesRequestPaginate(BaseValidatorModel):
    filters: Optional[Sequence[SystemTemplateFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchSystemTemplatesRequest(BaseValidatorModel):
    filters: Optional[Sequence[SystemTemplateFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SearchThingsResponse(BaseValidatorModel):
    things: List[Thing]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EntityDescription(BaseValidatorModel):
    pass


class GetEntitiesResponse(BaseValidatorModel):
    descriptions: List[EntityDescription]
    ResponseMetadata: ResponseMetadata


class SearchEntitiesResponse(BaseValidatorModel):
    descriptions: List[EntityDescription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetFlowTemplateResponse(BaseValidatorModel):
    description: FlowTemplateDescription
    ResponseMetadata: ResponseMetadata


class GetSystemTemplateResponse(BaseValidatorModel):
    description: SystemTemplateDescription
    ResponseMetadata: ResponseMetadata


class GetSystemInstanceResponse(BaseValidatorModel):
    description: SystemInstanceDescription
    ResponseMetadata: ResponseMetadata



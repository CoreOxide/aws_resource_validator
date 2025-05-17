from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssociateEntityToThingRequest(BaseValidatorModel):
    thingName: str
    entityId: str
    namespaceVersion: Optional[int] = None


class DefinitionDocument(BaseValidatorModel):
    language: Literal['GRAPHQL']
    text: str


class FlowTemplateSummary(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    revisionNumber: Optional[int] = None
    createdAt: Optional[datetime] = None


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


class SystemInstanceSummary(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[SystemInstanceDeploymentStatusType] = None
    target: Optional[DeploymentTargetType] = None
    greengrassGroupName: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    greengrassGroupId: Optional[str] = None
    greengrassGroupVersionId: Optional[str] = None


class SystemTemplateSummary(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    revisionNumber: Optional[int] = None
    createdAt: Optional[datetime] = None


class DeleteFlowTemplateRequest(BaseValidatorModel):
    id: str


class DeleteSystemInstanceRequest(BaseValidatorModel):
    id: Optional[str] = None


class DeleteSystemTemplateRequest(BaseValidatorModel):
    id: str


class DependencyRevision(BaseValidatorModel):
    id: Optional[str] = None
    revisionNumber: Optional[int] = None


# This class is the input for the 'deploy_system_instance' function.
class DeploySystemInstanceRequest(BaseValidatorModel):
    id: Optional[str] = None


class DeprecateFlowTemplateRequest(BaseValidatorModel):
    id: str


class DeprecateSystemTemplateRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'describe_namespace' function.
class DescribeNamespaceRequest(BaseValidatorModel):
    namespaceName: Optional[str] = None


class DissociateEntityFromThingRequest(BaseValidatorModel):
    thingName: str
    entityType: EntityTypeType


class EntityFilter(BaseValidatorModel):
    name: Optional[EntityFilterNameType] = None
    value: Optional[List[str]] = None


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
    name: Literal['DEVICE_MODEL_ID']
    value: List[str]


# This class is the input for the 'get_entities' function.
class GetEntitiesRequest(BaseValidatorModel):
    ids: List[str]
    namespaceVersion: Optional[int] = None


# This class is the input for the 'get_flow_template' function.
class GetFlowTemplateRequest(BaseValidatorModel):
    id: str
    revisionNumber: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_flow_template_revisions' function.
class GetFlowTemplateRevisionsRequest(BaseValidatorModel):
    id: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_system_instance' function.
class GetSystemInstanceRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_system_template' function.
class GetSystemTemplateRequest(BaseValidatorModel):
    id: str
    revisionNumber: Optional[int] = None


# This class is the input for the 'get_system_template_revisions' function.
class GetSystemTemplateRevisionsRequest(BaseValidatorModel):
    id: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_upload_status' function.
class GetUploadStatusRequest(BaseValidatorModel):
    uploadId: str


# This class is the input for the 'list_flow_execution_messages' function.
class ListFlowExecutionMessagesRequest(BaseValidatorModel):
    flowExecutionId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

Timestamp = Union[datetime, str]


class SystemInstanceFilter(BaseValidatorModel):
    name: Optional[SystemInstanceFilterNameType] = None
    value: Optional[List[str]] = None


class SystemTemplateFilter(BaseValidatorModel):
    name: Literal['FLOW_TEMPLATE_ID']
    value: List[str]


# This class is the input for the 'search_things' function.
class SearchThingsRequest(BaseValidatorModel):
    entityId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None


class Thing(BaseValidatorModel):
    thingArn: Optional[str] = None
    thingName: Optional[str] = None


# This class is the input for the 'undeploy_system_instance' function.
class UndeploySystemInstanceRequest(BaseValidatorModel):
    id: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'create_flow_template' function.
class CreateFlowTemplateRequest(BaseValidatorModel):
    definition: DefinitionDocument
    compatibleNamespaceVersion: Optional[int] = None


# This class is the input for the 'create_system_template' function.
class CreateSystemTemplateRequest(BaseValidatorModel):
    definition: DefinitionDocument
    compatibleNamespaceVersion: Optional[int] = None


class EntityDescription(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    type: Optional[EntityTypeType] = None
    createdAt: Optional[datetime] = None
    definition: Optional[DefinitionDocument] = None


# This class is the input for the 'update_flow_template' function.
class UpdateFlowTemplateRequest(BaseValidatorModel):
    id: str
    definition: DefinitionDocument
    compatibleNamespaceVersion: Optional[int] = None


# This class is the input for the 'update_system_template' function.
class UpdateSystemTemplateRequest(BaseValidatorModel):
    id: str
    definition: DefinitionDocument
    compatibleNamespaceVersion: Optional[int] = None


# This class is the input for the 'upload_entity_definitions' function.
class UploadEntityDefinitionsRequest(BaseValidatorModel):
    document: Optional[DefinitionDocument] = None
    syncWithPublicNamespace: Optional[bool] = None
    deprecateExistingEntities: Optional[bool] = None


class FlowTemplateDescription(BaseValidatorModel):
    summary: Optional[FlowTemplateSummary] = None
    definition: Optional[DefinitionDocument] = None
    validatedNamespaceVersion: Optional[int] = None


# This class is the output for the 'create_flow_template' function.
class CreateFlowTemplateResponse(BaseValidatorModel):
    summary: FlowTemplateSummary
    ResponseMetadata: ResponseMetadata


class DeleteNamespaceResponse(BaseValidatorModel):
    namespaceArn: str
    namespaceName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_namespace' function.
class DescribeNamespaceResponse(BaseValidatorModel):
    namespaceArn: str
    namespaceName: str
    trackingNamespaceName: str
    trackingNamespaceVersion: int
    namespaceVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_flow_template_revisions' function.
class GetFlowTemplateRevisionsResponse(BaseValidatorModel):
    summaries: List[FlowTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetNamespaceDeletionStatusResponse(BaseValidatorModel):
    namespaceArn: str
    namespaceName: str
    status: NamespaceDeletionStatusType
    errorCode: Literal['VALIDATION_FAILED']
    errorMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_upload_status' function.
class GetUploadStatusResponse(BaseValidatorModel):
    uploadId: str
    uploadStatus: UploadStatusType
    namespaceArn: str
    namespaceName: str
    namespaceVersion: int
    failureReason: List[str]
    createdDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_flow_templates' function.
class SearchFlowTemplatesResponse(BaseValidatorModel):
    summaries: List[FlowTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_flow_template' function.
class UpdateFlowTemplateResponse(BaseValidatorModel):
    summary: FlowTemplateSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upload_entity_definitions' function.
class UploadEntityDefinitionsResponse(BaseValidatorModel):
    uploadId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_system_instance' function.
class CreateSystemInstanceRequest(BaseValidatorModel):
    definition: DefinitionDocument
    target: DeploymentTargetType
    tags: Optional[List[Tag]] = None
    greengrassGroupName: Optional[str] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfiguration] = None
    flowActionsRoleArn: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the output for the 'create_system_instance' function.
class CreateSystemInstanceResponse(BaseValidatorModel):
    summary: SystemInstanceSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deploy_system_instance' function.
class DeploySystemInstanceResponse(BaseValidatorModel):
    summary: SystemInstanceSummary
    greengrassDeploymentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_system_instances' function.
class SearchSystemInstancesResponse(BaseValidatorModel):
    summaries: List[SystemInstanceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'undeploy_system_instance' function.
class UndeploySystemInstanceResponse(BaseValidatorModel):
    summary: SystemInstanceSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_system_template' function.
class CreateSystemTemplateResponse(BaseValidatorModel):
    summary: SystemTemplateSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_system_template_revisions' function.
class GetSystemTemplateRevisionsResponse(BaseValidatorModel):
    summaries: List[SystemTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'search_system_templates' function.
class SearchSystemTemplatesResponse(BaseValidatorModel):
    summaries: List[SystemTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SystemTemplateDescription(BaseValidatorModel):
    summary: Optional[SystemTemplateSummary] = None
    definition: Optional[DefinitionDocument] = None
    validatedNamespaceVersion: Optional[int] = None


# This class is the output for the 'update_system_template' function.
class UpdateSystemTemplateResponse(BaseValidatorModel):
    summary: SystemTemplateSummary
    ResponseMetadata: ResponseMetadata


class SystemInstanceDescription(BaseValidatorModel):
    summary: Optional[SystemInstanceSummary] = None
    definition: Optional[DefinitionDocument] = None
    s3BucketName: Optional[str] = None
    metricsConfiguration: Optional[MetricsConfiguration] = None
    validatedNamespaceVersion: Optional[int] = None
    validatedDependencyRevisions: Optional[List[DependencyRevision]] = None
    flowActionsRoleArn: Optional[str] = None


# This class is the input for the 'search_entities' function.
class SearchEntitiesRequest(BaseValidatorModel):
    entityTypes: List[EntityTypeType]
    filters: Optional[List[EntityFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namespaceVersion: Optional[int] = None


# This class is the output for the 'list_flow_execution_messages' function.
class ListFlowExecutionMessagesResponse(BaseValidatorModel):
    messages: List[FlowExecutionMessage]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'search_flow_executions' function.
class SearchFlowExecutionsResponse(BaseValidatorModel):
    summaries: List[FlowExecutionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'search_flow_templates' function.
class SearchFlowTemplatesRequest(BaseValidatorModel):
    filters: Optional[List[FlowTemplateFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetFlowTemplateRevisionsRequestPaginate(BaseValidatorModel):
    id: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSystemTemplateRevisionsRequestPaginate(BaseValidatorModel):
    id: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFlowExecutionMessagesRequestPaginate(BaseValidatorModel):
    flowExecutionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchEntitiesRequestPaginate(BaseValidatorModel):
    entityTypes: List[EntityTypeType]
    filters: Optional[List[EntityFilter]] = None
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchFlowTemplatesRequestPaginate(BaseValidatorModel):
    filters: Optional[List[FlowTemplateFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchThingsRequestPaginate(BaseValidatorModel):
    entityId: str
    namespaceVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchFlowExecutionsRequestPaginate(BaseValidatorModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_flow_executions' function.
class SearchFlowExecutionsRequest(BaseValidatorModel):
    systemInstanceId: str
    flowExecutionId: Optional[str] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SearchSystemInstancesRequestPaginate(BaseValidatorModel):
    filters: Optional[List[SystemInstanceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_system_instances' function.
class SearchSystemInstancesRequest(BaseValidatorModel):
    filters: Optional[List[SystemInstanceFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SearchSystemTemplatesRequestPaginate(BaseValidatorModel):
    filters: Optional[List[SystemTemplateFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_system_templates' function.
class SearchSystemTemplatesRequest(BaseValidatorModel):
    filters: Optional[List[SystemTemplateFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'search_things' function.
class SearchThingsResponse(BaseValidatorModel):
    things: List[Thing]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_entities' function.
class GetEntitiesResponse(BaseValidatorModel):
    descriptions: List[EntityDescription]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_entities' function.
class SearchEntitiesResponse(BaseValidatorModel):
    descriptions: List[EntityDescription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_flow_template' function.
class GetFlowTemplateResponse(BaseValidatorModel):
    description: FlowTemplateDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_system_template' function.
class GetSystemTemplateResponse(BaseValidatorModel):
    description: SystemTemplateDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_system_instance' function.
class GetSystemInstanceResponse(BaseValidatorModel):
    description: SystemInstanceDescription
    ResponseMetadata: ResponseMetadata
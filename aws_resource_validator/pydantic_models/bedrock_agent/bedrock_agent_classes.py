from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.bedrock_agent.bedrock_agent_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class S3Identifier(BaseValidatorModel):
    s3BucketName: Optional[str] = None
    s3ObjectKey: Optional[str] = None


class ActionGroupExecutor(BaseValidatorModel):
    customControl: Optional[Literal['RETURN_CONTROL']] = None
    lambda_:Optional[str] = None


class ActionGroupSummary(BaseValidatorModel):
    actionGroupId: str
    actionGroupName: str
    actionGroupState: ActionGroupStateType
    updatedAt: datetime
    description: Optional[str] = None


class AgentAliasRoutingConfigurationListItem(BaseValidatorModel):
    agentVersion: Optional[str] = None
    provisionedThroughput: Optional[str] = None


class AgentDescriptor(BaseValidatorModel):
    aliasArn: Optional[str] = None


class AgentFlowNodeConfiguration(BaseValidatorModel):
    agentAliasArn: str


class AgentKnowledgeBaseSummary(BaseValidatorModel):
    knowledgeBaseId: str
    knowledgeBaseState: KnowledgeBaseStateType
    updatedAt: datetime
    description: Optional[str] = None


class AgentKnowledgeBase(BaseValidatorModel):
    agentId: str
    agentVersion: str
    createdAt: datetime
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: KnowledgeBaseStateType
    updatedAt: datetime


class GuardrailConfiguration(BaseValidatorModel):
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'associate_agent_knowledge_base' function.
class AssociateAgentKnowledgeBaseRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: Optional[KnowledgeBaseStateType] = None


class BedrockDataAutomationConfiguration(BaseValidatorModel):
    parsingModality: Optional[Literal['MULTIMODAL']] = None


class BedrockEmbeddingModelConfiguration(BaseValidatorModel):
    dimensions: Optional[int] = None
    embeddingDataType: Optional[EmbeddingDataTypeType] = None


class ParsingPrompt(BaseValidatorModel):
    parsingPromptText: str


class EnrichmentStrategyConfiguration(BaseValidatorModel):
    method: Literal['CHUNK_ENTITY_EXTRACTION']

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CachePointBlock(BaseValidatorModel):
    type: Literal['default']


class PromptInputVariable(BaseValidatorModel):
    name: Optional[str] = None


class FixedSizeChunkingConfiguration(BaseValidatorModel):
    maxTokens: int
    overlapPercentage: int


class SemanticChunkingConfiguration(BaseValidatorModel):
    breakpointPercentileThreshold: int
    bufferSize: int
    maxTokens: int


class FlowCondition(BaseValidatorModel):
    name: str
    expression: Optional[str] = None


class ConfluenceSourceConfiguration(BaseValidatorModel):
    authType: ConfluenceAuthTypeType
    credentialsSecretArn: str
    hostType: Literal['SAAS']
    hostUrl: str


class ServerSideEncryptionConfiguration(BaseValidatorModel):
    kmsKeyArn: Optional[str] = None


class FlowAliasRoutingConfigurationListItem(BaseValidatorModel):
    flowVersion: Optional[str] = None


# This class is the input for the 'create_flow_version' function.
class CreateFlowVersionRequest(BaseValidatorModel):
    flowIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'create_prompt_version' function.
class CreatePromptVersionRequest(BaseValidatorModel):
    promptIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CuratedQuery(BaseValidatorModel):
    naturalLanguage: str
    sql: str


class CustomDocumentIdentifier(BaseValidatorModel):
    id: str


class CustomS3Location(BaseValidatorModel):
    uri: str
    bucketOwnerAccountId: Optional[str] = None


class OrchestrationExecutor(BaseValidatorModel):
    lambda_:Optional[str] = None


class CyclicConnectionFlowValidationDetails(BaseValidatorModel):
    connection: str


class S3DataSourceConfigurationOutput(BaseValidatorModel):
    bucketArn: str
    bucketOwnerAccountId: Optional[str] = None
    inclusionPrefixes: Optional[List[str]] = None


class S3DataSourceConfiguration(BaseValidatorModel):
    bucketArn: str
    bucketOwnerAccountId: Optional[str] = None
    inclusionPrefixes: Optional[List[str]] = None


class DataSourceSummary(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    status: DataSourceStatusType
    updatedAt: datetime
    description: Optional[str] = None


class DeleteAgentActionGroupRequest(BaseValidatorModel):
    actionGroupId: str
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: Optional[bool] = None


# This class is the input for the 'delete_agent_alias' function.
class DeleteAgentAliasRequest(BaseValidatorModel):
    agentAliasId: str
    agentId: str


# This class is the input for the 'delete_agent' function.
class DeleteAgentRequest(BaseValidatorModel):
    agentId: str
    skipResourceInUseCheck: Optional[bool] = None


# This class is the input for the 'delete_agent_version' function.
class DeleteAgentVersionRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: Optional[bool] = None


# This class is the input for the 'delete_data_source' function.
class DeleteDataSourceRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str


# This class is the input for the 'delete_flow_alias' function.
class DeleteFlowAliasRequest(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str


# This class is the input for the 'delete_flow' function.
class DeleteFlowRequest(BaseValidatorModel):
    flowIdentifier: str
    skipResourceInUseCheck: Optional[bool] = None


# This class is the input for the 'delete_flow_version' function.
class DeleteFlowVersionRequest(BaseValidatorModel):
    flowIdentifier: str
    flowVersion: str
    skipResourceInUseCheck: Optional[bool] = None


# This class is the input for the 'delete_knowledge_base' function.
class DeleteKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseId: str


# This class is the input for the 'delete_prompt' function.
class DeletePromptRequest(BaseValidatorModel):
    promptIdentifier: str
    promptVersion: Optional[str] = None


class DisassociateAgentCollaboratorRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    collaboratorId: str


class DisassociateAgentKnowledgeBaseRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str


class S3Location(BaseValidatorModel):
    uri: str


class DuplicateConditionExpressionFlowValidationDetails(BaseValidatorModel):
    expression: str
    node: str


class DuplicateConnectionsFlowValidationDetails(BaseValidatorModel):
    source: str
    target: str


class FlowConditionalConnectionConfiguration(BaseValidatorModel):
    condition: str


class FlowDataConnectionConfiguration(BaseValidatorModel):
    sourceOutput: str
    targetInput: str


class LambdaFunctionFlowNodeConfiguration(BaseValidatorModel):
    lambdaArn: str


class LexFlowNodeConfiguration(BaseValidatorModel):
    botAliasArn: str
    localeId: str


class FlowNodeInput(BaseValidatorModel):
    expression: str
    name: str
    type: FlowNodeIODataTypeType


class FlowNodeOutput(BaseValidatorModel):
    name: str
    type: FlowNodeIODataTypeType


class FlowSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    id: str
    name: str
    status: FlowStatusType
    updatedAt: datetime
    version: str
    description: Optional[str] = None


class IncompatibleConnectionDataTypeFlowValidationDetails(BaseValidatorModel):
    connection: str


class MalformedConditionExpressionFlowValidationDetails(BaseValidatorModel):
    cause: str
    condition: str
    node: str


class MalformedNodeInputExpressionFlowValidationDetails(BaseValidatorModel):
    cause: str
    input: str
    node: str


class MismatchedNodeInputTypeFlowValidationDetails(BaseValidatorModel):
    expectedType: FlowNodeIODataTypeType
    input: str
    node: str


class MismatchedNodeOutputTypeFlowValidationDetails(BaseValidatorModel):
    expectedType: FlowNodeIODataTypeType
    node: str
    output: str


class MissingConnectionConfigurationFlowValidationDetails(BaseValidatorModel):
    connection: str


class MissingDefaultConditionFlowValidationDetails(BaseValidatorModel):
    node: str


class MissingNodeConfigurationFlowValidationDetails(BaseValidatorModel):
    node: str


class MissingNodeInputFlowValidationDetails(BaseValidatorModel):
    input: str
    node: str


class MissingNodeOutputFlowValidationDetails(BaseValidatorModel):
    node: str
    output: str


class MultipleNodeInputConnectionsFlowValidationDetails(BaseValidatorModel):
    input: str
    node: str


class UnfulfilledNodeInputFlowValidationDetails(BaseValidatorModel):
    input: str
    node: str


class UnknownConnectionConditionFlowValidationDetails(BaseValidatorModel):
    connection: str


class UnknownConnectionSourceFlowValidationDetails(BaseValidatorModel):
    connection: str


class UnknownConnectionSourceOutputFlowValidationDetails(BaseValidatorModel):
    connection: str


class UnknownConnectionTargetFlowValidationDetails(BaseValidatorModel):
    connection: str


class UnknownConnectionTargetInputFlowValidationDetails(BaseValidatorModel):
    connection: str


class UnknownNodeInputFlowValidationDetails(BaseValidatorModel):
    input: str
    node: str


class UnknownNodeOutputFlowValidationDetails(BaseValidatorModel):
    node: str
    output: str


class UnreachableNodeFlowValidationDetails(BaseValidatorModel):
    node: str


class UnsatisfiedConnectionConditionsFlowValidationDetails(BaseValidatorModel):
    connection: str


class FlowVersionSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    id: str
    status: FlowStatusType
    version: str


class ParameterDetail(BaseValidatorModel):
    type: TypeType
    description: Optional[str] = None
    required: Optional[bool] = None


# This class is the input for the 'get_agent_action_group' function.
class GetAgentActionGroupRequest(BaseValidatorModel):
    actionGroupId: str
    agentId: str
    agentVersion: str


# This class is the input for the 'get_agent_alias' function.
class GetAgentAliasRequest(BaseValidatorModel):
    agentAliasId: str
    agentId: str


# This class is the input for the 'get_agent_collaborator' function.
class GetAgentCollaboratorRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    collaboratorId: str


# This class is the input for the 'get_agent_knowledge_base' function.
class GetAgentKnowledgeBaseRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str


# This class is the input for the 'get_agent' function.
class GetAgentRequest(BaseValidatorModel):
    agentId: str


# This class is the input for the 'get_agent_version' function.
class GetAgentVersionRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str


# This class is the input for the 'get_data_source' function.
class GetDataSourceRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str


# This class is the input for the 'get_flow_alias' function.
class GetFlowAliasRequest(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str


# This class is the input for the 'get_flow' function.
class GetFlowRequest(BaseValidatorModel):
    flowIdentifier: str


# This class is the input for the 'get_flow_version' function.
class GetFlowVersionRequest(BaseValidatorModel):
    flowIdentifier: str
    flowVersion: str


# This class is the input for the 'get_ingestion_job' function.
class GetIngestionJobRequest(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str


# This class is the input for the 'get_knowledge_base' function.
class GetKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseId: str


# This class is the input for the 'get_prompt' function.
class GetPromptRequest(BaseValidatorModel):
    promptIdentifier: str
    promptVersion: Optional[str] = None


class HierarchicalChunkingLevelConfiguration(BaseValidatorModel):
    maxTokens: int


class InferenceConfigurationOutput(BaseValidatorModel):
    maximumLength: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None


class InferenceConfiguration(BaseValidatorModel):
    maximumLength: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None


class IngestionJobFilter(BaseValidatorModel):
    attribute: Literal['STATUS']
    operator: Literal['EQ']
    values: List[str]


class IngestionJobSortBy(BaseValidatorModel):
    attribute: IngestionJobSortByAttributeType
    order: SortOrderType


class IngestionJobStatistics(BaseValidatorModel):
    numberOfDocumentsDeleted: Optional[int] = None
    numberOfDocumentsFailed: Optional[int] = None
    numberOfDocumentsScanned: Optional[int] = None
    numberOfMetadataDocumentsModified: Optional[int] = None
    numberOfMetadataDocumentsScanned: Optional[int] = None
    numberOfModifiedDocumentsIndexed: Optional[int] = None
    numberOfNewDocumentsIndexed: Optional[int] = None


class TextContentDoc(BaseValidatorModel):
    data: str


class KendraKnowledgeBaseConfiguration(BaseValidatorModel):
    kendraIndexArn: str


class KnowledgeBaseSummary(BaseValidatorModel):
    knowledgeBaseId: str
    name: str
    status: KnowledgeBaseStatusType
    updatedAt: datetime
    description: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_agent_action_groups' function.
class ListAgentActionGroupsRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_agent_aliases' function.
class ListAgentAliasesRequest(BaseValidatorModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_agent_collaborators' function.
class ListAgentCollaboratorsRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_agent_knowledge_bases' function.
class ListAgentKnowledgeBasesRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_agent_versions' function.
class ListAgentVersionsRequest(BaseValidatorModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_agents' function.
class ListAgentsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_data_sources' function.
class ListDataSourcesRequest(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_flow_aliases' function.
class ListFlowAliasesRequest(BaseValidatorModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_flow_versions' function.
class ListFlowVersionsRequest(BaseValidatorModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_flows' function.
class ListFlowsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_knowledge_base_documents' function.
class ListKnowledgeBaseDocumentsRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_knowledge_bases' function.
class ListKnowledgeBasesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_prompts' function.
class ListPromptsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    promptIdentifier: Optional[str] = None


class PromptSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    id: str
    name: str
    updatedAt: datetime
    version: str
    description: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class SessionSummaryConfiguration(BaseValidatorModel):
    maxRecentSessions: Optional[int] = None


class MetadataAttributeValue(BaseValidatorModel):
    type: MetadataValueTypeType
    booleanValue: Optional[bool] = None
    numberValue: Optional[float] = None
    stringListValue: Optional[List[str]] = None
    stringValue: Optional[str] = None


class MongoDbAtlasFieldMapping(BaseValidatorModel):
    metadataField: str
    textField: str
    vectorField: str


class NeptuneAnalyticsFieldMapping(BaseValidatorModel):
    metadataField: str
    textField: str


class OpenSearchServerlessFieldMapping(BaseValidatorModel):
    metadataField: str
    textField: str
    vectorField: str


class PatternObjectFilterOutput(BaseValidatorModel):
    objectType: str
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None


class PatternObjectFilter(BaseValidatorModel):
    objectType: str
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None


class PineconeFieldMapping(BaseValidatorModel):
    metadataField: str
    textField: str


# This class is the input for the 'prepare_agent' function.
class PrepareAgentRequest(BaseValidatorModel):
    agentId: str


# This class is the input for the 'prepare_flow' function.
class PrepareFlowRequest(BaseValidatorModel):
    flowIdentifier: str


class PromptAgentResource(BaseValidatorModel):
    agentIdentifier: str


class PromptFlowNodeResourceConfiguration(BaseValidatorModel):
    promptArn: str


class PromptModelInferenceConfigurationOutput(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None


class PromptMetadataEntry(BaseValidatorModel):
    key: str
    value: str


class PromptModelInferenceConfiguration(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None


class QueryGenerationColumn(BaseValidatorModel):
    description: Optional[str] = None
    inclusion: Optional[IncludeExcludeType] = None
    name: Optional[str] = None


class RdsFieldMapping(BaseValidatorModel):
    metadataField: str
    primaryKeyField: str
    textField: str
    vectorField: str


class RedisEnterpriseCloudFieldMapping(BaseValidatorModel):
    metadataField: str
    textField: str
    vectorField: str


class RedshiftProvisionedAuthConfiguration(BaseValidatorModel):
    type: RedshiftProvisionedAuthTypeType
    databaseUser: Optional[str] = None
    usernamePasswordSecretArn: Optional[str] = None


class RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutput(BaseValidatorModel):
    tableNames: List[str]


class RedshiftQueryEngineAwsDataCatalogStorageConfiguration(BaseValidatorModel):
    tableNames: List[str]


class RedshiftQueryEngineRedshiftStorageConfiguration(BaseValidatorModel):
    databaseName: str


class RedshiftServerlessAuthConfiguration(BaseValidatorModel):
    type: RedshiftServerlessAuthTypeType
    usernamePasswordSecretArn: Optional[str] = None


class RetrievalFlowNodeS3Configuration(BaseValidatorModel):
    bucketName: str


class SalesforceSourceConfiguration(BaseValidatorModel):
    authType: Literal['OAUTH2_CLIENT_CREDENTIALS']
    credentialsSecretArn: str
    hostUrl: str


class SeedUrl(BaseValidatorModel):
    url: Optional[str] = None


class SharePointSourceConfigurationOutput(BaseValidatorModel):
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    domain: str
    hostType: Literal['ONLINE']
    siteUrls: List[str]
    tenantId: Optional[str] = None


class SharePointSourceConfiguration(BaseValidatorModel):
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    domain: str
    hostType: Literal['ONLINE']
    siteUrls: List[str]
    tenantId: Optional[str] = None


class SpecificToolChoice(BaseValidatorModel):
    name: str


# This class is the input for the 'start_ingestion_job' function.
class StartIngestionJobRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'stop_ingestion_job' function.
class StopIngestionJobRequest(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str


class StorageFlowNodeS3Configuration(BaseValidatorModel):
    bucketName: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class ToolInputSchemaOutput(BaseValidatorModel):
    json: Optional[Dict[str, Any]] = None


class ToolInputSchema(BaseValidatorModel):
    json: Optional[Dict[str, Any]] = None


class TransformationLambdaConfiguration(BaseValidatorModel):
    lambdaArn: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_agent_knowledge_base' function.
class UpdateAgentKnowledgeBaseRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str
    description: Optional[str] = None
    knowledgeBaseState: Optional[KnowledgeBaseStateType] = None


class WebCrawlerLimits(BaseValidatorModel):
    maxPages: Optional[int] = None
    rateLimit: Optional[int] = None


class APISchema(BaseValidatorModel):
    payload: Optional[str] = None
    s3: Optional[S3Identifier] = None


class AgentAliasHistoryEvent(BaseValidatorModel):
    endDate: Optional[datetime] = None
    routingConfiguration: Optional[List[AgentAliasRoutingConfigurationListItem]] = None
    startDate: Optional[datetime] = None


class AgentAliasSummary(BaseValidatorModel):
    agentAliasId: str
    agentAliasName: str
    agentAliasStatus: AgentAliasStatusType
    createdAt: datetime
    updatedAt: datetime
    description: Optional[str] = None
    routingConfiguration: Optional[List[AgentAliasRoutingConfigurationListItem]] = None


# This class is the input for the 'create_agent_alias' function.
class CreateAgentAliasRequest(BaseValidatorModel):
    agentAliasName: str
    agentId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    routingConfiguration: Optional[List[AgentAliasRoutingConfigurationListItem]] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_agent_alias' function.
class UpdateAgentAliasRequest(BaseValidatorModel):
    agentAliasId: str
    agentAliasName: str
    agentId: str
    description: Optional[str] = None
    routingConfiguration: Optional[List[AgentAliasRoutingConfigurationListItem]] = None


class AgentCollaboratorSummary(BaseValidatorModel):
    agentDescriptor: AgentDescriptor
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorId: str
    collaboratorName: str
    createdAt: datetime
    lastUpdatedAt: datetime
    relayConversationHistory: RelayConversationHistoryType


class AgentCollaborator(BaseValidatorModel):
    agentDescriptor: AgentDescriptor
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorId: str
    collaboratorName: str
    createdAt: datetime
    lastUpdatedAt: datetime
    clientToken: Optional[str] = None
    relayConversationHistory: Optional[RelayConversationHistoryType] = None


# This class is the input for the 'associate_agent_collaborator' function.
class AssociateAgentCollaboratorRequest(BaseValidatorModel):
    agentDescriptor: AgentDescriptor
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorName: str
    clientToken: Optional[str] = None
    relayConversationHistory: Optional[RelayConversationHistoryType] = None


# This class is the input for the 'update_agent_collaborator' function.
class UpdateAgentCollaboratorRequest(BaseValidatorModel):
    agentDescriptor: AgentDescriptor
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorId: str
    collaboratorName: str
    relayConversationHistory: Optional[RelayConversationHistoryType] = None


class AgentSummary(BaseValidatorModel):
    agentId: str
    agentName: str
    agentStatus: AgentStatusType
    updatedAt: datetime
    description: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    latestAgentVersion: Optional[str] = None


class AgentVersionSummary(BaseValidatorModel):
    agentName: str
    agentStatus: AgentStatusType
    agentVersion: str
    createdAt: datetime
    updatedAt: datetime
    description: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None


class KnowledgeBaseFlowNodeConfiguration(BaseValidatorModel):
    knowledgeBaseId: str
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    modelId: Optional[str] = None


# This class is the output for the 'associate_agent_knowledge_base' function.
class AssociateAgentKnowledgeBaseResponse(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBase
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_agent_alias' function.
class DeleteAgentAliasResponse(BaseValidatorModel):
    agentAliasId: str
    agentAliasStatus: AgentAliasStatusType
    agentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_agent' function.
class DeleteAgentResponse(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_agent_version' function.
class DeleteAgentVersionResponse(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_data_source' function.
class DeleteDataSourceResponse(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    status: DataSourceStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_flow_alias' function.
class DeleteFlowAliasResponse(BaseValidatorModel):
    flowId: str
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_flow' function.
class DeleteFlowResponse(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_flow_version' function.
class DeleteFlowVersionResponse(BaseValidatorModel):
    id: str
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_knowledge_base' function.
class DeleteKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBaseId: str
    status: KnowledgeBaseStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_prompt' function.
class DeletePromptResponse(BaseValidatorModel):
    id: str
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_agent_knowledge_base' function.
class GetAgentKnowledgeBaseResponse(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBase
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_agent_action_groups' function.
class ListAgentActionGroupsResponse(BaseValidatorModel):
    actionGroupSummaries: List[ActionGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_agent_knowledge_bases' function.
class ListAgentKnowledgeBasesResponse(BaseValidatorModel):
    agentKnowledgeBaseSummaries: List[AgentKnowledgeBaseSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'prepare_agent' function.
class PrepareAgentResponse(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    preparedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'prepare_flow' function.
class PrepareFlowResponse(BaseValidatorModel):
    id: str
    status: FlowStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_agent_knowledge_base' function.
class UpdateAgentKnowledgeBaseResponse(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBase
    ResponseMetadata: ResponseMetadata


class EmbeddingModelConfiguration(BaseValidatorModel):
    bedrockEmbeddingModelConfiguration: Optional[BedrockEmbeddingModelConfiguration] = None


class BedrockFoundationModelConfiguration(BaseValidatorModel):
    modelArn: str
    parsingModality: Optional[Literal['MULTIMODAL']] = None
    parsingPrompt: Optional[ParsingPrompt] = None


class BedrockFoundationModelContextEnrichmentConfiguration(BaseValidatorModel):
    enrichmentStrategyConfiguration: EnrichmentStrategyConfiguration
    modelArn: str


class ByteContentDoc(BaseValidatorModel):
    data: Blob
    mimeType: str


class ContentBlock(BaseValidatorModel):
    cachePoint: Optional[CachePointBlock] = None
    text: Optional[str] = None


class SystemContentBlock(BaseValidatorModel):
    cachePoint: Optional[CachePointBlock] = None
    text: Optional[str] = None


class TextPromptTemplateConfigurationOutput(BaseValidatorModel):
    text: str
    cachePoint: Optional[CachePointBlock] = None
    inputVariables: Optional[List[PromptInputVariable]] = None


class TextPromptTemplateConfiguration(BaseValidatorModel):
    text: str
    cachePoint: Optional[CachePointBlock] = None
    inputVariables: Optional[List[PromptInputVariable]] = None


class ConditionFlowNodeConfigurationOutput(BaseValidatorModel):
    conditions: List[FlowCondition]


class ConditionFlowNodeConfiguration(BaseValidatorModel):
    conditions: List[FlowCondition]


# This class is the input for the 'create_flow_alias' function.
class CreateFlowAliasRequest(BaseValidatorModel):
    flowIdentifier: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItem]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_flow_alias' function.
class CreateFlowAliasResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    description: str
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItem]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class FlowAliasSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItem]
    updatedAt: datetime
    description: Optional[str] = None


# This class is the output for the 'get_flow_alias' function.
class GetFlowAliasResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    description: str
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItem]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_flow_alias' function.
class UpdateFlowAliasRequest(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItem]
    description: Optional[str] = None


# This class is the output for the 'update_flow_alias' function.
class UpdateFlowAliasResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    description: str
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItem]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class CustomOrchestration(BaseValidatorModel):
    executor: Optional[OrchestrationExecutor] = None


# This class is the output for the 'list_data_sources' function.
class ListDataSourcesResponse(BaseValidatorModel):
    dataSourceSummaries: List[DataSourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DocumentIdentifier(BaseValidatorModel):
    dataSourceType: ContentDataSourceTypeType
    custom: Optional[CustomDocumentIdentifier] = None
    s3: Optional[S3Location] = None


class IntermediateStorage(BaseValidatorModel):
    s3Location: S3Location


class S3Content(BaseValidatorModel):
    s3Location: S3Location


class SupplementalDataStorageLocation(BaseValidatorModel):
    type: Literal['S3']
    s3Location: Optional[S3Location] = None


class FlowConnectionConfiguration(BaseValidatorModel):
    conditional: Optional[FlowConditionalConnectionConfiguration] = None
    data: Optional[FlowDataConnectionConfiguration] = None


# This class is the output for the 'list_flows' function.
class ListFlowsResponse(BaseValidatorModel):
    flowSummaries: List[FlowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FlowValidationDetails(BaseValidatorModel):
    cyclicConnection: Optional[CyclicConnectionFlowValidationDetails] = None
    duplicateConditionExpression: Optional[DuplicateConditionExpressionFlowValidationDetails] = None
    duplicateConnections: Optional[DuplicateConnectionsFlowValidationDetails] = None
    incompatibleConnectionDataType: Optional[IncompatibleConnectionDataTypeFlowValidationDetails] = None
    malformedConditionExpression: Optional[MalformedConditionExpressionFlowValidationDetails] = None
    malformedNodeInputExpression: Optional[MalformedNodeInputExpressionFlowValidationDetails] = None
    mismatchedNodeInputType: Optional[MismatchedNodeInputTypeFlowValidationDetails] = None
    mismatchedNodeOutputType: Optional[MismatchedNodeOutputTypeFlowValidationDetails] = None
    missingConnectionConfiguration: Optional[MissingConnectionConfigurationFlowValidationDetails] = None
    missingDefaultCondition: Optional[MissingDefaultConditionFlowValidationDetails] = None
    missingEndingNodes: Optional[Dict[str, Any]] = None
    missingNodeConfiguration: Optional[MissingNodeConfigurationFlowValidationDetails] = None
    missingNodeInput: Optional[MissingNodeInputFlowValidationDetails] = None
    missingNodeOutput: Optional[MissingNodeOutputFlowValidationDetails] = None
    missingStartingNodes: Optional[Dict[str, Any]] = None
    multipleNodeInputConnections: Optional[MultipleNodeInputConnectionsFlowValidationDetails] = None
    unfulfilledNodeInput: Optional[UnfulfilledNodeInputFlowValidationDetails] = None
    unknownConnectionCondition: Optional[UnknownConnectionConditionFlowValidationDetails] = None
    unknownConnectionSource: Optional[UnknownConnectionSourceFlowValidationDetails] = None
    unknownConnectionSourceOutput: Optional[UnknownConnectionSourceOutputFlowValidationDetails] = None
    unknownConnectionTarget: Optional[UnknownConnectionTargetFlowValidationDetails] = None
    unknownConnectionTargetInput: Optional[UnknownConnectionTargetInputFlowValidationDetails] = None
    unknownNodeInput: Optional[UnknownNodeInputFlowValidationDetails] = None
    unknownNodeOutput: Optional[UnknownNodeOutputFlowValidationDetails] = None
    unreachableNode: Optional[UnreachableNodeFlowValidationDetails] = None
    unsatisfiedConnectionConditions: Optional[UnsatisfiedConnectionConditionsFlowValidationDetails] = None
    unspecified: Optional[Dict[str, Any]] = None


# This class is the output for the 'list_flow_versions' function.
class ListFlowVersionsResponse(BaseValidatorModel):
    flowVersionSummaries: List[FlowVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FunctionOutput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, ParameterDetail]] = None
    requireConfirmation: Optional[RequireConfirmationType] = None


class Function(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, ParameterDetail]] = None
    requireConfirmation: Optional[RequireConfirmationType] = None


class HierarchicalChunkingConfigurationOutput(BaseValidatorModel):
    levelConfigurations: List[HierarchicalChunkingLevelConfiguration]
    overlapTokens: int


class HierarchicalChunkingConfiguration(BaseValidatorModel):
    levelConfigurations: List[HierarchicalChunkingLevelConfiguration]
    overlapTokens: int


class PromptConfigurationOutput(BaseValidatorModel):
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    basePromptTemplate: Optional[str] = None
    foundationModel: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationOutput] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None


class PromptConfiguration(BaseValidatorModel):
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    basePromptTemplate: Optional[str] = None
    foundationModel: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfiguration] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None


# This class is the input for the 'list_ingestion_jobs' function.
class ListIngestionJobsRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    filters: Optional[List[IngestionJobFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[IngestionJobSortBy] = None


class IngestionJobSummary(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str
    startedAt: datetime
    status: IngestionJobStatusType
    updatedAt: datetime
    description: Optional[str] = None
    statistics: Optional[IngestionJobStatistics] = None


class IngestionJob(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str
    startedAt: datetime
    status: IngestionJobStatusType
    updatedAt: datetime
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    statistics: Optional[IngestionJobStatistics] = None


# This class is the output for the 'list_knowledge_bases' function.
class ListKnowledgeBasesResponse(BaseValidatorModel):
    knowledgeBaseSummaries: List[KnowledgeBaseSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAgentActionGroupsRequestPaginate(BaseValidatorModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAgentAliasesRequestPaginate(BaseValidatorModel):
    agentId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAgentCollaboratorsRequestPaginate(BaseValidatorModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAgentKnowledgeBasesRequestPaginate(BaseValidatorModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAgentVersionsRequestPaginate(BaseValidatorModel):
    agentId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAgentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSourcesRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFlowAliasesRequestPaginate(BaseValidatorModel):
    flowIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFlowVersionsRequestPaginate(BaseValidatorModel):
    flowIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFlowsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIngestionJobsRequestPaginate(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    filters: Optional[List[IngestionJobFilter]] = None
    sortBy: Optional[IngestionJobSortBy] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKnowledgeBaseDocumentsRequestPaginate(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKnowledgeBasesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPromptsRequestPaginate(BaseValidatorModel):
    promptIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_prompts' function.
class ListPromptsResponse(BaseValidatorModel):
    promptSummaries: List[PromptSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MemoryConfigurationOutput(BaseValidatorModel):
    enabledMemoryTypes: List[Literal['SESSION_SUMMARY']]
    sessionSummaryConfiguration: Optional[SessionSummaryConfiguration] = None
    storageDays: Optional[int] = None


class MemoryConfiguration(BaseValidatorModel):
    enabledMemoryTypes: List[Literal['SESSION_SUMMARY']]
    sessionSummaryConfiguration: Optional[SessionSummaryConfiguration] = None
    storageDays: Optional[int] = None


class MetadataAttribute(BaseValidatorModel):
    key: str
    value: MetadataAttributeValue


class MongoDbAtlasConfiguration(BaseValidatorModel):
    collectionName: str
    credentialsSecretArn: str
    databaseName: str
    endpoint: str
    fieldMapping: MongoDbAtlasFieldMapping
    vectorIndexName: str
    endpointServiceName: Optional[str] = None


class NeptuneAnalyticsConfiguration(BaseValidatorModel):
    fieldMapping: NeptuneAnalyticsFieldMapping
    graphArn: str


class OpenSearchServerlessConfiguration(BaseValidatorModel):
    collectionArn: str
    fieldMapping: OpenSearchServerlessFieldMapping
    vectorIndexName: str


class PatternObjectFilterConfigurationOutput(BaseValidatorModel):
    filters: List[PatternObjectFilterOutput]


class PatternObjectFilterConfiguration(BaseValidatorModel):
    filters: List[PatternObjectFilter]


class PineconeConfiguration(BaseValidatorModel):
    connectionString: str
    credentialsSecretArn: str
    fieldMapping: PineconeFieldMapping
    namespace: Optional[str] = None


class PromptGenAiResource(BaseValidatorModel):
    agent: Optional[PromptAgentResource] = None


class PromptInferenceConfigurationOutput(BaseValidatorModel):
    text: Optional[PromptModelInferenceConfigurationOutput] = None

PromptModelInferenceConfigurationUnion = Union[PromptModelInferenceConfiguration, PromptModelInferenceConfigurationOutput]


class QueryGenerationTableOutput(BaseValidatorModel):
    name: str
    columns: Optional[List[QueryGenerationColumn]] = None
    description: Optional[str] = None
    inclusion: Optional[IncludeExcludeType] = None


class QueryGenerationTable(BaseValidatorModel):
    name: str
    columns: Optional[List[QueryGenerationColumn]] = None
    description: Optional[str] = None
    inclusion: Optional[IncludeExcludeType] = None


class RdsConfiguration(BaseValidatorModel):
    credentialsSecretArn: str
    databaseName: str
    fieldMapping: RdsFieldMapping
    resourceArn: str
    tableName: str


class RedisEnterpriseCloudConfiguration(BaseValidatorModel):
    credentialsSecretArn: str
    endpoint: str
    fieldMapping: RedisEnterpriseCloudFieldMapping
    vectorIndexName: str


class RedshiftProvisionedConfiguration(BaseValidatorModel):
    authConfiguration: RedshiftProvisionedAuthConfiguration
    clusterIdentifier: str


class RedshiftQueryEngineStorageConfigurationOutput(BaseValidatorModel):
    type: RedshiftQueryEngineStorageTypeType
    awsDataCatalogConfiguration: Optional[RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutput] = None
    redshiftConfiguration: Optional[RedshiftQueryEngineRedshiftStorageConfiguration] = None


class RedshiftQueryEngineStorageConfiguration(BaseValidatorModel):
    type: RedshiftQueryEngineStorageTypeType
    awsDataCatalogConfiguration: Optional[RedshiftQueryEngineAwsDataCatalogStorageConfiguration] = None
    redshiftConfiguration: Optional[RedshiftQueryEngineRedshiftStorageConfiguration] = None


class RedshiftServerlessConfiguration(BaseValidatorModel):
    authConfiguration: RedshiftServerlessAuthConfiguration
    workgroupArn: str


class RetrievalFlowNodeServiceConfiguration(BaseValidatorModel):
    s3: Optional[RetrievalFlowNodeS3Configuration] = None


class UrlConfigurationOutput(BaseValidatorModel):
    seedUrls: Optional[List[SeedUrl]] = None


class UrlConfiguration(BaseValidatorModel):
    seedUrls: Optional[List[SeedUrl]] = None


class ToolChoiceOutput(BaseValidatorModel):
    any: Optional[Dict[str, Any]] = None
    auto: Optional[Dict[str, Any]] = None
    tool: Optional[SpecificToolChoice] = None


class ToolChoice(BaseValidatorModel):
    any: Optional[Dict[str, Any]] = None
    auto: Optional[Dict[str, Any]] = None
    tool: Optional[SpecificToolChoice] = None


class StorageFlowNodeServiceConfiguration(BaseValidatorModel):
    s3: Optional[StorageFlowNodeS3Configuration] = None


class ToolSpecificationOutput(BaseValidatorModel):
    inputSchema: ToolInputSchemaOutput
    name: str
    description: Optional[str] = None

ToolInputSchemaUnion = Union[ToolInputSchema, ToolInputSchemaOutput]


class TransformationFunction(BaseValidatorModel):
    transformationLambdaConfiguration: TransformationLambdaConfiguration


class WebCrawlerConfigurationOutput(BaseValidatorModel):
    crawlerLimits: Optional[WebCrawlerLimits] = None
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None
    scope: Optional[WebScopeTypeType] = None
    userAgent: Optional[str] = None
    userAgentHeader: Optional[str] = None


class WebCrawlerConfiguration(BaseValidatorModel):
    crawlerLimits: Optional[WebCrawlerLimits] = None
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None
    scope: Optional[WebScopeTypeType] = None
    userAgent: Optional[str] = None
    userAgentHeader: Optional[str] = None


class AgentAlias(BaseValidatorModel):
    agentAliasArn: str
    agentAliasId: str
    agentAliasName: str
    agentAliasStatus: AgentAliasStatusType
    agentId: str
    createdAt: datetime
    routingConfiguration: List[AgentAliasRoutingConfigurationListItem]
    updatedAt: datetime
    agentAliasHistoryEvents: Optional[List[AgentAliasHistoryEvent]] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None


# This class is the output for the 'list_agent_aliases' function.
class ListAgentAliasesResponse(BaseValidatorModel):
    agentAliasSummaries: List[AgentAliasSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_agent_collaborators' function.
class ListAgentCollaboratorsResponse(BaseValidatorModel):
    agentCollaboratorSummaries: List[AgentCollaboratorSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'associate_agent_collaborator' function.
class AssociateAgentCollaboratorResponse(BaseValidatorModel):
    agentCollaborator: AgentCollaborator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_agent_collaborator' function.
class GetAgentCollaboratorResponse(BaseValidatorModel):
    agentCollaborator: AgentCollaborator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_agent_collaborator' function.
class UpdateAgentCollaboratorResponse(BaseValidatorModel):
    agentCollaborator: AgentCollaborator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_agents' function.
class ListAgentsResponse(BaseValidatorModel):
    agentSummaries: List[AgentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_agent_versions' function.
class ListAgentVersionsResponse(BaseValidatorModel):
    agentVersionSummaries: List[AgentVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ParsingConfiguration(BaseValidatorModel):
    parsingStrategy: ParsingStrategyType
    bedrockDataAutomationConfiguration: Optional[BedrockDataAutomationConfiguration] = None
    bedrockFoundationModelConfiguration: Optional[BedrockFoundationModelConfiguration] = None


class ContextEnrichmentConfiguration(BaseValidatorModel):
    type: Literal['BEDROCK_FOUNDATION_MODEL']
    bedrockFoundationModelConfiguration: Optional[BedrockFoundationModelContextEnrichmentConfiguration] = None


class InlineContent(BaseValidatorModel):
    type: InlineContentTypeType
    byteContent: Optional[ByteContentDoc] = None
    textContent: Optional[TextContentDoc] = None


class MessageOutput(BaseValidatorModel):
    content: List[ContentBlock]
    role: ConversationRoleType


class Message(BaseValidatorModel):
    content: List[ContentBlock]
    role: ConversationRoleType

TextPromptTemplateConfigurationUnion = Union[TextPromptTemplateConfiguration, TextPromptTemplateConfigurationOutput]


# This class is the output for the 'list_flow_aliases' function.
class ListFlowAliasesResponse(BaseValidatorModel):
    flowAliasSummaries: List[FlowAliasSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'delete_knowledge_base_documents' function.
class DeleteKnowledgeBaseDocumentsRequest(BaseValidatorModel):
    dataSourceId: str
    documentIdentifiers: List[DocumentIdentifier]
    knowledgeBaseId: str
    clientToken: Optional[str] = None


# This class is the input for the 'get_knowledge_base_documents' function.
class GetKnowledgeBaseDocumentsRequest(BaseValidatorModel):
    dataSourceId: str
    documentIdentifiers: List[DocumentIdentifier]
    knowledgeBaseId: str


class KnowledgeBaseDocumentDetail(BaseValidatorModel):
    dataSourceId: str
    identifier: DocumentIdentifier
    knowledgeBaseId: str
    status: DocumentStatusType
    statusReason: Optional[str] = None
    updatedAt: Optional[datetime] = None


class SupplementalDataStorageConfigurationOutput(BaseValidatorModel):
    storageLocations: List[SupplementalDataStorageLocation]


class SupplementalDataStorageConfiguration(BaseValidatorModel):
    storageLocations: List[SupplementalDataStorageLocation]


class FlowConnection(BaseValidatorModel):
    name: str
    source: str
    target: str
    type: FlowConnectionTypeType
    configuration: Optional[FlowConnectionConfiguration] = None


class FlowValidation(BaseValidatorModel):
    message: str
    severity: FlowValidationSeverityType
    details: Optional[FlowValidationDetails] = None
    type: Optional[FlowValidationTypeType] = None


class FunctionSchemaOutput(BaseValidatorModel):
    functions: Optional[List[FunctionOutput]] = None


class FunctionSchema(BaseValidatorModel):
    functions: Optional[List[Function]] = None


class ChunkingConfigurationOutput(BaseValidatorModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfiguration] = None
    hierarchicalChunkingConfiguration: Optional[HierarchicalChunkingConfigurationOutput] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfiguration] = None


class ChunkingConfiguration(BaseValidatorModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfiguration] = None
    hierarchicalChunkingConfiguration: Optional[HierarchicalChunkingConfiguration] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfiguration] = None


class PromptOverrideConfigurationOutput(BaseValidatorModel):
    promptConfigurations: List[PromptConfigurationOutput]
    overrideLambda: Optional[str] = None


class PromptOverrideConfiguration(BaseValidatorModel):
    promptConfigurations: List[PromptConfiguration]
    overrideLambda: Optional[str] = None


# This class is the output for the 'list_ingestion_jobs' function.
class ListIngestionJobsResponse(BaseValidatorModel):
    ingestionJobSummaries: List[IngestionJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_ingestion_job' function.
class GetIngestionJobResponse(BaseValidatorModel):
    ingestionJob: IngestionJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_ingestion_job' function.
class StartIngestionJobResponse(BaseValidatorModel):
    ingestionJob: IngestionJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_ingestion_job' function.
class StopIngestionJobResponse(BaseValidatorModel):
    ingestionJob: IngestionJob
    ResponseMetadata: ResponseMetadata

MemoryConfigurationUnion = Union[MemoryConfiguration, MemoryConfigurationOutput]


class DocumentMetadata(BaseValidatorModel):
    type: MetadataSourceTypeType
    inlineAttributes: Optional[List[MetadataAttribute]] = None
    s3Location: Optional[CustomS3Location] = None


class CrawlFilterConfigurationOutput(BaseValidatorModel):
    type: Literal['PATTERN']
    patternObjectFilter: Optional[PatternObjectFilterConfigurationOutput] = None


class CrawlFilterConfiguration(BaseValidatorModel):
    type: Literal['PATTERN']
    patternObjectFilter: Optional[PatternObjectFilterConfiguration] = None


class PromptInferenceConfiguration(BaseValidatorModel):
    text: Optional[PromptModelInferenceConfigurationUnion] = None


class QueryGenerationContextOutput(BaseValidatorModel):
    curatedQueries: Optional[List[CuratedQuery]] = None
    tables: Optional[List[QueryGenerationTableOutput]] = None


class QueryGenerationContext(BaseValidatorModel):
    curatedQueries: Optional[List[CuratedQuery]] = None
    tables: Optional[List[QueryGenerationTable]] = None


class StorageConfiguration(BaseValidatorModel):
    type: KnowledgeBaseStorageTypeType
    mongoDbAtlasConfiguration: Optional[MongoDbAtlasConfiguration] = None
    neptuneAnalyticsConfiguration: Optional[NeptuneAnalyticsConfiguration] = None
    opensearchServerlessConfiguration: Optional[OpenSearchServerlessConfiguration] = None
    pineconeConfiguration: Optional[PineconeConfiguration] = None
    rdsConfiguration: Optional[RdsConfiguration] = None
    redisEnterpriseCloudConfiguration: Optional[RedisEnterpriseCloudConfiguration] = None


class RedshiftQueryEngineConfiguration(BaseValidatorModel):
    type: RedshiftQueryEngineTypeType
    provisionedConfiguration: Optional[RedshiftProvisionedConfiguration] = None
    serverlessConfiguration: Optional[RedshiftServerlessConfiguration] = None


class RetrievalFlowNodeConfiguration(BaseValidatorModel):
    serviceConfiguration: RetrievalFlowNodeServiceConfiguration


class WebSourceConfigurationOutput(BaseValidatorModel):
    urlConfiguration: UrlConfigurationOutput


class WebSourceConfiguration(BaseValidatorModel):
    urlConfiguration: UrlConfiguration

ToolChoiceUnion = Union[ToolChoice, ToolChoiceOutput]


class StorageFlowNodeConfiguration(BaseValidatorModel):
    serviceConfiguration: StorageFlowNodeServiceConfiguration


class ToolOutput(BaseValidatorModel):
    cachePoint: Optional[CachePointBlock] = None
    toolSpec: Optional[ToolSpecificationOutput] = None


class ToolSpecification(BaseValidatorModel):
    inputSchema: ToolInputSchemaUnion
    name: str
    description: Optional[str] = None


class Transformation(BaseValidatorModel):
    stepToApply: Literal['POST_CHUNKING']
    transformationFunction: TransformationFunction


# This class is the output for the 'create_agent_alias' function.
class CreateAgentAliasResponse(BaseValidatorModel):
    agentAlias: AgentAlias
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_agent_alias' function.
class GetAgentAliasResponse(BaseValidatorModel):
    agentAlias: AgentAlias
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_agent_alias' function.
class UpdateAgentAliasResponse(BaseValidatorModel):
    agentAlias: AgentAlias
    ResponseMetadata: ResponseMetadata


class CustomContent(BaseValidatorModel):
    customDocumentIdentifier: CustomDocumentIdentifier
    sourceType: CustomSourceTypeType
    inlineContent: Optional[InlineContent] = None
    s3Location: Optional[CustomS3Location] = None

MessageUnion = Union[Message, MessageOutput]


# This class is the output for the 'delete_knowledge_base_documents' function.
class DeleteKnowledgeBaseDocumentsResponse(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_knowledge_base_documents' function.
class GetKnowledgeBaseDocumentsResponse(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'ingest_knowledge_base_documents' function.
class IngestKnowledgeBaseDocumentsResponse(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_knowledge_base_documents' function.
class ListKnowledgeBaseDocumentsResponse(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class VectorKnowledgeBaseConfigurationOutput(BaseValidatorModel):
    embeddingModelArn: str
    embeddingModelConfiguration: Optional[EmbeddingModelConfiguration] = None
    supplementalDataStorageConfiguration: Optional[SupplementalDataStorageConfigurationOutput] = None


class VectorKnowledgeBaseConfiguration(BaseValidatorModel):
    embeddingModelArn: str
    embeddingModelConfiguration: Optional[EmbeddingModelConfiguration] = None
    supplementalDataStorageConfiguration: Optional[SupplementalDataStorageConfiguration] = None


# This class is the output for the 'validate_flow_definition' function.
class ValidateFlowDefinitionResponse(BaseValidatorModel):
    validations: List[FlowValidation]
    ResponseMetadata: ResponseMetadata


class AgentActionGroup(BaseValidatorModel):
    actionGroupId: str
    actionGroupName: str
    actionGroupState: ActionGroupStateType
    agentId: str
    agentVersion: str
    createdAt: datetime
    updatedAt: datetime
    actionGroupExecutor: Optional[ActionGroupExecutor] = None
    apiSchema: Optional[APISchema] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchemaOutput] = None
    parentActionGroupSignatureParams: Optional[Dict[str, str]] = None
    parentActionSignature: Optional[ActionGroupSignatureType] = None

FunctionSchemaUnion = Union[FunctionSchema, FunctionSchemaOutput]


class Agent(BaseValidatorModel):
    agentArn: str
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    agentStatus: AgentStatusType
    agentVersion: str
    createdAt: datetime
    idleSessionTTLInSeconds: int
    updatedAt: datetime
    agentCollaboration: Optional[AgentCollaborationType] = None
    clientToken: Optional[str] = None
    customOrchestration: Optional[CustomOrchestration] = None
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    foundationModel: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationOutput] = None
    orchestrationType: Optional[OrchestrationTypeType] = None
    preparedAt: Optional[datetime] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationOutput] = None
    recommendedActions: Optional[List[str]] = None


class AgentVersion(BaseValidatorModel):
    agentArn: str
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    agentStatus: AgentStatusType
    createdAt: datetime
    idleSessionTTLInSeconds: int
    updatedAt: datetime
    version: str
    agentCollaboration: Optional[AgentCollaborationType] = None
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    foundationModel: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationOutput] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationOutput] = None
    recommendedActions: Optional[List[str]] = None

PromptOverrideConfigurationUnion = Union[PromptOverrideConfiguration, PromptOverrideConfigurationOutput]


class ConfluenceCrawlerConfigurationOutput(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutput] = None


class SalesforceCrawlerConfigurationOutput(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutput] = None


class SharePointCrawlerConfigurationOutput(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutput] = None


class ConfluenceCrawlerConfiguration(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfiguration] = None


class SalesforceCrawlerConfiguration(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfiguration] = None


class SharePointCrawlerConfiguration(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfiguration] = None

PromptInferenceConfigurationUnion = Union[PromptInferenceConfiguration, PromptInferenceConfigurationOutput]


class QueryGenerationConfigurationOutput(BaseValidatorModel):
    executionTimeoutSeconds: Optional[int] = None
    generationContext: Optional[QueryGenerationContextOutput] = None


class QueryGenerationConfiguration(BaseValidatorModel):
    executionTimeoutSeconds: Optional[int] = None
    generationContext: Optional[QueryGenerationContext] = None


class WebDataSourceConfigurationOutput(BaseValidatorModel):
    sourceConfiguration: WebSourceConfigurationOutput
    crawlerConfiguration: Optional[WebCrawlerConfigurationOutput] = None


class WebDataSourceConfiguration(BaseValidatorModel):
    sourceConfiguration: WebSourceConfiguration
    crawlerConfiguration: Optional[WebCrawlerConfiguration] = None


class ToolConfigurationOutput(BaseValidatorModel):
    tools: List[ToolOutput]
    toolChoice: Optional[ToolChoiceOutput] = None

ToolSpecificationUnion = Union[ToolSpecification, ToolSpecificationOutput]


class CustomTransformationConfigurationOutput(BaseValidatorModel):
    intermediateStorage: IntermediateStorage
    transformations: List[Transformation]


class CustomTransformationConfiguration(BaseValidatorModel):
    intermediateStorage: IntermediateStorage
    transformations: List[Transformation]


class DocumentContent(BaseValidatorModel):
    dataSourceType: ContentDataSourceTypeType
    custom: Optional[CustomContent] = None
    s3: Optional[S3Content] = None


# This class is the output for the 'create_agent_action_group' function.
class CreateAgentActionGroupResponse(BaseValidatorModel):
    agentActionGroup: AgentActionGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_agent_action_group' function.
class GetAgentActionGroupResponse(BaseValidatorModel):
    agentActionGroup: AgentActionGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_agent_action_group' function.
class UpdateAgentActionGroupResponse(BaseValidatorModel):
    agentActionGroup: AgentActionGroup
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_agent_action_group' function.
class CreateAgentActionGroupRequest(BaseValidatorModel):
    actionGroupName: str
    agentId: str
    agentVersion: str
    actionGroupExecutor: Optional[ActionGroupExecutor] = None
    actionGroupState: Optional[ActionGroupStateType] = None
    apiSchema: Optional[APISchema] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchemaUnion] = None
    parentActionGroupSignature: Optional[ActionGroupSignatureType] = None
    parentActionGroupSignatureParams: Optional[Dict[str, str]] = None


# This class is the input for the 'update_agent_action_group' function.
class UpdateAgentActionGroupRequest(BaseValidatorModel):
    actionGroupId: str
    actionGroupName: str
    agentId: str
    agentVersion: str
    actionGroupExecutor: Optional[ActionGroupExecutor] = None
    actionGroupState: Optional[ActionGroupStateType] = None
    apiSchema: Optional[APISchema] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchemaUnion] = None
    parentActionGroupSignature: Optional[ActionGroupSignatureType] = None
    parentActionGroupSignatureParams: Optional[Dict[str, str]] = None


# This class is the output for the 'create_agent' function.
class CreateAgentResponse(BaseValidatorModel):
    agent: Agent
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_agent' function.
class GetAgentResponse(BaseValidatorModel):
    agent: Agent
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_agent' function.
class UpdateAgentResponse(BaseValidatorModel):
    agent: Agent
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_agent_version' function.
class GetAgentVersionResponse(BaseValidatorModel):
    agentVersion: AgentVersion
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_agent' function.
class CreateAgentRequest(BaseValidatorModel):
    agentName: str
    agentCollaboration: Optional[AgentCollaborationType] = None
    agentResourceRoleArn: Optional[str] = None
    clientToken: Optional[str] = None
    customOrchestration: Optional[CustomOrchestration] = None
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    foundationModel: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    idleSessionTTLInSeconds: Optional[int] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationUnion] = None
    orchestrationType: Optional[OrchestrationTypeType] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationUnion] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_agent' function.
class UpdateAgentRequest(BaseValidatorModel):
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    foundationModel: str
    agentCollaboration: Optional[AgentCollaborationType] = None
    customOrchestration: Optional[CustomOrchestration] = None
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    idleSessionTTLInSeconds: Optional[int] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationUnion] = None
    orchestrationType: Optional[OrchestrationTypeType] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationUnion] = None


class ConfluenceDataSourceConfigurationOutput(BaseValidatorModel):
    sourceConfiguration: ConfluenceSourceConfiguration
    crawlerConfiguration: Optional[ConfluenceCrawlerConfigurationOutput] = None


class SalesforceDataSourceConfigurationOutput(BaseValidatorModel):
    sourceConfiguration: SalesforceSourceConfiguration
    crawlerConfiguration: Optional[SalesforceCrawlerConfigurationOutput] = None


class SharePointDataSourceConfigurationOutput(BaseValidatorModel):
    sourceConfiguration: SharePointSourceConfigurationOutput
    crawlerConfiguration: Optional[SharePointCrawlerConfigurationOutput] = None


class ConfluenceDataSourceConfiguration(BaseValidatorModel):
    sourceConfiguration: ConfluenceSourceConfiguration
    crawlerConfiguration: Optional[ConfluenceCrawlerConfiguration] = None


class SalesforceDataSourceConfiguration(BaseValidatorModel):
    sourceConfiguration: SalesforceSourceConfiguration
    crawlerConfiguration: Optional[SalesforceCrawlerConfiguration] = None


class SharePointDataSourceConfiguration(BaseValidatorModel):
    sourceConfiguration: SharePointSourceConfiguration
    crawlerConfiguration: Optional[SharePointCrawlerConfiguration] = None


class RedshiftConfigurationOutput(BaseValidatorModel):
    queryEngineConfiguration: RedshiftQueryEngineConfiguration
    storageConfigurations: List[RedshiftQueryEngineStorageConfigurationOutput]
    queryGenerationConfiguration: Optional[QueryGenerationConfigurationOutput] = None


class RedshiftConfiguration(BaseValidatorModel):
    queryEngineConfiguration: RedshiftQueryEngineConfiguration
    storageConfigurations: List[RedshiftQueryEngineStorageConfiguration]
    queryGenerationConfiguration: Optional[QueryGenerationConfiguration] = None


class ChatPromptTemplateConfigurationOutput(BaseValidatorModel):
    messages: List[MessageOutput]
    inputVariables: Optional[List[PromptInputVariable]] = None
    system: Optional[List[SystemContentBlock]] = None
    toolConfiguration: Optional[ToolConfigurationOutput] = None


class Tool(BaseValidatorModel):
    cachePoint: Optional[CachePointBlock] = None
    toolSpec: Optional[ToolSpecificationUnion] = None


class VectorIngestionConfigurationOutput(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfigurationOutput] = None
    contextEnrichmentConfiguration: Optional[ContextEnrichmentConfiguration] = None
    customTransformationConfiguration: Optional[CustomTransformationConfigurationOutput] = None
    parsingConfiguration: Optional[ParsingConfiguration] = None


class VectorIngestionConfiguration(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfiguration] = None
    contextEnrichmentConfiguration: Optional[ContextEnrichmentConfiguration] = None
    customTransformationConfiguration: Optional[CustomTransformationConfiguration] = None
    parsingConfiguration: Optional[ParsingConfiguration] = None


class KnowledgeBaseDocument(BaseValidatorModel):
    content: DocumentContent
    metadata: Optional[DocumentMetadata] = None


class DataSourceConfigurationOutput(BaseValidatorModel):
    type: DataSourceTypeType
    confluenceConfiguration: Optional[ConfluenceDataSourceConfigurationOutput] = None
    s3Configuration: Optional[S3DataSourceConfigurationOutput] = None
    salesforceConfiguration: Optional[SalesforceDataSourceConfigurationOutput] = None
    sharePointConfiguration: Optional[SharePointDataSourceConfigurationOutput] = None
    webConfiguration: Optional[WebDataSourceConfigurationOutput] = None


class DataSourceConfiguration(BaseValidatorModel):
    type: DataSourceTypeType
    confluenceConfiguration: Optional[ConfluenceDataSourceConfiguration] = None
    s3Configuration: Optional[S3DataSourceConfiguration] = None
    salesforceConfiguration: Optional[SalesforceDataSourceConfiguration] = None
    sharePointConfiguration: Optional[SharePointDataSourceConfiguration] = None
    webConfiguration: Optional[WebDataSourceConfiguration] = None


class SqlKnowledgeBaseConfigurationOutput(BaseValidatorModel):
    type: Literal['REDSHIFT']
    redshiftConfiguration: Optional[RedshiftConfigurationOutput] = None


class SqlKnowledgeBaseConfiguration(BaseValidatorModel):
    type: Literal['REDSHIFT']
    redshiftConfiguration: Optional[RedshiftConfiguration] = None


class PromptTemplateConfigurationOutput(BaseValidatorModel):
    chat: Optional[ChatPromptTemplateConfigurationOutput] = None
    text: Optional[TextPromptTemplateConfigurationOutput] = None

ToolUnion = Union[Tool, ToolOutput]

VectorIngestionConfigurationUnion = Union[VectorIngestionConfiguration, VectorIngestionConfigurationOutput]


# This class is the input for the 'ingest_knowledge_base_documents' function.
class IngestKnowledgeBaseDocumentsRequest(BaseValidatorModel):
    dataSourceId: str
    documents: List[KnowledgeBaseDocument]
    knowledgeBaseId: str
    clientToken: Optional[str] = None


class DataSource(BaseValidatorModel):
    createdAt: datetime
    dataSourceConfiguration: DataSourceConfigurationOutput
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    status: DataSourceStatusType
    updatedAt: datetime
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationOutput] = None

DataSourceConfigurationUnion = Union[DataSourceConfiguration, DataSourceConfigurationOutput]


class KnowledgeBaseConfigurationOutput(BaseValidatorModel):
    type: KnowledgeBaseTypeType
    kendraKnowledgeBaseConfiguration: Optional[KendraKnowledgeBaseConfiguration] = None
    sqlKnowledgeBaseConfiguration: Optional[SqlKnowledgeBaseConfigurationOutput] = None
    vectorKnowledgeBaseConfiguration: Optional[VectorKnowledgeBaseConfigurationOutput] = None


class KnowledgeBaseConfiguration(BaseValidatorModel):
    type: KnowledgeBaseTypeType
    kendraKnowledgeBaseConfiguration: Optional[KendraKnowledgeBaseConfiguration] = None
    sqlKnowledgeBaseConfiguration: Optional[SqlKnowledgeBaseConfiguration] = None
    vectorKnowledgeBaseConfiguration: Optional[VectorKnowledgeBaseConfiguration] = None


class PromptFlowNodeInlineConfigurationOutput(BaseValidatorModel):
    modelId: str
    templateConfiguration: PromptTemplateConfigurationOutput
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    inferenceConfiguration: Optional[PromptInferenceConfigurationOutput] = None


class PromptVariantOutput(BaseValidatorModel):
    name: str
    templateConfiguration: PromptTemplateConfigurationOutput
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    genAiResource: Optional[PromptGenAiResource] = None
    inferenceConfiguration: Optional[PromptInferenceConfigurationOutput] = None
    metadata: Optional[List[PromptMetadataEntry]] = None
    modelId: Optional[str] = None


class ToolConfiguration(BaseValidatorModel):
    tools: List[ToolUnion]
    toolChoice: Optional[ToolChoiceUnion] = None


# This class is the output for the 'create_data_source' function.
class CreateDataSourceResponse(BaseValidatorModel):
    dataSource: DataSource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_data_source' function.
class GetDataSourceResponse(BaseValidatorModel):
    dataSource: DataSource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_data_source' function.
class UpdateDataSourceResponse(BaseValidatorModel):
    dataSource: DataSource
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_data_source' function.
class CreateDataSourceRequest(BaseValidatorModel):
    dataSourceConfiguration: DataSourceConfigurationUnion
    knowledgeBaseId: str
    name: str
    clientToken: Optional[str] = None
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationUnion] = None


# This class is the input for the 'update_data_source' function.
class UpdateDataSourceRequest(BaseValidatorModel):
    dataSourceConfiguration: DataSourceConfigurationUnion
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationUnion] = None


class KnowledgeBase(BaseValidatorModel):
    createdAt: datetime
    knowledgeBaseArn: str
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationOutput
    knowledgeBaseId: str
    name: str
    roleArn: str
    status: KnowledgeBaseStatusType
    updatedAt: datetime
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    storageConfiguration: Optional[StorageConfiguration] = None

KnowledgeBaseConfigurationUnion = Union[KnowledgeBaseConfiguration, KnowledgeBaseConfigurationOutput]


class PromptFlowNodeSourceConfigurationOutput(BaseValidatorModel):
    inline: Optional[PromptFlowNodeInlineConfigurationOutput] = None
    resource: Optional[PromptFlowNodeResourceConfiguration] = None


# This class is the output for the 'create_prompt' function.
class CreatePromptResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    defaultVariant: str
    description: str
    id: str
    name: str
    updatedAt: datetime
    variants: List[PromptVariantOutput]
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_prompt_version' function.
class CreatePromptVersionResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    defaultVariant: str
    description: str
    id: str
    name: str
    updatedAt: datetime
    variants: List[PromptVariantOutput]
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_prompt' function.
class GetPromptResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    defaultVariant: str
    description: str
    id: str
    name: str
    updatedAt: datetime
    variants: List[PromptVariantOutput]
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_prompt' function.
class UpdatePromptResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    defaultVariant: str
    description: str
    id: str
    name: str
    updatedAt: datetime
    variants: List[PromptVariantOutput]
    version: str
    ResponseMetadata: ResponseMetadata

ToolConfigurationUnion = Union[ToolConfiguration, ToolConfigurationOutput]


# This class is the output for the 'create_knowledge_base' function.
class CreateKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBase: KnowledgeBase
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_knowledge_base' function.
class GetKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBase: KnowledgeBase
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_knowledge_base' function.
class UpdateKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBase: KnowledgeBase
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_knowledge_base' function.
class CreateKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationUnion
    name: str
    roleArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    storageConfiguration: Optional[StorageConfiguration] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_knowledge_base' function.
class UpdateKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationUnion
    knowledgeBaseId: str
    name: str
    roleArn: str
    description: Optional[str] = None
    storageConfiguration: Optional[StorageConfiguration] = None


class PromptFlowNodeConfigurationOutput(BaseValidatorModel):
    sourceConfiguration: PromptFlowNodeSourceConfigurationOutput
    guardrailConfiguration: Optional[GuardrailConfiguration] = None


class ChatPromptTemplateConfiguration(BaseValidatorModel):
    messages: List[MessageUnion]
    inputVariables: Optional[List[PromptInputVariable]] = None
    system: Optional[List[SystemContentBlock]] = None
    toolConfiguration: Optional[ToolConfigurationUnion] = None


class FlowNodeConfigurationOutput(BaseValidatorModel):
    agent: Optional[AgentFlowNodeConfiguration] = None
    collector: Optional[Dict[str, Any]] = None
    condition: Optional[ConditionFlowNodeConfigurationOutput] = None
    input: Optional[Dict[str, Any]] = None
    iterator: Optional[Dict[str, Any]] = None
    knowledgeBase: Optional[KnowledgeBaseFlowNodeConfiguration] = None
    lambdaFunction: Optional[LambdaFunctionFlowNodeConfiguration] = None
    lex: Optional[LexFlowNodeConfiguration] = None
    output: Optional[Dict[str, Any]] = None
    prompt: Optional[PromptFlowNodeConfigurationOutput] = None
    retrieval: Optional[RetrievalFlowNodeConfiguration] = None
    storage: Optional[StorageFlowNodeConfiguration] = None

ChatPromptTemplateConfigurationUnion = Union[ChatPromptTemplateConfiguration, ChatPromptTemplateConfigurationOutput]


class FlowNodeExtra(BaseValidatorModel):
    name: str
    type: FlowNodeTypeType
    configuration: Optional[FlowNodeConfigurationOutput] = None
    inputs: Optional[List[FlowNodeInput]] = None
    outputs: Optional[List[FlowNodeOutput]] = None


class PromptTemplateConfiguration(BaseValidatorModel):
    chat: Optional[ChatPromptTemplateConfigurationUnion] = None
    text: Optional[TextPromptTemplateConfigurationUnion] = None


class FlowDefinitionOutput(BaseValidatorModel):
    connections: Optional[List[FlowConnection]] = None
    nodes: Optional[List[FlowNodeExtra]] = None


class PromptFlowNodeInlineConfiguration(BaseValidatorModel):
    modelId: str
    templateConfiguration: PromptTemplateConfiguration
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    inferenceConfiguration: Optional[PromptInferenceConfiguration] = None

PromptTemplateConfigurationUnion = Union[PromptTemplateConfiguration, PromptTemplateConfigurationOutput]


# This class is the output for the 'create_flow' function.
class CreateFlowResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutput
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    updatedAt: datetime
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_flow_version' function.
class CreateFlowVersionResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutput
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_flow' function.
class GetFlowResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutput
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    updatedAt: datetime
    validations: List[FlowValidation]
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_flow_version' function.
class GetFlowVersionResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutput
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_flow' function.
class UpdateFlowResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutput
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    updatedAt: datetime
    version: str
    ResponseMetadata: ResponseMetadata


class PromptFlowNodeSourceConfiguration(BaseValidatorModel):
    inline: Optional[PromptFlowNodeInlineConfiguration] = None
    resource: Optional[PromptFlowNodeResourceConfiguration] = None


class PromptVariant(BaseValidatorModel):
    name: str
    templateConfiguration: PromptTemplateConfigurationUnion
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    genAiResource: Optional[PromptGenAiResource] = None
    inferenceConfiguration: Optional[PromptInferenceConfigurationUnion] = None
    metadata: Optional[List[PromptMetadataEntry]] = None
    modelId: Optional[str] = None


class PromptFlowNodeConfiguration(BaseValidatorModel):
    sourceConfiguration: PromptFlowNodeSourceConfiguration
    guardrailConfiguration: Optional[GuardrailConfiguration] = None

PromptVariantUnion = Union[PromptVariant, PromptVariantOutput]


class FlowNodeConfiguration(BaseValidatorModel):
    agent: Optional[AgentFlowNodeConfiguration] = None
    collector: Optional[Dict[str, Any]] = None
    condition: Optional[ConditionFlowNodeConfiguration] = None
    input: Optional[Dict[str, Any]] = None
    iterator: Optional[Dict[str, Any]] = None
    knowledgeBase: Optional[KnowledgeBaseFlowNodeConfiguration] = None
    lambdaFunction: Optional[LambdaFunctionFlowNodeConfiguration] = None
    lex: Optional[LexFlowNodeConfiguration] = None
    output: Optional[Dict[str, Any]] = None
    prompt: Optional[PromptFlowNodeConfiguration] = None
    retrieval: Optional[RetrievalFlowNodeConfiguration] = None
    storage: Optional[StorageFlowNodeConfiguration] = None


# This class is the input for the 'create_prompt' function.
class CreatePromptRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    variants: Optional[List[PromptVariantUnion]] = None


# This class is the input for the 'update_prompt' function.
class UpdatePromptRequest(BaseValidatorModel):
    name: str
    promptIdentifier: str
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    variants: Optional[List[PromptVariantUnion]] = None


class FlowNode(BaseValidatorModel):
    name: str
    type: FlowNodeTypeType
    configuration: Optional[FlowNodeConfiguration] = None
    inputs: Optional[List[FlowNodeInput]] = None
    outputs: Optional[List[FlowNodeOutput]] = None


class FlowDefinition(BaseValidatorModel):
    connections: Optional[List[FlowConnection]] = None
    nodes: Optional[List[FlowNode]] = None

FlowDefinitionUnion = Union[FlowDefinition, FlowDefinitionOutput]


# This class is the input for the 'create_flow' function.
class CreateFlowRequest(BaseValidatorModel):
    executionRoleArn: str
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionUnion] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_flow' function.
class UpdateFlowRequest(BaseValidatorModel):
    executionRoleArn: str
    flowIdentifier: str
    name: str
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionUnion] = None
    description: Optional[str] = None


# This class is the input for the 'validate_flow_definition' function.
class ValidateFlowDefinitionRequest(BaseValidatorModel):
    definition: FlowDefinitionUnion
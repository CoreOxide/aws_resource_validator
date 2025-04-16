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
from aws_resource_validator.pydantic_models.bedrock_agent_constants import *

class S3Identifier(BaseValidatorModel):
    s3BucketName: Optional[str] = None
    s3ObjectKey: Optional[str] = None


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


class AssociateAgentKnowledgeBaseRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: Optional[KnowledgeBaseStateType] = None


class BedrockDataAutomationConfiguration(BaseValidatorModel):
    parsingModality: Optional[Literal["MULTIMODAL"]] = None


class BedrockEmbeddingModelConfiguration(BaseValidatorModel):
    dimensions: Optional[int] = None
    embeddingDataType: Optional[EmbeddingDataTypeType] = None


class ParsingPrompt(BaseValidatorModel):
    parsingPromptText: str


class EnrichmentStrategyConfiguration(BaseValidatorModel):
    method: Literal["CHUNK_ENTITY_EXTRACTION"]


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
    hostType: Literal["SAAS"]
    hostUrl: str


class ServerSideEncryptionConfiguration(BaseValidatorModel):
    kmsKeyArn: Optional[str] = None


class FlowAliasRoutingConfigurationListItem(BaseValidatorModel):
    flowVersion: Optional[str] = None


class CreateFlowVersionRequest(BaseValidatorModel):
    flowIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class CreatePromptVersionRequest(BaseValidatorModel):
    promptIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CuratedQuery(BaseValidatorModel):
    naturalLanguage: str
    sql: str


class CustomS3Location(BaseValidatorModel):
    uri: str
    bucketOwnerAccountId: Optional[str] = None


class CyclicConnectionFlowValidationDetails(BaseValidatorModel):
    connection: str


class S3DataSourceConfigurationOutput(BaseValidatorModel):
    bucketArn: str
    bucketOwnerAccountId: Optional[str] = None
    inclusionPrefixes: Optional[List[str]] = None


class S3DataSourceConfiguration(BaseValidatorModel):
    bucketArn: str
    bucketOwnerAccountId: Optional[str] = None
    inclusionPrefixes: Optional[Sequence[str]] = None


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


class DeleteAgentAliasRequest(BaseValidatorModel):
    agentAliasId: str
    agentId: str


class DeleteAgentRequest(BaseValidatorModel):
    agentId: str
    skipResourceInUseCheck: Optional[bool] = None


class DeleteAgentVersionRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: Optional[bool] = None


class DeleteDataSourceRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str


class DeleteFlowAliasRequest(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str


class DeleteFlowRequest(BaseValidatorModel):
    flowIdentifier: str
    skipResourceInUseCheck: Optional[bool] = None


class DeleteFlowVersionRequest(BaseValidatorModel):
    flowIdentifier: str
    flowVersion: str
    skipResourceInUseCheck: Optional[bool] = None


class DeleteKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseId: str


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


class IncompatibleConnectionDataTypeFlowValidationDetails(BaseValidatorModel):
    connection: str


class MalformedConditionExpressionFlowValidationDetails(BaseValidatorModel):
    cause: str
    condition: str
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


class MissingNodeOutputFlowValidationDetails(BaseValidatorModel):
    node: str
    output: str


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


class UnknownNodeOutputFlowValidationDetails(BaseValidatorModel):
    node: str
    output: str


class UnreachableNodeFlowValidationDetails(BaseValidatorModel):
    node: str


class UnsatisfiedConnectionConditionsFlowValidationDetails(BaseValidatorModel):
    connection: str


class GetAgentActionGroupRequest(BaseValidatorModel):
    actionGroupId: str
    agentId: str
    agentVersion: str


class GetAgentAliasRequest(BaseValidatorModel):
    agentAliasId: str
    agentId: str


class GetAgentCollaboratorRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    collaboratorId: str


class GetAgentKnowledgeBaseRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str


class GetAgentRequest(BaseValidatorModel):
    agentId: str


class GetAgentVersionRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str


class GetDataSourceRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str


class GetFlowAliasRequest(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str


class GetFlowRequest(BaseValidatorModel):
    flowIdentifier: str


class GetFlowVersionRequest(BaseValidatorModel):
    flowIdentifier: str
    flowVersion: str


class GetIngestionJobRequest(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str


class GetKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseId: str


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
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None


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


class ListAgentActionGroupsRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentAliasesRequest(BaseValidatorModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentCollaboratorsRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentKnowledgeBasesRequest(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentVersionsRequest(BaseValidatorModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDataSourcesRequest(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFlowAliasesRequest(BaseValidatorModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFlowVersionsRequest(BaseValidatorModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFlowsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKnowledgeBaseDocumentsRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKnowledgeBasesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPromptsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    promptIdentifier: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class SessionSummaryConfiguration(BaseValidatorModel):
    maxRecentSessions: Optional[int] = None


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
    exclusionFilters: Optional[Sequence[str]] = None
    inclusionFilters: Optional[Sequence[str]] = None


class PineconeFieldMapping(BaseValidatorModel):
    metadataField: str
    textField: str


class PrepareAgentRequest(BaseValidatorModel):
    agentId: str


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
    stopSequences: Optional[Sequence[str]] = None
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


class RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutput(BaseValidatorModel):
    tableNames: List[str]


class RedshiftQueryEngineAwsDataCatalogStorageConfiguration(BaseValidatorModel):
    tableNames: Sequence[str]


class RedshiftQueryEngineRedshiftStorageConfiguration(BaseValidatorModel):
    databaseName: str


class RetrievalFlowNodeS3Configuration(BaseValidatorModel):
    bucketName: str


class SalesforceSourceConfiguration(BaseValidatorModel):
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str
    hostUrl: str


class SeedUrl(BaseValidatorModel):
    url: Optional[str] = None


class SharePointSourceConfigurationOutput(BaseValidatorModel):
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: List[str]
    tenantId: Optional[str] = None


class SharePointSourceConfiguration(BaseValidatorModel):
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: Sequence[str]
    tenantId: Optional[str] = None


class SpecificToolChoice(BaseValidatorModel):
    name: str


class StartIngestionJobRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class StopIngestionJobRequest(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str


class StorageFlowNodeS3Configuration(BaseValidatorModel):
    bucketName: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class ToolInputSchemaOutput(BaseValidatorModel):
    json: Optional[Dict[str, Any]] = None


class ToolInputSchema(BaseValidatorModel):
    json: Optional[Mapping[str, Any]] = None


class TransformationLambdaConfiguration(BaseValidatorModel):
    lambdaArn: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


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


class CreateAgentAliasRequest(BaseValidatorModel):
    agentAliasName: str
    agentId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    routingConfiguration: Optional[Sequence[AgentAliasRoutingConfigurationListItem]] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateAgentAliasRequest(BaseValidatorModel):
    agentAliasId: str
    agentAliasName: str
    agentId: str
    description: Optional[str] = None
    routingConfiguration: Optional[Sequence[AgentAliasRoutingConfigurationListItem]] = None


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


class AssociateAgentCollaboratorRequest(BaseValidatorModel):
    agentDescriptor: AgentDescriptor
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorName: str
    clientToken: Optional[str] = None
    relayConversationHistory: Optional[RelayConversationHistoryType] = None


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


class AssociateAgentKnowledgeBaseResponse(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBase
    ResponseMetadata: ResponseMetadata


class DeleteAgentAliasResponse(BaseValidatorModel):
    agentAliasId: str
    agentAliasStatus: AgentAliasStatusType
    agentId: str
    ResponseMetadata: ResponseMetadata


class DeleteAgentResponse(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    ResponseMetadata: ResponseMetadata


class DeleteAgentVersionResponse(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    ResponseMetadata: ResponseMetadata


class DeleteDataSourceResponse(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    status: DataSourceStatusType
    ResponseMetadata: ResponseMetadata


class DeleteKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBaseId: str
    status: KnowledgeBaseStatusType
    ResponseMetadata: ResponseMetadata


class GetAgentKnowledgeBaseResponse(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBase
    ResponseMetadata: ResponseMetadata


class ListAgentActionGroupsResponse(BaseValidatorModel):
    actionGroupSummaries: List[ActionGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAgentKnowledgeBasesResponse(BaseValidatorModel):
    agentKnowledgeBaseSummaries: List[AgentKnowledgeBaseSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PrepareAgentResponse(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    preparedAt: datetime
    ResponseMetadata: ResponseMetadata


class UpdateAgentKnowledgeBaseResponse(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBase
    ResponseMetadata: ResponseMetadata


class EmbeddingModelConfiguration(BaseValidatorModel):
    bedrockEmbeddingModelConfiguration: Optional[BedrockEmbeddingModelConfiguration] = None


class BedrockFoundationModelConfiguration(BaseValidatorModel):
    modelArn: str
    parsingModality: Optional[Literal["MULTIMODAL"]] = None
    parsingPrompt: Optional[ParsingPrompt] = None


class BedrockFoundationModelContextEnrichmentConfiguration(BaseValidatorModel):
    enrichmentStrategyConfiguration: EnrichmentStrategyConfiguration
    modelArn: str


class Blob(BaseValidatorModel):
    pass


class ByteContentDoc(BaseValidatorModel):
    data: Blob
    mimeType: str


class CachePointBlock(BaseValidatorModel):
    pass


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
    inputVariables: Optional[Sequence[PromptInputVariable]] = None


class ConditionFlowNodeConfigurationOutput(BaseValidatorModel):
    conditions: List[FlowCondition]


class ConditionFlowNodeConfiguration(BaseValidatorModel):
    conditions: Sequence[FlowCondition]


class CreateFlowAliasRequest(BaseValidatorModel):
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItem]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateFlowAliasRequest(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItem]
    description: Optional[str] = None


class OrchestrationExecutor(BaseValidatorModel):
    pass


class CustomOrchestration(BaseValidatorModel):
    executor: Optional[OrchestrationExecutor] = None


class ListDataSourcesResponse(BaseValidatorModel):
    dataSourceSummaries: List[DataSourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CustomDocumentIdentifier(BaseValidatorModel):
    pass


class DocumentIdentifier(BaseValidatorModel):
    dataSourceType: ContentDataSourceTypeType
    custom: Optional[CustomDocumentIdentifier] = None
    s3: Optional[S3Location] = None


class IntermediateStorage(BaseValidatorModel):
    s3Location: S3Location


class S3Content(BaseValidatorModel):
    s3Location: S3Location


class FlowConnectionConfiguration(BaseValidatorModel):
    conditional: Optional[FlowConditionalConnectionConfiguration] = None
    data: Optional[FlowDataConnectionConfiguration] = None


class FlowSummary(BaseValidatorModel):
    pass


class ListFlowsResponse(BaseValidatorModel):
    flowSummaries: List[FlowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MismatchedNodeInputTypeFlowValidationDetails(BaseValidatorModel):
    pass


class UnknownNodeInputFlowValidationDetails(BaseValidatorModel):
    pass


class UnfulfilledNodeInputFlowValidationDetails(BaseValidatorModel):
    pass


class MultipleNodeInputConnectionsFlowValidationDetails(BaseValidatorModel):
    pass


class MissingNodeInputFlowValidationDetails(BaseValidatorModel):
    pass


class MalformedNodeInputExpressionFlowValidationDetails(BaseValidatorModel):
    pass


class FlowValidationDetails(BaseValidatorModel):
    cyclicConnection: Optional[CyclicConnectionFlowValidationDetails] = None
    duplicateConditionExpression: Optional[ DuplicateConditionExpressionFlowValidationDetails ] = None
    duplicateConnections: Optional[DuplicateConnectionsFlowValidationDetails] = None
    incompatibleConnectionDataType: Optional[ IncompatibleConnectionDataTypeFlowValidationDetails ] = None
    malformedConditionExpression: Optional[ MalformedConditionExpressionFlowValidationDetails ] = None
    malformedNodeInputExpression: Optional[ MalformedNodeInputExpressionFlowValidationDetails ] = None
    mismatchedNodeInputType: Optional[MismatchedNodeInputTypeFlowValidationDetails] = None
    mismatchedNodeOutputType: Optional[MismatchedNodeOutputTypeFlowValidationDetails] = None
    missingConnectionConfiguration: Optional[ MissingConnectionConfigurationFlowValidationDetails ] = None
    missingDefaultCondition: Optional[MissingDefaultConditionFlowValidationDetails] = None
    missingEndingNodes: Optional[Dict[str, Any]] = None
    missingNodeConfiguration: Optional[MissingNodeConfigurationFlowValidationDetails] = None
    missingNodeInput: Optional[MissingNodeInputFlowValidationDetails] = None
    missingNodeOutput: Optional[MissingNodeOutputFlowValidationDetails] = None
    missingStartingNodes: Optional[Dict[str, Any]] = None
    multipleNodeInputConnections: Optional[ MultipleNodeInputConnectionsFlowValidationDetails ] = None
    unfulfilledNodeInput: Optional[UnfulfilledNodeInputFlowValidationDetails] = None
    unknownConnectionCondition: Optional[UnknownConnectionConditionFlowValidationDetails] = None
    unknownConnectionSource: Optional[UnknownConnectionSourceFlowValidationDetails] = None
    unknownConnectionSourceOutput: Optional[ UnknownConnectionSourceOutputFlowValidationDetails ] = None
    unknownConnectionTarget: Optional[UnknownConnectionTargetFlowValidationDetails] = None
    unknownConnectionTargetInput: Optional[ UnknownConnectionTargetInputFlowValidationDetails ] = None
    unknownNodeInput: Optional[UnknownNodeInputFlowValidationDetails] = None
    unknownNodeOutput: Optional[UnknownNodeOutputFlowValidationDetails] = None
    unreachableNode: Optional[UnreachableNodeFlowValidationDetails] = None
    unsatisfiedConnectionConditions: Optional[ UnsatisfiedConnectionConditionsFlowValidationDetails ] = None
    unspecified: Optional[Dict[str, Any]] = None


class FlowVersionSummary(BaseValidatorModel):
    pass


class ListFlowVersionsResponse(BaseValidatorModel):
    flowVersionSummaries: List[FlowVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ParameterDetail(BaseValidatorModel):
    pass


class FunctionOutput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, ParameterDetail]] = None
    requireConfirmation: Optional[RequireConfirmationType] = None


class Function(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Mapping[str, ParameterDetail]] = None
    requireConfirmation: Optional[RequireConfirmationType] = None


class HierarchicalChunkingConfigurationOutput(BaseValidatorModel):
    levelConfigurations: List[HierarchicalChunkingLevelConfiguration]
    overlapTokens: int


class HierarchicalChunkingConfiguration(BaseValidatorModel):
    levelConfigurations: Sequence[HierarchicalChunkingLevelConfiguration]
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
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    basePromptTemplate: Optional[str] = None
    foundationModel: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfiguration] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None


class IngestionJobFilter(BaseValidatorModel):
    pass


class ListIngestionJobsRequest(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    filters: Optional[Sequence[IngestionJobFilter]] = None
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
    filters: Optional[Sequence[IngestionJobFilter]] = None
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


class PromptSummary(BaseValidatorModel):
    pass


class ListPromptsResponse(BaseValidatorModel):
    promptSummaries: List[PromptSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MemoryConfigurationOutput(BaseValidatorModel):
    enabledMemoryTypes: List[Literal["SESSION_SUMMARY"]]
    sessionSummaryConfiguration: Optional[SessionSummaryConfiguration] = None
    storageDays: Optional[int] = None


class MemoryConfiguration(BaseValidatorModel):
    enabledMemoryTypes: Sequence[Literal["SESSION_SUMMARY"]]
    sessionSummaryConfiguration: Optional[SessionSummaryConfiguration] = None
    storageDays: Optional[int] = None


class MetadataAttributeValue(BaseValidatorModel):
    pass


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
    filters: Sequence[PatternObjectFilter]


class PineconeConfiguration(BaseValidatorModel):
    connectionString: str
    credentialsSecretArn: str
    fieldMapping: PineconeFieldMapping
    namespace: Optional[str] = None


class PromptGenAiResource(BaseValidatorModel):
    agent: Optional[PromptAgentResource] = None


class PromptInferenceConfigurationOutput(BaseValidatorModel):
    text: Optional[PromptModelInferenceConfigurationOutput] = None


class QueryGenerationTableOutput(BaseValidatorModel):
    name: str
    columns: Optional[List[QueryGenerationColumn]] = None
    description: Optional[str] = None
    inclusion: Optional[IncludeExcludeType] = None


class QueryGenerationTable(BaseValidatorModel):
    name: str
    columns: Optional[Sequence[QueryGenerationColumn]] = None
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


class RedshiftProvisionedAuthConfiguration(BaseValidatorModel):
    pass


class RedshiftProvisionedConfiguration(BaseValidatorModel):
    authConfiguration: RedshiftProvisionedAuthConfiguration
    clusterIdentifier: str


class RedshiftServerlessAuthConfiguration(BaseValidatorModel):
    pass


class RedshiftServerlessConfiguration(BaseValidatorModel):
    authConfiguration: RedshiftServerlessAuthConfiguration
    workgroupArn: str


class RetrievalFlowNodeServiceConfiguration(BaseValidatorModel):
    s3: Optional[RetrievalFlowNodeS3Configuration] = None


class UrlConfigurationOutput(BaseValidatorModel):
    seedUrls: Optional[List[SeedUrl]] = None


class UrlConfiguration(BaseValidatorModel):
    seedUrls: Optional[Sequence[SeedUrl]] = None


class StorageFlowNodeServiceConfiguration(BaseValidatorModel):
    s3: Optional[StorageFlowNodeS3Configuration] = None


class ToolSpecificationOutput(BaseValidatorModel):
    inputSchema: ToolInputSchemaOutput
    name: str
    description: Optional[str] = None


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
    exclusionFilters: Optional[Sequence[str]] = None
    inclusionFilters: Optional[Sequence[str]] = None
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


class ListAgentAliasesResponse(BaseValidatorModel):
    agentAliasSummaries: List[AgentAliasSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAgentCollaboratorsResponse(BaseValidatorModel):
    agentCollaboratorSummaries: List[AgentCollaboratorSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssociateAgentCollaboratorResponse(BaseValidatorModel):
    agentCollaborator: AgentCollaborator
    ResponseMetadata: ResponseMetadata


class GetAgentCollaboratorResponse(BaseValidatorModel):
    agentCollaborator: AgentCollaborator
    ResponseMetadata: ResponseMetadata


class UpdateAgentCollaboratorResponse(BaseValidatorModel):
    agentCollaborator: AgentCollaborator
    ResponseMetadata: ResponseMetadata


class ListAgentsResponse(BaseValidatorModel):
    agentSummaries: List[AgentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAgentVersionsResponse(BaseValidatorModel):
    agentVersionSummaries: List[AgentVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ParsingConfiguration(BaseValidatorModel):
    parsingStrategy: ParsingStrategyType
    bedrockDataAutomationConfiguration: Optional[BedrockDataAutomationConfiguration] = None
    bedrockFoundationModelConfiguration: Optional[BedrockFoundationModelConfiguration] = None


class MessageOutput(BaseValidatorModel):
    content: List[ContentBlock]
    role: ConversationRoleType


class Message(BaseValidatorModel):
    content: Sequence[ContentBlock]
    role: ConversationRoleType


class FlowAliasSummary(BaseValidatorModel):
    pass


class ListFlowAliasesResponse(BaseValidatorModel):
    flowAliasSummaries: List[FlowAliasSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DeleteKnowledgeBaseDocumentsRequest(BaseValidatorModel):
    dataSourceId: str
    documentIdentifiers: Sequence[DocumentIdentifier]
    knowledgeBaseId: str
    clientToken: Optional[str] = None


class GetKnowledgeBaseDocumentsRequest(BaseValidatorModel):
    dataSourceId: str
    documentIdentifiers: Sequence[DocumentIdentifier]
    knowledgeBaseId: str


class KnowledgeBaseDocumentDetail(BaseValidatorModel):
    dataSourceId: str
    identifier: DocumentIdentifier
    knowledgeBaseId: str
    status: DocumentStatusType
    statusReason: Optional[str] = None
    updatedAt: Optional[datetime] = None


class SupplementalDataStorageLocation(BaseValidatorModel):
    pass


class SupplementalDataStorageConfigurationOutput(BaseValidatorModel):
    storageLocations: List[SupplementalDataStorageLocation]


class SupplementalDataStorageConfiguration(BaseValidatorModel):
    storageLocations: Sequence[SupplementalDataStorageLocation]


class FunctionSchemaOutput(BaseValidatorModel):
    functions: Optional[List[FunctionOutput]] = None


class FunctionSchema(BaseValidatorModel):
    functions: Optional[Sequence[Function]] = None


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
    promptConfigurations: Sequence[PromptConfiguration]
    overrideLambda: Optional[str] = None


class ListIngestionJobsResponse(BaseValidatorModel):
    ingestionJobSummaries: List[IngestionJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetIngestionJobResponse(BaseValidatorModel):
    ingestionJob: IngestionJob
    ResponseMetadata: ResponseMetadata


class StartIngestionJobResponse(BaseValidatorModel):
    ingestionJob: IngestionJob
    ResponseMetadata: ResponseMetadata


class StopIngestionJobResponse(BaseValidatorModel):
    ingestionJob: IngestionJob
    ResponseMetadata: ResponseMetadata


class PromptModelInferenceConfigurationUnion(BaseValidatorModel):
    pass


class PromptInferenceConfiguration(BaseValidatorModel):
    text: Optional[PromptModelInferenceConfigurationUnion] = None


class QueryGenerationContextOutput(BaseValidatorModel):
    curatedQueries: Optional[List[CuratedQuery]] = None
    tables: Optional[List[QueryGenerationTableOutput]] = None


class QueryGenerationContext(BaseValidatorModel):
    curatedQueries: Optional[Sequence[CuratedQuery]] = None
    tables: Optional[Sequence[QueryGenerationTable]] = None


class RetrievalFlowNodeConfiguration(BaseValidatorModel):
    serviceConfiguration: RetrievalFlowNodeServiceConfiguration


class WebSourceConfigurationOutput(BaseValidatorModel):
    urlConfiguration: UrlConfigurationOutput


class WebSourceConfiguration(BaseValidatorModel):
    urlConfiguration: UrlConfiguration


class StorageFlowNodeConfiguration(BaseValidatorModel):
    serviceConfiguration: StorageFlowNodeServiceConfiguration


class ToolOutput(BaseValidatorModel):
    cachePoint: Optional[CachePointBlock] = None
    toolSpec: Optional[ToolSpecificationOutput] = None


class ToolInputSchemaUnion(BaseValidatorModel):
    pass


class ToolSpecification(BaseValidatorModel):
    inputSchema: ToolInputSchemaUnion
    name: str
    description: Optional[str] = None


class Transformation(BaseValidatorModel):
    stepToApply: Literal["POST_CHUNKING"]
    transformationFunction: TransformationFunction


class CreateAgentAliasResponse(BaseValidatorModel):
    agentAlias: AgentAlias
    ResponseMetadata: ResponseMetadata


class GetAgentAliasResponse(BaseValidatorModel):
    agentAlias: AgentAlias
    ResponseMetadata: ResponseMetadata


class UpdateAgentAliasResponse(BaseValidatorModel):
    agentAlias: AgentAlias
    ResponseMetadata: ResponseMetadata


class InlineContent(BaseValidatorModel):
    pass


class CustomContent(BaseValidatorModel):
    customDocumentIdentifier: CustomDocumentIdentifier
    sourceType: CustomSourceTypeType
    inlineContent: Optional[InlineContent] = None
    s3Location: Optional[CustomS3Location] = None


class DeleteKnowledgeBaseDocumentsResponse(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetail]
    ResponseMetadata: ResponseMetadata


class GetKnowledgeBaseDocumentsResponse(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetail]
    ResponseMetadata: ResponseMetadata


class IngestKnowledgeBaseDocumentsResponse(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetail]
    ResponseMetadata: ResponseMetadata


class ListKnowledgeBaseDocumentsResponse(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class VectorKnowledgeBaseConfigurationOutput(BaseValidatorModel):
    embeddingModelArn: str
    embeddingModelConfiguration: Optional[EmbeddingModelConfiguration] = None
    supplementalDataStorageConfiguration: Optional[ SupplementalDataStorageConfigurationOutput ] = None


class VectorKnowledgeBaseConfiguration(BaseValidatorModel):
    embeddingModelArn: str
    embeddingModelConfiguration: Optional[EmbeddingModelConfiguration] = None
    supplementalDataStorageConfiguration: Optional[SupplementalDataStorageConfiguration] = None


class FlowValidation(BaseValidatorModel):
    pass


class ValidateFlowDefinitionResponse(BaseValidatorModel):
    validations: List[FlowValidation]
    ResponseMetadata: ResponseMetadata


class ActionGroupExecutor(BaseValidatorModel):
    pass


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


class CrawlFilterConfigurationOutput(BaseValidatorModel):
    pass


class ConfluenceCrawlerConfigurationOutput(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutput] = None


class SalesforceCrawlerConfigurationOutput(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutput] = None


class SharePointCrawlerConfigurationOutput(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutput] = None


class CrawlFilterConfiguration(BaseValidatorModel):
    pass


class ConfluenceCrawlerConfiguration(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfiguration] = None


class SalesforceCrawlerConfiguration(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfiguration] = None


class SharePointCrawlerConfiguration(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfiguration] = None


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


class ToolChoiceOutput(BaseValidatorModel):
    pass


class ToolConfigurationOutput(BaseValidatorModel):
    tools: List[ToolOutput]
    toolChoice: Optional[ToolChoiceOutput] = None


class CustomTransformationConfigurationOutput(BaseValidatorModel):
    intermediateStorage: IntermediateStorage
    transformations: List[Transformation]


class CustomTransformationConfiguration(BaseValidatorModel):
    intermediateStorage: IntermediateStorage
    transformations: Sequence[Transformation]


class DocumentContent(BaseValidatorModel):
    dataSourceType: ContentDataSourceTypeType
    custom: Optional[CustomContent] = None
    s3: Optional[S3Content] = None


class CreateAgentActionGroupResponse(BaseValidatorModel):
    agentActionGroup: AgentActionGroup
    ResponseMetadata: ResponseMetadata


class GetAgentActionGroupResponse(BaseValidatorModel):
    agentActionGroup: AgentActionGroup
    ResponseMetadata: ResponseMetadata


class UpdateAgentActionGroupResponse(BaseValidatorModel):
    agentActionGroup: AgentActionGroup
    ResponseMetadata: ResponseMetadata


class FunctionSchemaUnion(BaseValidatorModel):
    pass


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
    parentActionGroupSignatureParams: Optional[Mapping[str, str]] = None


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
    parentActionGroupSignatureParams: Optional[Mapping[str, str]] = None


class CreateAgentResponse(BaseValidatorModel):
    agent: Agent
    ResponseMetadata: ResponseMetadata


class GetAgentResponse(BaseValidatorModel):
    agent: Agent
    ResponseMetadata: ResponseMetadata


class UpdateAgentResponse(BaseValidatorModel):
    agent: Agent
    ResponseMetadata: ResponseMetadata


class GetAgentVersionResponse(BaseValidatorModel):
    agentVersion: AgentVersion
    ResponseMetadata: ResponseMetadata


class PromptOverrideConfigurationUnion(BaseValidatorModel):
    pass


class MemoryConfigurationUnion(BaseValidatorModel):
    pass


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
    tags: Optional[Mapping[str, str]] = None


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


class RedshiftQueryEngineConfiguration(BaseValidatorModel):
    pass


class RedshiftQueryEngineStorageConfigurationOutput(BaseValidatorModel):
    pass


class RedshiftConfigurationOutput(BaseValidatorModel):
    queryEngineConfiguration: RedshiftQueryEngineConfiguration
    storageConfigurations: List[RedshiftQueryEngineStorageConfigurationOutput]
    queryGenerationConfiguration: Optional[QueryGenerationConfigurationOutput] = None


class RedshiftQueryEngineStorageConfiguration(BaseValidatorModel):
    pass


class RedshiftConfiguration(BaseValidatorModel):
    queryEngineConfiguration: RedshiftQueryEngineConfiguration
    storageConfigurations: Sequence[RedshiftQueryEngineStorageConfiguration]
    queryGenerationConfiguration: Optional[QueryGenerationConfiguration] = None


class ChatPromptTemplateConfigurationOutput(BaseValidatorModel):
    messages: List[MessageOutput]
    inputVariables: Optional[List[PromptInputVariable]] = None
    system: Optional[List[SystemContentBlock]] = None
    toolConfiguration: Optional[ToolConfigurationOutput] = None


class ToolSpecificationUnion(BaseValidatorModel):
    pass


class Tool(BaseValidatorModel):
    cachePoint: Optional[CachePointBlock] = None
    toolSpec: Optional[ToolSpecificationUnion] = None


class ContextEnrichmentConfiguration(BaseValidatorModel):
    pass


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


class DocumentMetadata(BaseValidatorModel):
    pass


class KnowledgeBaseDocument(BaseValidatorModel):
    content: DocumentContent
    metadata: Optional[DocumentMetadata] = None


class PromptTemplateConfigurationOutput(BaseValidatorModel):
    chat: Optional[ChatPromptTemplateConfigurationOutput] = None
    text: Optional[TextPromptTemplateConfigurationOutput] = None


class IngestKnowledgeBaseDocumentsRequest(BaseValidatorModel):
    dataSourceId: str
    documents: Sequence[KnowledgeBaseDocument]
    knowledgeBaseId: str
    clientToken: Optional[str] = None


class DataSourceConfigurationOutput(BaseValidatorModel):
    pass


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


class ToolUnion(BaseValidatorModel):
    pass


class ToolChoiceUnion(BaseValidatorModel):
    pass


class ToolConfiguration(BaseValidatorModel):
    tools: Sequence[ToolUnion]
    toolChoice: Optional[ToolChoiceUnion] = None


class CreateDataSourceResponse(BaseValidatorModel):
    dataSource: DataSource
    ResponseMetadata: ResponseMetadata


class GetDataSourceResponse(BaseValidatorModel):
    dataSource: DataSource
    ResponseMetadata: ResponseMetadata


class UpdateDataSourceResponse(BaseValidatorModel):
    dataSource: DataSource
    ResponseMetadata: ResponseMetadata


class DataSourceConfigurationUnion(BaseValidatorModel):
    pass


class VectorIngestionConfigurationUnion(BaseValidatorModel):
    pass


class CreateDataSourceRequest(BaseValidatorModel):
    dataSourceConfiguration: DataSourceConfigurationUnion
    knowledgeBaseId: str
    name: str
    clientToken: Optional[str] = None
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationUnion] = None


class UpdateDataSourceRequest(BaseValidatorModel):
    dataSourceConfiguration: DataSourceConfigurationUnion
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationUnion] = None


class KnowledgeBaseConfigurationOutput(BaseValidatorModel):
    pass


class StorageConfiguration(BaseValidatorModel):
    pass


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


class PromptFlowNodeSourceConfigurationOutput(BaseValidatorModel):
    inline: Optional[PromptFlowNodeInlineConfigurationOutput] = None
    resource: Optional[PromptFlowNodeResourceConfiguration] = None


class CreateKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBase: KnowledgeBase
    ResponseMetadata: ResponseMetadata


class GetKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBase: KnowledgeBase
    ResponseMetadata: ResponseMetadata


class UpdateKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBase: KnowledgeBase
    ResponseMetadata: ResponseMetadata


class KnowledgeBaseConfigurationUnion(BaseValidatorModel):
    pass


class CreateKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationUnion
    name: str
    roleArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    storageConfiguration: Optional[StorageConfiguration] = None
    tags: Optional[Mapping[str, str]] = None


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


class ToolConfigurationUnion(BaseValidatorModel):
    pass


class MessageUnion(BaseValidatorModel):
    pass


class ChatPromptTemplateConfiguration(BaseValidatorModel):
    messages: Sequence[MessageUnion]
    inputVariables: Optional[Sequence[PromptInputVariable]] = None
    system: Optional[Sequence[SystemContentBlock]] = None
    toolConfiguration: Optional[ToolConfigurationUnion] = None


class TextPromptTemplateConfigurationUnion(BaseValidatorModel):
    pass


class ChatPromptTemplateConfigurationUnion(BaseValidatorModel):
    pass


class PromptTemplateConfiguration(BaseValidatorModel):
    chat: Optional[ChatPromptTemplateConfigurationUnion] = None
    text: Optional[TextPromptTemplateConfigurationUnion] = None


class FlowConnection(BaseValidatorModel):
    pass


class FlowNodeExtra(BaseValidatorModel):
    pass


class FlowDefinitionOutput(BaseValidatorModel):
    connections: Optional[List[FlowConnection]] = None
    nodes: Optional[List[FlowNodeExtra]] = None


class PromptFlowNodeInlineConfiguration(BaseValidatorModel):
    modelId: str
    templateConfiguration: PromptTemplateConfiguration
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    inferenceConfiguration: Optional[PromptInferenceConfiguration] = None


class PromptFlowNodeSourceConfiguration(BaseValidatorModel):
    inline: Optional[PromptFlowNodeInlineConfiguration] = None
    resource: Optional[PromptFlowNodeResourceConfiguration] = None


class PromptInferenceConfigurationUnion(BaseValidatorModel):
    pass


class PromptTemplateConfigurationUnion(BaseValidatorModel):
    pass


class PromptVariant(BaseValidatorModel):
    name: str
    templateConfiguration: PromptTemplateConfigurationUnion
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    genAiResource: Optional[PromptGenAiResource] = None
    inferenceConfiguration: Optional[PromptInferenceConfigurationUnion] = None
    metadata: Optional[Sequence[PromptMetadataEntry]] = None
    modelId: Optional[str] = None


class PromptFlowNodeConfiguration(BaseValidatorModel):
    sourceConfiguration: PromptFlowNodeSourceConfiguration
    guardrailConfiguration: Optional[GuardrailConfiguration] = None


class PromptVariantUnion(BaseValidatorModel):
    pass


class CreatePromptRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    variants: Optional[Sequence[PromptVariantUnion]] = None


class UpdatePromptRequest(BaseValidatorModel):
    name: str
    promptIdentifier: str
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    variants: Optional[Sequence[PromptVariantUnion]] = None


class FlowNode(BaseValidatorModel):
    pass


class FlowDefinition(BaseValidatorModel):
    connections: Optional[Sequence[FlowConnection]] = None
    nodes: Optional[Sequence[FlowNode]] = None


class FlowDefinitionUnion(BaseValidatorModel):
    pass


class CreateFlowRequest(BaseValidatorModel):
    executionRoleArn: str
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionUnion] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateFlowRequest(BaseValidatorModel):
    executionRoleArn: str
    flowIdentifier: str
    name: str
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionUnion] = None
    description: Optional[str] = None


class ValidateFlowDefinitionRequest(BaseValidatorModel):
    definition: FlowDefinitionUnion



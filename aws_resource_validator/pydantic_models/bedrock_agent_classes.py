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

class S3IdentifierTypeDef(BaseValidatorModel):
    s3BucketName: Optional[str] = None
    s3ObjectKey: Optional[str] = None


class ActionGroupSummaryTypeDef(BaseValidatorModel):
    actionGroupId: str
    actionGroupName: str
    actionGroupState: ActionGroupStateType
    updatedAt: datetime
    description: Optional[str] = None


class AgentAliasRoutingConfigurationListItemTypeDef(BaseValidatorModel):
    agentVersion: Optional[str] = None
    provisionedThroughput: Optional[str] = None


class AgentDescriptorTypeDef(BaseValidatorModel):
    aliasArn: Optional[str] = None


class AgentFlowNodeConfigurationTypeDef(BaseValidatorModel):
    agentAliasArn: str


class AgentKnowledgeBaseSummaryTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    knowledgeBaseState: KnowledgeBaseStateType
    updatedAt: datetime
    description: Optional[str] = None


class AgentKnowledgeBaseTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    createdAt: datetime
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: KnowledgeBaseStateType
    updatedAt: datetime


class GuardrailConfigurationTypeDef(BaseValidatorModel):
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateAgentKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: Optional[KnowledgeBaseStateType] = None


class BedrockDataAutomationConfigurationTypeDef(BaseValidatorModel):
    parsingModality: Optional[Literal["MULTIMODAL"]] = None


class BedrockEmbeddingModelConfigurationTypeDef(BaseValidatorModel):
    dimensions: Optional[int] = None
    embeddingDataType: Optional[EmbeddingDataTypeType] = None


class ParsingPromptTypeDef(BaseValidatorModel):
    parsingPromptText: str


class EnrichmentStrategyConfigurationTypeDef(BaseValidatorModel):
    method: Literal["CHUNK_ENTITY_EXTRACTION"]


class PromptInputVariableTypeDef(BaseValidatorModel):
    name: Optional[str] = None


class FixedSizeChunkingConfigurationTypeDef(BaseValidatorModel):
    maxTokens: int
    overlapPercentage: int


class SemanticChunkingConfigurationTypeDef(BaseValidatorModel):
    breakpointPercentileThreshold: int
    bufferSize: int
    maxTokens: int


class FlowConditionTypeDef(BaseValidatorModel):
    name: str
    expression: Optional[str] = None


class ConfluenceSourceConfigurationTypeDef(BaseValidatorModel):
    authType: ConfluenceAuthTypeType
    credentialsSecretArn: str
    hostType: Literal["SAAS"]
    hostUrl: str


class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyArn: Optional[str] = None


class FlowAliasRoutingConfigurationListItemTypeDef(BaseValidatorModel):
    flowVersion: Optional[str] = None


class CreateFlowVersionRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class CreatePromptVersionRequestTypeDef(BaseValidatorModel):
    promptIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CuratedQueryTypeDef(BaseValidatorModel):
    naturalLanguage: str
    sql: str


class CustomS3LocationTypeDef(BaseValidatorModel):
    uri: str
    bucketOwnerAccountId: Optional[str] = None


class CyclicConnectionFlowValidationDetailsTypeDef(BaseValidatorModel):
    connection: str


class S3DataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    bucketArn: str
    bucketOwnerAccountId: Optional[str] = None
    inclusionPrefixes: Optional[List[str]] = None


class S3DataSourceConfigurationTypeDef(BaseValidatorModel):
    bucketArn: str
    bucketOwnerAccountId: Optional[str] = None
    inclusionPrefixes: Optional[Sequence[str]] = None


class DataSourceSummaryTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    status: DataSourceStatusType
    updatedAt: datetime
    description: Optional[str] = None


class DeleteAgentActionGroupRequestTypeDef(BaseValidatorModel):
    actionGroupId: str
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: Optional[bool] = None


class DeleteAgentAliasRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str


class DeleteAgentRequestTypeDef(BaseValidatorModel):
    agentId: str
    skipResourceInUseCheck: Optional[bool] = None


class DeleteAgentVersionRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: Optional[bool] = None


class DeleteDataSourceRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str


class DeleteFlowAliasRequestTypeDef(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str


class DeleteFlowRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    skipResourceInUseCheck: Optional[bool] = None


class DeleteFlowVersionRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    flowVersion: str
    skipResourceInUseCheck: Optional[bool] = None


class DeleteKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str


class DeletePromptRequestTypeDef(BaseValidatorModel):
    promptIdentifier: str
    promptVersion: Optional[str] = None


class DisassociateAgentCollaboratorRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    collaboratorId: str


class DisassociateAgentKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str


class S3LocationTypeDef(BaseValidatorModel):
    uri: str


class DuplicateConditionExpressionFlowValidationDetailsTypeDef(BaseValidatorModel):
    expression: str
    node: str


class DuplicateConnectionsFlowValidationDetailsTypeDef(BaseValidatorModel):
    source: str
    target: str


class FlowConditionalConnectionConfigurationTypeDef(BaseValidatorModel):
    condition: str


class FlowDataConnectionConfigurationTypeDef(BaseValidatorModel):
    sourceOutput: str
    targetInput: str


class LambdaFunctionFlowNodeConfigurationTypeDef(BaseValidatorModel):
    lambdaArn: str


class LexFlowNodeConfigurationTypeDef(BaseValidatorModel):
    botAliasArn: str
    localeId: str


class IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef(BaseValidatorModel):
    connection: str


class MalformedConditionExpressionFlowValidationDetailsTypeDef(BaseValidatorModel):
    cause: str
    condition: str
    node: str


class MismatchedNodeOutputTypeFlowValidationDetailsTypeDef(BaseValidatorModel):
    expectedType: FlowNodeIODataTypeType
    node: str
    output: str


class MissingConnectionConfigurationFlowValidationDetailsTypeDef(BaseValidatorModel):
    connection: str


class MissingDefaultConditionFlowValidationDetailsTypeDef(BaseValidatorModel):
    node: str


class MissingNodeConfigurationFlowValidationDetailsTypeDef(BaseValidatorModel):
    node: str


class MissingNodeOutputFlowValidationDetailsTypeDef(BaseValidatorModel):
    node: str
    output: str


class UnknownConnectionConditionFlowValidationDetailsTypeDef(BaseValidatorModel):
    connection: str


class UnknownConnectionSourceFlowValidationDetailsTypeDef(BaseValidatorModel):
    connection: str


class UnknownConnectionSourceOutputFlowValidationDetailsTypeDef(BaseValidatorModel):
    connection: str


class UnknownConnectionTargetFlowValidationDetailsTypeDef(BaseValidatorModel):
    connection: str


class UnknownConnectionTargetInputFlowValidationDetailsTypeDef(BaseValidatorModel):
    connection: str


class UnknownNodeOutputFlowValidationDetailsTypeDef(BaseValidatorModel):
    node: str
    output: str


class UnreachableNodeFlowValidationDetailsTypeDef(BaseValidatorModel):
    node: str


class UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef(BaseValidatorModel):
    connection: str


class GetAgentActionGroupRequestTypeDef(BaseValidatorModel):
    actionGroupId: str
    agentId: str
    agentVersion: str


class GetAgentAliasRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str


class GetAgentCollaboratorRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    collaboratorId: str


class GetAgentKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str


class GetAgentRequestTypeDef(BaseValidatorModel):
    agentId: str


class GetAgentVersionRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str


class GetDataSourceRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str


class GetFlowAliasRequestTypeDef(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str


class GetFlowRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str


class GetFlowVersionRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    flowVersion: str


class GetIngestionJobRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str


class GetKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str


class GetPromptRequestTypeDef(BaseValidatorModel):
    promptIdentifier: str
    promptVersion: Optional[str] = None


class HierarchicalChunkingLevelConfigurationTypeDef(BaseValidatorModel):
    maxTokens: int


class InferenceConfigurationOutputTypeDef(BaseValidatorModel):
    maximumLength: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None


class InferenceConfigurationTypeDef(BaseValidatorModel):
    maximumLength: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None


class IngestionJobSortByTypeDef(BaseValidatorModel):
    attribute: IngestionJobSortByAttributeType
    order: SortOrderType


class IngestionJobStatisticsTypeDef(BaseValidatorModel):
    numberOfDocumentsDeleted: Optional[int] = None
    numberOfDocumentsFailed: Optional[int] = None
    numberOfDocumentsScanned: Optional[int] = None
    numberOfMetadataDocumentsModified: Optional[int] = None
    numberOfMetadataDocumentsScanned: Optional[int] = None
    numberOfModifiedDocumentsIndexed: Optional[int] = None
    numberOfNewDocumentsIndexed: Optional[int] = None


class TextContentDocTypeDef(BaseValidatorModel):
    data: str


class KendraKnowledgeBaseConfigurationTypeDef(BaseValidatorModel):
    kendraIndexArn: str


class KnowledgeBaseSummaryTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    name: str
    status: KnowledgeBaseStatusType
    updatedAt: datetime
    description: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAgentActionGroupsRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentAliasesRequestTypeDef(BaseValidatorModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentCollaboratorsRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentKnowledgeBasesRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentVersionsRequestTypeDef(BaseValidatorModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAgentsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDataSourcesRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFlowAliasesRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFlowVersionsRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFlowsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKnowledgeBaseDocumentsRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKnowledgeBasesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPromptsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    promptIdentifier: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class SessionSummaryConfigurationTypeDef(BaseValidatorModel):
    maxRecentSessions: Optional[int] = None


class MongoDbAtlasFieldMappingTypeDef(BaseValidatorModel):
    metadataField: str
    textField: str
    vectorField: str


class NeptuneAnalyticsFieldMappingTypeDef(BaseValidatorModel):
    metadataField: str
    textField: str


class OpenSearchServerlessFieldMappingTypeDef(BaseValidatorModel):
    metadataField: str
    textField: str
    vectorField: str


class PatternObjectFilterOutputTypeDef(BaseValidatorModel):
    objectType: str
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None


class PatternObjectFilterTypeDef(BaseValidatorModel):
    objectType: str
    exclusionFilters: Optional[Sequence[str]] = None
    inclusionFilters: Optional[Sequence[str]] = None


class PineconeFieldMappingTypeDef(BaseValidatorModel):
    metadataField: str
    textField: str


class PrepareAgentRequestTypeDef(BaseValidatorModel):
    agentId: str


class PrepareFlowRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str


class PromptAgentResourceTypeDef(BaseValidatorModel):
    agentIdentifier: str


class PromptFlowNodeResourceConfigurationTypeDef(BaseValidatorModel):
    promptArn: str


class PromptModelInferenceConfigurationOutputTypeDef(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None


class PromptMetadataEntryTypeDef(BaseValidatorModel):
    key: str
    value: str


class PromptModelInferenceConfigurationTypeDef(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None


class QueryGenerationColumnTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    inclusion: Optional[IncludeExcludeType] = None
    name: Optional[str] = None


class RdsFieldMappingTypeDef(BaseValidatorModel):
    metadataField: str
    primaryKeyField: str
    textField: str
    vectorField: str


class RedisEnterpriseCloudFieldMappingTypeDef(BaseValidatorModel):
    metadataField: str
    textField: str
    vectorField: str


class RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutputTypeDef(BaseValidatorModel):
    tableNames: List[str]


class RedshiftQueryEngineAwsDataCatalogStorageConfigurationTypeDef(BaseValidatorModel):
    tableNames: Sequence[str]


class RedshiftQueryEngineRedshiftStorageConfigurationTypeDef(BaseValidatorModel):
    databaseName: str


class RetrievalFlowNodeS3ConfigurationTypeDef(BaseValidatorModel):
    bucketName: str


class SalesforceSourceConfigurationTypeDef(BaseValidatorModel):
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str
    hostUrl: str


class SeedUrlTypeDef(BaseValidatorModel):
    url: Optional[str] = None


class SharePointSourceConfigurationOutputTypeDef(BaseValidatorModel):
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: List[str]
    tenantId: Optional[str] = None


class SharePointSourceConfigurationTypeDef(BaseValidatorModel):
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: Sequence[str]
    tenantId: Optional[str] = None


class SpecificToolChoiceTypeDef(BaseValidatorModel):
    name: str


class StartIngestionJobRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class StopIngestionJobRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str


class StorageFlowNodeS3ConfigurationTypeDef(BaseValidatorModel):
    bucketName: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class ToolInputSchemaOutputTypeDef(BaseValidatorModel):
    json: Optional[Dict[str, Any]] = None


class ToolInputSchemaTypeDef(BaseValidatorModel):
    json: Optional[Mapping[str, Any]] = None


class TransformationLambdaConfigurationTypeDef(BaseValidatorModel):
    lambdaArn: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAgentKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str
    description: Optional[str] = None
    knowledgeBaseState: Optional[KnowledgeBaseStateType] = None


class WebCrawlerLimitsTypeDef(BaseValidatorModel):
    maxPages: Optional[int] = None
    rateLimit: Optional[int] = None


class APISchemaTypeDef(BaseValidatorModel):
    payload: Optional[str] = None
    s3: Optional[S3IdentifierTypeDef] = None


class AgentAliasHistoryEventTypeDef(BaseValidatorModel):
    endDate: Optional[datetime] = None
    routingConfiguration: Optional[List[AgentAliasRoutingConfigurationListItemTypeDef]] = None
    startDate: Optional[datetime] = None


class AgentAliasSummaryTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentAliasName: str
    agentAliasStatus: AgentAliasStatusType
    createdAt: datetime
    updatedAt: datetime
    description: Optional[str] = None
    routingConfiguration: Optional[List[AgentAliasRoutingConfigurationListItemTypeDef]] = None


class CreateAgentAliasRequestTypeDef(BaseValidatorModel):
    agentAliasName: str
    agentId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    routingConfiguration: Optional[Sequence[AgentAliasRoutingConfigurationListItemTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateAgentAliasRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentAliasName: str
    agentId: str
    description: Optional[str] = None
    routingConfiguration: Optional[Sequence[AgentAliasRoutingConfigurationListItemTypeDef]] = None


class AgentCollaboratorSummaryTypeDef(BaseValidatorModel):
    agentDescriptor: AgentDescriptorTypeDef
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorId: str
    collaboratorName: str
    createdAt: datetime
    lastUpdatedAt: datetime
    relayConversationHistory: RelayConversationHistoryType


class AgentCollaboratorTypeDef(BaseValidatorModel):
    agentDescriptor: AgentDescriptorTypeDef
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorId: str
    collaboratorName: str
    createdAt: datetime
    lastUpdatedAt: datetime
    clientToken: Optional[str] = None
    relayConversationHistory: Optional[RelayConversationHistoryType] = None


class AssociateAgentCollaboratorRequestTypeDef(BaseValidatorModel):
    agentDescriptor: AgentDescriptorTypeDef
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorName: str
    clientToken: Optional[str] = None
    relayConversationHistory: Optional[RelayConversationHistoryType] = None


class UpdateAgentCollaboratorRequestTypeDef(BaseValidatorModel):
    agentDescriptor: AgentDescriptorTypeDef
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorId: str
    collaboratorName: str
    relayConversationHistory: Optional[RelayConversationHistoryType] = None


class AgentSummaryTypeDef(BaseValidatorModel):
    agentId: str
    agentName: str
    agentStatus: AgentStatusType
    updatedAt: datetime
    description: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    latestAgentVersion: Optional[str] = None


class AgentVersionSummaryTypeDef(BaseValidatorModel):
    agentName: str
    agentStatus: AgentStatusType
    agentVersion: str
    createdAt: datetime
    updatedAt: datetime
    description: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None


class KnowledgeBaseFlowNodeConfigurationTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    modelId: Optional[str] = None


class AssociateAgentKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAgentAliasResponseTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentAliasStatus: AgentAliasStatusType
    agentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAgentResponseTypeDef(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAgentVersionResponseTypeDef(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataSourceResponseTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    status: DataSourceStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    status: KnowledgeBaseStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetAgentKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAgentActionGroupsResponseTypeDef(BaseValidatorModel):
    actionGroupSummaries: List[ActionGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAgentKnowledgeBasesResponseTypeDef(BaseValidatorModel):
    agentKnowledgeBaseSummaries: List[AgentKnowledgeBaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PrepareAgentResponseTypeDef(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    preparedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAgentKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmbeddingModelConfigurationTypeDef(BaseValidatorModel):
    bedrockEmbeddingModelConfiguration: Optional[BedrockEmbeddingModelConfigurationTypeDef] = None


class BedrockFoundationModelConfigurationTypeDef(BaseValidatorModel):
    modelArn: str
    parsingModality: Optional[Literal["MULTIMODAL"]] = None
    parsingPrompt: Optional[ParsingPromptTypeDef] = None


class BedrockFoundationModelContextEnrichmentConfigurationTypeDef(BaseValidatorModel):
    enrichmentStrategyConfiguration: EnrichmentStrategyConfigurationTypeDef
    modelArn: str


class BlobTypeDef(BaseValidatorModel):
    pass


class ByteContentDocTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    mimeType: str


class CachePointBlockTypeDef(BaseValidatorModel):
    pass


class ContentBlockTypeDef(BaseValidatorModel):
    cachePoint: Optional[CachePointBlockTypeDef] = None
    text: Optional[str] = None


class SystemContentBlockTypeDef(BaseValidatorModel):
    cachePoint: Optional[CachePointBlockTypeDef] = None
    text: Optional[str] = None


class TextPromptTemplateConfigurationOutputTypeDef(BaseValidatorModel):
    text: str
    cachePoint: Optional[CachePointBlockTypeDef] = None
    inputVariables: Optional[List[PromptInputVariableTypeDef]] = None


class TextPromptTemplateConfigurationTypeDef(BaseValidatorModel):
    text: str
    cachePoint: Optional[CachePointBlockTypeDef] = None
    inputVariables: Optional[Sequence[PromptInputVariableTypeDef]] = None


class ConditionFlowNodeConfigurationOutputTypeDef(BaseValidatorModel):
    conditions: List[FlowConditionTypeDef]


class ConditionFlowNodeConfigurationTypeDef(BaseValidatorModel):
    conditions: Sequence[FlowConditionTypeDef]


class CreateFlowAliasRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateFlowAliasRequestTypeDef(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    description: Optional[str] = None


class OrchestrationExecutorTypeDef(BaseValidatorModel):
    pass


class CustomOrchestrationTypeDef(BaseValidatorModel):
    executor: Optional[OrchestrationExecutorTypeDef] = None


class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    dataSourceSummaries: List[DataSourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CustomDocumentIdentifierTypeDef(BaseValidatorModel):
    pass


class DocumentIdentifierTypeDef(BaseValidatorModel):
    dataSourceType: ContentDataSourceTypeType
    custom: Optional[CustomDocumentIdentifierTypeDef] = None
    s3: Optional[S3LocationTypeDef] = None


class IntermediateStorageTypeDef(BaseValidatorModel):
    s3Location: S3LocationTypeDef


class S3ContentTypeDef(BaseValidatorModel):
    s3Location: S3LocationTypeDef


class FlowConnectionConfigurationTypeDef(BaseValidatorModel):
    conditional: Optional[FlowConditionalConnectionConfigurationTypeDef] = None
    data: Optional[FlowDataConnectionConfigurationTypeDef] = None


class FlowSummaryTypeDef(BaseValidatorModel):
    pass


class ListFlowsResponseTypeDef(BaseValidatorModel):
    flowSummaries: List[FlowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MismatchedNodeInputTypeFlowValidationDetailsTypeDef(BaseValidatorModel):
    pass


class UnknownNodeInputFlowValidationDetailsTypeDef(BaseValidatorModel):
    pass


class UnfulfilledNodeInputFlowValidationDetailsTypeDef(BaseValidatorModel):
    pass


class MultipleNodeInputConnectionsFlowValidationDetailsTypeDef(BaseValidatorModel):
    pass


class MissingNodeInputFlowValidationDetailsTypeDef(BaseValidatorModel):
    pass


class MalformedNodeInputExpressionFlowValidationDetailsTypeDef(BaseValidatorModel):
    pass


class FlowValidationDetailsTypeDef(BaseValidatorModel):
    cyclicConnection: Optional[CyclicConnectionFlowValidationDetailsTypeDef] = None
    duplicateConditionExpression: Optional[ DuplicateConditionExpressionFlowValidationDetailsTypeDef ] = None
    duplicateConnections: Optional[DuplicateConnectionsFlowValidationDetailsTypeDef] = None
    incompatibleConnectionDataType: Optional[ IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef ] = None
    malformedConditionExpression: Optional[ MalformedConditionExpressionFlowValidationDetailsTypeDef ] = None
    malformedNodeInputExpression: Optional[ MalformedNodeInputExpressionFlowValidationDetailsTypeDef ] = None
    mismatchedNodeInputType: Optional[MismatchedNodeInputTypeFlowValidationDetailsTypeDef] = None
    mismatchedNodeOutputType: Optional[MismatchedNodeOutputTypeFlowValidationDetailsTypeDef] = None
    missingConnectionConfiguration: Optional[ MissingConnectionConfigurationFlowValidationDetailsTypeDef ] = None
    missingDefaultCondition: Optional[MissingDefaultConditionFlowValidationDetailsTypeDef] = None
    missingEndingNodes: Optional[Dict[str, Any]] = None
    missingNodeConfiguration: Optional[MissingNodeConfigurationFlowValidationDetailsTypeDef] = None
    missingNodeInput: Optional[MissingNodeInputFlowValidationDetailsTypeDef] = None
    missingNodeOutput: Optional[MissingNodeOutputFlowValidationDetailsTypeDef] = None
    missingStartingNodes: Optional[Dict[str, Any]] = None
    multipleNodeInputConnections: Optional[ MultipleNodeInputConnectionsFlowValidationDetailsTypeDef ] = None
    unfulfilledNodeInput: Optional[UnfulfilledNodeInputFlowValidationDetailsTypeDef] = None
    unknownConnectionCondition: Optional[UnknownConnectionConditionFlowValidationDetailsTypeDef] = None
    unknownConnectionSource: Optional[UnknownConnectionSourceFlowValidationDetailsTypeDef] = None
    unknownConnectionSourceOutput: Optional[ UnknownConnectionSourceOutputFlowValidationDetailsTypeDef ] = None
    unknownConnectionTarget: Optional[UnknownConnectionTargetFlowValidationDetailsTypeDef] = None
    unknownConnectionTargetInput: Optional[ UnknownConnectionTargetInputFlowValidationDetailsTypeDef ] = None
    unknownNodeInput: Optional[UnknownNodeInputFlowValidationDetailsTypeDef] = None
    unknownNodeOutput: Optional[UnknownNodeOutputFlowValidationDetailsTypeDef] = None
    unreachableNode: Optional[UnreachableNodeFlowValidationDetailsTypeDef] = None
    unsatisfiedConnectionConditions: Optional[ UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef ] = None
    unspecified: Optional[Dict[str, Any]] = None


class FlowVersionSummaryTypeDef(BaseValidatorModel):
    pass


class ListFlowVersionsResponseTypeDef(BaseValidatorModel):
    flowVersionSummaries: List[FlowVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ParameterDetailTypeDef(BaseValidatorModel):
    pass


class FunctionOutputTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, ParameterDetailTypeDef]] = None
    requireConfirmation: Optional[RequireConfirmationType] = None


class FunctionTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Mapping[str, ParameterDetailTypeDef]] = None
    requireConfirmation: Optional[RequireConfirmationType] = None


class HierarchicalChunkingConfigurationOutputTypeDef(BaseValidatorModel):
    levelConfigurations: List[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int


class HierarchicalChunkingConfigurationTypeDef(BaseValidatorModel):
    levelConfigurations: Sequence[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int


class PromptConfigurationOutputTypeDef(BaseValidatorModel):
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    basePromptTemplate: Optional[str] = None
    foundationModel: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationOutputTypeDef] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None


class PromptConfigurationTypeDef(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    basePromptTemplate: Optional[str] = None
    foundationModel: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationTypeDef] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None


class IngestionJobFilterTypeDef(BaseValidatorModel):
    pass


class ListIngestionJobsRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    filters: Optional[Sequence[IngestionJobFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[IngestionJobSortByTypeDef] = None


class IngestionJobSummaryTypeDef(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str
    startedAt: datetime
    status: IngestionJobStatusType
    updatedAt: datetime
    description: Optional[str] = None
    statistics: Optional[IngestionJobStatisticsTypeDef] = None


class IngestionJobTypeDef(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str
    startedAt: datetime
    status: IngestionJobStatusType
    updatedAt: datetime
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    statistics: Optional[IngestionJobStatisticsTypeDef] = None


class ListKnowledgeBasesResponseTypeDef(BaseValidatorModel):
    knowledgeBaseSummaries: List[KnowledgeBaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAgentActionGroupsRequestPaginateTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAgentAliasesRequestPaginateTypeDef(BaseValidatorModel):
    agentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAgentCollaboratorsRequestPaginateTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAgentKnowledgeBasesRequestPaginateTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAgentVersionsRequestPaginateTypeDef(BaseValidatorModel):
    agentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAgentsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataSourcesRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFlowAliasesRequestPaginateTypeDef(BaseValidatorModel):
    flowIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFlowVersionsRequestPaginateTypeDef(BaseValidatorModel):
    flowIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFlowsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIngestionJobsRequestPaginateTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    filters: Optional[Sequence[IngestionJobFilterTypeDef]] = None
    sortBy: Optional[IngestionJobSortByTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListKnowledgeBaseDocumentsRequestPaginateTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListKnowledgeBasesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPromptsRequestPaginateTypeDef(BaseValidatorModel):
    promptIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class PromptSummaryTypeDef(BaseValidatorModel):
    pass


class ListPromptsResponseTypeDef(BaseValidatorModel):
    promptSummaries: List[PromptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MemoryConfigurationOutputTypeDef(BaseValidatorModel):
    enabledMemoryTypes: List[Literal["SESSION_SUMMARY"]]
    sessionSummaryConfiguration: Optional[SessionSummaryConfigurationTypeDef] = None
    storageDays: Optional[int] = None


class MemoryConfigurationTypeDef(BaseValidatorModel):
    enabledMemoryTypes: Sequence[Literal["SESSION_SUMMARY"]]
    sessionSummaryConfiguration: Optional[SessionSummaryConfigurationTypeDef] = None
    storageDays: Optional[int] = None


class MetadataAttributeValueTypeDef(BaseValidatorModel):
    pass


class MetadataAttributeTypeDef(BaseValidatorModel):
    key: str
    value: MetadataAttributeValueTypeDef


class MongoDbAtlasConfigurationTypeDef(BaseValidatorModel):
    collectionName: str
    credentialsSecretArn: str
    databaseName: str
    endpoint: str
    fieldMapping: MongoDbAtlasFieldMappingTypeDef
    vectorIndexName: str
    endpointServiceName: Optional[str] = None


class NeptuneAnalyticsConfigurationTypeDef(BaseValidatorModel):
    fieldMapping: NeptuneAnalyticsFieldMappingTypeDef
    graphArn: str


class OpenSearchServerlessConfigurationTypeDef(BaseValidatorModel):
    collectionArn: str
    fieldMapping: OpenSearchServerlessFieldMappingTypeDef
    vectorIndexName: str


class PatternObjectFilterConfigurationOutputTypeDef(BaseValidatorModel):
    filters: List[PatternObjectFilterOutputTypeDef]


class PatternObjectFilterConfigurationTypeDef(BaseValidatorModel):
    filters: Sequence[PatternObjectFilterTypeDef]


class PineconeConfigurationTypeDef(BaseValidatorModel):
    connectionString: str
    credentialsSecretArn: str
    fieldMapping: PineconeFieldMappingTypeDef
    namespace: Optional[str] = None


class PromptGenAiResourceTypeDef(BaseValidatorModel):
    agent: Optional[PromptAgentResourceTypeDef] = None


class PromptInferenceConfigurationOutputTypeDef(BaseValidatorModel):
    text: Optional[PromptModelInferenceConfigurationOutputTypeDef] = None


class QueryGenerationTableOutputTypeDef(BaseValidatorModel):
    name: str
    columns: Optional[List[QueryGenerationColumnTypeDef]] = None
    description: Optional[str] = None
    inclusion: Optional[IncludeExcludeType] = None


class QueryGenerationTableTypeDef(BaseValidatorModel):
    name: str
    columns: Optional[Sequence[QueryGenerationColumnTypeDef]] = None
    description: Optional[str] = None
    inclusion: Optional[IncludeExcludeType] = None


class RdsConfigurationTypeDef(BaseValidatorModel):
    credentialsSecretArn: str
    databaseName: str
    fieldMapping: RdsFieldMappingTypeDef
    resourceArn: str
    tableName: str


class RedisEnterpriseCloudConfigurationTypeDef(BaseValidatorModel):
    credentialsSecretArn: str
    endpoint: str
    fieldMapping: RedisEnterpriseCloudFieldMappingTypeDef
    vectorIndexName: str


class RedshiftProvisionedAuthConfigurationTypeDef(BaseValidatorModel):
    pass


class RedshiftProvisionedConfigurationTypeDef(BaseValidatorModel):
    authConfiguration: RedshiftProvisionedAuthConfigurationTypeDef
    clusterIdentifier: str


class RedshiftServerlessAuthConfigurationTypeDef(BaseValidatorModel):
    pass


class RedshiftServerlessConfigurationTypeDef(BaseValidatorModel):
    authConfiguration: RedshiftServerlessAuthConfigurationTypeDef
    workgroupArn: str


class RetrievalFlowNodeServiceConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[RetrievalFlowNodeS3ConfigurationTypeDef] = None


class UrlConfigurationOutputTypeDef(BaseValidatorModel):
    seedUrls: Optional[List[SeedUrlTypeDef]] = None


class UrlConfigurationTypeDef(BaseValidatorModel):
    seedUrls: Optional[Sequence[SeedUrlTypeDef]] = None


class StorageFlowNodeServiceConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[StorageFlowNodeS3ConfigurationTypeDef] = None


class ToolSpecificationOutputTypeDef(BaseValidatorModel):
    inputSchema: ToolInputSchemaOutputTypeDef
    name: str
    description: Optional[str] = None


class TransformationFunctionTypeDef(BaseValidatorModel):
    transformationLambdaConfiguration: TransformationLambdaConfigurationTypeDef


class WebCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    crawlerLimits: Optional[WebCrawlerLimitsTypeDef] = None
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None
    scope: Optional[WebScopeTypeType] = None
    userAgent: Optional[str] = None
    userAgentHeader: Optional[str] = None


class WebCrawlerConfigurationTypeDef(BaseValidatorModel):
    crawlerLimits: Optional[WebCrawlerLimitsTypeDef] = None
    exclusionFilters: Optional[Sequence[str]] = None
    inclusionFilters: Optional[Sequence[str]] = None
    scope: Optional[WebScopeTypeType] = None
    userAgent: Optional[str] = None
    userAgentHeader: Optional[str] = None


class AgentAliasTypeDef(BaseValidatorModel):
    agentAliasArn: str
    agentAliasId: str
    agentAliasName: str
    agentAliasStatus: AgentAliasStatusType
    agentId: str
    createdAt: datetime
    routingConfiguration: List[AgentAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    agentAliasHistoryEvents: Optional[List[AgentAliasHistoryEventTypeDef]] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None


class ListAgentAliasesResponseTypeDef(BaseValidatorModel):
    agentAliasSummaries: List[AgentAliasSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAgentCollaboratorsResponseTypeDef(BaseValidatorModel):
    agentCollaboratorSummaries: List[AgentCollaboratorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssociateAgentCollaboratorResponseTypeDef(BaseValidatorModel):
    agentCollaborator: AgentCollaboratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAgentCollaboratorResponseTypeDef(BaseValidatorModel):
    agentCollaborator: AgentCollaboratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAgentCollaboratorResponseTypeDef(BaseValidatorModel):
    agentCollaborator: AgentCollaboratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAgentsResponseTypeDef(BaseValidatorModel):
    agentSummaries: List[AgentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAgentVersionsResponseTypeDef(BaseValidatorModel):
    agentVersionSummaries: List[AgentVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ParsingConfigurationTypeDef(BaseValidatorModel):
    parsingStrategy: ParsingStrategyType
    bedrockDataAutomationConfiguration: Optional[BedrockDataAutomationConfigurationTypeDef] = None
    bedrockFoundationModelConfiguration: Optional[BedrockFoundationModelConfigurationTypeDef] = None


class MessageOutputTypeDef(BaseValidatorModel):
    content: List[ContentBlockTypeDef]
    role: ConversationRoleType


class MessageTypeDef(BaseValidatorModel):
    content: Sequence[ContentBlockTypeDef]
    role: ConversationRoleType


class FlowAliasSummaryTypeDef(BaseValidatorModel):
    pass


class ListFlowAliasesResponseTypeDef(BaseValidatorModel):
    flowAliasSummaries: List[FlowAliasSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DeleteKnowledgeBaseDocumentsRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    documentIdentifiers: Sequence[DocumentIdentifierTypeDef]
    knowledgeBaseId: str
    clientToken: Optional[str] = None


class GetKnowledgeBaseDocumentsRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    documentIdentifiers: Sequence[DocumentIdentifierTypeDef]
    knowledgeBaseId: str


class KnowledgeBaseDocumentDetailTypeDef(BaseValidatorModel):
    dataSourceId: str
    identifier: DocumentIdentifierTypeDef
    knowledgeBaseId: str
    status: DocumentStatusType
    statusReason: Optional[str] = None
    updatedAt: Optional[datetime] = None


class SupplementalDataStorageLocationTypeDef(BaseValidatorModel):
    pass


class SupplementalDataStorageConfigurationOutputTypeDef(BaseValidatorModel):
    storageLocations: List[SupplementalDataStorageLocationTypeDef]


class SupplementalDataStorageConfigurationTypeDef(BaseValidatorModel):
    storageLocations: Sequence[SupplementalDataStorageLocationTypeDef]


class FunctionSchemaOutputTypeDef(BaseValidatorModel):
    functions: Optional[List[FunctionOutputTypeDef]] = None


class FunctionSchemaTypeDef(BaseValidatorModel):
    functions: Optional[Sequence[FunctionTypeDef]] = None


class ChunkingConfigurationOutputTypeDef(BaseValidatorModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfigurationTypeDef] = None
    hierarchicalChunkingConfiguration: Optional[HierarchicalChunkingConfigurationOutputTypeDef] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfigurationTypeDef] = None


class ChunkingConfigurationTypeDef(BaseValidatorModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfigurationTypeDef] = None
    hierarchicalChunkingConfiguration: Optional[HierarchicalChunkingConfigurationTypeDef] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfigurationTypeDef] = None


class PromptOverrideConfigurationOutputTypeDef(BaseValidatorModel):
    promptConfigurations: List[PromptConfigurationOutputTypeDef]
    overrideLambda: Optional[str] = None


class PromptOverrideConfigurationTypeDef(BaseValidatorModel):
    promptConfigurations: Sequence[PromptConfigurationTypeDef]
    overrideLambda: Optional[str] = None


class ListIngestionJobsResponseTypeDef(BaseValidatorModel):
    ingestionJobSummaries: List[IngestionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetIngestionJobResponseTypeDef(BaseValidatorModel):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartIngestionJobResponseTypeDef(BaseValidatorModel):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopIngestionJobResponseTypeDef(BaseValidatorModel):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PromptModelInferenceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PromptInferenceConfigurationTypeDef(BaseValidatorModel):
    text: Optional[PromptModelInferenceConfigurationUnionTypeDef] = None


class QueryGenerationContextOutputTypeDef(BaseValidatorModel):
    curatedQueries: Optional[List[CuratedQueryTypeDef]] = None
    tables: Optional[List[QueryGenerationTableOutputTypeDef]] = None


class QueryGenerationContextTypeDef(BaseValidatorModel):
    curatedQueries: Optional[Sequence[CuratedQueryTypeDef]] = None
    tables: Optional[Sequence[QueryGenerationTableTypeDef]] = None


class RetrievalFlowNodeConfigurationTypeDef(BaseValidatorModel):
    serviceConfiguration: RetrievalFlowNodeServiceConfigurationTypeDef


class WebSourceConfigurationOutputTypeDef(BaseValidatorModel):
    urlConfiguration: UrlConfigurationOutputTypeDef


class WebSourceConfigurationTypeDef(BaseValidatorModel):
    urlConfiguration: UrlConfigurationTypeDef


class StorageFlowNodeConfigurationTypeDef(BaseValidatorModel):
    serviceConfiguration: StorageFlowNodeServiceConfigurationTypeDef


class ToolOutputTypeDef(BaseValidatorModel):
    cachePoint: Optional[CachePointBlockTypeDef] = None
    toolSpec: Optional[ToolSpecificationOutputTypeDef] = None


class ToolInputSchemaUnionTypeDef(BaseValidatorModel):
    pass


class ToolSpecificationTypeDef(BaseValidatorModel):
    inputSchema: ToolInputSchemaUnionTypeDef
    name: str
    description: Optional[str] = None


class TransformationTypeDef(BaseValidatorModel):
    stepToApply: Literal["POST_CHUNKING"]
    transformationFunction: TransformationFunctionTypeDef


class CreateAgentAliasResponseTypeDef(BaseValidatorModel):
    agentAlias: AgentAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAgentAliasResponseTypeDef(BaseValidatorModel):
    agentAlias: AgentAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAgentAliasResponseTypeDef(BaseValidatorModel):
    agentAlias: AgentAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InlineContentTypeDef(BaseValidatorModel):
    pass


class CustomContentTypeDef(BaseValidatorModel):
    customDocumentIdentifier: CustomDocumentIdentifierTypeDef
    sourceType: CustomSourceTypeType
    inlineContent: Optional[InlineContentTypeDef] = None
    s3Location: Optional[CustomS3LocationTypeDef] = None


class DeleteKnowledgeBaseDocumentsResponseTypeDef(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetKnowledgeBaseDocumentsResponseTypeDef(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class IngestKnowledgeBaseDocumentsResponseTypeDef(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListKnowledgeBaseDocumentsResponseTypeDef(BaseValidatorModel):
    documentDetails: List[KnowledgeBaseDocumentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class VectorKnowledgeBaseConfigurationOutputTypeDef(BaseValidatorModel):
    embeddingModelArn: str
    embeddingModelConfiguration: Optional[EmbeddingModelConfigurationTypeDef] = None
    supplementalDataStorageConfiguration: Optional[ SupplementalDataStorageConfigurationOutputTypeDef ] = None


class VectorKnowledgeBaseConfigurationTypeDef(BaseValidatorModel):
    embeddingModelArn: str
    embeddingModelConfiguration: Optional[EmbeddingModelConfigurationTypeDef] = None
    supplementalDataStorageConfiguration: Optional[SupplementalDataStorageConfigurationTypeDef] = None


class FlowValidationTypeDef(BaseValidatorModel):
    pass


class ValidateFlowDefinitionResponseTypeDef(BaseValidatorModel):
    validations: List[FlowValidationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ActionGroupExecutorTypeDef(BaseValidatorModel):
    pass


class AgentActionGroupTypeDef(BaseValidatorModel):
    actionGroupId: str
    actionGroupName: str
    actionGroupState: ActionGroupStateType
    agentId: str
    agentVersion: str
    createdAt: datetime
    updatedAt: datetime
    actionGroupExecutor: Optional[ActionGroupExecutorTypeDef] = None
    apiSchema: Optional[APISchemaTypeDef] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchemaOutputTypeDef] = None
    parentActionGroupSignatureParams: Optional[Dict[str, str]] = None
    parentActionSignature: Optional[ActionGroupSignatureType] = None


class AgentTypeDef(BaseValidatorModel):
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
    customOrchestration: Optional[CustomOrchestrationTypeDef] = None
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    foundationModel: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationOutputTypeDef] = None
    orchestrationType: Optional[OrchestrationTypeType] = None
    preparedAt: Optional[datetime] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationOutputTypeDef] = None
    recommendedActions: Optional[List[str]] = None


class AgentVersionTypeDef(BaseValidatorModel):
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
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationOutputTypeDef] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationOutputTypeDef] = None
    recommendedActions: Optional[List[str]] = None


class CrawlFilterConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class ConfluenceCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutputTypeDef] = None


class SalesforceCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutputTypeDef] = None


class SharePointCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutputTypeDef] = None


class CrawlFilterConfigurationTypeDef(BaseValidatorModel):
    pass


class ConfluenceCrawlerConfigurationTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationTypeDef] = None


class SalesforceCrawlerConfigurationTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationTypeDef] = None


class SharePointCrawlerConfigurationTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationTypeDef] = None


class QueryGenerationConfigurationOutputTypeDef(BaseValidatorModel):
    executionTimeoutSeconds: Optional[int] = None
    generationContext: Optional[QueryGenerationContextOutputTypeDef] = None


class QueryGenerationConfigurationTypeDef(BaseValidatorModel):
    executionTimeoutSeconds: Optional[int] = None
    generationContext: Optional[QueryGenerationContextTypeDef] = None


class WebDataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    sourceConfiguration: WebSourceConfigurationOutputTypeDef
    crawlerConfiguration: Optional[WebCrawlerConfigurationOutputTypeDef] = None


class WebDataSourceConfigurationTypeDef(BaseValidatorModel):
    sourceConfiguration: WebSourceConfigurationTypeDef
    crawlerConfiguration: Optional[WebCrawlerConfigurationTypeDef] = None


class ToolChoiceOutputTypeDef(BaseValidatorModel):
    pass


class ToolConfigurationOutputTypeDef(BaseValidatorModel):
    tools: List[ToolOutputTypeDef]
    toolChoice: Optional[ToolChoiceOutputTypeDef] = None


class CustomTransformationConfigurationOutputTypeDef(BaseValidatorModel):
    intermediateStorage: IntermediateStorageTypeDef
    transformations: List[TransformationTypeDef]


class CustomTransformationConfigurationTypeDef(BaseValidatorModel):
    intermediateStorage: IntermediateStorageTypeDef
    transformations: Sequence[TransformationTypeDef]


class DocumentContentTypeDef(BaseValidatorModel):
    dataSourceType: ContentDataSourceTypeType
    custom: Optional[CustomContentTypeDef] = None
    s3: Optional[S3ContentTypeDef] = None


class CreateAgentActionGroupResponseTypeDef(BaseValidatorModel):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAgentActionGroupResponseTypeDef(BaseValidatorModel):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAgentActionGroupResponseTypeDef(BaseValidatorModel):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FunctionSchemaUnionTypeDef(BaseValidatorModel):
    pass


class CreateAgentActionGroupRequestTypeDef(BaseValidatorModel):
    actionGroupName: str
    agentId: str
    agentVersion: str
    actionGroupExecutor: Optional[ActionGroupExecutorTypeDef] = None
    actionGroupState: Optional[ActionGroupStateType] = None
    apiSchema: Optional[APISchemaTypeDef] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchemaUnionTypeDef] = None
    parentActionGroupSignature: Optional[ActionGroupSignatureType] = None
    parentActionGroupSignatureParams: Optional[Mapping[str, str]] = None


class UpdateAgentActionGroupRequestTypeDef(BaseValidatorModel):
    actionGroupId: str
    actionGroupName: str
    agentId: str
    agentVersion: str
    actionGroupExecutor: Optional[ActionGroupExecutorTypeDef] = None
    actionGroupState: Optional[ActionGroupStateType] = None
    apiSchema: Optional[APISchemaTypeDef] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchemaUnionTypeDef] = None
    parentActionGroupSignature: Optional[ActionGroupSignatureType] = None
    parentActionGroupSignatureParams: Optional[Mapping[str, str]] = None


class CreateAgentResponseTypeDef(BaseValidatorModel):
    agent: AgentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAgentResponseTypeDef(BaseValidatorModel):
    agent: AgentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAgentResponseTypeDef(BaseValidatorModel):
    agent: AgentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAgentVersionResponseTypeDef(BaseValidatorModel):
    agentVersion: AgentVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PromptOverrideConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class MemoryConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateAgentRequestTypeDef(BaseValidatorModel):
    agentName: str
    agentCollaboration: Optional[AgentCollaborationType] = None
    agentResourceRoleArn: Optional[str] = None
    clientToken: Optional[str] = None
    customOrchestration: Optional[CustomOrchestrationTypeDef] = None
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    foundationModel: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    idleSessionTTLInSeconds: Optional[int] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationUnionTypeDef] = None
    orchestrationType: Optional[OrchestrationTypeType] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateAgentRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    foundationModel: str
    agentCollaboration: Optional[AgentCollaborationType] = None
    customOrchestration: Optional[CustomOrchestrationTypeDef] = None
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    idleSessionTTLInSeconds: Optional[int] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationUnionTypeDef] = None
    orchestrationType: Optional[OrchestrationTypeType] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationUnionTypeDef] = None


class ConfluenceDataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    sourceConfiguration: ConfluenceSourceConfigurationTypeDef
    crawlerConfiguration: Optional[ConfluenceCrawlerConfigurationOutputTypeDef] = None


class SalesforceDataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    sourceConfiguration: SalesforceSourceConfigurationTypeDef
    crawlerConfiguration: Optional[SalesforceCrawlerConfigurationOutputTypeDef] = None


class SharePointDataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    sourceConfiguration: SharePointSourceConfigurationOutputTypeDef
    crawlerConfiguration: Optional[SharePointCrawlerConfigurationOutputTypeDef] = None


class ConfluenceDataSourceConfigurationTypeDef(BaseValidatorModel):
    sourceConfiguration: ConfluenceSourceConfigurationTypeDef
    crawlerConfiguration: Optional[ConfluenceCrawlerConfigurationTypeDef] = None


class SalesforceDataSourceConfigurationTypeDef(BaseValidatorModel):
    sourceConfiguration: SalesforceSourceConfigurationTypeDef
    crawlerConfiguration: Optional[SalesforceCrawlerConfigurationTypeDef] = None


class SharePointDataSourceConfigurationTypeDef(BaseValidatorModel):
    sourceConfiguration: SharePointSourceConfigurationTypeDef
    crawlerConfiguration: Optional[SharePointCrawlerConfigurationTypeDef] = None


class RedshiftQueryEngineConfigurationTypeDef(BaseValidatorModel):
    pass


class RedshiftQueryEngineStorageConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class RedshiftConfigurationOutputTypeDef(BaseValidatorModel):
    queryEngineConfiguration: RedshiftQueryEngineConfigurationTypeDef
    storageConfigurations: List[RedshiftQueryEngineStorageConfigurationOutputTypeDef]
    queryGenerationConfiguration: Optional[QueryGenerationConfigurationOutputTypeDef] = None


class RedshiftQueryEngineStorageConfigurationTypeDef(BaseValidatorModel):
    pass


class RedshiftConfigurationTypeDef(BaseValidatorModel):
    queryEngineConfiguration: RedshiftQueryEngineConfigurationTypeDef
    storageConfigurations: Sequence[RedshiftQueryEngineStorageConfigurationTypeDef]
    queryGenerationConfiguration: Optional[QueryGenerationConfigurationTypeDef] = None


class ChatPromptTemplateConfigurationOutputTypeDef(BaseValidatorModel):
    messages: List[MessageOutputTypeDef]
    inputVariables: Optional[List[PromptInputVariableTypeDef]] = None
    system: Optional[List[SystemContentBlockTypeDef]] = None
    toolConfiguration: Optional[ToolConfigurationOutputTypeDef] = None


class ToolSpecificationUnionTypeDef(BaseValidatorModel):
    pass


class ToolTypeDef(BaseValidatorModel):
    cachePoint: Optional[CachePointBlockTypeDef] = None
    toolSpec: Optional[ToolSpecificationUnionTypeDef] = None


class ContextEnrichmentConfigurationTypeDef(BaseValidatorModel):
    pass


class VectorIngestionConfigurationOutputTypeDef(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfigurationOutputTypeDef] = None
    contextEnrichmentConfiguration: Optional[ContextEnrichmentConfigurationTypeDef] = None
    customTransformationConfiguration: Optional[CustomTransformationConfigurationOutputTypeDef] = None
    parsingConfiguration: Optional[ParsingConfigurationTypeDef] = None


class VectorIngestionConfigurationTypeDef(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfigurationTypeDef] = None
    contextEnrichmentConfiguration: Optional[ContextEnrichmentConfigurationTypeDef] = None
    customTransformationConfiguration: Optional[CustomTransformationConfigurationTypeDef] = None
    parsingConfiguration: Optional[ParsingConfigurationTypeDef] = None


class DocumentMetadataTypeDef(BaseValidatorModel):
    pass


class KnowledgeBaseDocumentTypeDef(BaseValidatorModel):
    content: DocumentContentTypeDef
    metadata: Optional[DocumentMetadataTypeDef] = None


class PromptTemplateConfigurationOutputTypeDef(BaseValidatorModel):
    chat: Optional[ChatPromptTemplateConfigurationOutputTypeDef] = None
    text: Optional[TextPromptTemplateConfigurationOutputTypeDef] = None


class IngestKnowledgeBaseDocumentsRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    documents: Sequence[KnowledgeBaseDocumentTypeDef]
    knowledgeBaseId: str
    clientToken: Optional[str] = None


class DataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class DataSourceTypeDef(BaseValidatorModel):
    createdAt: datetime
    dataSourceConfiguration: DataSourceConfigurationOutputTypeDef
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    status: DataSourceStatusType
    updatedAt: datetime
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationOutputTypeDef] = None


class PromptFlowNodeInlineConfigurationOutputTypeDef(BaseValidatorModel):
    modelId: str
    templateConfiguration: PromptTemplateConfigurationOutputTypeDef
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    inferenceConfiguration: Optional[PromptInferenceConfigurationOutputTypeDef] = None


class PromptVariantOutputTypeDef(BaseValidatorModel):
    name: str
    templateConfiguration: PromptTemplateConfigurationOutputTypeDef
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    genAiResource: Optional[PromptGenAiResourceTypeDef] = None
    inferenceConfiguration: Optional[PromptInferenceConfigurationOutputTypeDef] = None
    metadata: Optional[List[PromptMetadataEntryTypeDef]] = None
    modelId: Optional[str] = None


class ToolUnionTypeDef(BaseValidatorModel):
    pass


class ToolChoiceUnionTypeDef(BaseValidatorModel):
    pass


class ToolConfigurationTypeDef(BaseValidatorModel):
    tools: Sequence[ToolUnionTypeDef]
    toolChoice: Optional[ToolChoiceUnionTypeDef] = None


class CreateDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DataSourceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class VectorIngestionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataSourceRequestTypeDef(BaseValidatorModel):
    dataSourceConfiguration: DataSourceConfigurationUnionTypeDef
    knowledgeBaseId: str
    name: str
    clientToken: Optional[str] = None
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationUnionTypeDef] = None


class UpdateDataSourceRequestTypeDef(BaseValidatorModel):
    dataSourceConfiguration: DataSourceConfigurationUnionTypeDef
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationUnionTypeDef] = None


class KnowledgeBaseConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class StorageConfigurationTypeDef(BaseValidatorModel):
    pass


class KnowledgeBaseTypeDef(BaseValidatorModel):
    createdAt: datetime
    knowledgeBaseArn: str
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationOutputTypeDef
    knowledgeBaseId: str
    name: str
    roleArn: str
    status: KnowledgeBaseStatusType
    updatedAt: datetime
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    storageConfiguration: Optional[StorageConfigurationTypeDef] = None


class PromptFlowNodeSourceConfigurationOutputTypeDef(BaseValidatorModel):
    inline: Optional[PromptFlowNodeInlineConfigurationOutputTypeDef] = None
    resource: Optional[PromptFlowNodeResourceConfigurationTypeDef] = None


class CreateKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class KnowledgeBaseConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationUnionTypeDef
    name: str
    roleArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    storageConfiguration: Optional[StorageConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationUnionTypeDef
    knowledgeBaseId: str
    name: str
    roleArn: str
    description: Optional[str] = None
    storageConfiguration: Optional[StorageConfigurationTypeDef] = None


class PromptFlowNodeConfigurationOutputTypeDef(BaseValidatorModel):
    sourceConfiguration: PromptFlowNodeSourceConfigurationOutputTypeDef
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None


class ToolConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class MessageUnionTypeDef(BaseValidatorModel):
    pass


class ChatPromptTemplateConfigurationTypeDef(BaseValidatorModel):
    messages: Sequence[MessageUnionTypeDef]
    inputVariables: Optional[Sequence[PromptInputVariableTypeDef]] = None
    system: Optional[Sequence[SystemContentBlockTypeDef]] = None
    toolConfiguration: Optional[ToolConfigurationUnionTypeDef] = None


class TextPromptTemplateConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ChatPromptTemplateConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PromptTemplateConfigurationTypeDef(BaseValidatorModel):
    chat: Optional[ChatPromptTemplateConfigurationUnionTypeDef] = None
    text: Optional[TextPromptTemplateConfigurationUnionTypeDef] = None


class FlowConnectionTypeDef(BaseValidatorModel):
    pass


class FlowNodeExtraTypeDef(BaseValidatorModel):
    pass


class FlowDefinitionOutputTypeDef(BaseValidatorModel):
    connections: Optional[List[FlowConnectionTypeDef]] = None
    nodes: Optional[List[FlowNodeExtraTypeDef]] = None


class PromptFlowNodeInlineConfigurationTypeDef(BaseValidatorModel):
    modelId: str
    templateConfiguration: PromptTemplateConfigurationTypeDef
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    inferenceConfiguration: Optional[PromptInferenceConfigurationTypeDef] = None


class PromptFlowNodeSourceConfigurationTypeDef(BaseValidatorModel):
    inline: Optional[PromptFlowNodeInlineConfigurationTypeDef] = None
    resource: Optional[PromptFlowNodeResourceConfigurationTypeDef] = None


class PromptInferenceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PromptTemplateConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PromptVariantTypeDef(BaseValidatorModel):
    name: str
    templateConfiguration: PromptTemplateConfigurationUnionTypeDef
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    genAiResource: Optional[PromptGenAiResourceTypeDef] = None
    inferenceConfiguration: Optional[PromptInferenceConfigurationUnionTypeDef] = None
    metadata: Optional[Sequence[PromptMetadataEntryTypeDef]] = None
    modelId: Optional[str] = None


class PromptFlowNodeConfigurationTypeDef(BaseValidatorModel):
    sourceConfiguration: PromptFlowNodeSourceConfigurationTypeDef
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None


class PromptVariantUnionTypeDef(BaseValidatorModel):
    pass


class CreatePromptRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    variants: Optional[Sequence[PromptVariantUnionTypeDef]] = None


class UpdatePromptRequestTypeDef(BaseValidatorModel):
    name: str
    promptIdentifier: str
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    variants: Optional[Sequence[PromptVariantUnionTypeDef]] = None


class FlowNodeTypeDef(BaseValidatorModel):
    pass


class FlowDefinitionTypeDef(BaseValidatorModel):
    connections: Optional[Sequence[FlowConnectionTypeDef]] = None
    nodes: Optional[Sequence[FlowNodeTypeDef]] = None


class FlowDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class CreateFlowRequestTypeDef(BaseValidatorModel):
    executionRoleArn: str
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionUnionTypeDef] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateFlowRequestTypeDef(BaseValidatorModel):
    executionRoleArn: str
    flowIdentifier: str
    name: str
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionUnionTypeDef] = None
    description: Optional[str] = None


class ValidateFlowDefinitionRequestTypeDef(BaseValidatorModel):
    definition: FlowDefinitionUnionTypeDef



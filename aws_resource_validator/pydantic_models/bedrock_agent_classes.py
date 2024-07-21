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
from aws_resource_validator.pydantic_models.bedrock_agent_constants import *

class S3IdentifierTypeDef(BaseModel):
    s3BucketName: Optional[str] = None
    s3ObjectKey: Optional[str] = None

class ActionGroupExecutorTypeDef(BaseModel):
    customControl: Optional[Literal["RETURN_CONTROL"]] = None
    lambda: Optional[str] = None

class ActionGroupSummaryTypeDef(BaseModel):
    actionGroupId: str
    actionGroupName: str
    actionGroupState: ActionGroupStateType
    updatedAt: datetime
    description: Optional[str] = None

class AgentAliasRoutingConfigurationListItemTypeDef(BaseModel):
    agentVersion: Optional[str] = None
    provisionedThroughput: Optional[str] = None

class AgentFlowNodeConfigurationTypeDef(BaseModel):
    agentAliasArn: str

class AgentKnowledgeBaseSummaryTypeDef(BaseModel):
    knowledgeBaseId: str
    knowledgeBaseState: KnowledgeBaseStateType
    updatedAt: datetime
    description: Optional[str] = None

class AgentKnowledgeBaseTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    createdAt: datetime
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: KnowledgeBaseStateType
    updatedAt: datetime

class GuardrailConfigurationTypeDef(BaseModel):
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None

class MemoryConfigurationOutputTypeDef(BaseModel):
    enabledMemoryTypes: List[Literal["SESSION_SUMMARY"]]
    storageDays: Optional[int] = None

class AssociateAgentKnowledgeBaseRequestRequestTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: Optional[KnowledgeBaseStateType] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BedrockEmbeddingModelConfigurationTypeDef(BaseModel):
    dimensions: Optional[int] = None

class ParsingPromptTypeDef(BaseModel):
    parsingPromptText: str

class FixedSizeChunkingConfigurationTypeDef(BaseModel):
    maxTokens: int
    overlapPercentage: int

class SemanticChunkingConfigurationTypeDef(BaseModel):
    breakpointPercentileThreshold: int
    bufferSize: int
    maxTokens: int

class FlowConditionTypeDef(BaseModel):
    name: str
    expression: Optional[str] = None

class ConfluenceSourceConfigurationTypeDef(BaseModel):
    authType: ConfluenceAuthTypeType
    credentialsSecretArn: str
    hostType: Literal["SAAS"]
    hostUrl: str

class MemoryConfigurationTypeDef(BaseModel):
    enabledMemoryTypes: Sequence[Literal["SESSION_SUMMARY"]]
    storageDays: Optional[int] = None

class ServerSideEncryptionConfigurationTypeDef(BaseModel):
    kmsKeyArn: Optional[str] = None

class FlowAliasRoutingConfigurationListItemTypeDef(BaseModel):
    flowVersion: Optional[str] = None

class CreateFlowVersionRequestRequestTypeDef(BaseModel):
    flowIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class CreatePromptVersionRequestRequestTypeDef(BaseModel):
    promptIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class S3DataSourceConfigurationOutputTypeDef(BaseModel):
    bucketArn: str
    bucketOwnerAccountId: Optional[str] = None
    inclusionPrefixes: Optional[List[str]] = None

class S3DataSourceConfigurationTypeDef(BaseModel):
    bucketArn: str
    bucketOwnerAccountId: Optional[str] = None
    inclusionPrefixes: Optional[Sequence[str]] = None

class DataSourceSummaryTypeDef(BaseModel):
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    status: DataSourceStatusType
    updatedAt: datetime
    description: Optional[str] = None

class DeleteAgentActionGroupRequestRequestTypeDef(BaseModel):
    actionGroupId: str
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteAgentAliasRequestRequestTypeDef(BaseModel):
    agentAliasId: str
    agentId: str

class DeleteAgentRequestRequestTypeDef(BaseModel):
    agentId: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteAgentVersionRequestRequestTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteDataSourceRequestRequestTypeDef(BaseModel):
    dataSourceId: str
    knowledgeBaseId: str

class DeleteFlowAliasRequestRequestTypeDef(BaseModel):
    aliasIdentifier: str
    flowIdentifier: str

class DeleteFlowRequestRequestTypeDef(BaseModel):
    flowIdentifier: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteFlowVersionRequestRequestTypeDef(BaseModel):
    flowIdentifier: str
    flowVersion: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteKnowledgeBaseRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str

class DeletePromptRequestRequestTypeDef(BaseModel):
    promptIdentifier: str
    promptVersion: Optional[str] = None

class DisassociateAgentKnowledgeBaseRequestRequestTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str

class FlowConditionalConnectionConfigurationTypeDef(BaseModel):
    condition: str

class FlowDataConnectionConfigurationTypeDef(BaseModel):
    sourceOutput: str
    targetInput: str

class KnowledgeBaseFlowNodeConfigurationTypeDef(BaseModel):
    knowledgeBaseId: str
    modelId: Optional[str] = None

class LambdaFunctionFlowNodeConfigurationTypeDef(BaseModel):
    lambdaArn: str

class LexFlowNodeConfigurationTypeDef(BaseModel):
    botAliasArn: str
    localeId: str

class FlowNodeInputTypeDef(BaseModel):
    expression: str
    name: str
    type: FlowNodeIODataTypeType

class FlowNodeOutputTypeDef(BaseModel):
    name: str
    type: FlowNodeIODataTypeType

class FlowSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    id: str
    name: str
    status: FlowStatusType
    updatedAt: datetime
    version: str
    description: Optional[str] = None

class FlowValidationTypeDef(BaseModel):
    message: str
    severity: FlowValidationSeverityType

class FlowVersionSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    id: str
    status: FlowStatusType
    version: str

class ParameterDetailTypeDef(BaseModel):
    type: TypeType
    description: Optional[str] = None
    required: Optional[bool] = None

class GetAgentActionGroupRequestRequestTypeDef(BaseModel):
    actionGroupId: str
    agentId: str
    agentVersion: str

class GetAgentAliasRequestRequestTypeDef(BaseModel):
    agentAliasId: str
    agentId: str

class GetAgentKnowledgeBaseRequestRequestTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str

class GetAgentRequestRequestTypeDef(BaseModel):
    agentId: str

class GetAgentVersionRequestRequestTypeDef(BaseModel):
    agentId: str
    agentVersion: str

class GetDataSourceRequestRequestTypeDef(BaseModel):
    dataSourceId: str
    knowledgeBaseId: str

class GetFlowAliasRequestRequestTypeDef(BaseModel):
    aliasIdentifier: str
    flowIdentifier: str

class GetFlowRequestRequestTypeDef(BaseModel):
    flowIdentifier: str

class GetFlowVersionRequestRequestTypeDef(BaseModel):
    flowIdentifier: str
    flowVersion: str

class GetIngestionJobRequestRequestTypeDef(BaseModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str

class GetKnowledgeBaseRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str

class GetPromptRequestRequestTypeDef(BaseModel):
    promptIdentifier: str
    promptVersion: Optional[str] = None

class HierarchicalChunkingLevelConfigurationTypeDef(BaseModel):
    maxTokens: int

class InferenceConfigurationOutputTypeDef(BaseModel):
    maximumLength: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None

class InferenceConfigurationTypeDef(BaseModel):
    maximumLength: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None

class IngestionJobFilterTypeDef(BaseModel):
    attribute: Literal["STATUS"]
    operator: Literal["EQ"]
    values: Sequence[str]

class IngestionJobSortByTypeDef(BaseModel):
    attribute: IngestionJobSortByAttributeType
    order: SortOrderType

class IngestionJobStatisticsTypeDef(BaseModel):
    numberOfDocumentsDeleted: Optional[int] = None
    numberOfDocumentsFailed: Optional[int] = None
    numberOfDocumentsScanned: Optional[int] = None
    numberOfMetadataDocumentsModified: Optional[int] = None
    numberOfMetadataDocumentsScanned: Optional[int] = None
    numberOfModifiedDocumentsIndexed: Optional[int] = None
    numberOfNewDocumentsIndexed: Optional[int] = None

class S3LocationTypeDef(BaseModel):
    uri: str

class KnowledgeBaseSummaryTypeDef(BaseModel):
    knowledgeBaseId: str
    name: str
    status: KnowledgeBaseStatusType
    updatedAt: datetime
    description: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAgentActionGroupsRequestRequestTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAgentAliasesRequestRequestTypeDef(BaseModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAgentKnowledgeBasesRequestRequestTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAgentVersionsRequestRequestTypeDef(BaseModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAgentsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDataSourcesRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFlowAliasesRequestRequestTypeDef(BaseModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFlowVersionsRequestRequestTypeDef(BaseModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFlowsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListKnowledgeBasesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPromptsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    promptIdentifier: Optional[str] = None

class PromptSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    id: str
    name: str
    updatedAt: datetime
    version: str
    description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class MongoDbAtlasFieldMappingTypeDef(BaseModel):
    metadataField: str
    textField: str
    vectorField: str

class OpenSearchServerlessFieldMappingTypeDef(BaseModel):
    metadataField: str
    textField: str
    vectorField: str

class PatternObjectFilterOutputTypeDef(BaseModel):
    objectType: str
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None

class PatternObjectFilterTypeDef(BaseModel):
    objectType: str
    exclusionFilters: Optional[Sequence[str]] = None
    inclusionFilters: Optional[Sequence[str]] = None

class PineconeFieldMappingTypeDef(BaseModel):
    metadataField: str
    textField: str

class PrepareAgentRequestRequestTypeDef(BaseModel):
    agentId: str

class PrepareFlowRequestRequestTypeDef(BaseModel):
    flowIdentifier: str

class PromptFlowNodeResourceConfigurationTypeDef(BaseModel):
    promptArn: str

class PromptModelInferenceConfigurationOutputTypeDef(BaseModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None

class PromptModelInferenceConfigurationTypeDef(BaseModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None

class PromptInputVariableTypeDef(BaseModel):
    name: Optional[str] = None

class RdsFieldMappingTypeDef(BaseModel):
    metadataField: str
    primaryKeyField: str
    textField: str
    vectorField: str

class RedisEnterpriseCloudFieldMappingTypeDef(BaseModel):
    metadataField: str
    textField: str
    vectorField: str

class RetrievalFlowNodeS3ConfigurationTypeDef(BaseModel):
    bucketName: str

class SalesforceSourceConfigurationTypeDef(BaseModel):
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str
    hostUrl: str

class SeedUrlTypeDef(BaseModel):
    url: Optional[str] = None

class SharePointSourceConfigurationOutputTypeDef(BaseModel):
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: List[str]
    tenantId: Optional[str] = None

class SharePointSourceConfigurationTypeDef(BaseModel):
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: Sequence[str]
    tenantId: Optional[str] = None

class StartIngestionJobRequestRequestTypeDef(BaseModel):
    dataSourceId: str
    knowledgeBaseId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class StorageFlowNodeS3ConfigurationTypeDef(BaseModel):
    bucketName: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TransformationLambdaConfigurationTypeDef(BaseModel):
    lambdaArn: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAgentKnowledgeBaseRequestRequestTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str
    description: Optional[str] = None
    knowledgeBaseState: Optional[KnowledgeBaseStateType] = None

class WebCrawlerLimitsTypeDef(BaseModel):
    rateLimit: Optional[int] = None

class APISchemaTypeDef(BaseModel):
    payload: Optional[str] = None
    s3: Optional[S3IdentifierTypeDef] = None

class AgentAliasHistoryEventTypeDef(BaseModel):
    endDate: Optional[datetime] = None
    routingConfiguration: Optional[List[AgentAliasRoutingConfigurationListItemTypeDef]] = None
    startDate: Optional[datetime] = None

class AgentAliasSummaryTypeDef(BaseModel):
    agentAliasId: str
    agentAliasName: str
    agentAliasStatus: AgentAliasStatusType
    createdAt: datetime
    updatedAt: datetime
    description: Optional[str] = None
    routingConfiguration: Optional[List[AgentAliasRoutingConfigurationListItemTypeDef]] = None

class CreateAgentAliasRequestRequestTypeDef(BaseModel):
    agentAliasName: str
    agentId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    routingConfiguration: Optional[       Sequence[AgentAliasRoutingConfigurationListItemTypeDef]     ] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateAgentAliasRequestRequestTypeDef(BaseModel):
    agentAliasId: str
    agentAliasName: str
    agentId: str
    description: Optional[str] = None
    routingConfiguration: Optional[       Sequence[AgentAliasRoutingConfigurationListItemTypeDef]     ] = None

class AgentSummaryTypeDef(BaseModel):
    agentId: str
    agentName: str
    agentStatus: AgentStatusType
    updatedAt: datetime
    description: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    latestAgentVersion: Optional[str] = None

class AgentVersionSummaryTypeDef(BaseModel):
    agentName: str
    agentStatus: AgentStatusType
    agentVersion: str
    createdAt: datetime
    updatedAt: datetime
    description: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None

class AssociateAgentKnowledgeBaseResponseTypeDef(BaseModel):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentAliasResponseTypeDef(BaseModel):
    agentAliasId: str
    agentAliasStatus: AgentAliasStatusType
    agentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentResponseTypeDef(BaseModel):
    agentId: str
    agentStatus: AgentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentVersionResponseTypeDef(BaseModel):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceResponseTypeDef(BaseModel):
    dataSourceId: str
    knowledgeBaseId: str
    status: DataSourceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowAliasResponseTypeDef(BaseModel):
    flowId: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowResponseTypeDef(BaseModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowVersionResponseTypeDef(BaseModel):
    id: str
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKnowledgeBaseResponseTypeDef(BaseModel):
    knowledgeBaseId: str
    status: KnowledgeBaseStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePromptResponseTypeDef(BaseModel):
    id: str
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentKnowledgeBaseResponseTypeDef(BaseModel):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentActionGroupsResponseTypeDef(BaseModel):
    actionGroupSummaries: List[ActionGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentKnowledgeBasesResponseTypeDef(BaseModel):
    agentKnowledgeBaseSummaries: List[AgentKnowledgeBaseSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PrepareAgentResponseTypeDef(BaseModel):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    preparedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PrepareFlowResponseTypeDef(BaseModel):
    id: str
    status: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentKnowledgeBaseResponseTypeDef(BaseModel):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmbeddingModelConfigurationTypeDef(BaseModel):
    bedrockEmbeddingModelConfiguration: Optional[       BedrockEmbeddingModelConfigurationTypeDef     ] = None

class BedrockFoundationModelConfigurationTypeDef(BaseModel):
    modelArn: str
    parsingPrompt: Optional[ParsingPromptTypeDef] = None

class ConditionFlowNodeConfigurationOutputTypeDef(BaseModel):
    conditions: List[FlowConditionTypeDef]

class ConditionFlowNodeConfigurationTypeDef(BaseModel):
    conditions: Sequence[FlowConditionTypeDef]

class CreateFlowAliasRequestRequestTypeDef(BaseModel):
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateFlowAliasResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    description: str
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class FlowAliasSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    description: Optional[str] = None

class GetFlowAliasResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    description: str
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowAliasRequestRequestTypeDef(BaseModel):
    aliasIdentifier: str
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    description: Optional[str] = None

class UpdateFlowAliasResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    description: str
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourcesResponseTypeDef(BaseModel):
    dataSourceSummaries: List[DataSourceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FlowConnectionConfigurationTypeDef(BaseModel):
    conditional: Optional[FlowConditionalConnectionConfigurationTypeDef] = None
    data: Optional[FlowDataConnectionConfigurationTypeDef] = None

class ListFlowsResponseTypeDef(BaseModel):
    flowSummaries: List[FlowSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFlowVersionsResponseTypeDef(BaseModel):
    flowVersionSummaries: List[FlowVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionOutputTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, ParameterDetailTypeDef]] = None

class FunctionTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Mapping[str, ParameterDetailTypeDef]] = None

class HierarchicalChunkingConfigurationOutputTypeDef(BaseModel):
    levelConfigurations: List[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int

class HierarchicalChunkingConfigurationTypeDef(BaseModel):
    levelConfigurations: Sequence[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int

class PromptConfigurationOutputTypeDef(BaseModel):
    basePromptTemplate: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationOutputTypeDef] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None

class PromptConfigurationTypeDef(BaseModel):
    basePromptTemplate: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationTypeDef] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None

class ListIngestionJobsRequestRequestTypeDef(BaseModel):
    dataSourceId: str
    knowledgeBaseId: str
    filters: Optional[Sequence[IngestionJobFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[IngestionJobSortByTypeDef] = None

class IngestionJobSummaryTypeDef(BaseModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str
    startedAt: datetime
    status: IngestionJobStatusType
    updatedAt: datetime
    description: Optional[str] = None
    statistics: Optional[IngestionJobStatisticsTypeDef] = None

class IngestionJobTypeDef(BaseModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str
    startedAt: datetime
    status: IngestionJobStatusType
    updatedAt: datetime
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    statistics: Optional[IngestionJobStatisticsTypeDef] = None

class IntermediateStorageTypeDef(BaseModel):
    s3Location: S3LocationTypeDef

class ListKnowledgeBasesResponseTypeDef(BaseModel):
    knowledgeBaseSummaries: List[KnowledgeBaseSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentActionGroupsRequestListAgentActionGroupsPaginateTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgentAliasesRequestListAgentAliasesPaginateTypeDef(BaseModel):
    agentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgentKnowledgeBasesRequestListAgentKnowledgeBasesPaginateTypeDef(BaseModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgentVersionsRequestListAgentVersionsPaginateTypeDef(BaseModel):
    agentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgentsRequestListAgentsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesRequestListDataSourcesPaginateTypeDef(BaseModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowAliasesRequestListFlowAliasesPaginateTypeDef(BaseModel):
    flowIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowVersionsRequestListFlowVersionsPaginateTypeDef(BaseModel):
    flowIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowsRequestListFlowsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIngestionJobsRequestListIngestionJobsPaginateTypeDef(BaseModel):
    dataSourceId: str
    knowledgeBaseId: str
    filters: Optional[Sequence[IngestionJobFilterTypeDef]] = None
    sortBy: Optional[IngestionJobSortByTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPromptsRequestListPromptsPaginateTypeDef(BaseModel):
    promptIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPromptsResponseTypeDef(BaseModel):
    nextToken: str
    promptSummaries: List[PromptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MongoDbAtlasConfigurationTypeDef(BaseModel):
    collectionName: str
    credentialsSecretArn: str
    databaseName: str
    endpoint: str
    fieldMapping: MongoDbAtlasFieldMappingTypeDef
    vectorIndexName: str
    endpointServiceName: Optional[str] = None

class OpenSearchServerlessConfigurationTypeDef(BaseModel):
    collectionArn: str
    fieldMapping: OpenSearchServerlessFieldMappingTypeDef
    vectorIndexName: str

class PatternObjectFilterConfigurationOutputTypeDef(BaseModel):
    filters: List[PatternObjectFilterOutputTypeDef]

class PatternObjectFilterConfigurationTypeDef(BaseModel):
    filters: Sequence[PatternObjectFilterTypeDef]

class PineconeConfigurationTypeDef(BaseModel):
    connectionString: str
    credentialsSecretArn: str
    fieldMapping: PineconeFieldMappingTypeDef
    namespace: Optional[str] = None

class PromptInferenceConfigurationOutputTypeDef(BaseModel):
    text: Optional[PromptModelInferenceConfigurationOutputTypeDef] = None

class PromptInferenceConfigurationTypeDef(BaseModel):
    text: Optional[PromptModelInferenceConfigurationTypeDef] = None

class TextPromptTemplateConfigurationOutputTypeDef(BaseModel):
    text: str
    inputVariables: Optional[List[PromptInputVariableTypeDef]] = None

class TextPromptTemplateConfigurationTypeDef(BaseModel):
    text: str
    inputVariables: Optional[Sequence[PromptInputVariableTypeDef]] = None

class RdsConfigurationTypeDef(BaseModel):
    credentialsSecretArn: str
    databaseName: str
    fieldMapping: RdsFieldMappingTypeDef
    resourceArn: str
    tableName: str

class RedisEnterpriseCloudConfigurationTypeDef(BaseModel):
    credentialsSecretArn: str
    endpoint: str
    fieldMapping: RedisEnterpriseCloudFieldMappingTypeDef
    vectorIndexName: str

class RetrievalFlowNodeServiceConfigurationTypeDef(BaseModel):
    s3: Optional[RetrievalFlowNodeS3ConfigurationTypeDef] = None

class UrlConfigurationOutputTypeDef(BaseModel):
    seedUrls: Optional[List[SeedUrlTypeDef]] = None

class UrlConfigurationTypeDef(BaseModel):
    seedUrls: Optional[Sequence[SeedUrlTypeDef]] = None

class StorageFlowNodeServiceConfigurationTypeDef(BaseModel):
    s3: Optional[StorageFlowNodeS3ConfigurationTypeDef] = None

class TransformationFunctionTypeDef(BaseModel):
    transformationLambdaConfiguration: TransformationLambdaConfigurationTypeDef

class WebCrawlerConfigurationOutputTypeDef(BaseModel):
    crawlerLimits: Optional[WebCrawlerLimitsTypeDef] = None
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None
    scope: Optional[WebScopeTypeType] = None

class WebCrawlerConfigurationTypeDef(BaseModel):
    crawlerLimits: Optional[WebCrawlerLimitsTypeDef] = None
    exclusionFilters: Optional[Sequence[str]] = None
    inclusionFilters: Optional[Sequence[str]] = None
    scope: Optional[WebScopeTypeType] = None

class AgentAliasTypeDef(BaseModel):
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

class ListAgentAliasesResponseTypeDef(BaseModel):
    agentAliasSummaries: List[AgentAliasSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentsResponseTypeDef(BaseModel):
    agentSummaries: List[AgentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentVersionsResponseTypeDef(BaseModel):
    agentVersionSummaries: List[AgentVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class VectorKnowledgeBaseConfigurationTypeDef(BaseModel):
    embeddingModelArn: str
    embeddingModelConfiguration: Optional[EmbeddingModelConfigurationTypeDef] = None

class ParsingConfigurationTypeDef(BaseModel):
    parsingStrategy: Literal["BEDROCK_FOUNDATION_MODEL"]
    bedrockFoundationModelConfiguration: Optional[       BedrockFoundationModelConfigurationTypeDef     ] = None

class ListFlowAliasesResponseTypeDef(BaseModel):
    flowAliasSummaries: List[FlowAliasSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FlowConnectionTypeDef(BaseModel):
    name: str
    source: str
    target: str
    type: FlowConnectionTypeType
    configuration: Optional[FlowConnectionConfigurationTypeDef] = None

class FunctionSchemaOutputTypeDef(BaseModel):
    functions: Optional[List[FunctionOutputTypeDef]] = None

class FunctionSchemaTypeDef(BaseModel):
    functions: Optional[Sequence[FunctionTypeDef]] = None

class ChunkingConfigurationOutputTypeDef(BaseModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfigurationTypeDef] = None
    hierarchicalChunkingConfiguration: Optional[       HierarchicalChunkingConfigurationOutputTypeDef     ] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfigurationTypeDef] = None

class ChunkingConfigurationTypeDef(BaseModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfigurationTypeDef] = None
    hierarchicalChunkingConfiguration: Optional[HierarchicalChunkingConfigurationTypeDef] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfigurationTypeDef] = None

class PromptOverrideConfigurationOutputTypeDef(BaseModel):
    promptConfigurations: List[PromptConfigurationOutputTypeDef]
    overrideLambda: Optional[str] = None

class PromptOverrideConfigurationTypeDef(BaseModel):
    promptConfigurations: Sequence[PromptConfigurationTypeDef]
    overrideLambda: Optional[str] = None

class ListIngestionJobsResponseTypeDef(BaseModel):
    ingestionJobSummaries: List[IngestionJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIngestionJobResponseTypeDef(BaseModel):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartIngestionJobResponseTypeDef(BaseModel):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CrawlFilterConfigurationOutputTypeDef(BaseModel):
    type: Literal["PATTERN"]
    patternObjectFilter: Optional[PatternObjectFilterConfigurationOutputTypeDef] = None

class CrawlFilterConfigurationTypeDef(BaseModel):
    type: Literal["PATTERN"]
    patternObjectFilter: Optional[PatternObjectFilterConfigurationTypeDef] = None

class PromptTemplateConfigurationOutputTypeDef(BaseModel):
    text: Optional[TextPromptTemplateConfigurationOutputTypeDef] = None

class PromptTemplateConfigurationTypeDef(BaseModel):
    text: Optional[TextPromptTemplateConfigurationTypeDef] = None

class StorageConfigurationTypeDef(BaseModel):
    type: KnowledgeBaseStorageTypeType
    mongoDbAtlasConfiguration: Optional[MongoDbAtlasConfigurationTypeDef] = None
    opensearchServerlessConfiguration: Optional[OpenSearchServerlessConfigurationTypeDef] = None
    pineconeConfiguration: Optional[PineconeConfigurationTypeDef] = None
    rdsConfiguration: Optional[RdsConfigurationTypeDef] = None
    redisEnterpriseCloudConfiguration: Optional[RedisEnterpriseCloudConfigurationTypeDef] = None

class RetrievalFlowNodeConfigurationTypeDef(BaseModel):
    serviceConfiguration: RetrievalFlowNodeServiceConfigurationTypeDef

class WebSourceConfigurationOutputTypeDef(BaseModel):
    urlConfiguration: UrlConfigurationOutputTypeDef

class WebSourceConfigurationTypeDef(BaseModel):
    urlConfiguration: UrlConfigurationTypeDef

class StorageFlowNodeConfigurationTypeDef(BaseModel):
    serviceConfiguration: StorageFlowNodeServiceConfigurationTypeDef

class TransformationTypeDef(BaseModel):
    stepToApply: Literal["POST_CHUNKING"]
    transformationFunction: TransformationFunctionTypeDef

class CreateAgentAliasResponseTypeDef(BaseModel):
    agentAlias: AgentAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentAliasResponseTypeDef(BaseModel):
    agentAlias: AgentAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentAliasResponseTypeDef(BaseModel):
    agentAlias: AgentAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KnowledgeBaseConfigurationTypeDef(BaseModel):
    type: Literal["VECTOR"]
    vectorKnowledgeBaseConfiguration: Optional[VectorKnowledgeBaseConfigurationTypeDef] = None

class AgentActionGroupTypeDef(BaseModel):
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
    parentActionSignature: Optional[ActionGroupSignatureType] = None

class CreateAgentActionGroupRequestRequestTypeDef(BaseModel):
    actionGroupName: str
    agentId: str
    agentVersion: str
    actionGroupExecutor: Optional[ActionGroupExecutorTypeDef] = None
    actionGroupState: Optional[ActionGroupStateType] = None
    apiSchema: Optional[APISchemaTypeDef] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchemaTypeDef] = None
    parentActionGroupSignature: Optional[ActionGroupSignatureType] = None

class UpdateAgentActionGroupRequestRequestTypeDef(BaseModel):
    actionGroupId: str
    actionGroupName: str
    agentId: str
    agentVersion: str
    actionGroupExecutor: Optional[ActionGroupExecutorTypeDef] = None
    actionGroupState: Optional[ActionGroupStateType] = None
    apiSchema: Optional[APISchemaTypeDef] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchemaTypeDef] = None
    parentActionGroupSignature: Optional[ActionGroupSignatureType] = None

class AgentTypeDef(BaseModel):
    agentArn: str
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    agentStatus: AgentStatusType
    agentVersion: str
    createdAt: datetime
    idleSessionTTLInSeconds: int
    updatedAt: datetime
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    foundationModel: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationOutputTypeDef] = None
    preparedAt: Optional[datetime] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationOutputTypeDef] = None
    recommendedActions: Optional[List[str]] = None

class AgentVersionTypeDef(BaseModel):
    agentArn: str
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    agentStatus: AgentStatusType
    createdAt: datetime
    idleSessionTTLInSeconds: int
    updatedAt: datetime
    version: str
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    foundationModel: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationOutputTypeDef] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationOutputTypeDef] = None
    recommendedActions: Optional[List[str]] = None

class CreateAgentRequestRequestTypeDef(BaseModel):
    agentName: str
    agentResourceRoleArn: Optional[str] = None
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    foundationModel: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    idleSessionTTLInSeconds: Optional[int] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationTypeDef] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateAgentRequestRequestTypeDef(BaseModel):
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    foundationModel: str
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    idleSessionTTLInSeconds: Optional[int] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationTypeDef] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationTypeDef] = None

class ConfluenceCrawlerConfigurationOutputTypeDef(BaseModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutputTypeDef] = None

class SalesforceCrawlerConfigurationOutputTypeDef(BaseModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutputTypeDef] = None

class SharePointCrawlerConfigurationOutputTypeDef(BaseModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutputTypeDef] = None

class ConfluenceCrawlerConfigurationTypeDef(BaseModel):
    filterConfiguration: Optional[CrawlFilterConfigurationTypeDef] = None

class SalesforceCrawlerConfigurationTypeDef(BaseModel):
    filterConfiguration: Optional[CrawlFilterConfigurationTypeDef] = None

class SharePointCrawlerConfigurationTypeDef(BaseModel):
    filterConfiguration: Optional[CrawlFilterConfigurationTypeDef] = None

class PromptFlowNodeInlineConfigurationOutputTypeDef(BaseModel):
    modelId: str
    templateConfiguration: PromptTemplateConfigurationOutputTypeDef
    templateType: Literal["TEXT"]
    inferenceConfiguration: Optional[PromptInferenceConfigurationOutputTypeDef] = None

class PromptVariantOutputTypeDef(BaseModel):
    name: str
    templateType: Literal["TEXT"]
    inferenceConfiguration: Optional[PromptInferenceConfigurationOutputTypeDef] = None
    modelId: Optional[str] = None
    templateConfiguration: Optional[PromptTemplateConfigurationOutputTypeDef] = None

class PromptFlowNodeInlineConfigurationTypeDef(BaseModel):
    modelId: str
    templateConfiguration: PromptTemplateConfigurationTypeDef
    templateType: Literal["TEXT"]
    inferenceConfiguration: Optional[PromptInferenceConfigurationTypeDef] = None

class PromptVariantTypeDef(BaseModel):
    name: str
    templateType: Literal["TEXT"]
    inferenceConfiguration: Optional[PromptInferenceConfigurationTypeDef] = None
    modelId: Optional[str] = None
    templateConfiguration: Optional[PromptTemplateConfigurationTypeDef] = None

class WebDataSourceConfigurationOutputTypeDef(BaseModel):
    sourceConfiguration: WebSourceConfigurationOutputTypeDef
    crawlerConfiguration: Optional[WebCrawlerConfigurationOutputTypeDef] = None

class WebDataSourceConfigurationTypeDef(BaseModel):
    sourceConfiguration: WebSourceConfigurationTypeDef
    crawlerConfiguration: Optional[WebCrawlerConfigurationTypeDef] = None

class CustomTransformationConfigurationOutputTypeDef(BaseModel):
    intermediateStorage: IntermediateStorageTypeDef
    transformations: List[TransformationTypeDef]

class CustomTransformationConfigurationTypeDef(BaseModel):
    intermediateStorage: IntermediateStorageTypeDef
    transformations: Sequence[TransformationTypeDef]

class CreateKnowledgeBaseRequestRequestTypeDef(BaseModel):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationTypeDef
    name: str
    roleArn: str
    storageConfiguration: StorageConfigurationTypeDef
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class KnowledgeBaseTypeDef(BaseModel):
    createdAt: datetime
    knowledgeBaseArn: str
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationTypeDef
    knowledgeBaseId: str
    name: str
    roleArn: str
    status: KnowledgeBaseStatusType
    storageConfiguration: StorageConfigurationTypeDef
    updatedAt: datetime
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None

class UpdateKnowledgeBaseRequestRequestTypeDef(BaseModel):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationTypeDef
    knowledgeBaseId: str
    name: str
    roleArn: str
    storageConfiguration: StorageConfigurationTypeDef
    description: Optional[str] = None

class CreateAgentActionGroupResponseTypeDef(BaseModel):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentActionGroupResponseTypeDef(BaseModel):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentActionGroupResponseTypeDef(BaseModel):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgentResponseTypeDef(BaseModel):
    agent: AgentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentResponseTypeDef(BaseModel):
    agent: AgentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentResponseTypeDef(BaseModel):
    agent: AgentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentVersionResponseTypeDef(BaseModel):
    agentVersion: AgentVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConfluenceDataSourceConfigurationOutputTypeDef(BaseModel):
    sourceConfiguration: ConfluenceSourceConfigurationTypeDef
    crawlerConfiguration: Optional[ConfluenceCrawlerConfigurationOutputTypeDef] = None

class SalesforceDataSourceConfigurationOutputTypeDef(BaseModel):
    sourceConfiguration: SalesforceSourceConfigurationTypeDef
    crawlerConfiguration: Optional[SalesforceCrawlerConfigurationOutputTypeDef] = None

class SharePointDataSourceConfigurationOutputTypeDef(BaseModel):
    sourceConfiguration: SharePointSourceConfigurationOutputTypeDef
    crawlerConfiguration: Optional[SharePointCrawlerConfigurationOutputTypeDef] = None

class ConfluenceDataSourceConfigurationTypeDef(BaseModel):
    sourceConfiguration: ConfluenceSourceConfigurationTypeDef
    crawlerConfiguration: Optional[ConfluenceCrawlerConfigurationTypeDef] = None

class SalesforceDataSourceConfigurationTypeDef(BaseModel):
    sourceConfiguration: SalesforceSourceConfigurationTypeDef
    crawlerConfiguration: Optional[SalesforceCrawlerConfigurationTypeDef] = None

class SharePointDataSourceConfigurationTypeDef(BaseModel):
    sourceConfiguration: SharePointSourceConfigurationTypeDef
    crawlerConfiguration: Optional[SharePointCrawlerConfigurationTypeDef] = None

class PromptFlowNodeSourceConfigurationOutputTypeDef(BaseModel):
    inline: Optional[PromptFlowNodeInlineConfigurationOutputTypeDef] = None
    resource: Optional[PromptFlowNodeResourceConfigurationTypeDef] = None

class CreatePromptResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    defaultVariant: str
    description: str
    id: str
    name: str
    updatedAt: datetime
    variants: List[PromptVariantOutputTypeDef]
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePromptVersionResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    defaultVariant: str
    description: str
    id: str
    name: str
    updatedAt: datetime
    variants: List[PromptVariantOutputTypeDef]
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPromptResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    defaultVariant: str
    description: str
    id: str
    name: str
    updatedAt: datetime
    variants: List[PromptVariantOutputTypeDef]
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePromptResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    defaultVariant: str
    description: str
    id: str
    name: str
    updatedAt: datetime
    variants: List[PromptVariantOutputTypeDef]
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class PromptFlowNodeSourceConfigurationTypeDef(BaseModel):
    inline: Optional[PromptFlowNodeInlineConfigurationTypeDef] = None
    resource: Optional[PromptFlowNodeResourceConfigurationTypeDef] = None

class VectorIngestionConfigurationOutputTypeDef(BaseModel):
    chunkingConfiguration: Optional[ChunkingConfigurationOutputTypeDef] = None
    customTransformationConfiguration: Optional[       CustomTransformationConfigurationOutputTypeDef     ] = None
    parsingConfiguration: Optional[ParsingConfigurationTypeDef] = None

class VectorIngestionConfigurationTypeDef(BaseModel):
    chunkingConfiguration: Optional[ChunkingConfigurationTypeDef] = None
    customTransformationConfiguration: Optional[CustomTransformationConfigurationTypeDef] = None
    parsingConfiguration: Optional[ParsingConfigurationTypeDef] = None

class CreateKnowledgeBaseResponseTypeDef(BaseModel):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKnowledgeBaseResponseTypeDef(BaseModel):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKnowledgeBaseResponseTypeDef(BaseModel):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceConfigurationOutputTypeDef(BaseModel):
    type: DataSourceTypeType
    confluenceConfiguration: Optional[ConfluenceDataSourceConfigurationOutputTypeDef] = None
    s3Configuration: Optional[S3DataSourceConfigurationOutputTypeDef] = None
    salesforceConfiguration: Optional[SalesforceDataSourceConfigurationOutputTypeDef] = None
    sharePointConfiguration: Optional[SharePointDataSourceConfigurationOutputTypeDef] = None
    webConfiguration: Optional[WebDataSourceConfigurationOutputTypeDef] = None

class DataSourceConfigurationTypeDef(BaseModel):
    type: DataSourceTypeType
    confluenceConfiguration: Optional[ConfluenceDataSourceConfigurationTypeDef] = None
    s3Configuration: Optional[S3DataSourceConfigurationTypeDef] = None
    salesforceConfiguration: Optional[SalesforceDataSourceConfigurationTypeDef] = None
    sharePointConfiguration: Optional[SharePointDataSourceConfigurationTypeDef] = None
    webConfiguration: Optional[WebDataSourceConfigurationTypeDef] = None

class PromptFlowNodeConfigurationOutputTypeDef(BaseModel):
    sourceConfiguration: PromptFlowNodeSourceConfigurationOutputTypeDef

class PromptFlowNodeConfigurationTypeDef(BaseModel):
    sourceConfiguration: PromptFlowNodeSourceConfigurationTypeDef

class CreatePromptRequestRequestTypeDef(BaseModel):
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    variants: Optional[Sequence[PromptVariantUnionTypeDef]] = None

class UpdatePromptRequestRequestTypeDef(BaseModel):
    name: str
    promptIdentifier: str
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    variants: Optional[Sequence[PromptVariantUnionTypeDef]] = None

class DataSourceTypeDef(BaseModel):
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

class CreateDataSourceRequestRequestTypeDef(BaseModel):
    dataSourceConfiguration: DataSourceConfigurationTypeDef
    knowledgeBaseId: str
    name: str
    clientToken: Optional[str] = None
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationTypeDef] = None

class UpdateDataSourceRequestRequestTypeDef(BaseModel):
    dataSourceConfiguration: DataSourceConfigurationTypeDef
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationTypeDef] = None

class FlowNodeConfigurationOutputTypeDef(BaseModel):
    agent: Optional[AgentFlowNodeConfigurationTypeDef] = None
    collector: Optional[Dict[str, Any]] = None
    condition: Optional[ConditionFlowNodeConfigurationOutputTypeDef] = None
    input: Optional[Dict[str, Any]] = None
    iterator: Optional[Dict[str, Any]] = None
    knowledgeBase: Optional[KnowledgeBaseFlowNodeConfigurationTypeDef] = None
    lambdaFunction: Optional[LambdaFunctionFlowNodeConfigurationTypeDef] = None
    lex: Optional[LexFlowNodeConfigurationTypeDef] = None
    output: Optional[Dict[str, Any]] = None
    prompt: Optional[PromptFlowNodeConfigurationOutputTypeDef] = None
    retrieval: Optional[RetrievalFlowNodeConfigurationTypeDef] = None
    storage: Optional[StorageFlowNodeConfigurationTypeDef] = None

class FlowNodeConfigurationTypeDef(BaseModel):
    agent: Optional[AgentFlowNodeConfigurationTypeDef] = None
    collector: Optional[Mapping[str, Any]] = None
    condition: Optional[ConditionFlowNodeConfigurationTypeDef] = None
    input: Optional[Mapping[str, Any]] = None
    iterator: Optional[Mapping[str, Any]] = None
    knowledgeBase: Optional[KnowledgeBaseFlowNodeConfigurationTypeDef] = None
    lambdaFunction: Optional[LambdaFunctionFlowNodeConfigurationTypeDef] = None
    lex: Optional[LexFlowNodeConfigurationTypeDef] = None
    output: Optional[Mapping[str, Any]] = None
    prompt: Optional[PromptFlowNodeConfigurationTypeDef] = None
    retrieval: Optional[RetrievalFlowNodeConfigurationTypeDef] = None
    storage: Optional[StorageFlowNodeConfigurationTypeDef] = None

class CreateDataSourceResponseTypeDef(BaseModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceResponseTypeDef(BaseModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceResponseTypeDef(BaseModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FlowNodeExtraOutputTypeDef(BaseModel):
    name: str
    type: FlowNodeTypeType
    configuration: Optional[FlowNodeConfigurationOutputTypeDef] = None
    inputs: Optional[List[FlowNodeInputTypeDef]] = None
    outputs: Optional[List[FlowNodeOutputTypeDef]] = None

class FlowNodeTypeDef(BaseModel):
    name: str
    type: FlowNodeTypeType
    configuration: Optional[FlowNodeConfigurationTypeDef] = None
    inputs: Optional[Sequence[FlowNodeInputTypeDef]] = None
    outputs: Optional[Sequence[FlowNodeOutputTypeDef]] = None

class FlowDefinitionOutputTypeDef(BaseModel):
    connections: Optional[List[FlowConnectionTypeDef]] = None
    nodes: Optional[List[FlowNodeExtraOutputTypeDef]] = None

class FlowDefinitionTypeDef(BaseModel):
    connections: Optional[Sequence[FlowConnectionTypeDef]] = None
    nodes: Optional[Sequence[FlowNodeTypeDef]] = None

class CreateFlowResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutputTypeDef
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    updatedAt: datetime
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowVersionResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutputTypeDef
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutputTypeDef
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    updatedAt: datetime
    validations: List[FlowValidationTypeDef]
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowVersionResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutputTypeDef
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    customerEncryptionKeyArn: str
    definition: FlowDefinitionOutputTypeDef
    description: str
    executionRoleArn: str
    id: str
    name: str
    status: FlowStatusType
    updatedAt: datetime
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowRequestRequestTypeDef(BaseModel):
    executionRoleArn: str
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionTypeDef] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateFlowRequestRequestTypeDef(BaseModel):
    executionRoleArn: str
    flowIdentifier: str
    name: str
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionTypeDef] = None
    description: Optional[str] = None


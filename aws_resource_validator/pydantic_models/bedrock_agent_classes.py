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
from aws_resource_validator.pydantic_models.bedrock_agent_constants import *

class S3IdentifierTypeDef(BaseValidatorModel):
    s3BucketName: Optional[str] = None
    s3ObjectKey: Optional[str] = None

class ActionGroupExecutorTypeDef(BaseValidatorModel):
    customControl: Optional[Literal["RETURN_CONTROL"]] = None
    _lambda: Optional[str] = None

class ActionGroupSummaryTypeDef(BaseValidatorModel):
    actionGroupId: str
    actionGroupName: str
    actionGroupState: ActionGroupStateType
    updatedAt: datetime
    description: Optional[str] = None

class AgentAliasRoutingConfigurationListItemTypeDef(BaseValidatorModel):
    agentVersion: Optional[str] = None
    provisionedThroughput: Optional[str] = None

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

class MemoryConfigurationOutputTypeDef(BaseValidatorModel):
    enabledMemoryTypes: List[Literal["SESSION_SUMMARY"]]
    storageDays: Optional[int] = None

class AssociateAgentKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: Optional[KnowledgeBaseStateType] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BedrockEmbeddingModelConfigurationTypeDef(BaseValidatorModel):
    dimensions: Optional[int] = None

class ParsingPromptTypeDef(BaseValidatorModel):
    parsingPromptText: str

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

class MemoryConfigurationTypeDef(BaseValidatorModel):
    enabledMemoryTypes: Sequence[Literal["SESSION_SUMMARY"]]
    storageDays: Optional[int] = None

class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyArn: Optional[str] = None

class FlowAliasRoutingConfigurationListItemTypeDef(BaseValidatorModel):
    flowVersion: Optional[str] = None

class CreateFlowVersionRequestRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class CreatePromptVersionRequestRequestTypeDef(BaseValidatorModel):
    promptIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

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

class DeleteAgentActionGroupRequestRequestTypeDef(BaseValidatorModel):
    actionGroupId: str
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteAgentAliasRequestRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str

class DeleteAgentRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteAgentVersionRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteDataSourceRequestRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str

class DeleteFlowAliasRequestRequestTypeDef(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str

class DeleteFlowRequestRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteFlowVersionRequestRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    flowVersion: str
    skipResourceInUseCheck: Optional[bool] = None

class DeleteKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str

class DeletePromptRequestRequestTypeDef(BaseValidatorModel):
    promptIdentifier: str
    promptVersion: Optional[str] = None

class DisassociateAgentKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str

class FlowConditionalConnectionConfigurationTypeDef(BaseValidatorModel):
    condition: str

class FlowDataConnectionConfigurationTypeDef(BaseValidatorModel):
    sourceOutput: str
    targetInput: str

class KnowledgeBaseFlowNodeConfigurationTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    modelId: Optional[str] = None

class LambdaFunctionFlowNodeConfigurationTypeDef(BaseValidatorModel):
    lambdaArn: str

class LexFlowNodeConfigurationTypeDef(BaseValidatorModel):
    botAliasArn: str
    localeId: str

class FlowNodeInputTypeDef(BaseValidatorModel):
    expression: str
    name: str
    type: FlowNodeIODataTypeType

class FlowNodeOutputTypeDef(BaseValidatorModel):
    name: str
    type: FlowNodeIODataTypeType

class FlowSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    id: str
    name: str
    status: FlowStatusType
    updatedAt: datetime
    version: str
    description: Optional[str] = None

class FlowValidationTypeDef(BaseValidatorModel):
    message: str
    severity: FlowValidationSeverityType

class FlowVersionSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    id: str
    status: FlowStatusType
    version: str

class ParameterDetailTypeDef(BaseValidatorModel):
    type: TypeType
    description: Optional[str] = None
    required: Optional[bool] = None

class GetAgentActionGroupRequestRequestTypeDef(BaseValidatorModel):
    actionGroupId: str
    agentId: str
    agentVersion: str

class GetAgentAliasRequestRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str

class GetAgentKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str

class GetAgentRequestRequestTypeDef(BaseValidatorModel):
    agentId: str

class GetAgentVersionRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str

class GetDataSourceRequestRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str

class GetFlowAliasRequestRequestTypeDef(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str

class GetFlowRequestRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str

class GetFlowVersionRequestRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    flowVersion: str

class GetIngestionJobRequestRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str

class GetKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str

class GetPromptRequestRequestTypeDef(BaseValidatorModel):
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

class IngestionJobFilterTypeDef(BaseValidatorModel):
    attribute: Literal["STATUS"]
    operator: Literal["EQ"]
    values: Sequence[str]

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

class S3LocationTypeDef(BaseValidatorModel):
    uri: str

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

class ListAgentActionGroupsRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAgentAliasesRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAgentKnowledgeBasesRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAgentVersionsRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAgentsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDataSourcesRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFlowAliasesRequestRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFlowVersionsRequestRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFlowsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListKnowledgeBasesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPromptsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    promptIdentifier: Optional[str] = None

class PromptSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    id: str
    name: str
    updatedAt: datetime
    version: str
    description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class MongoDbAtlasFieldMappingTypeDef(BaseValidatorModel):
    metadataField: str
    textField: str
    vectorField: str

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

class PrepareAgentRequestRequestTypeDef(BaseValidatorModel):
    agentId: str

class PrepareFlowRequestRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str

class PromptFlowNodeResourceConfigurationTypeDef(BaseValidatorModel):
    promptArn: str

class PromptModelInferenceConfigurationOutputTypeDef(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None

class PromptModelInferenceConfigurationTypeDef(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None

class PromptInputVariableTypeDef(BaseValidatorModel):
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

class RetrievalFlowNodeS3ConfigurationTypeDef(BaseValidatorModel):
    bucketName: str

class SalesforceSourceConfigurationTypeDef(BaseValidatorModel):
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str
    hostUrl: str

class SeedUrlTypeDef(BaseValidatorModel):
    url: Optional[str] = None

class SharePointSourceConfigurationOutputTypeDef(BaseValidatorModel):
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: List[str]
    tenantId: Optional[str] = None

class SharePointSourceConfigurationTypeDef(BaseValidatorModel):
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: Sequence[str]
    tenantId: Optional[str] = None

class StartIngestionJobRequestRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class StorageFlowNodeS3ConfigurationTypeDef(BaseValidatorModel):
    bucketName: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TransformationLambdaConfigurationTypeDef(BaseValidatorModel):
    lambdaArn: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAgentKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str
    description: Optional[str] = None
    knowledgeBaseState: Optional[KnowledgeBaseStateType] = None

class WebCrawlerLimitsTypeDef(BaseValidatorModel):
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

class CreateAgentAliasRequestRequestTypeDef(BaseValidatorModel):
    agentAliasName: str
    agentId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    routingConfiguration: Optional[       Sequence[AgentAliasRoutingConfigurationListItemTypeDef]     ] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateAgentAliasRequestRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentAliasName: str
    agentId: str
    description: Optional[str] = None
    routingConfiguration: Optional[       Sequence[AgentAliasRoutingConfigurationListItemTypeDef]     ] = None

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

class DeleteFlowAliasResponseTypeDef(BaseValidatorModel):
    flowId: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowResponseTypeDef(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowVersionResponseTypeDef(BaseValidatorModel):
    id: str
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    status: KnowledgeBaseStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePromptResponseTypeDef(BaseValidatorModel):
    id: str
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentActionGroupsResponseTypeDef(BaseValidatorModel):
    actionGroupSummaries: List[ActionGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentKnowledgeBasesResponseTypeDef(BaseValidatorModel):
    agentKnowledgeBaseSummaries: List[AgentKnowledgeBaseSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PrepareAgentResponseTypeDef(BaseValidatorModel):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    preparedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PrepareFlowResponseTypeDef(BaseValidatorModel):
    id: str
    status: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmbeddingModelConfigurationTypeDef(BaseValidatorModel):
    bedrockEmbeddingModelConfiguration: Optional[       BedrockEmbeddingModelConfigurationTypeDef     ] = None

class BedrockFoundationModelConfigurationTypeDef(BaseValidatorModel):
    modelArn: str
    parsingPrompt: Optional[ParsingPromptTypeDef] = None

class ConditionFlowNodeConfigurationOutputTypeDef(BaseValidatorModel):
    conditions: List[FlowConditionTypeDef]

class ConditionFlowNodeConfigurationTypeDef(BaseValidatorModel):
    conditions: Sequence[FlowConditionTypeDef]

class CreateFlowAliasRequestRequestTypeDef(BaseValidatorModel):
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateFlowAliasResponseTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    description: str
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class FlowAliasSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    description: Optional[str] = None

class GetFlowAliasResponseTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    description: str
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowAliasRequestRequestTypeDef(BaseValidatorModel):
    aliasIdentifier: str
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    description: Optional[str] = None

class UpdateFlowAliasResponseTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    description: str
    flowId: str
    id: str
    name: str
    routingConfiguration: List[FlowAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    dataSourceSummaries: List[DataSourceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FlowConnectionConfigurationTypeDef(BaseValidatorModel):
    conditional: Optional[FlowConditionalConnectionConfigurationTypeDef] = None
    data: Optional[FlowDataConnectionConfigurationTypeDef] = None

class ListFlowsResponseTypeDef(BaseValidatorModel):
    flowSummaries: List[FlowSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFlowVersionsResponseTypeDef(BaseValidatorModel):
    flowVersionSummaries: List[FlowVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionOutputTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, ParameterDetailTypeDef]] = None

class FunctionTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Mapping[str, ParameterDetailTypeDef]] = None

class HierarchicalChunkingConfigurationOutputTypeDef(BaseValidatorModel):
    levelConfigurations: List[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int

class HierarchicalChunkingConfigurationTypeDef(BaseValidatorModel):
    levelConfigurations: Sequence[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int

class PromptConfigurationOutputTypeDef(BaseValidatorModel):
    basePromptTemplate: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationOutputTypeDef] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None

class PromptConfigurationTypeDef(BaseValidatorModel):
    basePromptTemplate: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationTypeDef] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None

class ListIngestionJobsRequestRequestTypeDef(BaseValidatorModel):
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

class IntermediateStorageTypeDef(BaseValidatorModel):
    s3Location: S3LocationTypeDef

class ListKnowledgeBasesResponseTypeDef(BaseValidatorModel):
    knowledgeBaseSummaries: List[KnowledgeBaseSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentActionGroupsRequestListAgentActionGroupsPaginateTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgentAliasesRequestListAgentAliasesPaginateTypeDef(BaseValidatorModel):
    agentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgentKnowledgeBasesRequestListAgentKnowledgeBasesPaginateTypeDef(BaseValidatorModel):
    agentId: str
    agentVersion: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgentVersionsRequestListAgentVersionsPaginateTypeDef(BaseValidatorModel):
    agentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgentsRequestListAgentsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesRequestListDataSourcesPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowAliasesRequestListFlowAliasesPaginateTypeDef(BaseValidatorModel):
    flowIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowVersionsRequestListFlowVersionsPaginateTypeDef(BaseValidatorModel):
    flowIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowsRequestListFlowsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIngestionJobsRequestListIngestionJobsPaginateTypeDef(BaseValidatorModel):
    dataSourceId: str
    knowledgeBaseId: str
    filters: Optional[Sequence[IngestionJobFilterTypeDef]] = None
    sortBy: Optional[IngestionJobSortByTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPromptsRequestListPromptsPaginateTypeDef(BaseValidatorModel):
    promptIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPromptsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    promptSummaries: List[PromptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MongoDbAtlasConfigurationTypeDef(BaseValidatorModel):
    collectionName: str
    credentialsSecretArn: str
    databaseName: str
    endpoint: str
    fieldMapping: MongoDbAtlasFieldMappingTypeDef
    vectorIndexName: str
    endpointServiceName: Optional[str] = None

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

class PromptInferenceConfigurationOutputTypeDef(BaseValidatorModel):
    text: Optional[PromptModelInferenceConfigurationOutputTypeDef] = None

class PromptInferenceConfigurationTypeDef(BaseValidatorModel):
    text: Optional[PromptModelInferenceConfigurationTypeDef] = None

class TextPromptTemplateConfigurationOutputTypeDef(BaseValidatorModel):
    text: str
    inputVariables: Optional[List[PromptInputVariableTypeDef]] = None

class TextPromptTemplateConfigurationTypeDef(BaseValidatorModel):
    text: str
    inputVariables: Optional[Sequence[PromptInputVariableTypeDef]] = None

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

class RetrievalFlowNodeServiceConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[RetrievalFlowNodeS3ConfigurationTypeDef] = None

class UrlConfigurationOutputTypeDef(BaseValidatorModel):
    seedUrls: Optional[List[SeedUrlTypeDef]] = None

class UrlConfigurationTypeDef(BaseValidatorModel):
    seedUrls: Optional[Sequence[SeedUrlTypeDef]] = None

class StorageFlowNodeServiceConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[StorageFlowNodeS3ConfigurationTypeDef] = None

class TransformationFunctionTypeDef(BaseValidatorModel):
    transformationLambdaConfiguration: TransformationLambdaConfigurationTypeDef

class WebCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    crawlerLimits: Optional[WebCrawlerLimitsTypeDef] = None
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None
    scope: Optional[WebScopeTypeType] = None

class WebCrawlerConfigurationTypeDef(BaseValidatorModel):
    crawlerLimits: Optional[WebCrawlerLimitsTypeDef] = None
    exclusionFilters: Optional[Sequence[str]] = None
    inclusionFilters: Optional[Sequence[str]] = None
    scope: Optional[WebScopeTypeType] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentsResponseTypeDef(BaseValidatorModel):
    agentSummaries: List[AgentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentVersionsResponseTypeDef(BaseValidatorModel):
    agentVersionSummaries: List[AgentVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class VectorKnowledgeBaseConfigurationTypeDef(BaseValidatorModel):
    embeddingModelArn: str
    embeddingModelConfiguration: Optional[EmbeddingModelConfigurationTypeDef] = None

class ParsingConfigurationTypeDef(BaseValidatorModel):
    parsingStrategy: Literal["BEDROCK_FOUNDATION_MODEL"]
    bedrockFoundationModelConfiguration: Optional[       BedrockFoundationModelConfigurationTypeDef     ] = None

class ListFlowAliasesResponseTypeDef(BaseValidatorModel):
    flowAliasSummaries: List[FlowAliasSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FlowConnectionTypeDef(BaseValidatorModel):
    name: str
    source: str
    target: str
    type: FlowConnectionTypeType
    configuration: Optional[FlowConnectionConfigurationTypeDef] = None

class FunctionSchemaOutputTypeDef(BaseValidatorModel):
    functions: Optional[List[FunctionOutputTypeDef]] = None

class FunctionSchemaTypeDef(BaseValidatorModel):
    functions: Optional[Sequence[FunctionTypeDef]] = None

class ChunkingConfigurationOutputTypeDef(BaseValidatorModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfigurationTypeDef] = None
    hierarchicalChunkingConfiguration: Optional[       HierarchicalChunkingConfigurationOutputTypeDef     ] = None
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIngestionJobResponseTypeDef(BaseValidatorModel):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartIngestionJobResponseTypeDef(BaseValidatorModel):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CrawlFilterConfigurationOutputTypeDef(BaseValidatorModel):
    type: Literal["PATTERN"]
    patternObjectFilter: Optional[PatternObjectFilterConfigurationOutputTypeDef] = None

class CrawlFilterConfigurationTypeDef(BaseValidatorModel):
    type: Literal["PATTERN"]
    patternObjectFilter: Optional[PatternObjectFilterConfigurationTypeDef] = None

class PromptTemplateConfigurationOutputTypeDef(BaseValidatorModel):
    text: Optional[TextPromptTemplateConfigurationOutputTypeDef] = None

class PromptTemplateConfigurationTypeDef(BaseValidatorModel):
    text: Optional[TextPromptTemplateConfigurationTypeDef] = None

class StorageConfigurationTypeDef(BaseValidatorModel):
    type: KnowledgeBaseStorageTypeType
    mongoDbAtlasConfiguration: Optional[MongoDbAtlasConfigurationTypeDef] = None
    opensearchServerlessConfiguration: Optional[OpenSearchServerlessConfigurationTypeDef] = None
    pineconeConfiguration: Optional[PineconeConfigurationTypeDef] = None
    rdsConfiguration: Optional[RdsConfigurationTypeDef] = None
    redisEnterpriseCloudConfiguration: Optional[RedisEnterpriseCloudConfigurationTypeDef] = None

class RetrievalFlowNodeConfigurationTypeDef(BaseValidatorModel):
    serviceConfiguration: RetrievalFlowNodeServiceConfigurationTypeDef

class WebSourceConfigurationOutputTypeDef(BaseValidatorModel):
    urlConfiguration: UrlConfigurationOutputTypeDef

class WebSourceConfigurationTypeDef(BaseValidatorModel):
    urlConfiguration: UrlConfigurationTypeDef

class StorageFlowNodeConfigurationTypeDef(BaseValidatorModel):
    serviceConfiguration: StorageFlowNodeServiceConfigurationTypeDef

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

class KnowledgeBaseConfigurationTypeDef(BaseValidatorModel):
    type: Literal["VECTOR"]
    vectorKnowledgeBaseConfiguration: Optional[VectorKnowledgeBaseConfigurationTypeDef] = None

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
    parentActionSignature: Optional[ActionGroupSignatureType] = None

class CreateAgentActionGroupRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateAgentActionGroupRequestRequestTypeDef(BaseValidatorModel):
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
    customerEncryptionKeyArn: Optional[str] = None
    description: Optional[str] = None
    failureReasons: Optional[List[str]] = None
    foundationModel: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    instruction: Optional[str] = None
    memoryConfiguration: Optional[MemoryConfigurationOutputTypeDef] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationOutputTypeDef] = None
    recommendedActions: Optional[List[str]] = None

class CreateAgentRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateAgentRequestRequestTypeDef(BaseValidatorModel):
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

class ConfluenceCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutputTypeDef] = None

class SalesforceCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutputTypeDef] = None

class SharePointCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationOutputTypeDef] = None

class ConfluenceCrawlerConfigurationTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationTypeDef] = None

class SalesforceCrawlerConfigurationTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationTypeDef] = None

class SharePointCrawlerConfigurationTypeDef(BaseValidatorModel):
    filterConfiguration: Optional[CrawlFilterConfigurationTypeDef] = None

class PromptFlowNodeInlineConfigurationOutputTypeDef(BaseValidatorModel):
    modelId: str
    templateConfiguration: PromptTemplateConfigurationOutputTypeDef
    templateType: Literal["TEXT"]
    inferenceConfiguration: Optional[PromptInferenceConfigurationOutputTypeDef] = None

class PromptVariantOutputTypeDef(BaseValidatorModel):
    name: str
    templateType: Literal["TEXT"]
    inferenceConfiguration: Optional[PromptInferenceConfigurationOutputTypeDef] = None
    modelId: Optional[str] = None
    templateConfiguration: Optional[PromptTemplateConfigurationOutputTypeDef] = None

class PromptFlowNodeInlineConfigurationTypeDef(BaseValidatorModel):
    modelId: str
    templateConfiguration: PromptTemplateConfigurationTypeDef
    templateType: Literal["TEXT"]
    inferenceConfiguration: Optional[PromptInferenceConfigurationTypeDef] = None

class PromptVariantTypeDef(BaseValidatorModel):
    name: str
    templateType: Literal["TEXT"]
    inferenceConfiguration: Optional[PromptInferenceConfigurationTypeDef] = None
    modelId: Optional[str] = None
    templateConfiguration: Optional[PromptTemplateConfigurationTypeDef] = None

class WebDataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    sourceConfiguration: WebSourceConfigurationOutputTypeDef
    crawlerConfiguration: Optional[WebCrawlerConfigurationOutputTypeDef] = None

class WebDataSourceConfigurationTypeDef(BaseValidatorModel):
    sourceConfiguration: WebSourceConfigurationTypeDef
    crawlerConfiguration: Optional[WebCrawlerConfigurationTypeDef] = None

class CustomTransformationConfigurationOutputTypeDef(BaseValidatorModel):
    intermediateStorage: IntermediateStorageTypeDef
    transformations: List[TransformationTypeDef]

class CustomTransformationConfigurationTypeDef(BaseValidatorModel):
    intermediateStorage: IntermediateStorageTypeDef
    transformations: Sequence[TransformationTypeDef]

class CreateKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationTypeDef
    name: str
    roleArn: str
    storageConfiguration: StorageConfigurationTypeDef
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class KnowledgeBaseTypeDef(BaseValidatorModel):
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

class UpdateKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationTypeDef
    knowledgeBaseId: str
    name: str
    roleArn: str
    storageConfiguration: StorageConfigurationTypeDef
    description: Optional[str] = None

class CreateAgentActionGroupResponseTypeDef(BaseValidatorModel):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentActionGroupResponseTypeDef(BaseValidatorModel):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentActionGroupResponseTypeDef(BaseValidatorModel):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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

class PromptFlowNodeSourceConfigurationOutputTypeDef(BaseValidatorModel):
    inline: Optional[PromptFlowNodeInlineConfigurationOutputTypeDef] = None
    resource: Optional[PromptFlowNodeResourceConfigurationTypeDef] = None

class CreatePromptResponseTypeDef(BaseValidatorModel):
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

class CreatePromptVersionResponseTypeDef(BaseValidatorModel):
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

class GetPromptResponseTypeDef(BaseValidatorModel):
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

class UpdatePromptResponseTypeDef(BaseValidatorModel):
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

class PromptFlowNodeSourceConfigurationTypeDef(BaseValidatorModel):
    inline: Optional[PromptFlowNodeInlineConfigurationTypeDef] = None
    resource: Optional[PromptFlowNodeResourceConfigurationTypeDef] = None

class VectorIngestionConfigurationOutputTypeDef(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfigurationOutputTypeDef] = None
    customTransformationConfiguration: Optional[       CustomTransformationConfigurationOutputTypeDef     ] = None
    parsingConfiguration: Optional[ParsingConfigurationTypeDef] = None

class VectorIngestionConfigurationTypeDef(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfigurationTypeDef] = None
    customTransformationConfiguration: Optional[CustomTransformationConfigurationTypeDef] = None
    parsingConfiguration: Optional[ParsingConfigurationTypeDef] = None

class CreateKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    type: DataSourceTypeType
    confluenceConfiguration: Optional[ConfluenceDataSourceConfigurationOutputTypeDef] = None
    s3Configuration: Optional[S3DataSourceConfigurationOutputTypeDef] = None
    salesforceConfiguration: Optional[SalesforceDataSourceConfigurationOutputTypeDef] = None
    sharePointConfiguration: Optional[SharePointDataSourceConfigurationOutputTypeDef] = None
    webConfiguration: Optional[WebDataSourceConfigurationOutputTypeDef] = None

class DataSourceConfigurationTypeDef(BaseValidatorModel):
    type: DataSourceTypeType
    confluenceConfiguration: Optional[ConfluenceDataSourceConfigurationTypeDef] = None
    s3Configuration: Optional[S3DataSourceConfigurationTypeDef] = None
    salesforceConfiguration: Optional[SalesforceDataSourceConfigurationTypeDef] = None
    sharePointConfiguration: Optional[SharePointDataSourceConfigurationTypeDef] = None
    webConfiguration: Optional[WebDataSourceConfigurationTypeDef] = None

class PromptFlowNodeConfigurationOutputTypeDef(BaseValidatorModel):
    sourceConfiguration: PromptFlowNodeSourceConfigurationOutputTypeDef

class PromptFlowNodeConfigurationTypeDef(BaseValidatorModel):
    sourceConfiguration: PromptFlowNodeSourceConfigurationTypeDef

class CreatePromptRequestRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    variants: Optional[Sequence[PromptVariantUnionTypeDef]] = None

class UpdatePromptRequestRequestTypeDef(BaseValidatorModel):
    name: str
    promptIdentifier: str
    customerEncryptionKeyArn: Optional[str] = None
    defaultVariant: Optional[str] = None
    description: Optional[str] = None
    variants: Optional[Sequence[PromptVariantUnionTypeDef]] = None

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

class CreateDataSourceRequestRequestTypeDef(BaseValidatorModel):
    dataSourceConfiguration: DataSourceConfigurationTypeDef
    knowledgeBaseId: str
    name: str
    clientToken: Optional[str] = None
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationTypeDef] = None

class UpdateDataSourceRequestRequestTypeDef(BaseValidatorModel):
    dataSourceConfiguration: DataSourceConfigurationTypeDef
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    dataDeletionPolicy: Optional[DataDeletionPolicyType] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationTypeDef] = None

class FlowNodeConfigurationOutputTypeDef(BaseValidatorModel):
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

class FlowNodeConfigurationTypeDef(BaseValidatorModel):
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

class CreateDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FlowNodeExtraOutputTypeDef(BaseValidatorModel):
    name: str
    type: FlowNodeTypeType
    configuration: Optional[FlowNodeConfigurationOutputTypeDef] = None
    inputs: Optional[List[FlowNodeInputTypeDef]] = None
    outputs: Optional[List[FlowNodeOutputTypeDef]] = None

class FlowNodeTypeDef(BaseValidatorModel):
    name: str
    type: FlowNodeTypeType
    configuration: Optional[FlowNodeConfigurationTypeDef] = None
    inputs: Optional[Sequence[FlowNodeInputTypeDef]] = None
    outputs: Optional[Sequence[FlowNodeOutputTypeDef]] = None

class FlowDefinitionOutputTypeDef(BaseValidatorModel):
    connections: Optional[List[FlowConnectionTypeDef]] = None
    nodes: Optional[List[FlowNodeExtraOutputTypeDef]] = None

class FlowDefinitionTypeDef(BaseValidatorModel):
    connections: Optional[Sequence[FlowConnectionTypeDef]] = None
    nodes: Optional[Sequence[FlowNodeTypeDef]] = None

class CreateFlowResponseTypeDef(BaseValidatorModel):
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

class CreateFlowVersionResponseTypeDef(BaseValidatorModel):
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

class GetFlowResponseTypeDef(BaseValidatorModel):
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

class GetFlowVersionResponseTypeDef(BaseValidatorModel):
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

class UpdateFlowResponseTypeDef(BaseValidatorModel):
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

class CreateFlowRequestRequestTypeDef(BaseValidatorModel):
    executionRoleArn: str
    name: str
    clientToken: Optional[str] = None
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionTypeDef] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateFlowRequestRequestTypeDef(BaseValidatorModel):
    executionRoleArn: str
    flowIdentifier: str
    name: str
    customerEncryptionKeyArn: Optional[str] = None
    definition: Optional[FlowDefinitionTypeDef] = None
    description: Optional[str] = None


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
from aws_resource_validator.pydantic_models.bedrock_agent_runtime_constants import *

class S3IdentifierTypeDef(BaseValidatorModel):
    s3BucketName: Optional[str] = None
    s3ObjectKey: Optional[str] = None


class AccessDeniedExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class ActionGroupInvocationOutputTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class AnalyzePromptEventTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class BadGatewayExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    resourceName: Optional[str] = None


class PerformanceConfigurationTypeDef(BaseValidatorModel):
    latency: Optional[PerformanceConfigLatencyType] = None


class BedrockRerankingModelConfigurationTypeDef(BaseValidatorModel):
    modelArn: str
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None


class CallerTypeDef(BaseValidatorModel):
    agentAliasArn: Optional[str] = None


class CodeInterpreterInvocationInputTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    files: Optional[List[str]] = None


class CodeInterpreterInvocationOutputTypeDef(BaseValidatorModel):
    executionError: Optional[str] = None
    executionOutput: Optional[str] = None
    executionTimeout: Optional[bool] = None
    files: Optional[List[str]] = None


class CollaboratorConfigurationTypeDef(BaseValidatorModel):
    collaboratorInstruction: str
    collaboratorName: str
    agentAliasArn: Optional[str] = None
    relayConversationHistory: Optional[RelayConversationHistoryType] = None


class GuardrailConfigurationWithArnTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str


class ConflictExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class ContentBlockTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class CreateInvocationRequestTypeDef(BaseValidatorModel):
    sessionIdentifier: str
    description: Optional[str] = None
    invocationId: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateSessionRequestTypeDef(BaseValidatorModel):
    encryptionKeyArn: Optional[str] = None
    sessionMetadata: Optional[Mapping[str, str]] = None
    tags: Optional[Mapping[str, str]] = None


class CustomOrchestrationTraceEventTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class DeleteAgentMemoryRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: Optional[str] = None
    sessionId: Optional[str] = None


class DeleteSessionRequestTypeDef(BaseValidatorModel):
    sessionIdentifier: str


class DependencyFailedExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    resourceName: Optional[str] = None


class EndSessionRequestTypeDef(BaseValidatorModel):
    sessionIdentifier: str


class S3ObjectDocTypeDef(BaseValidatorModel):
    uri: str


class GuardrailConfigurationTypeDef(BaseValidatorModel):
    guardrailId: str
    guardrailVersion: str


class PromptTemplateTypeDef(BaseValidatorModel):
    textPromptTemplate: Optional[str] = None


class FailureTraceTypeDef(BaseValidatorModel):
    failureReason: Optional[str] = None
    traceId: Optional[str] = None


class FieldForRerankingTypeDef(BaseValidatorModel):
    fieldName: str


class S3ObjectFileTypeDef(BaseValidatorModel):
    uri: str


class FilterAttributeTypeDef(BaseValidatorModel):
    key: str
    value: Mapping[str, Any]


class FinalResponseTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class FlowCompletionEventTypeDef(BaseValidatorModel):
    completionReason: FlowCompletionReasonType


class FlowInputContentTypeDef(BaseValidatorModel):
    document: Optional[Mapping[str, Any]] = None


class FlowMultiTurnInputContentTypeDef(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None


class FlowOutputContentTypeDef(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None


class InternalServerExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    reason: Optional[str] = None


class ResourceNotFoundExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class ServiceQuotaExceededExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class ThrottlingExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class ValidationExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class FlowTraceConditionTypeDef(BaseValidatorModel):
    conditionName: str


class FlowTraceNodeInputContentTypeDef(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None


class FlowTraceNodeOutputContentTypeDef(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetAgentMemoryRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal["SESSION_SUMMARY"]
    maxItems: Optional[int] = None
    nextToken: Optional[str] = None


class GetInvocationStepRequestTypeDef(BaseValidatorModel):
    invocationIdentifier: str
    invocationStepId: str
    sessionIdentifier: str


class GetSessionRequestTypeDef(BaseValidatorModel):
    sessionIdentifier: str


class GuardrailCustomWordTypeDef(BaseValidatorModel):
    action: Optional[Literal["BLOCKED"]] = None
    match: Optional[str] = None


class GuardrailEventTypeDef(BaseValidatorModel):
    action: Optional[GuadrailActionType] = None


class GuardrailRegexFilterTypeDef(BaseValidatorModel):
    action: Optional[GuardrailSensitiveInformationPolicyActionType] = None
    match: Optional[str] = None
    name: Optional[str] = None
    regex: Optional[str] = None


class S3LocationTypeDef(BaseValidatorModel):
    uri: str


class TextInferenceConfigTypeDef(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None


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


class TextPromptTypeDef(BaseValidatorModel):
    text: str


class KnowledgeBaseLookupInputTypeDef(BaseValidatorModel):
    knowledgeBaseId: Optional[str] = None
    text: Optional[str] = None


class InvocationStepSummaryTypeDef(BaseValidatorModel):
    invocationId: str
    invocationStepId: str
    invocationStepTime: datetime
    sessionId: str


class InvocationSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    invocationId: str
    sessionId: str


class StreamingConfigurationsTypeDef(BaseValidatorModel):
    applyGuardrailInterval: Optional[int] = None
    streamFinalResponse: Optional[bool] = None


class KnowledgeBaseQueryTypeDef(BaseValidatorModel):
    text: str


class ListInvocationStepsRequestTypeDef(BaseValidatorModel):
    sessionIdentifier: str
    invocationIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListInvocationsRequestTypeDef(BaseValidatorModel):
    sessionIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSessionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SessionSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    sessionArn: str
    sessionId: str
    sessionStatus: SessionStatusType


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class MemorySessionSummaryTypeDef(BaseValidatorModel):
    memoryId: Optional[str] = None
    sessionExpiryTime: Optional[datetime] = None
    sessionId: Optional[str] = None
    sessionStartTime: Optional[datetime] = None
    summaryText: Optional[str] = None


class UsageTypeDef(BaseValidatorModel):
    inputTokens: Optional[int] = None
    outputTokens: Optional[int] = None


class ModelNotReadyExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class RepromptResponseTypeDef(BaseValidatorModel):
    source: Optional[SourceType] = None
    text: Optional[str] = None


class RawResponseTypeDef(BaseValidatorModel):
    content: Optional[str] = None


class RationaleTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    traceId: Optional[str] = None


class PostProcessingParsedResponseTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class PreProcessingParsedResponseTypeDef(BaseValidatorModel):
    isValid: Optional[bool] = None
    rationale: Optional[str] = None


class ReasoningTextBlockTypeDef(BaseValidatorModel):
    text: str
    signature: Optional[str] = None


class RerankTextDocumentTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class RetrievalResultConfluenceLocationTypeDef(BaseValidatorModel):
    url: Optional[str] = None


class RetrievalResultKendraDocumentLocationTypeDef(BaseValidatorModel):
    uri: Optional[str] = None


class RetrievalResultS3LocationTypeDef(BaseValidatorModel):
    uri: Optional[str] = None


class RetrievalResultSalesforceLocationTypeDef(BaseValidatorModel):
    url: Optional[str] = None


class RetrievalResultSharePointLocationTypeDef(BaseValidatorModel):
    url: Optional[str] = None


class RetrievalResultSqlLocationTypeDef(BaseValidatorModel):
    query: Optional[str] = None


class RetrievalResultWebLocationTypeDef(BaseValidatorModel):
    url: Optional[str] = None


class RetrieveAndGenerateInputTypeDef(BaseValidatorModel):
    text: str


class RetrieveAndGenerateOutputEventTypeDef(BaseValidatorModel):
    text: str


class RetrieveAndGenerateOutputTypeDef(BaseValidatorModel):
    text: str


class RetrieveAndGenerateSessionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyArn: str


class SpanTypeDef(BaseValidatorModel):
    end: Optional[int] = None
    start: Optional[int] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TextToSqlKnowledgeBaseConfigurationTypeDef(BaseValidatorModel):
    knowledgeBaseArn: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateSessionRequestTypeDef(BaseValidatorModel):
    sessionIdentifier: str
    sessionMetadata: Optional[Mapping[str, str]] = None


class VectorSearchBedrockRerankingModelConfigurationTypeDef(BaseValidatorModel):
    modelArn: str
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None


class APISchemaTypeDef(BaseValidatorModel):
    payload: Optional[str] = None
    s3: Optional[S3IdentifierTypeDef] = None


class ParameterTypeDef(BaseValidatorModel):
    pass


class PropertyParametersTypeDef(BaseValidatorModel):
    properties: Optional[List[ParameterTypeDef]] = None


class RequestBodyTypeDef(BaseValidatorModel):
    content: Optional[Dict[str, List[ParameterTypeDef]]] = None


class BedrockModelConfigurationsTypeDef(BaseValidatorModel):
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None


class InlineBedrockModelConfigurationsTypeDef(BaseValidatorModel):
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None


class ModelPerformanceConfigurationTypeDef(BaseValidatorModel):
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None


class BedrockRerankingConfigurationTypeDef(BaseValidatorModel):
    modelConfiguration: BedrockRerankingModelConfigurationTypeDef
    numberOfResults: Optional[int] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class ByteContentDocTypeDef(BaseValidatorModel):
    contentType: str
    data: BlobTypeDef
    identifier: str


class ByteContentFileTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    mediaType: str


class MessageTypeDef(BaseValidatorModel):
    content: Sequence[ContentBlockTypeDef]
    role: ConversationRoleType


class CreateInvocationResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    invocationId: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSessionResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    sessionArn: str
    sessionId: str
    sessionStatus: SessionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EndSessionResponseTypeDef(BaseValidatorModel):
    sessionArn: str
    sessionId: str
    sessionStatus: SessionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetSessionResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    encryptionKeyArn: str
    lastUpdatedAt: datetime
    sessionArn: str
    sessionId: str
    sessionMetadata: Dict[str, str]
    sessionStatus: SessionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutInvocationStepResponseTypeDef(BaseValidatorModel):
    invocationStepId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSessionResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    sessionArn: str
    sessionId: str
    sessionStatus: SessionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CustomOrchestrationTraceTypeDef(BaseValidatorModel):
    event: Optional[CustomOrchestrationTraceEventTypeDef] = None
    traceId: Optional[str] = None


class RerankingMetadataSelectiveModeConfigurationTypeDef(BaseValidatorModel):
    fieldsToExclude: Optional[Sequence[FieldForRerankingTypeDef]] = None
    fieldsToInclude: Optional[Sequence[FieldForRerankingTypeDef]] = None


class OutputFileTypeDef(BaseValidatorModel):
    pass


class FilePartTypeDef(BaseValidatorModel):
    files: Optional[List[OutputFileTypeDef]] = None


class InlineAgentFilePartTypeDef(BaseValidatorModel):
    files: Optional[List[OutputFileTypeDef]] = None


class FlowInputTypeDef(BaseValidatorModel):
    content: FlowInputContentTypeDef
    nodeName: str
    nodeInputName: Optional[str] = None
    nodeOutputName: Optional[str] = None


class FlowMultiTurnInputRequestEventTypeDef(BaseValidatorModel):
    content: FlowMultiTurnInputContentTypeDef
    nodeName: str
    nodeType: NodeTypeType


class FlowOutputEventTypeDef(BaseValidatorModel):
    content: FlowOutputContentTypeDef
    nodeName: str
    nodeType: NodeTypeType


class FlowTraceConditionNodeResultEventTypeDef(BaseValidatorModel):
    nodeName: str
    satisfiedConditions: List[FlowTraceConditionTypeDef]
    timestamp: datetime


class FlowTraceNodeInputFieldTypeDef(BaseValidatorModel):
    content: FlowTraceNodeInputContentTypeDef
    nodeInputName: str


class FlowTraceNodeOutputFieldTypeDef(BaseValidatorModel):
    content: FlowTraceNodeOutputContentTypeDef
    nodeOutputName: str


class ParameterDetailTypeDef(BaseValidatorModel):
    pass


class FunctionDefinitionTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Mapping[str, ParameterDetailTypeDef]] = None
    requireConfirmation: Optional[RequireConfirmationType] = None


class FunctionParameterTypeDef(BaseValidatorModel):
    pass


class FunctionInvocationInputTypeDef(BaseValidatorModel):
    actionGroup: str
    actionInvocationType: Optional[ActionInvocationTypeType] = None
    agentId: Optional[str] = None
    collaboratorName: Optional[str] = None
    function: Optional[str] = None
    parameters: Optional[List[FunctionParameterTypeDef]] = None


class GeneratedQueryTypeDef(BaseValidatorModel):
    pass


class GenerateQueryResponseTypeDef(BaseValidatorModel):
    queries: List[GeneratedQueryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetAgentMemoryRequestPaginateTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal["SESSION_SUMMARY"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInvocationStepsRequestPaginateTypeDef(BaseValidatorModel):
    sessionIdentifier: str
    invocationIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInvocationsRequestPaginateTypeDef(BaseValidatorModel):
    sessionIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSessionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GuardrailContentFilterTypeDef(BaseValidatorModel):
    pass


class GuardrailContentPolicyAssessmentTypeDef(BaseValidatorModel):
    filters: Optional[List[GuardrailContentFilterTypeDef]] = None


class GuardrailManagedWordTypeDef(BaseValidatorModel):
    pass


class GuardrailWordPolicyAssessmentTypeDef(BaseValidatorModel):
    customWords: Optional[List[GuardrailCustomWordTypeDef]] = None
    managedWordLists: Optional[List[GuardrailManagedWordTypeDef]] = None


class GuardrailPiiEntityFilterTypeDef(BaseValidatorModel):
    pass


class GuardrailSensitiveInformationPolicyAssessmentTypeDef(BaseValidatorModel):
    piiEntities: Optional[List[GuardrailPiiEntityFilterTypeDef]] = None
    regexes: Optional[List[GuardrailRegexFilterTypeDef]] = None


class GuardrailTopicTypeDef(BaseValidatorModel):
    pass


class GuardrailTopicPolicyAssessmentTypeDef(BaseValidatorModel):
    topics: Optional[List[GuardrailTopicTypeDef]] = None


class MetadataAttributeSchemaTypeDef(BaseValidatorModel):
    pass


class ImplicitFilterConfigurationTypeDef(BaseValidatorModel):
    metadataAttributes: Sequence[MetadataAttributeSchemaTypeDef]
    modelArn: str


class InferenceConfigTypeDef(BaseValidatorModel):
    textInferenceConfig: Optional[TextInferenceConfigTypeDef] = None


class InputPromptTypeDef(BaseValidatorModel):
    textPrompt: Optional[TextPromptTypeDef] = None


class OptimizedPromptTypeDef(BaseValidatorModel):
    textPrompt: Optional[TextPromptTypeDef] = None


class ListInvocationStepsResponseTypeDef(BaseValidatorModel):
    invocationStepSummaries: List[InvocationStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListInvocationsResponseTypeDef(BaseValidatorModel):
    invocationSummaries: List[InvocationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSessionsResponseTypeDef(BaseValidatorModel):
    sessionSummaries: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MemoryTypeDef(BaseValidatorModel):
    sessionSummary: Optional[MemorySessionSummaryTypeDef] = None


class MetadataTypeDef(BaseValidatorModel):
    usage: Optional[UsageTypeDef] = None


class ReasoningContentBlockTypeDef(BaseValidatorModel):
    reasoningText: Optional[ReasoningTextBlockTypeDef] = None
    redactedContent: Optional[bytes] = None


class TextResponsePartTypeDef(BaseValidatorModel):
    span: Optional[SpanTypeDef] = None
    text: Optional[str] = None


class ApiRequestBodyTypeDef(BaseValidatorModel):
    content: Optional[Dict[str, PropertyParametersTypeDef]] = None


class ActionGroupInvocationInputTypeDef(BaseValidatorModel):
    actionGroupName: Optional[str] = None
    apiPath: Optional[str] = None
    executionType: Optional[ExecutionTypeType] = None
    function: Optional[str] = None
    invocationId: Optional[str] = None
    parameters: Optional[List[ParameterTypeDef]] = None
    requestBody: Optional[RequestBodyTypeDef] = None
    verb: Optional[str] = None


class ExternalSourceTypeDef(BaseValidatorModel):
    sourceType: ExternalSourceTypeType
    byteContent: Optional[ByteContentDocTypeDef] = None
    s3Location: Optional[S3ObjectDocTypeDef] = None


class FileSourceTypeDef(BaseValidatorModel):
    sourceType: FileSourceTypeType
    byteContent: Optional[ByteContentFileTypeDef] = None
    s3Location: Optional[S3ObjectFileTypeDef] = None


class ConversationHistoryTypeDef(BaseValidatorModel):
    messages: Optional[Sequence[MessageTypeDef]] = None


class MetadataConfigurationForRerankingTypeDef(BaseValidatorModel):
    selectionMode: RerankingMetadataSelectionModeType
    selectiveModeConfiguration: Optional[RerankingMetadataSelectiveModeConfigurationTypeDef] = None


class InvokeFlowRequestTypeDef(BaseValidatorModel):
    flowAliasIdentifier: str
    flowIdentifier: str
    inputs: Sequence[FlowInputTypeDef]
    enableTrace: Optional[bool] = None
    executionId: Optional[str] = None
    modelPerformanceConfiguration: Optional[ModelPerformanceConfigurationTypeDef] = None


class FlowTraceNodeInputEventTypeDef(BaseValidatorModel):
    fields: List[FlowTraceNodeInputFieldTypeDef]
    nodeName: str
    timestamp: datetime


class FlowTraceNodeOutputEventTypeDef(BaseValidatorModel):
    fields: List[FlowTraceNodeOutputFieldTypeDef]
    nodeName: str
    timestamp: datetime


class FunctionSchemaTypeDef(BaseValidatorModel):
    functions: Optional[Sequence[FunctionDefinitionTypeDef]] = None


class GuardrailAssessmentTypeDef(BaseValidatorModel):
    contentPolicy: Optional[GuardrailContentPolicyAssessmentTypeDef] = None
    sensitiveInformationPolicy: Optional[GuardrailSensitiveInformationPolicyAssessmentTypeDef] = None
    topicPolicy: Optional[GuardrailTopicPolicyAssessmentTypeDef] = None
    wordPolicy: Optional[GuardrailWordPolicyAssessmentTypeDef] = None


class ImageInputOutputTypeDef(BaseValidatorModel):
    pass


class ContentBodyOutputTypeDef(BaseValidatorModel):
    body: Optional[str] = None
    images: Optional[List[ImageInputOutputTypeDef]] = None


class ExternalSourcesGenerationConfigurationTypeDef(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    inferenceConfig: Optional[InferenceConfigTypeDef] = None
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None
    promptTemplate: Optional[PromptTemplateTypeDef] = None


class GenerationConfigurationTypeDef(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    inferenceConfig: Optional[InferenceConfigTypeDef] = None
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None
    promptTemplate: Optional[PromptTemplateTypeDef] = None


class QueryTransformationConfigurationTypeDef(BaseValidatorModel):
    pass


class OrchestrationConfigurationTypeDef(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    inferenceConfig: Optional[InferenceConfigTypeDef] = None
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None
    promptTemplate: Optional[PromptTemplateTypeDef] = None
    queryTransformationConfiguration: Optional[QueryTransformationConfigurationTypeDef] = None


class InferenceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PromptConfigurationTypeDef(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    basePromptTemplate: Optional[str] = None
    foundationModel: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationUnionTypeDef] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None


class OptimizedPromptEventTypeDef(BaseValidatorModel):
    optimizedPrompt: Optional[OptimizedPromptTypeDef] = None


class GetAgentMemoryResponseTypeDef(BaseValidatorModel):
    memoryContents: List[MemoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RoutingClassifierModelInvocationOutputTypeDef(BaseValidatorModel):
    metadata: Optional[MetadataTypeDef] = None
    rawResponse: Optional[RawResponseTypeDef] = None
    traceId: Optional[str] = None


class OrchestrationModelInvocationOutputTypeDef(BaseValidatorModel):
    metadata: Optional[MetadataTypeDef] = None
    rawResponse: Optional[RawResponseTypeDef] = None
    reasoningContent: Optional[ReasoningContentBlockTypeDef] = None
    traceId: Optional[str] = None


class PostProcessingModelInvocationOutputTypeDef(BaseValidatorModel):
    metadata: Optional[MetadataTypeDef] = None
    parsedResponse: Optional[PostProcessingParsedResponseTypeDef] = None
    rawResponse: Optional[RawResponseTypeDef] = None
    reasoningContent: Optional[ReasoningContentBlockTypeDef] = None
    traceId: Optional[str] = None


class PreProcessingModelInvocationOutputTypeDef(BaseValidatorModel):
    metadata: Optional[MetadataTypeDef] = None
    parsedResponse: Optional[PreProcessingParsedResponseTypeDef] = None
    rawResponse: Optional[RawResponseTypeDef] = None
    reasoningContent: Optional[ReasoningContentBlockTypeDef] = None
    traceId: Optional[str] = None


class RerankDocumentOutputTypeDef(BaseValidatorModel):
    pass


class RerankResultTypeDef(BaseValidatorModel):
    index: int
    relevanceScore: float
    document: Optional[RerankDocumentOutputTypeDef] = None


class RetrievalResultContentTypeDef(BaseValidatorModel):
    pass


class RetrievalResultLocationTypeDef(BaseValidatorModel):
    pass


class KnowledgeBaseRetrievalResultTypeDef(BaseValidatorModel):
    content: RetrievalResultContentTypeDef
    location: Optional[RetrievalResultLocationTypeDef] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    score: Optional[float] = None


class RetrievedReferenceTypeDef(BaseValidatorModel):
    content: Optional[RetrievalResultContentTypeDef] = None
    location: Optional[RetrievalResultLocationTypeDef] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None


class GeneratedResponsePartTypeDef(BaseValidatorModel):
    textResponsePart: Optional[TextResponsePartTypeDef] = None


class TextToSqlConfigurationTypeDef(BaseValidatorModel):
    pass


class TransformationConfigurationTypeDef(BaseValidatorModel):
    mode: Literal["TEXT_TO_SQL"]
    textToSqlConfiguration: Optional[TextToSqlConfigurationTypeDef] = None


class ApiParameterTypeDef(BaseValidatorModel):
    pass


class ApiInvocationInputTypeDef(BaseValidatorModel):
    actionGroup: str
    actionInvocationType: Optional[ActionInvocationTypeType] = None
    agentId: Optional[str] = None
    apiPath: Optional[str] = None
    collaboratorName: Optional[str] = None
    httpMethod: Optional[str] = None
    parameters: Optional[List[ApiParameterTypeDef]] = None
    requestBody: Optional[ApiRequestBodyTypeDef] = None


class InputFileTypeDef(BaseValidatorModel):
    name: str
    source: FileSourceTypeDef
    useCase: FileUseCaseType


class VectorSearchBedrockRerankingConfigurationTypeDef(BaseValidatorModel):
    modelConfiguration: VectorSearchBedrockRerankingModelConfigurationTypeDef
    metadataConfiguration: Optional[MetadataConfigurationForRerankingTypeDef] = None
    numberOfRerankedResults: Optional[int] = None


class FlowTraceTypeDef(BaseValidatorModel):
    conditionNodeResultTrace: Optional[FlowTraceConditionNodeResultEventTypeDef] = None
    nodeInputTrace: Optional[FlowTraceNodeInputEventTypeDef] = None
    nodeOutputTrace: Optional[FlowTraceNodeOutputEventTypeDef] = None


class ActionGroupExecutorTypeDef(BaseValidatorModel):
    pass


class AgentActionGroupTypeDef(BaseValidatorModel):
    actionGroupName: str
    actionGroupExecutor: Optional[ActionGroupExecutorTypeDef] = None
    apiSchema: Optional[APISchemaTypeDef] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchemaTypeDef] = None
    parentActionGroupSignature: Optional[ActionGroupSignatureType] = None
    parentActionGroupSignatureParams: Optional[Mapping[str, str]] = None


class GuardrailTraceTypeDef(BaseValidatorModel):
    action: Optional[GuardrailActionType] = None
    inputAssessments: Optional[List[GuardrailAssessmentTypeDef]] = None
    outputAssessments: Optional[List[GuardrailAssessmentTypeDef]] = None
    traceId: Optional[str] = None


class ApiResultOutputTypeDef(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    apiPath: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    httpMethod: Optional[str] = None
    httpStatusCode: Optional[int] = None
    responseBody: Optional[Dict[str, ContentBodyOutputTypeDef]] = None
    responseState: Optional[ResponseStateType] = None


class FunctionResultOutputTypeDef(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    function: Optional[str] = None
    responseBody: Optional[Dict[str, ContentBodyOutputTypeDef]] = None
    responseState: Optional[ResponseStateType] = None


class ImageBlockOutputTypeDef(BaseValidatorModel):
    pass


class BedrockSessionContentBlockOutputTypeDef(BaseValidatorModel):
    image: Optional[ImageBlockOutputTypeDef] = None
    text: Optional[str] = None


class ImageBlockTypeDef(BaseValidatorModel):
    pass


class BedrockSessionContentBlockTypeDef(BaseValidatorModel):
    image: Optional[ImageBlockTypeDef] = None
    text: Optional[str] = None


class ExternalSourcesRetrieveAndGenerateConfigurationTypeDef(BaseValidatorModel):
    modelArn: str
    sources: Sequence[ExternalSourceTypeDef]
    generationConfiguration: Optional[ExternalSourcesGenerationConfigurationTypeDef] = None


class PromptOverrideConfigurationTypeDef(BaseValidatorModel):
    promptConfigurations: Sequence[PromptConfigurationTypeDef]
    overrideLambda: Optional[str] = None


class OptimizedPromptStreamTypeDef(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedExceptionTypeDef] = None
    analyzePromptEvent: Optional[AnalyzePromptEventTypeDef] = None
    badGatewayException: Optional[BadGatewayExceptionTypeDef] = None
    dependencyFailedException: Optional[DependencyFailedExceptionTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    optimizedPromptEvent: Optional[OptimizedPromptEventTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None


class ModelInvocationInputTypeDef(BaseValidatorModel):
    pass


class PostProcessingTraceTypeDef(BaseValidatorModel):
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    modelInvocationOutput: Optional[PostProcessingModelInvocationOutputTypeDef] = None


class PreProcessingTraceTypeDef(BaseValidatorModel):
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    modelInvocationOutput: Optional[PreProcessingModelInvocationOutputTypeDef] = None


class RerankResponseTypeDef(BaseValidatorModel):
    results: List[RerankResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RetrieveResponseTypeDef(BaseValidatorModel):
    guardrailAction: GuadrailActionType
    retrievalResults: List[KnowledgeBaseRetrievalResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class KnowledgeBaseLookupOutputTypeDef(BaseValidatorModel):
    retrievedReferences: Optional[List[RetrievedReferenceTypeDef]] = None


class CitationTypeDef(BaseValidatorModel):
    generatedResponsePart: Optional[GeneratedResponsePartTypeDef] = None
    retrievedReferences: Optional[List[RetrievedReferenceTypeDef]] = None


class QueryGenerationInputTypeDef(BaseValidatorModel):
    pass


class GenerateQueryRequestTypeDef(BaseValidatorModel):
    queryGenerationInput: QueryGenerationInputTypeDef
    transformationConfiguration: TransformationConfigurationTypeDef


class InvocationInputMemberTypeDef(BaseValidatorModel):
    apiInvocationInput: Optional[ApiInvocationInputTypeDef] = None
    functionInvocationInput: Optional[FunctionInvocationInputTypeDef] = None


class FlowTraceEventTypeDef(BaseValidatorModel):
    trace: FlowTraceTypeDef


class InvocationResultMemberOutputTypeDef(BaseValidatorModel):
    apiResult: Optional[ApiResultOutputTypeDef] = None
    functionResult: Optional[FunctionResultOutputTypeDef] = None


class InvocationStepPayloadOutputTypeDef(BaseValidatorModel):
    contentBlocks: Optional[List[BedrockSessionContentBlockOutputTypeDef]] = None


class InvocationStepPayloadTypeDef(BaseValidatorModel):
    contentBlocks: Optional[Sequence[BedrockSessionContentBlockTypeDef]] = None


class OptimizePromptResponseTypeDef(BaseValidatorModel):
    optimizedPrompt: EventStream[OptimizedPromptStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RerankSourceTypeDef(BaseValidatorModel):
    pass


class RerankQueryTypeDef(BaseValidatorModel):
    pass


class RerankingConfigurationTypeDef(BaseValidatorModel):
    pass


class RerankRequestPaginateTypeDef(BaseValidatorModel):
    queries: Sequence[RerankQueryTypeDef]
    rerankingConfiguration: RerankingConfigurationTypeDef
    sources: Sequence[RerankSourceTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class RerankRequestTypeDef(BaseValidatorModel):
    queries: Sequence[RerankQueryTypeDef]
    rerankingConfiguration: RerankingConfigurationTypeDef
    sources: Sequence[RerankSourceTypeDef]
    nextToken: Optional[str] = None


class AttributionTypeDef(BaseValidatorModel):
    citations: Optional[List[CitationTypeDef]] = None


class CitationEventTypeDef(BaseValidatorModel):
    citation: Optional[CitationTypeDef] = None
    generatedResponsePart: Optional[GeneratedResponsePartTypeDef] = None
    retrievedReferences: Optional[List[RetrievedReferenceTypeDef]] = None


class RetrieveAndGenerateResponseTypeDef(BaseValidatorModel):
    citations: List[CitationTypeDef]
    guardrailAction: GuadrailActionType
    output: RetrieveAndGenerateOutputTypeDef
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class InlineAgentReturnControlPayloadTypeDef(BaseValidatorModel):
    invocationId: Optional[str] = None
    invocationInputs: Optional[List[InvocationInputMemberTypeDef]] = None


class ReturnControlPayloadTypeDef(BaseValidatorModel):
    invocationId: Optional[str] = None
    invocationInputs: Optional[List[InvocationInputMemberTypeDef]] = None


class ImageInputUnionTypeDef(BaseValidatorModel):
    pass


class ContentBodyTypeDef(BaseValidatorModel):
    body: Optional[str] = None
    images: Optional[Sequence[ImageInputUnionTypeDef]] = None


class FlowResponseStreamTypeDef(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedExceptionTypeDef] = None
    badGatewayException: Optional[BadGatewayExceptionTypeDef] = None
    conflictException: Optional[ConflictExceptionTypeDef] = None
    dependencyFailedException: Optional[DependencyFailedExceptionTypeDef] = None
    flowCompletionEvent: Optional[FlowCompletionEventTypeDef] = None
    flowMultiTurnInputRequestEvent: Optional[FlowMultiTurnInputRequestEventTypeDef] = None
    flowOutputEvent: Optional[FlowOutputEventTypeDef] = None
    flowTraceEvent: Optional[FlowTraceEventTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    resourceNotFoundException: Optional[ResourceNotFoundExceptionTypeDef] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None


class ReturnControlResultsTypeDef(BaseValidatorModel):
    invocationId: Optional[str] = None
    returnControlInvocationResults: Optional[List[InvocationResultMemberOutputTypeDef]] = None


class InvocationStepTypeDef(BaseValidatorModel):
    invocationId: str
    invocationStepId: str
    invocationStepTime: datetime
    payload: InvocationStepPayloadOutputTypeDef
    sessionId: str


class RetrieveAndGenerateStreamResponseOutputTypeDef(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedExceptionTypeDef] = None
    badGatewayException: Optional[BadGatewayExceptionTypeDef] = None
    citation: Optional[CitationEventTypeDef] = None
    conflictException: Optional[ConflictExceptionTypeDef] = None
    dependencyFailedException: Optional[DependencyFailedExceptionTypeDef] = None
    guardrail: Optional[GuardrailEventTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    output: Optional[RetrieveAndGenerateOutputEventTypeDef] = None
    resourceNotFoundException: Optional[ResourceNotFoundExceptionTypeDef] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None


class KnowledgeBaseVectorSearchConfigurationPaginatorTypeDef(BaseValidatorModel):
    pass


class KnowledgeBaseRetrievalConfigurationPaginatorTypeDef(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfigurationPaginatorTypeDef


class KnowledgeBaseVectorSearchConfigurationTypeDef(BaseValidatorModel):
    pass


class KnowledgeBaseRetrievalConfigurationTypeDef(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfigurationTypeDef


class InvokeFlowResponseTypeDef(BaseValidatorModel):
    executionId: str
    responseStream: EventStream[FlowResponseStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetInvocationStepResponseTypeDef(BaseValidatorModel):
    invocationStep: InvocationStepTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InvocationStepPayloadUnionTypeDef(BaseValidatorModel):
    pass


class TimestampTypeDef(BaseValidatorModel):
    pass


class PutInvocationStepRequestTypeDef(BaseValidatorModel):
    invocationIdentifier: str
    invocationStepTime: TimestampTypeDef
    payload: InvocationStepPayloadUnionTypeDef
    sessionIdentifier: str
    invocationStepId: Optional[str] = None


class RetrieveAndGenerateStreamResponseTypeDef(BaseValidatorModel):
    sessionId: str
    stream: EventStream[RetrieveAndGenerateStreamResponseOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AgentCollaboratorOutputPayloadTypeDef(BaseValidatorModel):
    pass


class AgentCollaboratorInvocationOutputTypeDef(BaseValidatorModel):
    agentCollaboratorAliasArn: Optional[str] = None
    agentCollaboratorName: Optional[str] = None
    output: Optional[AgentCollaboratorOutputPayloadTypeDef] = None


class ContentBodyUnionTypeDef(BaseValidatorModel):
    pass


class ApiResultTypeDef(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    apiPath: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    httpMethod: Optional[str] = None
    httpStatusCode: Optional[int] = None
    responseBody: Optional[Mapping[str, ContentBodyUnionTypeDef]] = None
    responseState: Optional[ResponseStateType] = None


class FunctionResultTypeDef(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    function: Optional[str] = None
    responseBody: Optional[Mapping[str, ContentBodyUnionTypeDef]] = None
    responseState: Optional[ResponseStateType] = None


class RetrieveRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    retrievalQuery: KnowledgeBaseQueryTypeDef
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class KnowledgeBaseConfigurationTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    retrievalConfiguration: KnowledgeBaseRetrievalConfigurationTypeDef


class KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    modelArn: str
    generationConfiguration: Optional[GenerationConfigurationTypeDef] = None
    orchestrationConfiguration: Optional[OrchestrationConfigurationTypeDef] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None


class KnowledgeBaseTypeDef(BaseValidatorModel):
    description: str
    knowledgeBaseId: str
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None


class RetrieveRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    retrievalQuery: KnowledgeBaseQueryTypeDef
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    nextToken: Optional[str] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None


class CollaboratorTypeDef(BaseValidatorModel):
    foundationModel: str
    instruction: str
    actionGroups: Optional[Sequence[AgentActionGroupTypeDef]] = None
    agentCollaboration: Optional[AgentCollaborationType] = None
    agentName: Optional[str] = None
    collaboratorConfigurations: Optional[Sequence[CollaboratorConfigurationTypeDef]] = None
    customerEncryptionKeyArn: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationWithArnTypeDef] = None
    idleSessionTTLInSeconds: Optional[int] = None
    knowledgeBases: Optional[Sequence[KnowledgeBaseTypeDef]] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationTypeDef] = None


class AgentCollaboratorInvocationInputTypeDef(BaseValidatorModel):
    pass


class InvocationInputTypeDef(BaseValidatorModel):
    actionGroupInvocationInput: Optional[ActionGroupInvocationInputTypeDef] = None
    agentCollaboratorInvocationInput: Optional[AgentCollaboratorInvocationInputTypeDef] = None
    codeInterpreterInvocationInput: Optional[CodeInterpreterInvocationInputTypeDef] = None
    invocationType: Optional[InvocationTypeType] = None
    knowledgeBaseLookupInput: Optional[KnowledgeBaseLookupInputTypeDef] = None
    traceId: Optional[str] = None


class ApiResultUnionTypeDef(BaseValidatorModel):
    pass


class FunctionResultUnionTypeDef(BaseValidatorModel):
    pass


class InvocationResultMemberTypeDef(BaseValidatorModel):
    apiResult: Optional[ApiResultUnionTypeDef] = None
    functionResult: Optional[FunctionResultUnionTypeDef] = None


class ObservationTypeDef(BaseValidatorModel):
    pass


class OrchestrationTraceTypeDef(BaseValidatorModel):
    invocationInput: Optional[InvocationInputTypeDef] = None
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    modelInvocationOutput: Optional[OrchestrationModelInvocationOutputTypeDef] = None
    observation: Optional[ObservationTypeDef] = None
    rationale: Optional[RationaleTypeDef] = None


class RoutingClassifierTraceTypeDef(BaseValidatorModel):
    invocationInput: Optional[InvocationInputTypeDef] = None
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    modelInvocationOutput: Optional[RoutingClassifierModelInvocationOutputTypeDef] = None
    observation: Optional[ObservationTypeDef] = None


class TraceTypeDef(BaseValidatorModel):
    customOrchestrationTrace: Optional[CustomOrchestrationTraceTypeDef] = None
    failureTrace: Optional[FailureTraceTypeDef] = None
    guardrailTrace: Optional[GuardrailTraceTypeDef] = None
    orchestrationTrace: Optional[OrchestrationTraceTypeDef] = None
    postProcessingTrace: Optional[PostProcessingTraceTypeDef] = None
    preProcessingTrace: Optional[PreProcessingTraceTypeDef] = None
    routingClassifierTrace: Optional[RoutingClassifierTraceTypeDef] = None


class InvocationResultMemberUnionTypeDef(BaseValidatorModel):
    pass


class InlineSessionStateTypeDef(BaseValidatorModel):
    conversationHistory: Optional[ConversationHistoryTypeDef] = None
    files: Optional[Sequence[InputFileTypeDef]] = None
    invocationId: Optional[str] = None
    promptSessionAttributes: Optional[Mapping[str, str]] = None
    returnControlInvocationResults: Optional[Sequence[InvocationResultMemberUnionTypeDef]] = None
    sessionAttributes: Optional[Mapping[str, str]] = None


class SessionStateTypeDef(BaseValidatorModel):
    conversationHistory: Optional[ConversationHistoryTypeDef] = None
    files: Optional[Sequence[InputFileTypeDef]] = None
    invocationId: Optional[str] = None
    knowledgeBaseConfigurations: Optional[Sequence[KnowledgeBaseConfigurationTypeDef]] = None
    promptSessionAttributes: Optional[Mapping[str, str]] = None
    returnControlInvocationResults: Optional[Sequence[InvocationResultMemberUnionTypeDef]] = None
    sessionAttributes: Optional[Mapping[str, str]] = None


class InlineAgentTracePartTypeDef(BaseValidatorModel):
    sessionId: Optional[str] = None
    trace: Optional[TraceTypeDef] = None


class TracePartTypeDef(BaseValidatorModel):
    agentAliasId: Optional[str] = None
    agentId: Optional[str] = None
    agentVersion: Optional[str] = None
    callerChain: Optional[List[CallerTypeDef]] = None
    collaboratorName: Optional[str] = None
    eventTime: Optional[datetime] = None
    sessionId: Optional[str] = None
    trace: Optional[TraceTypeDef] = None


class InvokeInlineAgentRequestTypeDef(BaseValidatorModel):
    foundationModel: str
    instruction: str
    sessionId: str
    actionGroups: Optional[Sequence[AgentActionGroupTypeDef]] = None
    agentCollaboration: Optional[AgentCollaborationType] = None
    bedrockModelConfigurations: Optional[InlineBedrockModelConfigurationsTypeDef] = None
    collaboratorConfigurations: Optional[Sequence[CollaboratorConfigurationTypeDef]] = None
    collaborators: Optional[Sequence[CollaboratorTypeDef]] = None
    customerEncryptionKeyArn: Optional[str] = None
    enableTrace: Optional[bool] = None
    endSession: Optional[bool] = None
    guardrailConfiguration: Optional[GuardrailConfigurationWithArnTypeDef] = None
    idleSessionTTLInSeconds: Optional[int] = None
    inlineSessionState: Optional[InlineSessionStateTypeDef] = None
    inputText: Optional[str] = None
    knowledgeBases: Optional[Sequence[KnowledgeBaseTypeDef]] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfigurationTypeDef] = None
    streamingConfigurations: Optional[StreamingConfigurationsTypeDef] = None


class InvokeAgentRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    sessionId: str
    bedrockModelConfigurations: Optional[BedrockModelConfigurationsTypeDef] = None
    enableTrace: Optional[bool] = None
    endSession: Optional[bool] = None
    inputText: Optional[str] = None
    memoryId: Optional[str] = None
    sessionState: Optional[SessionStateTypeDef] = None
    sourceArn: Optional[str] = None
    streamingConfigurations: Optional[StreamingConfigurationsTypeDef] = None


class InlineAgentPayloadPartTypeDef(BaseValidatorModel):
    pass


class InlineAgentResponseStreamTypeDef(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedExceptionTypeDef] = None
    badGatewayException: Optional[BadGatewayExceptionTypeDef] = None
    chunk: Optional[InlineAgentPayloadPartTypeDef] = None
    conflictException: Optional[ConflictExceptionTypeDef] = None
    dependencyFailedException: Optional[DependencyFailedExceptionTypeDef] = None
    files: Optional[InlineAgentFilePartTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    resourceNotFoundException: Optional[ResourceNotFoundExceptionTypeDef] = None
    returnControl: Optional[InlineAgentReturnControlPayloadTypeDef] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    trace: Optional[InlineAgentTracePartTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None


class PayloadPartTypeDef(BaseValidatorModel):
    pass


class ResponseStreamTypeDef(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedExceptionTypeDef] = None
    badGatewayException: Optional[BadGatewayExceptionTypeDef] = None
    chunk: Optional[PayloadPartTypeDef] = None
    conflictException: Optional[ConflictExceptionTypeDef] = None
    dependencyFailedException: Optional[DependencyFailedExceptionTypeDef] = None
    files: Optional[FilePartTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    modelNotReadyException: Optional[ModelNotReadyExceptionTypeDef] = None
    resourceNotFoundException: Optional[ResourceNotFoundExceptionTypeDef] = None
    returnControl: Optional[ReturnControlPayloadTypeDef] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    trace: Optional[TracePartTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None


class InvokeInlineAgentResponseTypeDef(BaseValidatorModel):
    completion: EventStream[InlineAgentResponseStreamTypeDef]
    contentType: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class InvokeAgentResponseTypeDef(BaseValidatorModel):
    completion: EventStream[ResponseStreamTypeDef]
    contentType: str
    memoryId: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef



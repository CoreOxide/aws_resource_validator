
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel, EventStream
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

class S3Identifier(BaseValidatorModel):
    s3BucketName: Optional[str] = None
    s3ObjectKey: Optional[str] = None


class AccessDeniedException(BaseValidatorModel):
    message: Optional[str] = None


class ActionGroupInvocationOutput(BaseValidatorModel):
    text: Optional[str] = None


class AnalyzePromptEvent(BaseValidatorModel):
    message: Optional[str] = None


class BadGatewayException(BaseValidatorModel):
    message: Optional[str] = None
    resourceName: Optional[str] = None


class PerformanceConfiguration(BaseValidatorModel):
    latency: Optional[PerformanceConfigLatencyType] = None


class BedrockRerankingModelConfiguration(BaseValidatorModel):
    modelArn: str
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None


class Caller(BaseValidatorModel):
    agentAliasArn: Optional[str] = None


class CodeInterpreterInvocationInput(BaseValidatorModel):
    code: Optional[str] = None
    files: Optional[List[str]] = None


class CodeInterpreterInvocationOutput(BaseValidatorModel):
    executionError: Optional[str] = None
    executionOutput: Optional[str] = None
    executionTimeout: Optional[bool] = None
    files: Optional[List[str]] = None


class CollaboratorConfiguration(BaseValidatorModel):
    collaboratorInstruction: str
    collaboratorName: str
    agentAliasArn: Optional[str] = None
    relayConversationHistory: Optional[RelayConversationHistoryType] = None


class GuardrailConfigurationWithArn(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str


class ConflictException(BaseValidatorModel):
    message: Optional[str] = None


class ContentBlock(BaseValidatorModel):
    text: Optional[str] = None


class CreateInvocationRequest(BaseValidatorModel):
    sessionIdentifier: str
    description: Optional[str] = None
    invocationId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateSessionRequest(BaseValidatorModel):
    encryptionKeyArn: Optional[str] = None
    sessionMetadata: Optional[Mapping[str, str]] = None
    tags: Optional[Mapping[str, str]] = None


class CustomOrchestrationTraceEvent(BaseValidatorModel):
    text: Optional[str] = None


class DeleteAgentMemoryRequest(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: Optional[str] = None
    sessionId: Optional[str] = None


class DeleteSessionRequest(BaseValidatorModel):
    sessionIdentifier: str


class DependencyFailedException(BaseValidatorModel):
    message: Optional[str] = None
    resourceName: Optional[str] = None


class EndSessionRequest(BaseValidatorModel):
    sessionIdentifier: str


class S3ObjectDoc(BaseValidatorModel):
    uri: str


class GuardrailConfiguration(BaseValidatorModel):
    guardrailId: str
    guardrailVersion: str


class PromptTemplate(BaseValidatorModel):
    textPromptTemplate: Optional[str] = None


class FailureTrace(BaseValidatorModel):
    failureReason: Optional[str] = None
    traceId: Optional[str] = None


class FieldForReranking(BaseValidatorModel):
    fieldName: str


class S3ObjectFile(BaseValidatorModel):
    uri: str


class FilterAttribute(BaseValidatorModel):
    key: str
    value: Mapping[str, Any]


class FinalResponse(BaseValidatorModel):
    text: Optional[str] = None


class FlowCompletionEvent(BaseValidatorModel):
    completionReason: FlowCompletionReasonType


class FlowInputContent(BaseValidatorModel):
    document: Optional[Mapping[str, Any]] = None


class FlowMultiTurnInputContent(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None


class FlowOutputContent(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None


class InternalServerException(BaseValidatorModel):
    message: Optional[str] = None
    reason: Optional[str] = None


class ResourceNotFoundException(BaseValidatorModel):
    message: Optional[str] = None


class ServiceQuotaExceededException(BaseValidatorModel):
    message: Optional[str] = None


class ThrottlingException(BaseValidatorModel):
    message: Optional[str] = None


class ValidationException(BaseValidatorModel):
    message: Optional[str] = None


class FlowTraceCondition(BaseValidatorModel):
    conditionName: str


class FlowTraceNodeInputContent(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None


class FlowTraceNodeOutputContent(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetAgentMemoryRequest(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal["SESSION_SUMMARY"]
    maxItems: Optional[int] = None
    nextToken: Optional[str] = None


class GetInvocationStepRequest(BaseValidatorModel):
    invocationIdentifier: str
    invocationStepId: str
    sessionIdentifier: str


class GetSessionRequest(BaseValidatorModel):
    sessionIdentifier: str


class GuardrailCustomWord(BaseValidatorModel):
    action: Optional[Literal["BLOCKED"]] = None
    match: Optional[str] = None


class GuardrailEvent(BaseValidatorModel):
    action: Optional[GuadrailActionType] = None


class GuardrailRegexFilter(BaseValidatorModel):
    action: Optional[GuardrailSensitiveInformationPolicyActionType] = None
    match: Optional[str] = None
    name: Optional[str] = None
    regex: Optional[str] = None


class S3Location(BaseValidatorModel):
    uri: str


class TextInferenceConfig(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None


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


class TextPrompt(BaseValidatorModel):
    text: str


class KnowledgeBaseLookupInput(BaseValidatorModel):
    knowledgeBaseId: Optional[str] = None
    text: Optional[str] = None


class InvocationStepSummary(BaseValidatorModel):
    invocationId: str
    invocationStepId: str
    invocationStepTime: datetime
    sessionId: str


class InvocationSummary(BaseValidatorModel):
    createdAt: datetime
    invocationId: str
    sessionId: str


class StreamingConfigurations(BaseValidatorModel):
    applyGuardrailInterval: Optional[int] = None
    streamFinalResponse: Optional[bool] = None


class KnowledgeBaseQuery(BaseValidatorModel):
    text: str


class ListInvocationStepsRequest(BaseValidatorModel):
    sessionIdentifier: str
    invocationIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListInvocationsRequest(BaseValidatorModel):
    sessionIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSessionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SessionSummary(BaseValidatorModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    sessionArn: str
    sessionId: str
    sessionStatus: SessionStatusType


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class MemorySessionSummary(BaseValidatorModel):
    memoryId: Optional[str] = None
    sessionExpiryTime: Optional[datetime] = None
    sessionId: Optional[str] = None
    sessionStartTime: Optional[datetime] = None
    summaryText: Optional[str] = None


class Usage(BaseValidatorModel):
    inputTokens: Optional[int] = None
    outputTokens: Optional[int] = None


class ModelNotReadyException(BaseValidatorModel):
    message: Optional[str] = None


class RepromptResponse(BaseValidatorModel):
    source: Optional[SourceType] = None
    text: Optional[str] = None


class RawResponse(BaseValidatorModel):
    content: Optional[str] = None


class Rationale(BaseValidatorModel):
    text: Optional[str] = None
    traceId: Optional[str] = None


class PostProcessingParsedResponse(BaseValidatorModel):
    text: Optional[str] = None


class PreProcessingParsedResponse(BaseValidatorModel):
    isValid: Optional[bool] = None
    rationale: Optional[str] = None


class ReasoningTextBlock(BaseValidatorModel):
    text: str
    signature: Optional[str] = None


class RerankTextDocument(BaseValidatorModel):
    text: Optional[str] = None


class RetrievalResultConfluenceLocation(BaseValidatorModel):
    url: Optional[str] = None


class RetrievalResultKendraDocumentLocation(BaseValidatorModel):
    uri: Optional[str] = None


class RetrievalResultS3Location(BaseValidatorModel):
    uri: Optional[str] = None


class RetrievalResultSalesforceLocation(BaseValidatorModel):
    url: Optional[str] = None


class RetrievalResultSharePointLocation(BaseValidatorModel):
    url: Optional[str] = None


class RetrievalResultSqlLocation(BaseValidatorModel):
    query: Optional[str] = None


class RetrievalResultWebLocation(BaseValidatorModel):
    url: Optional[str] = None


class RetrieveAndGenerateInput(BaseValidatorModel):
    text: str


class RetrieveAndGenerateOutputEvent(BaseValidatorModel):
    text: str


class RetrieveAndGenerateOutput(BaseValidatorModel):
    text: str


class RetrieveAndGenerateSessionConfiguration(BaseValidatorModel):
    kmsKeyArn: str


class Span(BaseValidatorModel):
    end: Optional[int] = None
    start: Optional[int] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TextToSqlKnowledgeBaseConfiguration(BaseValidatorModel):
    knowledgeBaseArn: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateSessionRequest(BaseValidatorModel):
    sessionIdentifier: str
    sessionMetadata: Optional[Mapping[str, str]] = None


class VectorSearchBedrockRerankingModelConfiguration(BaseValidatorModel):
    modelArn: str
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None


class APISchema(BaseValidatorModel):
    payload: Optional[str] = None
    s3: Optional[S3Identifier] = None


class Parameter(BaseValidatorModel):
    pass


class PropertyParameters(BaseValidatorModel):
    properties: Optional[List[Parameter]] = None


class RequestBody(BaseValidatorModel):
    content: Optional[Dict[str, List[Parameter]]] = None


class BedrockModelConfigurations(BaseValidatorModel):
    performanceConfig: Optional[PerformanceConfiguration] = None


class InlineBedrockModelConfigurations(BaseValidatorModel):
    performanceConfig: Optional[PerformanceConfiguration] = None


class ModelPerformanceConfiguration(BaseValidatorModel):
    performanceConfig: Optional[PerformanceConfiguration] = None


class BedrockRerankingConfiguration(BaseValidatorModel):
    modelConfiguration: BedrockRerankingModelConfiguration
    numberOfResults: Optional[int] = None


class Blob(BaseValidatorModel):
    pass


class ByteContentDoc(BaseValidatorModel):
    contentType: str
    data: Blob
    identifier: str


class ByteContentFile(BaseValidatorModel):
    data: Blob
    mediaType: str


class Message(BaseValidatorModel):
    content: Sequence[ContentBlock]
    role: ConversationRoleType


class CreateInvocationResponse(BaseValidatorModel):
    createdAt: datetime
    invocationId: str
    sessionId: str
    ResponseMetadata: ResponseMetadata


class CreateSessionResponse(BaseValidatorModel):
    createdAt: datetime
    sessionArn: str
    sessionId: str
    sessionStatus: SessionStatusType
    ResponseMetadata: ResponseMetadata


class EndSessionResponse(BaseValidatorModel):
    sessionArn: str
    sessionId: str
    sessionStatus: SessionStatusType
    ResponseMetadata: ResponseMetadata


class GetSessionResponse(BaseValidatorModel):
    createdAt: datetime
    encryptionKeyArn: str
    lastUpdatedAt: datetime
    sessionArn: str
    sessionId: str
    sessionMetadata: Dict[str, str]
    sessionStatus: SessionStatusType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutInvocationStepResponse(BaseValidatorModel):
    invocationStepId: str
    ResponseMetadata: ResponseMetadata


class UpdateSessionResponse(BaseValidatorModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    sessionArn: str
    sessionId: str
    sessionStatus: SessionStatusType
    ResponseMetadata: ResponseMetadata


class CustomOrchestrationTrace(BaseValidatorModel):
    event: Optional[CustomOrchestrationTraceEvent] = None
    traceId: Optional[str] = None


class RerankingMetadataSelectiveModeConfiguration(BaseValidatorModel):
    fieldsToExclude: Optional[Sequence[FieldForReranking]] = None
    fieldsToInclude: Optional[Sequence[FieldForReranking]] = None


class OutputFile(BaseValidatorModel):
    pass


class FilePart(BaseValidatorModel):
    files: Optional[List[OutputFile]] = None


class InlineAgentFilePart(BaseValidatorModel):
    files: Optional[List[OutputFile]] = None


class FlowInput(BaseValidatorModel):
    content: FlowInputContent
    nodeName: str
    nodeInputName: Optional[str] = None
    nodeOutputName: Optional[str] = None


class FlowMultiTurnInputRequestEvent(BaseValidatorModel):
    content: FlowMultiTurnInputContent
    nodeName: str
    nodeType: NodeTypeType


class FlowOutputEvent(BaseValidatorModel):
    content: FlowOutputContent
    nodeName: str
    nodeType: NodeTypeType


class FlowTraceConditionNodeResultEvent(BaseValidatorModel):
    nodeName: str
    satisfiedConditions: List[FlowTraceCondition]
    timestamp: datetime


class FlowTraceNodeInputField(BaseValidatorModel):
    content: FlowTraceNodeInputContent
    nodeInputName: str


class FlowTraceNodeOutputField(BaseValidatorModel):
    content: FlowTraceNodeOutputContent
    nodeOutputName: str


class ParameterDetail(BaseValidatorModel):
    pass


class FunctionDefinition(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Mapping[str, ParameterDetail]] = None
    requireConfirmation: Optional[RequireConfirmationType] = None


class FunctionParameter(BaseValidatorModel):
    pass


class FunctionInvocationInput(BaseValidatorModel):
    actionGroup: str
    actionInvocationType: Optional[ActionInvocationTypeType] = None
    agentId: Optional[str] = None
    collaboratorName: Optional[str] = None
    function: Optional[str] = None
    parameters: Optional[List[FunctionParameter]] = None


class GeneratedQuery(BaseValidatorModel):
    pass


class GenerateQueryResponse(BaseValidatorModel):
    queries: List[GeneratedQuery]
    ResponseMetadata: ResponseMetadata


class GetAgentMemoryRequestPaginate(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal["SESSION_SUMMARY"]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInvocationStepsRequestPaginate(BaseValidatorModel):
    sessionIdentifier: str
    invocationIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInvocationsRequestPaginate(BaseValidatorModel):
    sessionIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSessionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GuardrailContentFilter(BaseValidatorModel):
    pass


class GuardrailContentPolicyAssessment(BaseValidatorModel):
    filters: Optional[List[GuardrailContentFilter]] = None


class GuardrailManagedWord(BaseValidatorModel):
    pass


class GuardrailWordPolicyAssessment(BaseValidatorModel):
    customWords: Optional[List[GuardrailCustomWord]] = None
    managedWordLists: Optional[List[GuardrailManagedWord]] = None


class GuardrailPiiEntityFilter(BaseValidatorModel):
    pass


class GuardrailSensitiveInformationPolicyAssessment(BaseValidatorModel):
    piiEntities: Optional[List[GuardrailPiiEntityFilter]] = None
    regexes: Optional[List[GuardrailRegexFilter]] = None


class GuardrailTopic(BaseValidatorModel):
    pass


class GuardrailTopicPolicyAssessment(BaseValidatorModel):
    topics: Optional[List[GuardrailTopic]] = None


class MetadataAttributeSchema(BaseValidatorModel):
    pass


class ImplicitFilterConfiguration(BaseValidatorModel):
    metadataAttributes: Sequence[MetadataAttributeSchema]
    modelArn: str


class InferenceConfig(BaseValidatorModel):
    textInferenceConfig: Optional[TextInferenceConfig] = None


class InputPrompt(BaseValidatorModel):
    textPrompt: Optional[TextPrompt] = None


class OptimizedPrompt(BaseValidatorModel):
    textPrompt: Optional[TextPrompt] = None


class ListInvocationStepsResponse(BaseValidatorModel):
    invocationStepSummaries: List[InvocationStepSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListInvocationsResponse(BaseValidatorModel):
    invocationSummaries: List[InvocationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSessionsResponse(BaseValidatorModel):
    sessionSummaries: List[SessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Memory(BaseValidatorModel):
    sessionSummary: Optional[MemorySessionSummary] = None


class Metadata(BaseValidatorModel):
    usage: Optional[Usage] = None


class ReasoningContentBlock(BaseValidatorModel):
    reasoningText: Optional[ReasoningTextBlock] = None
    redactedContent: Optional[bytes] = None


class TextResponsePart(BaseValidatorModel):
    span: Optional[Span] = None
    text: Optional[str] = None


class ApiRequestBody(BaseValidatorModel):
    content: Optional[Dict[str, PropertyParameters]] = None


class ActionGroupInvocationInput(BaseValidatorModel):
    actionGroupName: Optional[str] = None
    apiPath: Optional[str] = None
    executionType: Optional[ExecutionTypeType] = None
    function: Optional[str] = None
    invocationId: Optional[str] = None
    parameters: Optional[List[Parameter]] = None
    requestBody: Optional[RequestBody] = None
    verb: Optional[str] = None


class ExternalSource(BaseValidatorModel):
    sourceType: ExternalSourceTypeType
    byteContent: Optional[ByteContentDoc] = None
    s3Location: Optional[S3ObjectDoc] = None


class FileSource(BaseValidatorModel):
    sourceType: FileSourceTypeType
    byteContent: Optional[ByteContentFile] = None
    s3Location: Optional[S3ObjectFile] = None


class ConversationHistory(BaseValidatorModel):
    messages: Optional[Sequence[Message]] = None


class MetadataConfigurationForReranking(BaseValidatorModel):
    selectionMode: RerankingMetadataSelectionModeType
    selectiveModeConfiguration: Optional[RerankingMetadataSelectiveModeConfiguration] = None


class InvokeFlowRequest(BaseValidatorModel):
    flowAliasIdentifier: str
    flowIdentifier: str
    inputs: Sequence[FlowInput]
    enableTrace: Optional[bool] = None
    executionId: Optional[str] = None
    modelPerformanceConfiguration: Optional[ModelPerformanceConfiguration] = None


class FlowTraceNodeInputEvent(BaseValidatorModel):
    fields: List[FlowTraceNodeInputField]
    nodeName: str
    timestamp: datetime


class FlowTraceNodeOutputEvent(BaseValidatorModel):
    fields: List[FlowTraceNodeOutputField]
    nodeName: str
    timestamp: datetime


class FunctionSchema(BaseValidatorModel):
    functions: Optional[Sequence[FunctionDefinition]] = None


class GuardrailAssessment(BaseValidatorModel):
    contentPolicy: Optional[GuardrailContentPolicyAssessment] = None
    sensitiveInformationPolicy: Optional[GuardrailSensitiveInformationPolicyAssessment] = None
    topicPolicy: Optional[GuardrailTopicPolicyAssessment] = None
    wordPolicy: Optional[GuardrailWordPolicyAssessment] = None


class ImageInputOutput(BaseValidatorModel):
    pass


class ContentBodyOutput(BaseValidatorModel):
    body: Optional[str] = None
    images: Optional[List[ImageInputOutput]] = None


class ExternalSourcesGenerationConfiguration(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    inferenceConfig: Optional[InferenceConfig] = None
    performanceConfig: Optional[PerformanceConfiguration] = None
    promptTemplate: Optional[PromptTemplate] = None


class GenerationConfiguration(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    inferenceConfig: Optional[InferenceConfig] = None
    performanceConfig: Optional[PerformanceConfiguration] = None
    promptTemplate: Optional[PromptTemplate] = None


class QueryTransformationConfiguration(BaseValidatorModel):
    pass


class OrchestrationConfiguration(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    inferenceConfig: Optional[InferenceConfig] = None
    performanceConfig: Optional[PerformanceConfiguration] = None
    promptTemplate: Optional[PromptTemplate] = None
    queryTransformationConfiguration: Optional[QueryTransformationConfiguration] = None


class InferenceConfigurationUnion(BaseValidatorModel):
    pass


class PromptConfiguration(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    basePromptTemplate: Optional[str] = None
    foundationModel: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationUnion] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None


class OptimizedPromptEvent(BaseValidatorModel):
    optimizedPrompt: Optional[OptimizedPrompt] = None


class GetAgentMemoryResponse(BaseValidatorModel):
    memoryContents: List[Memory]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RoutingClassifierModelInvocationOutput(BaseValidatorModel):
    metadata: Optional[Metadata] = None
    rawResponse: Optional[RawResponse] = None
    traceId: Optional[str] = None


class OrchestrationModelInvocationOutput(BaseValidatorModel):
    metadata: Optional[Metadata] = None
    rawResponse: Optional[RawResponse] = None
    reasoningContent: Optional[ReasoningContentBlock] = None
    traceId: Optional[str] = None


class PostProcessingModelInvocationOutput(BaseValidatorModel):
    metadata: Optional[Metadata] = None
    parsedResponse: Optional[PostProcessingParsedResponse] = None
    rawResponse: Optional[RawResponse] = None
    reasoningContent: Optional[ReasoningContentBlock] = None
    traceId: Optional[str] = None


class PreProcessingModelInvocationOutput(BaseValidatorModel):
    metadata: Optional[Metadata] = None
    parsedResponse: Optional[PreProcessingParsedResponse] = None
    rawResponse: Optional[RawResponse] = None
    reasoningContent: Optional[ReasoningContentBlock] = None
    traceId: Optional[str] = None


class RerankDocumentOutput(BaseValidatorModel):
    pass


class RerankResult(BaseValidatorModel):
    index: int
    relevanceScore: float
    document: Optional[RerankDocumentOutput] = None


class RetrievalResultContent(BaseValidatorModel):
    pass


class RetrievalResultLocation(BaseValidatorModel):
    pass


class KnowledgeBaseRetrievalResult(BaseValidatorModel):
    content: RetrievalResultContent
    location: Optional[RetrievalResultLocation] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    score: Optional[float] = None


class RetrievedReference(BaseValidatorModel):
    content: Optional[RetrievalResultContent] = None
    location: Optional[RetrievalResultLocation] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None


class GeneratedResponsePart(BaseValidatorModel):
    textResponsePart: Optional[TextResponsePart] = None


class TextToSqlConfiguration(BaseValidatorModel):
    pass


class TransformationConfiguration(BaseValidatorModel):
    mode: Literal["TEXT_TO_SQL"]
    textToSqlConfiguration: Optional[TextToSqlConfiguration] = None


class ApiParameter(BaseValidatorModel):
    pass


class ApiInvocationInput(BaseValidatorModel):
    actionGroup: str
    actionInvocationType: Optional[ActionInvocationTypeType] = None
    agentId: Optional[str] = None
    apiPath: Optional[str] = None
    collaboratorName: Optional[str] = None
    httpMethod: Optional[str] = None
    parameters: Optional[List[ApiParameter]] = None
    requestBody: Optional[ApiRequestBody] = None


class InputFile(BaseValidatorModel):
    name: str
    source: FileSource
    useCase: FileUseCaseType


class VectorSearchBedrockRerankingConfiguration(BaseValidatorModel):
    modelConfiguration: VectorSearchBedrockRerankingModelConfiguration
    metadataConfiguration: Optional[MetadataConfigurationForReranking] = None
    numberOfRerankedResults: Optional[int] = None


class FlowTrace(BaseValidatorModel):
    conditionNodeResultTrace: Optional[FlowTraceConditionNodeResultEvent] = None
    nodeInputTrace: Optional[FlowTraceNodeInputEvent] = None
    nodeOutputTrace: Optional[FlowTraceNodeOutputEvent] = None


class ActionGroupExecutor(BaseValidatorModel):
    pass


class AgentActionGroup(BaseValidatorModel):
    actionGroupName: str
    actionGroupExecutor: Optional[ActionGroupExecutor] = None
    apiSchema: Optional[APISchema] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchema] = None
    parentActionGroupSignature: Optional[ActionGroupSignatureType] = None
    parentActionGroupSignatureParams: Optional[Mapping[str, str]] = None


class GuardrailTrace(BaseValidatorModel):
    action: Optional[GuardrailActionType] = None
    inputAssessments: Optional[List[GuardrailAssessment]] = None
    outputAssessments: Optional[List[GuardrailAssessment]] = None
    traceId: Optional[str] = None


class ApiResultOutput(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    apiPath: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    httpMethod: Optional[str] = None
    httpStatusCode: Optional[int] = None
    responseBody: Optional[Dict[str, ContentBodyOutput]] = None
    responseState: Optional[ResponseStateType] = None


class FunctionResultOutput(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    function: Optional[str] = None
    responseBody: Optional[Dict[str, ContentBodyOutput]] = None
    responseState: Optional[ResponseStateType] = None


class ImageBlockOutput(BaseValidatorModel):
    pass


class BedrockSessionContentBlockOutput(BaseValidatorModel):
    image: Optional[ImageBlockOutput] = None
    text: Optional[str] = None


class ImageBlock(BaseValidatorModel):
    pass


class BedrockSessionContentBlock(BaseValidatorModel):
    image: Optional[ImageBlock] = None
    text: Optional[str] = None


class ExternalSourcesRetrieveAndGenerateConfiguration(BaseValidatorModel):
    modelArn: str
    sources: Sequence[ExternalSource]
    generationConfiguration: Optional[ExternalSourcesGenerationConfiguration] = None


class PromptOverrideConfiguration(BaseValidatorModel):
    promptConfigurations: Sequence[PromptConfiguration]
    overrideLambda: Optional[str] = None


class OptimizedPromptStream(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedException] = None
    analyzePromptEvent: Optional[AnalyzePromptEvent] = None
    badGatewayException: Optional[BadGatewayException] = None
    dependencyFailedException: Optional[DependencyFailedException] = None
    internalServerException: Optional[InternalServerException] = None
    optimizedPromptEvent: Optional[OptimizedPromptEvent] = None
    throttlingException: Optional[ThrottlingException] = None
    validationException: Optional[ValidationException] = None


class ModelInvocationInput(BaseValidatorModel):
    pass


class PostProcessingTrace(BaseValidatorModel):
    modelInvocationInput: Optional[ModelInvocationInput] = None
    modelInvocationOutput: Optional[PostProcessingModelInvocationOutput] = None


class PreProcessingTrace(BaseValidatorModel):
    modelInvocationInput: Optional[ModelInvocationInput] = None
    modelInvocationOutput: Optional[PreProcessingModelInvocationOutput] = None


class RerankResponse(BaseValidatorModel):
    results: List[RerankResult]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RetrieveResponse(BaseValidatorModel):
    guardrailAction: GuadrailActionType
    retrievalResults: List[KnowledgeBaseRetrievalResult]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class KnowledgeBaseLookupOutput(BaseValidatorModel):
    retrievedReferences: Optional[List[RetrievedReference]] = None


class Citation(BaseValidatorModel):
    generatedResponsePart: Optional[GeneratedResponsePart] = None
    retrievedReferences: Optional[List[RetrievedReference]] = None


class QueryGenerationInput(BaseValidatorModel):
    pass


class GenerateQueryRequest(BaseValidatorModel):
    queryGenerationInput: QueryGenerationInput
    transformationConfiguration: TransformationConfiguration


class InvocationInputMember(BaseValidatorModel):
    apiInvocationInput: Optional[ApiInvocationInput] = None
    functionInvocationInput: Optional[FunctionInvocationInput] = None


class FlowTraceEvent(BaseValidatorModel):
    trace: FlowTrace


class InvocationResultMemberOutput(BaseValidatorModel):
    apiResult: Optional[ApiResultOutput] = None
    functionResult: Optional[FunctionResultOutput] = None


class InvocationStepPayloadOutput(BaseValidatorModel):
    contentBlocks: Optional[List[BedrockSessionContentBlockOutput]] = None


class InvocationStepPayload(BaseValidatorModel):
    contentBlocks: Optional[Sequence[BedrockSessionContentBlock]] = None


class OptimizePromptResponse(BaseValidatorModel):
    optimizedPrompt: EventStream[OptimizedPromptStream]
    ResponseMetadata: ResponseMetadata


class RerankSource(BaseValidatorModel):
    pass


class RerankQuery(BaseValidatorModel):
    pass


class RerankingConfiguration(BaseValidatorModel):
    pass


class RerankRequestPaginate(BaseValidatorModel):
    queries: Sequence[RerankQuery]
    rerankingConfiguration: RerankingConfiguration
    sources: Sequence[RerankSource]
    PaginationConfig: Optional[PaginatorConfig] = None


class RerankRequest(BaseValidatorModel):
    queries: Sequence[RerankQuery]
    rerankingConfiguration: RerankingConfiguration
    sources: Sequence[RerankSource]
    nextToken: Optional[str] = None


class Attribution(BaseValidatorModel):
    citations: Optional[List[Citation]] = None


class CitationEvent(BaseValidatorModel):
    citation: Optional[Citation] = None
    generatedResponsePart: Optional[GeneratedResponsePart] = None
    retrievedReferences: Optional[List[RetrievedReference]] = None


class RetrieveAndGenerateResponse(BaseValidatorModel):
    citations: List[Citation]
    guardrailAction: GuadrailActionType
    output: RetrieveAndGenerateOutput
    sessionId: str
    ResponseMetadata: ResponseMetadata


class InlineAgentReturnControlPayload(BaseValidatorModel):
    invocationId: Optional[str] = None
    invocationInputs: Optional[List[InvocationInputMember]] = None


class ReturnControlPayload(BaseValidatorModel):
    invocationId: Optional[str] = None
    invocationInputs: Optional[List[InvocationInputMember]] = None


class ImageInputUnion(BaseValidatorModel):
    pass


class ContentBody(BaseValidatorModel):
    body: Optional[str] = None
    images: Optional[Sequence[ImageInputUnion]] = None


class FlowResponseStream(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedException] = None
    badGatewayException: Optional[BadGatewayException] = None
    conflictException: Optional[ConflictException] = None
    dependencyFailedException: Optional[DependencyFailedException] = None
    flowCompletionEvent: Optional[FlowCompletionEvent] = None
    flowMultiTurnInputRequestEvent: Optional[FlowMultiTurnInputRequestEvent] = None
    flowOutputEvent: Optional[FlowOutputEvent] = None
    flowTraceEvent: Optional[FlowTraceEvent] = None
    internalServerException: Optional[InternalServerException] = None
    resourceNotFoundException: Optional[ResourceNotFoundException] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededException] = None
    throttlingException: Optional[ThrottlingException] = None
    validationException: Optional[ValidationException] = None


class ReturnControlResults(BaseValidatorModel):
    invocationId: Optional[str] = None
    returnControlInvocationResults: Optional[List[InvocationResultMemberOutput]] = None


class InvocationStep(BaseValidatorModel):
    invocationId: str
    invocationStepId: str
    invocationStepTime: datetime
    payload: InvocationStepPayloadOutput
    sessionId: str


class RetrieveAndGenerateStreamResponseOutput(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedException] = None
    badGatewayException: Optional[BadGatewayException] = None
    citation: Optional[CitationEvent] = None
    conflictException: Optional[ConflictException] = None
    dependencyFailedException: Optional[DependencyFailedException] = None
    guardrail: Optional[GuardrailEvent] = None
    internalServerException: Optional[InternalServerException] = None
    output: Optional[RetrieveAndGenerateOutputEvent] = None
    resourceNotFoundException: Optional[ResourceNotFoundException] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededException] = None
    throttlingException: Optional[ThrottlingException] = None
    validationException: Optional[ValidationException] = None


class KnowledgeBaseVectorSearchConfigurationPaginator(BaseValidatorModel):
    pass


class KnowledgeBaseRetrievalConfigurationPaginator(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfigurationPaginator


class KnowledgeBaseVectorSearchConfiguration(BaseValidatorModel):
    pass


class KnowledgeBaseRetrievalConfiguration(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfiguration


class InvokeFlowResponse(BaseValidatorModel):
    executionId: str
    responseStream: EventStream[FlowResponseStream]
    ResponseMetadata: ResponseMetadata


class GetInvocationStepResponse(BaseValidatorModel):
    invocationStep: InvocationStep
    ResponseMetadata: ResponseMetadata


class InvocationStepPayloadUnion(BaseValidatorModel):
    pass


class Timestamp(BaseValidatorModel):
    pass


class PutInvocationStepRequest(BaseValidatorModel):
    invocationIdentifier: str
    invocationStepTime: Timestamp
    payload: InvocationStepPayloadUnion
    sessionIdentifier: str
    invocationStepId: Optional[str] = None


class RetrieveAndGenerateStreamResponse(BaseValidatorModel):
    sessionId: str
    stream: EventStream[RetrieveAndGenerateStreamResponseOutput]
    ResponseMetadata: ResponseMetadata


class AgentCollaboratorOutputPayload(BaseValidatorModel):
    pass


class AgentCollaboratorInvocationOutput(BaseValidatorModel):
    agentCollaboratorAliasArn: Optional[str] = None
    agentCollaboratorName: Optional[str] = None
    output: Optional[AgentCollaboratorOutputPayload] = None


class ContentBodyUnion(BaseValidatorModel):
    pass


class ApiResult(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    apiPath: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    httpMethod: Optional[str] = None
    httpStatusCode: Optional[int] = None
    responseBody: Optional[Mapping[str, ContentBodyUnion]] = None
    responseState: Optional[ResponseStateType] = None


class FunctionResult(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    function: Optional[str] = None
    responseBody: Optional[Mapping[str, ContentBodyUnion]] = None
    responseState: Optional[ResponseStateType] = None


class RetrieveRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    retrievalQuery: KnowledgeBaseQuery
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class KnowledgeBaseConfiguration(BaseValidatorModel):
    knowledgeBaseId: str
    retrievalConfiguration: KnowledgeBaseRetrievalConfiguration


class KnowledgeBaseRetrieveAndGenerateConfiguration(BaseValidatorModel):
    knowledgeBaseId: str
    modelArn: str
    generationConfiguration: Optional[GenerationConfiguration] = None
    orchestrationConfiguration: Optional[OrchestrationConfiguration] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfiguration] = None


class KnowledgeBase(BaseValidatorModel):
    description: str
    knowledgeBaseId: str
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfiguration] = None


class RetrieveRequest(BaseValidatorModel):
    knowledgeBaseId: str
    retrievalQuery: KnowledgeBaseQuery
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    nextToken: Optional[str] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfiguration] = None


class Collaborator(BaseValidatorModel):
    foundationModel: str
    instruction: str
    actionGroups: Optional[Sequence[AgentActionGroup]] = None
    agentCollaboration: Optional[AgentCollaborationType] = None
    agentName: Optional[str] = None
    collaboratorConfigurations: Optional[Sequence[CollaboratorConfiguration]] = None
    customerEncryptionKeyArn: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationWithArn] = None
    idleSessionTTLInSeconds: Optional[int] = None
    knowledgeBases: Optional[Sequence[KnowledgeBase]] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfiguration] = None


class AgentCollaboratorInvocationInput(BaseValidatorModel):
    pass


class InvocationInput(BaseValidatorModel):
    actionGroupInvocationInput: Optional[ActionGroupInvocationInput] = None
    agentCollaboratorInvocationInput: Optional[AgentCollaboratorInvocationInput] = None
    codeInterpreterInvocationInput: Optional[CodeInterpreterInvocationInput] = None
    invocationType: Optional[InvocationTypeType] = None
    knowledgeBaseLookupInput: Optional[KnowledgeBaseLookupInput] = None
    traceId: Optional[str] = None


class ApiResultUnion(BaseValidatorModel):
    pass


class FunctionResultUnion(BaseValidatorModel):
    pass


class InvocationResultMember(BaseValidatorModel):
    apiResult: Optional[ApiResultUnion] = None
    functionResult: Optional[FunctionResultUnion] = None


class Observation(BaseValidatorModel):
    pass


class OrchestrationTrace(BaseValidatorModel):
    invocationInput: Optional[InvocationInput] = None
    modelInvocationInput: Optional[ModelInvocationInput] = None
    modelInvocationOutput: Optional[OrchestrationModelInvocationOutput] = None
    observation: Optional[Observation] = None
    rationale: Optional[Rationale] = None


class RoutingClassifierTrace(BaseValidatorModel):
    invocationInput: Optional[InvocationInput] = None
    modelInvocationInput: Optional[ModelInvocationInput] = None
    modelInvocationOutput: Optional[RoutingClassifierModelInvocationOutput] = None
    observation: Optional[Observation] = None


class Trace(BaseValidatorModel):
    customOrchestrationTrace: Optional[CustomOrchestrationTrace] = None
    failureTrace: Optional[FailureTrace] = None
    guardrailTrace: Optional[GuardrailTrace] = None
    orchestrationTrace: Optional[OrchestrationTrace] = None
    postProcessingTrace: Optional[PostProcessingTrace] = None
    preProcessingTrace: Optional[PreProcessingTrace] = None
    routingClassifierTrace: Optional[RoutingClassifierTrace] = None


class InvocationResultMemberUnion(BaseValidatorModel):
    pass


class InlineSessionState(BaseValidatorModel):
    conversationHistory: Optional[ConversationHistory] = None
    files: Optional[Sequence[InputFile]] = None
    invocationId: Optional[str] = None
    promptSessionAttributes: Optional[Mapping[str, str]] = None
    returnControlInvocationResults: Optional[Sequence[InvocationResultMemberUnion]] = None
    sessionAttributes: Optional[Mapping[str, str]] = None


class SessionState(BaseValidatorModel):
    conversationHistory: Optional[ConversationHistory] = None
    files: Optional[Sequence[InputFile]] = None
    invocationId: Optional[str] = None
    knowledgeBaseConfigurations: Optional[Sequence[KnowledgeBaseConfiguration]] = None
    promptSessionAttributes: Optional[Mapping[str, str]] = None
    returnControlInvocationResults: Optional[Sequence[InvocationResultMemberUnion]] = None
    sessionAttributes: Optional[Mapping[str, str]] = None


class InlineAgentTracePart(BaseValidatorModel):
    sessionId: Optional[str] = None
    trace: Optional[Trace] = None


class TracePart(BaseValidatorModel):
    agentAliasId: Optional[str] = None
    agentId: Optional[str] = None
    agentVersion: Optional[str] = None
    callerChain: Optional[List[Caller]] = None
    collaboratorName: Optional[str] = None
    eventTime: Optional[datetime] = None
    sessionId: Optional[str] = None
    trace: Optional[Trace] = None


class InvokeInlineAgentRequest(BaseValidatorModel):
    foundationModel: str
    instruction: str
    sessionId: str
    actionGroups: Optional[Sequence[AgentActionGroup]] = None
    agentCollaboration: Optional[AgentCollaborationType] = None
    bedrockModelConfigurations: Optional[InlineBedrockModelConfigurations] = None
    collaboratorConfigurations: Optional[Sequence[CollaboratorConfiguration]] = None
    collaborators: Optional[Sequence[Collaborator]] = None
    customerEncryptionKeyArn: Optional[str] = None
    enableTrace: Optional[bool] = None
    endSession: Optional[bool] = None
    guardrailConfiguration: Optional[GuardrailConfigurationWithArn] = None
    idleSessionTTLInSeconds: Optional[int] = None
    inlineSessionState: Optional[InlineSessionState] = None
    inputText: Optional[str] = None
    knowledgeBases: Optional[Sequence[KnowledgeBase]] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfiguration] = None
    streamingConfigurations: Optional[StreamingConfigurations] = None


class InvokeAgentRequest(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    sessionId: str
    bedrockModelConfigurations: Optional[BedrockModelConfigurations] = None
    enableTrace: Optional[bool] = None
    endSession: Optional[bool] = None
    inputText: Optional[str] = None
    memoryId: Optional[str] = None
    sessionState: Optional[SessionState] = None
    sourceArn: Optional[str] = None
    streamingConfigurations: Optional[StreamingConfigurations] = None


class InlineAgentPayloadPart(BaseValidatorModel):
    pass


class InlineAgentResponseStream(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedException] = None
    badGatewayException: Optional[BadGatewayException] = None
    chunk: Optional[InlineAgentPayloadPart] = None
    conflictException: Optional[ConflictException] = None
    dependencyFailedException: Optional[DependencyFailedException] = None
    files: Optional[InlineAgentFilePart] = None
    internalServerException: Optional[InternalServerException] = None
    resourceNotFoundException: Optional[ResourceNotFoundException] = None
    returnControl: Optional[InlineAgentReturnControlPayload] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededException] = None
    throttlingException: Optional[ThrottlingException] = None
    trace: Optional[InlineAgentTracePart] = None
    validationException: Optional[ValidationException] = None


class PayloadPart(BaseValidatorModel):
    pass


class ResponseStream(BaseValidatorModel):
    accessDeniedException: Optional[AccessDeniedException] = None
    badGatewayException: Optional[BadGatewayException] = None
    chunk: Optional[PayloadPart] = None
    conflictException: Optional[ConflictException] = None
    dependencyFailedException: Optional[DependencyFailedException] = None
    files: Optional[FilePart] = None
    internalServerException: Optional[InternalServerException] = None
    modelNotReadyException: Optional[ModelNotReadyException] = None
    resourceNotFoundException: Optional[ResourceNotFoundException] = None
    returnControl: Optional[ReturnControlPayload] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededException] = None
    throttlingException: Optional[ThrottlingException] = None
    trace: Optional[TracePart] = None
    validationException: Optional[ValidationException] = None


class InvokeInlineAgentResponse(BaseValidatorModel):
    completion: EventStream[InlineAgentResponseStream]
    contentType: str
    sessionId: str
    ResponseMetadata: ResponseMetadata


class InvokeAgentResponse(BaseValidatorModel):
    completion: EventStream[ResponseStream]
    contentType: str
    memoryId: str
    sessionId: str
    ResponseMetadata: ResponseMetadata



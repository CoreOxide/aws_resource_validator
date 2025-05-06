from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class S3Identifier(BaseValidatorModel):
    s3BucketName: Optional[str] = None
    s3ObjectKey: Optional[str] = None


class AccessDeniedException(BaseValidatorModel):
    message: Optional[str] = None


class ActionGroupExecutor(BaseValidatorModel):
    customControl: Optional[Literal['RETURN_CONTROL']] = None
    lambda_:Optional[str] = None


class Parameter(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None


class ActionGroupInvocationOutput(BaseValidatorModel):
    text: Optional[str] = None


class AnalyzePromptEvent(BaseValidatorModel):
    message: Optional[str] = None


class ApiParameter(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None


class BadGatewayException(BaseValidatorModel):
    message: Optional[str] = None
    resourceName: Optional[str] = None


class PerformanceConfiguration(BaseValidatorModel):
    latency: Optional[PerformanceConfigLatencyType] = None


class BedrockRerankingModelConfiguration(BaseValidatorModel):
    modelArn: str
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


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
    sessionMetadata: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None


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


class OutputFile(BaseValidatorModel):
    bytes: Optional[bytes] = None
    name: Optional[str] = None
    type: Optional[str] = None


class S3ObjectFile(BaseValidatorModel):
    uri: str


class FilterAttribute(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class FinalResponse(BaseValidatorModel):
    text: Optional[str] = None


class FlowCompletionEvent(BaseValidatorModel):
    completionReason: FlowCompletionReasonType


class FlowInputContent(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None


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


class ParameterDetail(BaseValidatorModel):
    type: ParameterTypeType
    description: Optional[str] = None
    required: Optional[bool] = None


class FunctionParameter(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None


class QueryGenerationInput(BaseValidatorModel):
    text: str
    type: Literal['TEXT']


class GeneratedQuery(BaseValidatorModel):
    sql: Optional[str] = None
    type: Optional[Literal['REDSHIFT_SQL']] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetAgentMemoryRequest(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal['SESSION_SUMMARY']
    maxItems: Optional[int] = None
    nextToken: Optional[str] = None


class GetInvocationStepRequest(BaseValidatorModel):
    invocationIdentifier: str
    invocationStepId: str
    sessionIdentifier: str


class GetSessionRequest(BaseValidatorModel):
    sessionIdentifier: str


class GuardrailContentFilter(BaseValidatorModel):
    action: Optional[Literal['BLOCKED']] = None
    confidence: Optional[GuardrailContentFilterConfidenceType] = None
    type: Optional[GuardrailContentFilterTypeType] = None


class GuardrailCustomWord(BaseValidatorModel):
    action: Optional[Literal['BLOCKED']] = None
    match: Optional[str] = None


class GuardrailEvent(BaseValidatorModel):
    action: Optional[GuadrailActionType] = None


class GuardrailManagedWord(BaseValidatorModel):
    action: Optional[Literal['BLOCKED']] = None
    match: Optional[str] = None
    type: Optional[Literal['PROFANITY']] = None


class GuardrailPiiEntityFilter(BaseValidatorModel):
    action: Optional[GuardrailSensitiveInformationPolicyActionType] = None
    match: Optional[str] = None
    type: Optional[GuardrailPiiEntityTypeType] = None


class GuardrailRegexFilter(BaseValidatorModel):
    action: Optional[GuardrailSensitiveInformationPolicyActionType] = None
    match: Optional[str] = None
    name: Optional[str] = None
    regex: Optional[str] = None


class GuardrailTopic(BaseValidatorModel):
    action: Optional[Literal['BLOCKED']] = None
    name: Optional[str] = None
    type: Optional[Literal['DENY']] = None


class ImageInputSourceOutput(BaseValidatorModel):
    bytes: Optional[bytes] = None


class S3Location(BaseValidatorModel):
    uri: str


class MetadataAttributeSchema(BaseValidatorModel):
    description: str
    key: str
    type: AttributeTypeType


class TextInferenceConfig(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[List[str]] = None
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
    stopSequences: Optional[List[str]] = None
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


class QueryTransformationConfiguration(BaseValidatorModel):
    type: Literal['QUERY_DECOMPOSITION']


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

Timestamp = Union[datetime, str]


class ReasoningTextBlock(BaseValidatorModel):
    text: str
    signature: Optional[str] = None


class RerankTextDocument(BaseValidatorModel):
    text: Optional[str] = None


class RetrievalResultConfluenceLocation(BaseValidatorModel):
    url: Optional[str] = None


class RetrievalResultContentColumn(BaseValidatorModel):
    columnName: Optional[str] = None
    columnValue: Optional[str] = None
    type: Optional[RetrievalResultContentColumnTypeType] = None


class RetrievalResultCustomDocumentLocation(BaseValidatorModel):
    id: Optional[str] = None


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
    tags: Dict[str, str]


class TextToSqlKnowledgeBaseConfiguration(BaseValidatorModel):
    knowledgeBaseArn: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateSessionRequest(BaseValidatorModel):
    sessionIdentifier: str
    sessionMetadata: Optional[Dict[str, str]] = None


class VectorSearchBedrockRerankingModelConfiguration(BaseValidatorModel):
    modelArn: str
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None


class APISchema(BaseValidatorModel):
    payload: Optional[str] = None
    s3: Optional[S3Identifier] = None


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


class ByteContentDoc(BaseValidatorModel):
    contentType: str
    data: Blob
    identifier: str


class ByteContentFile(BaseValidatorModel):
    data: Blob
    mediaType: str


class ImageInputSource(BaseValidatorModel):
    bytes: Optional[Blob] = None


class Message(BaseValidatorModel):
    content: List[ContentBlock]
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
    fieldsToExclude: Optional[List[FieldForReranking]] = None
    fieldsToInclude: Optional[List[FieldForReranking]] = None


class FilePart(BaseValidatorModel):
    files: Optional[List[OutputFile]] = None


class InlineAgentFilePart(BaseValidatorModel):
    files: Optional[List[OutputFile]] = None


class RetrievalFilterPaginator(BaseValidatorModel):
    andAll: Optional[List[Dict[str, Any]]] = None
    equals: Optional[FilterAttribute] = None
    greaterThan: Optional[FilterAttribute] = None
    greaterThanOrEquals: Optional[FilterAttribute] = None
    in_: Optional[FilterAttribute] = None
    lessThan: Optional[FilterAttribute] = None
    lessThanOrEquals: Optional[FilterAttribute] = None
    listContains: Optional[FilterAttribute] = None
    notEquals: Optional[FilterAttribute] = None
    notIn: Optional[FilterAttribute] = None
    orAll: Optional[List[Dict[str, Any]]] = None
    startsWith: Optional[FilterAttribute] = None
    stringContains: Optional[FilterAttribute] = None


class RetrievalFilter(BaseValidatorModel):
    andAll: Optional[List[Dict[str, Any]]] = None
    equals: Optional[FilterAttribute] = None
    greaterThan: Optional[FilterAttribute] = None
    greaterThanOrEquals: Optional[FilterAttribute] = None
    in_: Optional[FilterAttribute] = None
    lessThan: Optional[FilterAttribute] = None
    lessThanOrEquals: Optional[FilterAttribute] = None
    listContains: Optional[FilterAttribute] = None
    notEquals: Optional[FilterAttribute] = None
    notIn: Optional[FilterAttribute] = None
    orAll: Optional[List[Dict[str, Any]]] = None
    startsWith: Optional[FilterAttribute] = None
    stringContains: Optional[FilterAttribute] = None


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


class FunctionDefinition(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, ParameterDetail]] = None
    requireConfirmation: Optional[RequireConfirmationType] = None


class FunctionInvocationInput(BaseValidatorModel):
    actionGroup: str
    actionInvocationType: Optional[ActionInvocationTypeType] = None
    agentId: Optional[str] = None
    collaboratorName: Optional[str] = None
    function: Optional[str] = None
    parameters: Optional[List[FunctionParameter]] = None


class GenerateQueryResponse(BaseValidatorModel):
    queries: List[GeneratedQuery]
    ResponseMetadata: ResponseMetadata


class GetAgentMemoryRequestPaginate(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal['SESSION_SUMMARY']
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


class GuardrailContentPolicyAssessment(BaseValidatorModel):
    filters: Optional[List[GuardrailContentFilter]] = None


class GuardrailWordPolicyAssessment(BaseValidatorModel):
    customWords: Optional[List[GuardrailCustomWord]] = None
    managedWordLists: Optional[List[GuardrailManagedWord]] = None


class GuardrailSensitiveInformationPolicyAssessment(BaseValidatorModel):
    piiEntities: Optional[List[GuardrailPiiEntityFilter]] = None
    regexes: Optional[List[GuardrailRegexFilter]] = None


class GuardrailTopicPolicyAssessment(BaseValidatorModel):
    topics: Optional[List[GuardrailTopic]] = None


class ImageInputOutput(BaseValidatorModel):
    format: ImageInputFormatType
    source: ImageInputSourceOutput


class ImageSourceOutput(BaseValidatorModel):
    bytes: Optional[bytes] = None
    s3Location: Optional[S3Location] = None


class ImageSource(BaseValidatorModel):
    bytes: Optional[Blob] = None
    s3Location: Optional[S3Location] = None


class ImplicitFilterConfiguration(BaseValidatorModel):
    metadataAttributes: List[MetadataAttributeSchema]
    modelArn: str


class InferenceConfig(BaseValidatorModel):
    textInferenceConfig: Optional[TextInferenceConfig] = None


class ModelInvocationInput(BaseValidatorModel):
    foundationModel: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationOutput] = None
    overrideLambda: Optional[str] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    text: Optional[str] = None
    traceId: Optional[str] = None
    type: Optional[PromptTypeType] = None

InferenceConfigurationUnion = Union[InferenceConfiguration, InferenceConfigurationOutput]


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


class RerankDocumentOutput(BaseValidatorModel):
    type: RerankDocumentTypeType
    jsonDocument: Optional[Dict[str, Any]] = None
    textDocument: Optional[RerankTextDocument] = None


class RerankDocument(BaseValidatorModel):
    type: RerankDocumentTypeType
    jsonDocument: Optional[Dict[str, Any]] = None
    textDocument: Optional[RerankTextDocument] = None


class RerankQuery(BaseValidatorModel):
    textQuery: RerankTextDocument
    type: Literal['TEXT']


class RetrievalResultContent(BaseValidatorModel):
    byteContent: Optional[str] = None
    row: Optional[List[RetrievalResultContentColumn]] = None
    text: Optional[str] = None
    type: Optional[RetrievalResultContentTypeType] = None


class RetrievalResultLocation(BaseValidatorModel):
    type: RetrievalResultLocationTypeType
    confluenceLocation: Optional[RetrievalResultConfluenceLocation] = None
    customDocumentLocation: Optional[RetrievalResultCustomDocumentLocation] = None
    kendraDocumentLocation: Optional[RetrievalResultKendraDocumentLocation] = None
    s3Location: Optional[RetrievalResultS3Location] = None
    salesforceLocation: Optional[RetrievalResultSalesforceLocation] = None
    sharePointLocation: Optional[RetrievalResultSharePointLocation] = None
    sqlLocation: Optional[RetrievalResultSqlLocation] = None
    webLocation: Optional[RetrievalResultWebLocation] = None


class TextResponsePart(BaseValidatorModel):
    span: Optional[Span] = None
    text: Optional[str] = None


class TextToSqlConfiguration(BaseValidatorModel):
    type: Literal['KNOWLEDGE_BASE']
    knowledgeBaseConfiguration: Optional[TextToSqlKnowledgeBaseConfiguration] = None


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


class RerankingConfiguration(BaseValidatorModel):
    bedrockRerankingConfiguration: BedrockRerankingConfiguration
    type: Literal['BEDROCK_RERANKING_MODEL']


class ExternalSource(BaseValidatorModel):
    sourceType: ExternalSourceTypeType
    byteContent: Optional[ByteContentDoc] = None
    s3Location: Optional[S3ObjectDoc] = None


class FileSource(BaseValidatorModel):
    sourceType: FileSourceTypeType
    byteContent: Optional[ByteContentFile] = None
    s3Location: Optional[S3ObjectFile] = None

ImageInputSourceUnion = Union[ImageInputSource, ImageInputSourceOutput]


class ConversationHistory(BaseValidatorModel):
    messages: Optional[List[Message]] = None


class MetadataConfigurationForReranking(BaseValidatorModel):
    selectionMode: RerankingMetadataSelectionModeType
    selectiveModeConfiguration: Optional[RerankingMetadataSelectiveModeConfiguration] = None


class InvokeFlowRequest(BaseValidatorModel):
    flowAliasIdentifier: str
    flowIdentifier: str
    inputs: List[FlowInput]
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
    functions: Optional[List[FunctionDefinition]] = None


class GuardrailAssessment(BaseValidatorModel):
    contentPolicy: Optional[GuardrailContentPolicyAssessment] = None
    sensitiveInformationPolicy: Optional[GuardrailSensitiveInformationPolicyAssessment] = None
    topicPolicy: Optional[GuardrailTopicPolicyAssessment] = None
    wordPolicy: Optional[GuardrailWordPolicyAssessment] = None


class ContentBodyOutput(BaseValidatorModel):
    body: Optional[str] = None
    images: Optional[List[ImageInputOutput]] = None


class ImageBlockOutput(BaseValidatorModel):
    format: ImageFormatType
    source: ImageSourceOutput


class ImageBlock(BaseValidatorModel):
    format: ImageFormatType
    source: ImageSource


class ExternalSourcesGenerationConfiguration(BaseValidatorModel):
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    inferenceConfig: Optional[InferenceConfig] = None
    performanceConfig: Optional[PerformanceConfiguration] = None
    promptTemplate: Optional[PromptTemplate] = None


class GenerationConfiguration(BaseValidatorModel):
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    inferenceConfig: Optional[InferenceConfig] = None
    performanceConfig: Optional[PerformanceConfiguration] = None
    promptTemplate: Optional[PromptTemplate] = None


class OrchestrationConfiguration(BaseValidatorModel):
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None
    inferenceConfig: Optional[InferenceConfig] = None
    performanceConfig: Optional[PerformanceConfiguration] = None
    promptTemplate: Optional[PromptTemplate] = None
    queryTransformationConfiguration: Optional[QueryTransformationConfiguration] = None


class PromptConfiguration(BaseValidatorModel):
    additionalModelRequestFields: Optional[Dict[str, Any]] = None
    basePromptTemplate: Optional[str] = None
    foundationModel: Optional[str] = None
    inferenceConfiguration: Optional[InferenceConfigurationUnion] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    promptState: Optional[PromptStateType] = None
    promptType: Optional[PromptTypeType] = None


class OptimizePromptRequest(BaseValidatorModel):
    input: InputPrompt
    targetModelId: str


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


class RerankResult(BaseValidatorModel):
    index: int
    relevanceScore: float
    document: Optional[RerankDocumentOutput] = None

RerankDocumentUnion = Union[RerankDocument, RerankDocumentOutput]


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


class TransformationConfiguration(BaseValidatorModel):
    mode: Literal['TEXT_TO_SQL']
    textToSqlConfiguration: Optional[TextToSqlConfiguration] = None


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


class ImageInput(BaseValidatorModel):
    format: ImageInputFormatType
    source: ImageInputSourceUnion


class VectorSearchBedrockRerankingConfiguration(BaseValidatorModel):
    modelConfiguration: VectorSearchBedrockRerankingModelConfiguration
    metadataConfiguration: Optional[MetadataConfigurationForReranking] = None
    numberOfRerankedResults: Optional[int] = None


class FlowTrace(BaseValidatorModel):
    conditionNodeResultTrace: Optional[FlowTraceConditionNodeResultEvent] = None
    nodeInputTrace: Optional[FlowTraceNodeInputEvent] = None
    nodeOutputTrace: Optional[FlowTraceNodeOutputEvent] = None


class AgentActionGroup(BaseValidatorModel):
    actionGroupName: str
    actionGroupExecutor: Optional[ActionGroupExecutor] = None
    apiSchema: Optional[APISchema] = None
    description: Optional[str] = None
    functionSchema: Optional[FunctionSchema] = None
    parentActionGroupSignature: Optional[ActionGroupSignatureType] = None
    parentActionGroupSignatureParams: Optional[Dict[str, str]] = None


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


class BedrockSessionContentBlockOutput(BaseValidatorModel):
    image: Optional[ImageBlockOutput] = None
    text: Optional[str] = None


class BedrockSessionContentBlock(BaseValidatorModel):
    image: Optional[ImageBlock] = None
    text: Optional[str] = None


class ExternalSourcesRetrieveAndGenerateConfiguration(BaseValidatorModel):
    modelArn: str
    sources: List[ExternalSource]
    generationConfiguration: Optional[ExternalSourcesGenerationConfiguration] = None


class PromptOverrideConfiguration(BaseValidatorModel):
    promptConfigurations: List[PromptConfiguration]
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


class RerankSource(BaseValidatorModel):
    inlineDocumentSource: RerankDocumentUnion
    type: Literal['INLINE']


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


class GenerateQueryRequest(BaseValidatorModel):
    queryGenerationInput: QueryGenerationInput
    transformationConfiguration: TransformationConfiguration


class InvocationInputMember(BaseValidatorModel):
    apiInvocationInput: Optional[ApiInvocationInput] = None
    functionInvocationInput: Optional[FunctionInvocationInput] = None

ImageInputUnion = Union[ImageInput, ImageInputOutput]


class VectorSearchRerankingConfiguration(BaseValidatorModel):
    type: Literal['BEDROCK_RERANKING_MODEL']
    bedrockRerankingConfiguration: Optional[VectorSearchBedrockRerankingConfiguration] = None


class FlowTraceEvent(BaseValidatorModel):
    trace: FlowTrace


class InvocationResultMemberOutput(BaseValidatorModel):
    apiResult: Optional[ApiResultOutput] = None
    functionResult: Optional[FunctionResultOutput] = None


class InvocationStepPayloadOutput(BaseValidatorModel):
    contentBlocks: Optional[List[BedrockSessionContentBlockOutput]] = None


class InvocationStepPayload(BaseValidatorModel):
    contentBlocks: Optional[List[BedrockSessionContentBlock]] = None


class OptimizePromptResponse(BaseValidatorModel):
    optimizedPrompt: EventStream[OptimizedPromptStream]
    ResponseMetadata: ResponseMetadata


class RerankRequestPaginate(BaseValidatorModel):
    queries: List[RerankQuery]
    rerankingConfiguration: RerankingConfiguration
    sources: List[RerankSource]
    PaginationConfig: Optional[PaginatorConfig] = None


class RerankRequest(BaseValidatorModel):
    queries: List[RerankQuery]
    rerankingConfiguration: RerankingConfiguration
    sources: List[RerankSource]
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


class ContentBody(BaseValidatorModel):
    body: Optional[str] = None
    images: Optional[List[ImageInputUnion]] = None


class KnowledgeBaseVectorSearchConfigurationPaginator(BaseValidatorModel):
    filter: Optional[RetrievalFilterPaginator] = None
    implicitFilterConfiguration: Optional[ImplicitFilterConfiguration] = None
    numberOfResults: Optional[int] = None
    overrideSearchType: Optional[SearchTypeType] = None
    rerankingConfiguration: Optional[VectorSearchRerankingConfiguration] = None


class KnowledgeBaseVectorSearchConfiguration(BaseValidatorModel):
    filter: Optional[RetrievalFilter] = None
    implicitFilterConfiguration: Optional[ImplicitFilterConfiguration] = None
    numberOfResults: Optional[int] = None
    overrideSearchType: Optional[SearchTypeType] = None
    rerankingConfiguration: Optional[VectorSearchRerankingConfiguration] = None


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

InvocationStepPayloadUnion = Union[InvocationStepPayload, InvocationStepPayloadOutput]


class InlineAgentPayloadPart(BaseValidatorModel):
    attribution: Optional[Attribution] = None
    bytes: Optional[bytes] = None


class PayloadPart(BaseValidatorModel):
    attribution: Optional[Attribution] = None
    bytes: Optional[bytes] = None


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


class AgentCollaboratorOutputPayload(BaseValidatorModel):
    returnControlPayload: Optional[ReturnControlPayload] = None
    text: Optional[str] = None
    type: Optional[PayloadTypeType] = None

ContentBodyUnion = Union[ContentBody, ContentBodyOutput]


class KnowledgeBaseRetrievalConfigurationPaginator(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfigurationPaginator


class KnowledgeBaseRetrievalConfiguration(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfiguration


class InvokeFlowResponse(BaseValidatorModel):
    executionId: str
    responseStream: EventStream[FlowResponseStream]
    ResponseMetadata: ResponseMetadata


class AgentCollaboratorInputPayload(BaseValidatorModel):
    returnControlResults: Optional[ReturnControlResults] = None
    text: Optional[str] = None
    type: Optional[PayloadTypeType] = None


class GetInvocationStepResponse(BaseValidatorModel):
    invocationStep: InvocationStep
    ResponseMetadata: ResponseMetadata


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


class AgentCollaboratorInvocationOutput(BaseValidatorModel):
    agentCollaboratorAliasArn: Optional[str] = None
    agentCollaboratorName: Optional[str] = None
    output: Optional[AgentCollaboratorOutputPayload] = None


class ApiResult(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    apiPath: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    httpMethod: Optional[str] = None
    httpStatusCode: Optional[int] = None
    responseBody: Optional[Dict[str, ContentBodyUnion]] = None
    responseState: Optional[ResponseStateType] = None


class FunctionResult(BaseValidatorModel):
    actionGroup: str
    agentId: Optional[str] = None
    confirmationState: Optional[ConfirmationStateType] = None
    function: Optional[str] = None
    responseBody: Optional[Dict[str, ContentBodyUnion]] = None
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


class AgentCollaboratorInvocationInput(BaseValidatorModel):
    agentCollaboratorAliasArn: Optional[str] = None
    agentCollaboratorName: Optional[str] = None
    input: Optional[AgentCollaboratorInputPayload] = None


class Observation(BaseValidatorModel):
    actionGroupInvocationOutput: Optional[ActionGroupInvocationOutput] = None
    agentCollaboratorInvocationOutput: Optional[AgentCollaboratorInvocationOutput] = None
    codeInterpreterInvocationOutput: Optional[CodeInterpreterInvocationOutput] = None
    finalResponse: Optional[FinalResponse] = None
    knowledgeBaseLookupOutput: Optional[KnowledgeBaseLookupOutput] = None
    repromptResponse: Optional[RepromptResponse] = None
    traceId: Optional[str] = None
    type: Optional[TypeType] = None

ApiResultUnion = Union[ApiResult, ApiResultOutput]

FunctionResultUnion = Union[FunctionResult, FunctionResultOutput]


class RetrieveAndGenerateConfiguration(BaseValidatorModel):
    type: RetrieveAndGenerateTypeType
    externalSourcesConfiguration: Optional[ExternalSourcesRetrieveAndGenerateConfiguration] = None
    knowledgeBaseConfiguration: Optional[KnowledgeBaseRetrieveAndGenerateConfiguration] = None


class Collaborator(BaseValidatorModel):
    foundationModel: str
    instruction: str
    actionGroups: Optional[List[AgentActionGroup]] = None
    agentCollaboration: Optional[AgentCollaborationType] = None
    agentName: Optional[str] = None
    collaboratorConfigurations: Optional[List[CollaboratorConfiguration]] = None
    customerEncryptionKeyArn: Optional[str] = None
    guardrailConfiguration: Optional[GuardrailConfigurationWithArn] = None
    idleSessionTTLInSeconds: Optional[int] = None
    knowledgeBases: Optional[List[KnowledgeBase]] = None
    promptOverrideConfiguration: Optional[PromptOverrideConfiguration] = None


class InvocationInput(BaseValidatorModel):
    actionGroupInvocationInput: Optional[ActionGroupInvocationInput] = None
    agentCollaboratorInvocationInput: Optional[AgentCollaboratorInvocationInput] = None
    codeInterpreterInvocationInput: Optional[CodeInterpreterInvocationInput] = None
    invocationType: Optional[InvocationTypeType] = None
    knowledgeBaseLookupInput: Optional[KnowledgeBaseLookupInput] = None
    traceId: Optional[str] = None


class InvocationResultMember(BaseValidatorModel):
    apiResult: Optional[ApiResultUnion] = None
    functionResult: Optional[FunctionResultUnion] = None


class RetrieveAndGenerateRequest(BaseValidatorModel):
    input: RetrieveAndGenerateInput
    retrieveAndGenerateConfiguration: Optional[RetrieveAndGenerateConfiguration] = None
    sessionConfiguration: Optional[RetrieveAndGenerateSessionConfiguration] = None
    sessionId: Optional[str] = None


class RetrieveAndGenerateStreamRequest(BaseValidatorModel):
    input: RetrieveAndGenerateInput
    retrieveAndGenerateConfiguration: Optional[RetrieveAndGenerateConfiguration] = None
    sessionConfiguration: Optional[RetrieveAndGenerateSessionConfiguration] = None
    sessionId: Optional[str] = None


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

InvocationResultMemberUnion = Union[InvocationResultMember, InvocationResultMemberOutput]


class Trace(BaseValidatorModel):
    customOrchestrationTrace: Optional[CustomOrchestrationTrace] = None
    failureTrace: Optional[FailureTrace] = None
    guardrailTrace: Optional[GuardrailTrace] = None
    orchestrationTrace: Optional[OrchestrationTrace] = None
    postProcessingTrace: Optional[PostProcessingTrace] = None
    preProcessingTrace: Optional[PreProcessingTrace] = None
    routingClassifierTrace: Optional[RoutingClassifierTrace] = None


class InlineSessionState(BaseValidatorModel):
    conversationHistory: Optional[ConversationHistory] = None
    files: Optional[List[InputFile]] = None
    invocationId: Optional[str] = None
    promptSessionAttributes: Optional[Dict[str, str]] = None
    returnControlInvocationResults: Optional[List[InvocationResultMemberUnion]] = None
    sessionAttributes: Optional[Dict[str, str]] = None


class SessionState(BaseValidatorModel):
    conversationHistory: Optional[ConversationHistory] = None
    files: Optional[List[InputFile]] = None
    invocationId: Optional[str] = None
    knowledgeBaseConfigurations: Optional[List[KnowledgeBaseConfiguration]] = None
    promptSessionAttributes: Optional[Dict[str, str]] = None
    returnControlInvocationResults: Optional[List[InvocationResultMemberUnion]] = None
    sessionAttributes: Optional[Dict[str, str]] = None


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
    actionGroups: Optional[List[AgentActionGroup]] = None
    agentCollaboration: Optional[AgentCollaborationType] = None
    bedrockModelConfigurations: Optional[InlineBedrockModelConfigurations] = None
    collaboratorConfigurations: Optional[List[CollaboratorConfiguration]] = None
    collaborators: Optional[List[Collaborator]] = None
    customerEncryptionKeyArn: Optional[str] = None
    enableTrace: Optional[bool] = None
    endSession: Optional[bool] = None
    guardrailConfiguration: Optional[GuardrailConfigurationWithArn] = None
    idleSessionTTLInSeconds: Optional[int] = None
    inlineSessionState: Optional[InlineSessionState] = None
    inputText: Optional[str] = None
    knowledgeBases: Optional[List[KnowledgeBase]] = None
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
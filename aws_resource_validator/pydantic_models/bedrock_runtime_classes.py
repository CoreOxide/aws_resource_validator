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
from aws_resource_validator.pydantic_models.bedrock_runtime_constants import *

class GuardrailOutputContent(BaseValidatorModel):
    text: Optional[str] = None


class GuardrailUsage(BaseValidatorModel):
    topicPolicyUnits: int
    contentPolicyUnits: int
    wordPolicyUnits: int
    sensitiveInformationPolicyUnits: int
    sensitiveInformationPolicyFreeUnits: int
    contextualGroundingPolicyUnits: int


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AsyncInvokeS3OutputDataConfig(BaseValidatorModel):
    s3Uri: str
    kmsKeyId: Optional[str] = None
    bucketOwner: Optional[str] = None


class ReasoningContentBlockDelta(BaseValidatorModel):
    text: Optional[str] = None
    redactedContent: Optional[bytes] = None
    signature: Optional[str] = None


class ToolUseBlockStart(BaseValidatorModel):
    toolUseId: str
    name: str


class ContentBlockStopEvent(BaseValidatorModel):
    contentBlockIndex: int


class ConverseMetrics(BaseValidatorModel):
    latencyMs: int


class GuardrailConfiguration(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str
    trace: Optional[GuardrailTraceType] = None


class InferenceConfiguration(BaseValidatorModel):
    maxTokens: Optional[int] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None
    stopSequences: Optional[Sequence[str]] = None


class PerformanceConfiguration(BaseValidatorModel):
    latency: Optional[PerformanceConfigLatencyType] = None


class PromptVariableValues(BaseValidatorModel):
    text: Optional[str] = None


class TokenUsage(BaseValidatorModel):
    inputTokens: int
    outputTokens: int
    totalTokens: int


class ConverseStreamMetrics(BaseValidatorModel):
    latencyMs: int


class InternalServerException(BaseValidatorModel):
    message: Optional[str] = None


class MessageStartEvent(BaseValidatorModel):
    role: ConversationRoleType


class MessageStopEvent(BaseValidatorModel):
    stopReason: StopReasonType
    additionalModelResponseFields: Optional[Dict[str, Any]] = None


class ModelStreamErrorException(BaseValidatorModel):
    message: Optional[str] = None
    originalStatusCode: Optional[int] = None
    originalMessage: Optional[str] = None


class ServiceUnavailableException(BaseValidatorModel):
    message: Optional[str] = None


class ThrottlingException(BaseValidatorModel):
    message: Optional[str] = None


class ValidationException(BaseValidatorModel):
    message: Optional[str] = None


class GuardrailStreamConfiguration(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str
    trace: Optional[GuardrailTraceType] = None
    streamProcessingMode: Optional[GuardrailStreamProcessingModeType] = None


class PromptRouterTrace(BaseValidatorModel):
    invokedModelId: Optional[str] = None


class GetAsyncInvokeRequest(BaseValidatorModel):
    invocationArn: str


class GuardrailTextBlock(BaseValidatorModel):
    text: str
    qualifiers: Optional[Sequence[GuardrailContentQualifierType]] = None


class GuardrailConverseTextBlockOutput(BaseValidatorModel):
    text: str
    qualifiers: Optional[List[GuardrailConverseContentQualifierType]] = None


class GuardrailConverseTextBlock(BaseValidatorModel):
    text: str
    qualifiers: Optional[Sequence[GuardrailConverseContentQualifierType]] = None


class GuardrailImageCoverage(BaseValidatorModel):
    guarded: Optional[int] = None
    total: Optional[int] = None


class GuardrailTextCharactersCoverage(BaseValidatorModel):
    guarded: Optional[int] = None
    total: Optional[int] = None


class GuardrailCustomWord(BaseValidatorModel):
    match: str
    action: Literal["BLOCKED"]


class GuardrailRegexFilter(BaseValidatorModel):
    action: GuardrailSensitiveInformationPolicyActionType
    name: Optional[str] = None
    match: Optional[str] = None
    regex: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ModelTimeoutException(BaseValidatorModel):
    message: Optional[str] = None


class ReasoningTextBlock(BaseValidatorModel):
    text: str
    signature: Optional[str] = None


class S3Location(BaseValidatorModel):
    uri: str
    bucketOwner: Optional[str] = None


class SpecificToolChoice(BaseValidatorModel):
    name: str


class Tag(BaseValidatorModel):
    key: str
    value: str


class ToolInputSchema(BaseValidatorModel):
    json: Optional[Mapping[str, Any]] = None


class InvokeModelResponse(BaseValidatorModel):
    body: StreamingBody
    contentType: str
    performanceConfigLatency: PerformanceConfigLatencyType
    ResponseMetadata: ResponseMetadata


class StartAsyncInvokeResponse(BaseValidatorModel):
    invocationArn: str
    ResponseMetadata: ResponseMetadata


class AsyncInvokeOutputDataConfig(BaseValidatorModel):
    s3OutputDataConfig: Optional[AsyncInvokeS3OutputDataConfig] = None


class Blob(BaseValidatorModel):
    pass


class InvokeModelRequest(BaseValidatorModel):
    modelId: str
    body: Optional[Blob] = None
    contentType: Optional[str] = None
    accept: Optional[str] = None
    trace: Optional[TraceType] = None
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None
    performanceConfigLatency: Optional[PerformanceConfigLatencyType] = None


class InvokeModelWithResponseStreamRequest(BaseValidatorModel):
    modelId: str
    body: Optional[Blob] = None
    contentType: Optional[str] = None
    accept: Optional[str] = None
    trace: Optional[TraceType] = None
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None
    performanceConfigLatency: Optional[PerformanceConfigLatencyType] = None


class ToolUseBlockDelta(BaseValidatorModel):
    pass


class ContentBlockDelta(BaseValidatorModel):
    text: Optional[str] = None
    toolUse: Optional[ToolUseBlockDelta] = None
    reasoningContent: Optional[ReasoningContentBlockDelta] = None


class ContentBlockStart(BaseValidatorModel):
    toolUse: Optional[ToolUseBlockStart] = None


class GuardrailContentFilter(BaseValidatorModel):
    pass


class GuardrailContentPolicyAssessment(BaseValidatorModel):
    filters: List[GuardrailContentFilter]


class GuardrailContextualGroundingFilter(BaseValidatorModel):
    pass


class GuardrailContextualGroundingPolicyAssessment(BaseValidatorModel):
    filters: Optional[List[GuardrailContextualGroundingFilter]] = None


class GuardrailCoverage(BaseValidatorModel):
    textCharacters: Optional[GuardrailTextCharactersCoverage] = None
    images: Optional[GuardrailImageCoverage] = None


class GuardrailManagedWord(BaseValidatorModel):
    pass


class GuardrailWordPolicyAssessment(BaseValidatorModel):
    customWords: List[GuardrailCustomWord]
    managedWordLists: List[GuardrailManagedWord]


class GuardrailPiiEntityFilter(BaseValidatorModel):
    pass


class GuardrailSensitiveInformationPolicyAssessment(BaseValidatorModel):
    piiEntities: List[GuardrailPiiEntityFilter]
    regexes: List[GuardrailRegexFilter]


class GuardrailTopic(BaseValidatorModel):
    pass


class GuardrailTopicPolicyAssessment(BaseValidatorModel):
    topics: List[GuardrailTopic]


class Timestamp(BaseValidatorModel):
    pass


class ListAsyncInvokesRequestPaginate(BaseValidatorModel):
    submitTimeAfter: Optional[Timestamp] = None
    submitTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[AsyncInvokeStatusType] = None
    sortBy: Optional[Literal["SubmissionTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAsyncInvokesRequest(BaseValidatorModel):
    submitTimeAfter: Optional[Timestamp] = None
    submitTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[AsyncInvokeStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["SubmissionTime"]] = None
    sortOrder: Optional[SortOrderType] = None


class PayloadPart(BaseValidatorModel):
    pass


class ResponseStream(BaseValidatorModel):
    chunk: Optional[PayloadPart] = None
    internalServerException: Optional[InternalServerException] = None
    modelStreamErrorException: Optional[ModelStreamErrorException] = None
    validationException: Optional[ValidationException] = None
    throttlingException: Optional[ThrottlingException] = None
    modelTimeoutException: Optional[ModelTimeoutException] = None
    serviceUnavailableException: Optional[ServiceUnavailableException] = None


class ReasoningContentBlockOutput(BaseValidatorModel):
    reasoningText: Optional[ReasoningTextBlock] = None
    redactedContent: Optional[bytes] = None


class ReasoningContentBlock(BaseValidatorModel):
    reasoningText: Optional[ReasoningTextBlock] = None
    redactedContent: Optional[Blob] = None


class ToolSpecification(BaseValidatorModel):
    name: str
    inputSchema: ToolInputSchema
    description: Optional[str] = None


class AsyncInvokeSummary(BaseValidatorModel):
    invocationArn: str
    modelArn: str
    submitTime: datetime
    outputDataConfig: AsyncInvokeOutputDataConfig
    clientRequestToken: Optional[str] = None
    status: Optional[AsyncInvokeStatusType] = None
    failureMessage: Optional[str] = None
    lastModifiedTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetAsyncInvokeResponse(BaseValidatorModel):
    invocationArn: str
    modelArn: str
    clientRequestToken: str
    status: AsyncInvokeStatusType
    failureMessage: str
    submitTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    outputDataConfig: AsyncInvokeOutputDataConfig
    ResponseMetadata: ResponseMetadata


class StartAsyncInvokeRequest(BaseValidatorModel):
    modelId: str
    modelInput: Mapping[str, Any]
    outputDataConfig: AsyncInvokeOutputDataConfig
    clientRequestToken: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class ContentBlockDeltaEvent(BaseValidatorModel):
    delta: ContentBlockDelta
    contentBlockIndex: int


class ContentBlockStartEvent(BaseValidatorModel):
    start: ContentBlockStart
    contentBlockIndex: int


class GuardrailConverseImageBlockOutput(BaseValidatorModel):
    pass


class GuardrailConverseContentBlockOutput(BaseValidatorModel):
    text: Optional[GuardrailConverseTextBlockOutput] = None
    image: Optional[GuardrailConverseImageBlockOutput] = None


class GuardrailInvocationMetrics(BaseValidatorModel):
    guardrailProcessingLatency: Optional[int] = None
    usage: Optional[GuardrailUsage] = None
    guardrailCoverage: Optional[GuardrailCoverage] = None


class InvokeModelWithResponseStreamResponse(BaseValidatorModel):
    body: EventStream[ResponseStream]
    contentType: str
    performanceConfigLatency: PerformanceConfigLatencyType
    ResponseMetadata: ResponseMetadata


class Tool(BaseValidatorModel):
    toolSpec: Optional[ToolSpecification] = None


class ListAsyncInvokesResponse(BaseValidatorModel):
    asyncInvokeSummaries: List[AsyncInvokeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GuardrailImageBlock(BaseValidatorModel):
    pass


class GuardrailContentBlock(BaseValidatorModel):
    text: Optional[GuardrailTextBlock] = None
    image: Optional[GuardrailImageBlock] = None


class GuardrailAssessment(BaseValidatorModel):
    topicPolicy: Optional[GuardrailTopicPolicyAssessment] = None
    contentPolicy: Optional[GuardrailContentPolicyAssessment] = None
    wordPolicy: Optional[GuardrailWordPolicyAssessment] = None
    sensitiveInformationPolicy: Optional[GuardrailSensitiveInformationPolicyAssessment] = None
    contextualGroundingPolicy: Optional[GuardrailContextualGroundingPolicyAssessment] = None
    invocationMetrics: Optional[GuardrailInvocationMetrics] = None


class VideoBlockOutput(BaseValidatorModel):
    pass


class DocumentBlockOutput(BaseValidatorModel):
    pass


class ImageBlockOutput(BaseValidatorModel):
    pass


class ToolResultContentBlockOutput(BaseValidatorModel):
    json: Optional[Dict[str, Any]] = None
    text: Optional[str] = None
    image: Optional[ImageBlockOutput] = None
    document: Optional[DocumentBlockOutput] = None
    video: Optional[VideoBlockOutput] = None


class ToolChoice(BaseValidatorModel):
    pass


class ToolConfiguration(BaseValidatorModel):
    tools: Sequence[Tool]
    toolChoice: Optional[ToolChoice] = None


class ApplyGuardrailRequest(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str
    source: GuardrailContentSourceType
    content: Sequence[GuardrailContentBlock]


class ApplyGuardrailResponse(BaseValidatorModel):
    usage: GuardrailUsage
    action: GuardrailActionType
    outputs: List[GuardrailOutputContent]
    assessments: List[GuardrailAssessment]
    guardrailCoverage: GuardrailCoverage
    ResponseMetadata: ResponseMetadata


class GuardrailTraceAssessment(BaseValidatorModel):
    modelOutput: Optional[List[str]] = None
    inputAssessment: Optional[Dict[str, GuardrailAssessment]] = None
    outputAssessments: Optional[Dict[str, List[GuardrailAssessment]]] = None


class ToolResultBlockOutput(BaseValidatorModel):
    toolUseId: str
    content: List[ToolResultContentBlockOutput]
    status: Optional[ToolResultStatusType] = None


class GuardrailConverseTextBlockUnion(BaseValidatorModel):
    pass


class GuardrailConverseImageBlockUnion(BaseValidatorModel):
    pass


class GuardrailConverseContentBlock(BaseValidatorModel):
    text: Optional[GuardrailConverseTextBlockUnion] = None
    image: Optional[GuardrailConverseImageBlockUnion] = None


class ConverseStreamTrace(BaseValidatorModel):
    guardrail: Optional[GuardrailTraceAssessment] = None
    promptRouter: Optional[PromptRouterTrace] = None


class ConverseTrace(BaseValidatorModel):
    guardrail: Optional[GuardrailTraceAssessment] = None
    promptRouter: Optional[PromptRouterTrace] = None


class ToolUseBlockOutput(BaseValidatorModel):
    pass


class ContentBlockOutput(BaseValidatorModel):
    text: Optional[str] = None
    image: Optional[ImageBlockOutput] = None
    document: Optional[DocumentBlockOutput] = None
    video: Optional[VideoBlockOutput] = None
    toolUse: Optional[ToolUseBlockOutput] = None
    toolResult: Optional[ToolResultBlockOutput] = None
    guardContent: Optional[GuardrailConverseContentBlockOutput] = None
    reasoningContent: Optional[ReasoningContentBlockOutput] = None


class VideoBlockUnion(BaseValidatorModel):
    pass


class DocumentBlockUnion(BaseValidatorModel):
    pass


class ImageBlockUnion(BaseValidatorModel):
    pass


class ToolResultContentBlock(BaseValidatorModel):
    json: Optional[Mapping[str, Any]] = None
    text: Optional[str] = None
    image: Optional[ImageBlockUnion] = None
    document: Optional[DocumentBlockUnion] = None
    video: Optional[VideoBlockUnion] = None


class ConverseStreamMetadataEvent(BaseValidatorModel):
    usage: TokenUsage
    metrics: ConverseStreamMetrics
    trace: Optional[ConverseStreamTrace] = None
    performanceConfig: Optional[PerformanceConfiguration] = None


class MessageOutput(BaseValidatorModel):
    role: ConversationRoleType
    content: List[ContentBlockOutput]


class GuardrailConverseContentBlockUnion(BaseValidatorModel):
    pass


class SystemContentBlock(BaseValidatorModel):
    text: Optional[str] = None
    guardContent: Optional[GuardrailConverseContentBlockUnion] = None


class ConverseStreamOutput(BaseValidatorModel):
    messageStart: Optional[MessageStartEvent] = None
    contentBlockStart: Optional[ContentBlockStartEvent] = None
    contentBlockDelta: Optional[ContentBlockDeltaEvent] = None
    contentBlockStop: Optional[ContentBlockStopEvent] = None
    messageStop: Optional[MessageStopEvent] = None
    metadata: Optional[ConverseStreamMetadataEvent] = None
    internalServerException: Optional[InternalServerException] = None
    modelStreamErrorException: Optional[ModelStreamErrorException] = None
    validationException: Optional[ValidationException] = None
    throttlingException: Optional[ThrottlingException] = None
    serviceUnavailableException: Optional[ServiceUnavailableException] = None


class ConverseOutput(BaseValidatorModel):
    message: Optional[MessageOutput] = None


class ToolResultContentBlockUnion(BaseValidatorModel):
    pass


class ToolResultBlock(BaseValidatorModel):
    toolUseId: str
    content: Sequence[ToolResultContentBlockUnion]
    status: Optional[ToolResultStatusType] = None


class ConverseStreamResponse(BaseValidatorModel):
    stream: EventStream[ConverseStreamOutput]
    ResponseMetadata: ResponseMetadata


class ConverseResponse(BaseValidatorModel):
    output: ConverseOutput
    stopReason: StopReasonType
    usage: TokenUsage
    metrics: ConverseMetrics
    additionalModelResponseFields: Dict[str, Any]
    trace: ConverseTrace
    performanceConfig: PerformanceConfiguration
    ResponseMetadata: ResponseMetadata


class ReasoningContentBlockUnion(BaseValidatorModel):
    pass


class ToolResultBlockUnion(BaseValidatorModel):
    pass


class ToolUseBlockUnion(BaseValidatorModel):
    pass


class ContentBlock(BaseValidatorModel):
    text: Optional[str] = None
    image: Optional[ImageBlockUnion] = None
    document: Optional[DocumentBlockUnion] = None
    video: Optional[VideoBlockUnion] = None
    toolUse: Optional[ToolUseBlockUnion] = None
    toolResult: Optional[ToolResultBlockUnion] = None
    guardContent: Optional[GuardrailConverseContentBlockUnion] = None
    reasoningContent: Optional[ReasoningContentBlockUnion] = None


class ContentBlockUnion(BaseValidatorModel):
    pass


class Message(BaseValidatorModel):
    role: ConversationRoleType
    content: Sequence[ContentBlockUnion]


class MessageUnion(BaseValidatorModel):
    pass


class ConverseRequest(BaseValidatorModel):
    modelId: str
    messages: Optional[Sequence[MessageUnion]] = None
    system: Optional[Sequence[SystemContentBlock]] = None
    inferenceConfig: Optional[InferenceConfiguration] = None
    toolConfig: Optional[ToolConfiguration] = None
    guardrailConfig: Optional[GuardrailConfiguration] = None
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    promptVariables: Optional[Mapping[str, PromptVariableValues]] = None
    additionalModelResponseFieldPaths: Optional[Sequence[str]] = None
    requestMetadata: Optional[Mapping[str, str]] = None
    performanceConfig: Optional[PerformanceConfiguration] = None


class ConverseStreamRequest(BaseValidatorModel):
    modelId: str
    messages: Optional[Sequence[MessageUnion]] = None
    system: Optional[Sequence[SystemContentBlock]] = None
    inferenceConfig: Optional[InferenceConfiguration] = None
    toolConfig: Optional[ToolConfiguration] = None
    guardrailConfig: Optional[GuardrailStreamConfiguration] = None
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    promptVariables: Optional[Mapping[str, PromptVariableValues]] = None
    additionalModelResponseFieldPaths: Optional[Sequence[str]] = None
    requestMetadata: Optional[Mapping[str, str]] = None
    performanceConfig: Optional[PerformanceConfiguration] = None



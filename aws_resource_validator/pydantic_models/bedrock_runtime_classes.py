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

class GuardrailOutputContentTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class GuardrailUsageTypeDef(BaseValidatorModel):
    topicPolicyUnits: int
    contentPolicyUnits: int
    wordPolicyUnits: int
    sensitiveInformationPolicyUnits: int
    sensitiveInformationPolicyFreeUnits: int
    contextualGroundingPolicyUnits: int


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AsyncInvokeS3OutputDataConfigTypeDef(BaseValidatorModel):
    s3Uri: str
    kmsKeyId: Optional[str] = None
    bucketOwner: Optional[str] = None


class ReasoningContentBlockDeltaTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    redactedContent: Optional[bytes] = None
    signature: Optional[str] = None


class ToolUseBlockStartTypeDef(BaseValidatorModel):
    toolUseId: str
    name: str


class ContentBlockStopEventTypeDef(BaseValidatorModel):
    contentBlockIndex: int


class ConverseMetricsTypeDef(BaseValidatorModel):
    latencyMs: int


class GuardrailConfigurationTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str
    trace: Optional[GuardrailTraceType] = None


class InferenceConfigurationTypeDef(BaseValidatorModel):
    maxTokens: Optional[int] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None
    stopSequences: Optional[Sequence[str]] = None


class PerformanceConfigurationTypeDef(BaseValidatorModel):
    latency: Optional[PerformanceConfigLatencyType] = None


class PromptVariableValuesTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class TokenUsageTypeDef(BaseValidatorModel):
    inputTokens: int
    outputTokens: int
    totalTokens: int


class ConverseStreamMetricsTypeDef(BaseValidatorModel):
    latencyMs: int


class InternalServerExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class MessageStartEventTypeDef(BaseValidatorModel):
    role: ConversationRoleType


class MessageStopEventTypeDef(BaseValidatorModel):
    stopReason: StopReasonType
    additionalModelResponseFields: Optional[Dict[str, Any]] = None


class ModelStreamErrorExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    originalStatusCode: Optional[int] = None
    originalMessage: Optional[str] = None


class ServiceUnavailableExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class ThrottlingExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class ValidationExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class GuardrailStreamConfigurationTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str
    trace: Optional[GuardrailTraceType] = None
    streamProcessingMode: Optional[GuardrailStreamProcessingModeType] = None


class PromptRouterTraceTypeDef(BaseValidatorModel):
    invokedModelId: Optional[str] = None


class GetAsyncInvokeRequestTypeDef(BaseValidatorModel):
    invocationArn: str


class GuardrailTextBlockTypeDef(BaseValidatorModel):
    text: str
    qualifiers: Optional[Sequence[GuardrailContentQualifierType]] = None


class GuardrailConverseTextBlockOutputTypeDef(BaseValidatorModel):
    text: str
    qualifiers: Optional[List[GuardrailConverseContentQualifierType]] = None


class GuardrailConverseTextBlockTypeDef(BaseValidatorModel):
    text: str
    qualifiers: Optional[Sequence[GuardrailConverseContentQualifierType]] = None


class GuardrailImageCoverageTypeDef(BaseValidatorModel):
    guarded: Optional[int] = None
    total: Optional[int] = None


class GuardrailTextCharactersCoverageTypeDef(BaseValidatorModel):
    guarded: Optional[int] = None
    total: Optional[int] = None


class GuardrailCustomWordTypeDef(BaseValidatorModel):
    match: str
    action: Literal["BLOCKED"]


class GuardrailRegexFilterTypeDef(BaseValidatorModel):
    action: GuardrailSensitiveInformationPolicyActionType
    name: Optional[str] = None
    match: Optional[str] = None
    regex: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ModelTimeoutExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class ReasoningTextBlockTypeDef(BaseValidatorModel):
    text: str
    signature: Optional[str] = None


class S3LocationTypeDef(BaseValidatorModel):
    uri: str
    bucketOwner: Optional[str] = None


class SpecificToolChoiceTypeDef(BaseValidatorModel):
    name: str


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class ToolInputSchemaTypeDef(BaseValidatorModel):
    json: Optional[Mapping[str, Any]] = None


class InvokeModelResponseTypeDef(BaseValidatorModel):
    body: StreamingBody
    contentType: str
    performanceConfigLatency: PerformanceConfigLatencyType
    ResponseMetadata: ResponseMetadataTypeDef


class StartAsyncInvokeResponseTypeDef(BaseValidatorModel):
    invocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AsyncInvokeOutputDataConfigTypeDef(BaseValidatorModel):
    s3OutputDataConfig: Optional[AsyncInvokeS3OutputDataConfigTypeDef] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class InvokeModelRequestTypeDef(BaseValidatorModel):
    modelId: str
    body: Optional[BlobTypeDef] = None
    contentType: Optional[str] = None
    accept: Optional[str] = None
    trace: Optional[TraceType] = None
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None
    performanceConfigLatency: Optional[PerformanceConfigLatencyType] = None


class InvokeModelWithResponseStreamRequestTypeDef(BaseValidatorModel):
    modelId: str
    body: Optional[BlobTypeDef] = None
    contentType: Optional[str] = None
    accept: Optional[str] = None
    trace: Optional[TraceType] = None
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None
    performanceConfigLatency: Optional[PerformanceConfigLatencyType] = None


class ToolUseBlockDeltaTypeDef(BaseValidatorModel):
    pass


class ContentBlockDeltaTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    toolUse: Optional[ToolUseBlockDeltaTypeDef] = None
    reasoningContent: Optional[ReasoningContentBlockDeltaTypeDef] = None


class ContentBlockStartTypeDef(BaseValidatorModel):
    toolUse: Optional[ToolUseBlockStartTypeDef] = None


class GuardrailContentFilterTypeDef(BaseValidatorModel):
    pass


class GuardrailContentPolicyAssessmentTypeDef(BaseValidatorModel):
    filters: List[GuardrailContentFilterTypeDef]


class GuardrailContextualGroundingFilterTypeDef(BaseValidatorModel):
    pass


class GuardrailContextualGroundingPolicyAssessmentTypeDef(BaseValidatorModel):
    filters: Optional[List[GuardrailContextualGroundingFilterTypeDef]] = None


class GuardrailCoverageTypeDef(BaseValidatorModel):
    textCharacters: Optional[GuardrailTextCharactersCoverageTypeDef] = None
    images: Optional[GuardrailImageCoverageTypeDef] = None


class GuardrailManagedWordTypeDef(BaseValidatorModel):
    pass


class GuardrailWordPolicyAssessmentTypeDef(BaseValidatorModel):
    customWords: List[GuardrailCustomWordTypeDef]
    managedWordLists: List[GuardrailManagedWordTypeDef]


class GuardrailPiiEntityFilterTypeDef(BaseValidatorModel):
    pass


class GuardrailSensitiveInformationPolicyAssessmentTypeDef(BaseValidatorModel):
    piiEntities: List[GuardrailPiiEntityFilterTypeDef]
    regexes: List[GuardrailRegexFilterTypeDef]


class GuardrailTopicTypeDef(BaseValidatorModel):
    pass


class GuardrailTopicPolicyAssessmentTypeDef(BaseValidatorModel):
    topics: List[GuardrailTopicTypeDef]


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListAsyncInvokesRequestPaginateTypeDef(BaseValidatorModel):
    submitTimeAfter: Optional[TimestampTypeDef] = None
    submitTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[AsyncInvokeStatusType] = None
    sortBy: Optional[Literal["SubmissionTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAsyncInvokesRequestTypeDef(BaseValidatorModel):
    submitTimeAfter: Optional[TimestampTypeDef] = None
    submitTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[AsyncInvokeStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["SubmissionTime"]] = None
    sortOrder: Optional[SortOrderType] = None


class PayloadPartTypeDef(BaseValidatorModel):
    pass


class ResponseStreamTypeDef(BaseValidatorModel):
    chunk: Optional[PayloadPartTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    modelStreamErrorException: Optional[ModelStreamErrorExceptionTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    modelTimeoutException: Optional[ModelTimeoutExceptionTypeDef] = None
    serviceUnavailableException: Optional[ServiceUnavailableExceptionTypeDef] = None


class ReasoningContentBlockOutputTypeDef(BaseValidatorModel):
    reasoningText: Optional[ReasoningTextBlockTypeDef] = None
    redactedContent: Optional[bytes] = None


class ReasoningContentBlockTypeDef(BaseValidatorModel):
    reasoningText: Optional[ReasoningTextBlockTypeDef] = None
    redactedContent: Optional[BlobTypeDef] = None


class ToolSpecificationTypeDef(BaseValidatorModel):
    name: str
    inputSchema: ToolInputSchemaTypeDef
    description: Optional[str] = None


class AsyncInvokeSummaryTypeDef(BaseValidatorModel):
    invocationArn: str
    modelArn: str
    submitTime: datetime
    outputDataConfig: AsyncInvokeOutputDataConfigTypeDef
    clientRequestToken: Optional[str] = None
    status: Optional[AsyncInvokeStatusType] = None
    failureMessage: Optional[str] = None
    lastModifiedTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetAsyncInvokeResponseTypeDef(BaseValidatorModel):
    invocationArn: str
    modelArn: str
    clientRequestToken: str
    status: AsyncInvokeStatusType
    failureMessage: str
    submitTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    outputDataConfig: AsyncInvokeOutputDataConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartAsyncInvokeRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelInput: Mapping[str, Any]
    outputDataConfig: AsyncInvokeOutputDataConfigTypeDef
    clientRequestToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ContentBlockDeltaEventTypeDef(BaseValidatorModel):
    delta: ContentBlockDeltaTypeDef
    contentBlockIndex: int


class ContentBlockStartEventTypeDef(BaseValidatorModel):
    start: ContentBlockStartTypeDef
    contentBlockIndex: int


class GuardrailConverseImageBlockOutputTypeDef(BaseValidatorModel):
    pass


class GuardrailConverseContentBlockOutputTypeDef(BaseValidatorModel):
    text: Optional[GuardrailConverseTextBlockOutputTypeDef] = None
    image: Optional[GuardrailConverseImageBlockOutputTypeDef] = None


class GuardrailInvocationMetricsTypeDef(BaseValidatorModel):
    guardrailProcessingLatency: Optional[int] = None
    usage: Optional[GuardrailUsageTypeDef] = None
    guardrailCoverage: Optional[GuardrailCoverageTypeDef] = None


class InvokeModelWithResponseStreamResponseTypeDef(BaseValidatorModel):
    body: EventStream[ResponseStreamTypeDef]
    contentType: str
    performanceConfigLatency: PerformanceConfigLatencyType
    ResponseMetadata: ResponseMetadataTypeDef


class ToolTypeDef(BaseValidatorModel):
    toolSpec: Optional[ToolSpecificationTypeDef] = None


class ListAsyncInvokesResponseTypeDef(BaseValidatorModel):
    asyncInvokeSummaries: List[AsyncInvokeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GuardrailImageBlockTypeDef(BaseValidatorModel):
    pass


class GuardrailContentBlockTypeDef(BaseValidatorModel):
    text: Optional[GuardrailTextBlockTypeDef] = None
    image: Optional[GuardrailImageBlockTypeDef] = None


class GuardrailAssessmentTypeDef(BaseValidatorModel):
    topicPolicy: Optional[GuardrailTopicPolicyAssessmentTypeDef] = None
    contentPolicy: Optional[GuardrailContentPolicyAssessmentTypeDef] = None
    wordPolicy: Optional[GuardrailWordPolicyAssessmentTypeDef] = None
    sensitiveInformationPolicy: Optional[GuardrailSensitiveInformationPolicyAssessmentTypeDef] = None
    contextualGroundingPolicy: Optional[GuardrailContextualGroundingPolicyAssessmentTypeDef] = None
    invocationMetrics: Optional[GuardrailInvocationMetricsTypeDef] = None


class VideoBlockOutputTypeDef(BaseValidatorModel):
    pass


class DocumentBlockOutputTypeDef(BaseValidatorModel):
    pass


class ImageBlockOutputTypeDef(BaseValidatorModel):
    pass


class ToolResultContentBlockOutputTypeDef(BaseValidatorModel):
    json: Optional[Dict[str, Any]] = None
    text: Optional[str] = None
    image: Optional[ImageBlockOutputTypeDef] = None
    document: Optional[DocumentBlockOutputTypeDef] = None
    video: Optional[VideoBlockOutputTypeDef] = None


class ToolChoiceTypeDef(BaseValidatorModel):
    pass


class ToolConfigurationTypeDef(BaseValidatorModel):
    tools: Sequence[ToolTypeDef]
    toolChoice: Optional[ToolChoiceTypeDef] = None


class ApplyGuardrailRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str
    source: GuardrailContentSourceType
    content: Sequence[GuardrailContentBlockTypeDef]


class ApplyGuardrailResponseTypeDef(BaseValidatorModel):
    usage: GuardrailUsageTypeDef
    action: GuardrailActionType
    outputs: List[GuardrailOutputContentTypeDef]
    assessments: List[GuardrailAssessmentTypeDef]
    guardrailCoverage: GuardrailCoverageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GuardrailTraceAssessmentTypeDef(BaseValidatorModel):
    modelOutput: Optional[List[str]] = None
    inputAssessment: Optional[Dict[str, GuardrailAssessmentTypeDef]] = None
    outputAssessments: Optional[Dict[str, List[GuardrailAssessmentTypeDef]]] = None


class ToolResultBlockOutputTypeDef(BaseValidatorModel):
    toolUseId: str
    content: List[ToolResultContentBlockOutputTypeDef]
    status: Optional[ToolResultStatusType] = None


class GuardrailConverseTextBlockUnionTypeDef(BaseValidatorModel):
    pass


class GuardrailConverseImageBlockUnionTypeDef(BaseValidatorModel):
    pass


class GuardrailConverseContentBlockTypeDef(BaseValidatorModel):
    text: Optional[GuardrailConverseTextBlockUnionTypeDef] = None
    image: Optional[GuardrailConverseImageBlockUnionTypeDef] = None


class ConverseStreamTraceTypeDef(BaseValidatorModel):
    guardrail: Optional[GuardrailTraceAssessmentTypeDef] = None
    promptRouter: Optional[PromptRouterTraceTypeDef] = None


class ConverseTraceTypeDef(BaseValidatorModel):
    guardrail: Optional[GuardrailTraceAssessmentTypeDef] = None
    promptRouter: Optional[PromptRouterTraceTypeDef] = None


class ToolUseBlockOutputTypeDef(BaseValidatorModel):
    pass


class ContentBlockOutputTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    image: Optional[ImageBlockOutputTypeDef] = None
    document: Optional[DocumentBlockOutputTypeDef] = None
    video: Optional[VideoBlockOutputTypeDef] = None
    toolUse: Optional[ToolUseBlockOutputTypeDef] = None
    toolResult: Optional[ToolResultBlockOutputTypeDef] = None
    guardContent: Optional[GuardrailConverseContentBlockOutputTypeDef] = None
    reasoningContent: Optional[ReasoningContentBlockOutputTypeDef] = None


class VideoBlockUnionTypeDef(BaseValidatorModel):
    pass


class DocumentBlockUnionTypeDef(BaseValidatorModel):
    pass


class ImageBlockUnionTypeDef(BaseValidatorModel):
    pass


class ToolResultContentBlockTypeDef(BaseValidatorModel):
    json: Optional[Mapping[str, Any]] = None
    text: Optional[str] = None
    image: Optional[ImageBlockUnionTypeDef] = None
    document: Optional[DocumentBlockUnionTypeDef] = None
    video: Optional[VideoBlockUnionTypeDef] = None


class ConverseStreamMetadataEventTypeDef(BaseValidatorModel):
    usage: TokenUsageTypeDef
    metrics: ConverseStreamMetricsTypeDef
    trace: Optional[ConverseStreamTraceTypeDef] = None
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None


class MessageOutputTypeDef(BaseValidatorModel):
    role: ConversationRoleType
    content: List[ContentBlockOutputTypeDef]


class GuardrailConverseContentBlockUnionTypeDef(BaseValidatorModel):
    pass


class SystemContentBlockTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    guardContent: Optional[GuardrailConverseContentBlockUnionTypeDef] = None


class ConverseStreamOutputTypeDef(BaseValidatorModel):
    messageStart: Optional[MessageStartEventTypeDef] = None
    contentBlockStart: Optional[ContentBlockStartEventTypeDef] = None
    contentBlockDelta: Optional[ContentBlockDeltaEventTypeDef] = None
    contentBlockStop: Optional[ContentBlockStopEventTypeDef] = None
    messageStop: Optional[MessageStopEventTypeDef] = None
    metadata: Optional[ConverseStreamMetadataEventTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    modelStreamErrorException: Optional[ModelStreamErrorExceptionTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    serviceUnavailableException: Optional[ServiceUnavailableExceptionTypeDef] = None


class ConverseOutputTypeDef(BaseValidatorModel):
    message: Optional[MessageOutputTypeDef] = None


class ToolResultContentBlockUnionTypeDef(BaseValidatorModel):
    pass


class ToolResultBlockTypeDef(BaseValidatorModel):
    toolUseId: str
    content: Sequence[ToolResultContentBlockUnionTypeDef]
    status: Optional[ToolResultStatusType] = None


class ConverseStreamResponseTypeDef(BaseValidatorModel):
    stream: EventStream[ConverseStreamOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ConverseResponseTypeDef(BaseValidatorModel):
    output: ConverseOutputTypeDef
    stopReason: StopReasonType
    usage: TokenUsageTypeDef
    metrics: ConverseMetricsTypeDef
    additionalModelResponseFields: Dict[str, Any]
    trace: ConverseTraceTypeDef
    performanceConfig: PerformanceConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReasoningContentBlockUnionTypeDef(BaseValidatorModel):
    pass


class ToolResultBlockUnionTypeDef(BaseValidatorModel):
    pass


class ToolUseBlockUnionTypeDef(BaseValidatorModel):
    pass


class ContentBlockTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    image: Optional[ImageBlockUnionTypeDef] = None
    document: Optional[DocumentBlockUnionTypeDef] = None
    video: Optional[VideoBlockUnionTypeDef] = None
    toolUse: Optional[ToolUseBlockUnionTypeDef] = None
    toolResult: Optional[ToolResultBlockUnionTypeDef] = None
    guardContent: Optional[GuardrailConverseContentBlockUnionTypeDef] = None
    reasoningContent: Optional[ReasoningContentBlockUnionTypeDef] = None


class ContentBlockUnionTypeDef(BaseValidatorModel):
    pass


class MessageTypeDef(BaseValidatorModel):
    role: ConversationRoleType
    content: Sequence[ContentBlockUnionTypeDef]


class MessageUnionTypeDef(BaseValidatorModel):
    pass


class ConverseRequestTypeDef(BaseValidatorModel):
    modelId: str
    messages: Optional[Sequence[MessageUnionTypeDef]] = None
    system: Optional[Sequence[SystemContentBlockTypeDef]] = None
    inferenceConfig: Optional[InferenceConfigurationTypeDef] = None
    toolConfig: Optional[ToolConfigurationTypeDef] = None
    guardrailConfig: Optional[GuardrailConfigurationTypeDef] = None
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    promptVariables: Optional[Mapping[str, PromptVariableValuesTypeDef]] = None
    additionalModelResponseFieldPaths: Optional[Sequence[str]] = None
    requestMetadata: Optional[Mapping[str, str]] = None
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None


class ConverseStreamRequestTypeDef(BaseValidatorModel):
    modelId: str
    messages: Optional[Sequence[MessageUnionTypeDef]] = None
    system: Optional[Sequence[SystemContentBlockTypeDef]] = None
    inferenceConfig: Optional[InferenceConfigurationTypeDef] = None
    toolConfig: Optional[ToolConfigurationTypeDef] = None
    guardrailConfig: Optional[GuardrailStreamConfigurationTypeDef] = None
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    promptVariables: Optional[Mapping[str, PromptVariableValuesTypeDef]] = None
    additionalModelResponseFieldPaths: Optional[Sequence[str]] = None
    requestMetadata: Optional[Mapping[str, str]] = None
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None



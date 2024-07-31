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
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.bedrock_runtime_constants import *

class GuardrailOutputContentTypeDef(BaseModel):
    text: Optional[str] = None

class GuardrailUsageTypeDef(BaseModel):
    topicPolicyUnits: int
    contentPolicyUnits: int
    wordPolicyUnits: int
    sensitiveInformationPolicyUnits: int
    sensitiveInformationPolicyFreeUnits: int
    contextualGroundingPolicyUnits: int

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ToolUseBlockDeltaTypeDef(BaseModel):
    input: str

class ToolUseBlockOutputTypeDef(BaseModel):
    toolUseId: str
    name: str
    input: Dict[str, Any]

class ToolUseBlockStartTypeDef(BaseModel):
    toolUseId: str
    name: str

class ContentBlockStopEventTypeDef(BaseModel):
    contentBlockIndex: int

class ToolUseBlockTypeDef(BaseModel):
    toolUseId: str
    name: str
    input: Mapping[str, Any]

class ConverseMetricsTypeDef(BaseModel):
    latencyMs: int

class GuardrailConfigurationTypeDef(BaseModel):
    guardrailIdentifier: str
    guardrailVersion: str
    trace: Optional[GuardrailTraceType] = None

class InferenceConfigurationTypeDef(BaseModel):
    maxTokens: Optional[int] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None
    stopSequences: Optional[Sequence[str]] = None

class TokenUsageTypeDef(BaseModel):
    inputTokens: int
    outputTokens: int
    totalTokens: int

class ConverseStreamMetricsTypeDef(BaseModel):
    latencyMs: int

class InternalServerExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class MessageStartEventTypeDef(BaseModel):
    role: ConversationRoleType

class MessageStopEventTypeDef(BaseModel):
    stopReason: StopReasonType
    additionalModelResponseFields: Optional[Dict[str, Any]] = None

class ModelStreamErrorExceptionTypeDef(BaseModel):
    message: Optional[str] = None
    originalStatusCode: Optional[int] = None
    originalMessage: Optional[str] = None

class ThrottlingExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class ValidationExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class GuardrailStreamConfigurationTypeDef(BaseModel):
    guardrailIdentifier: str
    guardrailVersion: str
    trace: Optional[GuardrailTraceType] = None
    streamProcessingMode: Optional[GuardrailStreamProcessingModeType] = None

class DocumentSourceOutputTypeDef(BaseModel):
    bytes: Optional[bytes] = None

class GuardrailTextBlockTypeDef(BaseModel):
    text: str
    qualifiers: Optional[Sequence[GuardrailContentQualifierType]] = None

class GuardrailContentFilterTypeDef(BaseModel):
    type: GuardrailContentFilterTypeType
    confidence: GuardrailContentFilterConfidenceType
    action: Literal["BLOCKED"]

class GuardrailContextualGroundingFilterTypeDef(BaseModel):
    type: GuardrailContextualGroundingFilterTypeType
    threshold: float
    score: float
    action: GuardrailContextualGroundingPolicyActionType

class GuardrailConverseTextBlockOutputTypeDef(BaseModel):
    text: str
    qualifiers: Optional[List[GuardrailConverseContentQualifierType]] = None

class GuardrailConverseTextBlockTypeDef(BaseModel):
    text: str
    qualifiers: Optional[Sequence[GuardrailConverseContentQualifierType]] = None

class GuardrailCustomWordTypeDef(BaseModel):
    match: str
    action: Literal["BLOCKED"]

class GuardrailManagedWordTypeDef(BaseModel):
    match: str
    type: Literal["PROFANITY"]
    action: Literal["BLOCKED"]

class GuardrailPiiEntityFilterTypeDef(BaseModel):
    match: str
    type: GuardrailPiiEntityTypeType
    action: GuardrailSensitiveInformationPolicyActionType

class GuardrailRegexFilterTypeDef(BaseModel):
    action: GuardrailSensitiveInformationPolicyActionType
    name: Optional[str] = None
    match: Optional[str] = None
    regex: Optional[str] = None

class GuardrailTopicTypeDef(BaseModel):
    name: str
    type: Literal["DENY"]
    action: Literal["BLOCKED"]

class ImageSourceOutputTypeDef(BaseModel):
    bytes: Optional[bytes] = None

class ModelTimeoutExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class PayloadPartTypeDef(BaseModel):
    bytes: Optional[bytes] = None

class SpecificToolChoiceTypeDef(BaseModel):
    name: str

class ToolInputSchemaTypeDef(BaseModel):
    json: Optional[Mapping[str, Any]] = None

class InvokeModelResponseTypeDef(BaseModel):
    body: StreamingBody
    contentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentSourceTypeDef(BaseModel):
    bytes: Optional[BlobTypeDef] = None

class ImageSourceTypeDef(BaseModel):
    bytes: Optional[BlobTypeDef] = None

class InvokeModelRequestRequestTypeDef(BaseModel):
    body: BlobTypeDef
    modelId: str
    contentType: Optional[str] = None
    accept: Optional[str] = None
    trace: Optional[TraceType] = None
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None

class InvokeModelWithResponseStreamRequestRequestTypeDef(BaseModel):
    body: BlobTypeDef
    modelId: str
    contentType: Optional[str] = None
    accept: Optional[str] = None
    trace: Optional[TraceType] = None
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None

class ContentBlockDeltaTypeDef(BaseModel):
    text: Optional[str] = None
    toolUse: Optional[ToolUseBlockDeltaTypeDef] = None

class ContentBlockStartTypeDef(BaseModel):
    toolUse: Optional[ToolUseBlockStartTypeDef] = None

class DocumentBlockOutputTypeDef(BaseModel):
    format: DocumentFormatType
    name: str
    source: DocumentSourceOutputTypeDef

class GuardrailContentBlockTypeDef(BaseModel):
    text: Optional[GuardrailTextBlockTypeDef] = None

class GuardrailContentPolicyAssessmentTypeDef(BaseModel):
    filters: List[GuardrailContentFilterTypeDef]

class GuardrailContextualGroundingPolicyAssessmentTypeDef(BaseModel):
    filters: Optional[List[GuardrailContextualGroundingFilterTypeDef]] = None

class GuardrailConverseContentBlockOutputTypeDef(BaseModel):
    text: Optional[GuardrailConverseTextBlockOutputTypeDef] = None

class GuardrailConverseContentBlockTypeDef(BaseModel):
    text: Optional[GuardrailConverseTextBlockTypeDef] = None

class GuardrailWordPolicyAssessmentTypeDef(BaseModel):
    customWords: List[GuardrailCustomWordTypeDef]
    managedWordLists: List[GuardrailManagedWordTypeDef]

class GuardrailSensitiveInformationPolicyAssessmentTypeDef(BaseModel):
    piiEntities: List[GuardrailPiiEntityFilterTypeDef]
    regexes: List[GuardrailRegexFilterTypeDef]

class GuardrailTopicPolicyAssessmentTypeDef(BaseModel):
    topics: List[GuardrailTopicTypeDef]

class ImageBlockOutputTypeDef(BaseModel):
    format: ImageFormatType
    source: ImageSourceOutputTypeDef

class ResponseStreamTypeDef(BaseModel):
    chunk: Optional[PayloadPartTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    modelStreamErrorException: Optional[ModelStreamErrorExceptionTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    modelTimeoutException: Optional[ModelTimeoutExceptionTypeDef] = None

class ToolChoiceTypeDef(BaseModel):
    auto: Optional[Mapping[str, Any]] = None
    any: Optional[Mapping[str, Any]] = None
    tool: Optional[SpecificToolChoiceTypeDef] = None

class ToolSpecificationTypeDef(BaseModel):
    name: str
    inputSchema: ToolInputSchemaTypeDef
    description: Optional[str] = None

class DocumentBlockTypeDef(BaseModel):
    format: DocumentFormatType
    name: str
    source: DocumentSourceTypeDef

class ImageBlockTypeDef(BaseModel):
    format: ImageFormatType
    source: ImageSourceTypeDef

class ContentBlockDeltaEventTypeDef(BaseModel):
    delta: ContentBlockDeltaTypeDef
    contentBlockIndex: int

class ContentBlockStartEventTypeDef(BaseModel):
    start: ContentBlockStartTypeDef
    contentBlockIndex: int

class ApplyGuardrailRequestRequestTypeDef(BaseModel):
    guardrailIdentifier: str
    guardrailVersion: str
    source: GuardrailContentSourceType
    content: Sequence[GuardrailContentBlockTypeDef]

class SystemContentBlockTypeDef(BaseModel):
    text: Optional[str] = None
    guardContent: Optional[GuardrailConverseContentBlockTypeDef] = None

class GuardrailAssessmentTypeDef(BaseModel):
    topicPolicy: Optional[GuardrailTopicPolicyAssessmentTypeDef] = None
    contentPolicy: Optional[GuardrailContentPolicyAssessmentTypeDef] = None
    wordPolicy: Optional[GuardrailWordPolicyAssessmentTypeDef] = None
    sensitiveInformationPolicy: Optional[       GuardrailSensitiveInformationPolicyAssessmentTypeDef     ] = None
    contextualGroundingPolicy: Optional[       GuardrailContextualGroundingPolicyAssessmentTypeDef     ] = None

class ToolResultContentBlockOutputTypeDef(BaseModel):
    json: Optional[Dict[str, Any]] = None
    text: Optional[str] = None
    image: Optional[ImageBlockOutputTypeDef] = None
    document: Optional[DocumentBlockOutputTypeDef] = None

class InvokeModelWithResponseStreamResponseTypeDef(BaseModel):
    body: "EventStream[ResponseStreamTypeDef]"
    contentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class ToolTypeDef(BaseModel):
    toolSpec: Optional[ToolSpecificationTypeDef] = None

class ToolResultContentBlockTypeDef(BaseModel):
    json: Optional[Mapping[str, Any]] = None
    text: Optional[str] = None
    image: Optional[ImageBlockTypeDef] = None
    document: Optional[DocumentBlockTypeDef] = None

class ApplyGuardrailResponseTypeDef(BaseModel):
    usage: GuardrailUsageTypeDef
    action: GuardrailActionType
    outputs: List[GuardrailOutputContentTypeDef]
    assessments: List[GuardrailAssessmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GuardrailTraceAssessmentTypeDef(BaseModel):
    modelOutput: Optional[List[str]] = None
    inputAssessment: Optional[Dict[str, GuardrailAssessmentTypeDef]] = None
    outputAssessments: Optional[Dict[str, List[GuardrailAssessmentTypeDef]]] = None

class ToolResultBlockOutputTypeDef(BaseModel):
    toolUseId: str
    content: List[ToolResultContentBlockOutputTypeDef]
    status: Optional[ToolResultStatusType] = None

class ToolConfigurationTypeDef(BaseModel):
    tools: Sequence[ToolTypeDef]
    toolChoice: Optional[ToolChoiceTypeDef] = None

class ToolResultBlockTypeDef(BaseModel):
    toolUseId: str
    content: Sequence[ToolResultContentBlockTypeDef]
    status: Optional[ToolResultStatusType] = None

class ConverseStreamTraceTypeDef(BaseModel):
    guardrail: Optional[GuardrailTraceAssessmentTypeDef] = None

class ConverseTraceTypeDef(BaseModel):
    guardrail: Optional[GuardrailTraceAssessmentTypeDef] = None

class ContentBlockOutputTypeDef(BaseModel):
    text: Optional[str] = None
    image: Optional[ImageBlockOutputTypeDef] = None
    document: Optional[DocumentBlockOutputTypeDef] = None
    toolUse: Optional[ToolUseBlockOutputTypeDef] = None
    toolResult: Optional[ToolResultBlockOutputTypeDef] = None
    guardContent: Optional[GuardrailConverseContentBlockOutputTypeDef] = None

class ContentBlockTypeDef(BaseModel):
    text: Optional[str] = None
    image: Optional[ImageBlockTypeDef] = None
    document: Optional[DocumentBlockTypeDef] = None
    toolUse: Optional[ToolUseBlockTypeDef] = None
    toolResult: Optional[ToolResultBlockTypeDef] = None
    guardContent: Optional[GuardrailConverseContentBlockTypeDef] = None

class ConverseStreamMetadataEventTypeDef(BaseModel):
    usage: TokenUsageTypeDef
    metrics: ConverseStreamMetricsTypeDef
    trace: Optional[ConverseStreamTraceTypeDef] = None

class MessageOutputTypeDef(BaseModel):
    role: ConversationRoleType
    content: List[ContentBlockOutputTypeDef]

class MessageTypeDef(BaseModel):
    role: ConversationRoleType
    content: Sequence[ContentBlockTypeDef]

class ConverseStreamOutputTypeDef(BaseModel):
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

class ConverseOutputTypeDef(BaseModel):
    message: Optional[MessageOutputTypeDef] = None

class ConverseStreamResponseTypeDef(BaseModel):
    stream: "EventStream[ConverseStreamOutputTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

class ConverseResponseTypeDef(BaseModel):
    output: ConverseOutputTypeDef
    stopReason: StopReasonType
    usage: TokenUsageTypeDef
    metrics: ConverseMetricsTypeDef
    additionalModelResponseFields: Dict[str, Any]
    trace: ConverseTraceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConverseRequestRequestTypeDef(BaseModel):
    modelId: str
    messages: Sequence[MessageUnionTypeDef]
    system: Optional[Sequence[SystemContentBlockTypeDef]] = None
    inferenceConfig: Optional[InferenceConfigurationTypeDef] = None
    toolConfig: Optional[ToolConfigurationTypeDef] = None
    guardrailConfig: Optional[GuardrailConfigurationTypeDef] = None
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    additionalModelResponseFieldPaths: Optional[Sequence[str]] = None

class ConverseStreamRequestRequestTypeDef(BaseModel):
    modelId: str
    messages: Sequence[MessageUnionTypeDef]
    system: Optional[Sequence[SystemContentBlockTypeDef]] = None
    inferenceConfig: Optional[InferenceConfigurationTypeDef] = None
    toolConfig: Optional[ToolConfigurationTypeDef] = None
    guardrailConfig: Optional[GuardrailStreamConfigurationTypeDef] = None
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    additionalModelResponseFieldPaths: Optional[Sequence[str]] = None


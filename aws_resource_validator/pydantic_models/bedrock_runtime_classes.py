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
from botocore.response import StreamingBody
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

class ToolUseBlockDeltaTypeDef(BaseValidatorModel):
    input: str

class ToolUseBlockOutputTypeDef(BaseValidatorModel):
    toolUseId: str
    name: str
    input: Dict[str, Any]

class ToolUseBlockStartTypeDef(BaseValidatorModel):
    toolUseId: str
    name: str

class ContentBlockStopEventTypeDef(BaseValidatorModel):
    contentBlockIndex: int

class ToolUseBlockTypeDef(BaseValidatorModel):
    toolUseId: str
    name: str
    input: Mapping[str, Any]

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

class ThrottlingExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class ValidationExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class GuardrailStreamConfigurationTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str
    trace: Optional[GuardrailTraceType] = None
    streamProcessingMode: Optional[GuardrailStreamProcessingModeType] = None

class DocumentSourceOutputTypeDef(BaseValidatorModel):
    bytes: Optional[bytes] = None

class GuardrailTextBlockTypeDef(BaseValidatorModel):
    text: str
    qualifiers: Optional[Sequence[GuardrailContentQualifierType]] = None

class GuardrailContentFilterTypeDef(BaseValidatorModel):
    type: GuardrailContentFilterTypeType
    confidence: GuardrailContentFilterConfidenceType
    action: Literal["BLOCKED"]

class GuardrailContextualGroundingFilterTypeDef(BaseValidatorModel):
    type: GuardrailContextualGroundingFilterTypeType
    threshold: float
    score: float
    action: GuardrailContextualGroundingPolicyActionType

class GuardrailConverseTextBlockOutputTypeDef(BaseValidatorModel):
    text: str
    qualifiers: Optional[List[GuardrailConverseContentQualifierType]] = None

class GuardrailConverseTextBlockTypeDef(BaseValidatorModel):
    text: str
    qualifiers: Optional[Sequence[GuardrailConverseContentQualifierType]] = None

class GuardrailCustomWordTypeDef(BaseValidatorModel):
    match: str
    action: Literal["BLOCKED"]

class GuardrailManagedWordTypeDef(BaseValidatorModel):
    match: str
    type: Literal["PROFANITY"]
    action: Literal["BLOCKED"]

class GuardrailPiiEntityFilterTypeDef(BaseValidatorModel):
    match: str
    type: GuardrailPiiEntityTypeType
    action: GuardrailSensitiveInformationPolicyActionType

class GuardrailRegexFilterTypeDef(BaseValidatorModel):
    action: GuardrailSensitiveInformationPolicyActionType
    name: Optional[str] = None
    match: Optional[str] = None
    regex: Optional[str] = None

class GuardrailTopicTypeDef(BaseValidatorModel):
    name: str
    type: Literal["DENY"]
    action: Literal["BLOCKED"]

class ImageSourceOutputTypeDef(BaseValidatorModel):
    bytes: Optional[bytes] = None

class ModelTimeoutExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class PayloadPartTypeDef(BaseValidatorModel):
    bytes: Optional[bytes] = None

class SpecificToolChoiceTypeDef(BaseValidatorModel):
    name: str

class ToolInputSchemaTypeDef(BaseValidatorModel):
    json: Optional[Mapping[str, Any]] = None

class InvokeModelResponseTypeDef(BaseValidatorModel):
    body: StreamingBody
    contentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentSourceTypeDef(BaseValidatorModel):
    bytes: Optional[BlobTypeDef] = None

class ImageSourceTypeDef(BaseValidatorModel):
    bytes: Optional[BlobTypeDef] = None

class InvokeModelRequestRequestTypeDef(BaseValidatorModel):
    body: BlobTypeDef
    modelId: str
    contentType: Optional[str] = None
    accept: Optional[str] = None
    trace: Optional[TraceType] = None
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None

class InvokeModelWithResponseStreamRequestRequestTypeDef(BaseValidatorModel):
    body: BlobTypeDef
    modelId: str
    contentType: Optional[str] = None
    accept: Optional[str] = None
    trace: Optional[TraceType] = None
    guardrailIdentifier: Optional[str] = None
    guardrailVersion: Optional[str] = None

class ContentBlockDeltaTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    toolUse: Optional[ToolUseBlockDeltaTypeDef] = None

class ContentBlockStartTypeDef(BaseValidatorModel):
    toolUse: Optional[ToolUseBlockStartTypeDef] = None

class DocumentBlockOutputTypeDef(BaseValidatorModel):
    format: DocumentFormatType
    name: str
    source: DocumentSourceOutputTypeDef

class GuardrailContentBlockTypeDef(BaseValidatorModel):
    text: Optional[GuardrailTextBlockTypeDef] = None

class GuardrailContentPolicyAssessmentTypeDef(BaseValidatorModel):
    filters: List[GuardrailContentFilterTypeDef]

class GuardrailContextualGroundingPolicyAssessmentTypeDef(BaseValidatorModel):
    filters: Optional[List[GuardrailContextualGroundingFilterTypeDef]] = None

class GuardrailConverseContentBlockOutputTypeDef(BaseValidatorModel):
    text: Optional[GuardrailConverseTextBlockOutputTypeDef] = None

class GuardrailConverseContentBlockTypeDef(BaseValidatorModel):
    text: Optional[GuardrailConverseTextBlockTypeDef] = None

class GuardrailWordPolicyAssessmentTypeDef(BaseValidatorModel):
    customWords: List[GuardrailCustomWordTypeDef]
    managedWordLists: List[GuardrailManagedWordTypeDef]

class GuardrailSensitiveInformationPolicyAssessmentTypeDef(BaseValidatorModel):
    piiEntities: List[GuardrailPiiEntityFilterTypeDef]
    regexes: List[GuardrailRegexFilterTypeDef]

class GuardrailTopicPolicyAssessmentTypeDef(BaseValidatorModel):
    topics: List[GuardrailTopicTypeDef]

class ImageBlockOutputTypeDef(BaseValidatorModel):
    format: ImageFormatType
    source: ImageSourceOutputTypeDef

class ResponseStreamTypeDef(BaseValidatorModel):
    chunk: Optional[PayloadPartTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    modelStreamErrorException: Optional[ModelStreamErrorExceptionTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    modelTimeoutException: Optional[ModelTimeoutExceptionTypeDef] = None

class ToolChoiceTypeDef(BaseValidatorModel):
    auto: Optional[Mapping[str, Any]] = None
    any: Optional[Mapping[str, Any]] = None
    tool: Optional[SpecificToolChoiceTypeDef] = None

class ToolSpecificationTypeDef(BaseValidatorModel):
    name: str
    inputSchema: ToolInputSchemaTypeDef
    description: Optional[str] = None

class DocumentBlockTypeDef(BaseValidatorModel):
    format: DocumentFormatType
    name: str
    source: DocumentSourceTypeDef

class ImageBlockTypeDef(BaseValidatorModel):
    format: ImageFormatType
    source: ImageSourceTypeDef

class ContentBlockDeltaEventTypeDef(BaseValidatorModel):
    delta: ContentBlockDeltaTypeDef
    contentBlockIndex: int

class ContentBlockStartEventTypeDef(BaseValidatorModel):
    start: ContentBlockStartTypeDef
    contentBlockIndex: int

class ApplyGuardrailRequestRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: str
    source: GuardrailContentSourceType
    content: Sequence[GuardrailContentBlockTypeDef]

class SystemContentBlockTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    guardContent: Optional[GuardrailConverseContentBlockTypeDef] = None

class GuardrailAssessmentTypeDef(BaseValidatorModel):
    topicPolicy: Optional[GuardrailTopicPolicyAssessmentTypeDef] = None
    contentPolicy: Optional[GuardrailContentPolicyAssessmentTypeDef] = None
    wordPolicy: Optional[GuardrailWordPolicyAssessmentTypeDef] = None
    sensitiveInformationPolicy: Optional[       GuardrailSensitiveInformationPolicyAssessmentTypeDef     ] = None
    contextualGroundingPolicy: Optional[       GuardrailContextualGroundingPolicyAssessmentTypeDef     ] = None

class ToolResultContentBlockOutputTypeDef(BaseValidatorModel):
    json: Optional[Dict[str, Any]] = None
    text: Optional[str] = None
    image: Optional[ImageBlockOutputTypeDef] = None
    document: Optional[DocumentBlockOutputTypeDef] = None

class InvokeModelWithResponseStreamResponseTypeDef(BaseValidatorModel):
    body: "EventStream[ResponseStreamTypeDef]"
    contentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class ToolTypeDef(BaseValidatorModel):
    toolSpec: Optional[ToolSpecificationTypeDef] = None

class ToolResultContentBlockTypeDef(BaseValidatorModel):
    json: Optional[Mapping[str, Any]] = None
    text: Optional[str] = None
    image: Optional[ImageBlockTypeDef] = None
    document: Optional[DocumentBlockTypeDef] = None

class ApplyGuardrailResponseTypeDef(BaseValidatorModel):
    usage: GuardrailUsageTypeDef
    action: GuardrailActionType
    outputs: List[GuardrailOutputContentTypeDef]
    assessments: List[GuardrailAssessmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GuardrailTraceAssessmentTypeDef(BaseValidatorModel):
    modelOutput: Optional[List[str]] = None
    inputAssessment: Optional[Dict[str, GuardrailAssessmentTypeDef]] = None
    outputAssessments: Optional[Dict[str, List[GuardrailAssessmentTypeDef]]] = None

class ToolResultBlockOutputTypeDef(BaseValidatorModel):
    toolUseId: str
    content: List[ToolResultContentBlockOutputTypeDef]
    status: Optional[ToolResultStatusType] = None

class ToolConfigurationTypeDef(BaseValidatorModel):
    tools: Sequence[ToolTypeDef]
    toolChoice: Optional[ToolChoiceTypeDef] = None

class ToolResultBlockTypeDef(BaseValidatorModel):
    toolUseId: str
    content: Sequence[ToolResultContentBlockTypeDef]
    status: Optional[ToolResultStatusType] = None

class ConverseStreamTraceTypeDef(BaseValidatorModel):
    guardrail: Optional[GuardrailTraceAssessmentTypeDef] = None

class ConverseTraceTypeDef(BaseValidatorModel):
    guardrail: Optional[GuardrailTraceAssessmentTypeDef] = None

class ContentBlockOutputTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    image: Optional[ImageBlockOutputTypeDef] = None
    document: Optional[DocumentBlockOutputTypeDef] = None
    toolUse: Optional[ToolUseBlockOutputTypeDef] = None
    toolResult: Optional[ToolResultBlockOutputTypeDef] = None
    guardContent: Optional[GuardrailConverseContentBlockOutputTypeDef] = None

class ContentBlockTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    image: Optional[ImageBlockTypeDef] = None
    document: Optional[DocumentBlockTypeDef] = None
    toolUse: Optional[ToolUseBlockTypeDef] = None
    toolResult: Optional[ToolResultBlockTypeDef] = None
    guardContent: Optional[GuardrailConverseContentBlockTypeDef] = None

class ConverseStreamMetadataEventTypeDef(BaseValidatorModel):
    usage: TokenUsageTypeDef
    metrics: ConverseStreamMetricsTypeDef
    trace: Optional[ConverseStreamTraceTypeDef] = None

class MessageOutputTypeDef(BaseValidatorModel):
    role: ConversationRoleType
    content: List[ContentBlockOutputTypeDef]

class MessageTypeDef(BaseValidatorModel):
    role: ConversationRoleType
    content: Sequence[ContentBlockTypeDef]

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

class ConverseOutputTypeDef(BaseValidatorModel):
    message: Optional[MessageOutputTypeDef] = None

class ConverseStreamResponseTypeDef(BaseValidatorModel):
    stream: "EventStream[ConverseStreamOutputTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

class ConverseResponseTypeDef(BaseValidatorModel):
    output: ConverseOutputTypeDef
    stopReason: StopReasonType
    usage: TokenUsageTypeDef
    metrics: ConverseMetricsTypeDef
    additionalModelResponseFields: Dict[str, Any]
    trace: ConverseTraceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConverseRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    messages: Sequence[MessageUnionTypeDef]
    system: Optional[Sequence[SystemContentBlockTypeDef]] = None
    inferenceConfig: Optional[InferenceConfigurationTypeDef] = None
    toolConfig: Optional[ToolConfigurationTypeDef] = None
    guardrailConfig: Optional[GuardrailConfigurationTypeDef] = None
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    additionalModelResponseFieldPaths: Optional[Sequence[str]] = None

class ConverseStreamRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    messages: Sequence[MessageUnionTypeDef]
    system: Optional[Sequence[SystemContentBlockTypeDef]] = None
    inferenceConfig: Optional[InferenceConfigurationTypeDef] = None
    toolConfig: Optional[ToolConfigurationTypeDef] = None
    guardrailConfig: Optional[GuardrailStreamConfigurationTypeDef] = None
    additionalModelRequestFields: Optional[Mapping[str, Any]] = None
    additionalModelResponseFieldPaths: Optional[Sequence[str]] = None


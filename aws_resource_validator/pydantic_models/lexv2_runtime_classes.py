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
from aws_resource_validator.pydantic_models.lexv2_runtime_constants import *

class AccessDeniedException(BaseValidatorModel):
    message: str


class ActiveContextTimeToLive(BaseValidatorModel):
    timeToLiveInSeconds: int
    turnsToLive: int


class AudioResponseEvent(BaseValidatorModel):
    audioChunk: Optional[bytes] = None
    contentType: Optional[str] = None
    eventId: Optional[str] = None


class BadGatewayException(BaseValidatorModel):
    message: str


class Button(BaseValidatorModel):
    text: str
    value: str


class ConfidenceScore(BaseValidatorModel):
    score: Optional[float] = None


class ConflictException(BaseValidatorModel):
    message: str


class DTMFInputEvent(BaseValidatorModel):
    inputCharacter: str
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class DeleteSessionRequest(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DependencyFailedException(BaseValidatorModel):
    message: str


class ElicitSubSlotOutput(BaseValidatorModel):
    name: str
    subSlotToElicit: Optional[Dict[str, Any]] = None


class DisconnectionEvent(BaseValidatorModel):
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class ElicitSubSlot(BaseValidatorModel):
    name: str
    subSlotToElicit: Optional[Mapping[str, Any]] = None


class GetSessionRequest(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str


class HeartbeatEvent(BaseValidatorModel):
    eventId: Optional[str] = None


class RecognizedBotMember(BaseValidatorModel):
    botId: str
    botName: Optional[str] = None


class InternalServerException(BaseValidatorModel):
    message: str


class PlaybackCompletionEvent(BaseValidatorModel):
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class PlaybackInterruptionEvent(BaseValidatorModel):
    eventReason: Optional[PlaybackInterruptionReasonType] = None
    causedByEventId: Optional[str] = None
    eventId: Optional[str] = None


class ResourceNotFoundException(BaseValidatorModel):
    message: str


class RuntimeHintValue(BaseValidatorModel):
    phrase: str


class SentimentScore(BaseValidatorModel):
    positive: Optional[float] = None
    negative: Optional[float] = None
    neutral: Optional[float] = None
    mixed: Optional[float] = None


class ValueOutput(BaseValidatorModel):
    interpretedValue: str
    originalValue: Optional[str] = None
    resolvedValues: Optional[List[str]] = None


class TextInputEvent(BaseValidatorModel):
    text: str
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class ThrottlingException(BaseValidatorModel):
    message: str


class TranscriptEvent(BaseValidatorModel):
    transcript: Optional[str] = None
    eventId: Optional[str] = None


class ValidationException(BaseValidatorModel):
    message: str


class Value(BaseValidatorModel):
    interpretedValue: str
    originalValue: Optional[str] = None
    resolvedValues: Optional[Sequence[str]] = None


class ActiveContextOutput(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLive
    contextAttributes: Dict[str, str]


class ActiveContext(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLive
    contextAttributes: Mapping[str, str]


class Blob(BaseValidatorModel):
    pass


class AudioInputEvent(BaseValidatorModel):
    contentType: str
    audioChunk: Optional[Blob] = None
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class RecognizeUtteranceRequest(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    requestContentType: str
    sessionState: Optional[str] = None
    requestAttributes: Optional[str] = None
    responseContentType: Optional[str] = None
    inputStream: Optional[Blob] = None


class ImageResponseCardOutput(BaseValidatorModel):
    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[List[Button]] = None


class ImageResponseCard(BaseValidatorModel):
    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[Sequence[Button]] = None


class DeleteSessionResponse(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    ResponseMetadata: ResponseMetadata


class PutSessionResponse(BaseValidatorModel):
    contentType: str
    messages: str
    sessionState: str
    requestAttributes: str
    sessionId: str
    audioStream: StreamingBody
    ResponseMetadata: ResponseMetadata


class RecognizeUtteranceResponse(BaseValidatorModel):
    inputMode: str
    contentType: str
    messages: str
    interpretations: str
    sessionState: str
    requestAttributes: str
    sessionId: str
    inputTranscript: str
    audioStream: StreamingBody
    recognizedBotMember: str
    ResponseMetadata: ResponseMetadata


class RuntimeHintDetailsOutput(BaseValidatorModel):
    runtimeHintValues: Optional[List[RuntimeHintValue]] = None
    subSlotHints: Optional[Dict[str, Dict[str, Any]]] = None


class RuntimeHintDetails(BaseValidatorModel):
    runtimeHintValues: Optional[Sequence[RuntimeHintValue]] = None
    subSlotHints: Optional[Mapping[str, Mapping[str, Any]]] = None


class SentimentResponse(BaseValidatorModel):
    sentiment: Optional[SentimentTypeType] = None
    sentimentScore: Optional[SentimentScore] = None


class SlotOutput(BaseValidatorModel):
    value: Optional[ValueOutput] = None
    shape: Optional[ShapeType] = None
    values: Optional[List[Dict[str, Any]]] = None
    subSlots: Optional[Dict[str, Dict[str, Any]]] = None


class MessageOutput(BaseValidatorModel):
    contentType: MessageContentTypeType
    content: Optional[str] = None
    imageResponseCard: Optional[ImageResponseCardOutput] = None


class RuntimeHintsOutput(BaseValidatorModel):
    slotHints: Optional[Dict[str, Dict[str, RuntimeHintDetailsOutput]]] = None


class IntentOutput(BaseValidatorModel):
    name: str
    slots: Optional[Dict[str, SlotOutput]] = None
    state: Optional[IntentStateType] = None
    confirmationState: Optional[ConfirmationStateType] = None


class ValueUnion(BaseValidatorModel):
    pass


class Slot(BaseValidatorModel):
    value: Optional[ValueUnion] = None
    shape: Optional[ShapeType] = None
    values: Optional[Sequence[Mapping[str, Any]]] = None
    subSlots: Optional[Mapping[str, Mapping[str, Any]]] = None


class TextResponseEvent(BaseValidatorModel):
    messages: Optional[List[MessageOutput]] = None
    eventId: Optional[str] = None


class ImageResponseCardUnion(BaseValidatorModel):
    pass


class Message(BaseValidatorModel):
    contentType: MessageContentTypeType
    content: Optional[str] = None
    imageResponseCard: Optional[ImageResponseCardUnion] = None


class RuntimeHintDetailsUnion(BaseValidatorModel):
    pass


class RuntimeHints(BaseValidatorModel):
    slotHints: Optional[Mapping[str, Mapping[str, RuntimeHintDetailsUnion]]] = None


class Interpretation(BaseValidatorModel):
    nluConfidence: Optional[ConfidenceScore] = None
    sentimentResponse: Optional[SentimentResponse] = None
    intent: Optional[IntentOutput] = None
    interpretationSource: Optional[InterpretationSourceType] = None


class DialogActionOutput(BaseValidatorModel):
    pass


class SessionStateOutput(BaseValidatorModel):
    dialogAction: Optional[DialogActionOutput] = None
    intent: Optional[IntentOutput] = None
    activeContexts: Optional[List[ActiveContextOutput]] = None
    sessionAttributes: Optional[Dict[str, str]] = None
    originatingRequestId: Optional[str] = None
    runtimeHints: Optional[RuntimeHintsOutput] = None


class GetSessionResponse(BaseValidatorModel):
    sessionId: str
    messages: List[MessageOutput]
    interpretations: List[Interpretation]
    sessionState: SessionStateOutput
    ResponseMetadata: ResponseMetadata


class IntentResultEvent(BaseValidatorModel):
    inputMode: Optional[InputModeType] = None
    interpretations: Optional[List[Interpretation]] = None
    sessionState: Optional[SessionStateOutput] = None
    requestAttributes: Optional[Dict[str, str]] = None
    sessionId: Optional[str] = None
    eventId: Optional[str] = None
    recognizedBotMember: Optional[RecognizedBotMember] = None


class RecognizeTextResponse(BaseValidatorModel):
    messages: List[MessageOutput]
    sessionState: SessionStateOutput
    interpretations: List[Interpretation]
    requestAttributes: Dict[str, str]
    sessionId: str
    recognizedBotMember: RecognizedBotMember
    ResponseMetadata: ResponseMetadata


class SlotUnion(BaseValidatorModel):
    pass


class Intent(BaseValidatorModel):
    name: str
    slots: Optional[Mapping[str, SlotUnion]] = None
    state: Optional[IntentStateType] = None
    confirmationState: Optional[ConfirmationStateType] = None


class StartConversationResponseEventStream(BaseValidatorModel):
    PlaybackInterruptionEvent: Optional[PlaybackInterruptionEvent] = None
    TranscriptEvent: Optional[TranscriptEvent] = None
    IntentResultEvent: Optional[IntentResultEvent] = None
    TextResponseEvent: Optional[TextResponseEvent] = None
    AudioResponseEvent: Optional[AudioResponseEvent] = None
    HeartbeatEvent: Optional[HeartbeatEvent] = None
    AccessDeniedException: Optional[AccessDeniedException] = None
    ResourceNotFoundException: Optional[ResourceNotFoundException] = None
    ValidationException: Optional[ValidationException] = None
    ThrottlingException: Optional[ThrottlingException] = None
    InternalServerException: Optional[InternalServerException] = None
    ConflictException: Optional[ConflictException] = None
    DependencyFailedException: Optional[DependencyFailedException] = None
    BadGatewayException: Optional[BadGatewayException] = None


class StartConversationResponse(BaseValidatorModel):
    responseEventStream: EventStream[StartConversationResponseEventStream]
    ResponseMetadata: ResponseMetadata


class IntentUnion(BaseValidatorModel):
    pass


class ActiveContextUnion(BaseValidatorModel):
    pass


class RuntimeHintsUnion(BaseValidatorModel):
    pass


class DialogActionUnion(BaseValidatorModel):
    pass


class SessionState(BaseValidatorModel):
    dialogAction: Optional[DialogActionUnion] = None
    intent: Optional[IntentUnion] = None
    activeContexts: Optional[Sequence[ActiveContextUnion]] = None
    sessionAttributes: Optional[Mapping[str, str]] = None
    originatingRequestId: Optional[str] = None
    runtimeHints: Optional[RuntimeHintsUnion] = None


class MessageUnion(BaseValidatorModel):
    pass


class SessionStateUnion(BaseValidatorModel):
    pass


class ConfigurationEvent(BaseValidatorModel):
    responseContentType: str
    requestAttributes: Optional[Mapping[str, str]] = None
    sessionState: Optional[SessionStateUnion] = None
    welcomeMessages: Optional[Sequence[MessageUnion]] = None
    disablePlayback: Optional[bool] = None
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class PutSessionRequest(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    sessionState: SessionStateUnion
    messages: Optional[Sequence[MessageUnion]] = None
    requestAttributes: Optional[Mapping[str, str]] = None
    responseContentType: Optional[str] = None


class RecognizeTextRequest(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    text: str
    sessionState: Optional[SessionStateUnion] = None
    requestAttributes: Optional[Mapping[str, str]] = None


class StartConversationRequestEventStream(BaseValidatorModel):
    ConfigurationEvent: Optional[ConfigurationEvent] = None
    AudioInputEvent: Optional[AudioInputEvent] = None
    DTMFInputEvent: Optional[DTMFInputEvent] = None
    TextInputEvent: Optional[TextInputEvent] = None
    PlaybackCompletionEvent: Optional[PlaybackCompletionEvent] = None
    DisconnectionEvent: Optional[DisconnectionEvent] = None


class StartConversationRequest(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    requestEventStream: EventStream[StartConversationRequestEventStream]
    conversationMode: Optional[ConversationModeType] = None



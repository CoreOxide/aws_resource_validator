from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.lexv2_runtime.lexv2_runtime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessDeniedException(BaseValidatorModel):
    message: str


class ActiveContextTimeToLive(BaseValidatorModel):
    timeToLiveInSeconds: int
    turnsToLive: int

Blob = Union[str, bytes, IO[Any], StreamingBody]


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
    subSlotToElicit: Optional[Dict[str, Any]] = None


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
    resolvedValues: Optional[List[str]] = None


class ActiveContextOutput(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLive
    contextAttributes: Dict[str, str]


class ActiveContext(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLive
    contextAttributes: Dict[str, str]


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
    buttons: Optional[List[Button]] = None


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


class DialogActionOutput(BaseValidatorModel):
    type: DialogActionTypeType
    slotToElicit: Optional[str] = None
    slotElicitationStyle: Optional[StyleTypeType] = None
    subSlotToElicit: Optional[ElicitSubSlotOutput] = None

ElicitSubSlotUnion = Union[ElicitSubSlot, ElicitSubSlotOutput]


class RuntimeHintDetailsOutput(BaseValidatorModel):
    runtimeHintValues: Optional[List[RuntimeHintValue]] = None
    subSlotHints: Optional[Dict[str, Dict[str, Any]]] = None


class RuntimeHintDetails(BaseValidatorModel):
    runtimeHintValues: Optional[List[RuntimeHintValue]] = None
    subSlotHints: Optional[Dict[str, Dict[str, Any]]] = None


class SentimentResponse(BaseValidatorModel):
    sentiment: Optional[SentimentTypeType] = None
    sentimentScore: Optional[SentimentScore] = None


class SlotOutput(BaseValidatorModel):
    value: Optional[ValueOutput] = None
    shape: Optional[ShapeType] = None
    values: Optional[List[Dict[str, Any]]] = None
    subSlots: Optional[Dict[str, Dict[str, Any]]] = None

ValueUnion = Union[Value, ValueOutput]

ActiveContextUnion = Union[ActiveContext, ActiveContextOutput]


class MessageOutput(BaseValidatorModel):
    contentType: MessageContentTypeType
    content: Optional[str] = None
    imageResponseCard: Optional[ImageResponseCardOutput] = None

ImageResponseCardUnion = Union[ImageResponseCard, ImageResponseCardOutput]


class DialogAction(BaseValidatorModel):
    type: DialogActionTypeType
    slotToElicit: Optional[str] = None
    slotElicitationStyle: Optional[StyleTypeType] = None
    subSlotToElicit: Optional[ElicitSubSlotUnion] = None


class RuntimeHintsOutput(BaseValidatorModel):
    slotHints: Optional[Dict[str, Dict[str, RuntimeHintDetailsOutput]]] = None

RuntimeHintDetailsUnion = Union[RuntimeHintDetails, RuntimeHintDetailsOutput]


class IntentOutput(BaseValidatorModel):
    name: str
    slots: Optional[Dict[str, SlotOutput]] = None
    state: Optional[IntentStateType] = None
    confirmationState: Optional[ConfirmationStateType] = None


class Slot(BaseValidatorModel):
    value: Optional[ValueUnion] = None
    shape: Optional[ShapeType] = None
    values: Optional[List[Dict[str, Any]]] = None
    subSlots: Optional[Dict[str, Dict[str, Any]]] = None


class TextResponseEvent(BaseValidatorModel):
    messages: Optional[List[MessageOutput]] = None
    eventId: Optional[str] = None


class Message(BaseValidatorModel):
    contentType: MessageContentTypeType
    content: Optional[str] = None
    imageResponseCard: Optional[ImageResponseCardUnion] = None

DialogActionUnion = Union[DialogAction, DialogActionOutput]


class RuntimeHints(BaseValidatorModel):
    slotHints: Optional[Dict[str, Dict[str, RuntimeHintDetailsUnion]]] = None


class Interpretation(BaseValidatorModel):
    nluConfidence: Optional[ConfidenceScore] = None
    sentimentResponse: Optional[SentimentResponse] = None
    intent: Optional[IntentOutput] = None
    interpretationSource: Optional[InterpretationSourceType] = None


class SessionStateOutput(BaseValidatorModel):
    dialogAction: Optional[DialogActionOutput] = None
    intent: Optional[IntentOutput] = None
    activeContexts: Optional[List[ActiveContextOutput]] = None
    sessionAttributes: Optional[Dict[str, str]] = None
    originatingRequestId: Optional[str] = None
    runtimeHints: Optional[RuntimeHintsOutput] = None

SlotUnion = Union[Slot, SlotOutput]

MessageUnion = Union[Message, MessageOutput]

RuntimeHintsUnion = Union[RuntimeHints, RuntimeHintsOutput]


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


class Intent(BaseValidatorModel):
    name: str
    slots: Optional[Dict[str, SlotUnion]] = None
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

IntentUnion = Union[Intent, IntentOutput]


class StartConversationResponse(BaseValidatorModel):
    responseEventStream: EventStream[StartConversationResponseEventStream]
    ResponseMetadata: ResponseMetadata


class SessionState(BaseValidatorModel):
    dialogAction: Optional[DialogActionUnion] = None
    intent: Optional[IntentUnion] = None
    activeContexts: Optional[List[ActiveContextUnion]] = None
    sessionAttributes: Optional[Dict[str, str]] = None
    originatingRequestId: Optional[str] = None
    runtimeHints: Optional[RuntimeHintsUnion] = None

SessionStateUnion = Union[SessionState, SessionStateOutput]


class ConfigurationEvent(BaseValidatorModel):
    responseContentType: str
    requestAttributes: Optional[Dict[str, str]] = None
    sessionState: Optional[SessionStateUnion] = None
    welcomeMessages: Optional[List[MessageUnion]] = None
    disablePlayback: Optional[bool] = None
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class PutSessionRequest(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    sessionState: SessionStateUnion
    messages: Optional[List[MessageUnion]] = None
    requestAttributes: Optional[Dict[str, str]] = None
    responseContentType: Optional[str] = None


class RecognizeTextRequest(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    text: str
    sessionState: Optional[SessionStateUnion] = None
    requestAttributes: Optional[Dict[str, str]] = None


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
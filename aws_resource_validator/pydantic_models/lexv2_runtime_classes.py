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

class AccessDeniedExceptionTypeDef(BaseValidatorModel):
    message: str


class ActiveContextTimeToLiveTypeDef(BaseValidatorModel):
    timeToLiveInSeconds: int
    turnsToLive: int


class AudioResponseEventTypeDef(BaseValidatorModel):
    audioChunk: Optional[bytes] = None
    contentType: Optional[str] = None
    eventId: Optional[str] = None


class BadGatewayExceptionTypeDef(BaseValidatorModel):
    message: str


class ButtonTypeDef(BaseValidatorModel):
    text: str
    value: str


class ConfidenceScoreTypeDef(BaseValidatorModel):
    score: Optional[float] = None


class ConflictExceptionTypeDef(BaseValidatorModel):
    message: str


class DTMFInputEventTypeDef(BaseValidatorModel):
    inputCharacter: str
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class DeleteSessionRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DependencyFailedExceptionTypeDef(BaseValidatorModel):
    message: str


class ElicitSubSlotOutputTypeDef(BaseValidatorModel):
    name: str
    subSlotToElicit: Optional[Dict[str, Any]] = None


class DisconnectionEventTypeDef(BaseValidatorModel):
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class ElicitSubSlotTypeDef(BaseValidatorModel):
    name: str
    subSlotToElicit: Optional[Mapping[str, Any]] = None


class GetSessionRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str


class HeartbeatEventTypeDef(BaseValidatorModel):
    eventId: Optional[str] = None


class RecognizedBotMemberTypeDef(BaseValidatorModel):
    botId: str
    botName: Optional[str] = None


class InternalServerExceptionTypeDef(BaseValidatorModel):
    message: str


class PlaybackCompletionEventTypeDef(BaseValidatorModel):
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class PlaybackInterruptionEventTypeDef(BaseValidatorModel):
    eventReason: Optional[PlaybackInterruptionReasonType] = None
    causedByEventId: Optional[str] = None
    eventId: Optional[str] = None


class ResourceNotFoundExceptionTypeDef(BaseValidatorModel):
    message: str


class RuntimeHintValueTypeDef(BaseValidatorModel):
    phrase: str


class SentimentScoreTypeDef(BaseValidatorModel):
    positive: Optional[float] = None
    negative: Optional[float] = None
    neutral: Optional[float] = None
    mixed: Optional[float] = None


class ValueOutputTypeDef(BaseValidatorModel):
    interpretedValue: str
    originalValue: Optional[str] = None
    resolvedValues: Optional[List[str]] = None


class TextInputEventTypeDef(BaseValidatorModel):
    text: str
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class ThrottlingExceptionTypeDef(BaseValidatorModel):
    message: str


class TranscriptEventTypeDef(BaseValidatorModel):
    transcript: Optional[str] = None
    eventId: Optional[str] = None


class ValidationExceptionTypeDef(BaseValidatorModel):
    message: str


class ValueTypeDef(BaseValidatorModel):
    interpretedValue: str
    originalValue: Optional[str] = None
    resolvedValues: Optional[Sequence[str]] = None


class ActiveContextOutputTypeDef(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLiveTypeDef
    contextAttributes: Dict[str, str]


class ActiveContextTypeDef(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLiveTypeDef
    contextAttributes: Mapping[str, str]


class BlobTypeDef(BaseValidatorModel):
    pass


class AudioInputEventTypeDef(BaseValidatorModel):
    contentType: str
    audioChunk: Optional[BlobTypeDef] = None
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class RecognizeUtteranceRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    requestContentType: str
    sessionState: Optional[str] = None
    requestAttributes: Optional[str] = None
    responseContentType: Optional[str] = None
    inputStream: Optional[BlobTypeDef] = None


class ImageResponseCardOutputTypeDef(BaseValidatorModel):
    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[List[ButtonTypeDef]] = None


class ImageResponseCardTypeDef(BaseValidatorModel):
    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[Sequence[ButtonTypeDef]] = None


class DeleteSessionResponseTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutSessionResponseTypeDef(BaseValidatorModel):
    contentType: str
    messages: str
    sessionState: str
    requestAttributes: str
    sessionId: str
    audioStream: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class RecognizeUtteranceResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class RuntimeHintDetailsOutputTypeDef(BaseValidatorModel):
    runtimeHintValues: Optional[List[RuntimeHintValueTypeDef]] = None
    subSlotHints: Optional[Dict[str, Dict[str, Any]]] = None


class RuntimeHintDetailsTypeDef(BaseValidatorModel):
    runtimeHintValues: Optional[Sequence[RuntimeHintValueTypeDef]] = None
    subSlotHints: Optional[Mapping[str, Mapping[str, Any]]] = None


class SentimentResponseTypeDef(BaseValidatorModel):
    sentiment: Optional[SentimentTypeType] = None
    sentimentScore: Optional[SentimentScoreTypeDef] = None


class SlotOutputTypeDef(BaseValidatorModel):
    value: Optional[ValueOutputTypeDef] = None
    shape: Optional[ShapeType] = None
    values: Optional[List[Dict[str, Any]]] = None
    subSlots: Optional[Dict[str, Dict[str, Any]]] = None


class MessageOutputTypeDef(BaseValidatorModel):
    contentType: MessageContentTypeType
    content: Optional[str] = None
    imageResponseCard: Optional[ImageResponseCardOutputTypeDef] = None


class RuntimeHintsOutputTypeDef(BaseValidatorModel):
    slotHints: Optional[Dict[str, Dict[str, RuntimeHintDetailsOutputTypeDef]]] = None


class IntentOutputTypeDef(BaseValidatorModel):
    name: str
    slots: Optional[Dict[str, SlotOutputTypeDef]] = None
    state: Optional[IntentStateType] = None
    confirmationState: Optional[ConfirmationStateType] = None


class ValueUnionTypeDef(BaseValidatorModel):
    pass


class SlotTypeDef(BaseValidatorModel):
    value: Optional[ValueUnionTypeDef] = None
    shape: Optional[ShapeType] = None
    values: Optional[Sequence[Mapping[str, Any]]] = None
    subSlots: Optional[Mapping[str, Mapping[str, Any]]] = None


class TextResponseEventTypeDef(BaseValidatorModel):
    messages: Optional[List[MessageOutputTypeDef]] = None
    eventId: Optional[str] = None


class ImageResponseCardUnionTypeDef(BaseValidatorModel):
    pass


class MessageTypeDef(BaseValidatorModel):
    contentType: MessageContentTypeType
    content: Optional[str] = None
    imageResponseCard: Optional[ImageResponseCardUnionTypeDef] = None


class RuntimeHintDetailsUnionTypeDef(BaseValidatorModel):
    pass


class RuntimeHintsTypeDef(BaseValidatorModel):
    slotHints: Optional[Mapping[str, Mapping[str, RuntimeHintDetailsUnionTypeDef]]] = None


class InterpretationTypeDef(BaseValidatorModel):
    nluConfidence: Optional[ConfidenceScoreTypeDef] = None
    sentimentResponse: Optional[SentimentResponseTypeDef] = None
    intent: Optional[IntentOutputTypeDef] = None
    interpretationSource: Optional[InterpretationSourceType] = None


class DialogActionOutputTypeDef(BaseValidatorModel):
    pass


class SessionStateOutputTypeDef(BaseValidatorModel):
    dialogAction: Optional[DialogActionOutputTypeDef] = None
    intent: Optional[IntentOutputTypeDef] = None
    activeContexts: Optional[List[ActiveContextOutputTypeDef]] = None
    sessionAttributes: Optional[Dict[str, str]] = None
    originatingRequestId: Optional[str] = None
    runtimeHints: Optional[RuntimeHintsOutputTypeDef] = None


class GetSessionResponseTypeDef(BaseValidatorModel):
    sessionId: str
    messages: List[MessageOutputTypeDef]
    interpretations: List[InterpretationTypeDef]
    sessionState: SessionStateOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IntentResultEventTypeDef(BaseValidatorModel):
    inputMode: Optional[InputModeType] = None
    interpretations: Optional[List[InterpretationTypeDef]] = None
    sessionState: Optional[SessionStateOutputTypeDef] = None
    requestAttributes: Optional[Dict[str, str]] = None
    sessionId: Optional[str] = None
    eventId: Optional[str] = None
    recognizedBotMember: Optional[RecognizedBotMemberTypeDef] = None


class RecognizeTextResponseTypeDef(BaseValidatorModel):
    messages: List[MessageOutputTypeDef]
    sessionState: SessionStateOutputTypeDef
    interpretations: List[InterpretationTypeDef]
    requestAttributes: Dict[str, str]
    sessionId: str
    recognizedBotMember: RecognizedBotMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SlotUnionTypeDef(BaseValidatorModel):
    pass


class IntentTypeDef(BaseValidatorModel):
    name: str
    slots: Optional[Mapping[str, SlotUnionTypeDef]] = None
    state: Optional[IntentStateType] = None
    confirmationState: Optional[ConfirmationStateType] = None


class StartConversationResponseEventStreamTypeDef(BaseValidatorModel):
    PlaybackInterruptionEvent: Optional[PlaybackInterruptionEventTypeDef] = None
    TranscriptEvent: Optional[TranscriptEventTypeDef] = None
    IntentResultEvent: Optional[IntentResultEventTypeDef] = None
    TextResponseEvent: Optional[TextResponseEventTypeDef] = None
    AudioResponseEvent: Optional[AudioResponseEventTypeDef] = None
    HeartbeatEvent: Optional[HeartbeatEventTypeDef] = None
    AccessDeniedException: Optional[AccessDeniedExceptionTypeDef] = None
    ResourceNotFoundException: Optional[ResourceNotFoundExceptionTypeDef] = None
    ValidationException: Optional[ValidationExceptionTypeDef] = None
    ThrottlingException: Optional[ThrottlingExceptionTypeDef] = None
    InternalServerException: Optional[InternalServerExceptionTypeDef] = None
    ConflictException: Optional[ConflictExceptionTypeDef] = None
    DependencyFailedException: Optional[DependencyFailedExceptionTypeDef] = None
    BadGatewayException: Optional[BadGatewayExceptionTypeDef] = None


class StartConversationResponseTypeDef(BaseValidatorModel):
    responseEventStream: EventStream[StartConversationResponseEventStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class IntentUnionTypeDef(BaseValidatorModel):
    pass


class ActiveContextUnionTypeDef(BaseValidatorModel):
    pass


class RuntimeHintsUnionTypeDef(BaseValidatorModel):
    pass


class DialogActionUnionTypeDef(BaseValidatorModel):
    pass


class SessionStateTypeDef(BaseValidatorModel):
    dialogAction: Optional[DialogActionUnionTypeDef] = None
    intent: Optional[IntentUnionTypeDef] = None
    activeContexts: Optional[Sequence[ActiveContextUnionTypeDef]] = None
    sessionAttributes: Optional[Mapping[str, str]] = None
    originatingRequestId: Optional[str] = None
    runtimeHints: Optional[RuntimeHintsUnionTypeDef] = None


class MessageUnionTypeDef(BaseValidatorModel):
    pass


class SessionStateUnionTypeDef(BaseValidatorModel):
    pass


class ConfigurationEventTypeDef(BaseValidatorModel):
    responseContentType: str
    requestAttributes: Optional[Mapping[str, str]] = None
    sessionState: Optional[SessionStateUnionTypeDef] = None
    welcomeMessages: Optional[Sequence[MessageUnionTypeDef]] = None
    disablePlayback: Optional[bool] = None
    eventId: Optional[str] = None
    clientTimestampMillis: Optional[int] = None


class PutSessionRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    sessionState: SessionStateUnionTypeDef
    messages: Optional[Sequence[MessageUnionTypeDef]] = None
    requestAttributes: Optional[Mapping[str, str]] = None
    responseContentType: Optional[str] = None


class RecognizeTextRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    text: str
    sessionState: Optional[SessionStateUnionTypeDef] = None
    requestAttributes: Optional[Mapping[str, str]] = None


class StartConversationRequestEventStreamTypeDef(BaseValidatorModel):
    ConfigurationEvent: Optional[ConfigurationEventTypeDef] = None
    AudioInputEvent: Optional[AudioInputEventTypeDef] = None
    DTMFInputEvent: Optional[DTMFInputEventTypeDef] = None
    TextInputEvent: Optional[TextInputEventTypeDef] = None
    PlaybackCompletionEvent: Optional[PlaybackCompletionEventTypeDef] = None
    DisconnectionEvent: Optional[DisconnectionEventTypeDef] = None


class StartConversationRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    requestEventStream: EventStream[StartConversationRequestEventStreamTypeDef]
    conversationMode: Optional[ConversationModeType] = None



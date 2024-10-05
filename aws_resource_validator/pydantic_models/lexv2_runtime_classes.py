from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.lexv2_runtime_constants import *

class ActiveContextTimeToLiveTypeDef(BaseValidatorModel):
    timeToLiveInSeconds: int
    turnsToLive: int

class ButtonTypeDef(BaseValidatorModel):
    text: str
    value: str

class ConfidenceScoreTypeDef(BaseValidatorModel):
    score: Optional[float] = None

class DeleteSessionRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DialogActionTypeDef(BaseValidatorModel):
    type: DialogActionTypeType
    slotToElicit: Optional[str] = None
    slotElicitationStyle: Optional[StyleTypeType] = None
    subSlotToElicit: Optional["ElicitSubSlotTypeDef"] = None

class ElicitSubSlotTypeDef(BaseValidatorModel):
    name: str
    subSlotToElicit: Optional[Dict[str, Any]] = None

class GetSessionRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str

class IntentTypeDef(BaseValidatorModel):
    name: str
    slots: Optional[Dict[str, "SlotTypeDef"]] = None
    state: Optional[IntentStateType] = None
    confirmationState: Optional[ConfirmationStateType] = None

class RecognizedBotMemberTypeDef(BaseValidatorModel):
    botId: str
    botName: Optional[str] = None

class RuntimeHintValueTypeDef(BaseValidatorModel):
    phrase: str

class RuntimeHintsTypeDef(BaseValidatorModel):
    slotHints: Optional[Dict[str, Dict[str, "RuntimeHintDetailsTypeDef"]]] = None

class SentimentScoreTypeDef(BaseValidatorModel):
    positive: Optional[float] = None
    negative: Optional[float] = None
    neutral: Optional[float] = None
    mixed: Optional[float] = None

class ValueTypeDef(BaseValidatorModel):
    interpretedValue: str
    originalValue: Optional[str] = None
    resolvedValues: Optional[List[str]] = None

class ActiveContextTypeDef(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLiveTypeDef
    contextAttributes: Dict[str, str]

class RecognizeUtteranceRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    requestContentType: str
    sessionState: Optional[str] = None
    requestAttributes: Optional[str] = None
    responseContentType: Optional[str] = None
    inputStream: Optional[BlobTypeDef] = None

class ImageResponseCardTypeDef(BaseValidatorModel):
    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[List[ButtonTypeDef]] = None

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

class RuntimeHintDetailsTypeDef(BaseValidatorModel):
    runtimeHintValues: Optional[List[RuntimeHintValueTypeDef]] = None
    subSlotHints: Optional[Dict[str, Dict[str, Any]]] = None

class SentimentResponseTypeDef(BaseValidatorModel):
    sentiment: Optional[SentimentTypeType] = None
    sentimentScore: Optional[SentimentScoreTypeDef] = None

class SlotTypeDef(BaseValidatorModel):
    value: Optional[ValueTypeDef] = None
    shape: Optional[ShapeType] = None
    values: Optional[List[Dict[str, Any]]] = None
    subSlots: Optional[Dict[str, Dict[str, Any]]] = None

class SessionStateTypeDef(BaseValidatorModel):
    dialogAction: Optional[DialogActionTypeDef] = None
    intent: Optional[IntentTypeDef] = None
    activeContexts: Optional[List[ActiveContextTypeDef]] = None
    sessionAttributes: Optional[Dict[str, str]] = None
    originatingRequestId: Optional[str] = None
    runtimeHints: Optional[RuntimeHintsTypeDef] = None

class MessageTypeDef(BaseValidatorModel):
    contentType: MessageContentTypeType
    content: Optional[str] = None
    imageResponseCard: Optional[ImageResponseCardTypeDef] = None

class InterpretationTypeDef(BaseValidatorModel):
    nluConfidence: Optional[ConfidenceScoreTypeDef] = None
    sentimentResponse: Optional[SentimentResponseTypeDef] = None
    intent: Optional[IntentTypeDef] = None
    interpretationSource: Optional[InterpretationSourceType] = None

class RecognizeTextRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    text: str
    sessionState: Optional[SessionStateTypeDef] = None
    requestAttributes: Optional[Mapping[str, str]] = None

class PutSessionRequestRequestTypeDef(BaseValidatorModel):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str
    sessionState: SessionStateTypeDef
    messages: Optional[Sequence[MessageTypeDef]] = None
    requestAttributes: Optional[Mapping[str, str]] = None
    responseContentType: Optional[str] = None

class GetSessionResponseTypeDef(BaseValidatorModel):
    sessionId: str
    messages: List[MessageTypeDef]
    interpretations: List[InterpretationTypeDef]
    sessionState: SessionStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RecognizeTextResponseTypeDef(BaseValidatorModel):
    messages: List[MessageTypeDef]
    sessionState: SessionStateTypeDef
    interpretations: List[InterpretationTypeDef]
    requestAttributes: Dict[str, str]
    sessionId: str
    recognizedBotMember: RecognizedBotMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


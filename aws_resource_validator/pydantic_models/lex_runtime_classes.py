from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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
from aws_resource_validator.pydantic_models.lex_runtime_constants import *

class ActiveContextTimeToLive(BaseValidatorModel):
    timeToLiveInSeconds: Optional[int] = None
    turnsToLive: Optional[int] = None


class Button(BaseValidatorModel):
    text: str
    value: str


class DeleteSessionRequest(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetSessionRequest(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    checkpointLabelFilter: Optional[str] = None


class IntentSummaryOutput(BaseValidatorModel):
    dialogActionType: DialogActionTypeType
    intentName: Optional[str] = None
    checkpointLabel: Optional[str] = None
    slots: Optional[Dict[str, str]] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None
    fulfillmentState: Optional[FulfillmentStateType] = None
    slotToElicit: Optional[str] = None


class IntentConfidence(BaseValidatorModel):
    score: Optional[float] = None


class IntentSummary(BaseValidatorModel):
    dialogActionType: DialogActionTypeType
    intentName: Optional[str] = None
    checkpointLabel: Optional[str] = None
    slots: Optional[Mapping[str, str]] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None
    fulfillmentState: Optional[FulfillmentStateType] = None
    slotToElicit: Optional[str] = None


class SentimentResponse(BaseValidatorModel):
    sentimentLabel: Optional[str] = None
    sentimentScore: Optional[str] = None


class ActiveContextOutput(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLive
    parameters: Dict[str, str]


class ActiveContext(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLive
    parameters: Mapping[str, str]


class Blob(BaseValidatorModel):
    pass


class PostContentRequest(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    contentType: str
    inputStream: Blob
    sessionAttributes: Optional[str] = None
    requestAttributes: Optional[str] = None
    accept: Optional[str] = None
    activeContexts: Optional[str] = None


class GenericAttachment(BaseValidatorModel):
    title: Optional[str] = None
    subTitle: Optional[str] = None
    attachmentLinkUrl: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[List[Button]] = None


class DeleteSessionResponse(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    sessionId: str
    ResponseMetadata: ResponseMetadata


class PostContentResponse(BaseValidatorModel):
    contentType: str
    intentName: str
    nluIntentConfidence: str
    alternativeIntents: str
    slots: str
    sessionAttributes: str
    sentimentResponse: str
    message: str
    encodedMessage: str
    messageFormat: MessageFormatTypeType
    dialogState: DialogStateType
    slotToElicit: str
    inputTranscript: str
    encodedInputTranscript: str
    audioStream: StreamingBody
    botVersion: str
    sessionId: str
    activeContexts: str
    ResponseMetadata: ResponseMetadata


class PutSessionResponse(BaseValidatorModel):
    contentType: str
    intentName: str
    slots: str
    sessionAttributes: str
    message: str
    encodedMessage: str
    messageFormat: MessageFormatTypeType
    dialogState: DialogStateType
    slotToElicit: str
    audioStream: StreamingBody
    sessionId: str
    activeContexts: str
    ResponseMetadata: ResponseMetadata


class PredictedIntent(BaseValidatorModel):
    intentName: Optional[str] = None
    nluIntentConfidence: Optional[IntentConfidence] = None
    slots: Optional[Dict[str, str]] = None


class DialogActionOutput(BaseValidatorModel):
    pass


class GetSessionResponse(BaseValidatorModel):
    recentIntentSummaryView: List[IntentSummaryOutput]
    sessionAttributes: Dict[str, str]
    sessionId: str
    dialogAction: DialogActionOutput
    activeContexts: List[ActiveContextOutput]
    ResponseMetadata: ResponseMetadata


class ResponseCard(BaseValidatorModel):
    version: Optional[str] = None
    contentType: Optional[Literal["application/vnd.amazonaws.card.generic"]] = None
    genericAttachments: Optional[List[GenericAttachment]] = None


class ActiveContextUnion(BaseValidatorModel):
    pass


class PostTextRequest(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    inputText: str
    sessionAttributes: Optional[Mapping[str, str]] = None
    requestAttributes: Optional[Mapping[str, str]] = None
    activeContexts: Optional[Sequence[ActiveContextUnion]] = None


class IntentSummaryUnion(BaseValidatorModel):
    pass


class DialogActionUnion(BaseValidatorModel):
    pass


class PutSessionRequest(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    sessionAttributes: Optional[Mapping[str, str]] = None
    dialogAction: Optional[DialogActionUnion] = None
    recentIntentSummaryView: Optional[Sequence[IntentSummaryUnion]] = None
    accept: Optional[str] = None
    activeContexts: Optional[Sequence[ActiveContextUnion]] = None


class PostTextResponse(BaseValidatorModel):
    intentName: str
    nluIntentConfidence: IntentConfidence
    alternativeIntents: List[PredictedIntent]
    slots: Dict[str, str]
    sessionAttributes: Dict[str, str]
    message: str
    sentimentResponse: SentimentResponse
    messageFormat: MessageFormatTypeType
    dialogState: DialogStateType
    slotToElicit: str
    responseCard: ResponseCard
    sessionId: str
    botVersion: str
    activeContexts: List[ActiveContextOutput]
    ResponseMetadata: ResponseMetadata



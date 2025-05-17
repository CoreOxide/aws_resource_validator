from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.lex_runtime.lex_runtime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActiveContextTimeToLive(BaseValidatorModel):
    timeToLiveInSeconds: Optional[int] = None
    turnsToLive: Optional[int] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class Button(BaseValidatorModel):
    text: str
    value: str


# This class is the input for the 'delete_session' function.
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


class DialogActionOutput(BaseValidatorModel):
    type: DialogActionTypeType
    intentName: Optional[str] = None
    slots: Optional[Dict[str, str]] = None
    slotToElicit: Optional[str] = None
    fulfillmentState: Optional[FulfillmentStateType] = None
    message: Optional[str] = None
    messageFormat: Optional[MessageFormatTypeType] = None


class DialogAction(BaseValidatorModel):
    type: DialogActionTypeType
    intentName: Optional[str] = None
    slots: Optional[Dict[str, str]] = None
    slotToElicit: Optional[str] = None
    fulfillmentState: Optional[FulfillmentStateType] = None
    message: Optional[str] = None
    messageFormat: Optional[MessageFormatTypeType] = None


# This class is the input for the 'get_session' function.
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
    slots: Optional[Dict[str, str]] = None
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
    parameters: Dict[str, str]


# This class is the input for the 'post_content' function.
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


# This class is the output for the 'delete_session' function.
class DeleteSessionResponse(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    sessionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'post_content' function.
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


# This class is the output for the 'put_session' function.
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

DialogActionUnion = Union[DialogAction, DialogActionOutput]


class PredictedIntent(BaseValidatorModel):
    intentName: Optional[str] = None
    nluIntentConfidence: Optional[IntentConfidence] = None
    slots: Optional[Dict[str, str]] = None

IntentSummaryUnion = Union[IntentSummary, IntentSummaryOutput]


# This class is the output for the 'get_session' function.
class GetSessionResponse(BaseValidatorModel):
    recentIntentSummaryView: List[IntentSummaryOutput]
    sessionAttributes: Dict[str, str]
    sessionId: str
    dialogAction: DialogActionOutput
    activeContexts: List[ActiveContextOutput]
    ResponseMetadata: ResponseMetadata

ActiveContextUnion = Union[ActiveContext, ActiveContextOutput]


class ResponseCard(BaseValidatorModel):
    version: Optional[str] = None
    contentType: Optional[Literal['application/vnd.amazonaws.card.generic']] = None
    genericAttachments: Optional[List[GenericAttachment]] = None


# This class is the input for the 'post_text' function.
class PostTextRequest(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    inputText: str
    sessionAttributes: Optional[Dict[str, str]] = None
    requestAttributes: Optional[Dict[str, str]] = None
    activeContexts: Optional[List[ActiveContextUnion]] = None


# This class is the input for the 'put_session' function.
class PutSessionRequest(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    sessionAttributes: Optional[Dict[str, str]] = None
    dialogAction: Optional[DialogActionUnion] = None
    recentIntentSummaryView: Optional[List[IntentSummaryUnion]] = None
    accept: Optional[str] = None
    activeContexts: Optional[List[ActiveContextUnion]] = None


# This class is the output for the 'post_text' function.
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

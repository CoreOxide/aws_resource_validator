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

class ActiveContextTimeToLiveTypeDef(BaseValidatorModel):
    timeToLiveInSeconds: Optional[int] = None
    turnsToLive: Optional[int] = None


class ButtonTypeDef(BaseValidatorModel):
    text: str
    value: str


class DeleteSessionRequestTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetSessionRequestTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    checkpointLabelFilter: Optional[str] = None


class IntentSummaryOutputTypeDef(BaseValidatorModel):
    dialogActionType: DialogActionTypeType
    intentName: Optional[str] = None
    checkpointLabel: Optional[str] = None
    slots: Optional[Dict[str, str]] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None
    fulfillmentState: Optional[FulfillmentStateType] = None
    slotToElicit: Optional[str] = None


class IntentConfidenceTypeDef(BaseValidatorModel):
    score: Optional[float] = None


class IntentSummaryTypeDef(BaseValidatorModel):
    dialogActionType: DialogActionTypeType
    intentName: Optional[str] = None
    checkpointLabel: Optional[str] = None
    slots: Optional[Mapping[str, str]] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None
    fulfillmentState: Optional[FulfillmentStateType] = None
    slotToElicit: Optional[str] = None


class SentimentResponseTypeDef(BaseValidatorModel):
    sentimentLabel: Optional[str] = None
    sentimentScore: Optional[str] = None


class ActiveContextOutputTypeDef(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLiveTypeDef
    parameters: Dict[str, str]


class ActiveContextTypeDef(BaseValidatorModel):
    name: str
    timeToLive: ActiveContextTimeToLiveTypeDef
    parameters: Mapping[str, str]


class BlobTypeDef(BaseValidatorModel):
    pass


class PostContentRequestTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    contentType: str
    inputStream: BlobTypeDef
    sessionAttributes: Optional[str] = None
    requestAttributes: Optional[str] = None
    accept: Optional[str] = None
    activeContexts: Optional[str] = None


class GenericAttachmentTypeDef(BaseValidatorModel):
    title: Optional[str] = None
    subTitle: Optional[str] = None
    attachmentLinkUrl: Optional[str] = None
    imageUrl: Optional[str] = None
    buttons: Optional[List[ButtonTypeDef]] = None


class DeleteSessionResponseTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PostContentResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class PutSessionResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class PredictedIntentTypeDef(BaseValidatorModel):
    intentName: Optional[str] = None
    nluIntentConfidence: Optional[IntentConfidenceTypeDef] = None
    slots: Optional[Dict[str, str]] = None


class DialogActionOutputTypeDef(BaseValidatorModel):
    pass


class GetSessionResponseTypeDef(BaseValidatorModel):
    recentIntentSummaryView: List[IntentSummaryOutputTypeDef]
    sessionAttributes: Dict[str, str]
    sessionId: str
    dialogAction: DialogActionOutputTypeDef
    activeContexts: List[ActiveContextOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ResponseCardTypeDef(BaseValidatorModel):
    version: Optional[str] = None
    contentType: Optional[Literal["application/vnd.amazonaws.card.generic"]] = None
    genericAttachments: Optional[List[GenericAttachmentTypeDef]] = None


class ActiveContextUnionTypeDef(BaseValidatorModel):
    pass


class PostTextRequestTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    inputText: str
    sessionAttributes: Optional[Mapping[str, str]] = None
    requestAttributes: Optional[Mapping[str, str]] = None
    activeContexts: Optional[Sequence[ActiveContextUnionTypeDef]] = None


class IntentSummaryUnionTypeDef(BaseValidatorModel):
    pass


class DialogActionUnionTypeDef(BaseValidatorModel):
    pass


class PutSessionRequestTypeDef(BaseValidatorModel):
    botName: str
    botAlias: str
    userId: str
    sessionAttributes: Optional[Mapping[str, str]] = None
    dialogAction: Optional[DialogActionUnionTypeDef] = None
    recentIntentSummaryView: Optional[Sequence[IntentSummaryUnionTypeDef]] = None
    accept: Optional[str] = None
    activeContexts: Optional[Sequence[ActiveContextUnionTypeDef]] = None


class PostTextResponseTypeDef(BaseValidatorModel):
    intentName: str
    nluIntentConfidence: IntentConfidenceTypeDef
    alternativeIntents: List[PredictedIntentTypeDef]
    slots: Dict[str, str]
    sessionAttributes: Dict[str, str]
    message: str
    sentimentResponse: SentimentResponseTypeDef
    messageFormat: MessageFormatTypeType
    dialogState: DialogStateType
    slotToElicit: str
    responseCard: ResponseCardTypeDef
    sessionId: str
    botVersion: str
    activeContexts: List[ActiveContextOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef



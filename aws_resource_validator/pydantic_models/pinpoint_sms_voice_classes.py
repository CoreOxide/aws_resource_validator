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
from aws_resource_validator.pydantic_models.pinpoint_sms_voice_constants import *

class CallInstructionsMessageTypeTypeDef(BaseModel):
    Text: Optional[str] = None

class CloudWatchLogsDestinationTypeDef(BaseModel):
    IamRoleArn: Optional[str] = None
    LogGroupArn: Optional[str] = None

class CreateConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: Optional[str] = None

class DeleteConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class KinesisFirehoseDestinationTypeDef(BaseModel):
    DeliveryStreamArn: Optional[str] = None
    IamRoleArn: Optional[str] = None

class SnsDestinationTypeDef(BaseModel):
    TopicArn: Optional[str] = None

class GetConfigurationSetEventDestinationsRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class PlainTextMessageTypeTypeDef(BaseModel):
    LanguageCode: Optional[str] = None
    Text: Optional[str] = None
    VoiceId: Optional[str] = None

class SSMLMessageTypeTypeDef(BaseModel):
    LanguageCode: Optional[str] = None
    Text: Optional[str] = None
    VoiceId: Optional[str] = None

class EventDestinationDefinitionTypeDef(BaseModel):
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None

class EventDestinationTypeDef(BaseModel):
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    MatchingEventTypes: Optional[List[EventTypeType]] = None
    Name: Optional[str] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None

class SendVoiceMessageResponseTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VoiceMessageContentTypeDef(BaseModel):
    CallInstructionsMessage: Optional[CallInstructionsMessageTypeTypeDef] = None
    PlainTextMessage: Optional[PlainTextMessageTypeTypeDef] = None
    SSMLMessage: Optional[SSMLMessageTypeTypeDef] = None

class CreateConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestination: Optional[EventDestinationDefinitionTypeDef] = None
    EventDestinationName: Optional[str] = None

class UpdateConfigurationSetEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: Optional[EventDestinationDefinitionTypeDef] = None

class GetConfigurationSetEventDestinationsResponseTypeDef(BaseModel):
    EventDestinations: List[EventDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendVoiceMessageRequestRequestTypeDef(BaseModel):
    CallerId: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    Content: Optional[VoiceMessageContentTypeDef] = None
    DestinationPhoneNumber: Optional[str] = None
    OriginationPhoneNumber: Optional[str] = None


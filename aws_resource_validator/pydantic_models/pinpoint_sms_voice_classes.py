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
from aws_resource_validator.pydantic_models.pinpoint_sms_voice_constants import *

class CallInstructionsMessageTypeTypeDef(BaseValidatorModel):
    Text: Optional[str] = None

class CloudWatchLogsDestinationTypeDef(BaseValidatorModel):
    IamRoleArn: Optional[str] = None
    LogGroupArn: Optional[str] = None

class CreateConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: Optional[str] = None

class DeleteConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteConfigurationSetRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class KinesisFirehoseDestinationTypeDef(BaseValidatorModel):
    DeliveryStreamArn: Optional[str] = None
    IamRoleArn: Optional[str] = None

class SnsDestinationTypeDef(BaseValidatorModel):
    TopicArn: Optional[str] = None

class GetConfigurationSetEventDestinationsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class PlainTextMessageTypeTypeDef(BaseValidatorModel):
    LanguageCode: Optional[str] = None
    Text: Optional[str] = None
    VoiceId: Optional[str] = None

class SSMLMessageTypeTypeDef(BaseValidatorModel):
    LanguageCode: Optional[str] = None
    Text: Optional[str] = None
    VoiceId: Optional[str] = None

class EventDestinationDefinitionTypeDef(BaseValidatorModel):
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None

class EventDestinationTypeDef(BaseValidatorModel):
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    MatchingEventTypes: Optional[List[EventTypeType]] = None
    Name: Optional[str] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None

class SendVoiceMessageResponseTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VoiceMessageContentTypeDef(BaseValidatorModel):
    CallInstructionsMessage: Optional[CallInstructionsMessageTypeTypeDef] = None
    PlainTextMessage: Optional[PlainTextMessageTypeTypeDef] = None
    SSMLMessage: Optional[SSMLMessageTypeTypeDef] = None

class CreateConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestination: Optional[EventDestinationDefinitionTypeDef] = None
    EventDestinationName: Optional[str] = None

class UpdateConfigurationSetEventDestinationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: Optional[EventDestinationDefinitionTypeDef] = None

class GetConfigurationSetEventDestinationsResponseTypeDef(BaseValidatorModel):
    EventDestinations: List[EventDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendVoiceMessageRequestRequestTypeDef(BaseValidatorModel):
    CallerId: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    Content: Optional[VoiceMessageContentTypeDef] = None
    DestinationPhoneNumber: Optional[str] = None
    OriginationPhoneNumber: Optional[str] = None


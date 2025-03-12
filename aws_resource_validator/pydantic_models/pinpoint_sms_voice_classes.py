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
from aws_resource_validator.pydantic_models.pinpoint_sms_voice_constants import *

class CloudWatchLogsDestinationTypeDef(BaseValidatorModel):
    IamRoleArn: Optional[str] = None
    LogGroupArn: Optional[str] = None


class CreateConfigurationSetRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: Optional[str] = None


class DeleteConfigurationSetEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str


class DeleteConfigurationSetRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class KinesisFirehoseDestinationTypeDef(BaseValidatorModel):
    DeliveryStreamArn: Optional[str] = None
    IamRoleArn: Optional[str] = None


class SnsDestinationTypeDef(BaseValidatorModel):
    TopicArn: Optional[str] = None


class GetConfigurationSetEventDestinationsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class PlainTextMessageTypeTypeDef(BaseValidatorModel):
    pass


class SSMLMessageTypeTypeDef(BaseValidatorModel):
    pass


class CallInstructionsMessageTypeTypeDef(BaseValidatorModel):
    pass


class VoiceMessageContentTypeDef(BaseValidatorModel):
    CallInstructionsMessage: Optional[CallInstructionsMessageTypeTypeDef] = None
    PlainTextMessage: Optional[PlainTextMessageTypeTypeDef] = None
    SSMLMessage: Optional[SSMLMessageTypeTypeDef] = None


class CreateConfigurationSetEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestination: Optional[EventDestinationDefinitionTypeDef] = None
    EventDestinationName: Optional[str] = None


class UpdateConfigurationSetEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: Optional[EventDestinationDefinitionTypeDef] = None


class GetConfigurationSetEventDestinationsResponseTypeDef(BaseValidatorModel):
    EventDestinations: List[EventDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SendVoiceMessageRequestTypeDef(BaseValidatorModel):
    CallerId: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    Content: Optional[VoiceMessageContentTypeDef] = None
    DestinationPhoneNumber: Optional[str] = None
    OriginationPhoneNumber: Optional[str] = None



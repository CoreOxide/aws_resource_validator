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
from aws_resource_validator.pydantic_models.sms_voice_constants import *

class CloudWatchLogsDestination(BaseValidatorModel):
    IamRoleArn: Optional[str] = None
    LogGroupArn: Optional[str] = None


class CreateConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: Optional[str] = None


class DeleteConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str


class DeleteConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str


class KinesisFirehoseDestination(BaseValidatorModel):
    DeliveryStreamArn: Optional[str] = None
    IamRoleArn: Optional[str] = None


class SnsDestination(BaseValidatorModel):
    TopicArn: Optional[str] = None


class GetConfigurationSetEventDestinationsRequest(BaseValidatorModel):
    ConfigurationSetName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ListConfigurationSetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class EventDestinationDefinition(BaseValidatorModel):
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestination] = None
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    SnsDestination: Optional[SnsDestination] = None


class EventDestination(BaseValidatorModel):
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestination] = None
    Enabled: Optional[bool] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    MatchingEventTypes: Optional[List[EventTypeType]] = None
    Name: Optional[str] = None
    SnsDestination: Optional[SnsDestination] = None


class ListConfigurationSetsResponse(BaseValidatorModel):
    ConfigurationSets: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SendVoiceMessageResponse(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class PlainTextMessageType(BaseValidatorModel):
    pass


class SSMLMessageType(BaseValidatorModel):
    pass


class CallInstructionsMessageType(BaseValidatorModel):
    pass


class VoiceMessageContent(BaseValidatorModel):
    CallInstructionsMessage: Optional[CallInstructionsMessageType] = None
    PlainTextMessage: Optional[PlainTextMessageType] = None
    SSMLMessage: Optional[SSMLMessageType] = None


class CreateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestination: Optional[EventDestinationDefinition] = None
    EventDestinationName: Optional[str] = None


class UpdateConfigurationSetEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: Optional[EventDestinationDefinition] = None


class GetConfigurationSetEventDestinationsResponse(BaseValidatorModel):
    EventDestinations: List[EventDestination]
    ResponseMetadata: ResponseMetadata


class SendVoiceMessageRequest(BaseValidatorModel):
    CallerId: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    Content: Optional[VoiceMessageContent] = None
    DestinationPhoneNumber: Optional[str] = None
    OriginationPhoneNumber: Optional[str] = None



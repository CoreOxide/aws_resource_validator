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
from aws_resource_validator.pydantic_models.ivschat_constants import *

class CloudWatchLogsDestinationConfiguration(BaseValidatorModel):
    logGroupName: str


class CreateChatTokenRequest(BaseValidatorModel):
    roomIdentifier: str
    userId: str
    capabilities: Optional[Sequence[ChatTokenCapabilityType]] = None
    sessionDurationInMinutes: Optional[int] = None
    attributes: Optional[Mapping[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MessageReviewHandler(BaseValidatorModel):
    uri: Optional[str] = None
    fallbackResult: Optional[FallbackResultType] = None


class DeleteLoggingConfigurationRequest(BaseValidatorModel):
    identifier: str


class DeleteRoomRequest(BaseValidatorModel):
    identifier: str


class FirehoseDestinationConfiguration(BaseValidatorModel):
    deliveryStreamName: str


class S3DestinationConfiguration(BaseValidatorModel):
    bucketName: str


class DisconnectUserRequest(BaseValidatorModel):
    roomIdentifier: str
    userId: str
    reason: Optional[str] = None


class GetLoggingConfigurationRequest(BaseValidatorModel):
    identifier: str


class GetRoomRequest(BaseValidatorModel):
    identifier: str


class ListLoggingConfigurationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRoomsRequest(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    messageReviewHandlerUri: Optional[str] = None
    loggingConfigurationIdentifier: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class SendEventRequest(BaseValidatorModel):
    roomIdentifier: str
    eventName: str
    attributes: Optional[Mapping[str, str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateChatTokenResponse(BaseValidatorModel):
    token: str
    tokenExpirationTime: datetime
    sessionExpirationTime: datetime
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateRoomRequest(BaseValidatorModel):
    name: Optional[str] = None
    maximumMessageRatePerSecond: Optional[int] = None
    maximumMessageLength: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandler] = None
    tags: Optional[Mapping[str, str]] = None
    loggingConfigurationIdentifiers: Optional[Sequence[str]] = None


class UpdateRoomRequest(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    maximumMessageRatePerSecond: Optional[int] = None
    maximumMessageLength: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandler] = None
    loggingConfigurationIdentifiers: Optional[Sequence[str]] = None


class DestinationConfiguration(BaseValidatorModel):
    s3: Optional[S3DestinationConfiguration] = None
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfiguration] = None
    firehose: Optional[FirehoseDestinationConfiguration] = None


class RoomSummary(BaseValidatorModel):
    pass


class ListRoomsResponse(BaseValidatorModel):
    rooms: List[RoomSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateLoggingConfigurationRequest(BaseValidatorModel):
    destinationConfiguration: DestinationConfiguration
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateLoggingConfigurationRequest(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    destinationConfiguration: Optional[DestinationConfiguration] = None


class LoggingConfigurationSummary(BaseValidatorModel):
    pass


class ListLoggingConfigurationsResponse(BaseValidatorModel):
    loggingConfigurations: List[LoggingConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None



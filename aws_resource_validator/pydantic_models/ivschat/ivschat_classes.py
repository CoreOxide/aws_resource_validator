from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ivschat.ivschat_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CloudWatchLogsDestinationConfiguration(BaseValidatorModel):
    logGroupName: str


# This class is the input for the 'create_chat_token' function.
class CreateChatTokenRequest(BaseValidatorModel):
    roomIdentifier: str
    userId: str
    capabilities: Optional[List[ChatTokenCapabilityType]] = None
    sessionDurationInMinutes: Optional[int] = None
    attributes: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MessageReviewHandler(BaseValidatorModel):
    uri: Optional[str] = None
    fallbackResult: Optional[FallbackResultType] = None


# This class is the input for the 'delete_logging_configuration' function.
class DeleteLoggingConfigurationRequest(BaseValidatorModel):
    identifier: str


# This class is the input for the 'delete_message' function.
class DeleteMessageRequest(BaseValidatorModel):
    roomIdentifier: str
    id: str
    reason: Optional[str] = None


# This class is the input for the 'delete_room' function.
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


# This class is the input for the 'get_logging_configuration' function.
class GetLoggingConfigurationRequest(BaseValidatorModel):
    identifier: str


# This class is the input for the 'get_room' function.
class GetRoomRequest(BaseValidatorModel):
    identifier: str


# This class is the input for the 'list_logging_configurations' function.
class ListLoggingConfigurationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_rooms' function.
class ListRoomsRequest(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    messageReviewHandlerUri: Optional[str] = None
    loggingConfigurationIdentifier: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'send_event' function.
class SendEventRequest(BaseValidatorModel):
    roomIdentifier: str
    eventName: str
    attributes: Optional[Dict[str, str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the output for the 'create_chat_token' function.
class CreateChatTokenResponse(BaseValidatorModel):
    token: str
    tokenExpirationTime: datetime
    sessionExpirationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_message' function.
class DeleteMessageResponse(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_room' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_event' function.
class SendEventResponse(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_room' function.
class CreateRoomRequest(BaseValidatorModel):
    name: Optional[str] = None
    maximumMessageRatePerSecond: Optional[int] = None
    maximumMessageLength: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandler] = None
    tags: Optional[Dict[str, str]] = None
    loggingConfigurationIdentifiers: Optional[List[str]] = None


# This class is the output for the 'create_room' function.
class CreateRoomResponse(BaseValidatorModel):
    arn: str
    id: str
    name: str
    createTime: datetime
    updateTime: datetime
    maximumMessageRatePerSecond: int
    maximumMessageLength: int
    messageReviewHandler: MessageReviewHandler
    tags: Dict[str, str]
    loggingConfigurationIdentifiers: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_room' function.
class GetRoomResponse(BaseValidatorModel):
    arn: str
    id: str
    name: str
    createTime: datetime
    updateTime: datetime
    maximumMessageRatePerSecond: int
    maximumMessageLength: int
    messageReviewHandler: MessageReviewHandler
    tags: Dict[str, str]
    loggingConfigurationIdentifiers: List[str]
    ResponseMetadata: ResponseMetadata


class RoomSummary(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    messageReviewHandler: Optional[MessageReviewHandler] = None
    createTime: Optional[datetime] = None
    updateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    loggingConfigurationIdentifiers: Optional[List[str]] = None


# This class is the input for the 'update_room' function.
class UpdateRoomRequest(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    maximumMessageRatePerSecond: Optional[int] = None
    maximumMessageLength: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandler] = None
    loggingConfigurationIdentifiers: Optional[List[str]] = None


# This class is the output for the 'update_room' function.
class UpdateRoomResponse(BaseValidatorModel):
    arn: str
    id: str
    name: str
    createTime: datetime
    updateTime: datetime
    maximumMessageRatePerSecond: int
    maximumMessageLength: int
    messageReviewHandler: MessageReviewHandler
    tags: Dict[str, str]
    loggingConfigurationIdentifiers: List[str]
    ResponseMetadata: ResponseMetadata


class DestinationConfiguration(BaseValidatorModel):
    s3: Optional[S3DestinationConfiguration] = None
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfiguration] = None
    firehose: Optional[FirehoseDestinationConfiguration] = None


# This class is the output for the 'list_rooms' function.
class ListRoomsResponse(BaseValidatorModel):
    rooms: List[RoomSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_logging_configuration' function.
class CreateLoggingConfigurationRequest(BaseValidatorModel):
    destinationConfiguration: DestinationConfiguration
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_logging_configuration' function.
class CreateLoggingConfigurationResponse(BaseValidatorModel):
    arn: str
    id: str
    createTime: datetime
    updateTime: datetime
    name: str
    destinationConfiguration: DestinationConfiguration
    state: Literal['ACTIVE']
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_logging_configuration' function.
class GetLoggingConfigurationResponse(BaseValidatorModel):
    arn: str
    id: str
    createTime: datetime
    updateTime: datetime
    name: str
    destinationConfiguration: DestinationConfiguration
    state: LoggingConfigurationStateType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class LoggingConfigurationSummary(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    createTime: Optional[datetime] = None
    updateTime: Optional[datetime] = None
    name: Optional[str] = None
    destinationConfiguration: Optional[DestinationConfiguration] = None
    state: Optional[LoggingConfigurationStateType] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_logging_configuration' function.
class UpdateLoggingConfigurationRequest(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    destinationConfiguration: Optional[DestinationConfiguration] = None


# This class is the output for the 'update_logging_configuration' function.
class UpdateLoggingConfigurationResponse(BaseValidatorModel):
    arn: str
    id: str
    createTime: datetime
    updateTime: datetime
    name: str
    destinationConfiguration: DestinationConfiguration
    state: Literal['ACTIVE']
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_logging_configurations' function.
class ListLoggingConfigurationsResponse(BaseValidatorModel):
    loggingConfigurations: List[LoggingConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None
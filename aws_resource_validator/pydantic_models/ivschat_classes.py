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

class CloudWatchLogsDestinationConfigurationTypeDef(BaseValidatorModel):
    logGroupName: str


class CreateChatTokenRequestTypeDef(BaseValidatorModel):
    roomIdentifier: str
    userId: str
    capabilities: Optional[Sequence[ChatTokenCapabilityType]] = None
    sessionDurationInMinutes: Optional[int] = None
    attributes: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MessageReviewHandlerTypeDef(BaseValidatorModel):
    uri: Optional[str] = None
    fallbackResult: Optional[FallbackResultType] = None


class DeleteLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    identifier: str


class DeleteRoomRequestTypeDef(BaseValidatorModel):
    identifier: str


class FirehoseDestinationConfigurationTypeDef(BaseValidatorModel):
    deliveryStreamName: str


class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    bucketName: str


class DisconnectUserRequestTypeDef(BaseValidatorModel):
    roomIdentifier: str
    userId: str
    reason: Optional[str] = None


class GetLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    identifier: str


class GetRoomRequestTypeDef(BaseValidatorModel):
    identifier: str


class ListLoggingConfigurationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRoomsRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    messageReviewHandlerUri: Optional[str] = None
    loggingConfigurationIdentifier: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class SendEventRequestTypeDef(BaseValidatorModel):
    roomIdentifier: str
    eventName: str
    attributes: Optional[Mapping[str, str]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateChatTokenResponseTypeDef(BaseValidatorModel):
    token: str
    tokenExpirationTime: datetime
    sessionExpirationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRoomRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    maximumMessageRatePerSecond: Optional[int] = None
    maximumMessageLength: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandlerTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    loggingConfigurationIdentifiers: Optional[Sequence[str]] = None


class UpdateRoomRequestTypeDef(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    maximumMessageRatePerSecond: Optional[int] = None
    maximumMessageLength: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandlerTypeDef] = None
    loggingConfigurationIdentifiers: Optional[Sequence[str]] = None


class DestinationConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[S3DestinationConfigurationTypeDef] = None
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfigurationTypeDef] = None
    firehose: Optional[FirehoseDestinationConfigurationTypeDef] = None


class RoomSummaryTypeDef(BaseValidatorModel):
    pass


class ListRoomsResponseTypeDef(BaseValidatorModel):
    rooms: List[RoomSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    destinationConfiguration: DestinationConfigurationTypeDef
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    identifier: str
    name: Optional[str] = None
    destinationConfiguration: Optional[DestinationConfigurationTypeDef] = None


class LoggingConfigurationSummaryTypeDef(BaseValidatorModel):
    pass


class ListLoggingConfigurationsResponseTypeDef(BaseValidatorModel):
    loggingConfigurations: List[LoggingConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None



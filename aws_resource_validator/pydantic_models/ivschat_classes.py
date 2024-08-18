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
from aws_resource_validator.pydantic_models.ivschat_constants import *

class CloudWatchLogsDestinationConfigurationTypeDef(BaseValidatorModel):
    logGroupName: str

class CreateChatTokenRequestRequestTypeDef(BaseValidatorModel):
    roomIdentifier: str
    userId: str
    attributes: Optional[Mapping[str, str]] = None
    capabilities: Optional[Sequence[ChatTokenCapabilityType]] = None
    sessionDurationInMinutes: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class MessageReviewHandlerTypeDef(BaseValidatorModel):
    fallbackResult: Optional[FallbackResultType] = None
    uri: Optional[str] = None

class DeleteLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    identifier: str

class DeleteMessageRequestRequestTypeDef(BaseValidatorModel):
    id: str
    roomIdentifier: str
    reason: Optional[str] = None

class DeleteRoomRequestRequestTypeDef(BaseValidatorModel):
    identifier: str

class FirehoseDestinationConfigurationTypeDef(BaseValidatorModel):
    deliveryStreamName: str

class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    bucketName: str

class DisconnectUserRequestRequestTypeDef(BaseValidatorModel):
    roomIdentifier: str
    userId: str
    reason: Optional[str] = None

class GetLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    identifier: str

class GetRoomRequestRequestTypeDef(BaseValidatorModel):
    identifier: str

class ListLoggingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRoomsRequestRequestTypeDef(BaseValidatorModel):
    loggingConfigurationIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    messageReviewHandlerUri: Optional[str] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class SendEventRequestRequestTypeDef(BaseValidatorModel):
    eventName: str
    roomIdentifier: str
    attributes: Optional[Mapping[str, str]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateChatTokenResponseTypeDef(BaseValidatorModel):
    sessionExpirationTime: datetime
    token: str
    tokenExpirationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMessageResponseTypeDef(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SendEventResponseTypeDef(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoomRequestRequestTypeDef(BaseValidatorModel):
    loggingConfigurationIdentifiers: Optional[Sequence[str]] = None
    maximumMessageLength: Optional[int] = None
    maximumMessageRatePerSecond: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandlerTypeDef] = None
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateRoomResponseTypeDef(BaseValidatorModel):
    arn: str
    createTime: datetime
    id: str
    loggingConfigurationIdentifiers: List[str]
    maximumMessageLength: int
    maximumMessageRatePerSecond: int
    messageReviewHandler: MessageReviewHandlerTypeDef
    name: str
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoomResponseTypeDef(BaseValidatorModel):
    arn: str
    createTime: datetime
    id: str
    loggingConfigurationIdentifiers: List[str]
    maximumMessageLength: int
    maximumMessageRatePerSecond: int
    messageReviewHandler: MessageReviewHandlerTypeDef
    name: str
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RoomSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createTime: Optional[datetime] = None
    id: Optional[str] = None
    loggingConfigurationIdentifiers: Optional[List[str]] = None
    messageReviewHandler: Optional[MessageReviewHandlerTypeDef] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    updateTime: Optional[datetime] = None

class UpdateRoomRequestRequestTypeDef(BaseValidatorModel):
    identifier: str
    loggingConfigurationIdentifiers: Optional[Sequence[str]] = None
    maximumMessageLength: Optional[int] = None
    maximumMessageRatePerSecond: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandlerTypeDef] = None
    name: Optional[str] = None

class UpdateRoomResponseTypeDef(BaseValidatorModel):
    arn: str
    createTime: datetime
    id: str
    loggingConfigurationIdentifiers: List[str]
    maximumMessageLength: int
    maximumMessageRatePerSecond: int
    messageReviewHandler: MessageReviewHandlerTypeDef
    name: str
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationConfigurationTypeDef(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfigurationTypeDef] = None
    firehose: Optional[FirehoseDestinationConfigurationTypeDef] = None
    s3: Optional[S3DestinationConfigurationTypeDef] = None

class ListRoomsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    rooms: List[RoomSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    destinationConfiguration: DestinationConfigurationTypeDef
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    createTime: datetime
    destinationConfiguration: DestinationConfigurationTypeDef
    id: str
    name: str
    state: Literal["ACTIVE"]
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    createTime: datetime
    destinationConfiguration: DestinationConfigurationTypeDef
    id: str
    name: str
    state: LoggingConfigurationStateType
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createTime: Optional[datetime] = None
    destinationConfiguration: Optional[DestinationConfigurationTypeDef] = None
    id: Optional[str] = None
    name: Optional[str] = None
    state: Optional[LoggingConfigurationStateType] = None
    tags: Optional[Dict[str, str]] = None
    updateTime: Optional[datetime] = None

class UpdateLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    identifier: str
    destinationConfiguration: Optional[DestinationConfigurationTypeDef] = None
    name: Optional[str] = None

class UpdateLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    createTime: datetime
    destinationConfiguration: DestinationConfigurationTypeDef
    id: str
    name: str
    state: Literal["ACTIVE"]
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggingConfigurationsResponseTypeDef(BaseValidatorModel):
    loggingConfigurations: List[LoggingConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


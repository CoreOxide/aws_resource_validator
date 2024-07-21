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
from aws_resource_validator.pydantic_models.ivschat_constants import *

class CloudWatchLogsDestinationConfigurationTypeDef(BaseModel):
    logGroupName: str

class CreateChatTokenRequestRequestTypeDef(BaseModel):
    roomIdentifier: str
    userId: str
    attributes: Optional[Mapping[str, str]] = None
    capabilities: Optional[Sequence[ChatTokenCapabilityType]] = None
    sessionDurationInMinutes: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class MessageReviewHandlerTypeDef(BaseModel):
    fallbackResult: Optional[FallbackResultType] = None
    uri: Optional[str] = None

class DeleteLoggingConfigurationRequestRequestTypeDef(BaseModel):
    identifier: str

class DeleteMessageRequestRequestTypeDef(BaseModel):
    id: str
    roomIdentifier: str
    reason: Optional[str] = None

class DeleteRoomRequestRequestTypeDef(BaseModel):
    identifier: str

class FirehoseDestinationConfigurationTypeDef(BaseModel):
    deliveryStreamName: str

class S3DestinationConfigurationTypeDef(BaseModel):
    bucketName: str

class DisconnectUserRequestRequestTypeDef(BaseModel):
    roomIdentifier: str
    userId: str
    reason: Optional[str] = None

class GetLoggingConfigurationRequestRequestTypeDef(BaseModel):
    identifier: str

class GetRoomRequestRequestTypeDef(BaseModel):
    identifier: str

class ListLoggingConfigurationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRoomsRequestRequestTypeDef(BaseModel):
    loggingConfigurationIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    messageReviewHandlerUri: Optional[str] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class SendEventRequestRequestTypeDef(BaseModel):
    eventName: str
    roomIdentifier: str
    attributes: Optional[Mapping[str, str]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateChatTokenResponseTypeDef(BaseModel):
    sessionExpirationTime: datetime
    token: str
    tokenExpirationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMessageResponseTypeDef(BaseModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SendEventResponseTypeDef(BaseModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoomRequestRequestTypeDef(BaseModel):
    loggingConfigurationIdentifiers: Optional[Sequence[str]] = None
    maximumMessageLength: Optional[int] = None
    maximumMessageRatePerSecond: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandlerTypeDef] = None
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateRoomResponseTypeDef(BaseModel):
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

class GetRoomResponseTypeDef(BaseModel):
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

class RoomSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createTime: Optional[datetime] = None
    id: Optional[str] = None
    loggingConfigurationIdentifiers: Optional[List[str]] = None
    messageReviewHandler: Optional[MessageReviewHandlerTypeDef] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    updateTime: Optional[datetime] = None

class UpdateRoomRequestRequestTypeDef(BaseModel):
    identifier: str
    loggingConfigurationIdentifiers: Optional[Sequence[str]] = None
    maximumMessageLength: Optional[int] = None
    maximumMessageRatePerSecond: Optional[int] = None
    messageReviewHandler: Optional[MessageReviewHandlerTypeDef] = None
    name: Optional[str] = None

class UpdateRoomResponseTypeDef(BaseModel):
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

class DestinationConfigurationTypeDef(BaseModel):
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfigurationTypeDef] = None
    firehose: Optional[FirehoseDestinationConfigurationTypeDef] = None
    s3: Optional[S3DestinationConfigurationTypeDef] = None

class ListRoomsResponseTypeDef(BaseModel):
    nextToken: str
    rooms: List[RoomSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggingConfigurationRequestRequestTypeDef(BaseModel):
    destinationConfiguration: DestinationConfigurationTypeDef
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateLoggingConfigurationResponseTypeDef(BaseModel):
    arn: str
    createTime: datetime
    destinationConfiguration: DestinationConfigurationTypeDef
    id: str
    name: str
    state: Literal["ACTIVE"]
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoggingConfigurationResponseTypeDef(BaseModel):
    arn: str
    createTime: datetime
    destinationConfiguration: DestinationConfigurationTypeDef
    id: str
    name: str
    state: LoggingConfigurationStateType
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createTime: Optional[datetime] = None
    destinationConfiguration: Optional[DestinationConfigurationTypeDef] = None
    id: Optional[str] = None
    name: Optional[str] = None
    state: Optional[LoggingConfigurationStateType] = None
    tags: Optional[Dict[str, str]] = None
    updateTime: Optional[datetime] = None

class UpdateLoggingConfigurationRequestRequestTypeDef(BaseModel):
    identifier: str
    destinationConfiguration: Optional[DestinationConfigurationTypeDef] = None
    name: Optional[str] = None

class UpdateLoggingConfigurationResponseTypeDef(BaseModel):
    arn: str
    createTime: datetime
    destinationConfiguration: DestinationConfigurationTypeDef
    id: str
    name: str
    state: Literal["ACTIVE"]
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggingConfigurationsResponseTypeDef(BaseModel):
    loggingConfigurations: List[LoggingConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


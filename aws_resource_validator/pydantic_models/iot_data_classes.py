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
from aws_resource_validator.pydantic_models.iot_data_constants import *

class DeleteThingShadowRequestRequestTypeDef(BaseModel):
    thingName: str
    shadowName: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetRetainedMessageRequestRequestTypeDef(BaseModel):
    topic: str

class GetThingShadowRequestRequestTypeDef(BaseModel):
    thingName: str
    shadowName: Optional[str] = None

class ListNamedShadowsForThingRequestRequestTypeDef(BaseModel):
    thingName: str
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRetainedMessagesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RetainedMessageSummaryTypeDef(BaseModel):
    topic: Optional[str] = None
    payloadSize: Optional[int] = None
    qos: Optional[int] = None
    lastModifiedTime: Optional[int] = None

class PublishRequestRequestTypeDef(BaseModel):
    topic: str
    qos: Optional[int] = None
    retain: Optional[bool] = None
    payload: Optional[BlobTypeDef] = None
    userProperties: Optional[str] = None
    payloadFormatIndicator: Optional[PayloadFormatIndicatorType] = None
    contentType: Optional[str] = None
    responseTopic: Optional[str] = None
    correlationData: Optional[str] = None
    messageExpiry: Optional[int] = None

class UpdateThingShadowRequestRequestTypeDef(BaseModel):
    thingName: str
    payload: BlobTypeDef
    shadowName: Optional[str] = None

class DeleteThingShadowResponseTypeDef(BaseModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetRetainedMessageResponseTypeDef(BaseModel):
    topic: str
    payload: bytes
    qos: int
    lastModifiedTime: int
    userProperties: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GetThingShadowResponseTypeDef(BaseModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListNamedShadowsForThingResponseTypeDef(BaseModel):
    results: List[str]
    nextToken: str
    timestamp: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateThingShadowResponseTypeDef(BaseModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListRetainedMessagesRequestListRetainedMessagesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRetainedMessagesResponseTypeDef(BaseModel):
    retainedTopics: List[RetainedMessageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


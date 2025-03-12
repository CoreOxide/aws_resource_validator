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
from aws_resource_validator.pydantic_models.iot_data_constants import *

class DeleteThingShadowRequestTypeDef(BaseValidatorModel):
    thingName: str
    shadowName: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetRetainedMessageRequestTypeDef(BaseValidatorModel):
    topic: str


class GetThingShadowRequestTypeDef(BaseValidatorModel):
    thingName: str
    shadowName: Optional[str] = None


class ListNamedShadowsForThingRequestTypeDef(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRetainedMessagesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RetainedMessageSummaryTypeDef(BaseValidatorModel):
    topic: Optional[str] = None
    payloadSize: Optional[int] = None
    qos: Optional[int] = None
    lastModifiedTime: Optional[int] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class PublishRequestTypeDef(BaseValidatorModel):
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


class UpdateThingShadowRequestTypeDef(BaseValidatorModel):
    thingName: str
    payload: BlobTypeDef
    shadowName: Optional[str] = None


class DeleteThingShadowResponseTypeDef(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetRetainedMessageResponseTypeDef(BaseValidatorModel):
    topic: str
    payload: bytes
    qos: int
    lastModifiedTime: int
    userProperties: bytes
    ResponseMetadata: ResponseMetadataTypeDef


class GetThingShadowResponseTypeDef(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class ListNamedShadowsForThingResponseTypeDef(BaseValidatorModel):
    results: List[str]
    timestamp: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateThingShadowResponseTypeDef(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class ListRetainedMessagesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRetainedMessagesResponseTypeDef(BaseValidatorModel):
    retainedTopics: List[RetainedMessageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None



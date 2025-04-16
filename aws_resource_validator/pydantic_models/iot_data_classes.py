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

class DeleteThingShadowRequest(BaseValidatorModel):
    thingName: str
    shadowName: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetRetainedMessageRequest(BaseValidatorModel):
    topic: str


class GetThingShadowRequest(BaseValidatorModel):
    thingName: str
    shadowName: Optional[str] = None


class ListNamedShadowsForThingRequest(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRetainedMessagesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RetainedMessageSummary(BaseValidatorModel):
    topic: Optional[str] = None
    payloadSize: Optional[int] = None
    qos: Optional[int] = None
    lastModifiedTime: Optional[int] = None


class Blob(BaseValidatorModel):
    pass


class PublishRequest(BaseValidatorModel):
    topic: str
    qos: Optional[int] = None
    retain: Optional[bool] = None
    payload: Optional[Blob] = None
    userProperties: Optional[str] = None
    payloadFormatIndicator: Optional[PayloadFormatIndicatorType] = None
    contentType: Optional[str] = None
    responseTopic: Optional[str] = None
    correlationData: Optional[str] = None
    messageExpiry: Optional[int] = None


class UpdateThingShadowRequest(BaseValidatorModel):
    thingName: str
    payload: Blob
    shadowName: Optional[str] = None


class DeleteThingShadowResponse(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetRetainedMessageResponse(BaseValidatorModel):
    topic: str
    payload: bytes
    qos: int
    lastModifiedTime: int
    userProperties: bytes
    ResponseMetadata: ResponseMetadata


class GetThingShadowResponse(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadata


class ListNamedShadowsForThingResponse(BaseValidatorModel):
    results: List[str]
    timestamp: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateThingShadowResponse(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadata


class ListRetainedMessagesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRetainedMessagesResponse(BaseValidatorModel):
    retainedTopics: List[RetainedMessageSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None



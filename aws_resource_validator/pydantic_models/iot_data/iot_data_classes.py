from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iot_data.iot_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


# This class is the input for the 'delete_thing_shadow' function.
class DeleteThingShadowRequest(BaseValidatorModel):
    thingName: str
    shadowName: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'get_retained_message' function.
class GetRetainedMessageRequest(BaseValidatorModel):
    topic: str


# This class is the input for the 'get_thing_shadow' function.
class GetThingShadowRequest(BaseValidatorModel):
    thingName: str
    shadowName: Optional[str] = None


# This class is the input for the 'list_named_shadows_for_thing' function.
class ListNamedShadowsForThingRequest(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    pageSize: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_retained_messages' function.
class ListRetainedMessagesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RetainedMessageSummary(BaseValidatorModel):
    topic: Optional[str] = None
    payloadSize: Optional[int] = None
    qos: Optional[int] = None
    lastModifiedTime: Optional[int] = None


# This class is the input for the 'publish' function.
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


# This class is the input for the 'update_thing_shadow' function.
class UpdateThingShadowRequest(BaseValidatorModel):
    thingName: str
    payload: Blob
    shadowName: Optional[str] = None


# This class is the output for the 'delete_thing_shadow' function.
class DeleteThingShadowResponse(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'publish' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_retained_message' function.
class GetRetainedMessageResponse(BaseValidatorModel):
    topic: str
    payload: bytes
    qos: int
    lastModifiedTime: int
    userProperties: bytes
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_thing_shadow' function.
class GetThingShadowResponse(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_named_shadows_for_thing' function.
class ListNamedShadowsForThingResponse(BaseValidatorModel):
    results: List[str]
    timestamp: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_thing_shadow' function.
class UpdateThingShadowResponse(BaseValidatorModel):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadata


class ListRetainedMessagesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_retained_messages' function.
class ListRetainedMessagesResponse(BaseValidatorModel):
    retainedTopics: List[RetainedMessageSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None
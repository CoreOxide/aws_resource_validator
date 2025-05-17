from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.apigatewaymanagementapi.apigatewaymanagementapi_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


# This class is the input for the 'delete_connection' function.
class DeleteConnectionRequest(BaseValidatorModel):
    ConnectionId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'get_connection' function.
class GetConnectionRequest(BaseValidatorModel):
    ConnectionId: str


class Identity(BaseValidatorModel):
    SourceIp: str
    UserAgent: str


# This class is the input for the 'post_to_connection' function.
class PostToConnectionRequest(BaseValidatorModel):
    Data: Blob
    ConnectionId: str


# This class is the output for the 'post_to_connection' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_connection' function.
class GetConnectionResponse(BaseValidatorModel):
    ConnectedAt: datetime
    Identity: Identity
    LastActiveAt: datetime
    ResponseMetadata: ResponseMetadata
from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.apigatewaymanagementapi.apigatewaymanagementapi_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class DeleteConnectionRequest(BaseValidatorModel):
    ConnectionId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetConnectionRequest(BaseValidatorModel):
    ConnectionId: str


class Identity(BaseValidatorModel):
    SourceIp: str
    UserAgent: str


class PostToConnectionRequest(BaseValidatorModel):
    Data: Blob
    ConnectionId: str


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetConnectionResponse(BaseValidatorModel):
    ConnectedAt: datetime
    Identity: Identity
    LastActiveAt: datetime
    ResponseMetadata: ResponseMetadata
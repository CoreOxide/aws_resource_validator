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
from aws_resource_validator.pydantic_models.apigatewaymanagementapi_constants import *

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


class Blob(BaseValidatorModel):
    pass


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



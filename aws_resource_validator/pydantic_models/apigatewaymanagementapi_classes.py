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

class DeleteConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionId: str


class IdentityTypeDef(BaseValidatorModel):
    SourceIp: str
    UserAgent: str


class BlobTypeDef(BaseValidatorModel):
    pass


class PostToConnectionRequestTypeDef(BaseValidatorModel):
    Data: BlobTypeDef
    ConnectionId: str


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetConnectionResponseTypeDef(BaseValidatorModel):
    ConnectedAt: datetime
    Identity: IdentityTypeDef
    LastActiveAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef



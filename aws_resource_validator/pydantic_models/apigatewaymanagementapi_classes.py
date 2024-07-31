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
from aws_resource_validator.pydantic_models.apigatewaymanagementapi_constants import *

class DeleteConnectionRequestRequestTypeDef(BaseModel):
    ConnectionId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetConnectionRequestRequestTypeDef(BaseModel):
    ConnectionId: str

class IdentityTypeDef(BaseModel):
    SourceIp: str
    UserAgent: str

class PostToConnectionRequestRequestTypeDef(BaseModel):
    Data: BlobTypeDef
    ConnectionId: str

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionResponseTypeDef(BaseModel):
    ConnectedAt: datetime
    Identity: IdentityTypeDef
    LastActiveAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


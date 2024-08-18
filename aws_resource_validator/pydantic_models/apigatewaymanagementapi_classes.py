from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class DeleteConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionId: str

class IdentityTypeDef(BaseValidatorModel):
    SourceIp: str
    UserAgent: str

class PostToConnectionRequestRequestTypeDef(BaseValidatorModel):
    Data: BlobTypeDef
    ConnectionId: str

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionResponseTypeDef(BaseValidatorModel):
    ConnectedAt: datetime
    Identity: IdentityTypeDef
    LastActiveAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


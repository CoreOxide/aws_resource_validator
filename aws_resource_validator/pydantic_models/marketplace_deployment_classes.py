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
from aws_resource_validator.pydantic_models.marketplace_deployment_constants import *

class DeploymentParameterInputTypeDef(BaseModel):
    name: str
    secretString: str

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeploymentParameterResponseTypeDef(BaseModel):
    agreementId: str
    deploymentParameterId: str
    resourceArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeploymentParameterRequestRequestTypeDef(BaseModel):
    agreementId: str
    catalog: str
    deploymentParameter: DeploymentParameterInputTypeDef
    productId: str
    clientToken: Optional[str] = None
    expirationDate: Optional[TimestampTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


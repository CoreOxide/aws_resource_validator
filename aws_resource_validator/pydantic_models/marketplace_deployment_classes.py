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
from aws_resource_validator.pydantic_models.marketplace_deployment_constants import *

class DeploymentParameterInputTypeDef(BaseValidatorModel):
    name: str
    secretString: str

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeploymentParameterResponseTypeDef(BaseValidatorModel):
    agreementId: str
    deploymentParameterId: str
    resourceArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeploymentParameterRequestRequestTypeDef(BaseValidatorModel):
    agreementId: str
    catalog: str
    deploymentParameter: DeploymentParameterInputTypeDef
    productId: str
    clientToken: Optional[str] = None
    expirationDate: Optional[TimestampTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


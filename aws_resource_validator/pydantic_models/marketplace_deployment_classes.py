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
from aws_resource_validator.pydantic_models.marketplace_deployment_constants import *

class DeploymentParameterInput(BaseValidatorModel):
    name: str
    secretString: str


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Optional[Mapping[str, str]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutDeploymentParameterResponse(BaseValidatorModel):
    agreementId: str
    deploymentParameterId: str
    resourceArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class PutDeploymentParameterRequest(BaseValidatorModel):
    agreementId: str
    catalog: str
    deploymentParameter: DeploymentParameterInput
    productId: str
    clientToken: Optional[str] = None
    expirationDate: Optional[Timestamp] = None
    tags: Optional[Mapping[str, str]] = None



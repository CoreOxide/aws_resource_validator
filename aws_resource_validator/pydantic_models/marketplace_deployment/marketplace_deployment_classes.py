from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.marketplace_deployment.marketplace_deployment_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DeploymentParameterInput(BaseValidatorModel):
    name: str
    secretString: str


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Timestamp = Union[datetime, str]


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Optional[Dict[str, str]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_deployment_parameter' function.
class PutDeploymentParameterResponse(BaseValidatorModel):
    agreementId: str
    deploymentParameterId: str
    resourceArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_deployment_parameter' function.
class PutDeploymentParameterRequest(BaseValidatorModel):
    agreementId: str
    catalog: str
    deploymentParameter: DeploymentParameterInput
    productId: str
    clientToken: Optional[str] = None
    expirationDate: Optional[Timestamp] = None
    tags: Optional[Dict[str, str]] = None
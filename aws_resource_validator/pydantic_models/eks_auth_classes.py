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
from aws_resource_validator.pydantic_models.eks_auth_constants import *

class AssumeRoleForPodIdentityRequest(BaseValidatorModel):
    clusterName: str
    token: str


class AssumedRoleUser(BaseValidatorModel):
    arn: str
    assumeRoleId: str


class Credentials(BaseValidatorModel):
    sessionToken: str
    secretAccessKey: str
    accessKeyId: str
    expiration: datetime


class PodIdentityAssociation(BaseValidatorModel):
    associationArn: str
    associationId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Subject(BaseValidatorModel):
    namespace: str
    serviceAccount: str


class AssumeRoleForPodIdentityResponse(BaseValidatorModel):
    subject: Subject
    audience: str
    podIdentityAssociation: PodIdentityAssociation
    assumedRoleUser: AssumedRoleUser
    credentials: Credentials
    ResponseMetadata: ResponseMetadata



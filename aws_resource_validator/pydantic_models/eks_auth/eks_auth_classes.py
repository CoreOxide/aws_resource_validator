from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.eks_auth.eks_auth_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
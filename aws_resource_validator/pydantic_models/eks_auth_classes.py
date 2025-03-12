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

class AssumeRoleForPodIdentityRequestTypeDef(BaseValidatorModel):
    clusterName: str
    token: str


class AssumedRoleUserTypeDef(BaseValidatorModel):
    arn: str
    assumeRoleId: str


class CredentialsTypeDef(BaseValidatorModel):
    sessionToken: str
    secretAccessKey: str
    accessKeyId: str
    expiration: datetime


class PodIdentityAssociationTypeDef(BaseValidatorModel):
    associationArn: str
    associationId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SubjectTypeDef(BaseValidatorModel):
    namespace: str
    serviceAccount: str


class AssumeRoleForPodIdentityResponseTypeDef(BaseValidatorModel):
    subject: SubjectTypeDef
    audience: str
    podIdentityAssociation: PodIdentityAssociationTypeDef
    assumedRoleUser: AssumedRoleUserTypeDef
    credentials: CredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



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
from aws_resource_validator.pydantic_models.eks_auth_constants import *

class AssumeRoleForPodIdentityRequestRequestTypeDef(BaseModel):
    clusterName: str
    token: str

class AssumedRoleUserTypeDef(BaseModel):
    arn: str
    assumeRoleId: str

class CredentialsTypeDef(BaseModel):
    sessionToken: str
    secretAccessKey: str
    accessKeyId: str
    expiration: datetime

class PodIdentityAssociationTypeDef(BaseModel):
    associationArn: str
    associationId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class SubjectTypeDef(BaseModel):
    namespace: str
    serviceAccount: str

class AssumeRoleForPodIdentityResponseTypeDef(BaseModel):
    subject: SubjectTypeDef
    audience: str
    podIdentityAssociation: PodIdentityAssociationTypeDef
    assumedRoleUser: AssumedRoleUserTypeDef
    credentials: CredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


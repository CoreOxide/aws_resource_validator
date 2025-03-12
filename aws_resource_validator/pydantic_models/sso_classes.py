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
from aws_resource_validator.pydantic_models.sso_constants import *

class AccountInfoTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    accountName: Optional[str] = None
    emailAddress: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetRoleCredentialsRequestTypeDef(BaseValidatorModel):
    roleName: str
    accountId: str
    accessToken: str


class RoleCredentialsTypeDef(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None
    expiration: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccountRolesRequestTypeDef(BaseValidatorModel):
    accessToken: str
    accountId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RoleInfoTypeDef(BaseValidatorModel):
    roleName: Optional[str] = None
    accountId: Optional[str] = None


class ListAccountsRequestTypeDef(BaseValidatorModel):
    accessToken: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class LogoutRequestTypeDef(BaseValidatorModel):
    accessToken: str


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccountsResponseTypeDef(BaseValidatorModel):
    accountList: List[AccountInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetRoleCredentialsResponseTypeDef(BaseValidatorModel):
    roleCredentials: RoleCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccountRolesRequestPaginateTypeDef(BaseValidatorModel):
    accessToken: str
    accountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountsRequestPaginateTypeDef(BaseValidatorModel):
    accessToken: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountRolesResponseTypeDef(BaseValidatorModel):
    roleList: List[RoleInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None



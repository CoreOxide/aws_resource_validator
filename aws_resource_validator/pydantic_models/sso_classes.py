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

class AccountInfo(BaseValidatorModel):
    accountId: Optional[str] = None
    accountName: Optional[str] = None
    emailAddress: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetRoleCredentialsRequest(BaseValidatorModel):
    roleName: str
    accountId: str
    accessToken: str


class RoleCredentials(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None
    expiration: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccountRolesRequest(BaseValidatorModel):
    accessToken: str
    accountId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RoleInfo(BaseValidatorModel):
    roleName: Optional[str] = None
    accountId: Optional[str] = None


class ListAccountsRequest(BaseValidatorModel):
    accessToken: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class LogoutRequest(BaseValidatorModel):
    accessToken: str


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListAccountsResponse(BaseValidatorModel):
    accountList: List[AccountInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetRoleCredentialsResponse(BaseValidatorModel):
    roleCredentials: RoleCredentials
    ResponseMetadata: ResponseMetadata


class ListAccountRolesRequestPaginate(BaseValidatorModel):
    accessToken: str
    accountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountsRequestPaginate(BaseValidatorModel):
    accessToken: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountRolesResponse(BaseValidatorModel):
    roleList: List[RoleInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None



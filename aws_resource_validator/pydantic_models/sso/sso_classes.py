from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sso.sso_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'get_role_credentials' function.
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


# This class is the input for the 'list_account_roles' function.
class ListAccountRolesRequest(BaseValidatorModel):
    accessToken: str
    accountId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RoleInfo(BaseValidatorModel):
    roleName: Optional[str] = None
    accountId: Optional[str] = None


# This class is the input for the 'list_accounts' function.
class ListAccountsRequest(BaseValidatorModel):
    accessToken: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'logout' function.
class LogoutRequest(BaseValidatorModel):
    accessToken: str


# This class is the output for the 'logout' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_accounts' function.
class ListAccountsResponse(BaseValidatorModel):
    accountList: List[AccountInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_role_credentials' function.
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


# This class is the output for the 'list_account_roles' function.
class ListAccountRolesResponse(BaseValidatorModel):
    roleList: List[RoleInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None
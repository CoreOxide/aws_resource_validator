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
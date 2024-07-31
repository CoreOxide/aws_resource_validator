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
from aws_resource_validator.pydantic_models.sso_constants import *

class AccountInfoTypeDef(BaseModel):
    accountId: Optional[str] = None
    accountName: Optional[str] = None
    emailAddress: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetRoleCredentialsRequestRequestTypeDef(BaseModel):
    roleName: str
    accountId: str
    accessToken: str

class RoleCredentialsTypeDef(BaseModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None
    expiration: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccountRolesRequestRequestTypeDef(BaseModel):
    accessToken: str
    accountId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RoleInfoTypeDef(BaseModel):
    roleName: Optional[str] = None
    accountId: Optional[str] = None

class ListAccountsRequestRequestTypeDef(BaseModel):
    accessToken: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class LogoutRequestRequestTypeDef(BaseModel):
    accessToken: str

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsResponseTypeDef(BaseModel):
    nextToken: str
    accountList: List[AccountInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoleCredentialsResponseTypeDef(BaseModel):
    roleCredentials: RoleCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountRolesRequestListAccountRolesPaginateTypeDef(BaseModel):
    accessToken: str
    accountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountsRequestListAccountsPaginateTypeDef(BaseModel):
    accessToken: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountRolesResponseTypeDef(BaseModel):
    nextToken: str
    roleList: List[RoleInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


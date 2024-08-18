from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetRoleCredentialsRequestRequestTypeDef(BaseValidatorModel):
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

class ListAccountRolesRequestRequestTypeDef(BaseValidatorModel):
    accessToken: str
    accountId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RoleInfoTypeDef(BaseValidatorModel):
    roleName: Optional[str] = None
    accountId: Optional[str] = None

class ListAccountsRequestRequestTypeDef(BaseValidatorModel):
    accessToken: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class LogoutRequestRequestTypeDef(BaseValidatorModel):
    accessToken: str

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    accountList: List[AccountInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoleCredentialsResponseTypeDef(BaseValidatorModel):
    roleCredentials: RoleCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountRolesRequestListAccountRolesPaginateTypeDef(BaseValidatorModel):
    accessToken: str
    accountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountsRequestListAccountsPaginateTypeDef(BaseValidatorModel):
    accessToken: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountRolesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    roleList: List[RoleInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


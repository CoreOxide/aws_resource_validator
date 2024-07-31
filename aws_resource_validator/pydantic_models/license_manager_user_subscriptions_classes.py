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
from aws_resource_validator.pydantic_models.license_manager_user_subscriptions_constants import *

class ActiveDirectoryIdentityProviderTypeDef(BaseModel):
    DirectoryId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FilterTypeDef(BaseModel):
    Attribute: Optional[str] = None
    Operation: Optional[str] = None
    Value: Optional[str] = None

class SettingsTypeDef(BaseModel):
    SecurityGroupId: str
    Subnets: List[str]

class InstanceSummaryTypeDef(BaseModel):
    InstanceId: str
    Products: List[str]
    Status: str
    LastStatusCheckDate: Optional[str] = None
    StatusMessage: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListIdentityProvidersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UpdateSettingsTypeDef(BaseModel):
    AddSubnets: Sequence[str]
    RemoveSubnets: Sequence[str]
    SecurityGroupId: Optional[str] = None

class IdentityProviderTypeDef(BaseModel):
    ActiveDirectoryIdentityProvider: Optional[ActiveDirectoryIdentityProviderTypeDef] = None

class ListInstancesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInstancesResponseTypeDef(BaseModel):
    InstanceSummaries: List[InstanceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstancesRequestListInstancesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class AssociateUserRequestRequestTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Username: str
    Domain: Optional[str] = None

class DeregisterIdentityProviderRequestRequestTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str

class DisassociateUserRequestRequestTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Username: str
    Domain: Optional[str] = None

class IdentityProviderSummaryTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Settings: SettingsTypeDef
    Status: str
    FailureMessage: Optional[str] = None

class InstanceUserSummaryTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Status: str
    Username: str
    AssociationDate: Optional[str] = None
    DisassociationDate: Optional[str] = None
    Domain: Optional[str] = None
    StatusMessage: Optional[str] = None

class ListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProductSubscriptionsRequestRequestTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListUserAssociationsRequestListUserAssociationsPaginateTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserAssociationsRequestRequestTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ProductUserSummaryTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Status: str
    Username: str
    Domain: Optional[str] = None
    StatusMessage: Optional[str] = None
    SubscriptionEndDate: Optional[str] = None
    SubscriptionStartDate: Optional[str] = None

class RegisterIdentityProviderRequestRequestTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Settings: Optional[SettingsTypeDef] = None

class StartProductSubscriptionRequestRequestTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Username: str
    Domain: Optional[str] = None

class StopProductSubscriptionRequestRequestTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Username: str
    Domain: Optional[str] = None

class UpdateIdentityProviderSettingsRequestRequestTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    UpdateSettings: UpdateSettingsTypeDef

class DeregisterIdentityProviderResponseTypeDef(BaseModel):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityProvidersResponseTypeDef(BaseModel):
    IdentityProviderSummaries: List[IdentityProviderSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterIdentityProviderResponseTypeDef(BaseModel):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentityProviderSettingsResponseTypeDef(BaseModel):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateUserResponseTypeDef(BaseModel):
    InstanceUserSummary: InstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateUserResponseTypeDef(BaseModel):
    InstanceUserSummary: InstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserAssociationsResponseTypeDef(BaseModel):
    InstanceUserSummaries: List[InstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProductSubscriptionsResponseTypeDef(BaseModel):
    NextToken: str
    ProductUserSummaries: List[ProductUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartProductSubscriptionResponseTypeDef(BaseModel):
    ProductUserSummary: ProductUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopProductSubscriptionResponseTypeDef(BaseModel):
    ProductUserSummary: ProductUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


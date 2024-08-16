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
from aws_resource_validator.pydantic_models.license_manager_user_subscriptions_constants import *

class ActiveDirectoryIdentityProviderTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FilterTypeDef(BaseValidatorModel):
    Attribute: Optional[str] = None
    Operation: Optional[str] = None
    Value: Optional[str] = None

class SettingsTypeDef(BaseValidatorModel):
    SecurityGroupId: str
    Subnets: List[str]

class InstanceSummaryTypeDef(BaseValidatorModel):
    InstanceId: str
    Products: List[str]
    Status: str
    LastStatusCheckDate: Optional[str] = None
    StatusMessage: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListIdentityProvidersRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UpdateSettingsTypeDef(BaseValidatorModel):
    AddSubnets: Sequence[str]
    RemoveSubnets: Sequence[str]
    SecurityGroupId: Optional[str] = None

class IdentityProviderTypeDef(BaseValidatorModel):
    ActiveDirectoryIdentityProvider: Optional[ActiveDirectoryIdentityProviderTypeDef] = None

class ListInstancesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInstancesResponseTypeDef(BaseValidatorModel):
    InstanceSummaries: List[InstanceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstancesRequestListInstancesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class AssociateUserRequestRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Username: str
    Domain: Optional[str] = None

class DeregisterIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str

class DisassociateUserRequestRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Username: str
    Domain: Optional[str] = None

class IdentityProviderSummaryTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Settings: SettingsTypeDef
    Status: str
    FailureMessage: Optional[str] = None

class InstanceUserSummaryTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Status: str
    Username: str
    AssociationDate: Optional[str] = None
    DisassociationDate: Optional[str] = None
    Domain: Optional[str] = None
    StatusMessage: Optional[str] = None

class ListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProductSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListUserAssociationsRequestListUserAssociationsPaginateTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserAssociationsRequestRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    InstanceId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ProductUserSummaryTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Status: str
    Username: str
    Domain: Optional[str] = None
    StatusMessage: Optional[str] = None
    SubscriptionEndDate: Optional[str] = None
    SubscriptionStartDate: Optional[str] = None

class RegisterIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Settings: Optional[SettingsTypeDef] = None

class StartProductSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Username: str
    Domain: Optional[str] = None

class StopProductSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    Username: str
    Domain: Optional[str] = None

class UpdateIdentityProviderSettingsRequestRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeDef
    Product: str
    UpdateSettings: UpdateSettingsTypeDef

class DeregisterIdentityProviderResponseTypeDef(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityProvidersResponseTypeDef(BaseValidatorModel):
    IdentityProviderSummaries: List[IdentityProviderSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterIdentityProviderResponseTypeDef(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentityProviderSettingsResponseTypeDef(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateUserResponseTypeDef(BaseValidatorModel):
    InstanceUserSummary: InstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateUserResponseTypeDef(BaseValidatorModel):
    InstanceUserSummary: InstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserAssociationsResponseTypeDef(BaseValidatorModel):
    InstanceUserSummaries: List[InstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProductSubscriptionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ProductUserSummaries: List[ProductUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartProductSubscriptionResponseTypeDef(BaseValidatorModel):
    ProductUserSummary: ProductUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopProductSubscriptionResponseTypeDef(BaseValidatorModel):
    ProductUserSummary: ProductUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


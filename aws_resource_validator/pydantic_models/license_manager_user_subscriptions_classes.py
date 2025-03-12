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
from aws_resource_validator.pydantic_models.license_manager_user_subscriptions_constants import *

class DomainNetworkSettingsOutputTypeDef(BaseValidatorModel):
    Subnets: List[str]


class DomainNetworkSettingsTypeDef(BaseValidatorModel):
    Subnets: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SecretsManagerCredentialsProviderTypeDef(BaseValidatorModel):
    SecretId: Optional[str] = None


class DeleteLicenseServerEndpointRequestTypeDef(BaseValidatorModel):
    LicenseServerEndpointArn: str
    ServerType: Literal["RDS_SAL"]


class FilterTypeDef(BaseValidatorModel):
    Attribute: Optional[str] = None
    Operation: Optional[str] = None
    Value: Optional[str] = None


class SettingsOutputTypeDef(BaseValidatorModel):
    SecurityGroupId: str
    Subnets: List[str]


class InstanceSummaryTypeDef(BaseValidatorModel):
    InstanceId: str
    Products: List[str]
    Status: str
    LastStatusCheckDate: Optional[str] = None
    StatusMessage: Optional[str] = None


class LicenseServerTypeDef(BaseValidatorModel):
    HealthStatus: Optional[LicenseServerHealthStatusType] = None
    Ipv4Address: Optional[str] = None
    ProvisioningStatus: Optional[LicenseServerEndpointProvisioningStatusType] = None


class ServerEndpointTypeDef(BaseValidatorModel):
    Endpoint: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class SettingsTypeDef(BaseValidatorModel):
    SecurityGroupId: str
    Subnets: Sequence[str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateSettingsTypeDef(BaseValidatorModel):
    AddSubnets: Sequence[str]
    RemoveSubnets: Sequence[str]
    SecurityGroupId: Optional[str] = None


class CreateLicenseServerEndpointResponseTypeDef(BaseValidatorModel):
    IdentityProviderArn: str
    LicenseServerEndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CredentialsProviderTypeDef(BaseValidatorModel):
    SecretsManagerCredentialsProvider: Optional[SecretsManagerCredentialsProviderTypeDef] = None


class ListIdentityProvidersRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInstancesRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLicenseServerEndpointsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInstancesResponseTypeDef(BaseValidatorModel):
    InstanceSummaries: List[InstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LicenseServerEndpointTypeDef(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    IdentityProviderArn: Optional[str] = None
    LicenseServerEndpointArn: Optional[str] = None
    LicenseServerEndpointId: Optional[str] = None
    LicenseServerEndpointProvisioningStatus: Optional[ LicenseServerEndpointProvisioningStatusType ] = None
    LicenseServers: Optional[List[LicenseServerTypeDef]] = None
    ServerEndpoint: Optional[ServerEndpointTypeDef] = None
    ServerType: Optional[Literal["RDS_SAL"]] = None
    StatusMessage: Optional[str] = None


class ListIdentityProvidersRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstancesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLicenseServerEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ActiveDirectorySettingsOutputTypeDef(BaseValidatorModel):
    DomainCredentialsProvider: Optional[CredentialsProviderTypeDef] = None
    DomainIpv4List: Optional[List[str]] = None
    DomainName: Optional[str] = None
    DomainNetworkSettings: Optional[DomainNetworkSettingsOutputTypeDef] = None


class ActiveDirectorySettingsTypeDef(BaseValidatorModel):
    DomainCredentialsProvider: Optional[CredentialsProviderTypeDef] = None
    DomainIpv4List: Optional[Sequence[str]] = None
    DomainName: Optional[str] = None
    DomainNetworkSettings: Optional[DomainNetworkSettingsTypeDef] = None


class RdsSalSettingsTypeDef(BaseValidatorModel):
    RdsSalCredentialsProvider: CredentialsProviderTypeDef


class DeleteLicenseServerEndpointResponseTypeDef(BaseValidatorModel):
    LicenseServerEndpoint: LicenseServerEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLicenseServerEndpointsResponseTypeDef(BaseValidatorModel):
    LicenseServerEndpoints: List[LicenseServerEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ActiveDirectoryIdentityProviderOutputTypeDef(BaseValidatorModel):
    ActiveDirectorySettings: Optional[ActiveDirectorySettingsOutputTypeDef] = None
    ActiveDirectoryType: Optional[ActiveDirectoryTypeType] = None
    DirectoryId: Optional[str] = None


class ActiveDirectoryIdentityProviderTypeDef(BaseValidatorModel):
    ActiveDirectorySettings: Optional[ActiveDirectorySettingsTypeDef] = None
    ActiveDirectoryType: Optional[ActiveDirectoryTypeType] = None
    DirectoryId: Optional[str] = None


class ServerSettingsTypeDef(BaseValidatorModel):
    RdsSalSettings: Optional[RdsSalSettingsTypeDef] = None


class IdentityProviderOutputTypeDef(BaseValidatorModel):
    ActiveDirectoryIdentityProvider: Optional[ActiveDirectoryIdentityProviderOutputTypeDef] = None


class IdentityProviderTypeDef(BaseValidatorModel):
    ActiveDirectoryIdentityProvider: Optional[ActiveDirectoryIdentityProviderTypeDef] = None


class LicenseServerSettingsTypeDef(BaseValidatorModel):
    ServerSettings: ServerSettingsTypeDef
    ServerType: Literal["RDS_SAL"]


class IdentityProviderSummaryTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderOutputTypeDef
    Product: str
    Settings: SettingsOutputTypeDef
    Status: str
    FailureMessage: Optional[str] = None
    IdentityProviderArn: Optional[str] = None


class InstanceUserSummaryTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderOutputTypeDef
    InstanceId: str
    Status: str
    Username: str
    AssociationDate: Optional[str] = None
    DisassociationDate: Optional[str] = None
    Domain: Optional[str] = None
    InstanceUserArn: Optional[str] = None
    StatusMessage: Optional[str] = None


class ProductUserSummaryTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderOutputTypeDef
    Product: str
    Status: str
    Username: str
    Domain: Optional[str] = None
    ProductUserArn: Optional[str] = None
    StatusMessage: Optional[str] = None
    SubscriptionEndDate: Optional[str] = None
    SubscriptionStartDate: Optional[str] = None


class CreateLicenseServerEndpointRequestTypeDef(BaseValidatorModel):
    IdentityProviderArn: str
    LicenseServerSettings: LicenseServerSettingsTypeDef
    Tags: Optional[Mapping[str, str]] = None


class DeregisterIdentityProviderResponseTypeDef(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListIdentityProvidersResponseTypeDef(BaseValidatorModel):
    IdentityProviderSummaries: List[IdentityProviderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProductSubscriptionsResponseTypeDef(BaseValidatorModel):
    ProductUserSummaries: List[ProductUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StartProductSubscriptionResponseTypeDef(BaseValidatorModel):
    ProductUserSummary: ProductUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopProductSubscriptionResponseTypeDef(BaseValidatorModel):
    ProductUserSummary: ProductUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IdentityProviderUnionTypeDef(BaseValidatorModel):
    pass


class AssociateUserRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnionTypeDef
    InstanceId: str
    Username: str
    Domain: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class DeregisterIdentityProviderRequestTypeDef(BaseValidatorModel):
    IdentityProvider: Optional[IdentityProviderUnionTypeDef] = None
    IdentityProviderArn: Optional[str] = None
    Product: Optional[str] = None


class DisassociateUserRequestTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    IdentityProvider: Optional[IdentityProviderUnionTypeDef] = None
    InstanceId: Optional[str] = None
    InstanceUserArn: Optional[str] = None
    Username: Optional[str] = None


class ListProductSubscriptionsRequestPaginateTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnionTypeDef
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Product: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProductSubscriptionsRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnionTypeDef
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Product: Optional[str] = None


class ListUserAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnionTypeDef
    InstanceId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUserAssociationsRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnionTypeDef
    InstanceId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SettingsUnionTypeDef(BaseValidatorModel):
    pass


class RegisterIdentityProviderRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnionTypeDef
    Product: str
    Settings: Optional[SettingsUnionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class StartProductSubscriptionRequestTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnionTypeDef
    Product: str
    Username: str
    Domain: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class StopProductSubscriptionRequestTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    IdentityProvider: Optional[IdentityProviderUnionTypeDef] = None
    Product: Optional[str] = None
    ProductUserArn: Optional[str] = None
    Username: Optional[str] = None


class UpdateIdentityProviderSettingsRequestTypeDef(BaseValidatorModel):
    UpdateSettings: UpdateSettingsTypeDef
    IdentityProvider: Optional[IdentityProviderUnionTypeDef] = None
    IdentityProviderArn: Optional[str] = None
    Product: Optional[str] = None



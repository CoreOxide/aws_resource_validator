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

class DomainNetworkSettingsOutput(BaseValidatorModel):
    Subnets: List[str]


class DomainNetworkSettings(BaseValidatorModel):
    Subnets: Sequence[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SecretsManagerCredentialsProvider(BaseValidatorModel):
    SecretId: Optional[str] = None


class DeleteLicenseServerEndpointRequest(BaseValidatorModel):
    LicenseServerEndpointArn: str
    ServerType: Literal["RDS_SAL"]


class Filter(BaseValidatorModel):
    Attribute: Optional[str] = None
    Operation: Optional[str] = None
    Value: Optional[str] = None


class SettingsOutput(BaseValidatorModel):
    SecurityGroupId: str
    Subnets: List[str]


class InstanceSummary(BaseValidatorModel):
    InstanceId: str
    Products: List[str]
    Status: str
    LastStatusCheckDate: Optional[str] = None
    StatusMessage: Optional[str] = None


class LicenseServer(BaseValidatorModel):
    HealthStatus: Optional[LicenseServerHealthStatusType] = None
    Ipv4Address: Optional[str] = None
    ProvisioningStatus: Optional[LicenseServerEndpointProvisioningStatusType] = None


class ServerEndpoint(BaseValidatorModel):
    Endpoint: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class Settings(BaseValidatorModel):
    SecurityGroupId: str
    Subnets: Sequence[str]


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateSettings(BaseValidatorModel):
    AddSubnets: Sequence[str]
    RemoveSubnets: Sequence[str]
    SecurityGroupId: Optional[str] = None


class CreateLicenseServerEndpointResponse(BaseValidatorModel):
    IdentityProviderArn: str
    LicenseServerEndpointArn: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CredentialsProvider(BaseValidatorModel):
    SecretsManagerCredentialsProvider: Optional[SecretsManagerCredentialsProvider] = None


class ListIdentityProvidersRequest(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInstancesRequest(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLicenseServerEndpointsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInstancesResponse(BaseValidatorModel):
    InstanceSummaries: List[InstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LicenseServerEndpoint(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    IdentityProviderArn: Optional[str] = None
    LicenseServerEndpointArn: Optional[str] = None
    LicenseServerEndpointId: Optional[str] = None
    LicenseServerEndpointProvisioningStatus: Optional[ LicenseServerEndpointProvisioningStatusType ] = None
    LicenseServers: Optional[List[LicenseServer]] = None
    ServerEndpoint: Optional[ServerEndpoint] = None
    ServerType: Optional[Literal["RDS_SAL"]] = None
    StatusMessage: Optional[str] = None


class ListIdentityProvidersRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstancesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLicenseServerEndpointsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ActiveDirectorySettingsOutput(BaseValidatorModel):
    DomainCredentialsProvider: Optional[CredentialsProvider] = None
    DomainIpv4List: Optional[List[str]] = None
    DomainName: Optional[str] = None
    DomainNetworkSettings: Optional[DomainNetworkSettingsOutput] = None


class ActiveDirectorySettings(BaseValidatorModel):
    DomainCredentialsProvider: Optional[CredentialsProvider] = None
    DomainIpv4List: Optional[Sequence[str]] = None
    DomainName: Optional[str] = None
    DomainNetworkSettings: Optional[DomainNetworkSettings] = None


class RdsSalSettings(BaseValidatorModel):
    RdsSalCredentialsProvider: CredentialsProvider


class DeleteLicenseServerEndpointResponse(BaseValidatorModel):
    LicenseServerEndpoint: LicenseServerEndpoint
    ResponseMetadata: ResponseMetadata


class ListLicenseServerEndpointsResponse(BaseValidatorModel):
    LicenseServerEndpoints: List[LicenseServerEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ActiveDirectoryIdentityProviderOutput(BaseValidatorModel):
    ActiveDirectorySettings: Optional[ActiveDirectorySettingsOutput] = None
    ActiveDirectoryType: Optional[ActiveDirectoryTypeType] = None
    DirectoryId: Optional[str] = None


class ActiveDirectoryIdentityProvider(BaseValidatorModel):
    ActiveDirectorySettings: Optional[ActiveDirectorySettings] = None
    ActiveDirectoryType: Optional[ActiveDirectoryTypeType] = None
    DirectoryId: Optional[str] = None


class ServerSettings(BaseValidatorModel):
    RdsSalSettings: Optional[RdsSalSettings] = None


class IdentityProviderOutput(BaseValidatorModel):
    ActiveDirectoryIdentityProvider: Optional[ActiveDirectoryIdentityProviderOutput] = None


class IdentityProvider(BaseValidatorModel):
    ActiveDirectoryIdentityProvider: Optional[ActiveDirectoryIdentityProvider] = None


class LicenseServerSettings(BaseValidatorModel):
    ServerSettings: ServerSettings
    ServerType: Literal["RDS_SAL"]


class IdentityProviderSummary(BaseValidatorModel):
    IdentityProvider: IdentityProviderOutput
    Product: str
    Settings: SettingsOutput
    Status: str
    FailureMessage: Optional[str] = None
    IdentityProviderArn: Optional[str] = None


class InstanceUserSummary(BaseValidatorModel):
    IdentityProvider: IdentityProviderOutput
    InstanceId: str
    Status: str
    Username: str
    AssociationDate: Optional[str] = None
    DisassociationDate: Optional[str] = None
    Domain: Optional[str] = None
    InstanceUserArn: Optional[str] = None
    StatusMessage: Optional[str] = None


class ProductUserSummary(BaseValidatorModel):
    IdentityProvider: IdentityProviderOutput
    Product: str
    Status: str
    Username: str
    Domain: Optional[str] = None
    ProductUserArn: Optional[str] = None
    StatusMessage: Optional[str] = None
    SubscriptionEndDate: Optional[str] = None
    SubscriptionStartDate: Optional[str] = None


class CreateLicenseServerEndpointRequest(BaseValidatorModel):
    IdentityProviderArn: str
    LicenseServerSettings: LicenseServerSettings
    Tags: Optional[Mapping[str, str]] = None


class DeregisterIdentityProviderResponse(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummary
    ResponseMetadata: ResponseMetadata


class ListIdentityProvidersResponse(BaseValidatorModel):
    IdentityProviderSummaries: List[IdentityProviderSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RegisterIdentityProviderResponse(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummary
    ResponseMetadata: ResponseMetadata


class UpdateIdentityProviderSettingsResponse(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummary
    ResponseMetadata: ResponseMetadata


class AssociateUserResponse(BaseValidatorModel):
    InstanceUserSummary: InstanceUserSummary
    ResponseMetadata: ResponseMetadata


class DisassociateUserResponse(BaseValidatorModel):
    InstanceUserSummary: InstanceUserSummary
    ResponseMetadata: ResponseMetadata


class ListUserAssociationsResponse(BaseValidatorModel):
    InstanceUserSummaries: List[InstanceUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProductSubscriptionsResponse(BaseValidatorModel):
    ProductUserSummaries: List[ProductUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartProductSubscriptionResponse(BaseValidatorModel):
    ProductUserSummary: ProductUserSummary
    ResponseMetadata: ResponseMetadata


class StopProductSubscriptionResponse(BaseValidatorModel):
    ProductUserSummary: ProductUserSummary
    ResponseMetadata: ResponseMetadata


class IdentityProviderUnion(BaseValidatorModel):
    pass


class AssociateUserRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    InstanceId: str
    Username: str
    Domain: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class DeregisterIdentityProviderRequest(BaseValidatorModel):
    IdentityProvider: Optional[IdentityProviderUnion] = None
    IdentityProviderArn: Optional[str] = None
    Product: Optional[str] = None


class DisassociateUserRequest(BaseValidatorModel):
    Domain: Optional[str] = None
    IdentityProvider: Optional[IdentityProviderUnion] = None
    InstanceId: Optional[str] = None
    InstanceUserArn: Optional[str] = None
    Username: Optional[str] = None


class ListProductSubscriptionsRequestPaginate(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    Filters: Optional[Sequence[Filter]] = None
    Product: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProductSubscriptionsRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Product: Optional[str] = None


class ListUserAssociationsRequestPaginate(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    InstanceId: str
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUserAssociationsRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    InstanceId: str
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SettingsUnion(BaseValidatorModel):
    pass


class RegisterIdentityProviderRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    Product: str
    Settings: Optional[SettingsUnion] = None
    Tags: Optional[Mapping[str, str]] = None


class StartProductSubscriptionRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    Product: str
    Username: str
    Domain: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class StopProductSubscriptionRequest(BaseValidatorModel):
    Domain: Optional[str] = None
    IdentityProvider: Optional[IdentityProviderUnion] = None
    Product: Optional[str] = None
    ProductUserArn: Optional[str] = None
    Username: Optional[str] = None


class UpdateIdentityProviderSettingsRequest(BaseValidatorModel):
    UpdateSettings: UpdateSettings
    IdentityProvider: Optional[IdentityProviderUnion] = None
    IdentityProviderArn: Optional[str] = None
    Product: Optional[str] = None



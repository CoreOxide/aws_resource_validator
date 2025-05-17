from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DomainNetworkSettingsOutput(BaseValidatorModel):
    Subnets: List[str]


class DomainNetworkSettings(BaseValidatorModel):
    Subnets: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SecretsManagerCredentialsProvider(BaseValidatorModel):
    SecretId: Optional[str] = None


# This class is the input for the 'delete_license_server_endpoint' function.
class DeleteLicenseServerEndpointRequest(BaseValidatorModel):
    LicenseServerEndpointArn: str
    ServerType: Literal['RDS_SAL']


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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class Settings(BaseValidatorModel):
    SecurityGroupId: str
    Subnets: List[str]


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateSettings(BaseValidatorModel):
    AddSubnets: List[str]
    RemoveSubnets: List[str]
    SecurityGroupId: Optional[str] = None


# This class is the output for the 'create_license_server_endpoint' function.
class CreateLicenseServerEndpointResponse(BaseValidatorModel):
    IdentityProviderArn: str
    LicenseServerEndpointArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CredentialsProvider(BaseValidatorModel):
    SecretsManagerCredentialsProvider: Optional[SecretsManagerCredentialsProvider] = None


# This class is the input for the 'list_identity_providers' function.
class ListIdentityProvidersRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_instances' function.
class ListInstancesRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_license_server_endpoints' function.
class ListLicenseServerEndpointsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_instances' function.
class ListInstancesResponse(BaseValidatorModel):
    InstanceSummaries: List[InstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LicenseServerEndpoint(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    IdentityProviderArn: Optional[str] = None
    LicenseServerEndpointArn: Optional[str] = None
    LicenseServerEndpointId: Optional[str] = None
    LicenseServerEndpointProvisioningStatus: Optional[LicenseServerEndpointProvisioningStatusType] = None
    LicenseServers: Optional[List[LicenseServer]] = None
    ServerEndpoint: Optional[ServerEndpoint] = None
    ServerType: Optional[Literal['RDS_SAL']] = None
    StatusMessage: Optional[str] = None


class ListIdentityProvidersRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstancesRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLicenseServerEndpointsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None

SettingsUnion = Union[Settings, SettingsOutput]


class ActiveDirectorySettingsOutput(BaseValidatorModel):
    DomainCredentialsProvider: Optional[CredentialsProvider] = None
    DomainIpv4List: Optional[List[str]] = None
    DomainName: Optional[str] = None
    DomainNetworkSettings: Optional[DomainNetworkSettingsOutput] = None


class ActiveDirectorySettings(BaseValidatorModel):
    DomainCredentialsProvider: Optional[CredentialsProvider] = None
    DomainIpv4List: Optional[List[str]] = None
    DomainName: Optional[str] = None
    DomainNetworkSettings: Optional[DomainNetworkSettings] = None


class RdsSalSettings(BaseValidatorModel):
    RdsSalCredentialsProvider: CredentialsProvider


# This class is the output for the 'delete_license_server_endpoint' function.
class DeleteLicenseServerEndpointResponse(BaseValidatorModel):
    LicenseServerEndpoint: LicenseServerEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_license_server_endpoints' function.
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
    ServerType: Literal['RDS_SAL']


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

IdentityProviderUnion = Union[IdentityProvider, IdentityProviderOutput]


# This class is the input for the 'create_license_server_endpoint' function.
class CreateLicenseServerEndpointRequest(BaseValidatorModel):
    IdentityProviderArn: str
    LicenseServerSettings: LicenseServerSettings
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'deregister_identity_provider' function.
class DeregisterIdentityProviderResponse(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_identity_providers' function.
class ListIdentityProvidersResponse(BaseValidatorModel):
    IdentityProviderSummaries: List[IdentityProviderSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'register_identity_provider' function.
class RegisterIdentityProviderResponse(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_identity_provider_settings' function.
class UpdateIdentityProviderSettingsResponse(BaseValidatorModel):
    IdentityProviderSummary: IdentityProviderSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_user' function.
class AssociateUserResponse(BaseValidatorModel):
    InstanceUserSummary: InstanceUserSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_user' function.
class DisassociateUserResponse(BaseValidatorModel):
    InstanceUserSummary: InstanceUserSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_user_associations' function.
class ListUserAssociationsResponse(BaseValidatorModel):
    InstanceUserSummaries: List[InstanceUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_product_subscriptions' function.
class ListProductSubscriptionsResponse(BaseValidatorModel):
    ProductUserSummaries: List[ProductUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_product_subscription' function.
class StartProductSubscriptionResponse(BaseValidatorModel):
    ProductUserSummary: ProductUserSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_product_subscription' function.
class StopProductSubscriptionResponse(BaseValidatorModel):
    ProductUserSummary: ProductUserSummary
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'associate_user' function.
class AssociateUserRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    InstanceId: str
    Username: str
    Domain: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'deregister_identity_provider' function.
class DeregisterIdentityProviderRequest(BaseValidatorModel):
    IdentityProvider: Optional[IdentityProviderUnion] = None
    IdentityProviderArn: Optional[str] = None
    Product: Optional[str] = None


# This class is the input for the 'disassociate_user' function.
class DisassociateUserRequest(BaseValidatorModel):
    Domain: Optional[str] = None
    IdentityProvider: Optional[IdentityProviderUnion] = None
    InstanceId: Optional[str] = None
    InstanceUserArn: Optional[str] = None
    Username: Optional[str] = None


class ListProductSubscriptionsRequestPaginate(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    Filters: Optional[List[Filter]] = None
    Product: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_product_subscriptions' function.
class ListProductSubscriptionsRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Product: Optional[str] = None


class ListUserAssociationsRequestPaginate(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    InstanceId: str
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_user_associations' function.
class ListUserAssociationsRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    InstanceId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'register_identity_provider' function.
class RegisterIdentityProviderRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    Product: str
    Settings: Optional[SettingsUnion] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'start_product_subscription' function.
class StartProductSubscriptionRequest(BaseValidatorModel):
    IdentityProvider: IdentityProviderUnion
    Product: str
    Username: str
    Domain: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'stop_product_subscription' function.
class StopProductSubscriptionRequest(BaseValidatorModel):
    Domain: Optional[str] = None
    IdentityProvider: Optional[IdentityProviderUnion] = None
    Product: Optional[str] = None
    ProductUserArn: Optional[str] = None
    Username: Optional[str] = None


# This class is the input for the 'update_identity_provider_settings' function.
class UpdateIdentityProviderSettingsRequest(BaseValidatorModel):
    UpdateSettings: UpdateSettings
    IdentityProvider: Optional[IdentityProviderUnion] = None
    IdentityProviderArn: Optional[str] = None
    Product: Optional[str] = None
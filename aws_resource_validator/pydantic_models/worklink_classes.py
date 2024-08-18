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
from aws_resource_validator.pydantic_models.worklink_constants import *

class AssociateDomainRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    DomainName: str
    AcmCertificateArn: str
    DisplayName: Optional[str] = None

class AssociateWebsiteAuthorizationProviderRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    AuthorizationProviderType: Literal["SAML"]
    DomainName: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateWebsiteCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    Certificate: str
    DisplayName: Optional[str] = None

class CreateFleetRequestRequestTypeDef(BaseValidatorModel):
    FleetName: str
    DisplayName: Optional[str] = None
    OptimizeForEndUserLocation: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteFleetRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str

class DescribeAuditStreamConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str

class DescribeCompanyNetworkConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str

class DescribeDevicePolicyConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str

class DescribeDeviceRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    DeviceId: str

class DescribeDomainRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    DomainName: str

class DescribeFleetMetadataRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str

class DescribeIdentityProviderConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str

class DescribeWebsiteCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    WebsiteCaId: str

class DeviceSummaryTypeDef(BaseValidatorModel):
    DeviceId: Optional[str] = None
    DeviceStatus: Optional[DeviceStatusType] = None

class DisassociateDomainRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    DomainName: str

class DisassociateWebsiteAuthorizationProviderRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    AuthorizationProviderId: str

class DisassociateWebsiteCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    WebsiteCaId: str

class DomainSummaryTypeDef(BaseValidatorModel):
    DomainName: str
    CreatedTime: datetime
    DomainStatus: DomainStatusType
    DisplayName: Optional[str] = None

class FleetSummaryTypeDef(BaseValidatorModel):
    FleetArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    FleetName: Optional[str] = None
    DisplayName: Optional[str] = None
    CompanyCode: Optional[str] = None
    FleetStatus: Optional[FleetStatusType] = None
    Tags: Optional[Dict[str, str]] = None

class ListDevicesRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDomainsRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFleetsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListWebsiteAuthorizationProvidersRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class WebsiteAuthorizationProviderSummaryTypeDef(BaseValidatorModel):
    AuthorizationProviderType: Literal["SAML"]
    AuthorizationProviderId: Optional[str] = None
    DomainName: Optional[str] = None
    CreatedTime: Optional[datetime] = None

class ListWebsiteCertificateAuthoritiesRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class WebsiteCaSummaryTypeDef(BaseValidatorModel):
    WebsiteCaId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    DisplayName: Optional[str] = None

class RestoreDomainAccessRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    DomainName: str

class RevokeDomainAccessRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    DomainName: str

class SignOutUserRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    Username: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAuditStreamConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    AuditStreamArn: Optional[str] = None

class UpdateCompanyNetworkConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    VpcId: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]

class UpdateDevicePolicyConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    DeviceCaCertificate: Optional[str] = None

class UpdateDomainMetadataRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    DomainName: str
    DisplayName: Optional[str] = None

class UpdateFleetMetadataRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    DisplayName: Optional[str] = None
    OptimizeForEndUserLocation: Optional[bool] = None

class UpdateIdentityProviderConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FleetArn: str
    IdentityProviderType: Literal["SAML"]
    IdentityProviderSamlMetadata: Optional[str] = None

class AssociateWebsiteAuthorizationProviderResponseTypeDef(BaseValidatorModel):
    AuthorizationProviderId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateWebsiteCertificateAuthorityResponseTypeDef(BaseValidatorModel):
    WebsiteCaId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResponseTypeDef(BaseValidatorModel):
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAuditStreamConfigurationResponseTypeDef(BaseValidatorModel):
    AuditStreamArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCompanyNetworkConfigurationResponseTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDevicePolicyConfigurationResponseTypeDef(BaseValidatorModel):
    DeviceCaCertificate: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeviceResponseTypeDef(BaseValidatorModel):
    Status: DeviceStatusType
    Model: str
    Manufacturer: str
    OperatingSystem: str
    OperatingSystemVersion: str
    PatchLevel: str
    FirstAccessedTime: datetime
    LastAccessedTime: datetime
    Username: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainResponseTypeDef(BaseValidatorModel):
    DomainName: str
    DisplayName: str
    CreatedTime: datetime
    DomainStatus: DomainStatusType
    AcmCertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetMetadataResponseTypeDef(BaseValidatorModel):
    CreatedTime: datetime
    LastUpdatedTime: datetime
    FleetName: str
    DisplayName: str
    OptimizeForEndUserLocation: bool
    CompanyCode: str
    FleetStatus: FleetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdentityProviderConfigurationResponseTypeDef(BaseValidatorModel):
    IdentityProviderType: Literal["SAML"]
    ServiceProviderSamlMetadata: str
    IdentityProviderSamlMetadata: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWebsiteCertificateAuthorityResponseTypeDef(BaseValidatorModel):
    Certificate: str
    CreatedTime: datetime
    DisplayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(BaseValidatorModel):
    Devices: List[DeviceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResponseTypeDef(BaseValidatorModel):
    Domains: List[DomainSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsResponseTypeDef(BaseValidatorModel):
    FleetSummaryList: List[FleetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebsiteAuthorizationProvidersResponseTypeDef(BaseValidatorModel):
    WebsiteAuthorizationProviders: List[WebsiteAuthorizationProviderSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebsiteCertificateAuthoritiesResponseTypeDef(BaseValidatorModel):
    WebsiteCertificateAuthorities: List[WebsiteCaSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


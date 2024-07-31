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
from aws_resource_validator.pydantic_models.worklink_constants import *

class AssociateDomainRequestRequestTypeDef(BaseModel):
    FleetArn: str
    DomainName: str
    AcmCertificateArn: str
    DisplayName: Optional[str] = None

class AssociateWebsiteAuthorizationProviderRequestRequestTypeDef(BaseModel):
    FleetArn: str
    AuthorizationProviderType: Literal["SAML"]
    DomainName: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateWebsiteCertificateAuthorityRequestRequestTypeDef(BaseModel):
    FleetArn: str
    Certificate: str
    DisplayName: Optional[str] = None

class CreateFleetRequestRequestTypeDef(BaseModel):
    FleetName: str
    DisplayName: Optional[str] = None
    OptimizeForEndUserLocation: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteFleetRequestRequestTypeDef(BaseModel):
    FleetArn: str

class DescribeAuditStreamConfigurationRequestRequestTypeDef(BaseModel):
    FleetArn: str

class DescribeCompanyNetworkConfigurationRequestRequestTypeDef(BaseModel):
    FleetArn: str

class DescribeDevicePolicyConfigurationRequestRequestTypeDef(BaseModel):
    FleetArn: str

class DescribeDeviceRequestRequestTypeDef(BaseModel):
    FleetArn: str
    DeviceId: str

class DescribeDomainRequestRequestTypeDef(BaseModel):
    FleetArn: str
    DomainName: str

class DescribeFleetMetadataRequestRequestTypeDef(BaseModel):
    FleetArn: str

class DescribeIdentityProviderConfigurationRequestRequestTypeDef(BaseModel):
    FleetArn: str

class DescribeWebsiteCertificateAuthorityRequestRequestTypeDef(BaseModel):
    FleetArn: str
    WebsiteCaId: str

class DeviceSummaryTypeDef(BaseModel):
    DeviceId: Optional[str] = None
    DeviceStatus: Optional[DeviceStatusType] = None

class DisassociateDomainRequestRequestTypeDef(BaseModel):
    FleetArn: str
    DomainName: str

class DisassociateWebsiteAuthorizationProviderRequestRequestTypeDef(BaseModel):
    FleetArn: str
    AuthorizationProviderId: str

class DisassociateWebsiteCertificateAuthorityRequestRequestTypeDef(BaseModel):
    FleetArn: str
    WebsiteCaId: str

class DomainSummaryTypeDef(BaseModel):
    DomainName: str
    CreatedTime: datetime
    DomainStatus: DomainStatusType
    DisplayName: Optional[str] = None

class FleetSummaryTypeDef(BaseModel):
    FleetArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    FleetName: Optional[str] = None
    DisplayName: Optional[str] = None
    CompanyCode: Optional[str] = None
    FleetStatus: Optional[FleetStatusType] = None
    Tags: Optional[Dict[str, str]] = None

class ListDevicesRequestRequestTypeDef(BaseModel):
    FleetArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDomainsRequestRequestTypeDef(BaseModel):
    FleetArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFleetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListWebsiteAuthorizationProvidersRequestRequestTypeDef(BaseModel):
    FleetArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class WebsiteAuthorizationProviderSummaryTypeDef(BaseModel):
    AuthorizationProviderType: Literal["SAML"]
    AuthorizationProviderId: Optional[str] = None
    DomainName: Optional[str] = None
    CreatedTime: Optional[datetime] = None

class ListWebsiteCertificateAuthoritiesRequestRequestTypeDef(BaseModel):
    FleetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class WebsiteCaSummaryTypeDef(BaseModel):
    WebsiteCaId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    DisplayName: Optional[str] = None

class RestoreDomainAccessRequestRequestTypeDef(BaseModel):
    FleetArn: str
    DomainName: str

class RevokeDomainAccessRequestRequestTypeDef(BaseModel):
    FleetArn: str
    DomainName: str

class SignOutUserRequestRequestTypeDef(BaseModel):
    FleetArn: str
    Username: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAuditStreamConfigurationRequestRequestTypeDef(BaseModel):
    FleetArn: str
    AuditStreamArn: Optional[str] = None

class UpdateCompanyNetworkConfigurationRequestRequestTypeDef(BaseModel):
    FleetArn: str
    VpcId: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]

class UpdateDevicePolicyConfigurationRequestRequestTypeDef(BaseModel):
    FleetArn: str
    DeviceCaCertificate: Optional[str] = None

class UpdateDomainMetadataRequestRequestTypeDef(BaseModel):
    FleetArn: str
    DomainName: str
    DisplayName: Optional[str] = None

class UpdateFleetMetadataRequestRequestTypeDef(BaseModel):
    FleetArn: str
    DisplayName: Optional[str] = None
    OptimizeForEndUserLocation: Optional[bool] = None

class UpdateIdentityProviderConfigurationRequestRequestTypeDef(BaseModel):
    FleetArn: str
    IdentityProviderType: Literal["SAML"]
    IdentityProviderSamlMetadata: Optional[str] = None

class AssociateWebsiteAuthorizationProviderResponseTypeDef(BaseModel):
    AuthorizationProviderId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateWebsiteCertificateAuthorityResponseTypeDef(BaseModel):
    WebsiteCaId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResponseTypeDef(BaseModel):
    FleetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAuditStreamConfigurationResponseTypeDef(BaseModel):
    AuditStreamArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCompanyNetworkConfigurationResponseTypeDef(BaseModel):
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDevicePolicyConfigurationResponseTypeDef(BaseModel):
    DeviceCaCertificate: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeviceResponseTypeDef(BaseModel):
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

class DescribeDomainResponseTypeDef(BaseModel):
    DomainName: str
    DisplayName: str
    CreatedTime: datetime
    DomainStatus: DomainStatusType
    AcmCertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetMetadataResponseTypeDef(BaseModel):
    CreatedTime: datetime
    LastUpdatedTime: datetime
    FleetName: str
    DisplayName: str
    OptimizeForEndUserLocation: bool
    CompanyCode: str
    FleetStatus: FleetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdentityProviderConfigurationResponseTypeDef(BaseModel):
    IdentityProviderType: Literal["SAML"]
    ServiceProviderSamlMetadata: str
    IdentityProviderSamlMetadata: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWebsiteCertificateAuthorityResponseTypeDef(BaseModel):
    Certificate: str
    CreatedTime: datetime
    DisplayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(BaseModel):
    Devices: List[DeviceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResponseTypeDef(BaseModel):
    Domains: List[DomainSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsResponseTypeDef(BaseModel):
    FleetSummaryList: List[FleetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebsiteAuthorizationProvidersResponseTypeDef(BaseModel):
    WebsiteAuthorizationProviders: List[WebsiteAuthorizationProviderSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebsiteCertificateAuthoritiesResponseTypeDef(BaseModel):
    WebsiteCertificateAuthorities: List[WebsiteCaSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


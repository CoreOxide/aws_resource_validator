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
from aws_resource_validator.pydantic_models.workspaces_web_constants import *

class AssociateBrowserSettingsRequestRequestTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    portalArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociateIpAccessSettingsRequestRequestTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    portalArn: str

class AssociateNetworkSettingsRequestRequestTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    portalArn: str

class AssociateTrustStoreRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str
    trustStoreArn: str

class AssociateUserAccessLoggingSettingsRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str
    userAccessLoggingSettingsArn: str

class AssociateUserSettingsRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str
    userSettingsArn: str

class BrowserSettingsSummaryTypeDef(BaseValidatorModel):
    browserSettingsArn: str

class BrowserSettingsTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    browserPolicy: Optional[str] = None
    customerManagedKey: Optional[str] = None

class CertificateSummaryTypeDef(BaseValidatorModel):
    issuer: Optional[str] = None
    notValidAfter: Optional[datetime] = None
    notValidBefore: Optional[datetime] = None
    subject: Optional[str] = None
    thumbprint: Optional[str] = None

class CertificateTypeDef(BaseValidatorModel):
    body: Optional[bytes] = None
    issuer: Optional[str] = None
    notValidAfter: Optional[datetime] = None
    notValidBefore: Optional[datetime] = None
    subject: Optional[str] = None
    thumbprint: Optional[str] = None

class CookieSpecificationTypeDef(BaseValidatorModel):
    domain: str
    name: Optional[str] = None
    path: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class IpRuleTypeDef(BaseValidatorModel):
    ipRange: str
    description: Optional[str] = None

class DeleteBrowserSettingsRequestRequestTypeDef(BaseValidatorModel):
    browserSettingsArn: str

class DeleteIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    identityProviderArn: str

class DeleteIpAccessSettingsRequestRequestTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str

class DeleteNetworkSettingsRequestRequestTypeDef(BaseValidatorModel):
    networkSettingsArn: str

class DeletePortalRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str

class DeleteTrustStoreRequestRequestTypeDef(BaseValidatorModel):
    trustStoreArn: str

class DeleteUserAccessLoggingSettingsRequestRequestTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str

class DeleteUserSettingsRequestRequestTypeDef(BaseValidatorModel):
    userSettingsArn: str

class DisassociateBrowserSettingsRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str

class DisassociateIpAccessSettingsRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str

class DisassociateNetworkSettingsRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str

class DisassociateTrustStoreRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str

class DisassociateUserAccessLoggingSettingsRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str

class DisassociateUserSettingsRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str

class GetBrowserSettingsRequestRequestTypeDef(BaseValidatorModel):
    browserSettingsArn: str

class GetIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    identityProviderArn: str

class IdentityProviderTypeDef(BaseValidatorModel):
    identityProviderArn: str
    identityProviderDetails: Optional[Dict[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None

class GetIpAccessSettingsRequestRequestTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str

class GetNetworkSettingsRequestRequestTypeDef(BaseValidatorModel):
    networkSettingsArn: str

class NetworkSettingsTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None

class GetPortalRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str

class PortalTypeDef(BaseValidatorModel):
    portalArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    browserSettingsArn: Optional[str] = None
    browserType: Optional[Literal["Chrome"]] = None
    creationDate: Optional[datetime] = None
    customerManagedKey: Optional[str] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    ipAccessSettingsArn: Optional[str] = None
    maxConcurrentSessions: Optional[int] = None
    networkSettingsArn: Optional[str] = None
    portalEndpoint: Optional[str] = None
    portalStatus: Optional[PortalStatusType] = None
    rendererType: Optional[Literal["AppStream"]] = None
    statusReason: Optional[str] = None
    trustStoreArn: Optional[str] = None
    userAccessLoggingSettingsArn: Optional[str] = None
    userSettingsArn: Optional[str] = None

class GetPortalServiceProviderMetadataRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str

class GetTrustStoreCertificateRequestRequestTypeDef(BaseValidatorModel):
    thumbprint: str
    trustStoreArn: str

class GetTrustStoreRequestRequestTypeDef(BaseValidatorModel):
    trustStoreArn: str

class TrustStoreTypeDef(BaseValidatorModel):
    trustStoreArn: str
    associatedPortalArns: Optional[List[str]] = None

class GetUserAccessLoggingSettingsRequestRequestTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str

class UserAccessLoggingSettingsTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    kinesisStreamArn: Optional[str] = None

class GetUserSettingsRequestRequestTypeDef(BaseValidatorModel):
    userSettingsArn: str

class IdentityProviderSummaryTypeDef(BaseValidatorModel):
    identityProviderArn: str
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None

class IpAccessSettingsSummaryTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    creationDate: Optional[datetime] = None
    description: Optional[str] = None
    displayName: Optional[str] = None

class ListBrowserSettingsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIdentityProvidersRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIpAccessSettingsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListNetworkSettingsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class NetworkSettingsSummaryTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    vpcId: Optional[str] = None

class ListPortalsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PortalSummaryTypeDef(BaseValidatorModel):
    portalArn: str
    authenticationType: Optional[AuthenticationTypeType] = None
    browserSettingsArn: Optional[str] = None
    browserType: Optional[Literal["Chrome"]] = None
    creationDate: Optional[datetime] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    ipAccessSettingsArn: Optional[str] = None
    maxConcurrentSessions: Optional[int] = None
    networkSettingsArn: Optional[str] = None
    portalEndpoint: Optional[str] = None
    portalStatus: Optional[PortalStatusType] = None
    rendererType: Optional[Literal["AppStream"]] = None
    trustStoreArn: Optional[str] = None
    userAccessLoggingSettingsArn: Optional[str] = None
    userSettingsArn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTrustStoreCertificatesRequestRequestTypeDef(BaseValidatorModel):
    trustStoreArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTrustStoresRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TrustStoreSummaryTypeDef(BaseValidatorModel):
    trustStoreArn: Optional[str] = None

class ListUserAccessLoggingSettingsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class UserAccessLoggingSettingsSummaryTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    kinesisStreamArn: Optional[str] = None

class ListUserSettingsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateBrowserSettingsRequestRequestTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    browserPolicy: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    identityProviderArn: str
    clientToken: Optional[str] = None
    identityProviderDetails: Optional[Mapping[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None

class UpdateNetworkSettingsRequestRequestTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None
    vpcId: Optional[str] = None

class UpdatePortalRequestRequestTypeDef(BaseValidatorModel):
    portalArn: str
    authenticationType: Optional[AuthenticationTypeType] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None

class UpdateUserAccessLoggingSettingsRequestRequestTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    clientToken: Optional[str] = None
    kinesisStreamArn: Optional[str] = None

class AssociateBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateTrustStoreResponseTypeDef(BaseValidatorModel):
    portalArn: str
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    portalArn: str
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateUserSettingsResponseTypeDef(BaseValidatorModel):
    portalArn: str
    userSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIdentityProviderResponseTypeDef(BaseValidatorModel):
    identityProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePortalResponseTypeDef(BaseValidatorModel):
    portalArn: str
    portalEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustStoreResponseTypeDef(BaseValidatorModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserSettingsResponseTypeDef(BaseValidatorModel):
    userSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPortalServiceProviderMetadataResponseTypeDef(BaseValidatorModel):
    portalArn: str
    serviceProviderSamlMetadata: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustStoreResponseTypeDef(BaseValidatorModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustStoreRequestRequestTypeDef(BaseValidatorModel):
    trustStoreArn: str
    certificatesToAdd: Optional[Sequence[BlobTypeDef]] = None
    certificatesToDelete: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None

class ListBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettings: List[BrowserSettingsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustStoreCertificatesResponseTypeDef(BaseValidatorModel):
    certificateList: List[CertificateSummaryTypeDef]
    nextToken: str
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrustStoreCertificateResponseTypeDef(BaseValidatorModel):
    certificate: CertificateTypeDef
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CookieSynchronizationConfigurationOutputTypeDef(BaseValidatorModel):
    allowlist: List[CookieSpecificationTypeDef]
    blocklist: Optional[List[CookieSpecificationTypeDef]] = None

class CookieSynchronizationConfigurationTypeDef(BaseValidatorModel):
    allowlist: Sequence[CookieSpecificationTypeDef]
    blocklist: Optional[Sequence[CookieSpecificationTypeDef]] = None

class CreateBrowserSettingsRequestRequestTypeDef(BaseValidatorModel):
    browserPolicy: str
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    identityProviderDetails: Mapping[str, str]
    identityProviderName: str
    identityProviderType: IdentityProviderTypeType
    portalArn: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateNetworkSettingsRequestRequestTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreatePortalRequestRequestTypeDef(BaseValidatorModel):
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateTrustStoreRequestRequestTypeDef(BaseValidatorModel):
    certificateList: Sequence[BlobTypeDef]
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserAccessLoggingSettingsRequestRequestTypeDef(BaseValidatorModel):
    kinesisStreamArn: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]
    clientToken: Optional[str] = None

class CreateIpAccessSettingsRequestRequestTypeDef(BaseValidatorModel):
    ipRules: Sequence[IpRuleTypeDef]
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class IpAccessSettingsTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    creationDate: Optional[datetime] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    ipRules: Optional[List[IpRuleTypeDef]] = None

class UpdateIpAccessSettingsRequestRequestTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    ipRules: Optional[Sequence[IpRuleTypeDef]] = None

class GetIdentityProviderResponseTypeDef(BaseValidatorModel):
    identityProvider: IdentityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentityProviderResponseTypeDef(BaseValidatorModel):
    identityProvider: IdentityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettings: NetworkSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettings: NetworkSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPortalResponseTypeDef(BaseValidatorModel):
    portal: PortalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePortalResponseTypeDef(BaseValidatorModel):
    portal: PortalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrustStoreResponseTypeDef(BaseValidatorModel):
    trustStore: TrustStoreTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    userAccessLoggingSettings: UserAccessLoggingSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    userAccessLoggingSettings: UserAccessLoggingSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityProvidersResponseTypeDef(BaseValidatorModel):
    identityProviders: List[IdentityProviderSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettings: List[IpAccessSettingsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettings: List[NetworkSettingsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPortalsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    portals: List[PortalSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustStoresResponseTypeDef(BaseValidatorModel):
    nextToken: str
    trustStores: List[TrustStoreSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    userAccessLoggingSettings: List[UserAccessLoggingSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UserSettingsSummaryTypeDef(BaseValidatorModel):
    userSettingsArn: str
    cookieSynchronizationConfiguration: Optional[       CookieSynchronizationConfigurationOutputTypeDef     ] = None
    copyAllowed: Optional[EnabledTypeType] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    downloadAllowed: Optional[EnabledTypeType] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    pasteAllowed: Optional[EnabledTypeType] = None
    printAllowed: Optional[EnabledTypeType] = None
    uploadAllowed: Optional[EnabledTypeType] = None

class UserSettingsTypeDef(BaseValidatorModel):
    userSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    cookieSynchronizationConfiguration: Optional[       CookieSynchronizationConfigurationOutputTypeDef     ] = None
    copyAllowed: Optional[EnabledTypeType] = None
    customerManagedKey: Optional[str] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    downloadAllowed: Optional[EnabledTypeType] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    pasteAllowed: Optional[EnabledTypeType] = None
    printAllowed: Optional[EnabledTypeType] = None
    uploadAllowed: Optional[EnabledTypeType] = None

class CreateUserSettingsRequestRequestTypeDef(BaseValidatorModel):
    copyAllowed: EnabledTypeType
    downloadAllowed: EnabledTypeType
    pasteAllowed: EnabledTypeType
    printAllowed: EnabledTypeType
    uploadAllowed: EnabledTypeType
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    cookieSynchronizationConfiguration: Optional[       CookieSynchronizationConfigurationTypeDef     ] = None
    customerManagedKey: Optional[str] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateUserSettingsRequestRequestTypeDef(BaseValidatorModel):
    userSettingsArn: str
    clientToken: Optional[str] = None
    cookieSynchronizationConfiguration: Optional[       CookieSynchronizationConfigurationTypeDef     ] = None
    copyAllowed: Optional[EnabledTypeType] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    downloadAllowed: Optional[EnabledTypeType] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    pasteAllowed: Optional[EnabledTypeType] = None
    printAllowed: Optional[EnabledTypeType] = None
    uploadAllowed: Optional[EnabledTypeType] = None

class GetIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettings: IpAccessSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettings: IpAccessSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserSettingsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    userSettings: List[UserSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserSettingsResponseTypeDef(BaseValidatorModel):
    userSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserSettingsResponseTypeDef(BaseValidatorModel):
    userSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.workspaces_web_constants import *

class AssociateBrowserSettingsRequestRequestTypeDef(BaseModel):
    browserSettingsArn: str
    portalArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociateIpAccessSettingsRequestRequestTypeDef(BaseModel):
    ipAccessSettingsArn: str
    portalArn: str

class AssociateNetworkSettingsRequestRequestTypeDef(BaseModel):
    networkSettingsArn: str
    portalArn: str

class AssociateTrustStoreRequestRequestTypeDef(BaseModel):
    portalArn: str
    trustStoreArn: str

class AssociateUserAccessLoggingSettingsRequestRequestTypeDef(BaseModel):
    portalArn: str
    userAccessLoggingSettingsArn: str

class AssociateUserSettingsRequestRequestTypeDef(BaseModel):
    portalArn: str
    userSettingsArn: str

class BrowserSettingsSummaryTypeDef(BaseModel):
    browserSettingsArn: str

class BrowserSettingsTypeDef(BaseModel):
    browserSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    browserPolicy: Optional[str] = None
    customerManagedKey: Optional[str] = None

class CertificateSummaryTypeDef(BaseModel):
    issuer: Optional[str] = None
    notValidAfter: Optional[datetime] = None
    notValidBefore: Optional[datetime] = None
    subject: Optional[str] = None
    thumbprint: Optional[str] = None

class CertificateTypeDef(BaseModel):
    body: Optional[bytes] = None
    issuer: Optional[str] = None
    notValidAfter: Optional[datetime] = None
    notValidBefore: Optional[datetime] = None
    subject: Optional[str] = None
    thumbprint: Optional[str] = None

class CookieSpecificationTypeDef(BaseModel):
    domain: str
    name: Optional[str] = None
    path: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class IpRuleTypeDef(BaseModel):
    ipRange: str
    description: Optional[str] = None

class DeleteBrowserSettingsRequestRequestTypeDef(BaseModel):
    browserSettingsArn: str

class DeleteIdentityProviderRequestRequestTypeDef(BaseModel):
    identityProviderArn: str

class DeleteIpAccessSettingsRequestRequestTypeDef(BaseModel):
    ipAccessSettingsArn: str

class DeleteNetworkSettingsRequestRequestTypeDef(BaseModel):
    networkSettingsArn: str

class DeletePortalRequestRequestTypeDef(BaseModel):
    portalArn: str

class DeleteTrustStoreRequestRequestTypeDef(BaseModel):
    trustStoreArn: str

class DeleteUserAccessLoggingSettingsRequestRequestTypeDef(BaseModel):
    userAccessLoggingSettingsArn: str

class DeleteUserSettingsRequestRequestTypeDef(BaseModel):
    userSettingsArn: str

class DisassociateBrowserSettingsRequestRequestTypeDef(BaseModel):
    portalArn: str

class DisassociateIpAccessSettingsRequestRequestTypeDef(BaseModel):
    portalArn: str

class DisassociateNetworkSettingsRequestRequestTypeDef(BaseModel):
    portalArn: str

class DisassociateTrustStoreRequestRequestTypeDef(BaseModel):
    portalArn: str

class DisassociateUserAccessLoggingSettingsRequestRequestTypeDef(BaseModel):
    portalArn: str

class DisassociateUserSettingsRequestRequestTypeDef(BaseModel):
    portalArn: str

class GetBrowserSettingsRequestRequestTypeDef(BaseModel):
    browserSettingsArn: str

class GetIdentityProviderRequestRequestTypeDef(BaseModel):
    identityProviderArn: str

class IdentityProviderTypeDef(BaseModel):
    identityProviderArn: str
    identityProviderDetails: Optional[Dict[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None

class GetIpAccessSettingsRequestRequestTypeDef(BaseModel):
    ipAccessSettingsArn: str

class GetNetworkSettingsRequestRequestTypeDef(BaseModel):
    networkSettingsArn: str

class NetworkSettingsTypeDef(BaseModel):
    networkSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None

class GetPortalRequestRequestTypeDef(BaseModel):
    portalArn: str

class PortalTypeDef(BaseModel):
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

class GetPortalServiceProviderMetadataRequestRequestTypeDef(BaseModel):
    portalArn: str

class GetTrustStoreCertificateRequestRequestTypeDef(BaseModel):
    thumbprint: str
    trustStoreArn: str

class GetTrustStoreRequestRequestTypeDef(BaseModel):
    trustStoreArn: str

class TrustStoreTypeDef(BaseModel):
    trustStoreArn: str
    associatedPortalArns: Optional[List[str]] = None

class GetUserAccessLoggingSettingsRequestRequestTypeDef(BaseModel):
    userAccessLoggingSettingsArn: str

class UserAccessLoggingSettingsTypeDef(BaseModel):
    userAccessLoggingSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    kinesisStreamArn: Optional[str] = None

class GetUserSettingsRequestRequestTypeDef(BaseModel):
    userSettingsArn: str

class IdentityProviderSummaryTypeDef(BaseModel):
    identityProviderArn: str
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None

class IpAccessSettingsSummaryTypeDef(BaseModel):
    ipAccessSettingsArn: str
    creationDate: Optional[datetime] = None
    description: Optional[str] = None
    displayName: Optional[str] = None

class ListBrowserSettingsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIdentityProvidersRequestRequestTypeDef(BaseModel):
    portalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIpAccessSettingsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListNetworkSettingsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class NetworkSettingsSummaryTypeDef(BaseModel):
    networkSettingsArn: str
    vpcId: Optional[str] = None

class ListPortalsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PortalSummaryTypeDef(BaseModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTrustStoreCertificatesRequestRequestTypeDef(BaseModel):
    trustStoreArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTrustStoresRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TrustStoreSummaryTypeDef(BaseModel):
    trustStoreArn: Optional[str] = None

class ListUserAccessLoggingSettingsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class UserAccessLoggingSettingsSummaryTypeDef(BaseModel):
    userAccessLoggingSettingsArn: str
    kinesisStreamArn: Optional[str] = None

class ListUserSettingsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateBrowserSettingsRequestRequestTypeDef(BaseModel):
    browserSettingsArn: str
    browserPolicy: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateIdentityProviderRequestRequestTypeDef(BaseModel):
    identityProviderArn: str
    clientToken: Optional[str] = None
    identityProviderDetails: Optional[Mapping[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None

class UpdateNetworkSettingsRequestRequestTypeDef(BaseModel):
    networkSettingsArn: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None
    vpcId: Optional[str] = None

class UpdatePortalRequestRequestTypeDef(BaseModel):
    portalArn: str
    authenticationType: Optional[AuthenticationTypeType] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None

class UpdateUserAccessLoggingSettingsRequestRequestTypeDef(BaseModel):
    userAccessLoggingSettingsArn: str
    clientToken: Optional[str] = None
    kinesisStreamArn: Optional[str] = None

class AssociateBrowserSettingsResponseTypeDef(BaseModel):
    browserSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateIpAccessSettingsResponseTypeDef(BaseModel):
    ipAccessSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateNetworkSettingsResponseTypeDef(BaseModel):
    networkSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateTrustStoreResponseTypeDef(BaseModel):
    portalArn: str
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateUserAccessLoggingSettingsResponseTypeDef(BaseModel):
    portalArn: str
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateUserSettingsResponseTypeDef(BaseModel):
    portalArn: str
    userSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBrowserSettingsResponseTypeDef(BaseModel):
    browserSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIdentityProviderResponseTypeDef(BaseModel):
    identityProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpAccessSettingsResponseTypeDef(BaseModel):
    ipAccessSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkSettingsResponseTypeDef(BaseModel):
    networkSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePortalResponseTypeDef(BaseModel):
    portalArn: str
    portalEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustStoreResponseTypeDef(BaseModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserAccessLoggingSettingsResponseTypeDef(BaseModel):
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserSettingsResponseTypeDef(BaseModel):
    userSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPortalServiceProviderMetadataResponseTypeDef(BaseModel):
    portalArn: str
    serviceProviderSamlMetadata: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustStoreResponseTypeDef(BaseModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustStoreRequestRequestTypeDef(BaseModel):
    trustStoreArn: str
    certificatesToAdd: Optional[Sequence[BlobTypeDef]] = None
    certificatesToDelete: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None

class ListBrowserSettingsResponseTypeDef(BaseModel):
    browserSettings: List[BrowserSettingsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBrowserSettingsResponseTypeDef(BaseModel):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrowserSettingsResponseTypeDef(BaseModel):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustStoreCertificatesResponseTypeDef(BaseModel):
    certificateList: List[CertificateSummaryTypeDef]
    nextToken: str
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrustStoreCertificateResponseTypeDef(BaseModel):
    certificate: CertificateTypeDef
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CookieSynchronizationConfigurationOutputTypeDef(BaseModel):
    allowlist: List[CookieSpecificationTypeDef]
    blocklist: Optional[List[CookieSpecificationTypeDef]] = None

class CookieSynchronizationConfigurationTypeDef(BaseModel):
    allowlist: Sequence[CookieSpecificationTypeDef]
    blocklist: Optional[Sequence[CookieSpecificationTypeDef]] = None

class CreateBrowserSettingsRequestRequestTypeDef(BaseModel):
    browserPolicy: str
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateIdentityProviderRequestRequestTypeDef(BaseModel):
    identityProviderDetails: Mapping[str, str]
    identityProviderName: str
    identityProviderType: IdentityProviderTypeType
    portalArn: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateNetworkSettingsRequestRequestTypeDef(BaseModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreatePortalRequestRequestTypeDef(BaseModel):
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateTrustStoreRequestRequestTypeDef(BaseModel):
    certificateList: Sequence[BlobTypeDef]
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserAccessLoggingSettingsRequestRequestTypeDef(BaseModel):
    kinesisStreamArn: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]
    clientToken: Optional[str] = None

class CreateIpAccessSettingsRequestRequestTypeDef(BaseModel):
    ipRules: Sequence[IpRuleTypeDef]
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class IpAccessSettingsTypeDef(BaseModel):
    ipAccessSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    creationDate: Optional[datetime] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    ipRules: Optional[List[IpRuleTypeDef]] = None

class UpdateIpAccessSettingsRequestRequestTypeDef(BaseModel):
    ipAccessSettingsArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    ipRules: Optional[Sequence[IpRuleTypeDef]] = None

class GetIdentityProviderResponseTypeDef(BaseModel):
    identityProvider: IdentityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentityProviderResponseTypeDef(BaseModel):
    identityProvider: IdentityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkSettingsResponseTypeDef(BaseModel):
    networkSettings: NetworkSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkSettingsResponseTypeDef(BaseModel):
    networkSettings: NetworkSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPortalResponseTypeDef(BaseModel):
    portal: PortalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePortalResponseTypeDef(BaseModel):
    portal: PortalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrustStoreResponseTypeDef(BaseModel):
    trustStore: TrustStoreTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserAccessLoggingSettingsResponseTypeDef(BaseModel):
    userAccessLoggingSettings: UserAccessLoggingSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserAccessLoggingSettingsResponseTypeDef(BaseModel):
    userAccessLoggingSettings: UserAccessLoggingSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityProvidersResponseTypeDef(BaseModel):
    identityProviders: List[IdentityProviderSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIpAccessSettingsResponseTypeDef(BaseModel):
    ipAccessSettings: List[IpAccessSettingsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkSettingsResponseTypeDef(BaseModel):
    networkSettings: List[NetworkSettingsSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPortalsResponseTypeDef(BaseModel):
    nextToken: str
    portals: List[PortalSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustStoresResponseTypeDef(BaseModel):
    nextToken: str
    trustStores: List[TrustStoreSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserAccessLoggingSettingsResponseTypeDef(BaseModel):
    nextToken: str
    userAccessLoggingSettings: List[UserAccessLoggingSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UserSettingsSummaryTypeDef(BaseModel):
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

class UserSettingsTypeDef(BaseModel):
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

class CreateUserSettingsRequestRequestTypeDef(BaseModel):
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

class UpdateUserSettingsRequestRequestTypeDef(BaseModel):
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

class GetIpAccessSettingsResponseTypeDef(BaseModel):
    ipAccessSettings: IpAccessSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIpAccessSettingsResponseTypeDef(BaseModel):
    ipAccessSettings: IpAccessSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserSettingsResponseTypeDef(BaseModel):
    nextToken: str
    userSettings: List[UserSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserSettingsResponseTypeDef(BaseModel):
    userSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserSettingsResponseTypeDef(BaseModel):
    userSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


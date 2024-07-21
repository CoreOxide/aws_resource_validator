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
from aws_resource_validator.pydantic_models.grafana_constants import *

class AssertionAttributesTypeDef(BaseModel):
    email: Optional[str] = None
    groups: Optional[str] = None
    login: Optional[str] = None
    name: Optional[str] = None
    org: Optional[str] = None
    role: Optional[str] = None

class AssociateLicenseRequestRequestTypeDef(BaseModel):
    licenseType: LicenseTypeType
    workspaceId: str
    grafanaToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AwsSsoAuthenticationTypeDef(BaseModel):
    ssoClientId: Optional[str] = None

class AuthenticationSummaryTypeDef(BaseModel):
    providers: List[AuthenticationProviderTypesType]
    samlConfigurationStatus: Optional[SamlConfigurationStatusType] = None

class CreateWorkspaceApiKeyRequestRequestTypeDef(BaseModel):
    keyName: str
    keyRole: str
    secondsToLive: int
    workspaceId: str

class NetworkAccessConfigurationTypeDef(BaseModel):
    prefixListIds: Sequence[str]
    vpceIds: Sequence[str]

class VpcConfigurationTypeDef(BaseModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]

class CreateWorkspaceServiceAccountRequestRequestTypeDef(BaseModel):
    grafanaRole: RoleType
    name: str
    workspaceId: str

class CreateWorkspaceServiceAccountTokenRequestRequestTypeDef(BaseModel):
    name: str
    secondsToLive: int
    serviceAccountId: str
    workspaceId: str

class ServiceAccountTokenSummaryWithKeyTypeDef(BaseModel):
    id: str
    key: str
    name: str

class DeleteWorkspaceApiKeyRequestRequestTypeDef(BaseModel):
    keyName: str
    workspaceId: str

class DeleteWorkspaceRequestRequestTypeDef(BaseModel):
    workspaceId: str

class DeleteWorkspaceServiceAccountRequestRequestTypeDef(BaseModel):
    serviceAccountId: str
    workspaceId: str

class DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef(BaseModel):
    serviceAccountId: str
    tokenId: str
    workspaceId: str

class DescribeWorkspaceAuthenticationRequestRequestTypeDef(BaseModel):
    workspaceId: str

class DescribeWorkspaceConfigurationRequestRequestTypeDef(BaseModel):
    workspaceId: str

class DescribeWorkspaceRequestRequestTypeDef(BaseModel):
    workspaceId: str

class DisassociateLicenseRequestRequestTypeDef(BaseModel):
    licenseType: LicenseTypeType
    workspaceId: str

class IdpMetadataTypeDef(BaseModel):
    url: Optional[str] = None
    xml: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListPermissionsRequestRequestTypeDef(BaseModel):
    workspaceId: str
    groupId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    userId: Optional[str] = None
    userType: Optional[UserTypeType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListVersionsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    workspaceId: Optional[str] = None

class ListWorkspaceServiceAccountTokensRequestRequestTypeDef(BaseModel):
    serviceAccountId: str
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceAccountTokenSummaryTypeDef(BaseModel):
    createdAt: datetime
    expiresAt: datetime
    id: str
    name: str
    lastUsedAt: Optional[datetime] = None

class ListWorkspaceServiceAccountsRequestRequestTypeDef(BaseModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceAccountSummaryTypeDef(BaseModel):
    grafanaRole: RoleType
    id: str
    isDisabled: str
    name: str

class ListWorkspacesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class NetworkAccessConfigurationOutputTypeDef(BaseModel):
    prefixListIds: List[str]
    vpceIds: List[str]

class UserTypeDef(BaseModel):
    id: str
    type: UserTypeType

class RoleValuesOutputTypeDef(BaseModel):
    admin: Optional[List[str]] = None
    editor: Optional[List[str]] = None

class RoleValuesTypeDef(BaseModel):
    admin: Optional[Sequence[str]] = None
    editor: Optional[Sequence[str]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateWorkspaceConfigurationRequestRequestTypeDef(BaseModel):
    configuration: str
    workspaceId: str
    grafanaVersion: Optional[str] = None

class VpcConfigurationOutputTypeDef(BaseModel):
    securityGroupIds: List[str]
    subnetIds: List[str]

class CreateWorkspaceApiKeyResponseTypeDef(BaseModel):
    key: str
    keyName: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceServiceAccountResponseTypeDef(BaseModel):
    grafanaRole: RoleType
    id: str
    name: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceApiKeyResponseTypeDef(BaseModel):
    keyName: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceServiceAccountResponseTypeDef(BaseModel):
    serviceAccountId: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceServiceAccountTokenResponseTypeDef(BaseModel):
    serviceAccountId: str
    tokenId: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceConfigurationResponseTypeDef(BaseModel):
    configuration: str
    grafanaVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVersionsResponseTypeDef(BaseModel):
    grafanaVersions: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkspaceSummaryTypeDef(BaseModel):
    authentication: AuthenticationSummaryTypeDef
    created: datetime
    endpoint: str
    grafanaVersion: str
    id: str
    modified: datetime
    status: WorkspaceStatusType
    description: Optional[str] = None
    grafanaToken: Optional[str] = None
    licenseType: Optional[LicenseTypeType] = None
    name: Optional[str] = None
    notificationDestinations: Optional[List[Literal["SNS"]]] = None
    tags: Optional[Dict[str, str]] = None

class CreateWorkspaceRequestRequestTypeDef(BaseModel):
    accountAccessType: AccountAccessTypeType
    authenticationProviders: Sequence[AuthenticationProviderTypesType]
    permissionType: PermissionTypeType
    clientToken: Optional[str] = None
    configuration: Optional[str] = None
    grafanaVersion: Optional[str] = None
    networkAccessControl: Optional[NetworkAccessConfigurationTypeDef] = None
    organizationRoleName: Optional[str] = None
    stackSetName: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    vpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    workspaceDataSources: Optional[Sequence[DataSourceTypeType]] = None
    workspaceDescription: Optional[str] = None
    workspaceName: Optional[str] = None
    workspaceNotificationDestinations: Optional[Sequence[Literal["SNS"]]] = None
    workspaceOrganizationalUnits: Optional[Sequence[str]] = None
    workspaceRoleArn: Optional[str] = None

class UpdateWorkspaceRequestRequestTypeDef(BaseModel):
    workspaceId: str
    accountAccessType: Optional[AccountAccessTypeType] = None
    networkAccessControl: Optional[NetworkAccessConfigurationTypeDef] = None
    organizationRoleName: Optional[str] = None
    permissionType: Optional[PermissionTypeType] = None
    removeNetworkAccessConfiguration: Optional[bool] = None
    removeVpcConfiguration: Optional[bool] = None
    stackSetName: Optional[str] = None
    vpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    workspaceDataSources: Optional[Sequence[DataSourceTypeType]] = None
    workspaceDescription: Optional[str] = None
    workspaceName: Optional[str] = None
    workspaceNotificationDestinations: Optional[Sequence[Literal["SNS"]]] = None
    workspaceOrganizationalUnits: Optional[Sequence[str]] = None
    workspaceRoleArn: Optional[str] = None

class CreateWorkspaceServiceAccountTokenResponseTypeDef(BaseModel):
    serviceAccountId: str
    serviceAccountToken: ServiceAccountTokenSummaryWithKeyTypeDef
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionsRequestListPermissionsPaginateTypeDef(BaseModel):
    workspaceId: str
    groupId: Optional[str] = None
    userId: Optional[str] = None
    userType: Optional[UserTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVersionsRequestListVersionsPaginateTypeDef(BaseModel):
    workspaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkspaceServiceAccountsRequestListWorkspaceServiceAccountsPaginateTypeDef(BaseModel):
    workspaceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkspacesRequestListWorkspacesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkspaceServiceAccountTokensResponseTypeDef(BaseModel):
    nextToken: str
    serviceAccountId: str
    serviceAccountTokens: List[ServiceAccountTokenSummaryTypeDef]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkspaceServiceAccountsResponseTypeDef(BaseModel):
    nextToken: str
    serviceAccounts: List[ServiceAccountSummaryTypeDef]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PermissionEntryTypeDef(BaseModel):
    role: RoleType
    user: UserTypeDef

class UpdateInstructionOutputTypeDef(BaseModel):
    action: UpdateActionType
    role: RoleType
    users: List[UserTypeDef]

class UpdateInstructionTypeDef(BaseModel):
    action: UpdateActionType
    role: RoleType
    users: Sequence[UserTypeDef]

class SamlConfigurationOutputTypeDef(BaseModel):
    idpMetadata: IdpMetadataTypeDef
    allowedOrganizations: Optional[List[str]] = None
    assertionAttributes: Optional[AssertionAttributesTypeDef] = None
    loginValidityDuration: Optional[int] = None
    roleValues: Optional[RoleValuesOutputTypeDef] = None

class SamlConfigurationTypeDef(BaseModel):
    idpMetadata: IdpMetadataTypeDef
    allowedOrganizations: Optional[Sequence[str]] = None
    assertionAttributes: Optional[AssertionAttributesTypeDef] = None
    loginValidityDuration: Optional[int] = None
    roleValues: Optional[RoleValuesTypeDef] = None

class WorkspaceDescriptionTypeDef(BaseModel):
    authentication: AuthenticationSummaryTypeDef
    created: datetime
    dataSources: List[DataSourceTypeType]
    endpoint: str
    grafanaVersion: str
    id: str
    modified: datetime
    status: WorkspaceStatusType
    accountAccessType: Optional[AccountAccessTypeType] = None
    description: Optional[str] = None
    freeTrialConsumed: Optional[bool] = None
    freeTrialExpiration: Optional[datetime] = None
    grafanaToken: Optional[str] = None
    licenseExpiration: Optional[datetime] = None
    licenseType: Optional[LicenseTypeType] = None
    name: Optional[str] = None
    networkAccessControl: Optional[NetworkAccessConfigurationOutputTypeDef] = None
    notificationDestinations: Optional[List[Literal["SNS"]]] = None
    organizationRoleName: Optional[str] = None
    organizationalUnits: Optional[List[str]] = None
    permissionType: Optional[PermissionTypeType] = None
    stackSetName: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    vpcConfiguration: Optional[VpcConfigurationOutputTypeDef] = None
    workspaceRoleArn: Optional[str] = None

class ListWorkspacesResponseTypeDef(BaseModel):
    nextToken: str
    workspaces: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionsResponseTypeDef(BaseModel):
    nextToken: str
    permissions: List[PermissionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateErrorTypeDef(BaseModel):
    causedBy: UpdateInstructionOutputTypeDef
    code: int
    message: str

class SamlAuthenticationTypeDef(BaseModel):
    status: SamlConfigurationStatusType
    configuration: Optional[SamlConfigurationOutputTypeDef] = None

class UpdateWorkspaceAuthenticationRequestRequestTypeDef(BaseModel):
    authenticationProviders: Sequence[AuthenticationProviderTypesType]
    workspaceId: str
    samlConfiguration: Optional[SamlConfigurationTypeDef] = None

class AssociateLicenseResponseTypeDef(BaseModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(BaseModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceResponseTypeDef(BaseModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceResponseTypeDef(BaseModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateLicenseResponseTypeDef(BaseModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceResponseTypeDef(BaseModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePermissionsResponseTypeDef(BaseModel):
    errors: List[UpdateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePermissionsRequestRequestTypeDef(BaseModel):
    updateInstructionBatch: Sequence[UpdateInstructionUnionTypeDef]
    workspaceId: str

class AuthenticationDescriptionTypeDef(BaseModel):
    providers: List[AuthenticationProviderTypesType]
    awsSso: Optional[AwsSsoAuthenticationTypeDef] = None
    saml: Optional[SamlAuthenticationTypeDef] = None

class DescribeWorkspaceAuthenticationResponseTypeDef(BaseModel):
    authentication: AuthenticationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceAuthenticationResponseTypeDef(BaseModel):
    authentication: AuthenticationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.grafana_constants import *

class AssertionAttributesTypeDef(BaseValidatorModel):
    email: Optional[str] = None
    groups: Optional[str] = None
    login: Optional[str] = None
    name: Optional[str] = None
    org: Optional[str] = None
    role: Optional[str] = None

class AssociateLicenseRequestRequestTypeDef(BaseValidatorModel):
    licenseType: LicenseTypeType
    workspaceId: str
    grafanaToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AwsSsoAuthenticationTypeDef(BaseValidatorModel):
    ssoClientId: Optional[str] = None

class AuthenticationSummaryTypeDef(BaseValidatorModel):
    providers: List[AuthenticationProviderTypesType]
    samlConfigurationStatus: Optional[SamlConfigurationStatusType] = None

class CreateWorkspaceApiKeyRequestRequestTypeDef(BaseValidatorModel):
    keyName: str
    keyRole: str
    secondsToLive: int
    workspaceId: str

class NetworkAccessConfigurationTypeDef(BaseValidatorModel):
    prefixListIds: Sequence[str]
    vpceIds: Sequence[str]

class VpcConfigurationTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]

class CreateWorkspaceServiceAccountRequestRequestTypeDef(BaseValidatorModel):
    grafanaRole: RoleType
    name: str
    workspaceId: str

class CreateWorkspaceServiceAccountTokenRequestRequestTypeDef(BaseValidatorModel):
    name: str
    secondsToLive: int
    serviceAccountId: str
    workspaceId: str

class ServiceAccountTokenSummaryWithKeyTypeDef(BaseValidatorModel):
    id: str
    key: str
    name: str

class DeleteWorkspaceApiKeyRequestRequestTypeDef(BaseValidatorModel):
    keyName: str
    workspaceId: str

class DeleteWorkspaceRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str

class DeleteWorkspaceServiceAccountRequestRequestTypeDef(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str

class DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef(BaseValidatorModel):
    serviceAccountId: str
    tokenId: str
    workspaceId: str

class DescribeWorkspaceAuthenticationRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str

class DescribeWorkspaceConfigurationRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str

class DescribeWorkspaceRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str

class DisassociateLicenseRequestRequestTypeDef(BaseValidatorModel):
    licenseType: LicenseTypeType
    workspaceId: str

class IdpMetadataTypeDef(BaseValidatorModel):
    url: Optional[str] = None
    xml: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListPermissionsRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    groupId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    userId: Optional[str] = None
    userType: Optional[UserTypeType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListVersionsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    workspaceId: Optional[str] = None

class ListWorkspaceServiceAccountTokensRequestRequestTypeDef(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceAccountTokenSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    expiresAt: datetime
    id: str
    name: str
    lastUsedAt: Optional[datetime] = None

class ListWorkspaceServiceAccountsRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceAccountSummaryTypeDef(BaseValidatorModel):
    grafanaRole: RoleType
    id: str
    isDisabled: str
    name: str

class ListWorkspacesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class NetworkAccessConfigurationOutputTypeDef(BaseValidatorModel):
    prefixListIds: List[str]
    vpceIds: List[str]

class UserTypeDef(BaseValidatorModel):
    id: str
    type: UserTypeType

class RoleValuesOutputTypeDef(BaseValidatorModel):
    admin: Optional[List[str]] = None
    editor: Optional[List[str]] = None

class RoleValuesTypeDef(BaseValidatorModel):
    admin: Optional[Sequence[str]] = None
    editor: Optional[Sequence[str]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateWorkspaceConfigurationRequestRequestTypeDef(BaseValidatorModel):
    configuration: str
    workspaceId: str
    grafanaVersion: Optional[str] = None

class VpcConfigurationOutputTypeDef(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]

class CreateWorkspaceApiKeyResponseTypeDef(BaseValidatorModel):
    key: str
    keyName: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceServiceAccountResponseTypeDef(BaseValidatorModel):
    grafanaRole: RoleType
    id: str
    name: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceApiKeyResponseTypeDef(BaseValidatorModel):
    keyName: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceServiceAccountResponseTypeDef(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceServiceAccountTokenResponseTypeDef(BaseValidatorModel):
    serviceAccountId: str
    tokenId: str
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceConfigurationResponseTypeDef(BaseValidatorModel):
    configuration: str
    grafanaVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVersionsResponseTypeDef(BaseValidatorModel):
    grafanaVersions: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkspaceSummaryTypeDef(BaseValidatorModel):
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

class CreateWorkspaceRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateWorkspaceRequestRequestTypeDef(BaseValidatorModel):
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

class CreateWorkspaceServiceAccountTokenResponseTypeDef(BaseValidatorModel):
    serviceAccountId: str
    serviceAccountToken: ServiceAccountTokenSummaryWithKeyTypeDef
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionsRequestListPermissionsPaginateTypeDef(BaseValidatorModel):
    workspaceId: str
    groupId: Optional[str] = None
    userId: Optional[str] = None
    userType: Optional[UserTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVersionsRequestListVersionsPaginateTypeDef(BaseValidatorModel):
    workspaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkspaceServiceAccountsRequestListWorkspaceServiceAccountsPaginateTypeDef(BaseValidatorModel):
    workspaceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkspacesRequestListWorkspacesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkspaceServiceAccountTokensResponseTypeDef(BaseValidatorModel):
    nextToken: str
    serviceAccountId: str
    serviceAccountTokens: List[ServiceAccountTokenSummaryTypeDef]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkspaceServiceAccountsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    serviceAccounts: List[ServiceAccountSummaryTypeDef]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PermissionEntryTypeDef(BaseValidatorModel):
    role: RoleType
    user: UserTypeDef

class UpdateInstructionOutputTypeDef(BaseValidatorModel):
    action: UpdateActionType
    role: RoleType
    users: List[UserTypeDef]

class UpdateInstructionTypeDef(BaseValidatorModel):
    action: UpdateActionType
    role: RoleType
    users: Sequence[UserTypeDef]

class SamlConfigurationOutputTypeDef(BaseValidatorModel):
    idpMetadata: IdpMetadataTypeDef
    allowedOrganizations: Optional[List[str]] = None
    assertionAttributes: Optional[AssertionAttributesTypeDef] = None
    loginValidityDuration: Optional[int] = None
    roleValues: Optional[RoleValuesOutputTypeDef] = None

class SamlConfigurationTypeDef(BaseValidatorModel):
    idpMetadata: IdpMetadataTypeDef
    allowedOrganizations: Optional[Sequence[str]] = None
    assertionAttributes: Optional[AssertionAttributesTypeDef] = None
    loginValidityDuration: Optional[int] = None
    roleValues: Optional[RoleValuesTypeDef] = None

class WorkspaceDescriptionTypeDef(BaseValidatorModel):
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

class ListWorkspacesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    workspaces: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    permissions: List[PermissionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateErrorTypeDef(BaseValidatorModel):
    causedBy: UpdateInstructionOutputTypeDef
    code: int
    message: str

class SamlAuthenticationTypeDef(BaseValidatorModel):
    status: SamlConfigurationStatusType
    configuration: Optional[SamlConfigurationOutputTypeDef] = None

class UpdateWorkspaceAuthenticationRequestRequestTypeDef(BaseValidatorModel):
    authenticationProviders: Sequence[AuthenticationProviderTypesType]
    workspaceId: str
    samlConfiguration: Optional[SamlConfigurationTypeDef] = None

class AssociateLicenseResponseTypeDef(BaseValidatorModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(BaseValidatorModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceResponseTypeDef(BaseValidatorModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceResponseTypeDef(BaseValidatorModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateLicenseResponseTypeDef(BaseValidatorModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceResponseTypeDef(BaseValidatorModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePermissionsResponseTypeDef(BaseValidatorModel):
    errors: List[UpdateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePermissionsRequestRequestTypeDef(BaseValidatorModel):
    updateInstructionBatch: Sequence[UpdateInstructionUnionTypeDef]
    workspaceId: str

class AuthenticationDescriptionTypeDef(BaseValidatorModel):
    providers: List[AuthenticationProviderTypesType]
    awsSso: Optional[AwsSsoAuthenticationTypeDef] = None
    saml: Optional[SamlAuthenticationTypeDef] = None

class DescribeWorkspaceAuthenticationResponseTypeDef(BaseValidatorModel):
    authentication: AuthenticationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceAuthenticationResponseTypeDef(BaseValidatorModel):
    authentication: AuthenticationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


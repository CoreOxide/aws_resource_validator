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
from aws_resource_validator.pydantic_models.grafana_constants import *

class AssertionAttributesTypeDef(BaseValidatorModel):
    email: Optional[str] = None
    groups: Optional[str] = None
    login: Optional[str] = None
    name: Optional[str] = None
    org: Optional[str] = None
    role: Optional[str] = None


class AssociateLicenseRequestTypeDef(BaseValidatorModel):
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


class CreateWorkspaceApiKeyRequestTypeDef(BaseValidatorModel):
    keyName: str
    keyRole: str
    secondsToLive: int
    workspaceId: str


class CreateWorkspaceServiceAccountRequestTypeDef(BaseValidatorModel):
    grafanaRole: RoleType
    name: str
    workspaceId: str


class CreateWorkspaceServiceAccountTokenRequestTypeDef(BaseValidatorModel):
    name: str
    secondsToLive: int
    serviceAccountId: str
    workspaceId: str


class DeleteWorkspaceApiKeyRequestTypeDef(BaseValidatorModel):
    keyName: str
    workspaceId: str


class DeleteWorkspaceRequestTypeDef(BaseValidatorModel):
    workspaceId: str


class DeleteWorkspaceServiceAccountRequestTypeDef(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str


class DeleteWorkspaceServiceAccountTokenRequestTypeDef(BaseValidatorModel):
    serviceAccountId: str
    tokenId: str
    workspaceId: str


class DescribeWorkspaceAuthenticationRequestTypeDef(BaseValidatorModel):
    workspaceId: str


class DescribeWorkspaceConfigurationRequestTypeDef(BaseValidatorModel):
    workspaceId: str


class DescribeWorkspaceRequestTypeDef(BaseValidatorModel):
    workspaceId: str


class DisassociateLicenseRequestTypeDef(BaseValidatorModel):
    licenseType: LicenseTypeType
    workspaceId: str


class IdpMetadataTypeDef(BaseValidatorModel):
    url: Optional[str] = None
    xml: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListPermissionsRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    groupId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    userId: Optional[str] = None
    userType: Optional[UserTypeType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListVersionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    workspaceId: Optional[str] = None


class ListWorkspaceServiceAccountTokensRequestTypeDef(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkspaceServiceAccountsRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkspacesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NetworkAccessConfigurationOutputTypeDef(BaseValidatorModel):
    prefixListIds: List[str]
    vpceIds: List[str]


class NetworkAccessConfigurationTypeDef(BaseValidatorModel):
    prefixListIds: Sequence[str]
    vpceIds: Sequence[str]


class RoleValuesOutputTypeDef(BaseValidatorModel):
    admin: Optional[List[str]] = None
    editor: Optional[List[str]] = None


class RoleValuesTypeDef(BaseValidatorModel):
    admin: Optional[Sequence[str]] = None
    editor: Optional[Sequence[str]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateWorkspaceConfigurationRequestTypeDef(BaseValidatorModel):
    configuration: str
    workspaceId: str
    grafanaVersion: Optional[str] = None


class VpcConfigurationOutputTypeDef(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]


class VpcConfigurationTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]


class CreateWorkspaceApiKeyResponseTypeDef(BaseValidatorModel):
    key: str
    keyName: str
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ServiceAccountTokenSummaryWithKeyTypeDef(BaseValidatorModel):
    pass


class CreateWorkspaceServiceAccountTokenResponseTypeDef(BaseValidatorModel):
    serviceAccountId: str
    serviceAccountToken: ServiceAccountTokenSummaryWithKeyTypeDef
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPermissionsRequestPaginateTypeDef(BaseValidatorModel):
    workspaceId: str
    groupId: Optional[str] = None
    userId: Optional[str] = None
    userType: Optional[UserTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVersionsRequestPaginateTypeDef(BaseValidatorModel):
    workspaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkspaceServiceAccountTokensRequestPaginateTypeDef(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkspaceServiceAccountsRequestPaginateTypeDef(BaseValidatorModel):
    workspaceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkspacesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ServiceAccountTokenSummaryTypeDef(BaseValidatorModel):
    pass


class ListWorkspaceServiceAccountTokensResponseTypeDef(BaseValidatorModel):
    serviceAccountId: str
    serviceAccountTokens: List[ServiceAccountTokenSummaryTypeDef]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ServiceAccountSummaryTypeDef(BaseValidatorModel):
    pass


class ListWorkspaceServiceAccountsResponseTypeDef(BaseValidatorModel):
    serviceAccounts: List[ServiceAccountSummaryTypeDef]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UserTypeDef(BaseValidatorModel):
    pass


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


class WorkspaceSummaryTypeDef(BaseValidatorModel):
    pass


class ListWorkspacesResponseTypeDef(BaseValidatorModel):
    workspaces: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPermissionsResponseTypeDef(BaseValidatorModel):
    permissions: List[PermissionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateErrorTypeDef(BaseValidatorModel):
    causedBy: UpdateInstructionOutputTypeDef
    code: int
    message: str


class SamlAuthenticationTypeDef(BaseValidatorModel):
    status: SamlConfigurationStatusType
    configuration: Optional[SamlConfigurationOutputTypeDef] = None


class WorkspaceDescriptionTypeDef(BaseValidatorModel):
    pass


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


class NetworkAccessConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class VpcConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateWorkspaceRequestTypeDef(BaseValidatorModel):
    accountAccessType: AccountAccessTypeType
    authenticationProviders: Sequence[AuthenticationProviderTypesType]
    permissionType: PermissionTypeType
    clientToken: Optional[str] = None
    configuration: Optional[str] = None
    grafanaVersion: Optional[str] = None
    networkAccessControl: Optional[NetworkAccessConfigurationUnionTypeDef] = None
    organizationRoleName: Optional[str] = None
    stackSetName: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    vpcConfiguration: Optional[VpcConfigurationUnionTypeDef] = None
    workspaceDataSources: Optional[Sequence[DataSourceTypeType]] = None
    workspaceDescription: Optional[str] = None
    workspaceName: Optional[str] = None
    workspaceNotificationDestinations: Optional[Sequence[Literal["SNS"]]] = None
    workspaceOrganizationalUnits: Optional[Sequence[str]] = None
    workspaceRoleArn: Optional[str] = None


class UpdateWorkspaceRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    accountAccessType: Optional[AccountAccessTypeType] = None
    networkAccessControl: Optional[NetworkAccessConfigurationUnionTypeDef] = None
    organizationRoleName: Optional[str] = None
    permissionType: Optional[PermissionTypeType] = None
    removeNetworkAccessConfiguration: Optional[bool] = None
    removeVpcConfiguration: Optional[bool] = None
    stackSetName: Optional[str] = None
    vpcConfiguration: Optional[VpcConfigurationUnionTypeDef] = None
    workspaceDataSources: Optional[Sequence[DataSourceTypeType]] = None
    workspaceDescription: Optional[str] = None
    workspaceName: Optional[str] = None
    workspaceNotificationDestinations: Optional[Sequence[Literal["SNS"]]] = None
    workspaceOrganizationalUnits: Optional[Sequence[str]] = None
    workspaceRoleArn: Optional[str] = None


class UpdatePermissionsResponseTypeDef(BaseValidatorModel):
    errors: List[UpdateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateInstructionUnionTypeDef(BaseValidatorModel):
    pass


class UpdatePermissionsRequestTypeDef(BaseValidatorModel):
    updateInstructionBatch: Sequence[UpdateInstructionUnionTypeDef]
    workspaceId: str


class AuthenticationDescriptionTypeDef(BaseValidatorModel):
    providers: List[AuthenticationProviderTypesType]
    awsSso: Optional[AwsSsoAuthenticationTypeDef] = None
    saml: Optional[SamlAuthenticationTypeDef] = None


class SamlConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateWorkspaceAuthenticationRequestTypeDef(BaseValidatorModel):
    authenticationProviders: Sequence[AuthenticationProviderTypesType]
    workspaceId: str
    samlConfiguration: Optional[SamlConfigurationUnionTypeDef] = None


class DescribeWorkspaceAuthenticationResponseTypeDef(BaseValidatorModel):
    authentication: AuthenticationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWorkspaceAuthenticationResponseTypeDef(BaseValidatorModel):
    authentication: AuthenticationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



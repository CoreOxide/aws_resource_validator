from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.grafana.grafana_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssertionAttributes(BaseValidatorModel):
    email: Optional[str] = None
    groups: Optional[str] = None
    login: Optional[str] = None
    name: Optional[str] = None
    org: Optional[str] = None
    role: Optional[str] = None


class AssociateLicenseRequest(BaseValidatorModel):
    licenseType: LicenseTypeType
    workspaceId: str
    grafanaToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AwsSsoAuthentication(BaseValidatorModel):
    ssoClientId: Optional[str] = None


class AuthenticationSummary(BaseValidatorModel):
    providers: List[AuthenticationProviderTypesType]
    samlConfigurationStatus: Optional[SamlConfigurationStatusType] = None


class CreateWorkspaceApiKeyRequest(BaseValidatorModel):
    keyName: str
    keyRole: str
    secondsToLive: int
    workspaceId: str


class CreateWorkspaceServiceAccountRequest(BaseValidatorModel):
    grafanaRole: RoleType
    name: str
    workspaceId: str


class CreateWorkspaceServiceAccountTokenRequest(BaseValidatorModel):
    name: str
    secondsToLive: int
    serviceAccountId: str
    workspaceId: str


class ServiceAccountTokenSummaryWithKey(BaseValidatorModel):
    id: str
    key: str
    name: str


class DeleteWorkspaceApiKeyRequest(BaseValidatorModel):
    keyName: str
    workspaceId: str


class DeleteWorkspaceRequest(BaseValidatorModel):
    workspaceId: str


class DeleteWorkspaceServiceAccountRequest(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str


class DeleteWorkspaceServiceAccountTokenRequest(BaseValidatorModel):
    serviceAccountId: str
    tokenId: str
    workspaceId: str


class DescribeWorkspaceAuthenticationRequest(BaseValidatorModel):
    workspaceId: str


class DescribeWorkspaceConfigurationRequest(BaseValidatorModel):
    workspaceId: str


class DescribeWorkspaceRequest(BaseValidatorModel):
    workspaceId: str


class DisassociateLicenseRequest(BaseValidatorModel):
    licenseType: LicenseTypeType
    workspaceId: str


class IdpMetadata(BaseValidatorModel):
    url: Optional[str] = None
    xml: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListPermissionsRequest(BaseValidatorModel):
    workspaceId: str
    groupId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    userId: Optional[str] = None
    userType: Optional[UserTypeType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListVersionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    workspaceId: Optional[str] = None


class ListWorkspaceServiceAccountTokensRequest(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ServiceAccountTokenSummary(BaseValidatorModel):
    createdAt: datetime
    expiresAt: datetime
    id: str
    name: str
    lastUsedAt: Optional[datetime] = None


class ListWorkspaceServiceAccountsRequest(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ServiceAccountSummary(BaseValidatorModel):
    grafanaRole: RoleType
    id: str
    isDisabled: str
    name: str


class ListWorkspacesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NetworkAccessConfigurationOutput(BaseValidatorModel):
    prefixListIds: List[str]
    vpceIds: List[str]


class NetworkAccessConfiguration(BaseValidatorModel):
    prefixListIds: List[str]
    vpceIds: List[str]


class User(BaseValidatorModel):
    id: str
    type: UserTypeType


class RoleValuesOutput(BaseValidatorModel):
    admin: Optional[List[str]] = None
    editor: Optional[List[str]] = None


class RoleValues(BaseValidatorModel):
    admin: Optional[List[str]] = None
    editor: Optional[List[str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateWorkspaceConfigurationRequest(BaseValidatorModel):
    configuration: str
    workspaceId: str
    grafanaVersion: Optional[str] = None


class VpcConfigurationOutput(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]


class VpcConfiguration(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]


class CreateWorkspaceApiKeyResponse(BaseValidatorModel):
    key: str
    keyName: str
    workspaceId: str
    ResponseMetadata: ResponseMetadata


class CreateWorkspaceServiceAccountResponse(BaseValidatorModel):
    grafanaRole: RoleType
    id: str
    name: str
    workspaceId: str
    ResponseMetadata: ResponseMetadata


class DeleteWorkspaceApiKeyResponse(BaseValidatorModel):
    keyName: str
    workspaceId: str
    ResponseMetadata: ResponseMetadata


class DeleteWorkspaceServiceAccountResponse(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str
    ResponseMetadata: ResponseMetadata


class DeleteWorkspaceServiceAccountTokenResponse(BaseValidatorModel):
    serviceAccountId: str
    tokenId: str
    workspaceId: str
    ResponseMetadata: ResponseMetadata


class DescribeWorkspaceConfigurationResponse(BaseValidatorModel):
    configuration: str
    grafanaVersion: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListVersionsResponse(BaseValidatorModel):
    grafanaVersions: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkspaceSummary(BaseValidatorModel):
    authentication: AuthenticationSummary
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
    notificationDestinations: Optional[List[Literal['SNS']]] = None
    tags: Optional[Dict[str, str]] = None


class CreateWorkspaceServiceAccountTokenResponse(BaseValidatorModel):
    serviceAccountId: str
    serviceAccountToken: ServiceAccountTokenSummaryWithKey
    workspaceId: str
    ResponseMetadata: ResponseMetadata


class ListPermissionsRequestPaginate(BaseValidatorModel):
    workspaceId: str
    groupId: Optional[str] = None
    userId: Optional[str] = None
    userType: Optional[UserTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVersionsRequestPaginate(BaseValidatorModel):
    workspaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkspaceServiceAccountTokensRequestPaginate(BaseValidatorModel):
    serviceAccountId: str
    workspaceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkspaceServiceAccountsRequestPaginate(BaseValidatorModel):
    workspaceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkspacesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkspaceServiceAccountTokensResponse(BaseValidatorModel):
    serviceAccountId: str
    serviceAccountTokens: List[ServiceAccountTokenSummary]
    workspaceId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWorkspaceServiceAccountsResponse(BaseValidatorModel):
    serviceAccounts: List[ServiceAccountSummary]
    workspaceId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

NetworkAccessConfigurationUnion = Union[NetworkAccessConfiguration, NetworkAccessConfigurationOutput]


class PermissionEntry(BaseValidatorModel):
    role: RoleType
    user: User


class UpdateInstructionOutput(BaseValidatorModel):
    action: UpdateActionType
    role: RoleType
    users: List[User]


class UpdateInstruction(BaseValidatorModel):
    action: UpdateActionType
    role: RoleType
    users: List[User]


class SamlConfigurationOutput(BaseValidatorModel):
    idpMetadata: IdpMetadata
    allowedOrganizations: Optional[List[str]] = None
    assertionAttributes: Optional[AssertionAttributes] = None
    loginValidityDuration: Optional[int] = None
    roleValues: Optional[RoleValuesOutput] = None


class SamlConfiguration(BaseValidatorModel):
    idpMetadata: IdpMetadata
    allowedOrganizations: Optional[List[str]] = None
    assertionAttributes: Optional[AssertionAttributes] = None
    loginValidityDuration: Optional[int] = None
    roleValues: Optional[RoleValues] = None


class WorkspaceDescription(BaseValidatorModel):
    authentication: AuthenticationSummary
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
    networkAccessControl: Optional[NetworkAccessConfigurationOutput] = None
    notificationDestinations: Optional[List[Literal['SNS']]] = None
    organizationRoleName: Optional[str] = None
    organizationalUnits: Optional[List[str]] = None
    permissionType: Optional[PermissionTypeType] = None
    stackSetName: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    vpcConfiguration: Optional[VpcConfigurationOutput] = None
    workspaceRoleArn: Optional[str] = None

VpcConfigurationUnion = Union[VpcConfiguration, VpcConfigurationOutput]


class ListWorkspacesResponse(BaseValidatorModel):
    workspaces: List[WorkspaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListPermissionsResponse(BaseValidatorModel):
    permissions: List[PermissionEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateError(BaseValidatorModel):
    causedBy: UpdateInstructionOutput
    code: int
    message: str

UpdateInstructionUnion = Union[UpdateInstruction, UpdateInstructionOutput]


class SamlAuthentication(BaseValidatorModel):
    status: SamlConfigurationStatusType
    configuration: Optional[SamlConfigurationOutput] = None

SamlConfigurationUnion = Union[SamlConfiguration, SamlConfigurationOutput]


class AssociateLicenseResponse(BaseValidatorModel):
    workspace: WorkspaceDescription
    ResponseMetadata: ResponseMetadata


class CreateWorkspaceResponse(BaseValidatorModel):
    workspace: WorkspaceDescription
    ResponseMetadata: ResponseMetadata


class DeleteWorkspaceResponse(BaseValidatorModel):
    workspace: WorkspaceDescription
    ResponseMetadata: ResponseMetadata


class DescribeWorkspaceResponse(BaseValidatorModel):
    workspace: WorkspaceDescription
    ResponseMetadata: ResponseMetadata


class DisassociateLicenseResponse(BaseValidatorModel):
    workspace: WorkspaceDescription
    ResponseMetadata: ResponseMetadata


class UpdateWorkspaceResponse(BaseValidatorModel):
    workspace: WorkspaceDescription
    ResponseMetadata: ResponseMetadata


class CreateWorkspaceRequest(BaseValidatorModel):
    accountAccessType: AccountAccessTypeType
    authenticationProviders: List[AuthenticationProviderTypesType]
    permissionType: PermissionTypeType
    clientToken: Optional[str] = None
    configuration: Optional[str] = None
    grafanaVersion: Optional[str] = None
    networkAccessControl: Optional[NetworkAccessConfigurationUnion] = None
    organizationRoleName: Optional[str] = None
    stackSetName: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    vpcConfiguration: Optional[VpcConfigurationUnion] = None
    workspaceDataSources: Optional[List[DataSourceTypeType]] = None
    workspaceDescription: Optional[str] = None
    workspaceName: Optional[str] = None
    workspaceNotificationDestinations: Optional[List[Literal['SNS']]] = None
    workspaceOrganizationalUnits: Optional[List[str]] = None
    workspaceRoleArn: Optional[str] = None


class UpdateWorkspaceRequest(BaseValidatorModel):
    workspaceId: str
    accountAccessType: Optional[AccountAccessTypeType] = None
    networkAccessControl: Optional[NetworkAccessConfigurationUnion] = None
    organizationRoleName: Optional[str] = None
    permissionType: Optional[PermissionTypeType] = None
    removeNetworkAccessConfiguration: Optional[bool] = None
    removeVpcConfiguration: Optional[bool] = None
    stackSetName: Optional[str] = None
    vpcConfiguration: Optional[VpcConfigurationUnion] = None
    workspaceDataSources: Optional[List[DataSourceTypeType]] = None
    workspaceDescription: Optional[str] = None
    workspaceName: Optional[str] = None
    workspaceNotificationDestinations: Optional[List[Literal['SNS']]] = None
    workspaceOrganizationalUnits: Optional[List[str]] = None
    workspaceRoleArn: Optional[str] = None


class UpdatePermissionsResponse(BaseValidatorModel):
    errors: List[UpdateError]
    ResponseMetadata: ResponseMetadata


class UpdatePermissionsRequest(BaseValidatorModel):
    updateInstructionBatch: List[UpdateInstructionUnion]
    workspaceId: str


class AuthenticationDescription(BaseValidatorModel):
    providers: List[AuthenticationProviderTypesType]
    awsSso: Optional[AwsSsoAuthentication] = None
    saml: Optional[SamlAuthentication] = None


class UpdateWorkspaceAuthenticationRequest(BaseValidatorModel):
    authenticationProviders: List[AuthenticationProviderTypesType]
    workspaceId: str
    samlConfiguration: Optional[SamlConfigurationUnion] = None


class DescribeWorkspaceAuthenticationResponse(BaseValidatorModel):
    authentication: AuthenticationDescription
    ResponseMetadata: ResponseMetadata


class UpdateWorkspaceAuthenticationResponse(BaseValidatorModel):
    authentication: AuthenticationDescription
    ResponseMetadata: ResponseMetadata
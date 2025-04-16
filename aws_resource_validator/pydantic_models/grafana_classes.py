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


class ListWorkspaceServiceAccountsRequest(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkspacesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NetworkAccessConfigurationOutput(BaseValidatorModel):
    prefixListIds: List[str]
    vpceIds: List[str]


class NetworkAccessConfiguration(BaseValidatorModel):
    prefixListIds: Sequence[str]
    vpceIds: Sequence[str]


class RoleValuesOutput(BaseValidatorModel):
    admin: Optional[List[str]] = None
    editor: Optional[List[str]] = None


class RoleValues(BaseValidatorModel):
    admin: Optional[Sequence[str]] = None
    editor: Optional[Sequence[str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateWorkspaceConfigurationRequest(BaseValidatorModel):
    configuration: str
    workspaceId: str
    grafanaVersion: Optional[str] = None


class VpcConfigurationOutput(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]


class VpcConfiguration(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]


class CreateWorkspaceApiKeyResponse(BaseValidatorModel):
    key: str
    keyName: str
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


class ServiceAccountTokenSummaryWithKey(BaseValidatorModel):
    pass


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


class ServiceAccountTokenSummary(BaseValidatorModel):
    pass


class ListWorkspaceServiceAccountTokensResponse(BaseValidatorModel):
    serviceAccountId: str
    serviceAccountTokens: List[ServiceAccountTokenSummary]
    workspaceId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ServiceAccountSummary(BaseValidatorModel):
    pass


class ListWorkspaceServiceAccountsResponse(BaseValidatorModel):
    serviceAccounts: List[ServiceAccountSummary]
    workspaceId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class User(BaseValidatorModel):
    pass


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
    users: Sequence[User]


class SamlConfigurationOutput(BaseValidatorModel):
    idpMetadata: IdpMetadata
    allowedOrganizations: Optional[List[str]] = None
    assertionAttributes: Optional[AssertionAttributes] = None
    loginValidityDuration: Optional[int] = None
    roleValues: Optional[RoleValuesOutput] = None


class SamlConfiguration(BaseValidatorModel):
    idpMetadata: IdpMetadata
    allowedOrganizations: Optional[Sequence[str]] = None
    assertionAttributes: Optional[AssertionAttributes] = None
    loginValidityDuration: Optional[int] = None
    roleValues: Optional[RoleValues] = None


class WorkspaceSummary(BaseValidatorModel):
    pass


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


class SamlAuthentication(BaseValidatorModel):
    status: SamlConfigurationStatusType
    configuration: Optional[SamlConfigurationOutput] = None


class WorkspaceDescription(BaseValidatorModel):
    pass


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


class NetworkAccessConfigurationUnion(BaseValidatorModel):
    pass


class VpcConfigurationUnion(BaseValidatorModel):
    pass


class CreateWorkspaceRequest(BaseValidatorModel):
    accountAccessType: AccountAccessTypeType
    authenticationProviders: Sequence[AuthenticationProviderTypesType]
    permissionType: PermissionTypeType
    clientToken: Optional[str] = None
    configuration: Optional[str] = None
    grafanaVersion: Optional[str] = None
    networkAccessControl: Optional[NetworkAccessConfigurationUnion] = None
    organizationRoleName: Optional[str] = None
    stackSetName: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    vpcConfiguration: Optional[VpcConfigurationUnion] = None
    workspaceDataSources: Optional[Sequence[DataSourceTypeType]] = None
    workspaceDescription: Optional[str] = None
    workspaceName: Optional[str] = None
    workspaceNotificationDestinations: Optional[Sequence[Literal["SNS"]]] = None
    workspaceOrganizationalUnits: Optional[Sequence[str]] = None
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
    workspaceDataSources: Optional[Sequence[DataSourceTypeType]] = None
    workspaceDescription: Optional[str] = None
    workspaceName: Optional[str] = None
    workspaceNotificationDestinations: Optional[Sequence[Literal["SNS"]]] = None
    workspaceOrganizationalUnits: Optional[Sequence[str]] = None
    workspaceRoleArn: Optional[str] = None


class UpdatePermissionsResponse(BaseValidatorModel):
    errors: List[UpdateError]
    ResponseMetadata: ResponseMetadata


class UpdateInstructionUnion(BaseValidatorModel):
    pass


class UpdatePermissionsRequest(BaseValidatorModel):
    updateInstructionBatch: Sequence[UpdateInstructionUnion]
    workspaceId: str


class AuthenticationDescription(BaseValidatorModel):
    providers: List[AuthenticationProviderTypesType]
    awsSso: Optional[AwsSsoAuthentication] = None
    saml: Optional[SamlAuthentication] = None


class SamlConfigurationUnion(BaseValidatorModel):
    pass


class UpdateWorkspaceAuthenticationRequest(BaseValidatorModel):
    authenticationProviders: Sequence[AuthenticationProviderTypesType]
    workspaceId: str
    samlConfiguration: Optional[SamlConfigurationUnion] = None


class DescribeWorkspaceAuthenticationResponse(BaseValidatorModel):
    authentication: AuthenticationDescription
    ResponseMetadata: ResponseMetadata


class UpdateWorkspaceAuthenticationResponse(BaseValidatorModel):
    authentication: AuthenticationDescription
    ResponseMetadata: ResponseMetadata



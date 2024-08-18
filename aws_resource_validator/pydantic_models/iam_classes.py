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
from aws_resource_validator.pydantic_models.iam_constants import *

class AccessDetailTypeDef(BaseValidatorModel):
    ServiceName: str
    ServiceNamespace: str
    Region: Optional[str] = None
    EntityPath: Optional[str] = None
    LastAuthenticatedTime: Optional[datetime] = None
    TotalAuthenticatedEntities: Optional[int] = None

class AccessKeyLastUsedTypeDef(BaseValidatorModel):
    LastUsedDate: datetime
    ServiceName: str
    Region: str

class AccessKeyMetadataTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    AccessKeyId: Optional[str] = None
    Status: Optional[statusTypeType] = None
    CreateDate: Optional[datetime] = None

class AccessKeyTypeDef(BaseValidatorModel):
    UserName: str
    AccessKeyId: str
    Status: statusTypeType
    SecretAccessKey: str
    CreateDate: Optional[datetime] = None

class AddClientIDToOpenIDConnectProviderRequestRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ClientID: str

class AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef(BaseValidatorModel):
    RoleName: str

class AddRoleToInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    RoleName: str

class AddUserToGroupRequestGroupAddUserTypeDef(BaseValidatorModel):
    UserName: str

class AddUserToGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserName: str

class AddUserToGroupRequestUserAddGroupTypeDef(BaseValidatorModel):
    GroupName: str

class AttachGroupPolicyRequestGroupAttachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str

class AttachGroupPolicyRequestPolicyAttachGroupTypeDef(BaseValidatorModel):
    GroupName: str

class AttachGroupPolicyRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyArn: str

class AttachRolePolicyRequestPolicyAttachRoleTypeDef(BaseValidatorModel):
    RoleName: str

class AttachRolePolicyRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyArn: str

class AttachRolePolicyRequestRoleAttachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str

class AttachUserPolicyRequestPolicyAttachUserTypeDef(BaseValidatorModel):
    UserName: str

class AttachUserPolicyRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyArn: str

class AttachUserPolicyRequestUserAttachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AttachedPermissionsBoundaryTypeDef(BaseValidatorModel):
    PermissionsBoundaryType: Optional[Literal["PermissionsBoundaryPolicy"]] = None
    PermissionsBoundaryArn: Optional[str] = None

class AttachedPolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyArn: Optional[str] = None

class ChangePasswordRequestRequestTypeDef(BaseValidatorModel):
    OldPassword: str
    NewPassword: str

class ChangePasswordRequestServiceResourceChangePasswordTypeDef(BaseValidatorModel):
    OldPassword: str
    NewPassword: str

class ContextEntryTypeDef(BaseValidatorModel):
    ContextKeyName: Optional[str] = None
    ContextKeyValues: Optional[Sequence[str]] = None
    ContextKeyType: Optional[ContextKeyTypeEnumType] = None

class CreateAccessKeyRequestRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None

class CreateAccountAliasRequestRequestTypeDef(BaseValidatorModel):
    AccountAlias: str

class CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef(BaseValidatorModel):
    AccountAlias: str

class CreateGroupRequestGroupCreateTypeDef(BaseValidatorModel):
    Path: Optional[str] = None

class CreateGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    Path: Optional[str] = None

class CreateGroupRequestServiceResourceCreateGroupTypeDef(BaseValidatorModel):
    GroupName: str
    Path: Optional[str] = None

class GroupTypeDef(BaseValidatorModel):
    Path: str
    GroupName: str
    GroupId: str
    Arn: str
    CreateDate: datetime

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CreateLoginProfileRequestLoginProfileCreateTypeDef(BaseValidatorModel):
    Password: str
    PasswordResetRequired: Optional[bool] = None

class CreateLoginProfileRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    Password: str
    PasswordResetRequired: Optional[bool] = None

class CreateLoginProfileRequestUserCreateLoginProfileTypeDef(BaseValidatorModel):
    Password: str
    PasswordResetRequired: Optional[bool] = None

class LoginProfileTypeDef(BaseValidatorModel):
    UserName: str
    CreateDate: datetime
    PasswordResetRequired: Optional[bool] = None

class CreatePolicyVersionRequestPolicyCreateVersionTypeDef(BaseValidatorModel):
    PolicyDocument: str
    SetAsDefault: Optional[bool] = None

class CreatePolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    PolicyDocument: str
    SetAsDefault: Optional[bool] = None

class CreateServiceLinkedRoleRequestRequestTypeDef(BaseValidatorModel):
    AWSServiceName: str
    Description: Optional[str] = None
    CustomSuffix: Optional[str] = None

class CreateServiceSpecificCredentialRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    ServiceName: str

class ServiceSpecificCredentialTypeDef(BaseValidatorModel):
    CreateDate: datetime
    ServiceName: str
    ServiceUserName: str
    ServicePassword: str
    ServiceSpecificCredentialId: str
    UserName: str
    Status: statusTypeType

class DeactivateMFADeviceRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    SerialNumber: str

class DeleteAccessKeyRequestRequestTypeDef(BaseValidatorModel):
    AccessKeyId: str
    UserName: Optional[str] = None

class DeleteAccountAliasRequestRequestTypeDef(BaseValidatorModel):
    AccountAlias: str

class DeleteGroupPolicyRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyName: str

class DeleteGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str

class DeleteInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str

class DeleteLoginProfileRequestRequestTypeDef(BaseValidatorModel):
    UserName: str

class DeleteOpenIDConnectProviderRequestRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str

class DeletePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str

class DeletePolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    VersionId: str

class DeleteRolePermissionsBoundaryRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str

class DeleteRolePolicyRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyName: str

class DeleteRoleRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str

class DeleteSAMLProviderRequestRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str

class DeleteSSHPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str

class DeleteServerCertificateRequestRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str

class DeleteServiceLinkedRoleRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str

class DeleteServiceSpecificCredentialRequestRequestTypeDef(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None

class DeleteSigningCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateId: str
    UserName: Optional[str] = None

class DeleteUserPermissionsBoundaryRequestRequestTypeDef(BaseValidatorModel):
    UserName: str

class DeleteUserPolicyRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyName: str

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str

class DeleteVirtualMFADeviceRequestRequestTypeDef(BaseValidatorModel):
    SerialNumber: str

class RoleUsageTypeTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    Resources: Optional[List[str]] = None

class DetachGroupPolicyRequestGroupDetachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str

class DetachGroupPolicyRequestPolicyDetachGroupTypeDef(BaseValidatorModel):
    GroupName: str

class DetachGroupPolicyRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyArn: str

class DetachRolePolicyRequestPolicyDetachRoleTypeDef(BaseValidatorModel):
    RoleName: str

class DetachRolePolicyRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyArn: str

class DetachRolePolicyRequestRoleDetachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str

class DetachUserPolicyRequestPolicyDetachUserTypeDef(BaseValidatorModel):
    UserName: str

class DetachUserPolicyRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyArn: str

class DetachUserPolicyRequestUserDetachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str

class EnableMFADeviceRequestMfaDeviceAssociateTypeDef(BaseValidatorModel):
    AuthenticationCode1: str
    AuthenticationCode2: str

class EnableMFADeviceRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str

class EnableMFADeviceRequestUserEnableMfaTypeDef(BaseValidatorModel):
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str

class EntityInfoTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Type: policyOwnerEntityTypeType
    Id: str
    Path: Optional[str] = None

class ErrorDetailsTypeDef(BaseValidatorModel):
    Message: str
    Code: str

class OrganizationsDecisionDetailTypeDef(BaseValidatorModel):
    AllowedByOrganizations: Optional[bool] = None

class PermissionsBoundaryDecisionDetailTypeDef(BaseValidatorModel):
    AllowedByPermissionsBoundary: Optional[bool] = None

class GenerateOrganizationsAccessReportRequestRequestTypeDef(BaseValidatorModel):
    EntityPath: str
    OrganizationsPolicyId: Optional[str] = None

class GenerateServiceLastAccessedDetailsRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    Granularity: Optional[AccessAdvisorUsageGranularityTypeType] = None

class GetAccessKeyLastUsedRequestRequestTypeDef(BaseValidatorModel):
    AccessKeyId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetAccountAuthorizationDetailsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[Sequence[EntityTypeType]] = None
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class PasswordPolicyTypeDef(BaseValidatorModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    ExpirePasswords: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None

class GetContextKeysForCustomPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyInputList: Sequence[str]

class GetContextKeysForPrincipalPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicySourceArn: str
    PolicyInputList: Optional[Sequence[str]] = None

class GetGroupPolicyRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyName: str

class GetGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str

class GetLoginProfileRequestRequestTypeDef(BaseValidatorModel):
    UserName: str

class GetMFADeviceRequestRequestTypeDef(BaseValidatorModel):
    SerialNumber: str
    UserName: Optional[str] = None

class GetOpenIDConnectProviderRequestRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str

class GetOrganizationsAccessReportRequestRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    SortKey: Optional[sortKeyTypeType] = None

class GetPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str

class GetPolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    VersionId: str

class GetRolePolicyRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyName: str

class GetRoleRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str

class GetSAMLProviderRequestRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str

class GetSSHPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Encoding: encodingTypeType

class SSHPublicKeyTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Fingerprint: str
    SSHPublicKeyBody: str
    Status: statusTypeType
    UploadDate: Optional[datetime] = None

class GetServerCertificateRequestRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str

class GetServiceLastAccessedDetailsRequestRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef(BaseValidatorModel):
    JobId: str
    ServiceNamespace: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef(BaseValidatorModel):
    DeletionTaskId: str

class GetUserPolicyRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyName: str

class GetUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None

class ListAccessKeysRequestRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListAccountAliasesRequestRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListAttachedGroupPoliciesRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListAttachedRolePoliciesRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListAttachedUserPoliciesRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListEntitiesForPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    EntityFilter: Optional[EntityTypeType] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class PolicyGroupTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None

class PolicyRoleTypeDef(BaseValidatorModel):
    RoleName: Optional[str] = None
    RoleId: Optional[str] = None

class PolicyUserTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    UserId: Optional[str] = None

class ListGroupPoliciesRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListGroupsForUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListGroupsRequestRequestTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListInstanceProfileTagsRequestRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListInstanceProfilesForRoleRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListInstanceProfilesRequestRequestTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListMFADeviceTagsRequestRequestTypeDef(BaseValidatorModel):
    SerialNumber: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListMFADevicesRequestRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class MFADeviceTypeDef(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    EnableDate: datetime

class ListOpenIDConnectProviderTagsRequestRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class OpenIDConnectProviderListEntryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class PolicyGrantingServiceAccessTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyType: policyTypeType
    PolicyArn: Optional[str] = None
    EntityType: Optional[policyOwnerEntityTypeType] = None
    EntityName: Optional[str] = None

class ListPoliciesGrantingServiceAccessRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    ServiceNamespaces: Sequence[str]
    Marker: Optional[str] = None

class ListPoliciesRequestRequestTypeDef(BaseValidatorModel):
    Scope: Optional[policyScopeTypeType] = None
    OnlyAttached: Optional[bool] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListPolicyTagsRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListPolicyVersionsRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListRolePoliciesRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListRoleTagsRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListRolesRequestRequestTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListSAMLProviderTagsRequestRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class SAMLProviderListEntryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ValidUntil: Optional[datetime] = None
    CreateDate: Optional[datetime] = None

class ListSSHPublicKeysRequestRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class SSHPublicKeyMetadataTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Status: statusTypeType
    UploadDate: datetime

class ListServerCertificateTagsRequestRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListServerCertificatesRequestRequestTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ServerCertificateMetadataTypeDef(BaseValidatorModel):
    Path: str
    ServerCertificateName: str
    ServerCertificateId: str
    Arn: str
    UploadDate: Optional[datetime] = None
    Expiration: Optional[datetime] = None

class ListServiceSpecificCredentialsRequestRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    ServiceName: Optional[str] = None

class ServiceSpecificCredentialMetadataTypeDef(BaseValidatorModel):
    UserName: str
    Status: statusTypeType
    ServiceUserName: str
    CreateDate: datetime
    ServiceSpecificCredentialId: str
    ServiceName: str

class ListSigningCertificatesRequestRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class SigningCertificateTypeDef(BaseValidatorModel):
    UserName: str
    CertificateId: str
    CertificateBody: str
    Status: statusTypeType
    UploadDate: Optional[datetime] = None

class ListUserPoliciesRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListUserTagsRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListUsersRequestRequestTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListVirtualMFADevicesRequestRequestTypeDef(BaseValidatorModel):
    AssignmentStatus: Optional[assignmentStatusTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class PolicyDocumentStatementTypeDef(BaseValidatorModel):
    Effect: str
    Resource: Union[str, List[str]]
    Sid: str
    Action: Union[str, List[str]]

class PositionTypeDef(BaseValidatorModel):
    Line: Optional[int] = None
    Column: Optional[int] = None

class PutGroupPolicyRequestGroupCreatePolicyTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str

class PutGroupPolicyRequestGroupPolicyPutTypeDef(BaseValidatorModel):
    PolicyDocument: str

class PutGroupPolicyRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyName: str
    PolicyDocument: str

class PutRolePermissionsBoundaryRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PermissionsBoundary: str

class PutRolePolicyRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyName: str
    PolicyDocument: str

class PutRolePolicyRequestRolePolicyPutTypeDef(BaseValidatorModel):
    PolicyDocument: str

class PutUserPermissionsBoundaryRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    PermissionsBoundary: str

class PutUserPolicyRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyName: str
    PolicyDocument: str

class PutUserPolicyRequestUserCreatePolicyTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str

class PutUserPolicyRequestUserPolicyPutTypeDef(BaseValidatorModel):
    PolicyDocument: str

class RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ClientID: str

class RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef(BaseValidatorModel):
    RoleName: str

class RemoveRoleFromInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    RoleName: str

class RemoveUserFromGroupRequestGroupRemoveUserTypeDef(BaseValidatorModel):
    UserName: str

class RemoveUserFromGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserName: str

class RemoveUserFromGroupRequestUserRemoveGroupTypeDef(BaseValidatorModel):
    GroupName: str

class ResetServiceSpecificCredentialRequestRequestTypeDef(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None

class ResyncMFADeviceRequestMfaDeviceResyncTypeDef(BaseValidatorModel):
    AuthenticationCode1: str
    AuthenticationCode2: str

class ResyncMFADeviceRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str

class RoleLastUsedTypeDef(BaseValidatorModel):
    LastUsedDate: Optional[datetime] = None
    Region: Optional[str] = None

class TrackedActionLastAccessedTypeDef(BaseValidatorModel):
    ActionName: Optional[str] = None
    LastAccessedEntity: Optional[str] = None
    LastAccessedTime: Optional[datetime] = None
    LastAccessedRegion: Optional[str] = None

class SetDefaultPolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    VersionId: str

class SetSecurityTokenServicePreferencesRequestRequestTypeDef(BaseValidatorModel):
    GlobalEndpointTokenVersion: globalEndpointTokenVersionType

class UntagInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    TagKeys: Sequence[str]

class UntagMFADeviceRequestRequestTypeDef(BaseValidatorModel):
    SerialNumber: str
    TagKeys: Sequence[str]

class UntagOpenIDConnectProviderRequestRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    TagKeys: Sequence[str]

class UntagPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    TagKeys: Sequence[str]

class UntagRoleRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    TagKeys: Sequence[str]

class UntagSAMLProviderRequestRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    TagKeys: Sequence[str]

class UntagServerCertificateRequestRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    TagKeys: Sequence[str]

class UntagUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    TagKeys: Sequence[str]

class UpdateAccessKeyRequestAccessKeyActivateTypeDef(BaseValidatorModel):
    Status: Optional[statusTypeType] = None

class UpdateAccessKeyRequestAccessKeyDeactivateTypeDef(BaseValidatorModel):
    Status: Optional[statusTypeType] = None

class UpdateAccessKeyRequestAccessKeyPairActivateTypeDef(BaseValidatorModel):
    Status: Optional[statusTypeType] = None

class UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef(BaseValidatorModel):
    Status: Optional[statusTypeType] = None

class UpdateAccessKeyRequestRequestTypeDef(BaseValidatorModel):
    AccessKeyId: str
    Status: statusTypeType
    UserName: Optional[str] = None

class UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef(BaseValidatorModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None

class UpdateAccountPasswordPolicyRequestRequestTypeDef(BaseValidatorModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None

class UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef(BaseValidatorModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None

class UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef(BaseValidatorModel):
    PolicyDocument: str

class UpdateAssumeRolePolicyRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyDocument: str

class UpdateGroupRequestGroupUpdateTypeDef(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None

class UpdateGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None

class UpdateLoginProfileRequestLoginProfileUpdateTypeDef(BaseValidatorModel):
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None

class UpdateLoginProfileRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None

class UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ThumbprintList: Sequence[str]

class UpdateRoleDescriptionRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Description: str

class UpdateRoleRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None

class UpdateSAMLProviderRequestRequestTypeDef(BaseValidatorModel):
    SAMLMetadataDocument: str
    SAMLProviderArn: str

class UpdateSAMLProviderRequestSamlProviderUpdateTypeDef(BaseValidatorModel):
    SAMLMetadataDocument: str

class UpdateSSHPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Status: statusTypeType

class UpdateServerCertificateRequestRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None

class UpdateServerCertificateRequestServerCertificateUpdateTypeDef(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None

class UpdateServiceSpecificCredentialRequestRequestTypeDef(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    Status: statusTypeType
    UserName: Optional[str] = None

class UpdateSigningCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateId: str
    Status: statusTypeType
    UserName: Optional[str] = None

class UpdateSigningCertificateRequestSigningCertificateActivateTypeDef(BaseValidatorModel):
    Status: Optional[statusTypeType] = None

class UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef(BaseValidatorModel):
    Status: Optional[statusTypeType] = None

class UpdateUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None

class UpdateUserRequestUserUpdateTypeDef(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None

class UploadSSHPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyBody: str

class UploadSigningCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateBody: str
    UserName: Optional[str] = None

class UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef(BaseValidatorModel):
    CertificateBody: str
    UserName: Optional[str] = None

class AttachedPermissionsBoundaryResponseTypeDef(BaseValidatorModel):
    PermissionsBoundaryType: Literal["PermissionsBoundaryPolicy"]
    PermissionsBoundaryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessKeyResponseTypeDef(BaseValidatorModel):
    AccessKey: AccessKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceLinkedRoleResponseTypeDef(BaseValidatorModel):
    DeletionTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateCredentialReportResponseTypeDef(BaseValidatorModel):
    State: ReportStateTypeType
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateOrganizationsAccessReportResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateServiceLastAccessedDetailsResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessKeyLastUsedResponseTypeDef(BaseValidatorModel):
    UserName: str
    AccessKeyLastUsed: AccessKeyLastUsedTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSummaryResponseTypeDef(BaseValidatorModel):
    SummaryMap: Dict[summaryKeyTypeType, int]
    ResponseMetadata: ResponseMetadataTypeDef

class GetContextKeysForPolicyResponseTypeDef(BaseValidatorModel):
    ContextKeyNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCredentialReportResponseTypeDef(BaseValidatorModel):
    Content: bytes
    ReportFormat: Literal["text/csv"]
    GeneratedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMFADeviceResponseTypeDef(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    EnableDate: datetime
    Certifications: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessKeysResponseTypeDef(BaseValidatorModel):
    AccessKeyMetadata: List[AccessKeyMetadataTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAliasesResponseTypeDef(BaseValidatorModel):
    AccountAliases: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupPoliciesResponseTypeDef(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRolePoliciesResponseTypeDef(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserPoliciesResponseTypeDef(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RoleLastUsedResponseTypeDef(BaseValidatorModel):
    LastUsedDate: datetime
    Region: str
    ResponseMetadata: ResponseMetadataTypeDef

class ServerCertificateMetadataResponseTypeDef(BaseValidatorModel):
    Path: str
    ServerCertificateName: str
    ServerCertificateId: str
    Arn: str
    UploadDate: datetime
    Expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSAMLProviderResponseTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedGroupPoliciesResponseTypeDef(BaseValidatorModel):
    AttachedPolicies: List[AttachedPolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedRolePoliciesResponseTypeDef(BaseValidatorModel):
    AttachedPolicies: List[AttachedPolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedUserPoliciesResponseTypeDef(BaseValidatorModel):
    AttachedPolicies: List[AttachedPolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class SimulateCustomPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyInputList: Sequence[str]
    ActionNames: Sequence[str]
    PermissionsBoundaryPolicyInputList: Optional[Sequence[str]] = None
    ResourceArns: Optional[Sequence[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[Sequence[ContextEntryTypeDef]] = None
    ResourceHandlingOption: Optional[str] = None
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class SimulatePrincipalPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicySourceArn: str
    ActionNames: Sequence[str]
    PolicyInputList: Optional[Sequence[str]] = None
    PermissionsBoundaryPolicyInputList: Optional[Sequence[str]] = None
    ResourceArns: Optional[Sequence[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[Sequence[ContextEntryTypeDef]] = None
    ResourceHandlingOption: Optional[str] = None
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class CreateGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsForUserResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateOpenIDConnectProviderRequestRequestTypeDef(BaseValidatorModel):
    Url: str
    ClientIDList: Optional[Sequence[str]] = None
    ThumbprintList: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateOpenIDConnectProviderResponseTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreatePolicyRequestServiceResourceCreatePolicyTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateRoleRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateRoleRequestServiceResourceCreateRoleTypeDef(BaseValidatorModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSAMLProviderRequestRequestTypeDef(BaseValidatorModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef(BaseValidatorModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSAMLProviderResponseTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserRequestServiceResourceCreateUserTypeDef(BaseValidatorModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserRequestUserCreateTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVirtualMFADeviceRequestRequestTypeDef(BaseValidatorModel):
    VirtualMFADeviceName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef(BaseValidatorModel):
    VirtualMFADeviceName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetOpenIDConnectProviderResponseTypeDef(BaseValidatorModel):
    Url: str
    ClientIDList: List[str]
    ThumbprintList: List[str]
    CreateDate: datetime
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSAMLProviderResponseTypeDef(BaseValidatorModel):
    SAMLMetadataDocument: str
    CreateDate: datetime
    ValidUntil: datetime
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfileTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMFADeviceTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOpenIDConnectProviderTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoleTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSAMLProviderTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServerCertificateTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyId: Optional[str] = None
    Arn: Optional[str] = None
    Path: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    AttachmentCount: Optional[int] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    IsAttachable: Optional[bool] = None
    Description: Optional[str] = None
    CreateDate: Optional[datetime] = None
    UpdateDate: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    Tags: Sequence[TagTypeDef]

class TagMFADeviceRequestRequestTypeDef(BaseValidatorModel):
    SerialNumber: str
    Tags: Sequence[TagTypeDef]

class TagOpenIDConnectProviderRequestRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Tags: Sequence[TagTypeDef]

class TagPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    Tags: Sequence[TagTypeDef]

class TagRoleRequestRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Tags: Sequence[TagTypeDef]

class TagSAMLProviderRequestRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    Tags: Sequence[TagTypeDef]

class TagServerCertificateRequestRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    Tags: Sequence[TagTypeDef]

class TagUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    Tags: Sequence[TagTypeDef]

class UploadServerCertificateRequestRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UserResponseTypeDef(BaseValidatorModel):
    Path: str
    UserName: str
    UserId: str
    Arn: str
    CreateDate: datetime
    PasswordLastUsed: datetime
    PermissionsBoundary: AttachedPermissionsBoundaryTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UserTypeDef(BaseValidatorModel):
    Path: str
    UserName: str
    UserId: str
    Arn: str
    CreateDate: datetime
    PasswordLastUsed: Optional[datetime] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundaryTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateLoginProfileResponseTypeDef(BaseValidatorModel):
    LoginProfile: LoginProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoginProfileResponseTypeDef(BaseValidatorModel):
    LoginProfile: LoginProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceSpecificCredentialResponseTypeDef(BaseValidatorModel):
    ServiceSpecificCredential: ServiceSpecificCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetServiceSpecificCredentialResponseTypeDef(BaseValidatorModel):
    ServiceSpecificCredential: ServiceSpecificCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletionTaskFailureReasonTypeTypeDef(BaseValidatorModel):
    Reason: Optional[str] = None
    RoleUsageList: Optional[List[RoleUsageTypeTypeDef]] = None

class EntityDetailsTypeDef(BaseValidatorModel):
    EntityInfo: EntityInfoTypeDef
    LastAuthenticated: Optional[datetime] = None

class GetOrganizationsAccessReportResponseTypeDef(BaseValidatorModel):
    JobStatus: jobStatusTypeType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    NumberOfServicesAccessible: int
    NumberOfServicesNotAccessed: int
    AccessDetails: List[AccessDetailTypeDef]
    IsTruncated: bool
    Marker: str
    ErrorDetails: ErrorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountAuthorizationDetailsRequestGetAccountAuthorizationDetailsPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[Sequence[EntityTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetGroupRequestGetGroupPaginateTypeDef(BaseValidatorModel):
    GroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessKeysRequestListAccessKeysPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAliasesRequestListAccountAliasesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedGroupPoliciesRequestListAttachedGroupPoliciesPaginateTypeDef(BaseValidatorModel):
    GroupName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedRolePoliciesRequestListAttachedRolePoliciesPaginateTypeDef(BaseValidatorModel):
    RoleName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedUserPoliciesRequestListAttachedUserPoliciesPaginateTypeDef(BaseValidatorModel):
    UserName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEntitiesForPolicyRequestListEntitiesForPolicyPaginateTypeDef(BaseValidatorModel):
    PolicyArn: str
    EntityFilter: Optional[EntityTypeType] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupPoliciesRequestListGroupPoliciesPaginateTypeDef(BaseValidatorModel):
    GroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsForUserRequestListGroupsForUserPaginateTypeDef(BaseValidatorModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceProfileTagsRequestListInstanceProfileTagsPaginateTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceProfilesForRoleRequestListInstanceProfilesForRolePaginateTypeDef(BaseValidatorModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMFADeviceTagsRequestListMFADeviceTagsPaginateTypeDef(BaseValidatorModel):
    SerialNumber: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMFADevicesRequestListMFADevicesPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOpenIDConnectProviderTagsRequestListOpenIDConnectProviderTagsPaginateTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesRequestListPoliciesPaginateTypeDef(BaseValidatorModel):
    Scope: Optional[policyScopeTypeType] = None
    OnlyAttached: Optional[bool] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyTagsRequestListPolicyTagsPaginateTypeDef(BaseValidatorModel):
    PolicyArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyVersionsRequestListPolicyVersionsPaginateTypeDef(BaseValidatorModel):
    PolicyArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRolePoliciesRequestListRolePoliciesPaginateTypeDef(BaseValidatorModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoleTagsRequestListRoleTagsPaginateTypeDef(BaseValidatorModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRolesRequestListRolesPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSAMLProviderTagsRequestListSAMLProviderTagsPaginateTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSSHPublicKeysRequestListSSHPublicKeysPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServerCertificateTagsRequestListServerCertificateTagsPaginateTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServerCertificatesRequestListServerCertificatesPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSigningCertificatesRequestListSigningCertificatesPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserPoliciesRequestListUserPoliciesPaginateTypeDef(BaseValidatorModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserTagsRequestListUserTagsPaginateTypeDef(BaseValidatorModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualMFADevicesRequestListVirtualMFADevicesPaginateTypeDef(BaseValidatorModel):
    AssignmentStatus: Optional[assignmentStatusTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SimulateCustomPolicyRequestSimulateCustomPolicyPaginateTypeDef(BaseValidatorModel):
    PolicyInputList: Sequence[str]
    ActionNames: Sequence[str]
    PermissionsBoundaryPolicyInputList: Optional[Sequence[str]] = None
    ResourceArns: Optional[Sequence[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[Sequence[ContextEntryTypeDef]] = None
    ResourceHandlingOption: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SimulatePrincipalPolicyRequestSimulatePrincipalPolicyPaginateTypeDef(BaseValidatorModel):
    PolicySourceArn: str
    ActionNames: Sequence[str]
    PolicyInputList: Optional[Sequence[str]] = None
    PermissionsBoundaryPolicyInputList: Optional[Sequence[str]] = None
    ResourceArns: Optional[Sequence[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[Sequence[ContextEntryTypeDef]] = None
    ResourceHandlingOption: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAccountPasswordPolicyResponseTypeDef(BaseValidatorModel):
    PasswordPolicy: PasswordPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceProfileRequestInstanceProfileExistsWaitTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetPolicyRequestPolicyExistsWaitTypeDef(BaseValidatorModel):
    PolicyArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRoleRequestRoleExistsWaitTypeDef(BaseValidatorModel):
    RoleName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetUserRequestUserExistsWaitTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetSSHPublicKeyResponseTypeDef(BaseValidatorModel):
    SSHPublicKey: SSHPublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UploadSSHPublicKeyResponseTypeDef(BaseValidatorModel):
    SSHPublicKey: SSHPublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesForPolicyResponseTypeDef(BaseValidatorModel):
    PolicyGroups: List[PolicyGroupTypeDef]
    PolicyUsers: List[PolicyUserTypeDef]
    PolicyRoles: List[PolicyRoleTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMFADevicesResponseTypeDef(BaseValidatorModel):
    MFADevices: List[MFADeviceTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOpenIDConnectProvidersResponseTypeDef(BaseValidatorModel):
    OpenIDConnectProviderList: List[OpenIDConnectProviderListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesGrantingServiceAccessEntryTypeDef(BaseValidatorModel):
    ServiceNamespace: Optional[str] = None
    Policies: Optional[List[PolicyGrantingServiceAccessTypeDef]] = None

class ListSAMLProvidersResponseTypeDef(BaseValidatorModel):
    SAMLProviderList: List[SAMLProviderListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSSHPublicKeysResponseTypeDef(BaseValidatorModel):
    SSHPublicKeys: List[SSHPublicKeyMetadataTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServerCertificatesResponseTypeDef(BaseValidatorModel):
    ServerCertificateMetadataList: List[ServerCertificateMetadataTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ServerCertificateTypeDef(BaseValidatorModel):
    ServerCertificateMetadata: ServerCertificateMetadataTypeDef
    CertificateBody: str
    CertificateChain: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class UploadServerCertificateResponseTypeDef(BaseValidatorModel):
    ServerCertificateMetadata: ServerCertificateMetadataTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceSpecificCredentialsResponseTypeDef(BaseValidatorModel):
    ServiceSpecificCredentials: List[ServiceSpecificCredentialMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSigningCertificatesResponseTypeDef(BaseValidatorModel):
    Certificates: List[SigningCertificateTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UploadSigningCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: SigningCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyDocumentDictTypeDef(BaseValidatorModel):
    Version: str
    Statement: List[PolicyDocumentStatementTypeDef]

class StatementTypeDef(BaseValidatorModel):
    SourcePolicyId: Optional[str] = None
    SourcePolicyType: Optional[PolicySourceTypeType] = None
    StartPosition: Optional[PositionTypeDef] = None
    EndPosition: Optional[PositionTypeDef] = None

class ServiceLastAccessedTypeDef(BaseValidatorModel):
    ServiceName: str
    ServiceNamespace: str
    LastAuthenticated: Optional[datetime] = None
    LastAuthenticatedEntity: Optional[str] = None
    LastAuthenticatedRegion: Optional[str] = None
    TotalAuthenticatedEntities: Optional[int] = None
    TrackedActionsLastAccessed: Optional[List[TrackedActionLastAccessedTypeDef]] = None

class CreatePolicyResponseTypeDef(BaseValidatorModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyResponseTypeDef(BaseValidatorModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesResponseTypeDef(BaseValidatorModel):
    Policies: List[PolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    Users: List[UserTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualMFADeviceTypeDef(BaseValidatorModel):
    SerialNumber: str
    Base32StringSeed: Optional[bytes] = None
    QRCodePNG: Optional[bytes] = None
    User: Optional[UserTypeDef] = None
    EnableDate: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class GetServiceLinkedRoleDeletionStatusResponseTypeDef(BaseValidatorModel):
    Status: DeletionTaskStatusTypeType
    Reason: DeletionTaskFailureReasonTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef(BaseValidatorModel):
    JobStatus: jobStatusTypeType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    EntityDetailsList: List[EntityDetailsTypeDef]
    IsTruncated: bool
    Marker: str
    Error: ErrorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesGrantingServiceAccessResponseTypeDef(BaseValidatorModel):
    PoliciesGrantingServiceAccess: List[ListPoliciesGrantingServiceAccessEntryTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerCertificateResponseTypeDef(BaseValidatorModel):
    ServerCertificate: ServerCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceSpecificResultTypeDef(BaseValidatorModel):
    EvalResourceName: str
    EvalResourceDecision: PolicyEvaluationDecisionTypeType
    MatchedStatements: Optional[List[StatementTypeDef]] = None
    MissingContextValues: Optional[List[str]] = None
    EvalDecisionDetails: Optional[Dict[str, PolicyEvaluationDecisionTypeType]] = None
    PermissionsBoundaryDecisionDetail: Optional[PermissionsBoundaryDecisionDetailTypeDef] = None

class GetServiceLastAccessedDetailsResponseTypeDef(BaseValidatorModel):
    JobStatus: jobStatusTypeType
    JobType: AccessAdvisorUsageGranularityTypeType
    JobCreationDate: datetime
    ServicesLastAccessed: List[ServiceLastAccessedTypeDef]
    JobCompletionDate: datetime
    IsTruncated: bool
    Marker: str
    Error: ErrorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualMFADeviceResponseTypeDef(BaseValidatorModel):
    VirtualMFADevice: VirtualMFADeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualMFADevicesResponseTypeDef(BaseValidatorModel):
    VirtualMFADevices: List[VirtualMFADeviceTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupPolicyResponseTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyName: str
    PolicyDocument: PolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRolePolicyResponseTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyName: str
    PolicyDocument: PolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserPolicyResponseTypeDef(BaseValidatorModel):
    UserName: str
    PolicyName: str
    PolicyDocument: PolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyDetailTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyDocument: Optional[PolicyDocumentTypeDef] = None

class PolicyVersionTypeDef(BaseValidatorModel):
    Document: Optional[PolicyDocumentTypeDef] = None
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    CreateDate: Optional[datetime] = None

class RoleTypeDef(BaseValidatorModel):
    Path: str
    RoleName: str
    RoleId: str
    Arn: str
    CreateDate: datetime
    AssumeRolePolicyDocument: Optional[PolicyDocumentTypeDef] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundaryTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    RoleLastUsed: Optional[RoleLastUsedTypeDef] = None

class EvaluationResultTypeDef(BaseValidatorModel):
    EvalActionName: str
    EvalDecision: PolicyEvaluationDecisionTypeType
    EvalResourceName: Optional[str] = None
    MatchedStatements: Optional[List[StatementTypeDef]] = None
    MissingContextValues: Optional[List[str]] = None
    OrganizationsDecisionDetail: Optional[OrganizationsDecisionDetailTypeDef] = None
    PermissionsBoundaryDecisionDetail: Optional[PermissionsBoundaryDecisionDetailTypeDef] = None
    EvalDecisionDetails: Optional[Dict[str, PolicyEvaluationDecisionTypeType]] = None
    ResourceSpecificResults: Optional[List[ResourceSpecificResultTypeDef]] = None

class GroupDetailTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    Arn: Optional[str] = None
    CreateDate: Optional[datetime] = None
    GroupPolicyList: Optional[List[PolicyDetailTypeDef]] = None
    AttachedManagedPolicies: Optional[List[AttachedPolicyTypeDef]] = None

class UserDetailTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    UserName: Optional[str] = None
    UserId: Optional[str] = None
    Arn: Optional[str] = None
    CreateDate: Optional[datetime] = None
    UserPolicyList: Optional[List[PolicyDetailTypeDef]] = None
    GroupList: Optional[List[str]] = None
    AttachedManagedPolicies: Optional[List[AttachedPolicyTypeDef]] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundaryTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreatePolicyVersionResponseTypeDef(BaseValidatorModel):
    PolicyVersion: PolicyVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyVersionResponseTypeDef(BaseValidatorModel):
    PolicyVersion: PolicyVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[PolicyVersionTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedPolicyDetailTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyId: Optional[str] = None
    Arn: Optional[str] = None
    Path: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    AttachmentCount: Optional[int] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    IsAttachable: Optional[bool] = None
    Description: Optional[str] = None
    CreateDate: Optional[datetime] = None
    UpdateDate: Optional[datetime] = None
    PolicyVersionList: Optional[List[PolicyVersionTypeDef]] = None

class CreateRoleResponseTypeDef(BaseValidatorModel):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceLinkedRoleResponseTypeDef(BaseValidatorModel):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoleResponseTypeDef(BaseValidatorModel):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceProfileTypeDef(BaseValidatorModel):
    Path: str
    InstanceProfileName: str
    InstanceProfileId: str
    Arn: str
    CreateDate: datetime
    Roles: List[RoleTypeDef]
    Tags: Optional[List[TagTypeDef]] = None

class ListRolesResponseTypeDef(BaseValidatorModel):
    Roles: List[RoleTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoleDescriptionResponseTypeDef(BaseValidatorModel):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SimulatePolicyResponseTypeDef(BaseValidatorModel):
    EvaluationResults: List[EvaluationResultTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileResponseTypeDef(BaseValidatorModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceProfileResponseTypeDef(BaseValidatorModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfilesForRoleResponseTypeDef(BaseValidatorModel):
    InstanceProfiles: List[InstanceProfileTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfilesResponseTypeDef(BaseValidatorModel):
    InstanceProfiles: List[InstanceProfileTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RoleDetailTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    RoleName: Optional[str] = None
    RoleId: Optional[str] = None
    Arn: Optional[str] = None
    CreateDate: Optional[datetime] = None
    AssumeRolePolicyDocument: Optional[PolicyDocumentTypeDef] = None
    InstanceProfileList: Optional[List[InstanceProfileTypeDef]] = None
    RolePolicyList: Optional[List[PolicyDetailTypeDef]] = None
    AttachedManagedPolicies: Optional[List[AttachedPolicyTypeDef]] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundaryTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    RoleLastUsed: Optional[RoleLastUsedTypeDef] = None

class GetAccountAuthorizationDetailsResponseTypeDef(BaseValidatorModel):
    UserDetailList: List[UserDetailTypeDef]
    GroupDetailList: List[GroupDetailTypeDef]
    RoleDetailList: List[RoleDetailTypeDef]
    Policies: List[ManagedPolicyDetailTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


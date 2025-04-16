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
from aws_resource_validator.pydantic_models.iam_constants import *

class AccessKeyMetadata(BaseValidatorModel):
    UserName: Optional[str] = None
    AccessKeyId: Optional[str] = None
    Status: Optional[StatusTypeType] = None
    CreateDate: Optional[datetime] = None


class AccessKey(BaseValidatorModel):
    UserName: str
    AccessKeyId: str
    Status: StatusTypeType
    SecretAccessKey: str
    CreateDate: Optional[datetime] = None


class AddClientIDToOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ClientID: str


class AddRoleToInstanceProfileRequestInstanceProfileAddRole(BaseValidatorModel):
    RoleName: str


class AddRoleToInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    RoleName: str


class AddUserToGroupRequestGroupAddUser(BaseValidatorModel):
    UserName: str


class AddUserToGroupRequest(BaseValidatorModel):
    GroupName: str
    UserName: str


class AddUserToGroupRequestUserAddGroup(BaseValidatorModel):
    GroupName: str


class AttachGroupPolicyRequestGroupAttachPolicy(BaseValidatorModel):
    PolicyArn: str


class AttachGroupPolicyRequestPolicyAttachGroup(BaseValidatorModel):
    GroupName: str


class AttachGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyArn: str


class AttachRolePolicyRequestPolicyAttachRole(BaseValidatorModel):
    RoleName: str


class AttachRolePolicyRequestRoleAttachPolicy(BaseValidatorModel):
    PolicyArn: str


class AttachRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyArn: str


class AttachUserPolicyRequestPolicyAttachUser(BaseValidatorModel):
    UserName: str


class AttachUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyArn: str


class AttachUserPolicyRequestUserAttachPolicy(BaseValidatorModel):
    PolicyArn: str


class AttachedPermissionsBoundary(BaseValidatorModel):
    PermissionsBoundaryType: Optional[Literal["PermissionsBoundaryPolicy"]] = None
    PermissionsBoundaryArn: Optional[str] = None


class AttachedPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyArn: Optional[str] = None


class ChangePasswordRequestServiceResourceChangePassword(BaseValidatorModel):
    OldPassword: str
    NewPassword: str


class ChangePasswordRequest(BaseValidatorModel):
    OldPassword: str
    NewPassword: str


class ContextEntry(BaseValidatorModel):
    ContextKeyName: Optional[str] = None
    ContextKeyValues: Optional[Sequence[str]] = None
    ContextKeyType: Optional[ContextKeyTypeEnumType] = None


class CreateAccessKeyRequest(BaseValidatorModel):
    UserName: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateAccountAliasRequestServiceResourceCreateAccountAlias(BaseValidatorModel):
    AccountAlias: str


class CreateAccountAliasRequest(BaseValidatorModel):
    AccountAlias: str


class CreateGroupRequestGroupCreate(BaseValidatorModel):
    Path: Optional[str] = None


class CreateGroupRequestServiceResourceCreateGroup(BaseValidatorModel):
    GroupName: str
    Path: Optional[str] = None


class CreateGroupRequest(BaseValidatorModel):
    GroupName: str
    Path: Optional[str] = None


class Group(BaseValidatorModel):
    Path: str
    GroupName: str
    GroupId: str
    Arn: str
    CreateDate: datetime


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CreateLoginProfileRequestLoginProfileCreate(BaseValidatorModel):
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class CreateLoginProfileRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class CreateLoginProfileRequestUserCreateLoginProfile(BaseValidatorModel):
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class LoginProfile(BaseValidatorModel):
    UserName: str
    CreateDate: datetime
    PasswordResetRequired: Optional[bool] = None


class CreatePolicyVersionRequestPolicyCreateVersion(BaseValidatorModel):
    PolicyDocument: str
    SetAsDefault: Optional[bool] = None


class CreatePolicyVersionRequest(BaseValidatorModel):
    PolicyArn: str
    PolicyDocument: str
    SetAsDefault: Optional[bool] = None


class CreateServiceLinkedRoleRequest(BaseValidatorModel):
    AWSServiceName: str
    Description: Optional[str] = None
    CustomSuffix: Optional[str] = None


class DeactivateMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str
    UserName: Optional[str] = None


class DeleteAccessKeyRequest(BaseValidatorModel):
    AccessKeyId: str
    UserName: Optional[str] = None


class DeleteAccountAliasRequest(BaseValidatorModel):
    AccountAlias: str


class DeleteGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyName: str


class DeleteGroupRequest(BaseValidatorModel):
    GroupName: str


class DeleteInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str


class DeleteLoginProfileRequest(BaseValidatorModel):
    UserName: Optional[str] = None


class DeleteOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str


class DeletePolicyRequest(BaseValidatorModel):
    PolicyArn: str


class DeletePolicyVersionRequest(BaseValidatorModel):
    PolicyArn: str
    VersionId: str


class DeleteRolePermissionsBoundaryRequest(BaseValidatorModel):
    RoleName: str


class DeleteRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyName: str


class DeleteRoleRequest(BaseValidatorModel):
    RoleName: str


class DeleteSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str


class DeleteSSHPublicKeyRequest(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str


class DeleteServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str


class DeleteServiceLinkedRoleRequest(BaseValidatorModel):
    RoleName: str


class DeleteServiceSpecificCredentialRequest(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None


class DeleteSigningCertificateRequest(BaseValidatorModel):
    CertificateId: str
    UserName: Optional[str] = None


class DeleteUserPermissionsBoundaryRequest(BaseValidatorModel):
    UserName: str


class DeleteUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyName: str


class DeleteUserRequest(BaseValidatorModel):
    UserName: str


class DeleteVirtualMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str


class RoleUsageType(BaseValidatorModel):
    Region: Optional[str] = None
    Resources: Optional[List[str]] = None


class DetachGroupPolicyRequestGroupDetachPolicy(BaseValidatorModel):
    PolicyArn: str


class DetachGroupPolicyRequestPolicyDetachGroup(BaseValidatorModel):
    GroupName: str


class DetachGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyArn: str


class DetachRolePolicyRequestPolicyDetachRole(BaseValidatorModel):
    RoleName: str


class DetachRolePolicyRequestRoleDetachPolicy(BaseValidatorModel):
    PolicyArn: str


class DetachRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyArn: str


class DetachUserPolicyRequestPolicyDetachUser(BaseValidatorModel):
    UserName: str


class DetachUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyArn: str


class DetachUserPolicyRequestUserDetachPolicy(BaseValidatorModel):
    PolicyArn: str


class EnableMFADeviceRequestMfaDeviceAssociate(BaseValidatorModel):
    AuthenticationCode1: str
    AuthenticationCode2: str


class EnableMFADeviceRequest(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str


class EnableMFADeviceRequestUserEnableMfa(BaseValidatorModel):
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str


class ErrorDetails(BaseValidatorModel):
    Message: str
    Code: str


class OrganizationsDecisionDetail(BaseValidatorModel):
    AllowedByOrganizations: Optional[bool] = None


class PermissionsBoundaryDecisionDetail(BaseValidatorModel):
    AllowedByPermissionsBoundary: Optional[bool] = None


class GenerateOrganizationsAccessReportRequest(BaseValidatorModel):
    EntityPath: str
    OrganizationsPolicyId: Optional[str] = None


class GenerateServiceLastAccessedDetailsRequest(BaseValidatorModel):
    Arn: str
    Granularity: Optional[AccessAdvisorUsageGranularityTypeType] = None


class GetAccessKeyLastUsedRequest(BaseValidatorModel):
    AccessKeyId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetAccountAuthorizationDetailsRequest(BaseValidatorModel):
    Filter: Optional[Sequence[EntityTypeType]] = None
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


class PasswordPolicy(BaseValidatorModel):
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


class GetContextKeysForCustomPolicyRequest(BaseValidatorModel):
    PolicyInputList: Sequence[str]


class GetContextKeysForPrincipalPolicyRequest(BaseValidatorModel):
    PolicySourceArn: str
    PolicyInputList: Optional[Sequence[str]] = None


class GetGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyName: str


class GetGroupRequest(BaseValidatorModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class GetInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetLoginProfileRequest(BaseValidatorModel):
    UserName: Optional[str] = None


class GetMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str
    UserName: Optional[str] = None


class GetOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str


class GetOrganizationsAccessReportRequest(BaseValidatorModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    SortKey: Optional[SortKeyTypeType] = None


class GetPolicyRequest(BaseValidatorModel):
    PolicyArn: str


class GetPolicyVersionRequest(BaseValidatorModel):
    PolicyArn: str
    VersionId: str


class GetRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyName: str


class GetRoleRequest(BaseValidatorModel):
    RoleName: str


class GetSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str


class SAMLPrivateKey(BaseValidatorModel):
    KeyId: Optional[str] = None
    Timestamp: Optional[datetime] = None


class GetSSHPublicKeyRequest(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Encoding: EncodingTypeType


class SSHPublicKey(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Fingerprint: str
    SSHPublicKeyBody: str
    Status: StatusTypeType
    UploadDate: Optional[datetime] = None


class GetServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str


class GetServiceLastAccessedDetailsRequest(BaseValidatorModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


class GetServiceLastAccessedDetailsWithEntitiesRequest(BaseValidatorModel):
    JobId: str
    ServiceNamespace: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


class GetServiceLinkedRoleDeletionStatusRequest(BaseValidatorModel):
    DeletionTaskId: str


class GetUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyName: str


class GetUserRequest(BaseValidatorModel):
    UserName: Optional[str] = None


class ListAccessKeysRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListAccountAliasesRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListAttachedGroupPoliciesRequest(BaseValidatorModel):
    GroupName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListAttachedRolePoliciesRequest(BaseValidatorModel):
    RoleName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListAttachedUserPoliciesRequest(BaseValidatorModel):
    UserName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListEntitiesForPolicyRequest(BaseValidatorModel):
    PolicyArn: str
    EntityFilter: Optional[EntityTypeType] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class PolicyGroup(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None


class PolicyRole(BaseValidatorModel):
    RoleName: Optional[str] = None
    RoleId: Optional[str] = None


class PolicyUser(BaseValidatorModel):
    UserName: Optional[str] = None
    UserId: Optional[str] = None


class ListGroupPoliciesRequest(BaseValidatorModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListGroupsForUserRequest(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListGroupsRequest(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListInstanceProfileTagsRequest(BaseValidatorModel):
    InstanceProfileName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListInstanceProfilesForRoleRequest(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListInstanceProfilesRequest(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListMFADeviceTagsRequest(BaseValidatorModel):
    SerialNumber: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListMFADevicesRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class MFADevice(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    EnableDate: datetime


class ListOpenIDConnectProviderTagsRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class OpenIDConnectProviderListEntry(BaseValidatorModel):
    Arn: Optional[str] = None


class PolicyGrantingServiceAccess(BaseValidatorModel):
    PolicyName: str
    PolicyType: PolicyTypeType
    PolicyArn: Optional[str] = None
    EntityType: Optional[PolicyOwnerEntityTypeType] = None
    EntityName: Optional[str] = None


class ListPoliciesGrantingServiceAccessRequest(BaseValidatorModel):
    Arn: str
    ServiceNamespaces: Sequence[str]
    Marker: Optional[str] = None


class ListPoliciesRequest(BaseValidatorModel):
    Scope: Optional[PolicyScopeTypeType] = None
    OnlyAttached: Optional[bool] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListPolicyTagsRequest(BaseValidatorModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListPolicyVersionsRequest(BaseValidatorModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListRolePoliciesRequest(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListRoleTagsRequest(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListRolesRequest(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListSAMLProviderTagsRequest(BaseValidatorModel):
    SAMLProviderArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class SAMLProviderListEntry(BaseValidatorModel):
    Arn: Optional[str] = None
    ValidUntil: Optional[datetime] = None
    CreateDate: Optional[datetime] = None


class ListSSHPublicKeysRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class SSHPublicKeyMetadata(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Status: StatusTypeType
    UploadDate: datetime


class ListServerCertificateTagsRequest(BaseValidatorModel):
    ServerCertificateName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListServerCertificatesRequest(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ServerCertificateMetadata(BaseValidatorModel):
    Path: str
    ServerCertificateName: str
    ServerCertificateId: str
    Arn: str
    UploadDate: Optional[datetime] = None
    Expiration: Optional[datetime] = None


class ListSigningCertificatesRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class SigningCertificate(BaseValidatorModel):
    UserName: str
    CertificateId: str
    CertificateBody: str
    Status: StatusTypeType
    UploadDate: Optional[datetime] = None


class ListUserPoliciesRequest(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListUserTagsRequest(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListUsersRequest(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListVirtualMFADevicesRequest(BaseValidatorModel):
    AssignmentStatus: Optional[AssignmentStatusTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class PolicyDocumentStatement(BaseValidatorModel):
    Effect: str
    Resource: str | List[str]
    Sid: str
    Action: str | List[str]


class Position(BaseValidatorModel):
    Line: Optional[int] = None
    Column: Optional[int] = None


class PutGroupPolicyRequestGroupCreatePolicy(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str


class PutGroupPolicyRequestGroupPolicyPut(BaseValidatorModel):
    PolicyDocument: str


class PutGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyName: str
    PolicyDocument: str


class PutRolePermissionsBoundaryRequest(BaseValidatorModel):
    RoleName: str
    PermissionsBoundary: str


class PutRolePolicyRequestRolePolicyPut(BaseValidatorModel):
    PolicyDocument: str


class PutRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyName: str
    PolicyDocument: str


class PutUserPermissionsBoundaryRequest(BaseValidatorModel):
    UserName: str
    PermissionsBoundary: str


class PutUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyName: str
    PolicyDocument: str


class PutUserPolicyRequestUserCreatePolicy(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str


class PutUserPolicyRequestUserPolicyPut(BaseValidatorModel):
    PolicyDocument: str


class RemoveClientIDFromOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ClientID: str


class RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRole(BaseValidatorModel):
    RoleName: str


class RemoveRoleFromInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    RoleName: str


class RemoveUserFromGroupRequestGroupRemoveUser(BaseValidatorModel):
    UserName: str


class RemoveUserFromGroupRequest(BaseValidatorModel):
    GroupName: str
    UserName: str


class RemoveUserFromGroupRequestUserRemoveGroup(BaseValidatorModel):
    GroupName: str


class ResetServiceSpecificCredentialRequest(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None


class ResyncMFADeviceRequestMfaDeviceResync(BaseValidatorModel):
    AuthenticationCode1: str
    AuthenticationCode2: str


class ResyncMFADeviceRequest(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str


class RoleLastUsed(BaseValidatorModel):
    LastUsedDate: Optional[datetime] = None
    Region: Optional[str] = None


class TrackedActionLastAccessed(BaseValidatorModel):
    ActionName: Optional[str] = None
    LastAccessedEntity: Optional[str] = None
    LastAccessedTime: Optional[datetime] = None
    LastAccessedRegion: Optional[str] = None


class SetDefaultPolicyVersionRequest(BaseValidatorModel):
    PolicyArn: str
    VersionId: str


class SetSecurityTokenServicePreferencesRequest(BaseValidatorModel):
    GlobalEndpointTokenVersion: GlobalEndpointTokenVersionType


class UntagInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    TagKeys: Sequence[str]


class UntagMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str
    TagKeys: Sequence[str]


class UntagOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    TagKeys: Sequence[str]


class UntagPolicyRequest(BaseValidatorModel):
    PolicyArn: str
    TagKeys: Sequence[str]


class UntagRoleRequest(BaseValidatorModel):
    RoleName: str
    TagKeys: Sequence[str]


class UntagSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str
    TagKeys: Sequence[str]


class UntagServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str
    TagKeys: Sequence[str]


class UntagUserRequest(BaseValidatorModel):
    UserName: str
    TagKeys: Sequence[str]


class UpdateAccessKeyRequestAccessKeyActivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestAccessKeyDeactivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestAccessKeyPairActivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestAccessKeyPairDeactivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequest(BaseValidatorModel):
    AccessKeyId: str
    Status: StatusTypeType
    UserName: Optional[str] = None


class UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdate(BaseValidatorModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None


class UpdateAccountPasswordPolicyRequest(BaseValidatorModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None


class UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdate(BaseValidatorModel):
    PolicyDocument: str


class UpdateAssumeRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyDocument: str


class UpdateGroupRequestGroupUpdate(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None


class UpdateGroupRequest(BaseValidatorModel):
    GroupName: str
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None


class UpdateLoginProfileRequestLoginProfileUpdate(BaseValidatorModel):
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class UpdateLoginProfileRequest(BaseValidatorModel):
    UserName: str
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class UpdateOpenIDConnectProviderThumbprintRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ThumbprintList: Sequence[str]


class UpdateRoleDescriptionRequest(BaseValidatorModel):
    RoleName: str
    Description: str


class UpdateRoleRequest(BaseValidatorModel):
    RoleName: str
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None


class UpdateSAMLProviderRequestSamlProviderUpdate(BaseValidatorModel):
    SAMLMetadataDocument: Optional[str] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None
    RemovePrivateKey: Optional[str] = None


class UpdateSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str
    SAMLMetadataDocument: Optional[str] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None
    RemovePrivateKey: Optional[str] = None


class UpdateSSHPublicKeyRequest(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Status: StatusTypeType


class UpdateServerCertificateRequestServerCertificateUpdate(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None


class UpdateServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None


class UpdateServiceSpecificCredentialRequest(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    Status: StatusTypeType
    UserName: Optional[str] = None


class UpdateSigningCertificateRequestSigningCertificateActivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateSigningCertificateRequestSigningCertificateDeactivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateSigningCertificateRequest(BaseValidatorModel):
    CertificateId: str
    Status: StatusTypeType
    UserName: Optional[str] = None


class UpdateUserRequest(BaseValidatorModel):
    UserName: str
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None


class UpdateUserRequestUserUpdate(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None


class UploadSSHPublicKeyRequest(BaseValidatorModel):
    UserName: str
    SSHPublicKeyBody: str


class UploadSigningCertificateRequestServiceResourceCreateSigningCertificate(BaseValidatorModel):
    CertificateBody: str
    UserName: Optional[str] = None


class UploadSigningCertificateRequest(BaseValidatorModel):
    CertificateBody: str
    UserName: Optional[str] = None


class SimulateCustomPolicyRequest(BaseValidatorModel):
    PolicyInputList: Sequence[str]
    ActionNames: Sequence[str]
    PermissionsBoundaryPolicyInputList: Optional[Sequence[str]] = None
    ResourceArns: Optional[Sequence[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[Sequence[ContextEntry]] = None
    ResourceHandlingOption: Optional[str] = None
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


class SimulatePrincipalPolicyRequest(BaseValidatorModel):
    PolicySourceArn: str
    ActionNames: Sequence[str]
    PolicyInputList: Optional[Sequence[str]] = None
    PermissionsBoundaryPolicyInputList: Optional[Sequence[str]] = None
    ResourceArns: Optional[Sequence[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[Sequence[ContextEntry]] = None
    ResourceHandlingOption: Optional[str] = None
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


class CreateAccessKeyResponse(BaseValidatorModel):
    AccessKey: AccessKey
    ResponseMetadata: ResponseMetadata


class DeleteServiceLinkedRoleResponse(BaseValidatorModel):
    DeletionTaskId: str
    ResponseMetadata: ResponseMetadata


class DisableOrganizationsRootCredentialsManagementResponse(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadata


class DisableOrganizationsRootSessionsResponse(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class EnableOrganizationsRootCredentialsManagementResponse(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadata


class EnableOrganizationsRootSessionsResponse(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadata


class GenerateCredentialReportResponse(BaseValidatorModel):
    State: ReportStateTypeType
    Description: str
    ResponseMetadata: ResponseMetadata


class GenerateOrganizationsAccessReportResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class GenerateServiceLastAccessedDetailsResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class AccessKeyLastUsed(BaseValidatorModel):
    pass


class GetAccessKeyLastUsedResponse(BaseValidatorModel):
    UserName: str
    AccessKeyLastUsed: AccessKeyLastUsed
    ResponseMetadata: ResponseMetadata


class GetAccountSummaryResponse(BaseValidatorModel):
    SummaryMap: Dict[SummaryKeyTypeType, int]
    ResponseMetadata: ResponseMetadata


class GetContextKeysForPolicyResponse(BaseValidatorModel):
    ContextKeyNames: List[str]
    ResponseMetadata: ResponseMetadata


class GetCredentialReportResponse(BaseValidatorModel):
    Content: bytes
    ReportFormat: Literal["text/csv"]
    GeneratedTime: datetime
    ResponseMetadata: ResponseMetadata


class GetMFADeviceResponse(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    EnableDate: datetime
    Certifications: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListAccessKeysResponse(BaseValidatorModel):
    AccessKeyMetadata: List[AccessKeyMetadata]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListAccountAliasesResponse(BaseValidatorModel):
    AccountAliases: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListAttachedGroupPoliciesResponse(BaseValidatorModel):
    AttachedPolicies: List[AttachedPolicy]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListAttachedRolePoliciesResponse(BaseValidatorModel):
    AttachedPolicies: List[AttachedPolicy]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListAttachedUserPoliciesResponse(BaseValidatorModel):
    AttachedPolicies: List[AttachedPolicy]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListGroupPoliciesResponse(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListOrganizationsFeaturesResponse(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadata


class ListRolePoliciesResponse(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListUserPoliciesResponse(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class UpdateSAMLProviderResponse(BaseValidatorModel):
    SAMLProviderArn: str
    ResponseMetadata: ResponseMetadata


class CreateGroupResponse(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


class ListGroupsForUserResponse(BaseValidatorModel):
    Groups: List[Group]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListGroupsResponse(BaseValidatorModel):
    Groups: List[Group]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class CreateInstanceProfileRequestServiceResourceCreateInstanceProfile(BaseValidatorModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateOpenIDConnectProviderRequest(BaseValidatorModel):
    Url: str
    ClientIDList: Optional[Sequence[str]] = None
    ThumbprintList: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateOpenIDConnectProviderResponse(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreatePolicyRequestServiceResourceCreatePolicy(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreatePolicyRequest(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateRoleRequestServiceResourceCreateRole(BaseValidatorModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateRoleRequest(BaseValidatorModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateSAMLProviderRequestServiceResourceCreateSamlProvider(BaseValidatorModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[Sequence[Tag]] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None


class CreateSAMLProviderRequest(BaseValidatorModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[Sequence[Tag]] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None


class CreateSAMLProviderResponse(BaseValidatorModel):
    SAMLProviderArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateUserRequestServiceResourceCreateUser(BaseValidatorModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateUserRequest(BaseValidatorModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateUserRequestUserCreate(BaseValidatorModel):
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDevice(BaseValidatorModel):
    VirtualMFADeviceName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateVirtualMFADeviceRequest(BaseValidatorModel):
    VirtualMFADeviceName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class GetOpenIDConnectProviderResponse(BaseValidatorModel):
    Url: str
    ClientIDList: List[str]
    ThumbprintList: List[str]
    CreateDate: datetime
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ListInstanceProfileTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListMFADeviceTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListOpenIDConnectProviderTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListPolicyTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListRoleTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListSAMLProviderTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListServerCertificateTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListUserTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class Policy(BaseValidatorModel):
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
    Tags: Optional[List[Tag]] = None


class TagInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    Tags: Sequence[Tag]


class TagMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str
    Tags: Sequence[Tag]


class TagOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Tags: Sequence[Tag]


class TagPolicyRequest(BaseValidatorModel):
    PolicyArn: str
    Tags: Sequence[Tag]


class TagRoleRequest(BaseValidatorModel):
    RoleName: str
    Tags: Sequence[Tag]


class TagSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str
    Tags: Sequence[Tag]


class TagServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str
    Tags: Sequence[Tag]


class TagUserRequest(BaseValidatorModel):
    UserName: str
    Tags: Sequence[Tag]


class UploadServerCertificateRequestServiceResourceCreateServerCertificate(BaseValidatorModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class UploadServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class User(BaseValidatorModel):
    Path: str
    UserName: str
    UserId: str
    Arn: str
    CreateDate: datetime
    PasswordLastUsed: Optional[datetime] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundary] = None
    Tags: Optional[List[Tag]] = None


class CreateLoginProfileResponse(BaseValidatorModel):
    LoginProfile: LoginProfile
    ResponseMetadata: ResponseMetadata


class GetLoginProfileResponse(BaseValidatorModel):
    LoginProfile: LoginProfile
    ResponseMetadata: ResponseMetadata


class ServiceSpecificCredential(BaseValidatorModel):
    pass


class CreateServiceSpecificCredentialResponse(BaseValidatorModel):
    ServiceSpecificCredential: ServiceSpecificCredential
    ResponseMetadata: ResponseMetadata


class ResetServiceSpecificCredentialResponse(BaseValidatorModel):
    ServiceSpecificCredential: ServiceSpecificCredential
    ResponseMetadata: ResponseMetadata


class DeletionTaskFailureReasonType(BaseValidatorModel):
    Reason: Optional[str] = None
    RoleUsageList: Optional[List[RoleUsageType]] = None


class EntityInfo(BaseValidatorModel):
    pass


class EntityDetails(BaseValidatorModel):
    EntityInfo: EntityInfo
    LastAuthenticated: Optional[datetime] = None


class AccessDetail(BaseValidatorModel):
    pass


class GetOrganizationsAccessReportResponse(BaseValidatorModel):
    JobStatus: JobStatusTypeType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    NumberOfServicesAccessible: int
    NumberOfServicesNotAccessed: int
    AccessDetails: List[AccessDetail]
    IsTruncated: bool
    Marker: str
    ErrorDetails: ErrorDetails
    ResponseMetadata: ResponseMetadata


class GetAccountAuthorizationDetailsRequestPaginate(BaseValidatorModel):
    Filter: Optional[Sequence[EntityTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetGroupRequestPaginate(BaseValidatorModel):
    GroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccessKeysRequestPaginate(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountAliasesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttachedGroupPoliciesRequestPaginate(BaseValidatorModel):
    GroupName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttachedRolePoliciesRequestPaginate(BaseValidatorModel):
    RoleName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttachedUserPoliciesRequestPaginate(BaseValidatorModel):
    UserName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEntitiesForPolicyRequestPaginate(BaseValidatorModel):
    PolicyArn: str
    EntityFilter: Optional[EntityTypeType] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupPoliciesRequestPaginate(BaseValidatorModel):
    GroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsForUserRequestPaginate(BaseValidatorModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsRequestPaginate(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstanceProfileTagsRequestPaginate(BaseValidatorModel):
    InstanceProfileName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstanceProfilesForRoleRequestPaginate(BaseValidatorModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstanceProfilesRequestPaginate(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMFADeviceTagsRequestPaginate(BaseValidatorModel):
    SerialNumber: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMFADevicesRequestPaginate(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOpenIDConnectProviderTagsRequestPaginate(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPoliciesRequestPaginate(BaseValidatorModel):
    Scope: Optional[PolicyScopeTypeType] = None
    OnlyAttached: Optional[bool] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPolicyTagsRequestPaginate(BaseValidatorModel):
    PolicyArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPolicyVersionsRequestPaginate(BaseValidatorModel):
    PolicyArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRolePoliciesRequestPaginate(BaseValidatorModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRoleTagsRequestPaginate(BaseValidatorModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRolesRequestPaginate(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSAMLProviderTagsRequestPaginate(BaseValidatorModel):
    SAMLProviderArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSSHPublicKeysRequestPaginate(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServerCertificateTagsRequestPaginate(BaseValidatorModel):
    ServerCertificateName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServerCertificatesRequestPaginate(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSigningCertificatesRequestPaginate(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUserPoliciesRequestPaginate(BaseValidatorModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUserTagsRequestPaginate(BaseValidatorModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVirtualMFADevicesRequestPaginate(BaseValidatorModel):
    AssignmentStatus: Optional[AssignmentStatusTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SimulateCustomPolicyRequestPaginate(BaseValidatorModel):
    PolicyInputList: Sequence[str]
    ActionNames: Sequence[str]
    PermissionsBoundaryPolicyInputList: Optional[Sequence[str]] = None
    ResourceArns: Optional[Sequence[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[Sequence[ContextEntry]] = None
    ResourceHandlingOption: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SimulatePrincipalPolicyRequestPaginate(BaseValidatorModel):
    PolicySourceArn: str
    ActionNames: Sequence[str]
    PolicyInputList: Optional[Sequence[str]] = None
    PermissionsBoundaryPolicyInputList: Optional[Sequence[str]] = None
    ResourceArns: Optional[Sequence[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[Sequence[ContextEntry]] = None
    ResourceHandlingOption: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAccountPasswordPolicyResponse(BaseValidatorModel):
    PasswordPolicy: PasswordPolicy
    ResponseMetadata: ResponseMetadata


class GetInstanceProfileRequestWait(BaseValidatorModel):
    InstanceProfileName: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetPolicyRequestWait(BaseValidatorModel):
    PolicyArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetRoleRequestWait(BaseValidatorModel):
    RoleName: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetUserRequestWait(BaseValidatorModel):
    UserName: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetSAMLProviderResponse(BaseValidatorModel):
    SAMLProviderUUID: str
    SAMLMetadataDocument: str
    CreateDate: datetime
    ValidUntil: datetime
    Tags: List[Tag]
    AssertionEncryptionMode: AssertionEncryptionModeTypeType
    PrivateKeyList: List[SAMLPrivateKey]
    ResponseMetadata: ResponseMetadata


class GetSSHPublicKeyResponse(BaseValidatorModel):
    SSHPublicKey: SSHPublicKey
    ResponseMetadata: ResponseMetadata


class UploadSSHPublicKeyResponse(BaseValidatorModel):
    SSHPublicKey: SSHPublicKey
    ResponseMetadata: ResponseMetadata


class ListEntitiesForPolicyResponse(BaseValidatorModel):
    PolicyGroups: List[PolicyGroup]
    PolicyUsers: List[PolicyUser]
    PolicyRoles: List[PolicyRole]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListMFADevicesResponse(BaseValidatorModel):
    MFADevices: List[MFADevice]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListOpenIDConnectProvidersResponse(BaseValidatorModel):
    OpenIDConnectProviderList: List[OpenIDConnectProviderListEntry]
    ResponseMetadata: ResponseMetadata


class ListPoliciesGrantingServiceAccessEntry(BaseValidatorModel):
    ServiceNamespace: Optional[str] = None
    Policies: Optional[List[PolicyGrantingServiceAccess]] = None


class ListSAMLProvidersResponse(BaseValidatorModel):
    SAMLProviderList: List[SAMLProviderListEntry]
    ResponseMetadata: ResponseMetadata


class ListSSHPublicKeysResponse(BaseValidatorModel):
    SSHPublicKeys: List[SSHPublicKeyMetadata]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListServerCertificatesResponse(BaseValidatorModel):
    ServerCertificateMetadataList: List[ServerCertificateMetadata]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ServerCertificate(BaseValidatorModel):
    ServerCertificateMetadata: ServerCertificateMetadata
    CertificateBody: str
    CertificateChain: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UploadServerCertificateResponse(BaseValidatorModel):
    ServerCertificateMetadata: ServerCertificateMetadata
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ServiceSpecificCredentialMetadata(BaseValidatorModel):
    pass


class ListServiceSpecificCredentialsResponse(BaseValidatorModel):
    ServiceSpecificCredentials: List[ServiceSpecificCredentialMetadata]
    ResponseMetadata: ResponseMetadata


class ListSigningCertificatesResponse(BaseValidatorModel):
    Certificates: List[SigningCertificate]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class UploadSigningCertificateResponse(BaseValidatorModel):
    Certificate: SigningCertificate
    ResponseMetadata: ResponseMetadata


class PolicyDocumentDict(BaseValidatorModel):
    Version: str
    Statement: List[PolicyDocumentStatement]


class Statement(BaseValidatorModel):
    SourcePolicyId: Optional[str] = None
    SourcePolicyType: Optional[PolicySourceTypeType] = None
    StartPosition: Optional[Position] = None
    EndPosition: Optional[Position] = None


class CreatePolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


class GetPolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


class ListPoliciesResponse(BaseValidatorModel):
    Policies: List[Policy]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class CreateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class GetGroupResponse(BaseValidatorModel):
    Group: Group
    Users: List[User]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class GetUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class ListUsersResponse(BaseValidatorModel):
    Users: List[User]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class VirtualMFADevice(BaseValidatorModel):
    SerialNumber: str
    Base32StringSeed: Optional[bytes] = None
    QRCodePNG: Optional[bytes] = None
    User: Optional[User] = None
    EnableDate: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class GetServiceLinkedRoleDeletionStatusResponse(BaseValidatorModel):
    Status: DeletionTaskStatusTypeType
    Reason: DeletionTaskFailureReasonType
    ResponseMetadata: ResponseMetadata


class GetServiceLastAccessedDetailsWithEntitiesResponse(BaseValidatorModel):
    JobStatus: JobStatusTypeType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    EntityDetailsList: List[EntityDetails]
    IsTruncated: bool
    Marker: str
    Error: ErrorDetails
    ResponseMetadata: ResponseMetadata


class ListPoliciesGrantingServiceAccessResponse(BaseValidatorModel):
    PoliciesGrantingServiceAccess: List[ListPoliciesGrantingServiceAccessEntry]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class GetServerCertificateResponse(BaseValidatorModel):
    ServerCertificate: ServerCertificate
    ResponseMetadata: ResponseMetadata


class ResourceSpecificResult(BaseValidatorModel):
    EvalResourceName: str
    EvalResourceDecision: PolicyEvaluationDecisionTypeType
    MatchedStatements: Optional[List[Statement]] = None
    MissingContextValues: Optional[List[str]] = None
    EvalDecisionDetails: Optional[Dict[str, PolicyEvaluationDecisionTypeType]] = None
    PermissionsBoundaryDecisionDetail: Optional[PermissionsBoundaryDecisionDetail] = None


class ServiceLastAccessed(BaseValidatorModel):
    pass


class GetServiceLastAccessedDetailsResponse(BaseValidatorModel):
    JobStatus: JobStatusTypeType
    JobType: AccessAdvisorUsageGranularityTypeType
    JobCreationDate: datetime
    ServicesLastAccessed: List[ServiceLastAccessed]
    JobCompletionDate: datetime
    IsTruncated: bool
    Marker: str
    Error: ErrorDetails
    ResponseMetadata: ResponseMetadata


class CreateVirtualMFADeviceResponse(BaseValidatorModel):
    VirtualMFADevice: VirtualMFADevice
    ResponseMetadata: ResponseMetadata


class ListVirtualMFADevicesResponse(BaseValidatorModel):
    VirtualMFADevices: List[VirtualMFADevice]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class PolicyDocument(BaseValidatorModel):
    pass


class GetGroupPolicyResponse(BaseValidatorModel):
    GroupName: str
    PolicyName: str
    PolicyDocument: PolicyDocument
    ResponseMetadata: ResponseMetadata


class GetRolePolicyResponse(BaseValidatorModel):
    RoleName: str
    PolicyName: str
    PolicyDocument: PolicyDocument
    ResponseMetadata: ResponseMetadata


class GetUserPolicyResponse(BaseValidatorModel):
    UserName: str
    PolicyName: str
    PolicyDocument: PolicyDocument
    ResponseMetadata: ResponseMetadata


class PolicyDetail(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyDocument: Optional[PolicyDocument] = None


class PolicyVersion(BaseValidatorModel):
    Document: Optional[PolicyDocument] = None
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    CreateDate: Optional[datetime] = None


class Role(BaseValidatorModel):
    Path: str
    RoleName: str
    RoleId: str
    Arn: str
    CreateDate: datetime
    AssumeRolePolicyDocument: Optional[PolicyDocument] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundary] = None
    Tags: Optional[List[Tag]] = None
    RoleLastUsed: Optional[RoleLastUsed] = None


class EvaluationResult(BaseValidatorModel):
    EvalActionName: str
    EvalDecision: PolicyEvaluationDecisionTypeType
    EvalResourceName: Optional[str] = None
    MatchedStatements: Optional[List[Statement]] = None
    MissingContextValues: Optional[List[str]] = None
    OrganizationsDecisionDetail: Optional[OrganizationsDecisionDetail] = None
    PermissionsBoundaryDecisionDetail: Optional[PermissionsBoundaryDecisionDetail] = None
    EvalDecisionDetails: Optional[Dict[str, PolicyEvaluationDecisionTypeType]] = None
    ResourceSpecificResults: Optional[List[ResourceSpecificResult]] = None


class GroupDetail(BaseValidatorModel):
    Path: Optional[str] = None
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    Arn: Optional[str] = None
    CreateDate: Optional[datetime] = None
    GroupPolicyList: Optional[List[PolicyDetail]] = None
    AttachedManagedPolicies: Optional[List[AttachedPolicy]] = None


class UserDetail(BaseValidatorModel):
    Path: Optional[str] = None
    UserName: Optional[str] = None
    UserId: Optional[str] = None
    Arn: Optional[str] = None
    CreateDate: Optional[datetime] = None
    UserPolicyList: Optional[List[PolicyDetail]] = None
    GroupList: Optional[List[str]] = None
    AttachedManagedPolicies: Optional[List[AttachedPolicy]] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundary] = None
    Tags: Optional[List[Tag]] = None


class CreatePolicyVersionResponse(BaseValidatorModel):
    PolicyVersion: PolicyVersion
    ResponseMetadata: ResponseMetadata


class GetPolicyVersionResponse(BaseValidatorModel):
    PolicyVersion: PolicyVersion
    ResponseMetadata: ResponseMetadata


class ListPolicyVersionsResponse(BaseValidatorModel):
    Versions: List[PolicyVersion]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ManagedPolicyDetail(BaseValidatorModel):
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
    PolicyVersionList: Optional[List[PolicyVersion]] = None


class CreateRoleResponse(BaseValidatorModel):
    Role: Role
    ResponseMetadata: ResponseMetadata


class CreateServiceLinkedRoleResponse(BaseValidatorModel):
    Role: Role
    ResponseMetadata: ResponseMetadata


class GetRoleResponse(BaseValidatorModel):
    Role: Role
    ResponseMetadata: ResponseMetadata


class InstanceProfile(BaseValidatorModel):
    Path: str
    InstanceProfileName: str
    InstanceProfileId: str
    Arn: str
    CreateDate: datetime
    Roles: List[Role]
    Tags: Optional[List[Tag]] = None


class ListRolesResponse(BaseValidatorModel):
    Roles: List[Role]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class UpdateRoleDescriptionResponse(BaseValidatorModel):
    Role: Role
    ResponseMetadata: ResponseMetadata


class SimulatePolicyResponse(BaseValidatorModel):
    EvaluationResults: List[EvaluationResult]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class CreateInstanceProfileResponse(BaseValidatorModel):
    InstanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


class GetInstanceProfileResponse(BaseValidatorModel):
    InstanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


class ListInstanceProfilesForRoleResponse(BaseValidatorModel):
    InstanceProfiles: List[InstanceProfile]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListInstanceProfilesResponse(BaseValidatorModel):
    InstanceProfiles: List[InstanceProfile]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class RoleDetail(BaseValidatorModel):
    Path: Optional[str] = None
    RoleName: Optional[str] = None
    RoleId: Optional[str] = None
    Arn: Optional[str] = None
    CreateDate: Optional[datetime] = None
    AssumeRolePolicyDocument: Optional[PolicyDocument] = None
    InstanceProfileList: Optional[List[InstanceProfile]] = None
    RolePolicyList: Optional[List[PolicyDetail]] = None
    AttachedManagedPolicies: Optional[List[AttachedPolicy]] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundary] = None
    Tags: Optional[List[Tag]] = None
    RoleLastUsed: Optional[RoleLastUsed] = None


class GetAccountAuthorizationDetailsResponse(BaseValidatorModel):
    UserDetailList: List[UserDetail]
    GroupDetailList: List[GroupDetail]
    RoleDetailList: List[RoleDetail]
    Policies: List[ManagedPolicyDetail]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata



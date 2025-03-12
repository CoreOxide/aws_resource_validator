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

class AccessKeyMetadataTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    AccessKeyId: Optional[str] = None
    Status: Optional[StatusTypeType] = None
    CreateDate: Optional[datetime] = None


class AccessKeyTypeDef(BaseValidatorModel):
    UserName: str
    AccessKeyId: str
    Status: StatusTypeType
    SecretAccessKey: str
    CreateDate: Optional[datetime] = None


class AddClientIDToOpenIDConnectProviderRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ClientID: str


class AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef(BaseValidatorModel):
    RoleName: str


class AddRoleToInstanceProfileRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    RoleName: str


class AddUserToGroupRequestGroupAddUserTypeDef(BaseValidatorModel):
    UserName: str


class AddUserToGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserName: str


class AddUserToGroupRequestUserAddGroupTypeDef(BaseValidatorModel):
    GroupName: str


class AttachGroupPolicyRequestGroupAttachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str


class AttachGroupPolicyRequestPolicyAttachGroupTypeDef(BaseValidatorModel):
    GroupName: str


class AttachGroupPolicyRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyArn: str


class AttachRolePolicyRequestPolicyAttachRoleTypeDef(BaseValidatorModel):
    RoleName: str


class AttachRolePolicyRequestRoleAttachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str


class AttachRolePolicyRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyArn: str


class AttachUserPolicyRequestPolicyAttachUserTypeDef(BaseValidatorModel):
    UserName: str


class AttachUserPolicyRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyArn: str


class AttachUserPolicyRequestUserAttachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str


class AttachedPermissionsBoundaryTypeDef(BaseValidatorModel):
    PermissionsBoundaryType: Optional[Literal["PermissionsBoundaryPolicy"]] = None
    PermissionsBoundaryArn: Optional[str] = None


class AttachedPolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyArn: Optional[str] = None


class ChangePasswordRequestServiceResourceChangePasswordTypeDef(BaseValidatorModel):
    OldPassword: str
    NewPassword: str


class ChangePasswordRequestTypeDef(BaseValidatorModel):
    OldPassword: str
    NewPassword: str


class ContextEntryTypeDef(BaseValidatorModel):
    ContextKeyName: Optional[str] = None
    ContextKeyValues: Optional[Sequence[str]] = None
    ContextKeyType: Optional[ContextKeyTypeEnumType] = None


class CreateAccessKeyRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef(BaseValidatorModel):
    AccountAlias: str


class CreateAccountAliasRequestTypeDef(BaseValidatorModel):
    AccountAlias: str


class CreateGroupRequestGroupCreateTypeDef(BaseValidatorModel):
    Path: Optional[str] = None


class CreateGroupRequestServiceResourceCreateGroupTypeDef(BaseValidatorModel):
    GroupName: str
    Path: Optional[str] = None


class CreateGroupRequestTypeDef(BaseValidatorModel):
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
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class CreateLoginProfileRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class CreateLoginProfileRequestUserCreateLoginProfileTypeDef(BaseValidatorModel):
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class LoginProfileTypeDef(BaseValidatorModel):
    UserName: str
    CreateDate: datetime
    PasswordResetRequired: Optional[bool] = None


class CreatePolicyVersionRequestPolicyCreateVersionTypeDef(BaseValidatorModel):
    PolicyDocument: str
    SetAsDefault: Optional[bool] = None


class CreatePolicyVersionRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    PolicyDocument: str
    SetAsDefault: Optional[bool] = None


class CreateServiceLinkedRoleRequestTypeDef(BaseValidatorModel):
    AWSServiceName: str
    Description: Optional[str] = None
    CustomSuffix: Optional[str] = None


class DeactivateMFADeviceRequestTypeDef(BaseValidatorModel):
    SerialNumber: str
    UserName: Optional[str] = None


class DeleteAccessKeyRequestTypeDef(BaseValidatorModel):
    AccessKeyId: str
    UserName: Optional[str] = None


class DeleteAccountAliasRequestTypeDef(BaseValidatorModel):
    AccountAlias: str


class DeleteGroupPolicyRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyName: str


class DeleteGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str


class DeleteInstanceProfileRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str


class DeleteLoginProfileRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None


class DeleteOpenIDConnectProviderRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str


class DeletePolicyRequestTypeDef(BaseValidatorModel):
    PolicyArn: str


class DeletePolicyVersionRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    VersionId: str


class DeleteRolePermissionsBoundaryRequestTypeDef(BaseValidatorModel):
    RoleName: str


class DeleteRolePolicyRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyName: str


class DeleteRoleRequestTypeDef(BaseValidatorModel):
    RoleName: str


class DeleteSAMLProviderRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str


class DeleteSSHPublicKeyRequestTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str


class DeleteServerCertificateRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str


class DeleteServiceLinkedRoleRequestTypeDef(BaseValidatorModel):
    RoleName: str


class DeleteServiceSpecificCredentialRequestTypeDef(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None


class DeleteSigningCertificateRequestTypeDef(BaseValidatorModel):
    CertificateId: str
    UserName: Optional[str] = None


class DeleteUserPermissionsBoundaryRequestTypeDef(BaseValidatorModel):
    UserName: str


class DeleteUserPolicyRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyName: str


class DeleteUserRequestTypeDef(BaseValidatorModel):
    UserName: str


class DeleteVirtualMFADeviceRequestTypeDef(BaseValidatorModel):
    SerialNumber: str


class RoleUsageTypeTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    Resources: Optional[List[str]] = None


class DetachGroupPolicyRequestGroupDetachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str


class DetachGroupPolicyRequestPolicyDetachGroupTypeDef(BaseValidatorModel):
    GroupName: str


class DetachGroupPolicyRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyArn: str


class DetachRolePolicyRequestPolicyDetachRoleTypeDef(BaseValidatorModel):
    RoleName: str


class DetachRolePolicyRequestRoleDetachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str


class DetachRolePolicyRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyArn: str


class DetachUserPolicyRequestPolicyDetachUserTypeDef(BaseValidatorModel):
    UserName: str


class DetachUserPolicyRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyArn: str


class DetachUserPolicyRequestUserDetachPolicyTypeDef(BaseValidatorModel):
    PolicyArn: str


class EnableMFADeviceRequestMfaDeviceAssociateTypeDef(BaseValidatorModel):
    AuthenticationCode1: str
    AuthenticationCode2: str


class EnableMFADeviceRequestTypeDef(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str


class EnableMFADeviceRequestUserEnableMfaTypeDef(BaseValidatorModel):
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str


class ErrorDetailsTypeDef(BaseValidatorModel):
    Message: str
    Code: str


class OrganizationsDecisionDetailTypeDef(BaseValidatorModel):
    AllowedByOrganizations: Optional[bool] = None


class PermissionsBoundaryDecisionDetailTypeDef(BaseValidatorModel):
    AllowedByPermissionsBoundary: Optional[bool] = None


class GenerateOrganizationsAccessReportRequestTypeDef(BaseValidatorModel):
    EntityPath: str
    OrganizationsPolicyId: Optional[str] = None


class GenerateServiceLastAccessedDetailsRequestTypeDef(BaseValidatorModel):
    Arn: str
    Granularity: Optional[AccessAdvisorUsageGranularityTypeType] = None


class GetAccessKeyLastUsedRequestTypeDef(BaseValidatorModel):
    AccessKeyId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetAccountAuthorizationDetailsRequestTypeDef(BaseValidatorModel):
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


class GetContextKeysForCustomPolicyRequestTypeDef(BaseValidatorModel):
    PolicyInputList: Sequence[str]


class GetContextKeysForPrincipalPolicyRequestTypeDef(BaseValidatorModel):
    PolicySourceArn: str
    PolicyInputList: Optional[Sequence[str]] = None


class GetGroupPolicyRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyName: str


class GetGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class GetInstanceProfileRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetLoginProfileRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None


class GetMFADeviceRequestTypeDef(BaseValidatorModel):
    SerialNumber: str
    UserName: Optional[str] = None


class GetOpenIDConnectProviderRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str


class GetOrganizationsAccessReportRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    SortKey: Optional[SortKeyTypeType] = None


class GetPolicyRequestTypeDef(BaseValidatorModel):
    PolicyArn: str


class GetPolicyVersionRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    VersionId: str


class GetRolePolicyRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyName: str


class GetRoleRequestTypeDef(BaseValidatorModel):
    RoleName: str


class GetSAMLProviderRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str


class SAMLPrivateKeyTypeDef(BaseValidatorModel):
    KeyId: Optional[str] = None
    Timestamp: Optional[datetime] = None


class GetSSHPublicKeyRequestTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Encoding: EncodingTypeType


class SSHPublicKeyTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Fingerprint: str
    SSHPublicKeyBody: str
    Status: StatusTypeType
    UploadDate: Optional[datetime] = None


class GetServerCertificateRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str


class GetServiceLastAccessedDetailsRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


class GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef(BaseValidatorModel):
    JobId: str
    ServiceNamespace: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


class GetServiceLinkedRoleDeletionStatusRequestTypeDef(BaseValidatorModel):
    DeletionTaskId: str


class GetUserPolicyRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyName: str


class GetUserRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None


class ListAccessKeysRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListAccountAliasesRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListAttachedGroupPoliciesRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListAttachedRolePoliciesRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListAttachedUserPoliciesRequestTypeDef(BaseValidatorModel):
    UserName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListEntitiesForPolicyRequestTypeDef(BaseValidatorModel):
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


class ListGroupPoliciesRequestTypeDef(BaseValidatorModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListGroupsForUserRequestTypeDef(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListGroupsRequestTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListInstanceProfileTagsRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListInstanceProfilesForRoleRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListInstanceProfilesRequestTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListMFADeviceTagsRequestTypeDef(BaseValidatorModel):
    SerialNumber: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListMFADevicesRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class MFADeviceTypeDef(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    EnableDate: datetime


class ListOpenIDConnectProviderTagsRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class OpenIDConnectProviderListEntryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class PolicyGrantingServiceAccessTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyType: PolicyTypeType
    PolicyArn: Optional[str] = None
    EntityType: Optional[PolicyOwnerEntityTypeType] = None
    EntityName: Optional[str] = None


class ListPoliciesGrantingServiceAccessRequestTypeDef(BaseValidatorModel):
    Arn: str
    ServiceNamespaces: Sequence[str]
    Marker: Optional[str] = None


class ListPoliciesRequestTypeDef(BaseValidatorModel):
    Scope: Optional[PolicyScopeTypeType] = None
    OnlyAttached: Optional[bool] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListPolicyTagsRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListPolicyVersionsRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListRolePoliciesRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListRoleTagsRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListRolesRequestTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListSAMLProviderTagsRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class SAMLProviderListEntryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ValidUntil: Optional[datetime] = None
    CreateDate: Optional[datetime] = None


class ListSSHPublicKeysRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class SSHPublicKeyMetadataTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Status: StatusTypeType
    UploadDate: datetime


class ListServerCertificateTagsRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListServerCertificatesRequestTypeDef(BaseValidatorModel):
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


class ListSigningCertificatesRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class SigningCertificateTypeDef(BaseValidatorModel):
    UserName: str
    CertificateId: str
    CertificateBody: str
    Status: StatusTypeType
    UploadDate: Optional[datetime] = None


class ListUserPoliciesRequestTypeDef(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListUserTagsRequestTypeDef(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListUsersRequestTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListVirtualMFADevicesRequestTypeDef(BaseValidatorModel):
    AssignmentStatus: Optional[AssignmentStatusTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class PolicyDocumentStatementTypeDef(BaseValidatorModel):
    Effect: str
    Resource: str | List[str]
    Sid: str
    Action: str | List[str]


class PositionTypeDef(BaseValidatorModel):
    Line: Optional[int] = None
    Column: Optional[int] = None


class PutGroupPolicyRequestGroupCreatePolicyTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str


class PutGroupPolicyRequestGroupPolicyPutTypeDef(BaseValidatorModel):
    PolicyDocument: str


class PutGroupPolicyRequestTypeDef(BaseValidatorModel):
    GroupName: str
    PolicyName: str
    PolicyDocument: str


class PutRolePermissionsBoundaryRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PermissionsBoundary: str


class PutRolePolicyRequestRolePolicyPutTypeDef(BaseValidatorModel):
    PolicyDocument: str


class PutRolePolicyRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyName: str
    PolicyDocument: str


class PutUserPermissionsBoundaryRequestTypeDef(BaseValidatorModel):
    UserName: str
    PermissionsBoundary: str


class PutUserPolicyRequestTypeDef(BaseValidatorModel):
    UserName: str
    PolicyName: str
    PolicyDocument: str


class PutUserPolicyRequestUserCreatePolicyTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str


class PutUserPolicyRequestUserPolicyPutTypeDef(BaseValidatorModel):
    PolicyDocument: str


class RemoveClientIDFromOpenIDConnectProviderRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ClientID: str


class RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef(BaseValidatorModel):
    RoleName: str


class RemoveRoleFromInstanceProfileRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    RoleName: str


class RemoveUserFromGroupRequestGroupRemoveUserTypeDef(BaseValidatorModel):
    UserName: str


class RemoveUserFromGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserName: str


class RemoveUserFromGroupRequestUserRemoveGroupTypeDef(BaseValidatorModel):
    GroupName: str


class ResetServiceSpecificCredentialRequestTypeDef(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None


class ResyncMFADeviceRequestMfaDeviceResyncTypeDef(BaseValidatorModel):
    AuthenticationCode1: str
    AuthenticationCode2: str


class ResyncMFADeviceRequestTypeDef(BaseValidatorModel):
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


class SetDefaultPolicyVersionRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    VersionId: str


class SetSecurityTokenServicePreferencesRequestTypeDef(BaseValidatorModel):
    GlobalEndpointTokenVersion: GlobalEndpointTokenVersionType


class UntagInstanceProfileRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    TagKeys: Sequence[str]


class UntagMFADeviceRequestTypeDef(BaseValidatorModel):
    SerialNumber: str
    TagKeys: Sequence[str]


class UntagOpenIDConnectProviderRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    TagKeys: Sequence[str]


class UntagPolicyRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    TagKeys: Sequence[str]


class UntagRoleRequestTypeDef(BaseValidatorModel):
    RoleName: str
    TagKeys: Sequence[str]


class UntagSAMLProviderRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    TagKeys: Sequence[str]


class UntagServerCertificateRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    TagKeys: Sequence[str]


class UntagUserRequestTypeDef(BaseValidatorModel):
    UserName: str
    TagKeys: Sequence[str]


class UpdateAccessKeyRequestAccessKeyActivateTypeDef(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestAccessKeyDeactivateTypeDef(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestAccessKeyPairActivateTypeDef(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestTypeDef(BaseValidatorModel):
    AccessKeyId: str
    Status: StatusTypeType
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


class UpdateAccountPasswordPolicyRequestTypeDef(BaseValidatorModel):
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


class UpdateAssumeRolePolicyRequestTypeDef(BaseValidatorModel):
    RoleName: str
    PolicyDocument: str


class UpdateGroupRequestGroupUpdateTypeDef(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None


class UpdateGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None


class UpdateLoginProfileRequestLoginProfileUpdateTypeDef(BaseValidatorModel):
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class UpdateLoginProfileRequestTypeDef(BaseValidatorModel):
    UserName: str
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


class UpdateOpenIDConnectProviderThumbprintRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ThumbprintList: Sequence[str]


class UpdateRoleDescriptionRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Description: str


class UpdateRoleRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None


class UpdateSAMLProviderRequestSamlProviderUpdateTypeDef(BaseValidatorModel):
    SAMLMetadataDocument: Optional[str] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None
    RemovePrivateKey: Optional[str] = None


class UpdateSAMLProviderRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    SAMLMetadataDocument: Optional[str] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None
    RemovePrivateKey: Optional[str] = None


class UpdateSSHPublicKeyRequestTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Status: StatusTypeType


class UpdateServerCertificateRequestServerCertificateUpdateTypeDef(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None


class UpdateServerCertificateRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None


class UpdateServiceSpecificCredentialRequestTypeDef(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    Status: StatusTypeType
    UserName: Optional[str] = None


class UpdateSigningCertificateRequestSigningCertificateActivateTypeDef(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateSigningCertificateRequestTypeDef(BaseValidatorModel):
    CertificateId: str
    Status: StatusTypeType
    UserName: Optional[str] = None


class UpdateUserRequestTypeDef(BaseValidatorModel):
    UserName: str
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None


class UpdateUserRequestUserUpdateTypeDef(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None


class UploadSSHPublicKeyRequestTypeDef(BaseValidatorModel):
    UserName: str
    SSHPublicKeyBody: str


class UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef(BaseValidatorModel):
    CertificateBody: str
    UserName: Optional[str] = None


class UploadSigningCertificateRequestTypeDef(BaseValidatorModel):
    CertificateBody: str
    UserName: Optional[str] = None


class SimulateCustomPolicyRequestTypeDef(BaseValidatorModel):
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


class SimulatePrincipalPolicyRequestTypeDef(BaseValidatorModel):
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


class CreateAccessKeyResponseTypeDef(BaseValidatorModel):
    AccessKey: AccessKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteServiceLinkedRoleResponseTypeDef(BaseValidatorModel):
    DeletionTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisableOrganizationsRootCredentialsManagementResponseTypeDef(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadataTypeDef


class DisableOrganizationsRootSessionsResponseTypeDef(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class EnableOrganizationsRootCredentialsManagementResponseTypeDef(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadataTypeDef


class EnableOrganizationsRootSessionsResponseTypeDef(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
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


class AccessKeyLastUsedTypeDef(BaseValidatorModel):
    pass


class GetAccessKeyLastUsedResponseTypeDef(BaseValidatorModel):
    UserName: str
    AccessKeyLastUsed: AccessKeyLastUsedTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountSummaryResponseTypeDef(BaseValidatorModel):
    SummaryMap: Dict[SummaryKeyTypeType, int]
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


class ListGroupPoliciesResponseTypeDef(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListOrganizationsFeaturesResponseTypeDef(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
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


class UpdateSAMLProviderResponseTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef


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


class CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateInstanceProfileRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateOpenIDConnectProviderRequestTypeDef(BaseValidatorModel):
    Url: str
    ClientIDList: Optional[Sequence[str]] = None
    ThumbprintList: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateOpenIDConnectProviderResponseTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePolicyRequestServiceResourceCreatePolicyTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreatePolicyRequestTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateRoleRequestServiceResourceCreateRoleTypeDef(BaseValidatorModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateRoleRequestTypeDef(BaseValidatorModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef(BaseValidatorModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None


class CreateSAMLProviderRequestTypeDef(BaseValidatorModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None


class CreateSAMLProviderResponseTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserRequestServiceResourceCreateUserTypeDef(BaseValidatorModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateUserRequestTypeDef(BaseValidatorModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateUserRequestUserCreateTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef(BaseValidatorModel):
    VirtualMFADeviceName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateVirtualMFADeviceRequestTypeDef(BaseValidatorModel):
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


class TagInstanceProfileRequestTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    Tags: Sequence[TagTypeDef]


class TagMFADeviceRequestTypeDef(BaseValidatorModel):
    SerialNumber: str
    Tags: Sequence[TagTypeDef]


class TagOpenIDConnectProviderRequestTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Tags: Sequence[TagTypeDef]


class TagPolicyRequestTypeDef(BaseValidatorModel):
    PolicyArn: str
    Tags: Sequence[TagTypeDef]


class TagRoleRequestTypeDef(BaseValidatorModel):
    RoleName: str
    Tags: Sequence[TagTypeDef]


class TagSAMLProviderRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    Tags: Sequence[TagTypeDef]


class TagServerCertificateRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    Tags: Sequence[TagTypeDef]


class TagUserRequestTypeDef(BaseValidatorModel):
    UserName: str
    Tags: Sequence[TagTypeDef]


class UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UploadServerCertificateRequestTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


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


class ServiceSpecificCredentialTypeDef(BaseValidatorModel):
    pass


class CreateServiceSpecificCredentialResponseTypeDef(BaseValidatorModel):
    ServiceSpecificCredential: ServiceSpecificCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ResetServiceSpecificCredentialResponseTypeDef(BaseValidatorModel):
    ServiceSpecificCredential: ServiceSpecificCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeletionTaskFailureReasonTypeTypeDef(BaseValidatorModel):
    Reason: Optional[str] = None
    RoleUsageList: Optional[List[RoleUsageTypeTypeDef]] = None


class EntityInfoTypeDef(BaseValidatorModel):
    pass


class EntityDetailsTypeDef(BaseValidatorModel):
    EntityInfo: EntityInfoTypeDef
    LastAuthenticated: Optional[datetime] = None


class AccessDetailTypeDef(BaseValidatorModel):
    pass


class GetOrganizationsAccessReportResponseTypeDef(BaseValidatorModel):
    JobStatus: JobStatusTypeType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    NumberOfServicesAccessible: int
    NumberOfServicesNotAccessed: int
    AccessDetails: List[AccessDetailTypeDef]
    IsTruncated: bool
    Marker: str
    ErrorDetails: ErrorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountAuthorizationDetailsRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[Sequence[EntityTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetGroupRequestPaginateTypeDef(BaseValidatorModel):
    GroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccessKeysRequestPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountAliasesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttachedGroupPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    GroupName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttachedRolePoliciesRequestPaginateTypeDef(BaseValidatorModel):
    RoleName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttachedUserPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    UserName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEntitiesForPolicyRequestPaginateTypeDef(BaseValidatorModel):
    PolicyArn: str
    EntityFilter: Optional[EntityTypeType] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    GroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsForUserRequestPaginateTypeDef(BaseValidatorModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstanceProfileTagsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstanceProfilesForRoleRequestPaginateTypeDef(BaseValidatorModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstanceProfilesRequestPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMFADeviceTagsRequestPaginateTypeDef(BaseValidatorModel):
    SerialNumber: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMFADevicesRequestPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOpenIDConnectProviderTagsRequestPaginateTypeDef(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    Scope: Optional[PolicyScopeTypeType] = None
    OnlyAttached: Optional[bool] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPolicyTagsRequestPaginateTypeDef(BaseValidatorModel):
    PolicyArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPolicyVersionsRequestPaginateTypeDef(BaseValidatorModel):
    PolicyArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRolePoliciesRequestPaginateTypeDef(BaseValidatorModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRoleTagsRequestPaginateTypeDef(BaseValidatorModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRolesRequestPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSAMLProviderTagsRequestPaginateTypeDef(BaseValidatorModel):
    SAMLProviderArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSSHPublicKeysRequestPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServerCertificateTagsRequestPaginateTypeDef(BaseValidatorModel):
    ServerCertificateName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServerCertificatesRequestPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSigningCertificatesRequestPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUserPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUserTagsRequestPaginateTypeDef(BaseValidatorModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVirtualMFADevicesRequestPaginateTypeDef(BaseValidatorModel):
    AssignmentStatus: Optional[AssignmentStatusTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SimulateCustomPolicyRequestPaginateTypeDef(BaseValidatorModel):
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


class SimulatePrincipalPolicyRequestPaginateTypeDef(BaseValidatorModel):
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


class GetInstanceProfileRequestWaitTypeDef(BaseValidatorModel):
    InstanceProfileName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetPolicyRequestWaitTypeDef(BaseValidatorModel):
    PolicyArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetRoleRequestWaitTypeDef(BaseValidatorModel):
    RoleName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetUserRequestWaitTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetSAMLProviderResponseTypeDef(BaseValidatorModel):
    SAMLProviderUUID: str
    SAMLMetadataDocument: str
    CreateDate: datetime
    ValidUntil: datetime
    Tags: List[TagTypeDef]
    AssertionEncryptionMode: AssertionEncryptionModeTypeType
    PrivateKeyList: List[SAMLPrivateKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


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


class ServiceSpecificCredentialMetadataTypeDef(BaseValidatorModel):
    pass


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
    JobStatus: JobStatusTypeType
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


class ServiceLastAccessedTypeDef(BaseValidatorModel):
    pass


class GetServiceLastAccessedDetailsResponseTypeDef(BaseValidatorModel):
    JobStatus: JobStatusTypeType
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


class PolicyDocumentTypeDef(BaseValidatorModel):
    pass


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



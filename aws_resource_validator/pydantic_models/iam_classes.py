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
from aws_resource_validator.pydantic_models.iam_constants import *

class AccessDetailTypeDef(BaseModel):
    ServiceName: str
    ServiceNamespace: str
    Region: Optional[str] = None
    EntityPath: Optional[str] = None
    LastAuthenticatedTime: Optional[datetime] = None
    TotalAuthenticatedEntities: Optional[int] = None

class AccessKeyLastUsedTypeDef(BaseModel):
    LastUsedDate: datetime
    ServiceName: str
    Region: str

class AccessKeyMetadataTypeDef(BaseModel):
    UserName: Optional[str] = None
    AccessKeyId: Optional[str] = None
    Status: Optional[statusTypeType] = None
    CreateDate: Optional[datetime] = None

class AccessKeyTypeDef(BaseModel):
    UserName: str
    AccessKeyId: str
    Status: statusTypeType
    SecretAccessKey: str
    CreateDate: Optional[datetime] = None

class AddClientIDToOpenIDConnectProviderRequestRequestTypeDef(BaseModel):
    OpenIDConnectProviderArn: str
    ClientID: str

class AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef(BaseModel):
    RoleName: str

class AddRoleToInstanceProfileRequestRequestTypeDef(BaseModel):
    InstanceProfileName: str
    RoleName: str

class AddUserToGroupRequestGroupAddUserTypeDef(BaseModel):
    UserName: str

class AddUserToGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    UserName: str

class AddUserToGroupRequestUserAddGroupTypeDef(BaseModel):
    GroupName: str

class AttachGroupPolicyRequestGroupAttachPolicyTypeDef(BaseModel):
    PolicyArn: str

class AttachGroupPolicyRequestPolicyAttachGroupTypeDef(BaseModel):
    GroupName: str

class AttachGroupPolicyRequestRequestTypeDef(BaseModel):
    GroupName: str
    PolicyArn: str

class AttachRolePolicyRequestPolicyAttachRoleTypeDef(BaseModel):
    RoleName: str

class AttachRolePolicyRequestRequestTypeDef(BaseModel):
    RoleName: str
    PolicyArn: str

class AttachRolePolicyRequestRoleAttachPolicyTypeDef(BaseModel):
    PolicyArn: str

class AttachUserPolicyRequestPolicyAttachUserTypeDef(BaseModel):
    UserName: str

class AttachUserPolicyRequestRequestTypeDef(BaseModel):
    UserName: str
    PolicyArn: str

class AttachUserPolicyRequestUserAttachPolicyTypeDef(BaseModel):
    PolicyArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AttachedPermissionsBoundaryTypeDef(BaseModel):
    PermissionsBoundaryType: Optional[Literal["PermissionsBoundaryPolicy"]] = None
    PermissionsBoundaryArn: Optional[str] = None

class AttachedPolicyTypeDef(BaseModel):
    PolicyName: Optional[str] = None
    PolicyArn: Optional[str] = None

class ChangePasswordRequestRequestTypeDef(BaseModel):
    OldPassword: str
    NewPassword: str

class ChangePasswordRequestServiceResourceChangePasswordTypeDef(BaseModel):
    OldPassword: str
    NewPassword: str

class ContextEntryTypeDef(BaseModel):
    ContextKeyName: Optional[str] = None
    ContextKeyValues: Optional[Sequence[str]] = None
    ContextKeyType: Optional[ContextKeyTypeEnumType] = None

class CreateAccessKeyRequestRequestTypeDef(BaseModel):
    UserName: Optional[str] = None

class CreateAccountAliasRequestRequestTypeDef(BaseModel):
    AccountAlias: str

class CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef(BaseModel):
    AccountAlias: str

class CreateGroupRequestGroupCreateTypeDef(BaseModel):
    Path: Optional[str] = None

class CreateGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    Path: Optional[str] = None

class CreateGroupRequestServiceResourceCreateGroupTypeDef(BaseModel):
    GroupName: str
    Path: Optional[str] = None

class GroupTypeDef(BaseModel):
    Path: str
    GroupName: str
    GroupId: str
    Arn: str
    CreateDate: datetime

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreateLoginProfileRequestLoginProfileCreateTypeDef(BaseModel):
    Password: str
    PasswordResetRequired: Optional[bool] = None

class CreateLoginProfileRequestRequestTypeDef(BaseModel):
    UserName: str
    Password: str
    PasswordResetRequired: Optional[bool] = None

class CreateLoginProfileRequestUserCreateLoginProfileTypeDef(BaseModel):
    Password: str
    PasswordResetRequired: Optional[bool] = None

class LoginProfileTypeDef(BaseModel):
    UserName: str
    CreateDate: datetime
    PasswordResetRequired: Optional[bool] = None

class CreatePolicyVersionRequestPolicyCreateVersionTypeDef(BaseModel):
    PolicyDocument: str
    SetAsDefault: Optional[bool] = None

class CreatePolicyVersionRequestRequestTypeDef(BaseModel):
    PolicyArn: str
    PolicyDocument: str
    SetAsDefault: Optional[bool] = None

class CreateServiceLinkedRoleRequestRequestTypeDef(BaseModel):
    AWSServiceName: str
    Description: Optional[str] = None
    CustomSuffix: Optional[str] = None

class CreateServiceSpecificCredentialRequestRequestTypeDef(BaseModel):
    UserName: str
    ServiceName: str

class ServiceSpecificCredentialTypeDef(BaseModel):
    CreateDate: datetime
    ServiceName: str
    ServiceUserName: str
    ServicePassword: str
    ServiceSpecificCredentialId: str
    UserName: str
    Status: statusTypeType

class DeactivateMFADeviceRequestRequestTypeDef(BaseModel):
    UserName: str
    SerialNumber: str

class DeleteAccessKeyRequestRequestTypeDef(BaseModel):
    AccessKeyId: str
    UserName: Optional[str] = None

class DeleteAccountAliasRequestRequestTypeDef(BaseModel):
    AccountAlias: str

class DeleteGroupPolicyRequestRequestTypeDef(BaseModel):
    GroupName: str
    PolicyName: str

class DeleteGroupRequestRequestTypeDef(BaseModel):
    GroupName: str

class DeleteInstanceProfileRequestRequestTypeDef(BaseModel):
    InstanceProfileName: str

class DeleteLoginProfileRequestRequestTypeDef(BaseModel):
    UserName: str

class DeleteOpenIDConnectProviderRequestRequestTypeDef(BaseModel):
    OpenIDConnectProviderArn: str

class DeletePolicyRequestRequestTypeDef(BaseModel):
    PolicyArn: str

class DeletePolicyVersionRequestRequestTypeDef(BaseModel):
    PolicyArn: str
    VersionId: str

class DeleteRolePermissionsBoundaryRequestRequestTypeDef(BaseModel):
    RoleName: str

class DeleteRolePolicyRequestRequestTypeDef(BaseModel):
    RoleName: str
    PolicyName: str

class DeleteRoleRequestRequestTypeDef(BaseModel):
    RoleName: str

class DeleteSAMLProviderRequestRequestTypeDef(BaseModel):
    SAMLProviderArn: str

class DeleteSSHPublicKeyRequestRequestTypeDef(BaseModel):
    UserName: str
    SSHPublicKeyId: str

class DeleteServerCertificateRequestRequestTypeDef(BaseModel):
    ServerCertificateName: str

class DeleteServiceLinkedRoleRequestRequestTypeDef(BaseModel):
    RoleName: str

class DeleteServiceSpecificCredentialRequestRequestTypeDef(BaseModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None

class DeleteSigningCertificateRequestRequestTypeDef(BaseModel):
    CertificateId: str
    UserName: Optional[str] = None

class DeleteUserPermissionsBoundaryRequestRequestTypeDef(BaseModel):
    UserName: str

class DeleteUserPolicyRequestRequestTypeDef(BaseModel):
    UserName: str
    PolicyName: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    UserName: str

class DeleteVirtualMFADeviceRequestRequestTypeDef(BaseModel):
    SerialNumber: str

class RoleUsageTypeTypeDef(BaseModel):
    Region: Optional[str] = None
    Resources: Optional[List[str]] = None

class DetachGroupPolicyRequestGroupDetachPolicyTypeDef(BaseModel):
    PolicyArn: str

class DetachGroupPolicyRequestPolicyDetachGroupTypeDef(BaseModel):
    GroupName: str

class DetachGroupPolicyRequestRequestTypeDef(BaseModel):
    GroupName: str
    PolicyArn: str

class DetachRolePolicyRequestPolicyDetachRoleTypeDef(BaseModel):
    RoleName: str

class DetachRolePolicyRequestRequestTypeDef(BaseModel):
    RoleName: str
    PolicyArn: str

class DetachRolePolicyRequestRoleDetachPolicyTypeDef(BaseModel):
    PolicyArn: str

class DetachUserPolicyRequestPolicyDetachUserTypeDef(BaseModel):
    UserName: str

class DetachUserPolicyRequestRequestTypeDef(BaseModel):
    UserName: str
    PolicyArn: str

class DetachUserPolicyRequestUserDetachPolicyTypeDef(BaseModel):
    PolicyArn: str

class EnableMFADeviceRequestMfaDeviceAssociateTypeDef(BaseModel):
    AuthenticationCode1: str
    AuthenticationCode2: str

class EnableMFADeviceRequestRequestTypeDef(BaseModel):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str

class EnableMFADeviceRequestUserEnableMfaTypeDef(BaseModel):
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str

class EntityInfoTypeDef(BaseModel):
    Arn: str
    Name: str
    Type: policyOwnerEntityTypeType
    Id: str
    Path: Optional[str] = None

class ErrorDetailsTypeDef(BaseModel):
    Message: str
    Code: str

class OrganizationsDecisionDetailTypeDef(BaseModel):
    AllowedByOrganizations: Optional[bool] = None

class PermissionsBoundaryDecisionDetailTypeDef(BaseModel):
    AllowedByPermissionsBoundary: Optional[bool] = None

class GenerateOrganizationsAccessReportRequestRequestTypeDef(BaseModel):
    EntityPath: str
    OrganizationsPolicyId: Optional[str] = None

class GenerateServiceLastAccessedDetailsRequestRequestTypeDef(BaseModel):
    Arn: str
    Granularity: Optional[AccessAdvisorUsageGranularityTypeType] = None

class GetAccessKeyLastUsedRequestRequestTypeDef(BaseModel):
    AccessKeyId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetAccountAuthorizationDetailsRequestRequestTypeDef(BaseModel):
    Filter: Optional[Sequence[EntityTypeType]] = None
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class PasswordPolicyTypeDef(BaseModel):
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

class GetContextKeysForCustomPolicyRequestRequestTypeDef(BaseModel):
    PolicyInputList: Sequence[str]

class GetContextKeysForPrincipalPolicyRequestRequestTypeDef(BaseModel):
    PolicySourceArn: str
    PolicyInputList: Optional[Sequence[str]] = None

class GetGroupPolicyRequestRequestTypeDef(BaseModel):
    GroupName: str
    PolicyName: str

class GetGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetInstanceProfileRequestRequestTypeDef(BaseModel):
    InstanceProfileName: str

class GetLoginProfileRequestRequestTypeDef(BaseModel):
    UserName: str

class GetMFADeviceRequestRequestTypeDef(BaseModel):
    SerialNumber: str
    UserName: Optional[str] = None

class GetOpenIDConnectProviderRequestRequestTypeDef(BaseModel):
    OpenIDConnectProviderArn: str

class GetOrganizationsAccessReportRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    SortKey: Optional[sortKeyTypeType] = None

class GetPolicyRequestRequestTypeDef(BaseModel):
    PolicyArn: str

class GetPolicyVersionRequestRequestTypeDef(BaseModel):
    PolicyArn: str
    VersionId: str

class GetRolePolicyRequestRequestTypeDef(BaseModel):
    RoleName: str
    PolicyName: str

class GetRoleRequestRequestTypeDef(BaseModel):
    RoleName: str

class GetSAMLProviderRequestRequestTypeDef(BaseModel):
    SAMLProviderArn: str

class GetSSHPublicKeyRequestRequestTypeDef(BaseModel):
    UserName: str
    SSHPublicKeyId: str
    Encoding: encodingTypeType

class SSHPublicKeyTypeDef(BaseModel):
    UserName: str
    SSHPublicKeyId: str
    Fingerprint: str
    SSHPublicKeyBody: str
    Status: statusTypeType
    UploadDate: Optional[datetime] = None

class GetServerCertificateRequestRequestTypeDef(BaseModel):
    ServerCertificateName: str

class GetServiceLastAccessedDetailsRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef(BaseModel):
    JobId: str
    ServiceNamespace: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None

class GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef(BaseModel):
    DeletionTaskId: str

class GetUserPolicyRequestRequestTypeDef(BaseModel):
    UserName: str
    PolicyName: str

class GetUserRequestRequestTypeDef(BaseModel):
    UserName: Optional[str] = None

class ListAccessKeysRequestRequestTypeDef(BaseModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListAccountAliasesRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListAttachedGroupPoliciesRequestRequestTypeDef(BaseModel):
    GroupName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListAttachedRolePoliciesRequestRequestTypeDef(BaseModel):
    RoleName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListAttachedUserPoliciesRequestRequestTypeDef(BaseModel):
    UserName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListEntitiesForPolicyRequestRequestTypeDef(BaseModel):
    PolicyArn: str
    EntityFilter: Optional[EntityTypeType] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class PolicyGroupTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None

class PolicyRoleTypeDef(BaseModel):
    RoleName: Optional[str] = None
    RoleId: Optional[str] = None

class PolicyUserTypeDef(BaseModel):
    UserName: Optional[str] = None
    UserId: Optional[str] = None

class ListGroupPoliciesRequestRequestTypeDef(BaseModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListGroupsForUserRequestRequestTypeDef(BaseModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListGroupsRequestRequestTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListInstanceProfileTagsRequestRequestTypeDef(BaseModel):
    InstanceProfileName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListInstanceProfilesForRoleRequestRequestTypeDef(BaseModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListInstanceProfilesRequestRequestTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListMFADeviceTagsRequestRequestTypeDef(BaseModel):
    SerialNumber: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListMFADevicesRequestRequestTypeDef(BaseModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class MFADeviceTypeDef(BaseModel):
    UserName: str
    SerialNumber: str
    EnableDate: datetime

class ListOpenIDConnectProviderTagsRequestRequestTypeDef(BaseModel):
    OpenIDConnectProviderArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class OpenIDConnectProviderListEntryTypeDef(BaseModel):
    Arn: Optional[str] = None

class PolicyGrantingServiceAccessTypeDef(BaseModel):
    PolicyName: str
    PolicyType: policyTypeType
    PolicyArn: Optional[str] = None
    EntityType: Optional[policyOwnerEntityTypeType] = None
    EntityName: Optional[str] = None

class ListPoliciesGrantingServiceAccessRequestRequestTypeDef(BaseModel):
    Arn: str
    ServiceNamespaces: Sequence[str]
    Marker: Optional[str] = None

class ListPoliciesRequestRequestTypeDef(BaseModel):
    Scope: Optional[policyScopeTypeType] = None
    OnlyAttached: Optional[bool] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListPolicyTagsRequestRequestTypeDef(BaseModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListPolicyVersionsRequestRequestTypeDef(BaseModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListRolePoliciesRequestRequestTypeDef(BaseModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListRoleTagsRequestRequestTypeDef(BaseModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListRolesRequestRequestTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListSAMLProviderTagsRequestRequestTypeDef(BaseModel):
    SAMLProviderArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class SAMLProviderListEntryTypeDef(BaseModel):
    Arn: Optional[str] = None
    ValidUntil: Optional[datetime] = None
    CreateDate: Optional[datetime] = None

class ListSSHPublicKeysRequestRequestTypeDef(BaseModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class SSHPublicKeyMetadataTypeDef(BaseModel):
    UserName: str
    SSHPublicKeyId: str
    Status: statusTypeType
    UploadDate: datetime

class ListServerCertificateTagsRequestRequestTypeDef(BaseModel):
    ServerCertificateName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListServerCertificatesRequestRequestTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ServerCertificateMetadataTypeDef(BaseModel):
    Path: str
    ServerCertificateName: str
    ServerCertificateId: str
    Arn: str
    UploadDate: Optional[datetime] = None
    Expiration: Optional[datetime] = None

class ListServiceSpecificCredentialsRequestRequestTypeDef(BaseModel):
    UserName: Optional[str] = None
    ServiceName: Optional[str] = None

class ServiceSpecificCredentialMetadataTypeDef(BaseModel):
    UserName: str
    Status: statusTypeType
    ServiceUserName: str
    CreateDate: datetime
    ServiceSpecificCredentialId: str
    ServiceName: str

class ListSigningCertificatesRequestRequestTypeDef(BaseModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class SigningCertificateTypeDef(BaseModel):
    UserName: str
    CertificateId: str
    CertificateBody: str
    Status: statusTypeType
    UploadDate: Optional[datetime] = None

class ListUserPoliciesRequestRequestTypeDef(BaseModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListUserTagsRequestRequestTypeDef(BaseModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListUsersRequestRequestTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListVirtualMFADevicesRequestRequestTypeDef(BaseModel):
    AssignmentStatus: Optional[assignmentStatusTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class PolicyDocumentStatementTypeDef(BaseModel):
    Effect: str
    Resource: Union[str, List[str]]
    Sid: str
    Action: Union[str, List[str]]

class PositionTypeDef(BaseModel):
    Line: Optional[int] = None
    Column: Optional[int] = None

class PutGroupPolicyRequestGroupCreatePolicyTypeDef(BaseModel):
    PolicyName: str
    PolicyDocument: str

class PutGroupPolicyRequestGroupPolicyPutTypeDef(BaseModel):
    PolicyDocument: str

class PutGroupPolicyRequestRequestTypeDef(BaseModel):
    GroupName: str
    PolicyName: str
    PolicyDocument: str

class PutRolePermissionsBoundaryRequestRequestTypeDef(BaseModel):
    RoleName: str
    PermissionsBoundary: str

class PutRolePolicyRequestRequestTypeDef(BaseModel):
    RoleName: str
    PolicyName: str
    PolicyDocument: str

class PutRolePolicyRequestRolePolicyPutTypeDef(BaseModel):
    PolicyDocument: str

class PutUserPermissionsBoundaryRequestRequestTypeDef(BaseModel):
    UserName: str
    PermissionsBoundary: str

class PutUserPolicyRequestRequestTypeDef(BaseModel):
    UserName: str
    PolicyName: str
    PolicyDocument: str

class PutUserPolicyRequestUserCreatePolicyTypeDef(BaseModel):
    PolicyName: str
    PolicyDocument: str

class PutUserPolicyRequestUserPolicyPutTypeDef(BaseModel):
    PolicyDocument: str

class RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef(BaseModel):
    OpenIDConnectProviderArn: str
    ClientID: str

class RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef(BaseModel):
    RoleName: str

class RemoveRoleFromInstanceProfileRequestRequestTypeDef(BaseModel):
    InstanceProfileName: str
    RoleName: str

class RemoveUserFromGroupRequestGroupRemoveUserTypeDef(BaseModel):
    UserName: str

class RemoveUserFromGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    UserName: str

class RemoveUserFromGroupRequestUserRemoveGroupTypeDef(BaseModel):
    GroupName: str

class ResetServiceSpecificCredentialRequestRequestTypeDef(BaseModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None

class ResyncMFADeviceRequestMfaDeviceResyncTypeDef(BaseModel):
    AuthenticationCode1: str
    AuthenticationCode2: str

class ResyncMFADeviceRequestRequestTypeDef(BaseModel):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str

class RoleLastUsedTypeDef(BaseModel):
    LastUsedDate: Optional[datetime] = None
    Region: Optional[str] = None

class TrackedActionLastAccessedTypeDef(BaseModel):
    ActionName: Optional[str] = None
    LastAccessedEntity: Optional[str] = None
    LastAccessedTime: Optional[datetime] = None
    LastAccessedRegion: Optional[str] = None

class SetDefaultPolicyVersionRequestRequestTypeDef(BaseModel):
    PolicyArn: str
    VersionId: str

class SetSecurityTokenServicePreferencesRequestRequestTypeDef(BaseModel):
    GlobalEndpointTokenVersion: globalEndpointTokenVersionType

class UntagInstanceProfileRequestRequestTypeDef(BaseModel):
    InstanceProfileName: str
    TagKeys: Sequence[str]

class UntagMFADeviceRequestRequestTypeDef(BaseModel):
    SerialNumber: str
    TagKeys: Sequence[str]

class UntagOpenIDConnectProviderRequestRequestTypeDef(BaseModel):
    OpenIDConnectProviderArn: str
    TagKeys: Sequence[str]

class UntagPolicyRequestRequestTypeDef(BaseModel):
    PolicyArn: str
    TagKeys: Sequence[str]

class UntagRoleRequestRequestTypeDef(BaseModel):
    RoleName: str
    TagKeys: Sequence[str]

class UntagSAMLProviderRequestRequestTypeDef(BaseModel):
    SAMLProviderArn: str
    TagKeys: Sequence[str]

class UntagServerCertificateRequestRequestTypeDef(BaseModel):
    ServerCertificateName: str
    TagKeys: Sequence[str]

class UntagUserRequestRequestTypeDef(BaseModel):
    UserName: str
    TagKeys: Sequence[str]

class UpdateAccessKeyRequestAccessKeyActivateTypeDef(BaseModel):
    Status: Optional[statusTypeType] = None

class UpdateAccessKeyRequestAccessKeyDeactivateTypeDef(BaseModel):
    Status: Optional[statusTypeType] = None

class UpdateAccessKeyRequestAccessKeyPairActivateTypeDef(BaseModel):
    Status: Optional[statusTypeType] = None

class UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef(BaseModel):
    Status: Optional[statusTypeType] = None

class UpdateAccessKeyRequestRequestTypeDef(BaseModel):
    AccessKeyId: str
    Status: statusTypeType
    UserName: Optional[str] = None

class UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef(BaseModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None

class UpdateAccountPasswordPolicyRequestRequestTypeDef(BaseModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None

class UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef(BaseModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None

class UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef(BaseModel):
    PolicyDocument: str

class UpdateAssumeRolePolicyRequestRequestTypeDef(BaseModel):
    RoleName: str
    PolicyDocument: str

class UpdateGroupRequestGroupUpdateTypeDef(BaseModel):
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None

class UpdateGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None

class UpdateLoginProfileRequestLoginProfileUpdateTypeDef(BaseModel):
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None

class UpdateLoginProfileRequestRequestTypeDef(BaseModel):
    UserName: str
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None

class UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef(BaseModel):
    OpenIDConnectProviderArn: str
    ThumbprintList: Sequence[str]

class UpdateRoleDescriptionRequestRequestTypeDef(BaseModel):
    RoleName: str
    Description: str

class UpdateRoleRequestRequestTypeDef(BaseModel):
    RoleName: str
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None

class UpdateSAMLProviderRequestRequestTypeDef(BaseModel):
    SAMLMetadataDocument: str
    SAMLProviderArn: str

class UpdateSAMLProviderRequestSamlProviderUpdateTypeDef(BaseModel):
    SAMLMetadataDocument: str

class UpdateSSHPublicKeyRequestRequestTypeDef(BaseModel):
    UserName: str
    SSHPublicKeyId: str
    Status: statusTypeType

class UpdateServerCertificateRequestRequestTypeDef(BaseModel):
    ServerCertificateName: str
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None

class UpdateServerCertificateRequestServerCertificateUpdateTypeDef(BaseModel):
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None

class UpdateServiceSpecificCredentialRequestRequestTypeDef(BaseModel):
    ServiceSpecificCredentialId: str
    Status: statusTypeType
    UserName: Optional[str] = None

class UpdateSigningCertificateRequestRequestTypeDef(BaseModel):
    CertificateId: str
    Status: statusTypeType
    UserName: Optional[str] = None

class UpdateSigningCertificateRequestSigningCertificateActivateTypeDef(BaseModel):
    Status: Optional[statusTypeType] = None

class UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef(BaseModel):
    Status: Optional[statusTypeType] = None

class UpdateUserRequestRequestTypeDef(BaseModel):
    UserName: str
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None

class UpdateUserRequestUserUpdateTypeDef(BaseModel):
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None

class UploadSSHPublicKeyRequestRequestTypeDef(BaseModel):
    UserName: str
    SSHPublicKeyBody: str

class UploadSigningCertificateRequestRequestTypeDef(BaseModel):
    CertificateBody: str
    UserName: Optional[str] = None

class UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef(BaseModel):
    CertificateBody: str
    UserName: Optional[str] = None

class AttachedPermissionsBoundaryResponseTypeDef(BaseModel):
    PermissionsBoundaryType: Literal["PermissionsBoundaryPolicy"]
    PermissionsBoundaryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessKeyResponseTypeDef(BaseModel):
    AccessKey: AccessKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceLinkedRoleResponseTypeDef(BaseModel):
    DeletionTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateCredentialReportResponseTypeDef(BaseModel):
    State: ReportStateTypeType
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateOrganizationsAccessReportResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateServiceLastAccessedDetailsResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessKeyLastUsedResponseTypeDef(BaseModel):
    UserName: str
    AccessKeyLastUsed: AccessKeyLastUsedTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSummaryResponseTypeDef(BaseModel):
    SummaryMap: Dict[summaryKeyTypeType, int]
    ResponseMetadata: ResponseMetadataTypeDef

class GetContextKeysForPolicyResponseTypeDef(BaseModel):
    ContextKeyNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCredentialReportResponseTypeDef(BaseModel):
    Content: bytes
    ReportFormat: Literal["text/csv"]
    GeneratedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMFADeviceResponseTypeDef(BaseModel):
    UserName: str
    SerialNumber: str
    EnableDate: datetime
    Certifications: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessKeysResponseTypeDef(BaseModel):
    AccessKeyMetadata: List[AccessKeyMetadataTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAliasesResponseTypeDef(BaseModel):
    AccountAliases: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupPoliciesResponseTypeDef(BaseModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRolePoliciesResponseTypeDef(BaseModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserPoliciesResponseTypeDef(BaseModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RoleLastUsedResponseTypeDef(BaseModel):
    LastUsedDate: datetime
    Region: str
    ResponseMetadata: ResponseMetadataTypeDef

class ServerCertificateMetadataResponseTypeDef(BaseModel):
    Path: str
    ServerCertificateName: str
    ServerCertificateId: str
    Arn: str
    UploadDate: datetime
    Expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSAMLProviderResponseTypeDef(BaseModel):
    SAMLProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedGroupPoliciesResponseTypeDef(BaseModel):
    AttachedPolicies: List[AttachedPolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedRolePoliciesResponseTypeDef(BaseModel):
    AttachedPolicies: List[AttachedPolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedUserPoliciesResponseTypeDef(BaseModel):
    AttachedPolicies: List[AttachedPolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class SimulateCustomPolicyRequestRequestTypeDef(BaseModel):
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

class SimulatePrincipalPolicyRequestRequestTypeDef(BaseModel):
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

class CreateGroupResponseTypeDef(BaseModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsForUserResponseTypeDef(BaseModel):
    Groups: List[GroupTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseModel):
    Groups: List[GroupTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileRequestRequestTypeDef(BaseModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef(BaseModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateOpenIDConnectProviderRequestRequestTypeDef(BaseModel):
    Url: str
    ClientIDList: Optional[Sequence[str]] = None
    ThumbprintList: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateOpenIDConnectProviderResponseTypeDef(BaseModel):
    OpenIDConnectProviderArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyRequestRequestTypeDef(BaseModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreatePolicyRequestServiceResourceCreatePolicyTypeDef(BaseModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateRoleRequestRequestTypeDef(BaseModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateRoleRequestServiceResourceCreateRoleTypeDef(BaseModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSAMLProviderRequestRequestTypeDef(BaseModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef(BaseModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSAMLProviderResponseTypeDef(BaseModel):
    SAMLProviderArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserRequestRequestTypeDef(BaseModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserRequestServiceResourceCreateUserTypeDef(BaseModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserRequestUserCreateTypeDef(BaseModel):
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVirtualMFADeviceRequestRequestTypeDef(BaseModel):
    VirtualMFADeviceName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef(BaseModel):
    VirtualMFADeviceName: str
    Path: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetOpenIDConnectProviderResponseTypeDef(BaseModel):
    Url: str
    ClientIDList: List[str]
    ThumbprintList: List[str]
    CreateDate: datetime
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSAMLProviderResponseTypeDef(BaseModel):
    SAMLMetadataDocument: str
    CreateDate: datetime
    ValidUntil: datetime
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfileTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMFADeviceTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOpenIDConnectProviderTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoleTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSAMLProviderTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServerCertificateTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyTypeDef(BaseModel):
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

class TagInstanceProfileRequestRequestTypeDef(BaseModel):
    InstanceProfileName: str
    Tags: Sequence[TagTypeDef]

class TagMFADeviceRequestRequestTypeDef(BaseModel):
    SerialNumber: str
    Tags: Sequence[TagTypeDef]

class TagOpenIDConnectProviderRequestRequestTypeDef(BaseModel):
    OpenIDConnectProviderArn: str
    Tags: Sequence[TagTypeDef]

class TagPolicyRequestRequestTypeDef(BaseModel):
    PolicyArn: str
    Tags: Sequence[TagTypeDef]

class TagRoleRequestRequestTypeDef(BaseModel):
    RoleName: str
    Tags: Sequence[TagTypeDef]

class TagSAMLProviderRequestRequestTypeDef(BaseModel):
    SAMLProviderArn: str
    Tags: Sequence[TagTypeDef]

class TagServerCertificateRequestRequestTypeDef(BaseModel):
    ServerCertificateName: str
    Tags: Sequence[TagTypeDef]

class TagUserRequestRequestTypeDef(BaseModel):
    UserName: str
    Tags: Sequence[TagTypeDef]

class UploadServerCertificateRequestRequestTypeDef(BaseModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef(BaseModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UserResponseTypeDef(BaseModel):
    Path: str
    UserName: str
    UserId: str
    Arn: str
    CreateDate: datetime
    PasswordLastUsed: datetime
    PermissionsBoundary: AttachedPermissionsBoundaryTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UserTypeDef(BaseModel):
    Path: str
    UserName: str
    UserId: str
    Arn: str
    CreateDate: datetime
    PasswordLastUsed: Optional[datetime] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundaryTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateLoginProfileResponseTypeDef(BaseModel):
    LoginProfile: LoginProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoginProfileResponseTypeDef(BaseModel):
    LoginProfile: LoginProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceSpecificCredentialResponseTypeDef(BaseModel):
    ServiceSpecificCredential: ServiceSpecificCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetServiceSpecificCredentialResponseTypeDef(BaseModel):
    ServiceSpecificCredential: ServiceSpecificCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletionTaskFailureReasonTypeTypeDef(BaseModel):
    Reason: Optional[str] = None
    RoleUsageList: Optional[List[RoleUsageTypeTypeDef]] = None

class EntityDetailsTypeDef(BaseModel):
    EntityInfo: EntityInfoTypeDef
    LastAuthenticated: Optional[datetime] = None

class GetOrganizationsAccessReportResponseTypeDef(BaseModel):
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

class GetAccountAuthorizationDetailsRequestGetAccountAuthorizationDetailsPaginateTypeDef(BaseModel):
    Filter: Optional[Sequence[EntityTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetGroupRequestGetGroupPaginateTypeDef(BaseModel):
    GroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessKeysRequestListAccessKeysPaginateTypeDef(BaseModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAliasesRequestListAccountAliasesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedGroupPoliciesRequestListAttachedGroupPoliciesPaginateTypeDef(BaseModel):
    GroupName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedRolePoliciesRequestListAttachedRolePoliciesPaginateTypeDef(BaseModel):
    RoleName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedUserPoliciesRequestListAttachedUserPoliciesPaginateTypeDef(BaseModel):
    UserName: str
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEntitiesForPolicyRequestListEntitiesForPolicyPaginateTypeDef(BaseModel):
    PolicyArn: str
    EntityFilter: Optional[EntityTypeType] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupPoliciesRequestListGroupPoliciesPaginateTypeDef(BaseModel):
    GroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsForUserRequestListGroupsForUserPaginateTypeDef(BaseModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceProfileTagsRequestListInstanceProfileTagsPaginateTypeDef(BaseModel):
    InstanceProfileName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceProfilesForRoleRequestListInstanceProfilesForRolePaginateTypeDef(BaseModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMFADeviceTagsRequestListMFADeviceTagsPaginateTypeDef(BaseModel):
    SerialNumber: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMFADevicesRequestListMFADevicesPaginateTypeDef(BaseModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOpenIDConnectProviderTagsRequestListOpenIDConnectProviderTagsPaginateTypeDef(BaseModel):
    OpenIDConnectProviderArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesRequestListPoliciesPaginateTypeDef(BaseModel):
    Scope: Optional[policyScopeTypeType] = None
    OnlyAttached: Optional[bool] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyTagsRequestListPolicyTagsPaginateTypeDef(BaseModel):
    PolicyArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyVersionsRequestListPolicyVersionsPaginateTypeDef(BaseModel):
    PolicyArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRolePoliciesRequestListRolePoliciesPaginateTypeDef(BaseModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoleTagsRequestListRoleTagsPaginateTypeDef(BaseModel):
    RoleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRolesRequestListRolesPaginateTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSAMLProviderTagsRequestListSAMLProviderTagsPaginateTypeDef(BaseModel):
    SAMLProviderArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSSHPublicKeysRequestListSSHPublicKeysPaginateTypeDef(BaseModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServerCertificateTagsRequestListServerCertificateTagsPaginateTypeDef(BaseModel):
    ServerCertificateName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServerCertificatesRequestListServerCertificatesPaginateTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSigningCertificatesRequestListSigningCertificatesPaginateTypeDef(BaseModel):
    UserName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserPoliciesRequestListUserPoliciesPaginateTypeDef(BaseModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserTagsRequestListUserTagsPaginateTypeDef(BaseModel):
    UserName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    PathPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualMFADevicesRequestListVirtualMFADevicesPaginateTypeDef(BaseModel):
    AssignmentStatus: Optional[assignmentStatusTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SimulateCustomPolicyRequestSimulateCustomPolicyPaginateTypeDef(BaseModel):
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

class SimulatePrincipalPolicyRequestSimulatePrincipalPolicyPaginateTypeDef(BaseModel):
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

class GetAccountPasswordPolicyResponseTypeDef(BaseModel):
    PasswordPolicy: PasswordPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceProfileRequestInstanceProfileExistsWaitTypeDef(BaseModel):
    InstanceProfileName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetPolicyRequestPolicyExistsWaitTypeDef(BaseModel):
    PolicyArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetRoleRequestRoleExistsWaitTypeDef(BaseModel):
    RoleName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetUserRequestUserExistsWaitTypeDef(BaseModel):
    UserName: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetSSHPublicKeyResponseTypeDef(BaseModel):
    SSHPublicKey: SSHPublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UploadSSHPublicKeyResponseTypeDef(BaseModel):
    SSHPublicKey: SSHPublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesForPolicyResponseTypeDef(BaseModel):
    PolicyGroups: List[PolicyGroupTypeDef]
    PolicyUsers: List[PolicyUserTypeDef]
    PolicyRoles: List[PolicyRoleTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMFADevicesResponseTypeDef(BaseModel):
    MFADevices: List[MFADeviceTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOpenIDConnectProvidersResponseTypeDef(BaseModel):
    OpenIDConnectProviderList: List[OpenIDConnectProviderListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesGrantingServiceAccessEntryTypeDef(BaseModel):
    ServiceNamespace: Optional[str] = None
    Policies: Optional[List[PolicyGrantingServiceAccessTypeDef]] = None

class ListSAMLProvidersResponseTypeDef(BaseModel):
    SAMLProviderList: List[SAMLProviderListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSSHPublicKeysResponseTypeDef(BaseModel):
    SSHPublicKeys: List[SSHPublicKeyMetadataTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServerCertificatesResponseTypeDef(BaseModel):
    ServerCertificateMetadataList: List[ServerCertificateMetadataTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ServerCertificateTypeDef(BaseModel):
    ServerCertificateMetadata: ServerCertificateMetadataTypeDef
    CertificateBody: str
    CertificateChain: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class UploadServerCertificateResponseTypeDef(BaseModel):
    ServerCertificateMetadata: ServerCertificateMetadataTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceSpecificCredentialsResponseTypeDef(BaseModel):
    ServiceSpecificCredentials: List[ServiceSpecificCredentialMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSigningCertificatesResponseTypeDef(BaseModel):
    Certificates: List[SigningCertificateTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UploadSigningCertificateResponseTypeDef(BaseModel):
    Certificate: SigningCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyDocumentDictTypeDef(BaseModel):
    Version: str
    Statement: List[PolicyDocumentStatementTypeDef]

class StatementTypeDef(BaseModel):
    SourcePolicyId: Optional[str] = None
    SourcePolicyType: Optional[PolicySourceTypeType] = None
    StartPosition: Optional[PositionTypeDef] = None
    EndPosition: Optional[PositionTypeDef] = None

class ServiceLastAccessedTypeDef(BaseModel):
    ServiceName: str
    ServiceNamespace: str
    LastAuthenticated: Optional[datetime] = None
    LastAuthenticatedEntity: Optional[str] = None
    LastAuthenticatedRegion: Optional[str] = None
    TotalAuthenticatedEntities: Optional[int] = None
    TrackedActionsLastAccessed: Optional[List[TrackedActionLastAccessedTypeDef]] = None

class CreatePolicyResponseTypeDef(BaseModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyResponseTypeDef(BaseModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesResponseTypeDef(BaseModel):
    Policies: List[PolicyTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(BaseModel):
    Group: GroupTypeDef
    Users: List[UserTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(BaseModel):
    Users: List[UserTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualMFADeviceTypeDef(BaseModel):
    SerialNumber: str
    Base32StringSeed: Optional[bytes] = None
    QRCodePNG: Optional[bytes] = None
    User: Optional[UserTypeDef] = None
    EnableDate: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class GetServiceLinkedRoleDeletionStatusResponseTypeDef(BaseModel):
    Status: DeletionTaskStatusTypeType
    Reason: DeletionTaskFailureReasonTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef(BaseModel):
    JobStatus: jobStatusTypeType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    EntityDetailsList: List[EntityDetailsTypeDef]
    IsTruncated: bool
    Marker: str
    Error: ErrorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesGrantingServiceAccessResponseTypeDef(BaseModel):
    PoliciesGrantingServiceAccess: List[ListPoliciesGrantingServiceAccessEntryTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerCertificateResponseTypeDef(BaseModel):
    ServerCertificate: ServerCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceSpecificResultTypeDef(BaseModel):
    EvalResourceName: str
    EvalResourceDecision: PolicyEvaluationDecisionTypeType
    MatchedStatements: Optional[List[StatementTypeDef]] = None
    MissingContextValues: Optional[List[str]] = None
    EvalDecisionDetails: Optional[Dict[str, PolicyEvaluationDecisionTypeType]] = None
    PermissionsBoundaryDecisionDetail: Optional[PermissionsBoundaryDecisionDetailTypeDef] = None

class GetServiceLastAccessedDetailsResponseTypeDef(BaseModel):
    JobStatus: jobStatusTypeType
    JobType: AccessAdvisorUsageGranularityTypeType
    JobCreationDate: datetime
    ServicesLastAccessed: List[ServiceLastAccessedTypeDef]
    JobCompletionDate: datetime
    IsTruncated: bool
    Marker: str
    Error: ErrorDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualMFADeviceResponseTypeDef(BaseModel):
    VirtualMFADevice: VirtualMFADeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualMFADevicesResponseTypeDef(BaseModel):
    VirtualMFADevices: List[VirtualMFADeviceTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupPolicyResponseTypeDef(BaseModel):
    GroupName: str
    PolicyName: str
    PolicyDocument: PolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRolePolicyResponseTypeDef(BaseModel):
    RoleName: str
    PolicyName: str
    PolicyDocument: PolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserPolicyResponseTypeDef(BaseModel):
    UserName: str
    PolicyName: str
    PolicyDocument: PolicyDocumentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyDetailTypeDef(BaseModel):
    PolicyName: Optional[str] = None
    PolicyDocument: Optional[PolicyDocumentTypeDef] = None

class PolicyVersionTypeDef(BaseModel):
    Document: Optional[PolicyDocumentTypeDef] = None
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    CreateDate: Optional[datetime] = None

class RoleTypeDef(BaseModel):
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

class EvaluationResultTypeDef(BaseModel):
    EvalActionName: str
    EvalDecision: PolicyEvaluationDecisionTypeType
    EvalResourceName: Optional[str] = None
    MatchedStatements: Optional[List[StatementTypeDef]] = None
    MissingContextValues: Optional[List[str]] = None
    OrganizationsDecisionDetail: Optional[OrganizationsDecisionDetailTypeDef] = None
    PermissionsBoundaryDecisionDetail: Optional[PermissionsBoundaryDecisionDetailTypeDef] = None
    EvalDecisionDetails: Optional[Dict[str, PolicyEvaluationDecisionTypeType]] = None
    ResourceSpecificResults: Optional[List[ResourceSpecificResultTypeDef]] = None

class GroupDetailTypeDef(BaseModel):
    Path: Optional[str] = None
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    Arn: Optional[str] = None
    CreateDate: Optional[datetime] = None
    GroupPolicyList: Optional[List[PolicyDetailTypeDef]] = None
    AttachedManagedPolicies: Optional[List[AttachedPolicyTypeDef]] = None

class UserDetailTypeDef(BaseModel):
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

class CreatePolicyVersionResponseTypeDef(BaseModel):
    PolicyVersion: PolicyVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyVersionResponseTypeDef(BaseModel):
    PolicyVersion: PolicyVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyVersionsResponseTypeDef(BaseModel):
    Versions: List[PolicyVersionTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedPolicyDetailTypeDef(BaseModel):
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

class CreateRoleResponseTypeDef(BaseModel):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceLinkedRoleResponseTypeDef(BaseModel):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoleResponseTypeDef(BaseModel):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceProfileTypeDef(BaseModel):
    Path: str
    InstanceProfileName: str
    InstanceProfileId: str
    Arn: str
    CreateDate: datetime
    Roles: List[RoleTypeDef]
    Tags: Optional[List[TagTypeDef]] = None

class ListRolesResponseTypeDef(BaseModel):
    Roles: List[RoleTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoleDescriptionResponseTypeDef(BaseModel):
    Role: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SimulatePolicyResponseTypeDef(BaseModel):
    EvaluationResults: List[EvaluationResultTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileResponseTypeDef(BaseModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceProfileResponseTypeDef(BaseModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfilesForRoleResponseTypeDef(BaseModel):
    InstanceProfiles: List[InstanceProfileTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfilesResponseTypeDef(BaseModel):
    InstanceProfiles: List[InstanceProfileTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RoleDetailTypeDef(BaseModel):
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

class GetAccountAuthorizationDetailsResponseTypeDef(BaseModel):
    UserDetailList: List[UserDetailTypeDef]
    GroupDetailList: List[GroupDetailTypeDef]
    RoleDetailList: List[RoleDetailTypeDef]
    Policies: List[ManagedPolicyDetailTypeDef]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


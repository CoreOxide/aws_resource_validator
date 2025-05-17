from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iam.iam_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessDetail(BaseValidatorModel):
    ServiceName: str
    ServiceNamespace: str
    Region: Optional[str] = None
    EntityPath: Optional[str] = None
    LastAuthenticatedTime: Optional[datetime] = None
    TotalAuthenticatedEntities: Optional[int] = None


class AccessKeyLastUsed(BaseValidatorModel):
    ServiceName: str
    Region: str
    LastUsedDate: Optional[datetime] = None


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


# This class is the input for the 'add_client_id_to_open_id_connect_provider' function.
class AddClientIDToOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ClientID: str


class AddRoleToInstanceProfileRequestInstanceProfileAddRole(BaseValidatorModel):
    RoleName: str


# This class is the input for the 'add_role_to_instance_profile' function.
class AddRoleToInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    RoleName: str


class AddUserToGroupRequestGroupAddUser(BaseValidatorModel):
    UserName: str


# This class is the input for the 'add_user_to_group' function.
class AddUserToGroupRequest(BaseValidatorModel):
    GroupName: str
    UserName: str


class AddUserToGroupRequestUserAddGroup(BaseValidatorModel):
    GroupName: str


class AttachGroupPolicyRequestGroupAttachPolicy(BaseValidatorModel):
    PolicyArn: str


class AttachGroupPolicyRequestPolicyAttachGroup(BaseValidatorModel):
    GroupName: str


# This class is the input for the 'attach_group_policy' function.
class AttachGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyArn: str


class AttachRolePolicyRequestPolicyAttachRole(BaseValidatorModel):
    RoleName: str


class AttachRolePolicyRequestRoleAttachPolicy(BaseValidatorModel):
    PolicyArn: str


# This class is the input for the 'attach_role_policy' function.
class AttachRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyArn: str


class AttachUserPolicyRequestPolicyAttachUser(BaseValidatorModel):
    UserName: str


# This class is the input for the 'attach_user_policy' function.
class AttachUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyArn: str


class AttachUserPolicyRequestUserAttachPolicy(BaseValidatorModel):
    PolicyArn: str


class AttachedPermissionsBoundary(BaseValidatorModel):
    PermissionsBoundaryType: Optional[Literal['PermissionsBoundaryPolicy']] = None
    PermissionsBoundaryArn: Optional[str] = None


class AttachedPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyArn: Optional[str] = None


class ChangePasswordRequestServiceResourceChangePassword(BaseValidatorModel):
    OldPassword: str
    NewPassword: str


# This class is the input for the 'change_password' function.
class ChangePasswordRequest(BaseValidatorModel):
    OldPassword: str
    NewPassword: str


class ContextEntry(BaseValidatorModel):
    ContextKeyName: Optional[str] = None
    ContextKeyValues: Optional[List[str]] = None
    ContextKeyType: Optional[ContextKeyTypeEnumType] = None


# This class is the input for the 'create_access_key' function.
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


# This class is the input for the 'create_account_alias' function.
class CreateAccountAliasRequest(BaseValidatorModel):
    AccountAlias: str


class CreateGroupRequestGroupCreate(BaseValidatorModel):
    Path: Optional[str] = None


class CreateGroupRequestServiceResourceCreateGroup(BaseValidatorModel):
    GroupName: str
    Path: Optional[str] = None


# This class is the input for the 'create_group' function.
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


# This class is the input for the 'create_login_profile' function.
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


# This class is the input for the 'create_policy_version' function.
class CreatePolicyVersionRequest(BaseValidatorModel):
    PolicyArn: str
    PolicyDocument: str
    SetAsDefault: Optional[bool] = None


# This class is the input for the 'create_service_linked_role' function.
class CreateServiceLinkedRoleRequest(BaseValidatorModel):
    AWSServiceName: str
    Description: Optional[str] = None
    CustomSuffix: Optional[str] = None


# This class is the input for the 'create_service_specific_credential' function.
class CreateServiceSpecificCredentialRequest(BaseValidatorModel):
    UserName: str
    ServiceName: str


class ServiceSpecificCredential(BaseValidatorModel):
    CreateDate: datetime
    ServiceName: str
    ServiceUserName: str
    ServicePassword: str
    ServiceSpecificCredentialId: str
    UserName: str
    Status: StatusTypeType


# This class is the input for the 'deactivate_mfa_device' function.
class DeactivateMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str
    UserName: Optional[str] = None


# This class is the input for the 'delete_access_key' function.
class DeleteAccessKeyRequest(BaseValidatorModel):
    AccessKeyId: str
    UserName: Optional[str] = None


# This class is the input for the 'delete_account_alias' function.
class DeleteAccountAliasRequest(BaseValidatorModel):
    AccountAlias: str


# This class is the input for the 'delete_group_policy' function.
class DeleteGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyName: str


# This class is the input for the 'delete_group' function.
class DeleteGroupRequest(BaseValidatorModel):
    GroupName: str


# This class is the input for the 'delete_instance_profile' function.
class DeleteInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str


# This class is the input for the 'delete_login_profile' function.
class DeleteLoginProfileRequest(BaseValidatorModel):
    UserName: Optional[str] = None


# This class is the input for the 'delete_open_id_connect_provider' function.
class DeleteOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str


# This class is the input for the 'delete_policy' function.
class DeletePolicyRequest(BaseValidatorModel):
    PolicyArn: str


# This class is the input for the 'delete_policy_version' function.
class DeletePolicyVersionRequest(BaseValidatorModel):
    PolicyArn: str
    VersionId: str


# This class is the input for the 'delete_role_permissions_boundary' function.
class DeleteRolePermissionsBoundaryRequest(BaseValidatorModel):
    RoleName: str


# This class is the input for the 'delete_role_policy' function.
class DeleteRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyName: str


# This class is the input for the 'delete_role' function.
class DeleteRoleRequest(BaseValidatorModel):
    RoleName: str


# This class is the input for the 'delete_saml_provider' function.
class DeleteSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str


# This class is the input for the 'delete_ssh_public_key' function.
class DeleteSSHPublicKeyRequest(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str


# This class is the input for the 'delete_server_certificate' function.
class DeleteServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str


# This class is the input for the 'delete_service_linked_role' function.
class DeleteServiceLinkedRoleRequest(BaseValidatorModel):
    RoleName: str


# This class is the input for the 'delete_service_specific_credential' function.
class DeleteServiceSpecificCredentialRequest(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None


# This class is the input for the 'delete_signing_certificate' function.
class DeleteSigningCertificateRequest(BaseValidatorModel):
    CertificateId: str
    UserName: Optional[str] = None


# This class is the input for the 'delete_user_permissions_boundary' function.
class DeleteUserPermissionsBoundaryRequest(BaseValidatorModel):
    UserName: str


# This class is the input for the 'delete_user_policy' function.
class DeleteUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyName: str


# This class is the input for the 'delete_user' function.
class DeleteUserRequest(BaseValidatorModel):
    UserName: str


# This class is the input for the 'delete_virtual_mfa_device' function.
class DeleteVirtualMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str


class RoleUsageType(BaseValidatorModel):
    Region: Optional[str] = None
    Resources: Optional[List[str]] = None


class DetachGroupPolicyRequestGroupDetachPolicy(BaseValidatorModel):
    PolicyArn: str


class DetachGroupPolicyRequestPolicyDetachGroup(BaseValidatorModel):
    GroupName: str


# This class is the input for the 'detach_group_policy' function.
class DetachGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyArn: str


class DetachRolePolicyRequestPolicyDetachRole(BaseValidatorModel):
    RoleName: str


class DetachRolePolicyRequestRoleDetachPolicy(BaseValidatorModel):
    PolicyArn: str


# This class is the input for the 'detach_role_policy' function.
class DetachRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyArn: str


class DetachUserPolicyRequestPolicyDetachUser(BaseValidatorModel):
    UserName: str


# This class is the input for the 'detach_user_policy' function.
class DetachUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyArn: str


class DetachUserPolicyRequestUserDetachPolicy(BaseValidatorModel):
    PolicyArn: str


class EnableMFADeviceRequestMfaDeviceAssociate(BaseValidatorModel):
    AuthenticationCode1: str
    AuthenticationCode2: str


# This class is the input for the 'enable_mfa_device' function.
class EnableMFADeviceRequest(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str


class EnableMFADeviceRequestUserEnableMfa(BaseValidatorModel):
    SerialNumber: str
    AuthenticationCode1: str
    AuthenticationCode2: str


class EntityInfo(BaseValidatorModel):
    Arn: str
    Name: str
    Type: PolicyOwnerEntityTypeType
    Id: str
    Path: Optional[str] = None


class ErrorDetails(BaseValidatorModel):
    Message: str
    Code: str


class OrganizationsDecisionDetail(BaseValidatorModel):
    AllowedByOrganizations: Optional[bool] = None


class PermissionsBoundaryDecisionDetail(BaseValidatorModel):
    AllowedByPermissionsBoundary: Optional[bool] = None


# This class is the input for the 'generate_organizations_access_report' function.
class GenerateOrganizationsAccessReportRequest(BaseValidatorModel):
    EntityPath: str
    OrganizationsPolicyId: Optional[str] = None


# This class is the input for the 'generate_service_last_accessed_details' function.
class GenerateServiceLastAccessedDetailsRequest(BaseValidatorModel):
    Arn: str
    Granularity: Optional[AccessAdvisorUsageGranularityTypeType] = None


# This class is the input for the 'get_access_key_last_used' function.
class GetAccessKeyLastUsedRequest(BaseValidatorModel):
    AccessKeyId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_account_authorization_details' function.
class GetAccountAuthorizationDetailsRequest(BaseValidatorModel):
    Filter: Optional[List[EntityTypeType]] = None
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


# This class is the input for the 'get_context_keys_for_custom_policy' function.
class GetContextKeysForCustomPolicyRequest(BaseValidatorModel):
    PolicyInputList: List[str]


# This class is the input for the 'get_context_keys_for_principal_policy' function.
class GetContextKeysForPrincipalPolicyRequest(BaseValidatorModel):
    PolicySourceArn: str
    PolicyInputList: Optional[List[str]] = None


# This class is the input for the 'get_group_policy' function.
class GetGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyName: str


# This class is the input for the 'get_group' function.
class GetGroupRequest(BaseValidatorModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'get_instance_profile' function.
class GetInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'get_login_profile' function.
class GetLoginProfileRequest(BaseValidatorModel):
    UserName: Optional[str] = None


# This class is the input for the 'get_mfa_device' function.
class GetMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str
    UserName: Optional[str] = None


# This class is the input for the 'get_open_id_connect_provider' function.
class GetOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str


# This class is the input for the 'get_organizations_access_report' function.
class GetOrganizationsAccessReportRequest(BaseValidatorModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None
    SortKey: Optional[SortKeyTypeType] = None


# This class is the input for the 'get_policy' function.
class GetPolicyRequest(BaseValidatorModel):
    PolicyArn: str


# This class is the input for the 'get_policy_version' function.
class GetPolicyVersionRequest(BaseValidatorModel):
    PolicyArn: str
    VersionId: str


# This class is the input for the 'get_role_policy' function.
class GetRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyName: str


# This class is the input for the 'get_role' function.
class GetRoleRequest(BaseValidatorModel):
    RoleName: str


# This class is the input for the 'get_saml_provider' function.
class GetSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str


class SAMLPrivateKey(BaseValidatorModel):
    KeyId: Optional[str] = None
    Timestamp: Optional[datetime] = None


# This class is the input for the 'get_ssh_public_key' function.
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


# This class is the input for the 'get_server_certificate' function.
class GetServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str


# This class is the input for the 'get_service_last_accessed_details' function.
class GetServiceLastAccessedDetailsRequest(BaseValidatorModel):
    JobId: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'get_service_last_accessed_details_with_entities' function.
class GetServiceLastAccessedDetailsWithEntitiesRequest(BaseValidatorModel):
    JobId: str
    ServiceNamespace: str
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'get_service_linked_role_deletion_status' function.
class GetServiceLinkedRoleDeletionStatusRequest(BaseValidatorModel):
    DeletionTaskId: str


# This class is the input for the 'get_user_policy' function.
class GetUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyName: str


# This class is the input for the 'get_user' function.
class GetUserRequest(BaseValidatorModel):
    UserName: Optional[str] = None


# This class is the input for the 'list_access_keys' function.
class ListAccessKeysRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_account_aliases' function.
class ListAccountAliasesRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_attached_group_policies' function.
class ListAttachedGroupPoliciesRequest(BaseValidatorModel):
    GroupName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_attached_role_policies' function.
class ListAttachedRolePoliciesRequest(BaseValidatorModel):
    RoleName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_attached_user_policies' function.
class ListAttachedUserPoliciesRequest(BaseValidatorModel):
    UserName: str
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_entities_for_policy' function.
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


# This class is the input for the 'list_group_policies' function.
class ListGroupPoliciesRequest(BaseValidatorModel):
    GroupName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_groups_for_user' function.
class ListGroupsForUserRequest(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_groups' function.
class ListGroupsRequest(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_instance_profile_tags' function.
class ListInstanceProfileTagsRequest(BaseValidatorModel):
    InstanceProfileName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_instance_profiles_for_role' function.
class ListInstanceProfilesForRoleRequest(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_instance_profiles' function.
class ListInstanceProfilesRequest(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_mfa_device_tags' function.
class ListMFADeviceTagsRequest(BaseValidatorModel):
    SerialNumber: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_mfa_devices' function.
class ListMFADevicesRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class MFADevice(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    EnableDate: datetime


# This class is the input for the 'list_open_id_connect_provider_tags' function.
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


# This class is the input for the 'list_policies_granting_service_access' function.
class ListPoliciesGrantingServiceAccessRequest(BaseValidatorModel):
    Arn: str
    ServiceNamespaces: List[str]
    Marker: Optional[str] = None


# This class is the input for the 'list_policies' function.
class ListPoliciesRequest(BaseValidatorModel):
    Scope: Optional[PolicyScopeTypeType] = None
    OnlyAttached: Optional[bool] = None
    PathPrefix: Optional[str] = None
    PolicyUsageFilter: Optional[PolicyUsageTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_policy_tags' function.
class ListPolicyTagsRequest(BaseValidatorModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_policy_versions' function.
class ListPolicyVersionsRequest(BaseValidatorModel):
    PolicyArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_role_policies' function.
class ListRolePoliciesRequest(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_role_tags' function.
class ListRoleTagsRequest(BaseValidatorModel):
    RoleName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_roles' function.
class ListRolesRequest(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_saml_provider_tags' function.
class ListSAMLProviderTagsRequest(BaseValidatorModel):
    SAMLProviderArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class SAMLProviderListEntry(BaseValidatorModel):
    Arn: Optional[str] = None
    ValidUntil: Optional[datetime] = None
    CreateDate: Optional[datetime] = None


# This class is the input for the 'list_ssh_public_keys' function.
class ListSSHPublicKeysRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class SSHPublicKeyMetadata(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Status: StatusTypeType
    UploadDate: datetime


# This class is the input for the 'list_server_certificate_tags' function.
class ListServerCertificateTagsRequest(BaseValidatorModel):
    ServerCertificateName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_server_certificates' function.
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


# This class is the input for the 'list_service_specific_credentials' function.
class ListServiceSpecificCredentialsRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    ServiceName: Optional[str] = None


class ServiceSpecificCredentialMetadata(BaseValidatorModel):
    UserName: str
    Status: StatusTypeType
    ServiceUserName: str
    CreateDate: datetime
    ServiceSpecificCredentialId: str
    ServiceName: str


# This class is the input for the 'list_signing_certificates' function.
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


# This class is the input for the 'list_user_policies' function.
class ListUserPoliciesRequest(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_user_tags' function.
class ListUserTagsRequest(BaseValidatorModel):
    UserName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_users' function.
class ListUsersRequest(BaseValidatorModel):
    PathPrefix: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_virtual_mfa_devices' function.
class ListVirtualMFADevicesRequest(BaseValidatorModel):
    AssignmentStatus: Optional[AssignmentStatusTypeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class PolicyDocumentStatement(BaseValidatorModel):
    Effect: str
    Resource: Union[List[str], str]
    Sid: str
    Action: Union[List[str], str]


class Position(BaseValidatorModel):
    Line: Optional[int] = None
    Column: Optional[int] = None


class PutGroupPolicyRequestGroupCreatePolicy(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str


class PutGroupPolicyRequestGroupPolicyPut(BaseValidatorModel):
    PolicyDocument: str


# This class is the input for the 'put_group_policy' function.
class PutGroupPolicyRequest(BaseValidatorModel):
    GroupName: str
    PolicyName: str
    PolicyDocument: str


# This class is the input for the 'put_role_permissions_boundary' function.
class PutRolePermissionsBoundaryRequest(BaseValidatorModel):
    RoleName: str
    PermissionsBoundary: str


class PutRolePolicyRequestRolePolicyPut(BaseValidatorModel):
    PolicyDocument: str


# This class is the input for the 'put_role_policy' function.
class PutRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyName: str
    PolicyDocument: str


# This class is the input for the 'put_user_permissions_boundary' function.
class PutUserPermissionsBoundaryRequest(BaseValidatorModel):
    UserName: str
    PermissionsBoundary: str


# This class is the input for the 'put_user_policy' function.
class PutUserPolicyRequest(BaseValidatorModel):
    UserName: str
    PolicyName: str
    PolicyDocument: str


class PutUserPolicyRequestUserCreatePolicy(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str


class PutUserPolicyRequestUserPolicyPut(BaseValidatorModel):
    PolicyDocument: str


# This class is the input for the 'remove_client_id_from_open_id_connect_provider' function.
class RemoveClientIDFromOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ClientID: str


class RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRole(BaseValidatorModel):
    RoleName: str


# This class is the input for the 'remove_role_from_instance_profile' function.
class RemoveRoleFromInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    RoleName: str


class RemoveUserFromGroupRequestGroupRemoveUser(BaseValidatorModel):
    UserName: str


# This class is the input for the 'remove_user_from_group' function.
class RemoveUserFromGroupRequest(BaseValidatorModel):
    GroupName: str
    UserName: str


class RemoveUserFromGroupRequestUserRemoveGroup(BaseValidatorModel):
    GroupName: str


# This class is the input for the 'reset_service_specific_credential' function.
class ResetServiceSpecificCredentialRequest(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    UserName: Optional[str] = None


class ResyncMFADeviceRequestMfaDeviceResync(BaseValidatorModel):
    AuthenticationCode1: str
    AuthenticationCode2: str


# This class is the input for the 'resync_mfa_device' function.
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


# This class is the input for the 'set_default_policy_version' function.
class SetDefaultPolicyVersionRequest(BaseValidatorModel):
    PolicyArn: str
    VersionId: str


# This class is the input for the 'set_security_token_service_preferences' function.
class SetSecurityTokenServicePreferencesRequest(BaseValidatorModel):
    GlobalEndpointTokenVersion: GlobalEndpointTokenVersionType


# This class is the input for the 'untag_instance_profile' function.
class UntagInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    TagKeys: List[str]


# This class is the input for the 'untag_mfa_device' function.
class UntagMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str
    TagKeys: List[str]


# This class is the input for the 'untag_open_id_connect_provider' function.
class UntagOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    TagKeys: List[str]


# This class is the input for the 'untag_policy' function.
class UntagPolicyRequest(BaseValidatorModel):
    PolicyArn: str
    TagKeys: List[str]


# This class is the input for the 'untag_role' function.
class UntagRoleRequest(BaseValidatorModel):
    RoleName: str
    TagKeys: List[str]


# This class is the input for the 'untag_saml_provider' function.
class UntagSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str
    TagKeys: List[str]


# This class is the input for the 'untag_server_certificate' function.
class UntagServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str
    TagKeys: List[str]


# This class is the input for the 'untag_user' function.
class UntagUserRequest(BaseValidatorModel):
    UserName: str
    TagKeys: List[str]


class UpdateAccessKeyRequestAccessKeyActivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestAccessKeyDeactivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestAccessKeyPairActivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateAccessKeyRequestAccessKeyPairDeactivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


# This class is the input for the 'update_access_key' function.
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


class UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicy(BaseValidatorModel):
    MinimumPasswordLength: Optional[int] = None
    RequireSymbols: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireUppercaseCharacters: Optional[bool] = None
    RequireLowercaseCharacters: Optional[bool] = None
    AllowUsersToChangePassword: Optional[bool] = None
    MaxPasswordAge: Optional[int] = None
    PasswordReusePrevention: Optional[int] = None
    HardExpiry: Optional[bool] = None


# This class is the input for the 'update_account_password_policy' function.
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


# This class is the input for the 'update_assume_role_policy' function.
class UpdateAssumeRolePolicyRequest(BaseValidatorModel):
    RoleName: str
    PolicyDocument: str


class UpdateGroupRequestGroupUpdate(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None


# This class is the input for the 'update_group' function.
class UpdateGroupRequest(BaseValidatorModel):
    GroupName: str
    NewPath: Optional[str] = None
    NewGroupName: Optional[str] = None


class UpdateLoginProfileRequestLoginProfileUpdate(BaseValidatorModel):
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


# This class is the input for the 'update_login_profile' function.
class UpdateLoginProfileRequest(BaseValidatorModel):
    UserName: str
    Password: Optional[str] = None
    PasswordResetRequired: Optional[bool] = None


# This class is the input for the 'update_open_id_connect_provider_thumbprint' function.
class UpdateOpenIDConnectProviderThumbprintRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    ThumbprintList: List[str]


# This class is the input for the 'update_role_description' function.
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


# This class is the input for the 'update_saml_provider' function.
class UpdateSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str
    SAMLMetadataDocument: Optional[str] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None
    RemovePrivateKey: Optional[str] = None


# This class is the input for the 'update_ssh_public_key' function.
class UpdateSSHPublicKeyRequest(BaseValidatorModel):
    UserName: str
    SSHPublicKeyId: str
    Status: StatusTypeType


class UpdateServerCertificateRequestServerCertificateUpdate(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None


# This class is the input for the 'update_server_certificate' function.
class UpdateServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str
    NewPath: Optional[str] = None
    NewServerCertificateName: Optional[str] = None


# This class is the input for the 'update_service_specific_credential' function.
class UpdateServiceSpecificCredentialRequest(BaseValidatorModel):
    ServiceSpecificCredentialId: str
    Status: StatusTypeType
    UserName: Optional[str] = None


class UpdateSigningCertificateRequestSigningCertificateActivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


class UpdateSigningCertificateRequestSigningCertificateDeactivate(BaseValidatorModel):
    Status: Optional[StatusTypeType] = None


# This class is the input for the 'update_signing_certificate' function.
class UpdateSigningCertificateRequest(BaseValidatorModel):
    CertificateId: str
    Status: StatusTypeType
    UserName: Optional[str] = None


# This class is the input for the 'update_user' function.
class UpdateUserRequest(BaseValidatorModel):
    UserName: str
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None


class UpdateUserRequestUserUpdate(BaseValidatorModel):
    NewPath: Optional[str] = None
    NewUserName: Optional[str] = None


# This class is the input for the 'upload_ssh_public_key' function.
class UploadSSHPublicKeyRequest(BaseValidatorModel):
    UserName: str
    SSHPublicKeyBody: str


class UploadSigningCertificateRequestServiceResourceCreateSigningCertificate(BaseValidatorModel):
    CertificateBody: str
    UserName: Optional[str] = None


# This class is the input for the 'upload_signing_certificate' function.
class UploadSigningCertificateRequest(BaseValidatorModel):
    CertificateBody: str
    UserName: Optional[str] = None


# This class is the input for the 'simulate_custom_policy' function.
class SimulateCustomPolicyRequest(BaseValidatorModel):
    PolicyInputList: List[str]
    ActionNames: List[str]
    PermissionsBoundaryPolicyInputList: Optional[List[str]] = None
    ResourceArns: Optional[List[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[List[ContextEntry]] = None
    ResourceHandlingOption: Optional[str] = None
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'simulate_principal_policy' function.
class SimulatePrincipalPolicyRequest(BaseValidatorModel):
    PolicySourceArn: str
    ActionNames: List[str]
    PolicyInputList: Optional[List[str]] = None
    PermissionsBoundaryPolicyInputList: Optional[List[str]] = None
    ResourceArns: Optional[List[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[List[ContextEntry]] = None
    ResourceHandlingOption: Optional[str] = None
    MaxItems: Optional[int] = None
    Marker: Optional[str] = None


# This class is the output for the 'create_access_key' function.
class CreateAccessKeyResponse(BaseValidatorModel):
    AccessKey: AccessKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service_linked_role' function.
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


# This class is the output for the 'update_user' function.
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


# This class is the output for the 'generate_organizations_access_report' function.
class GenerateOrganizationsAccessReportResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'generate_service_last_accessed_details' function.
class GenerateServiceLastAccessedDetailsResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_access_key_last_used' function.
class GetAccessKeyLastUsedResponse(BaseValidatorModel):
    UserName: str
    AccessKeyLastUsed: AccessKeyLastUsed
    ResponseMetadata: ResponseMetadata


class GetAccountSummaryResponse(BaseValidatorModel):
    SummaryMap: Dict[SummaryKeyTypeType, int]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_context_keys_for_principal_policy' function.
class GetContextKeysForPolicyResponse(BaseValidatorModel):
    ContextKeyNames: List[str]
    ResponseMetadata: ResponseMetadata


class GetCredentialReportResponse(BaseValidatorModel):
    Content: bytes
    ReportFormat: Literal['text/csv']
    GeneratedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_mfa_device' function.
class GetMFADeviceResponse(BaseValidatorModel):
    UserName: str
    SerialNumber: str
    EnableDate: datetime
    Certifications: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_access_keys' function.
class ListAccessKeysResponse(BaseValidatorModel):
    AccessKeyMetadata: List[AccessKeyMetadata]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_account_aliases' function.
class ListAccountAliasesResponse(BaseValidatorModel):
    AccountAliases: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_attached_group_policies' function.
class ListAttachedGroupPoliciesResponse(BaseValidatorModel):
    AttachedPolicies: List[AttachedPolicy]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_attached_role_policies' function.
class ListAttachedRolePoliciesResponse(BaseValidatorModel):
    AttachedPolicies: List[AttachedPolicy]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_attached_user_policies' function.
class ListAttachedUserPoliciesResponse(BaseValidatorModel):
    AttachedPolicies: List[AttachedPolicy]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_group_policies' function.
class ListGroupPoliciesResponse(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class ListOrganizationsFeaturesResponse(BaseValidatorModel):
    OrganizationId: str
    EnabledFeatures: List[FeatureTypeType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_role_policies' function.
class ListRolePoliciesResponse(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_user_policies' function.
class ListUserPoliciesResponse(BaseValidatorModel):
    PolicyNames: List[str]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_saml_provider' function.
class UpdateSAMLProviderResponse(BaseValidatorModel):
    SAMLProviderArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_group' function.
class CreateGroupResponse(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_groups_for_user' function.
class ListGroupsForUserResponse(BaseValidatorModel):
    Groups: List[Group]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_groups' function.
class ListGroupsResponse(BaseValidatorModel):
    Groups: List[Group]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


class CreateInstanceProfileRequestServiceResourceCreateInstanceProfile(BaseValidatorModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_instance_profile' function.
class CreateInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    Path: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_open_id_connect_provider' function.
class CreateOpenIDConnectProviderRequest(BaseValidatorModel):
    Url: str
    ClientIDList: Optional[List[str]] = None
    ThumbprintList: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_open_id_connect_provider' function.
class CreateOpenIDConnectProviderResponse(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreatePolicyRequestServiceResourceCreatePolicy(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_policy' function.
class CreatePolicyRequest(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateRoleRequestServiceResourceCreateRole(BaseValidatorModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_role' function.
class CreateRoleRequest(BaseValidatorModel):
    RoleName: str
    AssumeRolePolicyDocument: str
    Path: Optional[str] = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateSAMLProviderRequestServiceResourceCreateSamlProvider(BaseValidatorModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[List[Tag]] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None


# This class is the input for the 'create_saml_provider' function.
class CreateSAMLProviderRequest(BaseValidatorModel):
    SAMLMetadataDocument: str
    Name: str
    Tags: Optional[List[Tag]] = None
    AssertionEncryptionMode: Optional[AssertionEncryptionModeTypeType] = None
    AddPrivateKey: Optional[str] = None


# This class is the output for the 'create_saml_provider' function.
class CreateSAMLProviderResponse(BaseValidatorModel):
    SAMLProviderArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateUserRequestServiceResourceCreateUser(BaseValidatorModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_user' function.
class CreateUserRequest(BaseValidatorModel):
    UserName: str
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateUserRequestUserCreate(BaseValidatorModel):
    Path: Optional[str] = None
    PermissionsBoundary: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDevice(BaseValidatorModel):
    VirtualMFADeviceName: str
    Path: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_virtual_mfa_device' function.
class CreateVirtualMFADeviceRequest(BaseValidatorModel):
    VirtualMFADeviceName: str
    Path: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'get_open_id_connect_provider' function.
class GetOpenIDConnectProviderResponse(BaseValidatorModel):
    Url: str
    ClientIDList: List[str]
    ThumbprintList: List[str]
    CreateDate: datetime
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_instance_profile_tags' function.
class ListInstanceProfileTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_mfa_device_tags' function.
class ListMFADeviceTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_open_id_connect_provider_tags' function.
class ListOpenIDConnectProviderTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_policy_tags' function.
class ListPolicyTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_role_tags' function.
class ListRoleTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_saml_provider_tags' function.
class ListSAMLProviderTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_server_certificate_tags' function.
class ListServerCertificateTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_user_tags' function.
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


# This class is the input for the 'tag_instance_profile' function.
class TagInstanceProfileRequest(BaseValidatorModel):
    InstanceProfileName: str
    Tags: List[Tag]


# This class is the input for the 'tag_mfa_device' function.
class TagMFADeviceRequest(BaseValidatorModel):
    SerialNumber: str
    Tags: List[Tag]


# This class is the input for the 'tag_open_id_connect_provider' function.
class TagOpenIDConnectProviderRequest(BaseValidatorModel):
    OpenIDConnectProviderArn: str
    Tags: List[Tag]


# This class is the input for the 'tag_policy' function.
class TagPolicyRequest(BaseValidatorModel):
    PolicyArn: str
    Tags: List[Tag]


# This class is the input for the 'tag_role' function.
class TagRoleRequest(BaseValidatorModel):
    RoleName: str
    Tags: List[Tag]


# This class is the input for the 'tag_saml_provider' function.
class TagSAMLProviderRequest(BaseValidatorModel):
    SAMLProviderArn: str
    Tags: List[Tag]


# This class is the input for the 'tag_server_certificate' function.
class TagServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str
    Tags: List[Tag]


# This class is the input for the 'tag_user' function.
class TagUserRequest(BaseValidatorModel):
    UserName: str
    Tags: List[Tag]


class UploadServerCertificateRequestServiceResourceCreateServerCertificate(BaseValidatorModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'upload_server_certificate' function.
class UploadServerCertificateRequest(BaseValidatorModel):
    ServerCertificateName: str
    CertificateBody: str
    PrivateKey: str
    Path: Optional[str] = None
    CertificateChain: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class User(BaseValidatorModel):
    Path: str
    UserName: str
    UserId: str
    Arn: str
    CreateDate: datetime
    PasswordLastUsed: Optional[datetime] = None
    PermissionsBoundary: Optional[AttachedPermissionsBoundary] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_login_profile' function.
class CreateLoginProfileResponse(BaseValidatorModel):
    LoginProfile: LoginProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_login_profile' function.
class GetLoginProfileResponse(BaseValidatorModel):
    LoginProfile: LoginProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service_specific_credential' function.
class CreateServiceSpecificCredentialResponse(BaseValidatorModel):
    ServiceSpecificCredential: ServiceSpecificCredential
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_service_specific_credential' function.
class ResetServiceSpecificCredentialResponse(BaseValidatorModel):
    ServiceSpecificCredential: ServiceSpecificCredential
    ResponseMetadata: ResponseMetadata


class DeletionTaskFailureReasonType(BaseValidatorModel):
    Reason: Optional[str] = None
    RoleUsageList: Optional[List[RoleUsageType]] = None


class EntityDetails(BaseValidatorModel):
    EntityInfo: EntityInfo
    LastAuthenticated: Optional[datetime] = None


# This class is the output for the 'get_organizations_access_report' function.
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
    Filter: Optional[List[EntityTypeType]] = None
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
    PolicyInputList: List[str]
    ActionNames: List[str]
    PermissionsBoundaryPolicyInputList: Optional[List[str]] = None
    ResourceArns: Optional[List[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[List[ContextEntry]] = None
    ResourceHandlingOption: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SimulatePrincipalPolicyRequestPaginate(BaseValidatorModel):
    PolicySourceArn: str
    ActionNames: List[str]
    PolicyInputList: Optional[List[str]] = None
    PermissionsBoundaryPolicyInputList: Optional[List[str]] = None
    ResourceArns: Optional[List[str]] = None
    ResourcePolicy: Optional[str] = None
    ResourceOwner: Optional[str] = None
    CallerArn: Optional[str] = None
    ContextEntries: Optional[List[ContextEntry]] = None
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


# This class is the output for the 'get_saml_provider' function.
class GetSAMLProviderResponse(BaseValidatorModel):
    SAMLProviderUUID: str
    SAMLMetadataDocument: str
    CreateDate: datetime
    ValidUntil: datetime
    Tags: List[Tag]
    AssertionEncryptionMode: AssertionEncryptionModeTypeType
    PrivateKeyList: List[SAMLPrivateKey]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ssh_public_key' function.
class GetSSHPublicKeyResponse(BaseValidatorModel):
    SSHPublicKey: SSHPublicKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upload_ssh_public_key' function.
class UploadSSHPublicKeyResponse(BaseValidatorModel):
    SSHPublicKey: SSHPublicKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_entities_for_policy' function.
class ListEntitiesForPolicyResponse(BaseValidatorModel):
    PolicyGroups: List[PolicyGroup]
    PolicyUsers: List[PolicyUser]
    PolicyRoles: List[PolicyRole]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_mfa_devices' function.
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


# This class is the output for the 'list_ssh_public_keys' function.
class ListSSHPublicKeysResponse(BaseValidatorModel):
    SSHPublicKeys: List[SSHPublicKeyMetadata]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_server_certificates' function.
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


# This class is the output for the 'upload_server_certificate' function.
class UploadServerCertificateResponse(BaseValidatorModel):
    ServerCertificateMetadata: ServerCertificateMetadata
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_service_specific_credentials' function.
class ListServiceSpecificCredentialsResponse(BaseValidatorModel):
    ServiceSpecificCredentials: List[ServiceSpecificCredentialMetadata]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_signing_certificates' function.
class ListSigningCertificatesResponse(BaseValidatorModel):
    Certificates: List[SigningCertificate]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upload_signing_certificate' function.
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


class ServiceLastAccessed(BaseValidatorModel):
    ServiceName: str
    ServiceNamespace: str
    LastAuthenticated: Optional[datetime] = None
    LastAuthenticatedEntity: Optional[str] = None
    LastAuthenticatedRegion: Optional[str] = None
    TotalAuthenticatedEntities: Optional[int] = None
    TrackedActionsLastAccessed: Optional[List[TrackedActionLastAccessed]] = None


# This class is the output for the 'create_policy' function.
class CreatePolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_policy' function.
class GetPolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_policies' function.
class ListPoliciesResponse(BaseValidatorModel):
    Policies: List[Policy]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user' function.
class CreateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_group' function.
class GetGroupResponse(BaseValidatorModel):
    Group: Group
    Users: List[User]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_user' function.
class GetUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_users' function.
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


# This class is the output for the 'get_service_linked_role_deletion_status' function.
class GetServiceLinkedRoleDeletionStatusResponse(BaseValidatorModel):
    Status: DeletionTaskStatusTypeType
    Reason: DeletionTaskFailureReasonType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_last_accessed_details_with_entities' function.
class GetServiceLastAccessedDetailsWithEntitiesResponse(BaseValidatorModel):
    JobStatus: JobStatusTypeType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    EntityDetailsList: List[EntityDetails]
    IsTruncated: bool
    Marker: str
    Error: ErrorDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_policies_granting_service_access' function.
class ListPoliciesGrantingServiceAccessResponse(BaseValidatorModel):
    PoliciesGrantingServiceAccess: List[ListPoliciesGrantingServiceAccessEntry]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_server_certificate' function.
class GetServerCertificateResponse(BaseValidatorModel):
    ServerCertificate: ServerCertificate
    ResponseMetadata: ResponseMetadata

PolicyDocument = Union[str, PolicyDocumentDict]


class ResourceSpecificResult(BaseValidatorModel):
    EvalResourceName: str
    EvalResourceDecision: PolicyEvaluationDecisionTypeType
    MatchedStatements: Optional[List[Statement]] = None
    MissingContextValues: Optional[List[str]] = None
    EvalDecisionDetails: Optional[Dict[str, PolicyEvaluationDecisionTypeType]] = None
    PermissionsBoundaryDecisionDetail: Optional[PermissionsBoundaryDecisionDetail] = None


# This class is the output for the 'get_service_last_accessed_details' function.
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


# This class is the output for the 'create_virtual_mfa_device' function.
class CreateVirtualMFADeviceResponse(BaseValidatorModel):
    VirtualMFADevice: VirtualMFADevice
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_virtual_mfa_devices' function.
class ListVirtualMFADevicesResponse(BaseValidatorModel):
    VirtualMFADevices: List[VirtualMFADevice]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_group_policy' function.
class GetGroupPolicyResponse(BaseValidatorModel):
    GroupName: str
    PolicyName: str
    PolicyDocument: PolicyDocument
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_role_policy' function.
class GetRolePolicyResponse(BaseValidatorModel):
    RoleName: str
    PolicyName: str
    PolicyDocument: PolicyDocument
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_user_policy' function.
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


# This class is the output for the 'create_policy_version' function.
class CreatePolicyVersionResponse(BaseValidatorModel):
    PolicyVersion: PolicyVersion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_policy_version' function.
class GetPolicyVersionResponse(BaseValidatorModel):
    PolicyVersion: PolicyVersion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_policy_versions' function.
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


# This class is the output for the 'create_role' function.
class CreateRoleResponse(BaseValidatorModel):
    Role: Role
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service_linked_role' function.
class CreateServiceLinkedRoleResponse(BaseValidatorModel):
    Role: Role
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_role' function.
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


# This class is the output for the 'list_roles' function.
class ListRolesResponse(BaseValidatorModel):
    Roles: List[Role]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_role_description' function.
class UpdateRoleDescriptionResponse(BaseValidatorModel):
    Role: Role
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'simulate_principal_policy' function.
class SimulatePolicyResponse(BaseValidatorModel):
    EvaluationResults: List[EvaluationResult]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_instance_profile' function.
class CreateInstanceProfileResponse(BaseValidatorModel):
    InstanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_profile' function.
class GetInstanceProfileResponse(BaseValidatorModel):
    InstanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_instance_profiles_for_role' function.
class ListInstanceProfilesForRoleResponse(BaseValidatorModel):
    InstanceProfiles: List[InstanceProfile]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_instance_profiles' function.
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


# This class is the output for the 'get_account_authorization_details' function.
class GetAccountAuthorizationDetailsResponse(BaseValidatorModel):
    UserDetailList: List[UserDetail]
    GroupDetailList: List[GroupDetail]
    RoleDetailList: List[RoleDetail]
    Policies: List[ManagedPolicyDetail]
    IsTruncated: bool
    Marker: str
    ResponseMetadata: ResponseMetadata
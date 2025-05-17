from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.workmail.workmail_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessControlRule(BaseValidatorModel):
    Name: Optional[str] = None
    Effect: Optional[AccessControlRuleEffectType] = None
    Description: Optional[str] = None
    IpRanges: Optional[List[str]] = None
    NotIpRanges: Optional[List[str]] = None
    Actions: Optional[List[str]] = None
    NotActions: Optional[List[str]] = None
    UserIds: Optional[List[str]] = None
    NotUserIds: Optional[List[str]] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None
    ImpersonationRoleIds: Optional[List[str]] = None
    NotImpersonationRoleIds: Optional[List[str]] = None


class AssociateDelegateToResourceRequest(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    EntityId: str


class AssociateMemberToGroupRequest(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    MemberId: str


# This class is the input for the 'assume_impersonation_role' function.
class AssumeImpersonationRoleRequest(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class LambdaAvailabilityProvider(BaseValidatorModel):
    LambdaArn: str


class RedactedEwsAvailabilityProvider(BaseValidatorModel):
    EwsEndpoint: Optional[str] = None
    EwsUsername: Optional[str] = None


class BookingOptions(BaseValidatorModel):
    AutoAcceptRequests: Optional[bool] = None
    AutoDeclineRecurringRequests: Optional[bool] = None
    AutoDeclineConflictingRequests: Optional[bool] = None


class CancelMailboxExportJobRequest(BaseValidatorModel):
    ClientToken: str
    JobId: str
    OrganizationId: str


class CreateAliasRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Alias: str


class EwsAvailabilityProvider(BaseValidatorModel):
    EwsEndpoint: str
    EwsUsername: str
    EwsPassword: str


# This class is the input for the 'create_group' function.
class CreateGroupRequest(BaseValidatorModel):
    OrganizationId: str
    Name: str
    HiddenFromGlobalAddressList: Optional[bool] = None


# This class is the input for the 'create_identity_center_application' function.
class CreateIdentityCenterApplicationRequest(BaseValidatorModel):
    Name: str
    InstanceArn: str
    ClientToken: Optional[str] = None


# This class is the input for the 'create_mobile_device_access_rule' function.
class CreateMobileDeviceAccessRuleRequest(BaseValidatorModel):
    OrganizationId: str
    Name: str
    Effect: MobileDeviceAccessRuleEffectType
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DeviceTypes: Optional[List[str]] = None
    NotDeviceTypes: Optional[List[str]] = None
    DeviceModels: Optional[List[str]] = None
    NotDeviceModels: Optional[List[str]] = None
    DeviceOperatingSystems: Optional[List[str]] = None
    NotDeviceOperatingSystems: Optional[List[str]] = None
    DeviceUserAgents: Optional[List[str]] = None
    NotDeviceUserAgents: Optional[List[str]] = None


class Domain(BaseValidatorModel):
    DomainName: str
    HostedZoneId: Optional[str] = None


# This class is the input for the 'create_resource' function.
class CreateResourceRequest(BaseValidatorModel):
    OrganizationId: str
    Name: str
    Type: ResourceTypeType
    Description: Optional[str] = None
    HiddenFromGlobalAddressList: Optional[bool] = None


# This class is the input for the 'create_user' function.
class CreateUserRequest(BaseValidatorModel):
    OrganizationId: str
    Name: str
    DisplayName: str
    Password: Optional[str] = None
    Role: Optional[UserRoleType] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    HiddenFromGlobalAddressList: Optional[bool] = None
    IdentityProviderUserId: Optional[str] = None


class Delegate(BaseValidatorModel):
    Id: str
    Type: MemberTypeType


class DeleteAccessControlRuleRequest(BaseValidatorModel):
    OrganizationId: str
    Name: str


class DeleteAliasRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Alias: str


class DeleteAvailabilityConfigurationRequest(BaseValidatorModel):
    OrganizationId: str
    DomainName: str


class DeleteEmailMonitoringConfigurationRequest(BaseValidatorModel):
    OrganizationId: str


class DeleteGroupRequest(BaseValidatorModel):
    OrganizationId: str
    GroupId: str


class DeleteIdentityCenterApplicationRequest(BaseValidatorModel):
    ApplicationArn: str


class DeleteIdentityProviderConfigurationRequest(BaseValidatorModel):
    OrganizationId: str


class DeleteImpersonationRoleRequest(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str


class DeleteMailboxPermissionsRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    GranteeId: str


class DeleteMobileDeviceAccessOverrideRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str


class DeleteMobileDeviceAccessRuleRequest(BaseValidatorModel):
    OrganizationId: str
    MobileDeviceAccessRuleId: str


# This class is the input for the 'delete_organization' function.
class DeleteOrganizationRequest(BaseValidatorModel):
    OrganizationId: str
    DeleteDirectory: bool
    ClientToken: Optional[str] = None
    ForceDelete: Optional[bool] = None
    DeleteIdentityCenterApplication: Optional[bool] = None


class DeletePersonalAccessTokenRequest(BaseValidatorModel):
    OrganizationId: str
    PersonalAccessTokenId: str


class DeleteResourceRequest(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str


class DeleteRetentionPolicyRequest(BaseValidatorModel):
    OrganizationId: str
    Id: str


class DeleteUserRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str


class DeregisterFromWorkMailRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str


class DeregisterMailDomainRequest(BaseValidatorModel):
    OrganizationId: str
    DomainName: str


# This class is the input for the 'describe_email_monitoring_configuration' function.
class DescribeEmailMonitoringConfigurationRequest(BaseValidatorModel):
    OrganizationId: str


# This class is the input for the 'describe_entity' function.
class DescribeEntityRequest(BaseValidatorModel):
    OrganizationId: str
    Email: str


# This class is the input for the 'describe_group' function.
class DescribeGroupRequest(BaseValidatorModel):
    OrganizationId: str
    GroupId: str


# This class is the input for the 'describe_identity_provider_configuration' function.
class DescribeIdentityProviderConfigurationRequest(BaseValidatorModel):
    OrganizationId: str


class IdentityCenterConfiguration(BaseValidatorModel):
    InstanceArn: str
    ApplicationArn: str


class PersonalAccessTokenConfiguration(BaseValidatorModel):
    Status: PersonalAccessTokenConfigurationStatusType
    LifetimeInDays: Optional[int] = None


# This class is the input for the 'describe_inbound_dmarc_settings' function.
class DescribeInboundDmarcSettingsRequest(BaseValidatorModel):
    OrganizationId: str


# This class is the input for the 'describe_mailbox_export_job' function.
class DescribeMailboxExportJobRequest(BaseValidatorModel):
    JobId: str
    OrganizationId: str


# This class is the input for the 'describe_organization' function.
class DescribeOrganizationRequest(BaseValidatorModel):
    OrganizationId: str


# This class is the input for the 'describe_resource' function.
class DescribeResourceRequest(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str


# This class is the input for the 'describe_user' function.
class DescribeUserRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str


class DisassociateDelegateFromResourceRequest(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    EntityId: str


class DisassociateMemberFromGroupRequest(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    MemberId: str


class DnsRecord(BaseValidatorModel):
    Type: Optional[str] = None
    Hostname: Optional[str] = None
    Value: Optional[str] = None


class FolderConfiguration(BaseValidatorModel):
    Name: FolderNameType
    Action: RetentionActionType
    Period: Optional[int] = None


# This class is the input for the 'get_access_control_effect' function.
class GetAccessControlEffectRequest(BaseValidatorModel):
    OrganizationId: str
    IpAddress: str
    Action: str
    UserId: Optional[str] = None
    ImpersonationRoleId: Optional[str] = None


# This class is the input for the 'get_default_retention_policy' function.
class GetDefaultRetentionPolicyRequest(BaseValidatorModel):
    OrganizationId: str


# This class is the input for the 'get_impersonation_role_effect' function.
class GetImpersonationRoleEffectRequest(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str
    TargetUser: str


class ImpersonationMatchedRule(BaseValidatorModel):
    ImpersonationRuleId: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'get_impersonation_role' function.
class GetImpersonationRoleRequest(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str


class ImpersonationRuleOutput(BaseValidatorModel):
    ImpersonationRuleId: str
    Effect: AccessEffectType
    Name: Optional[str] = None
    Description: Optional[str] = None
    TargetUsers: Optional[List[str]] = None
    NotTargetUsers: Optional[List[str]] = None


# This class is the input for the 'get_mail_domain' function.
class GetMailDomainRequest(BaseValidatorModel):
    OrganizationId: str
    DomainName: str


# This class is the input for the 'get_mailbox_details' function.
class GetMailboxDetailsRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str


# This class is the input for the 'get_mobile_device_access_effect' function.
class GetMobileDeviceAccessEffectRequest(BaseValidatorModel):
    OrganizationId: str
    DeviceType: Optional[str] = None
    DeviceModel: Optional[str] = None
    DeviceOperatingSystem: Optional[str] = None
    DeviceUserAgent: Optional[str] = None


class MobileDeviceAccessMatchedRule(BaseValidatorModel):
    MobileDeviceAccessRuleId: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'get_mobile_device_access_override' function.
class GetMobileDeviceAccessOverrideRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str


# This class is the input for the 'get_personal_access_token_metadata' function.
class GetPersonalAccessTokenMetadataRequest(BaseValidatorModel):
    OrganizationId: str
    PersonalAccessTokenId: str


class GroupIdentifier(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None


class Group(BaseValidatorModel):
    Id: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[EntityStateType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None


class ImpersonationRole(BaseValidatorModel):
    ImpersonationRoleId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ImpersonationRoleTypeType] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None


class ImpersonationRule(BaseValidatorModel):
    ImpersonationRuleId: str
    Effect: AccessEffectType
    Name: Optional[str] = None
    Description: Optional[str] = None
    TargetUsers: Optional[List[str]] = None
    NotTargetUsers: Optional[List[str]] = None


# This class is the input for the 'list_access_control_rules' function.
class ListAccessControlRulesRequest(BaseValidatorModel):
    OrganizationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_aliases' function.
class ListAliasesRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_availability_configurations' function.
class ListAvailabilityConfigurationsRequest(BaseValidatorModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_group_members' function.
class ListGroupMembersRequest(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Member(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[MemberTypeType] = None
    State: Optional[EntityStateType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None


class ListGroupsFilters(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None


class ListGroupsForEntityFilters(BaseValidatorModel):
    GroupNamePrefix: Optional[str] = None


# This class is the input for the 'list_impersonation_roles' function.
class ListImpersonationRolesRequest(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_mail_domains' function.
class ListMailDomainsRequest(BaseValidatorModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MailDomainSummary(BaseValidatorModel):
    DomainName: Optional[str] = None
    DefaultDomain: Optional[bool] = None


# This class is the input for the 'list_mailbox_export_jobs' function.
class ListMailboxExportJobsRequest(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MailboxExportJob(BaseValidatorModel):
    JobId: Optional[str] = None
    EntityId: Optional[str] = None
    Description: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3Path: Optional[str] = None
    EstimatedProgress: Optional[int] = None
    State: Optional[MailboxExportJobStateType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


# This class is the input for the 'list_mailbox_permissions' function.
class ListMailboxPermissionsRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Permission(BaseValidatorModel):
    GranteeId: str
    GranteeType: MemberTypeType
    PermissionValues: List[PermissionTypeType]


# This class is the input for the 'list_mobile_device_access_overrides' function.
class ListMobileDeviceAccessOverridesRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: Optional[str] = None
    DeviceId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MobileDeviceAccessOverride(BaseValidatorModel):
    UserId: Optional[str] = None
    DeviceId: Optional[str] = None
    Effect: Optional[MobileDeviceAccessRuleEffectType] = None
    Description: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None


# This class is the input for the 'list_mobile_device_access_rules' function.
class ListMobileDeviceAccessRulesRequest(BaseValidatorModel):
    OrganizationId: str


class MobileDeviceAccessRule(BaseValidatorModel):
    MobileDeviceAccessRuleId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Effect: Optional[MobileDeviceAccessRuleEffectType] = None
    DeviceTypes: Optional[List[str]] = None
    NotDeviceTypes: Optional[List[str]] = None
    DeviceModels: Optional[List[str]] = None
    NotDeviceModels: Optional[List[str]] = None
    DeviceOperatingSystems: Optional[List[str]] = None
    NotDeviceOperatingSystems: Optional[List[str]] = None
    DeviceUserAgents: Optional[List[str]] = None
    NotDeviceUserAgents: Optional[List[str]] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None


# This class is the input for the 'list_organizations' function.
class ListOrganizationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OrganizationSummary(BaseValidatorModel):
    OrganizationId: Optional[str] = None
    Alias: Optional[str] = None
    DefaultMailDomain: Optional[str] = None
    ErrorMessage: Optional[str] = None
    State: Optional[str] = None


# This class is the input for the 'list_personal_access_tokens' function.
class ListPersonalAccessTokensRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PersonalAccessTokenSummary(BaseValidatorModel):
    PersonalAccessTokenId: Optional[str] = None
    UserId: Optional[str] = None
    Name: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateLastUsed: Optional[datetime] = None
    ExpiresTime: Optional[datetime] = None
    Scopes: Optional[List[str]] = None


# This class is the input for the 'list_resource_delegates' function.
class ListResourceDelegatesRequest(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListResourcesFilters(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None


class Resource(BaseValidatorModel):
    Id: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ResourceTypeType] = None
    State: Optional[EntityStateType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None
    Description: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ListUsersFilters(BaseValidatorModel):
    UsernamePrefix: Optional[str] = None
    DisplayNamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None
    IdentityProviderUserIdPrefix: Optional[str] = None


class User(BaseValidatorModel):
    Id: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    DisplayName: Optional[str] = None
    State: Optional[EntityStateType] = None
    UserRole: Optional[UserRoleType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None
    IdentityProviderUserId: Optional[str] = None
    IdentityProviderIdentityStoreId: Optional[str] = None


class PutAccessControlRuleRequest(BaseValidatorModel):
    Name: str
    Effect: AccessControlRuleEffectType
    Description: str
    OrganizationId: str
    IpRanges: Optional[List[str]] = None
    NotIpRanges: Optional[List[str]] = None
    Actions: Optional[List[str]] = None
    NotActions: Optional[List[str]] = None
    UserIds: Optional[List[str]] = None
    NotUserIds: Optional[List[str]] = None
    ImpersonationRoleIds: Optional[List[str]] = None
    NotImpersonationRoleIds: Optional[List[str]] = None


class PutEmailMonitoringConfigurationRequest(BaseValidatorModel):
    OrganizationId: str
    RoleArn: str
    LogGroupArn: str


class PutInboundDmarcSettingsRequest(BaseValidatorModel):
    OrganizationId: str
    Enforced: bool


class PutMailboxPermissionsRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    GranteeId: str
    PermissionValues: List[PermissionTypeType]


class PutMobileDeviceAccessOverrideRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: Optional[str] = None


class RegisterMailDomainRequest(BaseValidatorModel):
    OrganizationId: str
    DomainName: str
    ClientToken: Optional[str] = None


class RegisterToWorkMailRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Email: str


class ResetPasswordRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    Password: str


# This class is the input for the 'start_mailbox_export_job' function.
class StartMailboxExportJobRequest(BaseValidatorModel):
    ClientToken: str
    OrganizationId: str
    EntityId: str
    RoleArn: str
    KmsKeyArn: str
    S3BucketName: str
    S3Prefix: str
    Description: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class UpdateDefaultMailDomainRequest(BaseValidatorModel):
    OrganizationId: str
    DomainName: str


class UpdateGroupRequest(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    HiddenFromGlobalAddressList: Optional[bool] = None


class UpdateMailboxQuotaRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    MailboxQuota: int


class UpdateMobileDeviceAccessRuleRequest(BaseValidatorModel):
    OrganizationId: str
    MobileDeviceAccessRuleId: str
    Name: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: Optional[str] = None
    DeviceTypes: Optional[List[str]] = None
    NotDeviceTypes: Optional[List[str]] = None
    DeviceModels: Optional[List[str]] = None
    NotDeviceModels: Optional[List[str]] = None
    DeviceOperatingSystems: Optional[List[str]] = None
    NotDeviceOperatingSystems: Optional[List[str]] = None
    DeviceUserAgents: Optional[List[str]] = None
    NotDeviceUserAgents: Optional[List[str]] = None


class UpdatePrimaryEmailAddressRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Email: str


class UpdateUserRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    Role: Optional[UserRoleType] = None
    DisplayName: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    HiddenFromGlobalAddressList: Optional[bool] = None
    Initials: Optional[str] = None
    Telephone: Optional[str] = None
    Street: Optional[str] = None
    JobTitle: Optional[str] = None
    City: Optional[str] = None
    Company: Optional[str] = None
    ZipCode: Optional[str] = None
    Department: Optional[str] = None
    Country: Optional[str] = None
    Office: Optional[str] = None
    IdentityProviderUserId: Optional[str] = None


# This class is the output for the 'assume_impersonation_role' function.
class AssumeImpersonationRoleResponse(BaseValidatorModel):
    Token: str
    ExpiresIn: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_group' function.
class CreateGroupResponse(BaseValidatorModel):
    GroupId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_identity_center_application' function.
class CreateIdentityCenterApplicationResponse(BaseValidatorModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_impersonation_role' function.
class CreateImpersonationRoleResponse(BaseValidatorModel):
    ImpersonationRoleId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_mobile_device_access_rule' function.
class CreateMobileDeviceAccessRuleResponse(BaseValidatorModel):
    MobileDeviceAccessRuleId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_organization' function.
class CreateOrganizationResponse(BaseValidatorModel):
    OrganizationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_resource' function.
class CreateResourceResponse(BaseValidatorModel):
    ResourceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user' function.
class CreateUserResponse(BaseValidatorModel):
    UserId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_organization' function.
class DeleteOrganizationResponse(BaseValidatorModel):
    OrganizationId: str
    State: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_email_monitoring_configuration' function.
class DescribeEmailMonitoringConfigurationResponse(BaseValidatorModel):
    RoleArn: str
    LogGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_entity' function.
class DescribeEntityResponse(BaseValidatorModel):
    EntityId: str
    Name: str
    Type: EntityTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_group' function.
class DescribeGroupResponse(BaseValidatorModel):
    GroupId: str
    Name: str
    Email: str
    State: EntityStateType
    EnabledDate: datetime
    DisabledDate: datetime
    HiddenFromGlobalAddressList: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_inbound_dmarc_settings' function.
class DescribeInboundDmarcSettingsResponse(BaseValidatorModel):
    Enforced: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_mailbox_export_job' function.
class DescribeMailboxExportJobResponse(BaseValidatorModel):
    EntityId: str
    Description: str
    RoleArn: str
    KmsKeyArn: str
    S3BucketName: str
    S3Prefix: str
    S3Path: str
    EstimatedProgress: int
    State: MailboxExportJobStateType
    ErrorInfo: str
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_organization' function.
class DescribeOrganizationResponse(BaseValidatorModel):
    OrganizationId: str
    Alias: str
    State: str
    DirectoryId: str
    DirectoryType: str
    DefaultMailDomain: str
    CompletedDate: datetime
    ErrorMessage: str
    ARN: str
    MigrationAdmin: str
    InteroperabilityEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_user' function.
class DescribeUserResponse(BaseValidatorModel):
    UserId: str
    Name: str
    Email: str
    DisplayName: str
    State: EntityStateType
    UserRole: UserRoleType
    EnabledDate: datetime
    DisabledDate: datetime
    MailboxProvisionedDate: datetime
    MailboxDeprovisionedDate: datetime
    FirstName: str
    LastName: str
    HiddenFromGlobalAddressList: bool
    Initials: str
    Telephone: str
    Street: str
    JobTitle: str
    City: str
    Company: str
    ZipCode: str
    Department: str
    Country: str
    Office: str
    IdentityProviderUserId: str
    IdentityProviderIdentityStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_access_control_effect' function.
class GetAccessControlEffectResponse(BaseValidatorModel):
    Effect: AccessControlRuleEffectType
    MatchedRules: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_mailbox_details' function.
class GetMailboxDetailsResponse(BaseValidatorModel):
    MailboxQuota: int
    MailboxSize: float
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_mobile_device_access_override' function.
class GetMobileDeviceAccessOverrideResponse(BaseValidatorModel):
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: str
    DateCreated: datetime
    DateModified: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_personal_access_token_metadata' function.
class GetPersonalAccessTokenMetadataResponse(BaseValidatorModel):
    PersonalAccessTokenId: str
    UserId: str
    Name: str
    DateCreated: datetime
    DateLastUsed: datetime
    ExpiresTime: datetime
    Scopes: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_access_control_rules' function.
class ListAccessControlRulesResponse(BaseValidatorModel):
    Rules: List[AccessControlRule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_aliases' function.
class ListAliasesResponse(BaseValidatorModel):
    Aliases: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_mailbox_export_job' function.
class StartMailboxExportJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_availability_configuration' function.
class TestAvailabilityConfigurationResponse(BaseValidatorModel):
    TestPassed: bool
    FailureReason: str
    ResponseMetadata: ResponseMetadata


class AvailabilityConfiguration(BaseValidatorModel):
    DomainName: Optional[str] = None
    ProviderType: Optional[AvailabilityProviderTypeType] = None
    EwsProvider: Optional[RedactedEwsAvailabilityProvider] = None
    LambdaProvider: Optional[LambdaAvailabilityProvider] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None


# This class is the output for the 'describe_resource' function.
class DescribeResourceResponse(BaseValidatorModel):
    ResourceId: str
    Email: str
    Name: str
    Type: ResourceTypeType
    BookingOptions: BookingOptions
    State: EntityStateType
    EnabledDate: datetime
    DisabledDate: datetime
    Description: str
    HiddenFromGlobalAddressList: bool
    ResponseMetadata: ResponseMetadata


class UpdateResourceRequest(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    Name: Optional[str] = None
    BookingOptions: Optional[BookingOptions] = None
    Description: Optional[str] = None
    Type: Optional[ResourceTypeType] = None
    HiddenFromGlobalAddressList: Optional[bool] = None


class CreateAvailabilityConfigurationRequest(BaseValidatorModel):
    OrganizationId: str
    DomainName: str
    ClientToken: Optional[str] = None
    EwsProvider: Optional[EwsAvailabilityProvider] = None
    LambdaProvider: Optional[LambdaAvailabilityProvider] = None


# This class is the input for the 'test_availability_configuration' function.
class TestAvailabilityConfigurationRequest(BaseValidatorModel):
    OrganizationId: str
    DomainName: Optional[str] = None
    EwsProvider: Optional[EwsAvailabilityProvider] = None
    LambdaProvider: Optional[LambdaAvailabilityProvider] = None


class UpdateAvailabilityConfigurationRequest(BaseValidatorModel):
    OrganizationId: str
    DomainName: str
    EwsProvider: Optional[EwsAvailabilityProvider] = None
    LambdaProvider: Optional[LambdaAvailabilityProvider] = None


# This class is the input for the 'create_organization' function.
class CreateOrganizationRequest(BaseValidatorModel):
    Alias: str
    DirectoryId: Optional[str] = None
    ClientToken: Optional[str] = None
    Domains: Optional[List[Domain]] = None
    KmsKeyArn: Optional[str] = None
    EnableInteroperability: Optional[bool] = None


# This class is the output for the 'list_resource_delegates' function.
class ListResourceDelegatesResponse(BaseValidatorModel):
    Delegates: List[Delegate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_identity_provider_configuration' function.
class DescribeIdentityProviderConfigurationResponse(BaseValidatorModel):
    AuthenticationMode: IdentityProviderAuthenticationModeType
    IdentityCenterConfiguration: IdentityCenterConfiguration
    PersonalAccessTokenConfiguration: PersonalAccessTokenConfiguration
    ResponseMetadata: ResponseMetadata


class PutIdentityProviderConfigurationRequest(BaseValidatorModel):
    OrganizationId: str
    AuthenticationMode: IdentityProviderAuthenticationModeType
    IdentityCenterConfiguration: IdentityCenterConfiguration
    PersonalAccessTokenConfiguration: PersonalAccessTokenConfiguration


# This class is the output for the 'get_mail_domain' function.
class GetMailDomainResponse(BaseValidatorModel):
    Records: List[DnsRecord]
    IsTestDomain: bool
    IsDefault: bool
    OwnershipVerificationStatus: DnsRecordVerificationStatusType
    DkimVerificationStatus: DnsRecordVerificationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_default_retention_policy' function.
class GetDefaultRetentionPolicyResponse(BaseValidatorModel):
    Id: str
    Name: str
    Description: str
    FolderConfigurations: List[FolderConfiguration]
    ResponseMetadata: ResponseMetadata


class PutRetentionPolicyRequest(BaseValidatorModel):
    OrganizationId: str
    Name: str
    FolderConfigurations: List[FolderConfiguration]
    Id: Optional[str] = None
    Description: Optional[str] = None


# This class is the output for the 'get_impersonation_role_effect' function.
class GetImpersonationRoleEffectResponse(BaseValidatorModel):
    Type: ImpersonationRoleTypeType
    Effect: AccessEffectType
    MatchedRules: List[ImpersonationMatchedRule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_impersonation_role' function.
class GetImpersonationRoleResponse(BaseValidatorModel):
    ImpersonationRoleId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Description: str
    Rules: List[ImpersonationRuleOutput]
    DateCreated: datetime
    DateModified: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_mobile_device_access_effect' function.
class GetMobileDeviceAccessEffectResponse(BaseValidatorModel):
    Effect: MobileDeviceAccessRuleEffectType
    MatchedRules: List[MobileDeviceAccessMatchedRule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_groups_for_entity' function.
class ListGroupsForEntityResponse(BaseValidatorModel):
    Groups: List[GroupIdentifier]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_groups' function.
class ListGroupsResponse(BaseValidatorModel):
    Groups: List[Group]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_impersonation_roles' function.
class ListImpersonationRolesResponse(BaseValidatorModel):
    Roles: List[ImpersonationRole]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

ImpersonationRuleUnion = Union[ImpersonationRule, ImpersonationRuleOutput]


class ListAliasesRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAvailabilityConfigurationsRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupMembersRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMailboxPermissionsRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPersonalAccessTokensRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    UserId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceDelegatesRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_group_members' function.
class ListGroupMembersResponse(BaseValidatorModel):
    Members: List[Member]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupsRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListGroupsFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_groups' function.
class ListGroupsRequest(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListGroupsFilters] = None


# This class is the input for the 'list_groups_for_entity' function.
class ListGroupsForEntityRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Filters: Optional[ListGroupsForEntityFilters] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'list_mail_domains' function.
class ListMailDomainsResponse(BaseValidatorModel):
    MailDomains: List[MailDomainSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_mailbox_export_jobs' function.
class ListMailboxExportJobsResponse(BaseValidatorModel):
    Jobs: List[MailboxExportJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_mailbox_permissions' function.
class ListMailboxPermissionsResponse(BaseValidatorModel):
    Permissions: List[Permission]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_mobile_device_access_overrides' function.
class ListMobileDeviceAccessOverridesResponse(BaseValidatorModel):
    Overrides: List[MobileDeviceAccessOverride]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_mobile_device_access_rules' function.
class ListMobileDeviceAccessRulesResponse(BaseValidatorModel):
    Rules: List[MobileDeviceAccessRule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_organizations' function.
class ListOrganizationsResponse(BaseValidatorModel):
    OrganizationSummaries: List[OrganizationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_personal_access_tokens' function.
class ListPersonalAccessTokensResponse(BaseValidatorModel):
    PersonalAccessTokenSummaries: List[PersonalAccessTokenSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourcesRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListResourcesFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_resources' function.
class ListResourcesRequest(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListResourcesFilters] = None


# This class is the output for the 'list_resources' function.
class ListResourcesResponse(BaseValidatorModel):
    Resources: List[Resource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class ListUsersRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListUsersFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_users' function.
class ListUsersRequest(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListUsersFilters] = None


# This class is the output for the 'list_users' function.
class ListUsersResponse(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_availability_configurations' function.
class ListAvailabilityConfigurationsResponse(BaseValidatorModel):
    AvailabilityConfigurations: List[AvailabilityConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_impersonation_role' function.
class CreateImpersonationRoleRequest(BaseValidatorModel):
    OrganizationId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Rules: List[ImpersonationRuleUnion]
    ClientToken: Optional[str] = None
    Description: Optional[str] = None


class UpdateImpersonationRoleRequest(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Rules: List[ImpersonationRuleUnion]
    Description: Optional[str] = None
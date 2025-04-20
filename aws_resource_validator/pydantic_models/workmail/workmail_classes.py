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


class CreateGroupRequest(BaseValidatorModel):
    OrganizationId: str
    Name: str
    HiddenFromGlobalAddressList: Optional[bool] = None


class CreateIdentityCenterApplicationRequest(BaseValidatorModel):
    Name: str
    InstanceArn: str
    ClientToken: Optional[str] = None


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


class CreateResourceRequest(BaseValidatorModel):
    OrganizationId: str
    Name: str
    Type: ResourceTypeType
    Description: Optional[str] = None
    HiddenFromGlobalAddressList: Optional[bool] = None


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


class DescribeEmailMonitoringConfigurationRequest(BaseValidatorModel):
    OrganizationId: str


class DescribeEntityRequest(BaseValidatorModel):
    OrganizationId: str
    Email: str


class DescribeGroupRequest(BaseValidatorModel):
    OrganizationId: str
    GroupId: str


class DescribeIdentityProviderConfigurationRequest(BaseValidatorModel):
    OrganizationId: str


class IdentityCenterConfiguration(BaseValidatorModel):
    InstanceArn: str
    ApplicationArn: str


class PersonalAccessTokenConfiguration(BaseValidatorModel):
    Status: PersonalAccessTokenConfigurationStatusType
    LifetimeInDays: Optional[int] = None


class DescribeInboundDmarcSettingsRequest(BaseValidatorModel):
    OrganizationId: str


class DescribeMailboxExportJobRequest(BaseValidatorModel):
    JobId: str
    OrganizationId: str


class DescribeOrganizationRequest(BaseValidatorModel):
    OrganizationId: str


class DescribeResourceRequest(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str


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


class GetAccessControlEffectRequest(BaseValidatorModel):
    OrganizationId: str
    IpAddress: str
    Action: str
    UserId: Optional[str] = None
    ImpersonationRoleId: Optional[str] = None


class GetDefaultRetentionPolicyRequest(BaseValidatorModel):
    OrganizationId: str


class GetImpersonationRoleEffectRequest(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str
    TargetUser: str


class ImpersonationMatchedRule(BaseValidatorModel):
    ImpersonationRuleId: Optional[str] = None
    Name: Optional[str] = None


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


class GetMailDomainRequest(BaseValidatorModel):
    OrganizationId: str
    DomainName: str


class GetMailboxDetailsRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str


class GetMobileDeviceAccessEffectRequest(BaseValidatorModel):
    OrganizationId: str
    DeviceType: Optional[str] = None
    DeviceModel: Optional[str] = None
    DeviceOperatingSystem: Optional[str] = None
    DeviceUserAgent: Optional[str] = None


class MobileDeviceAccessMatchedRule(BaseValidatorModel):
    MobileDeviceAccessRuleId: Optional[str] = None
    Name: Optional[str] = None


class GetMobileDeviceAccessOverrideRequest(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str


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


class ListAccessControlRulesRequest(BaseValidatorModel):
    OrganizationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAliasesRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAvailabilityConfigurationsRequest(BaseValidatorModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


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


class ListImpersonationRolesRequest(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMailDomainsRequest(BaseValidatorModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MailDomainSummary(BaseValidatorModel):
    DomainName: Optional[str] = None
    DefaultDomain: Optional[bool] = None


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


class ListMailboxPermissionsRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Permission(BaseValidatorModel):
    GranteeId: str
    GranteeType: MemberTypeType
    PermissionValues: List[PermissionTypeType]


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


class ListOrganizationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OrganizationSummary(BaseValidatorModel):
    OrganizationId: Optional[str] = None
    Alias: Optional[str] = None
    DefaultMailDomain: Optional[str] = None
    ErrorMessage: Optional[str] = None
    State: Optional[str] = None


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


class AssumeImpersonationRoleResponse(BaseValidatorModel):
    Token: str
    ExpiresIn: int
    ResponseMetadata: ResponseMetadata


class CreateGroupResponse(BaseValidatorModel):
    GroupId: str
    ResponseMetadata: ResponseMetadata


class CreateIdentityCenterApplicationResponse(BaseValidatorModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadata


class CreateImpersonationRoleResponse(BaseValidatorModel):
    ImpersonationRoleId: str
    ResponseMetadata: ResponseMetadata


class CreateMobileDeviceAccessRuleResponse(BaseValidatorModel):
    MobileDeviceAccessRuleId: str
    ResponseMetadata: ResponseMetadata


class CreateOrganizationResponse(BaseValidatorModel):
    OrganizationId: str
    ResponseMetadata: ResponseMetadata


class CreateResourceResponse(BaseValidatorModel):
    ResourceId: str
    ResponseMetadata: ResponseMetadata


class CreateUserResponse(BaseValidatorModel):
    UserId: str
    ResponseMetadata: ResponseMetadata


class DeleteOrganizationResponse(BaseValidatorModel):
    OrganizationId: str
    State: str
    ResponseMetadata: ResponseMetadata


class DescribeEmailMonitoringConfigurationResponse(BaseValidatorModel):
    RoleArn: str
    LogGroupArn: str
    ResponseMetadata: ResponseMetadata


class DescribeEntityResponse(BaseValidatorModel):
    EntityId: str
    Name: str
    Type: EntityTypeType
    ResponseMetadata: ResponseMetadata


class DescribeGroupResponse(BaseValidatorModel):
    GroupId: str
    Name: str
    Email: str
    State: EntityStateType
    EnabledDate: datetime
    DisabledDate: datetime
    HiddenFromGlobalAddressList: bool
    ResponseMetadata: ResponseMetadata


class DescribeInboundDmarcSettingsResponse(BaseValidatorModel):
    Enforced: bool
    ResponseMetadata: ResponseMetadata


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


class GetAccessControlEffectResponse(BaseValidatorModel):
    Effect: AccessControlRuleEffectType
    MatchedRules: List[str]
    ResponseMetadata: ResponseMetadata


class GetMailboxDetailsResponse(BaseValidatorModel):
    MailboxQuota: int
    MailboxSize: float
    ResponseMetadata: ResponseMetadata


class GetMobileDeviceAccessOverrideResponse(BaseValidatorModel):
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: str
    DateCreated: datetime
    DateModified: datetime
    ResponseMetadata: ResponseMetadata


class GetPersonalAccessTokenMetadataResponse(BaseValidatorModel):
    PersonalAccessTokenId: str
    UserId: str
    Name: str
    DateCreated: datetime
    DateLastUsed: datetime
    ExpiresTime: datetime
    Scopes: List[str]
    ResponseMetadata: ResponseMetadata


class ListAccessControlRulesResponse(BaseValidatorModel):
    Rules: List[AccessControlRule]
    ResponseMetadata: ResponseMetadata


class ListAliasesResponse(BaseValidatorModel):
    Aliases: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartMailboxExportJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


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


class CreateOrganizationRequest(BaseValidatorModel):
    Alias: str
    DirectoryId: Optional[str] = None
    ClientToken: Optional[str] = None
    Domains: Optional[List[Domain]] = None
    KmsKeyArn: Optional[str] = None
    EnableInteroperability: Optional[bool] = None


class ListResourceDelegatesResponse(BaseValidatorModel):
    Delegates: List[Delegate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class GetMailDomainResponse(BaseValidatorModel):
    Records: List[DnsRecord]
    IsTestDomain: bool
    IsDefault: bool
    OwnershipVerificationStatus: DnsRecordVerificationStatusType
    DkimVerificationStatus: DnsRecordVerificationStatusType
    ResponseMetadata: ResponseMetadata


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


class GetImpersonationRoleEffectResponse(BaseValidatorModel):
    Type: ImpersonationRoleTypeType
    Effect: AccessEffectType
    MatchedRules: List[ImpersonationMatchedRule]
    ResponseMetadata: ResponseMetadata


class GetImpersonationRoleResponse(BaseValidatorModel):
    ImpersonationRoleId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Description: str
    Rules: List[ImpersonationRuleOutput]
    DateCreated: datetime
    DateModified: datetime
    ResponseMetadata: ResponseMetadata


class GetMobileDeviceAccessEffectResponse(BaseValidatorModel):
    Effect: MobileDeviceAccessRuleEffectType
    MatchedRules: List[MobileDeviceAccessMatchedRule]
    ResponseMetadata: ResponseMetadata


class ListGroupsForEntityResponse(BaseValidatorModel):
    Groups: List[GroupIdentifier]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupsResponse(BaseValidatorModel):
    Groups: List[Group]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class ListGroupMembersResponse(BaseValidatorModel):
    Members: List[Member]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupsRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListGroupsFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsRequest(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListGroupsFilters] = None


class ListGroupsForEntityRequest(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Filters: Optional[ListGroupsForEntityFilters] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMailDomainsResponse(BaseValidatorModel):
    MailDomains: List[MailDomainSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMailboxExportJobsResponse(BaseValidatorModel):
    Jobs: List[MailboxExportJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMailboxPermissionsResponse(BaseValidatorModel):
    Permissions: List[Permission]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMobileDeviceAccessOverridesResponse(BaseValidatorModel):
    Overrides: List[MobileDeviceAccessOverride]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMobileDeviceAccessRulesResponse(BaseValidatorModel):
    Rules: List[MobileDeviceAccessRule]
    ResponseMetadata: ResponseMetadata


class ListOrganizationsResponse(BaseValidatorModel):
    OrganizationSummaries: List[OrganizationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPersonalAccessTokensResponse(BaseValidatorModel):
    PersonalAccessTokenSummaries: List[PersonalAccessTokenSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourcesRequestPaginate(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListResourcesFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourcesRequest(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListResourcesFilters] = None


class ListResourcesResponse(BaseValidatorModel):
    Resources: List[Resource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class ListUsersRequest(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListUsersFilters] = None


class ListUsersResponse(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAvailabilityConfigurationsResponse(BaseValidatorModel):
    AvailabilityConfigurations: List[AvailabilityConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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
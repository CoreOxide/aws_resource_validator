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
from aws_resource_validator.pydantic_models.workmail_constants import *

class AccessControlRuleTypeDef(BaseValidatorModel):
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


class AssociateDelegateToResourceRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    EntityId: str


class AssociateMemberToGroupRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    MemberId: str


class AssumeImpersonationRoleRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class LambdaAvailabilityProviderTypeDef(BaseValidatorModel):
    LambdaArn: str


class RedactedEwsAvailabilityProviderTypeDef(BaseValidatorModel):
    EwsEndpoint: Optional[str] = None
    EwsUsername: Optional[str] = None


class BookingOptionsTypeDef(BaseValidatorModel):
    AutoAcceptRequests: Optional[bool] = None
    AutoDeclineRecurringRequests: Optional[bool] = None
    AutoDeclineConflictingRequests: Optional[bool] = None


class CancelMailboxExportJobRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    JobId: str
    OrganizationId: str


class CreateAliasRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Alias: str


class EwsAvailabilityProviderTypeDef(BaseValidatorModel):
    EwsEndpoint: str
    EwsUsername: str
    EwsPassword: str


class CreateGroupRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str
    HiddenFromGlobalAddressList: Optional[bool] = None


class CreateIdentityCenterApplicationRequestTypeDef(BaseValidatorModel):
    Name: str
    InstanceArn: str
    ClientToken: Optional[str] = None


class CreateMobileDeviceAccessRuleRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str
    Effect: MobileDeviceAccessRuleEffectType
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DeviceTypes: Optional[Sequence[str]] = None
    NotDeviceTypes: Optional[Sequence[str]] = None
    DeviceModels: Optional[Sequence[str]] = None
    NotDeviceModels: Optional[Sequence[str]] = None
    DeviceOperatingSystems: Optional[Sequence[str]] = None
    NotDeviceOperatingSystems: Optional[Sequence[str]] = None
    DeviceUserAgents: Optional[Sequence[str]] = None
    NotDeviceUserAgents: Optional[Sequence[str]] = None


class DomainTypeDef(BaseValidatorModel):
    DomainName: str
    HostedZoneId: Optional[str] = None


class CreateUserRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str
    DisplayName: str
    Password: Optional[str] = None
    Role: Optional[UserRoleType] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    HiddenFromGlobalAddressList: Optional[bool] = None
    IdentityProviderUserId: Optional[str] = None


class DeleteAccessControlRuleRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str


class DeleteAliasRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Alias: str


class DeleteAvailabilityConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str


class DeleteEmailMonitoringConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str


class DeleteGroupRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str


class DeleteIdentityCenterApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str


class DeleteIdentityProviderConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str


class DeleteImpersonationRoleRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str


class DeleteMailboxPermissionsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    GranteeId: str


class DeleteMobileDeviceAccessOverrideRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str


class DeleteMobileDeviceAccessRuleRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    MobileDeviceAccessRuleId: str


class DeleteOrganizationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DeleteDirectory: bool
    ClientToken: Optional[str] = None
    ForceDelete: Optional[bool] = None
    DeleteIdentityCenterApplication: Optional[bool] = None


class DeletePersonalAccessTokenRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    PersonalAccessTokenId: str


class DeleteResourceRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str


class DeleteRetentionPolicyRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Id: str


class DeleteUserRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str


class DeregisterFromWorkMailRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str


class DeregisterMailDomainRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str


class DescribeEmailMonitoringConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str


class DescribeEntityRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Email: str


class DescribeGroupRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str


class DescribeIdentityProviderConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str


class IdentityCenterConfigurationTypeDef(BaseValidatorModel):
    InstanceArn: str
    ApplicationArn: str


class PersonalAccessTokenConfigurationTypeDef(BaseValidatorModel):
    Status: PersonalAccessTokenConfigurationStatusType
    LifetimeInDays: Optional[int] = None


class DescribeInboundDmarcSettingsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str


class DescribeMailboxExportJobRequestTypeDef(BaseValidatorModel):
    JobId: str
    OrganizationId: str


class DescribeOrganizationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str


class DescribeResourceRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str


class DescribeUserRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str


class DisassociateDelegateFromResourceRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    EntityId: str


class DisassociateMemberFromGroupRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    MemberId: str


class FolderConfigurationTypeDef(BaseValidatorModel):
    Name: FolderNameType
    Action: RetentionActionType
    Period: Optional[int] = None


class GetAccessControlEffectRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    IpAddress: str
    Action: str
    UserId: Optional[str] = None
    ImpersonationRoleId: Optional[str] = None


class GetDefaultRetentionPolicyRequestTypeDef(BaseValidatorModel):
    OrganizationId: str


class GetImpersonationRoleEffectRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str
    TargetUser: str


class ImpersonationMatchedRuleTypeDef(BaseValidatorModel):
    ImpersonationRuleId: Optional[str] = None
    Name: Optional[str] = None


class GetImpersonationRoleRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str


class ImpersonationRuleOutputTypeDef(BaseValidatorModel):
    ImpersonationRuleId: str
    Effect: AccessEffectType
    Name: Optional[str] = None
    Description: Optional[str] = None
    TargetUsers: Optional[List[str]] = None
    NotTargetUsers: Optional[List[str]] = None


class GetMailDomainRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str


class GetMailboxDetailsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str


class GetMobileDeviceAccessEffectRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DeviceType: Optional[str] = None
    DeviceModel: Optional[str] = None
    DeviceOperatingSystem: Optional[str] = None
    DeviceUserAgent: Optional[str] = None


class MobileDeviceAccessMatchedRuleTypeDef(BaseValidatorModel):
    MobileDeviceAccessRuleId: Optional[str] = None
    Name: Optional[str] = None


class GetMobileDeviceAccessOverrideRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str


class GetPersonalAccessTokenMetadataRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    PersonalAccessTokenId: str


class GroupIdentifierTypeDef(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None


class GroupTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[EntityStateType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None


class ImpersonationRuleTypeDef(BaseValidatorModel):
    ImpersonationRuleId: str
    Effect: AccessEffectType
    Name: Optional[str] = None
    Description: Optional[str] = None
    TargetUsers: Optional[Sequence[str]] = None
    NotTargetUsers: Optional[Sequence[str]] = None


class ListAccessControlRulesRequestTypeDef(BaseValidatorModel):
    OrganizationId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAliasesRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAvailabilityConfigurationsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListGroupMembersRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListGroupsFiltersTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None


class ListGroupsForEntityFiltersTypeDef(BaseValidatorModel):
    GroupNamePrefix: Optional[str] = None


class ListImpersonationRolesRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMailDomainsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MailDomainSummaryTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    DefaultDomain: Optional[bool] = None


class ListMailboxExportJobsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MailboxExportJobTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    EntityId: Optional[str] = None
    Description: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3Path: Optional[str] = None
    EstimatedProgress: Optional[int] = None
    State: Optional[MailboxExportJobStateType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class ListMailboxPermissionsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PermissionTypeDef(BaseValidatorModel):
    GranteeId: str
    GranteeType: MemberTypeType
    PermissionValues: List[PermissionTypeType]


class ListMobileDeviceAccessOverridesRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: Optional[str] = None
    DeviceId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MobileDeviceAccessOverrideTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None
    DeviceId: Optional[str] = None
    Effect: Optional[MobileDeviceAccessRuleEffectType] = None
    Description: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None


class ListMobileDeviceAccessRulesRequestTypeDef(BaseValidatorModel):
    OrganizationId: str


class MobileDeviceAccessRuleTypeDef(BaseValidatorModel):
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


class ListOrganizationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OrganizationSummaryTypeDef(BaseValidatorModel):
    OrganizationId: Optional[str] = None
    Alias: Optional[str] = None
    DefaultMailDomain: Optional[str] = None
    ErrorMessage: Optional[str] = None
    State: Optional[str] = None


class ListPersonalAccessTokensRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PersonalAccessTokenSummaryTypeDef(BaseValidatorModel):
    PersonalAccessTokenId: Optional[str] = None
    UserId: Optional[str] = None
    Name: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateLastUsed: Optional[datetime] = None
    ExpiresTime: Optional[datetime] = None
    Scopes: Optional[List[str]] = None


class ListResourceDelegatesRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListResourcesFiltersTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ListUsersFiltersTypeDef(BaseValidatorModel):
    UsernamePrefix: Optional[str] = None
    DisplayNamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None
    IdentityProviderUserIdPrefix: Optional[str] = None


class UserTypeDef(BaseValidatorModel):
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


class PutAccessControlRuleRequestTypeDef(BaseValidatorModel):
    Name: str
    Effect: AccessControlRuleEffectType
    Description: str
    OrganizationId: str
    IpRanges: Optional[Sequence[str]] = None
    NotIpRanges: Optional[Sequence[str]] = None
    Actions: Optional[Sequence[str]] = None
    NotActions: Optional[Sequence[str]] = None
    UserIds: Optional[Sequence[str]] = None
    NotUserIds: Optional[Sequence[str]] = None
    ImpersonationRoleIds: Optional[Sequence[str]] = None
    NotImpersonationRoleIds: Optional[Sequence[str]] = None


class PutEmailMonitoringConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    RoleArn: str
    LogGroupArn: str


class PutInboundDmarcSettingsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Enforced: bool


class PutMailboxPermissionsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    GranteeId: str
    PermissionValues: Sequence[PermissionTypeType]


class PutMobileDeviceAccessOverrideRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: Optional[str] = None


class RegisterMailDomainRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str
    ClientToken: Optional[str] = None


class RegisterToWorkMailRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Email: str


class ResetPasswordRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    Password: str


class StartMailboxExportJobRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    OrganizationId: str
    EntityId: str
    RoleArn: str
    KmsKeyArn: str
    S3BucketName: str
    S3Prefix: str
    Description: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateDefaultMailDomainRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str


class UpdateGroupRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    HiddenFromGlobalAddressList: Optional[bool] = None


class UpdateMailboxQuotaRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    MailboxQuota: int


class UpdateMobileDeviceAccessRuleRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    MobileDeviceAccessRuleId: str
    Name: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: Optional[str] = None
    DeviceTypes: Optional[Sequence[str]] = None
    NotDeviceTypes: Optional[Sequence[str]] = None
    DeviceModels: Optional[Sequence[str]] = None
    NotDeviceModels: Optional[Sequence[str]] = None
    DeviceOperatingSystems: Optional[Sequence[str]] = None
    NotDeviceOperatingSystems: Optional[Sequence[str]] = None
    DeviceUserAgents: Optional[Sequence[str]] = None
    NotDeviceUserAgents: Optional[Sequence[str]] = None


class UpdatePrimaryEmailAddressRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Email: str


class UpdateUserRequestTypeDef(BaseValidatorModel):
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


class AssumeImpersonationRoleResponseTypeDef(BaseValidatorModel):
    Token: str
    ExpiresIn: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGroupResponseTypeDef(BaseValidatorModel):
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIdentityCenterApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateImpersonationRoleResponseTypeDef(BaseValidatorModel):
    ImpersonationRoleId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMobileDeviceAccessRuleResponseTypeDef(BaseValidatorModel):
    MobileDeviceAccessRuleId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOrganizationResponseTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResourceResponseTypeDef(BaseValidatorModel):
    ResourceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserResponseTypeDef(BaseValidatorModel):
    UserId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteOrganizationResponseTypeDef(BaseValidatorModel):
    OrganizationId: str
    State: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEmailMonitoringConfigurationResponseTypeDef(BaseValidatorModel):
    RoleArn: str
    LogGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeGroupResponseTypeDef(BaseValidatorModel):
    GroupId: str
    Name: str
    Email: str
    State: EntityStateType
    EnabledDate: datetime
    DisabledDate: datetime
    HiddenFromGlobalAddressList: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeInboundDmarcSettingsResponseTypeDef(BaseValidatorModel):
    Enforced: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMailboxExportJobResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeOrganizationResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeUserResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessControlEffectResponseTypeDef(BaseValidatorModel):
    Effect: AccessControlRuleEffectType
    MatchedRules: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetMailboxDetailsResponseTypeDef(BaseValidatorModel):
    MailboxQuota: int
    MailboxSize: float
    ResponseMetadata: ResponseMetadataTypeDef


class GetMobileDeviceAccessOverrideResponseTypeDef(BaseValidatorModel):
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: str
    DateCreated: datetime
    DateModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetPersonalAccessTokenMetadataResponseTypeDef(BaseValidatorModel):
    PersonalAccessTokenId: str
    UserId: str
    Name: str
    DateCreated: datetime
    DateLastUsed: datetime
    ExpiresTime: datetime
    Scopes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccessControlRulesResponseTypeDef(BaseValidatorModel):
    Rules: List[AccessControlRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAliasesResponseTypeDef(BaseValidatorModel):
    Aliases: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StartMailboxExportJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class TestAvailabilityConfigurationResponseTypeDef(BaseValidatorModel):
    TestPassed: bool
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class AvailabilityConfigurationTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    ProviderType: Optional[AvailabilityProviderTypeType] = None
    EwsProvider: Optional[RedactedEwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None


class CreateAvailabilityConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str
    ClientToken: Optional[str] = None
    EwsProvider: Optional[EwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None


class TestAvailabilityConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: Optional[str] = None
    EwsProvider: Optional[EwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None


class UpdateAvailabilityConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str
    EwsProvider: Optional[EwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None


class CreateOrganizationRequestTypeDef(BaseValidatorModel):
    Alias: str
    DirectoryId: Optional[str] = None
    ClientToken: Optional[str] = None
    Domains: Optional[Sequence[DomainTypeDef]] = None
    KmsKeyArn: Optional[str] = None
    EnableInteroperability: Optional[bool] = None


class DelegateTypeDef(BaseValidatorModel):
    pass


class ListResourceDelegatesResponseTypeDef(BaseValidatorModel):
    Delegates: List[DelegateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeIdentityProviderConfigurationResponseTypeDef(BaseValidatorModel):
    AuthenticationMode: IdentityProviderAuthenticationModeType
    IdentityCenterConfiguration: IdentityCenterConfigurationTypeDef
    PersonalAccessTokenConfiguration: PersonalAccessTokenConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutIdentityProviderConfigurationRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    AuthenticationMode: IdentityProviderAuthenticationModeType
    IdentityCenterConfiguration: IdentityCenterConfigurationTypeDef
    PersonalAccessTokenConfiguration: PersonalAccessTokenConfigurationTypeDef


class DnsRecordTypeDef(BaseValidatorModel):
    pass


class GetMailDomainResponseTypeDef(BaseValidatorModel):
    Records: List[DnsRecordTypeDef]
    IsTestDomain: bool
    IsDefault: bool
    OwnershipVerificationStatus: DnsRecordVerificationStatusType
    DkimVerificationStatus: DnsRecordVerificationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetDefaultRetentionPolicyResponseTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    Description: str
    FolderConfigurations: List[FolderConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutRetentionPolicyRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str
    FolderConfigurations: Sequence[FolderConfigurationTypeDef]
    Id: Optional[str] = None
    Description: Optional[str] = None


class GetMobileDeviceAccessEffectResponseTypeDef(BaseValidatorModel):
    Effect: MobileDeviceAccessRuleEffectType
    MatchedRules: List[MobileDeviceAccessMatchedRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListGroupsForEntityResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListGroupsResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ImpersonationRoleTypeDef(BaseValidatorModel):
    pass


class ListImpersonationRolesResponseTypeDef(BaseValidatorModel):
    Roles: List[ImpersonationRoleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAliasesRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAvailabilityConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupMembersRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMailboxPermissionsRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrganizationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPersonalAccessTokensRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceDelegatesRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class MemberTypeDef(BaseValidatorModel):
    pass


class ListGroupMembersResponseTypeDef(BaseValidatorModel):
    Members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListGroupsRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListGroupsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListGroupsFiltersTypeDef] = None


class ListGroupsForEntityRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Filters: Optional[ListGroupsForEntityFiltersTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMailDomainsResponseTypeDef(BaseValidatorModel):
    MailDomains: List[MailDomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMailboxExportJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[MailboxExportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMailboxPermissionsResponseTypeDef(BaseValidatorModel):
    Permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMobileDeviceAccessOverridesResponseTypeDef(BaseValidatorModel):
    Overrides: List[MobileDeviceAccessOverrideTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMobileDeviceAccessRulesResponseTypeDef(BaseValidatorModel):
    Rules: List[MobileDeviceAccessRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListOrganizationsResponseTypeDef(BaseValidatorModel):
    OrganizationSummaries: List[OrganizationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPersonalAccessTokensResponseTypeDef(BaseValidatorModel):
    PersonalAccessTokenSummaries: List[PersonalAccessTokenSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListResourcesRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListResourcesFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourcesRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListResourcesFiltersTypeDef] = None


class ResourceTypeDef(BaseValidatorModel):
    pass


class ListResourcesResponseTypeDef(BaseValidatorModel):
    Resources: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListUsersFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListUsersFiltersTypeDef] = None


class ListUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAvailabilityConfigurationsResponseTypeDef(BaseValidatorModel):
    AvailabilityConfigurations: List[AvailabilityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None



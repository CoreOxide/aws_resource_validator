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
from aws_resource_validator.pydantic_models.workmail_constants import *

class AccessControlRuleTypeDef(BaseModel):
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

class AssociateDelegateToResourceRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ResourceId: str
    EntityId: str

class AssociateMemberToGroupRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    GroupId: str
    MemberId: str

class AssumeImpersonationRoleRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ImpersonationRoleId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class LambdaAvailabilityProviderTypeDef(BaseModel):
    LambdaArn: str

class RedactedEwsAvailabilityProviderTypeDef(BaseModel):
    EwsEndpoint: Optional[str] = None
    EwsUsername: Optional[str] = None

class BookingOptionsTypeDef(BaseModel):
    AutoAcceptRequests: Optional[bool] = None
    AutoDeclineRecurringRequests: Optional[bool] = None
    AutoDeclineConflictingRequests: Optional[bool] = None

class CancelMailboxExportJobRequestRequestTypeDef(BaseModel):
    ClientToken: str
    JobId: str
    OrganizationId: str

class CreateAliasRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    Alias: str

class EwsAvailabilityProviderTypeDef(BaseModel):
    EwsEndpoint: str
    EwsUsername: str
    EwsPassword: str

class CreateGroupRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Name: str
    HiddenFromGlobalAddressList: Optional[bool] = None

class ImpersonationRuleTypeDef(BaseModel):
    ImpersonationRuleId: str
    Effect: AccessEffectType
    Name: Optional[str] = None
    Description: Optional[str] = None
    TargetUsers: Optional[Sequence[str]] = None
    NotTargetUsers: Optional[Sequence[str]] = None

class CreateMobileDeviceAccessRuleRequestRequestTypeDef(BaseModel):
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

class DomainTypeDef(BaseModel):
    DomainName: str
    HostedZoneId: Optional[str] = None

class CreateResourceRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Name: str
    Type: ResourceTypeType
    Description: Optional[str] = None
    HiddenFromGlobalAddressList: Optional[bool] = None

class CreateUserRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Name: str
    DisplayName: str
    Password: Optional[str] = None
    Role: Optional[UserRoleType] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    HiddenFromGlobalAddressList: Optional[bool] = None

class DelegateTypeDef(BaseModel):
    Id: str
    Type: MemberTypeType

class DeleteAccessControlRuleRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Name: str

class DeleteAliasRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    Alias: str

class DeleteAvailabilityConfigurationRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DomainName: str

class DeleteEmailMonitoringConfigurationRequestRequestTypeDef(BaseModel):
    OrganizationId: str

class DeleteGroupRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    GroupId: str

class DeleteImpersonationRoleRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ImpersonationRoleId: str

class DeleteMailboxPermissionsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    GranteeId: str

class DeleteMobileDeviceAccessOverrideRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    UserId: str
    DeviceId: str

class DeleteMobileDeviceAccessRuleRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    MobileDeviceAccessRuleId: str

class DeleteOrganizationRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DeleteDirectory: bool
    ClientToken: Optional[str] = None
    ForceDelete: Optional[bool] = None

class DeleteResourceRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ResourceId: str

class DeleteRetentionPolicyRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Id: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    UserId: str

class DeregisterFromWorkMailRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str

class DeregisterMailDomainRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DomainName: str

class DescribeEmailMonitoringConfigurationRequestRequestTypeDef(BaseModel):
    OrganizationId: str

class DescribeEntityRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Email: str

class DescribeGroupRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    GroupId: str

class DescribeInboundDmarcSettingsRequestRequestTypeDef(BaseModel):
    OrganizationId: str

class DescribeMailboxExportJobRequestRequestTypeDef(BaseModel):
    JobId: str
    OrganizationId: str

class DescribeOrganizationRequestRequestTypeDef(BaseModel):
    OrganizationId: str

class DescribeResourceRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ResourceId: str

class DescribeUserRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    UserId: str

class DisassociateDelegateFromResourceRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ResourceId: str
    EntityId: str

class DisassociateMemberFromGroupRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    GroupId: str
    MemberId: str

class DnsRecordTypeDef(BaseModel):
    Type: Optional[str] = None
    Hostname: Optional[str] = None
    Value: Optional[str] = None

class FolderConfigurationTypeDef(BaseModel):
    Name: FolderNameType
    Action: RetentionActionType
    Period: Optional[int] = None

class GetAccessControlEffectRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    IpAddress: str
    Action: str
    UserId: Optional[str] = None
    ImpersonationRoleId: Optional[str] = None

class GetDefaultRetentionPolicyRequestRequestTypeDef(BaseModel):
    OrganizationId: str

class GetImpersonationRoleEffectRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ImpersonationRoleId: str
    TargetUser: str

class ImpersonationMatchedRuleTypeDef(BaseModel):
    ImpersonationRuleId: Optional[str] = None
    Name: Optional[str] = None

class GetImpersonationRoleRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ImpersonationRoleId: str

class GetMailDomainRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DomainName: str

class GetMailboxDetailsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    UserId: str

class GetMobileDeviceAccessEffectRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DeviceType: Optional[str] = None
    DeviceModel: Optional[str] = None
    DeviceOperatingSystem: Optional[str] = None
    DeviceUserAgent: Optional[str] = None

class MobileDeviceAccessMatchedRuleTypeDef(BaseModel):
    MobileDeviceAccessRuleId: Optional[str] = None
    Name: Optional[str] = None

class GetMobileDeviceAccessOverrideRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    UserId: str
    DeviceId: str

class GroupIdentifierTypeDef(BaseModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None

class GroupTypeDef(BaseModel):
    Id: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[EntityStateType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None

class ImpersonationRoleTypeDef(BaseModel):
    ImpersonationRoleId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ImpersonationRoleTypeType] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None

class ListAccessControlRulesRequestRequestTypeDef(BaseModel):
    OrganizationId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAliasesRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAvailabilityConfigurationsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGroupMembersRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    GroupId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MemberTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[MemberTypeType] = None
    State: Optional[EntityStateType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None

class ListGroupsFiltersTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None

class ListGroupsForEntityFiltersTypeDef(BaseModel):
    GroupNamePrefix: Optional[str] = None

class ListImpersonationRolesRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMailDomainsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MailDomainSummaryTypeDef(BaseModel):
    DomainName: Optional[str] = None
    DefaultDomain: Optional[bool] = None

class ListMailboxExportJobsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MailboxExportJobTypeDef(BaseModel):
    JobId: Optional[str] = None
    EntityId: Optional[str] = None
    Description: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3Path: Optional[str] = None
    EstimatedProgress: Optional[int] = None
    State: Optional[MailboxExportJobStateType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ListMailboxPermissionsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PermissionTypeDef(BaseModel):
    GranteeId: str
    GranteeType: MemberTypeType
    PermissionValues: List[PermissionTypeType]

class ListMobileDeviceAccessOverridesRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    UserId: Optional[str] = None
    DeviceId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MobileDeviceAccessOverrideTypeDef(BaseModel):
    UserId: Optional[str] = None
    DeviceId: Optional[str] = None
    Effect: Optional[MobileDeviceAccessRuleEffectType] = None
    Description: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None

class ListMobileDeviceAccessRulesRequestRequestTypeDef(BaseModel):
    OrganizationId: str

class MobileDeviceAccessRuleTypeDef(BaseModel):
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

class ListOrganizationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OrganizationSummaryTypeDef(BaseModel):
    OrganizationId: Optional[str] = None
    Alias: Optional[str] = None
    DefaultMailDomain: Optional[str] = None
    ErrorMessage: Optional[str] = None
    State: Optional[str] = None

class ListResourceDelegatesRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListResourcesFiltersTypeDef(BaseModel):
    NamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None

class ResourceTypeDef(BaseModel):
    Id: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ResourceTypeType] = None
    State: Optional[EntityStateType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None
    Description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ListUsersFiltersTypeDef(BaseModel):
    UsernamePrefix: Optional[str] = None
    DisplayNamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None

class UserTypeDef(BaseModel):
    Id: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    DisplayName: Optional[str] = None
    State: Optional[EntityStateType] = None
    UserRole: Optional[UserRoleType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None

class PutAccessControlRuleRequestRequestTypeDef(BaseModel):
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

class PutEmailMonitoringConfigurationRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    RoleArn: str
    LogGroupArn: str

class PutInboundDmarcSettingsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Enforced: bool

class PutMailboxPermissionsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    GranteeId: str
    PermissionValues: Sequence[PermissionTypeType]

class PutMobileDeviceAccessOverrideRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: Optional[str] = None

class RegisterMailDomainRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DomainName: str
    ClientToken: Optional[str] = None

class RegisterToWorkMailRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    Email: str

class ResetPasswordRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    UserId: str
    Password: str

class StartMailboxExportJobRequestRequestTypeDef(BaseModel):
    ClientToken: str
    OrganizationId: str
    EntityId: str
    RoleArn: str
    KmsKeyArn: str
    S3BucketName: str
    S3Prefix: str
    Description: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateDefaultMailDomainRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DomainName: str

class UpdateGroupRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    GroupId: str
    HiddenFromGlobalAddressList: Optional[bool] = None

class UpdateMailboxQuotaRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    UserId: str
    MailboxQuota: int

class UpdateMobileDeviceAccessRuleRequestRequestTypeDef(BaseModel):
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

class UpdatePrimaryEmailAddressRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    Email: str

class UpdateUserRequestRequestTypeDef(BaseModel):
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

class AssumeImpersonationRoleResponseTypeDef(BaseModel):
    Token: str
    ExpiresIn: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(BaseModel):
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImpersonationRoleResponseTypeDef(BaseModel):
    ImpersonationRoleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMobileDeviceAccessRuleResponseTypeDef(BaseModel):
    MobileDeviceAccessRuleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOrganizationResponseTypeDef(BaseModel):
    OrganizationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceResponseTypeDef(BaseModel):
    ResourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseModel):
    UserId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOrganizationResponseTypeDef(BaseModel):
    OrganizationId: str
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEmailMonitoringConfigurationResponseTypeDef(BaseModel):
    RoleArn: str
    LogGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntityResponseTypeDef(BaseModel):
    EntityId: str
    Name: str
    Type: EntityTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupResponseTypeDef(BaseModel):
    GroupId: str
    Name: str
    Email: str
    State: EntityStateType
    EnabledDate: datetime
    DisabledDate: datetime
    HiddenFromGlobalAddressList: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundDmarcSettingsResponseTypeDef(BaseModel):
    Enforced: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMailboxExportJobResponseTypeDef(BaseModel):
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

class DescribeOrganizationResponseTypeDef(BaseModel):
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

class DescribeUserResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessControlEffectResponseTypeDef(BaseModel):
    Effect: AccessControlRuleEffectType
    MatchedRules: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMailboxDetailsResponseTypeDef(BaseModel):
    MailboxQuota: int
    MailboxSize: float
    ResponseMetadata: ResponseMetadataTypeDef

class GetMobileDeviceAccessOverrideResponseTypeDef(BaseModel):
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: str
    DateCreated: datetime
    DateModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessControlRulesResponseTypeDef(BaseModel):
    Rules: List[AccessControlRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(BaseModel):
    Aliases: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMailboxExportJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestAvailabilityConfigurationResponseTypeDef(BaseModel):
    TestPassed: bool
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class AvailabilityConfigurationTypeDef(BaseModel):
    DomainName: Optional[str] = None
    ProviderType: Optional[AvailabilityProviderTypeType] = None
    EwsProvider: Optional[RedactedEwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None

class DescribeResourceResponseTypeDef(BaseModel):
    ResourceId: str
    Email: str
    Name: str
    Type: ResourceTypeType
    BookingOptions: BookingOptionsTypeDef
    State: EntityStateType
    EnabledDate: datetime
    DisabledDate: datetime
    Description: str
    HiddenFromGlobalAddressList: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResourceRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ResourceId: str
    Name: Optional[str] = None
    BookingOptions: Optional[BookingOptionsTypeDef] = None
    Description: Optional[str] = None
    Type: Optional[ResourceTypeType] = None
    HiddenFromGlobalAddressList: Optional[bool] = None

class CreateAvailabilityConfigurationRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DomainName: str
    ClientToken: Optional[str] = None
    EwsProvider: Optional[EwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None

class TestAvailabilityConfigurationRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DomainName: Optional[str] = None
    EwsProvider: Optional[EwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None

class UpdateAvailabilityConfigurationRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    DomainName: str
    EwsProvider: Optional[EwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None

class CreateImpersonationRoleRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Rules: Sequence[ImpersonationRuleTypeDef]
    ClientToken: Optional[str] = None
    Description: Optional[str] = None

class GetImpersonationRoleResponseTypeDef(BaseModel):
    ImpersonationRoleId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Description: str
    Rules: List[ImpersonationRuleTypeDef]
    DateCreated: datetime
    DateModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImpersonationRoleRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    ImpersonationRoleId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Rules: Sequence[ImpersonationRuleTypeDef]
    Description: Optional[str] = None

class CreateOrganizationRequestRequestTypeDef(BaseModel):
    Alias: str
    DirectoryId: Optional[str] = None
    ClientToken: Optional[str] = None
    Domains: Optional[Sequence[DomainTypeDef]] = None
    KmsKeyArn: Optional[str] = None
    EnableInteroperability: Optional[bool] = None

class ListResourceDelegatesResponseTypeDef(BaseModel):
    Delegates: List[DelegateTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMailDomainResponseTypeDef(BaseModel):
    Records: List[DnsRecordTypeDef]
    IsTestDomain: bool
    IsDefault: bool
    OwnershipVerificationStatus: DnsRecordVerificationStatusType
    DkimVerificationStatus: DnsRecordVerificationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetDefaultRetentionPolicyResponseTypeDef(BaseModel):
    Id: str
    Name: str
    Description: str
    FolderConfigurations: List[FolderConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRetentionPolicyRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    Name: str
    FolderConfigurations: Sequence[FolderConfigurationTypeDef]
    Id: Optional[str] = None
    Description: Optional[str] = None

class GetImpersonationRoleEffectResponseTypeDef(BaseModel):
    Type: ImpersonationRoleTypeType
    Effect: AccessEffectType
    MatchedRules: List[ImpersonationMatchedRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMobileDeviceAccessEffectResponseTypeDef(BaseModel):
    Effect: MobileDeviceAccessRuleEffectType
    MatchedRules: List[MobileDeviceAccessMatchedRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsForEntityResponseTypeDef(BaseModel):
    Groups: List[GroupIdentifierTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseModel):
    Groups: List[GroupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImpersonationRolesResponseTypeDef(BaseModel):
    Roles: List[ImpersonationRoleTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesRequestListAliasesPaginateTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAvailabilityConfigurationsRequestListAvailabilityConfigurationsPaginateTypeDef(BaseModel):
    OrganizationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupMembersRequestListGroupMembersPaginateTypeDef(BaseModel):
    OrganizationId: str
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMailboxPermissionsRequestListMailboxPermissionsPaginateTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationsRequestListOrganizationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceDelegatesRequestListResourceDelegatesPaginateTypeDef(BaseModel):
    OrganizationId: str
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupMembersResponseTypeDef(BaseModel):
    Members: List[MemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsRequestListGroupsPaginateTypeDef(BaseModel):
    OrganizationId: str
    Filters: Optional[ListGroupsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListGroupsFiltersTypeDef] = None

class ListGroupsForEntityRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    EntityId: str
    Filters: Optional[ListGroupsForEntityFiltersTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMailDomainsResponseTypeDef(BaseModel):
    MailDomains: List[MailDomainSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMailboxExportJobsResponseTypeDef(BaseModel):
    Jobs: List[MailboxExportJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMailboxPermissionsResponseTypeDef(BaseModel):
    Permissions: List[PermissionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMobileDeviceAccessOverridesResponseTypeDef(BaseModel):
    Overrides: List[MobileDeviceAccessOverrideTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMobileDeviceAccessRulesResponseTypeDef(BaseModel):
    Rules: List[MobileDeviceAccessRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationsResponseTypeDef(BaseModel):
    OrganizationSummaries: List[OrganizationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesRequestListResourcesPaginateTypeDef(BaseModel):
    OrganizationId: str
    Filters: Optional[ListResourcesFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListResourcesFiltersTypeDef] = None

class ListResourcesResponseTypeDef(BaseModel):
    Resources: List[ResourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    OrganizationId: str
    Filters: Optional[ListUsersFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestRequestTypeDef(BaseModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListUsersFiltersTypeDef] = None

class ListUsersResponseTypeDef(BaseModel):
    Users: List[UserTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailabilityConfigurationsResponseTypeDef(BaseModel):
    AvailabilityConfigurations: List[AvailabilityConfigurationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


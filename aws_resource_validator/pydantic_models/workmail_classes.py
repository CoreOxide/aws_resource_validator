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

class AssociateDelegateToResourceRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    EntityId: str

class AssociateMemberToGroupRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    MemberId: str

class AssumeImpersonationRoleRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class LambdaAvailabilityProviderTypeDef(BaseValidatorModel):
    LambdaArn: str

class RedactedEwsAvailabilityProviderTypeDef(BaseValidatorModel):
    EwsEndpoint: Optional[str] = None
    EwsUsername: Optional[str] = None

class BookingOptionsTypeDef(BaseValidatorModel):
    AutoAcceptRequests: Optional[bool] = None
    AutoDeclineRecurringRequests: Optional[bool] = None
    AutoDeclineConflictingRequests: Optional[bool] = None

class CancelMailboxExportJobRequestRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    JobId: str
    OrganizationId: str

class CreateAliasRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Alias: str

class EwsAvailabilityProviderTypeDef(BaseValidatorModel):
    EwsEndpoint: str
    EwsUsername: str
    EwsPassword: str

class CreateGroupRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str
    HiddenFromGlobalAddressList: Optional[bool] = None

class ImpersonationRuleTypeDef(BaseValidatorModel):
    ImpersonationRuleId: str
    Effect: AccessEffectType
    Name: Optional[str] = None
    Description: Optional[str] = None
    TargetUsers: Optional[Sequence[str]] = None
    NotTargetUsers: Optional[Sequence[str]] = None

class CreateMobileDeviceAccessRuleRequestRequestTypeDef(BaseValidatorModel):
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

class CreateResourceRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str
    Type: ResourceTypeType
    Description: Optional[str] = None
    HiddenFromGlobalAddressList: Optional[bool] = None

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str
    DisplayName: str
    Password: Optional[str] = None
    Role: Optional[UserRoleType] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    HiddenFromGlobalAddressList: Optional[bool] = None

class DelegateTypeDef(BaseValidatorModel):
    Id: str
    Type: MemberTypeType

class DeleteAccessControlRuleRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str

class DeleteAliasRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Alias: str

class DeleteAvailabilityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str

class DeleteEmailMonitoringConfigurationRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str

class DeleteGroupRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str

class DeleteImpersonationRoleRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str

class DeleteMailboxPermissionsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    GranteeId: str

class DeleteMobileDeviceAccessOverrideRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str

class DeleteMobileDeviceAccessRuleRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    MobileDeviceAccessRuleId: str

class DeleteOrganizationRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DeleteDirectory: bool
    ClientToken: Optional[str] = None
    ForceDelete: Optional[bool] = None

class DeleteResourceRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str

class DeleteRetentionPolicyRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Id: str

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str

class DeregisterFromWorkMailRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str

class DeregisterMailDomainRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str

class DescribeEmailMonitoringConfigurationRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str

class DescribeEntityRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Email: str

class DescribeGroupRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str

class DescribeInboundDmarcSettingsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str

class DescribeMailboxExportJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str
    OrganizationId: str

class DescribeOrganizationRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str

class DescribeResourceRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str

class DescribeUserRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str

class DisassociateDelegateFromResourceRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    EntityId: str

class DisassociateMemberFromGroupRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    MemberId: str

class DnsRecordTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Hostname: Optional[str] = None
    Value: Optional[str] = None

class FolderConfigurationTypeDef(BaseValidatorModel):
    Name: FolderNameType
    Action: RetentionActionType
    Period: Optional[int] = None

class GetAccessControlEffectRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    IpAddress: str
    Action: str
    UserId: Optional[str] = None
    ImpersonationRoleId: Optional[str] = None

class GetDefaultRetentionPolicyRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str

class GetImpersonationRoleEffectRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str
    TargetUser: str

class ImpersonationMatchedRuleTypeDef(BaseValidatorModel):
    ImpersonationRuleId: Optional[str] = None
    Name: Optional[str] = None

class GetImpersonationRoleRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str

class GetMailDomainRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str

class GetMailboxDetailsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str

class GetMobileDeviceAccessEffectRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DeviceType: Optional[str] = None
    DeviceModel: Optional[str] = None
    DeviceOperatingSystem: Optional[str] = None
    DeviceUserAgent: Optional[str] = None

class MobileDeviceAccessMatchedRuleTypeDef(BaseValidatorModel):
    MobileDeviceAccessRuleId: Optional[str] = None
    Name: Optional[str] = None

class GetMobileDeviceAccessOverrideRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str

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

class ImpersonationRoleTypeDef(BaseValidatorModel):
    ImpersonationRoleId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ImpersonationRoleTypeType] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None

class ListAccessControlRulesRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAliasesRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAvailabilityConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGroupMembersRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MemberTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[MemberTypeType] = None
    State: Optional[EntityStateType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None

class ListGroupsFiltersTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None

class ListGroupsForEntityFiltersTypeDef(BaseValidatorModel):
    GroupNamePrefix: Optional[str] = None

class ListImpersonationRolesRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMailDomainsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MailDomainSummaryTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    DefaultDomain: Optional[bool] = None

class ListMailboxExportJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListMailboxPermissionsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PermissionTypeDef(BaseValidatorModel):
    GranteeId: str
    GranteeType: MemberTypeType
    PermissionValues: List[PermissionTypeType]

class ListMobileDeviceAccessOverridesRequestRequestTypeDef(BaseValidatorModel):
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

class ListMobileDeviceAccessRulesRequestRequestTypeDef(BaseValidatorModel):
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

class ListOrganizationsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OrganizationSummaryTypeDef(BaseValidatorModel):
    OrganizationId: Optional[str] = None
    Alias: Optional[str] = None
    DefaultMailDomain: Optional[str] = None
    ErrorMessage: Optional[str] = None
    State: Optional[str] = None

class ListResourceDelegatesRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListResourcesFiltersTypeDef(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None

class ResourceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ResourceTypeType] = None
    State: Optional[EntityStateType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None
    Description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ListUsersFiltersTypeDef(BaseValidatorModel):
    UsernamePrefix: Optional[str] = None
    DisplayNamePrefix: Optional[str] = None
    PrimaryEmailPrefix: Optional[str] = None
    State: Optional[EntityStateType] = None

class UserTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    DisplayName: Optional[str] = None
    State: Optional[EntityStateType] = None
    UserRole: Optional[UserRoleType] = None
    EnabledDate: Optional[datetime] = None
    DisabledDate: Optional[datetime] = None

class PutAccessControlRuleRequestRequestTypeDef(BaseValidatorModel):
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

class PutEmailMonitoringConfigurationRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    RoleArn: str
    LogGroupArn: str

class PutInboundDmarcSettingsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Enforced: bool

class PutMailboxPermissionsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    GranteeId: str
    PermissionValues: Sequence[PermissionTypeType]

class PutMobileDeviceAccessOverrideRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: Optional[str] = None

class RegisterMailDomainRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str
    ClientToken: Optional[str] = None

class RegisterToWorkMailRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Email: str

class ResetPasswordRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    Password: str

class StartMailboxExportJobRequestRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    OrganizationId: str
    EntityId: str
    RoleArn: str
    KmsKeyArn: str
    S3BucketName: str
    S3Prefix: str
    Description: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateDefaultMailDomainRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str

class UpdateGroupRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    HiddenFromGlobalAddressList: Optional[bool] = None

class UpdateMailboxQuotaRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    UserId: str
    MailboxQuota: int

class UpdateMobileDeviceAccessRuleRequestRequestTypeDef(BaseValidatorModel):
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

class UpdatePrimaryEmailAddressRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Email: str

class UpdateUserRequestRequestTypeDef(BaseValidatorModel):
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

class AssumeImpersonationRoleResponseTypeDef(BaseValidatorModel):
    Token: str
    ExpiresIn: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(BaseValidatorModel):
    GroupId: str
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

class DescribeEntityResponseTypeDef(BaseValidatorModel):
    EntityId: str
    Name: str
    Type: EntityTypeType
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

class ListAccessControlRulesResponseTypeDef(BaseValidatorModel):
    Rules: List[AccessControlRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(BaseValidatorModel):
    Aliases: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class DescribeResourceResponseTypeDef(BaseValidatorModel):
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

class UpdateResourceRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    Name: Optional[str] = None
    BookingOptions: Optional[BookingOptionsTypeDef] = None
    Description: Optional[str] = None
    Type: Optional[ResourceTypeType] = None
    HiddenFromGlobalAddressList: Optional[bool] = None

class CreateAvailabilityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str
    ClientToken: Optional[str] = None
    EwsProvider: Optional[EwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None

class TestAvailabilityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: Optional[str] = None
    EwsProvider: Optional[EwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None

class UpdateAvailabilityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    DomainName: str
    EwsProvider: Optional[EwsAvailabilityProviderTypeDef] = None
    LambdaProvider: Optional[LambdaAvailabilityProviderTypeDef] = None

class CreateImpersonationRoleRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Rules: Sequence[ImpersonationRuleTypeDef]
    ClientToken: Optional[str] = None
    Description: Optional[str] = None

class GetImpersonationRoleResponseTypeDef(BaseValidatorModel):
    ImpersonationRoleId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Description: str
    Rules: List[ImpersonationRuleTypeDef]
    DateCreated: datetime
    DateModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImpersonationRoleRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    ImpersonationRoleId: str
    Name: str
    Type: ImpersonationRoleTypeType
    Rules: Sequence[ImpersonationRuleTypeDef]
    Description: Optional[str] = None

class CreateOrganizationRequestRequestTypeDef(BaseValidatorModel):
    Alias: str
    DirectoryId: Optional[str] = None
    ClientToken: Optional[str] = None
    Domains: Optional[Sequence[DomainTypeDef]] = None
    KmsKeyArn: Optional[str] = None
    EnableInteroperability: Optional[bool] = None

class ListResourceDelegatesResponseTypeDef(BaseValidatorModel):
    Delegates: List[DelegateTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class PutRetentionPolicyRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    Name: str
    FolderConfigurations: Sequence[FolderConfigurationTypeDef]
    Id: Optional[str] = None
    Description: Optional[str] = None

class GetImpersonationRoleEffectResponseTypeDef(BaseValidatorModel):
    Type: ImpersonationRoleTypeType
    Effect: AccessEffectType
    MatchedRules: List[ImpersonationMatchedRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMobileDeviceAccessEffectResponseTypeDef(BaseValidatorModel):
    Effect: MobileDeviceAccessRuleEffectType
    MatchedRules: List[MobileDeviceAccessMatchedRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsForEntityResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupIdentifierTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImpersonationRolesResponseTypeDef(BaseValidatorModel):
    Roles: List[ImpersonationRoleTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesRequestListAliasesPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAvailabilityConfigurationsRequestListAvailabilityConfigurationsPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupMembersRequestListGroupMembersPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMailboxPermissionsRequestListMailboxPermissionsPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationsRequestListOrganizationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceDelegatesRequestListResourceDelegatesPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupMembersResponseTypeDef(BaseValidatorModel):
    Members: List[MemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsRequestListGroupsPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListGroupsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListGroupsFiltersTypeDef] = None

class ListGroupsForEntityRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    EntityId: str
    Filters: Optional[ListGroupsForEntityFiltersTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMailDomainsResponseTypeDef(BaseValidatorModel):
    MailDomains: List[MailDomainSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMailboxExportJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[MailboxExportJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMailboxPermissionsResponseTypeDef(BaseValidatorModel):
    Permissions: List[PermissionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMobileDeviceAccessOverridesResponseTypeDef(BaseValidatorModel):
    Overrides: List[MobileDeviceAccessOverrideTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMobileDeviceAccessRulesResponseTypeDef(BaseValidatorModel):
    Rules: List[MobileDeviceAccessRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationsResponseTypeDef(BaseValidatorModel):
    OrganizationSummaries: List[OrganizationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesRequestListResourcesPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListResourcesFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListResourcesFiltersTypeDef] = None

class ListResourcesResponseTypeDef(BaseValidatorModel):
    Resources: List[ResourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ListUsersRequestListUsersPaginateTypeDef(BaseValidatorModel):
    OrganizationId: str
    Filters: Optional[ListUsersFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestRequestTypeDef(BaseValidatorModel):
    OrganizationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[ListUsersFiltersTypeDef] = None

class ListUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailabilityConfigurationsResponseTypeDef(BaseValidatorModel):
    AvailabilityConfigurations: List[AvailabilityConfigurationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


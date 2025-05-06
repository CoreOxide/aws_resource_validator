from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.guardduty.guardduty_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptAdministratorInvitationRequest(BaseValidatorModel):
    DetectorId: str
    AdministratorId: str
    InvitationId: str


class AcceptInvitationRequest(BaseValidatorModel):
    DetectorId: str
    MasterId: str
    InvitationId: str


class AccessControlList(BaseValidatorModel):
    AllowsPublicReadAccess: Optional[bool] = None
    AllowsPublicWriteAccess: Optional[bool] = None


class AccessKeyDetails(BaseValidatorModel):
    AccessKeyId: Optional[str] = None
    PrincipalId: Optional[str] = None
    UserName: Optional[str] = None
    UserType: Optional[str] = None


class AccessKey(BaseValidatorModel):
    PrincipalId: Optional[str] = None
    UserName: Optional[str] = None
    UserType: Optional[str] = None


class AccountDetail(BaseValidatorModel):
    AccountId: str
    Email: str


class FreeTrialFeatureConfigurationResult(BaseValidatorModel):
    Name: Optional[FreeTrialFeatureResultType] = None
    FreeTrialDaysRemaining: Optional[int] = None


class BlockPublicAccess(BaseValidatorModel):
    IgnorePublicAcls: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None
    BlockPublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None


class AccountStatistics(BaseValidatorModel):
    AccountId: Optional[str] = None
    LastGeneratedAt: Optional[datetime] = None
    TotalFindings: Optional[int] = None


class Account(BaseValidatorModel):
    Uid: str
    Name: Optional[str] = None


class DnsRequestAction(BaseValidatorModel):
    Domain: Optional[str] = None
    Protocol: Optional[str] = None
    Blocked: Optional[bool] = None
    DomainWithSuffix: Optional[str] = None


class KubernetesPermissionCheckedDetails(BaseValidatorModel):
    Verb: Optional[str] = None
    Resource: Optional[str] = None
    Namespace: Optional[str] = None
    Allowed: Optional[bool] = None


class KubernetesRoleBindingDetails(BaseValidatorModel):
    Kind: Optional[str] = None
    Name: Optional[str] = None
    Uid: Optional[str] = None
    RoleRefName: Optional[str] = None
    RoleRefKind: Optional[str] = None


class KubernetesRoleDetails(BaseValidatorModel):
    Kind: Optional[str] = None
    Name: Optional[str] = None
    Uid: Optional[str] = None


class Session(BaseValidatorModel):
    Uid: Optional[str] = None
    MfaStatus: Optional[MfaStatusType] = None
    CreatedTime: Optional[datetime] = None
    Issuer: Optional[str] = None


class AddonDetails(BaseValidatorModel):
    AddonVersion: Optional[str] = None
    AddonStatus: Optional[str] = None


class AdminAccount(BaseValidatorModel):
    AdminAccountId: Optional[str] = None
    AdminStatus: Optional[AdminStatusType] = None


class Administrator(BaseValidatorModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    RelationshipStatus: Optional[str] = None
    InvitedAt: Optional[str] = None


class AgentDetails(BaseValidatorModel):
    Version: Optional[str] = None


class Observations(BaseValidatorModel):
    Text: Optional[List[str]] = None


class ArchiveFindingsRequest(BaseValidatorModel):
    DetectorId: str
    FindingIds: List[str]


class AutonomousSystem(BaseValidatorModel):
    Name: str
    Number: int


class DomainDetails(BaseValidatorModel):
    Domain: Optional[str] = None


class RemoteAccountDetails(BaseValidatorModel):
    AccountId: Optional[str] = None
    Affiliated: Optional[bool] = None


class BucketPolicy(BaseValidatorModel):
    AllowsPublicReadAccess: Optional[bool] = None
    AllowsPublicWriteAccess: Optional[bool] = None


class City(BaseValidatorModel):
    CityName: Optional[str] = None


class CloudTrailConfigurationResult(BaseValidatorModel):
    Status: DataSourceStatusType


class ConditionOutput(BaseValidatorModel):
    Eq: Optional[List[str]] = None
    Neq: Optional[List[str]] = None
    Gt: Optional[int] = None
    Gte: Optional[int] = None
    Lt: Optional[int] = None
    Lte: Optional[int] = None
    Equals: Optional[List[str]] = None
    NotEquals: Optional[List[str]] = None
    GreaterThan: Optional[int] = None
    GreaterThanOrEqual: Optional[int] = None
    LessThan: Optional[int] = None
    LessThanOrEqual: Optional[int] = None


class Condition(BaseValidatorModel):
    Eq: Optional[List[str]] = None
    Neq: Optional[List[str]] = None
    Gt: Optional[int] = None
    Gte: Optional[int] = None
    Lt: Optional[int] = None
    Lte: Optional[int] = None
    Equals: Optional[List[str]] = None
    NotEquals: Optional[List[str]] = None
    GreaterThan: Optional[int] = None
    GreaterThanOrEqual: Optional[int] = None
    LessThan: Optional[int] = None
    LessThanOrEqual: Optional[int] = None


class ContainerInstanceDetails(BaseValidatorModel):
    CoveredContainerInstances: Optional[int] = None
    CompatibleContainerInstances: Optional[int] = None


class SecurityContext(BaseValidatorModel):
    Privileged: Optional[bool] = None
    AllowPrivilegeEscalation: Optional[bool] = None


class VolumeMount(BaseValidatorModel):
    Name: Optional[str] = None
    MountPath: Optional[str] = None


class Country(BaseValidatorModel):
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None


class FargateDetails(BaseValidatorModel):
    Issues: Optional[List[str]] = None
    ManagementType: Optional[ManagementTypeType] = None


class CoverageFilterCondition(BaseValidatorModel):
    Equals: Optional[List[str]] = None
    NotEquals: Optional[List[str]] = None


class CoverageSortCriteria(BaseValidatorModel):
    AttributeName: Optional[CoverageSortKeyType] = None
    OrderBy: Optional[OrderByType] = None


class CoverageStatistics(BaseValidatorModel):
    CountByResourceType: Optional[Dict[ResourceTypeType, int]] = None
    CountByCoverageStatus: Optional[Dict[CoverageStatusType, int]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateIPSetRequest(BaseValidatorModel):
    DetectorId: str
    Name: str
    Format: IpSetFormatType
    Location: str
    Activate: bool
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class UnprocessedAccount(BaseValidatorModel):
    AccountId: str
    Result: str


class CreateS3BucketResourceOutput(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectPrefixes: Optional[List[str]] = None


class CreateS3BucketResource(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectPrefixes: Optional[List[str]] = None


class DestinationProperties(BaseValidatorModel):
    DestinationArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class CreateSampleFindingsRequest(BaseValidatorModel):
    DetectorId: str
    FindingTypes: Optional[List[str]] = None


class CreateThreatIntelSetRequest(BaseValidatorModel):
    DetectorId: str
    Name: str
    Format: ThreatIntelSetFormatType
    Location: str
    Activate: bool
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class DNSLogsConfigurationResult(BaseValidatorModel):
    Status: DataSourceStatusType


class FlowLogsConfigurationResult(BaseValidatorModel):
    Status: DataSourceStatusType


class S3LogsConfigurationResult(BaseValidatorModel):
    Status: DataSourceStatusType


class S3LogsConfiguration(BaseValidatorModel):
    Enable: bool


class DataSourceFreeTrial(BaseValidatorModel):
    FreeTrialDaysRemaining: Optional[int] = None


class DateStatistics(BaseValidatorModel):
    Date: Optional[datetime] = None
    LastGeneratedAt: Optional[datetime] = None
    Severity: Optional[float] = None
    TotalFindings: Optional[int] = None


class DeclineInvitationsRequest(BaseValidatorModel):
    AccountIds: List[str]


class DefaultServerSideEncryption(BaseValidatorModel):
    EncryptionType: Optional[str] = None
    KmsMasterKeyArn: Optional[str] = None


class DeleteDetectorRequest(BaseValidatorModel):
    DetectorId: str


class DeleteFilterRequest(BaseValidatorModel):
    DetectorId: str
    FilterName: str


class DeleteIPSetRequest(BaseValidatorModel):
    DetectorId: str
    IpSetId: str


class DeleteInvitationsRequest(BaseValidatorModel):
    AccountIds: List[str]


class DeleteMalwareProtectionPlanRequest(BaseValidatorModel):
    MalwareProtectionPlanId: str


class DeleteMembersRequest(BaseValidatorModel):
    DetectorId: str
    AccountIds: List[str]


class DeletePublishingDestinationRequest(BaseValidatorModel):
    DetectorId: str
    DestinationId: str


class DeleteThreatIntelSetRequest(BaseValidatorModel):
    DetectorId: str
    ThreatIntelSetId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class SortCriteria(BaseValidatorModel):
    AttributeName: Optional[str] = None
    OrderBy: Optional[OrderByType] = None


class DescribeOrganizationConfigurationRequest(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePublishingDestinationRequest(BaseValidatorModel):
    DetectorId: str
    DestinationId: str


class Destination(BaseValidatorModel):
    DestinationId: str
    DestinationType: Literal['S3']
    Status: PublishingStatusType


class DetectorAdditionalConfigurationResult(BaseValidatorModel):
    Name: Optional[FeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None


class DetectorAdditionalConfiguration(BaseValidatorModel):
    Name: Optional[FeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None


class DisableOrganizationAdminAccountRequest(BaseValidatorModel):
    AdminAccountId: str


class DisassociateFromAdministratorAccountRequest(BaseValidatorModel):
    DetectorId: str


class DisassociateFromMasterAccountRequest(BaseValidatorModel):
    DetectorId: str


class DisassociateMembersRequest(BaseValidatorModel):
    DetectorId: str
    AccountIds: List[str]


class VolumeDetail(BaseValidatorModel):
    VolumeArn: Optional[str] = None
    VolumeType: Optional[str] = None
    DeviceName: Optional[str] = None
    VolumeSizeInGB: Optional[int] = None
    EncryptionType: Optional[str] = None
    SnapshotArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class EbsVolumesResult(BaseValidatorModel):
    Status: Optional[DataSourceStatusType] = None
    Reason: Optional[str] = None


class IamInstanceProfile(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None


class ProductCode(BaseValidatorModel):
    Code: Optional[str] = None
    ProductType: Optional[str] = None


class PrivateIpAddressDetails(BaseValidatorModel):
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None


class SecurityGroup(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class EnableOrganizationAdminAccountRequest(BaseValidatorModel):
    AdminAccountId: str


class ThreatIntelligenceDetail(BaseValidatorModel):
    ThreatListName: Optional[str] = None
    ThreatNames: Optional[List[str]] = None
    ThreatFileSha256: Optional[str] = None


class FilterCondition(BaseValidatorModel):
    EqualsValue: Optional[str] = None
    GreaterThan: Optional[int] = None
    LessThan: Optional[int] = None


class FindingTypeStatistics(BaseValidatorModel):
    FindingType: Optional[str] = None
    LastGeneratedAt: Optional[datetime] = None
    TotalFindings: Optional[int] = None


class ResourceStatistics(BaseValidatorModel):
    AccountId: Optional[str] = None
    LastGeneratedAt: Optional[datetime] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    TotalFindings: Optional[int] = None


class SeverityStatistics(BaseValidatorModel):
    LastGeneratedAt: Optional[datetime] = None
    Severity: Optional[float] = None
    TotalFindings: Optional[int] = None


class GeoLocation(BaseValidatorModel):
    Lat: Optional[float] = None
    Lon: Optional[float] = None


class GetAdministratorAccountRequest(BaseValidatorModel):
    DetectorId: str


class GetDetectorRequest(BaseValidatorModel):
    DetectorId: str


class GetFilterRequest(BaseValidatorModel):
    DetectorId: str
    FilterName: str


class GetIPSetRequest(BaseValidatorModel):
    DetectorId: str
    IpSetId: str


class GetMalwareProtectionPlanRequest(BaseValidatorModel):
    MalwareProtectionPlanId: str


class MalwareProtectionPlanStatusReason(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class GetMalwareScanSettingsRequest(BaseValidatorModel):
    DetectorId: str


class GetMasterAccountRequest(BaseValidatorModel):
    DetectorId: str


class Master(BaseValidatorModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    RelationshipStatus: Optional[str] = None
    InvitedAt: Optional[str] = None


class GetMemberDetectorsRequest(BaseValidatorModel):
    DetectorId: str
    AccountIds: List[str]


class GetMembersRequest(BaseValidatorModel):
    DetectorId: str
    AccountIds: List[str]


class Member(BaseValidatorModel):
    AccountId: str
    MasterId: str
    Email: str
    RelationshipStatus: str
    UpdatedAt: str
    DetectorId: Optional[str] = None
    InvitedAt: Optional[str] = None
    AdministratorId: Optional[str] = None


class GetRemainingFreeTrialDaysRequest(BaseValidatorModel):
    DetectorId: str
    AccountIds: Optional[List[str]] = None


class GetThreatIntelSetRequest(BaseValidatorModel):
    DetectorId: str
    ThreatIntelSetId: str


class UsageCriteria(BaseValidatorModel):
    AccountIds: Optional[List[str]] = None
    DataSources: Optional[List[DataSourceType]] = None
    Resources: Optional[List[str]] = None
    Features: Optional[List[UsageFeatureType]] = None


class HighestSeverityThreatDetails(BaseValidatorModel):
    Severity: Optional[str] = None
    ThreatName: Optional[str] = None
    Count: Optional[int] = None


class HostPath(BaseValidatorModel):
    Path: Optional[str] = None


class ImpersonatedUser(BaseValidatorModel):
    Username: Optional[str] = None
    Groups: Optional[List[str]] = None


class Indicator(BaseValidatorModel):
    Key: IndicatorTypeType
    Values: Optional[List[str]] = None
    Title: Optional[str] = None


class Invitation(BaseValidatorModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    RelationshipStatus: Optional[str] = None
    InvitedAt: Optional[str] = None


class InviteMembersRequest(BaseValidatorModel):
    DetectorId: str
    AccountIds: List[str]
    DisableEmailNotification: Optional[bool] = None
    Message: Optional[str] = None


class ItemPath(BaseValidatorModel):
    NestedItemPath: Optional[str] = None
    Hash: Optional[str] = None


class KubernetesAuditLogsConfigurationResult(BaseValidatorModel):
    Status: DataSourceStatusType


class KubernetesAuditLogsConfiguration(BaseValidatorModel):
    Enable: bool


class LineageObject(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    NamespacePid: Optional[int] = None
    UserId: Optional[int] = None
    Name: Optional[str] = None
    Pid: Optional[int] = None
    Uuid: Optional[str] = None
    ExecutablePath: Optional[str] = None
    Euid: Optional[int] = None
    ParentUuid: Optional[str] = None


class ListDetectorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFiltersRequest(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListIPSetsRequest(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInvitationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMalwareProtectionPlansRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class MalwareProtectionPlanSummary(BaseValidatorModel):
    MalwareProtectionPlanId: Optional[str] = None


class ListMembersRequest(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OnlyAssociated: Optional[str] = None


class ListOrganizationAdminAccountsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPublishingDestinationsRequest(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListThreatIntelSetsRequest(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LocalIpDetails(BaseValidatorModel):
    IpAddressV4: Optional[str] = None
    IpAddressV6: Optional[str] = None


class LocalPortDetails(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None


class LoginAttribute(BaseValidatorModel):
    User: Optional[str] = None
    Application: Optional[str] = None
    FailedLoginAttempts: Optional[int] = None
    SuccessfulLoginAttempts: Optional[int] = None


class ScanEc2InstanceWithFindings(BaseValidatorModel):
    EbsVolumes: Optional[bool] = None


class MalwareProtectionPlanTaggingAction(BaseValidatorModel):
    Status: Optional[MalwareProtectionPlanTaggingActionStatusType] = None


class MemberAdditionalConfigurationResult(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None


class MemberAdditionalConfiguration(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None


class RemotePortDetails(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None


class NetworkConnection(BaseValidatorModel):
    Direction: NetworkDirectionType


class NetworkGeoLocation(BaseValidatorModel):
    City: str
    Country: str
    Latitude: float
    Longitude: float


class OrganizationAdditionalConfigurationResult(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None


class OrganizationAdditionalConfiguration(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None


class OrganizationS3LogsConfigurationResult(BaseValidatorModel):
    AutoEnable: bool


class OrganizationS3LogsConfiguration(BaseValidatorModel):
    AutoEnable: bool


class OrganizationEbsVolumesResult(BaseValidatorModel):
    AutoEnable: Optional[bool] = None


class OrganizationEbsVolumes(BaseValidatorModel):
    AutoEnable: Optional[bool] = None


class OrganizationFeatureStatisticsAdditionalConfiguration(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    EnabledAccountsCount: Optional[int] = None


class OrganizationKubernetesAuditLogsConfigurationResult(BaseValidatorModel):
    AutoEnable: bool


class OrganizationKubernetesAuditLogsConfiguration(BaseValidatorModel):
    AutoEnable: bool


class Organization(BaseValidatorModel):
    Asn: Optional[str] = None
    AsnOrg: Optional[str] = None
    Isp: Optional[str] = None
    Org: Optional[str] = None


class Owner(BaseValidatorModel):
    Id: Optional[str] = None


class PublicAccessConfiguration(BaseValidatorModel):
    PublicAclAccess: Optional[PublicAccessStatusType] = None
    PublicPolicyAccess: Optional[PublicAccessStatusType] = None
    PublicAclIgnoreBehavior: Optional[PublicAclIgnoreBehaviorType] = None
    PublicBucketRestrictBehavior: Optional[PublicBucketRestrictBehaviorType] = None


class RdsDbUserDetails(BaseValidatorModel):
    User: Optional[str] = None
    Application: Optional[str] = None
    Database: Optional[str] = None
    Ssl: Optional[str] = None
    AuthMethod: Optional[str] = None


class S3Object(BaseValidatorModel):
    ETag: Optional[str] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None


class ResourceDetails(BaseValidatorModel):
    InstanceArn: Optional[str] = None


class S3ObjectDetail(BaseValidatorModel):
    ObjectArn: Optional[str] = None
    Key: Optional[str] = None
    ETag: Optional[str] = None
    Hash: Optional[str] = None
    VersionId: Optional[str] = None


class ScanConditionPair(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class ScannedItemCount(BaseValidatorModel):
    TotalGb: Optional[int] = None
    Files: Optional[int] = None
    Volumes: Optional[int] = None


class ThreatsDetectedItemCount(BaseValidatorModel):
    Files: Optional[int] = None


class ScanFilePath(BaseValidatorModel):
    FilePath: Optional[str] = None
    VolumeArn: Optional[str] = None
    Hash: Optional[str] = None
    FileName: Optional[str] = None


class ScanResultDetails(BaseValidatorModel):
    ScanResult: Optional[ScanResultType] = None


class TriggerDetails(BaseValidatorModel):
    GuardDutyFindingId: Optional[str] = None
    Description: Optional[str] = None


class ServiceAdditionalInfo(BaseValidatorModel):
    Value: Optional[str] = None
    Type: Optional[str] = None


class StartMalwareScanRequest(BaseValidatorModel):
    ResourceArn: str


class StartMonitoringMembersRequest(BaseValidatorModel):
    DetectorId: str
    AccountIds: List[str]


class StopMonitoringMembersRequest(BaseValidatorModel):
    DetectorId: str
    AccountIds: List[str]


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class Total(BaseValidatorModel):
    Amount: Optional[str] = None
    Unit: Optional[str] = None


class UnarchiveFindingsRequest(BaseValidatorModel):
    DetectorId: str
    FindingIds: List[str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateFindingsFeedbackRequest(BaseValidatorModel):
    DetectorId: str
    FindingIds: List[str]
    Feedback: FeedbackType
    Comments: Optional[str] = None


class UpdateIPSetRequest(BaseValidatorModel):
    DetectorId: str
    IpSetId: str
    Name: Optional[str] = None
    Location: Optional[str] = None
    Activate: Optional[bool] = None


class UpdateS3BucketResource(BaseValidatorModel):
    ObjectPrefixes: Optional[List[str]] = None


class UpdateThreatIntelSetRequest(BaseValidatorModel):
    DetectorId: str
    ThreatIntelSetId: str
    Name: Optional[str] = None
    Location: Optional[str] = None
    Activate: Optional[bool] = None


class CreateMembersRequest(BaseValidatorModel):
    DetectorId: str
    AccountDetails: List[AccountDetail]


class AccountLevelPermissions(BaseValidatorModel):
    BlockPublicAccess: Optional[BlockPublicAccess] = None


class User(BaseValidatorModel):
    Name: str
    Uid: str
    Type: str
    CredentialUid: Optional[str] = None
    Account: Optional[Account] = None


class CoverageEksClusterDetails(BaseValidatorModel):
    ClusterName: Optional[str] = None
    CoveredNodes: Optional[int] = None
    CompatibleNodes: Optional[int] = None
    AddonDetails: Optional[AddonDetails] = None
    ManagementType: Optional[ManagementTypeType] = None


class CoverageEc2InstanceDetails(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    ClusterArn: Optional[str] = None
    AgentDetails: Optional[AgentDetails] = None
    ManagementType: Optional[ManagementTypeType] = None


class AnomalyObject(BaseValidatorModel):
    ProfileType: Optional[Literal['FREQUENCY']] = None
    ProfileSubtype: Optional[ProfileSubtypeType] = None
    Observations: Optional[Observations] = None


class BucketLevelPermissions(BaseValidatorModel):
    AccessControlList: Optional[AccessControlList] = None
    BucketPolicy: Optional[BucketPolicy] = None
    BlockPublicAccess: Optional[BlockPublicAccess] = None


class FindingCriteriaOutput(BaseValidatorModel):
    Criterion: Optional[Dict[str, ConditionOutput]] = None


class FindingCriteria(BaseValidatorModel):
    Criterion: Optional[Dict[str, Condition]] = None


class Container(BaseValidatorModel):
    ContainerRuntime: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Image: Optional[str] = None
    ImagePrefix: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMount]] = None
    SecurityContext: Optional[SecurityContext] = None


class CoverageEcsClusterDetails(BaseValidatorModel):
    ClusterName: Optional[str] = None
    FargateDetails: Optional[FargateDetails] = None
    ContainerInstanceDetails: Optional[ContainerInstanceDetails] = None


class CoverageFilterCriterion(BaseValidatorModel):
    CriterionKey: Optional[CoverageFilterCriterionKeyType] = None
    FilterCondition: Optional[CoverageFilterCondition] = None


class CreateFilterResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateIPSetResponse(BaseValidatorModel):
    IpSetId: str
    ResponseMetadata: ResponseMetadata


class CreateMalwareProtectionPlanResponse(BaseValidatorModel):
    MalwareProtectionPlanId: str
    ResponseMetadata: ResponseMetadata


class CreatePublishingDestinationResponse(BaseValidatorModel):
    DestinationId: str
    ResponseMetadata: ResponseMetadata


class CreateThreatIntelSetResponse(BaseValidatorModel):
    ThreatIntelSetId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAdministratorAccountResponse(BaseValidatorModel):
    Administrator: Administrator
    ResponseMetadata: ResponseMetadata


class GetCoverageStatisticsResponse(BaseValidatorModel):
    CoverageStatistics: CoverageStatistics
    ResponseMetadata: ResponseMetadata


class GetIPSetResponse(BaseValidatorModel):
    Name: str
    Format: IpSetFormatType
    Location: str
    Status: IpSetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetInvitationsCountResponse(BaseValidatorModel):
    InvitationsCount: int
    ResponseMetadata: ResponseMetadata


class GetThreatIntelSetResponse(BaseValidatorModel):
    Name: str
    Format: ThreatIntelSetFormatType
    Location: str
    Status: ThreatIntelSetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListDetectorsResponse(BaseValidatorModel):
    DetectorIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFiltersResponse(BaseValidatorModel):
    FilterNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFindingsResponse(BaseValidatorModel):
    FindingIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIPSetsResponse(BaseValidatorModel):
    IpSetIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOrganizationAdminAccountsResponse(BaseValidatorModel):
    AdminAccounts: List[AdminAccount]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListThreatIntelSetsResponse(BaseValidatorModel):
    ThreatIntelSetIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartMalwareScanResponse(BaseValidatorModel):
    ScanId: str
    ResponseMetadata: ResponseMetadata


class UpdateFilterResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class DeclineInvitationsResponse(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class DeleteInvitationsResponse(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class DeleteMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class DisassociateMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class InviteMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class StartMonitoringMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class StopMonitoringMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class UpdateMemberDetectorsResponse(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class CreateProtectedResourceOutput(BaseValidatorModel):
    S3Bucket: Optional[CreateS3BucketResourceOutput] = None


class CreateProtectedResource(BaseValidatorModel):
    S3Bucket: Optional[CreateS3BucketResource] = None


class CreatePublishingDestinationRequest(BaseValidatorModel):
    DetectorId: str
    DestinationType: Literal['S3']
    DestinationProperties: DestinationProperties
    ClientToken: Optional[str] = None


class DescribePublishingDestinationResponse(BaseValidatorModel):
    DestinationId: str
    DestinationType: Literal['S3']
    Status: PublishingStatusType
    PublishingFailureStartTimestamp: int
    DestinationProperties: DestinationProperties
    ResponseMetadata: ResponseMetadata


class UpdatePublishingDestinationRequest(BaseValidatorModel):
    DetectorId: str
    DestinationId: str
    DestinationProperties: Optional[DestinationProperties] = None


class KubernetesDataSourceFreeTrial(BaseValidatorModel):
    AuditLogs: Optional[DataSourceFreeTrial] = None


class MalwareProtectionDataSourceFreeTrial(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[DataSourceFreeTrial] = None


class ListDetectorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFiltersRequestPaginate(BaseValidatorModel):
    DetectorId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIPSetsRequestPaginate(BaseValidatorModel):
    DetectorId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInvitationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembersRequestPaginate(BaseValidatorModel):
    DetectorId: str
    OnlyAssociated: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationAdminAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThreatIntelSetsRequestPaginate(BaseValidatorModel):
    DetectorId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetFindingsRequest(BaseValidatorModel):
    DetectorId: str
    FindingIds: List[str]
    SortCriteria: Optional[SortCriteria] = None


class ListPublishingDestinationsResponse(BaseValidatorModel):
    Destinations: List[Destination]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DetectorFeatureConfigurationResult(BaseValidatorModel):
    Name: Optional[DetectorFeatureResultType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None
    AdditionalConfiguration: Optional[List[DetectorAdditionalConfigurationResult]] = None


class DetectorFeatureConfiguration(BaseValidatorModel):
    Name: Optional[DetectorFeatureType] = None
    Status: Optional[FeatureStatusType] = None
    AdditionalConfiguration: Optional[List[DetectorAdditionalConfiguration]] = None


class EbsVolumeDetails(BaseValidatorModel):
    ScannedVolumeDetails: Optional[List[VolumeDetail]] = None
    SkippedVolumeDetails: Optional[List[VolumeDetail]] = None


class ScanEc2InstanceWithFindingsResult(BaseValidatorModel):
    EbsVolumes: Optional[EbsVolumesResult] = None


class Ec2Instance(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    ImageDescription: Optional[str] = None
    InstanceState: Optional[str] = None
    IamInstanceProfile: Optional[IamInstanceProfile] = None
    InstanceType: Optional[str] = None
    OutpostArn: Optional[str] = None
    Platform: Optional[str] = None
    ProductCodes: Optional[List[ProductCode]] = None
    Ec2NetworkInterfaceUids: Optional[List[str]] = None


class Ec2NetworkInterface(BaseValidatorModel):
    Ipv6Addresses: Optional[List[str]] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressDetails]] = None
    PublicIp: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroup]] = None
    SubNetId: Optional[str] = None
    VpcId: Optional[str] = None


class NetworkInterface(BaseValidatorModel):
    Ipv6Addresses: Optional[List[str]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressDetails]] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroup]] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None


class VpcConfig(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroup]] = None


class EksClusterDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    VpcId: Optional[str] = None
    Status: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    CreatedAt: Optional[datetime] = None


class RdsDbInstanceDetails(BaseValidatorModel):
    DbInstanceIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None
    DbInstanceArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class RdsLimitlessDbDetails(BaseValidatorModel):
    DbShardGroupIdentifier: Optional[str] = None
    DbShardGroupResourceId: Optional[str] = None
    DbShardGroupArn: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class Evidence(BaseValidatorModel):
    ThreatIntelligenceDetails: Optional[List[ThreatIntelligenceDetail]] = None


class FilterCriterion(BaseValidatorModel):
    CriterionKey: Optional[CriterionKeyType] = None
    FilterCondition: Optional[FilterCondition] = None


class FindingStatistics(BaseValidatorModel):
    CountBySeverity: Optional[Dict[str, int]] = None
    GroupedByAccount: Optional[List[AccountStatistics]] = None
    GroupedByDate: Optional[List[DateStatistics]] = None
    GroupedByFindingType: Optional[List[FindingTypeStatistics]] = None
    GroupedByResource: Optional[List[ResourceStatistics]] = None
    GroupedBySeverity: Optional[List[SeverityStatistics]] = None


class GetMasterAccountResponse(BaseValidatorModel):
    Master: Master
    ResponseMetadata: ResponseMetadata


class GetMembersResponse(BaseValidatorModel):
    Members: List[Member]
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class ListMembersResponse(BaseValidatorModel):
    Members: List[Member]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetUsageStatisticsRequest(BaseValidatorModel):
    DetectorId: str
    UsageStatisticType: UsageStatisticTypeType
    UsageCriteria: UsageCriteria
    Unit: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Volume(BaseValidatorModel):
    Name: Optional[str] = None
    HostPath: Optional[HostPath] = None


class KubernetesUserDetails(BaseValidatorModel):
    Username: Optional[str] = None
    Uid: Optional[str] = None
    Groups: Optional[List[str]] = None
    SessionName: Optional[List[str]] = None
    ImpersonatedUser: Optional[ImpersonatedUser] = None


class Signal(BaseValidatorModel):
    Uid: str
    Type: SignalTypeType
    Name: str
    CreatedAt: datetime
    UpdatedAt: datetime
    FirstSeenAt: datetime
    LastSeenAt: datetime
    Count: int
    Description: Optional[str] = None
    Severity: Optional[float] = None
    ResourceUids: Optional[List[str]] = None
    ActorIds: Optional[List[str]] = None
    EndpointIds: Optional[List[str]] = None
    SignalIndicators: Optional[List[Indicator]] = None


class ListInvitationsResponse(BaseValidatorModel):
    Invitations: List[Invitation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Threat(BaseValidatorModel):
    Name: Optional[str] = None
    Source: Optional[str] = None
    ItemPaths: Optional[List[ItemPath]] = None


class KubernetesConfigurationResult(BaseValidatorModel):
    AuditLogs: KubernetesAuditLogsConfigurationResult


class KubernetesConfiguration(BaseValidatorModel):
    AuditLogs: KubernetesAuditLogsConfiguration


class ProcessDetails(BaseValidatorModel):
    Name: Optional[str] = None
    ExecutablePath: Optional[str] = None
    ExecutableSha256: Optional[str] = None
    NamespacePid: Optional[int] = None
    Pwd: Optional[str] = None
    Pid: Optional[int] = None
    StartTime: Optional[datetime] = None
    Uuid: Optional[str] = None
    ParentUuid: Optional[str] = None
    User: Optional[str] = None
    UserId: Optional[int] = None
    Euid: Optional[int] = None
    Lineage: Optional[List[LineageObject]] = None


class ListMalwareProtectionPlansResponse(BaseValidatorModel):
    MalwareProtectionPlans: List[MalwareProtectionPlanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MalwareProtectionConfiguration(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[ScanEc2InstanceWithFindings] = None


class MalwareProtectionPlanActions(BaseValidatorModel):
    Tagging: Optional[MalwareProtectionPlanTaggingAction] = None


class MemberFeaturesConfigurationResult(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None
    AdditionalConfiguration: Optional[List[MemberAdditionalConfigurationResult]] = None


class MemberFeaturesConfiguration(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    Status: Optional[FeatureStatusType] = None
    AdditionalConfiguration: Optional[List[MemberAdditionalConfiguration]] = None


class NetworkEndpoint(BaseValidatorModel):
    Id: str
    Ip: Optional[str] = None
    Domain: Optional[str] = None
    Port: Optional[int] = None
    Location: Optional[NetworkGeoLocation] = None
    AutonomousSystem: Optional[AutonomousSystem] = None
    Connection: Optional[NetworkConnection] = None


class OrganizationFeatureConfigurationResult(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None
    AdditionalConfiguration: Optional[List[OrganizationAdditionalConfigurationResult]] = None


class OrganizationFeatureConfiguration(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None
    AdditionalConfiguration: Optional[List[OrganizationAdditionalConfiguration]] = None


class OrganizationScanEc2InstanceWithFindingsResult(BaseValidatorModel):
    EbsVolumes: Optional[OrganizationEbsVolumesResult] = None


class OrganizationScanEc2InstanceWithFindings(BaseValidatorModel):
    EbsVolumes: Optional[OrganizationEbsVolumes] = None


class OrganizationFeatureStatistics(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    EnabledAccountsCount: Optional[int] = None
    AdditionalConfiguration: Optional[List[OrganizationFeatureStatisticsAdditionalConfiguration]] = None


class OrganizationKubernetesConfigurationResult(BaseValidatorModel):
    AuditLogs: OrganizationKubernetesAuditLogsConfigurationResult


class OrganizationKubernetesConfiguration(BaseValidatorModel):
    AuditLogs: OrganizationKubernetesAuditLogsConfiguration


class RemoteIpDetails(BaseValidatorModel):
    City: Optional[City] = None
    Country: Optional[Country] = None
    GeoLocation: Optional[GeoLocation] = None
    IpAddressV4: Optional[str] = None
    IpAddressV6: Optional[str] = None
    Organization: Optional[Organization] = None


class S3Bucket(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    EncryptionType: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    EffectivePermission: Optional[str] = None
    PublicReadAccess: Optional[PublicAccessStatusType] = None
    PublicWriteAccess: Optional[PublicAccessStatusType] = None
    AccountPublicAccess: Optional[PublicAccessConfiguration] = None
    BucketPublicAccess: Optional[PublicAccessConfiguration] = None
    S3ObjectUids: Optional[List[str]] = None


class ScanConditionOutput(BaseValidatorModel):
    MapEquals: List[ScanConditionPair]


class ScanCondition(BaseValidatorModel):
    MapEquals: List[ScanConditionPair]


class ScanThreatName(BaseValidatorModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[ScanFilePath]] = None


class Scan(BaseValidatorModel):
    DetectorId: Optional[str] = None
    AdminDetectorId: Optional[str] = None
    ScanId: Optional[str] = None
    ScanStatus: Optional[ScanStatusType] = None
    FailureReason: Optional[str] = None
    ScanStartTime: Optional[datetime] = None
    ScanEndTime: Optional[datetime] = None
    TriggerDetails: Optional[TriggerDetails] = None
    ResourceDetails: Optional[ResourceDetails] = None
    ScanResultDetails: Optional[ScanResultDetails] = None
    AccountId: Optional[str] = None
    TotalBytes: Optional[int] = None
    FileCount: Optional[int] = None
    AttachedVolumes: Optional[List[VolumeDetail]] = None
    ScanType: Optional[ScanTypeType] = None


class UsageAccountResult(BaseValidatorModel):
    AccountId: Optional[str] = None
    Total: Optional[Total] = None


class UsageDataSourceResult(BaseValidatorModel):
    DataSource: Optional[DataSourceType] = None
    Total: Optional[Total] = None


class UsageFeatureResult(BaseValidatorModel):
    Feature: Optional[UsageFeatureType] = None
    Total: Optional[Total] = None


class UsageResourceResult(BaseValidatorModel):
    Resource: Optional[str] = None
    Total: Optional[Total] = None


class UsageTopAccountResult(BaseValidatorModel):
    AccountId: Optional[str] = None
    Total: Optional[Total] = None


class UpdateProtectedResource(BaseValidatorModel):
    S3Bucket: Optional[UpdateS3BucketResource] = None


class Actor(BaseValidatorModel):
    Id: str
    User: Optional[User] = None
    Session: Optional[Session] = None


class AnomalyUnusual(BaseValidatorModel):
    Behavior: Optional[Dict[str, Dict[str, AnomalyObject]]] = None


class PermissionConfiguration(BaseValidatorModel):
    BucketLevelPermissions: Optional[BucketLevelPermissions] = None
    AccountLevelPermissions: Optional[AccountLevelPermissions] = None


class GetFilterResponse(BaseValidatorModel):
    Name: str
    Description: str
    Action: FilterActionType
    Rank: int
    FindingCriteria: FindingCriteriaOutput
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

FindingCriteriaUnion = Union[FindingCriteria, FindingCriteriaOutput]


class CoverageResourceDetails(BaseValidatorModel):
    EksClusterDetails: Optional[CoverageEksClusterDetails] = None
    ResourceType: Optional[ResourceTypeType] = None
    EcsClusterDetails: Optional[CoverageEcsClusterDetails] = None
    Ec2InstanceDetails: Optional[CoverageEc2InstanceDetails] = None


class CoverageFilterCriteria(BaseValidatorModel):
    FilterCriterion: Optional[List[CoverageFilterCriterion]] = None

CreateProtectedResourceUnion = Union[CreateProtectedResource, CreateProtectedResourceOutput]


class DataSourcesFreeTrial(BaseValidatorModel):
    CloudTrail: Optional[DataSourceFreeTrial] = None
    DnsLogs: Optional[DataSourceFreeTrial] = None
    FlowLogs: Optional[DataSourceFreeTrial] = None
    S3Logs: Optional[DataSourceFreeTrial] = None
    Kubernetes: Optional[KubernetesDataSourceFreeTrial] = None
    MalwareProtection: Optional[MalwareProtectionDataSourceFreeTrial] = None


class MalwareProtectionConfigurationResult(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[ScanEc2InstanceWithFindingsResult] = None
    ServiceRole: Optional[str] = None


class InstanceDetails(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    IamInstanceProfile: Optional[IamInstanceProfile] = None
    ImageDescription: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceState: Optional[str] = None
    InstanceType: Optional[str] = None
    OutpostArn: Optional[str] = None
    LaunchTime: Optional[str] = None
    NetworkInterfaces: Optional[List[NetworkInterface]] = None
    Platform: Optional[str] = None
    ProductCodes: Optional[List[ProductCode]] = None
    Tags: Optional[List[Tag]] = None


class LambdaDetails(BaseValidatorModel):
    FunctionArn: Optional[str] = None
    FunctionName: Optional[str] = None
    Description: Optional[str] = None
    LastModifiedAt: Optional[datetime] = None
    RevisionId: Optional[str] = None
    FunctionVersion: Optional[str] = None
    Role: Optional[str] = None
    VpcConfig: Optional[VpcConfig] = None
    Tags: Optional[List[Tag]] = None


class FilterCriteria(BaseValidatorModel):
    FilterCriterion: Optional[List[FilterCriterion]] = None


class GetFindingsStatisticsResponse(BaseValidatorModel):
    FindingStatistics: FindingStatistics
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EcsTaskDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    DefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    TaskCreatedAt: Optional[datetime] = None
    StartedAt: Optional[datetime] = None
    StartedBy: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Volumes: Optional[List[Volume]] = None
    Containers: Optional[List[Container]] = None
    Group: Optional[str] = None
    LaunchType: Optional[str] = None


class KubernetesWorkloadDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Uid: Optional[str] = None
    Namespace: Optional[str] = None
    HostNetwork: Optional[bool] = None
    Containers: Optional[List[Container]] = None
    Volumes: Optional[List[Volume]] = None
    ServiceAccountName: Optional[str] = None
    HostIPC: Optional[bool] = None
    HostPID: Optional[bool] = None


class MalwareScanDetails(BaseValidatorModel):
    Threats: Optional[List[Threat]] = None


class RuntimeContext(BaseValidatorModel):
    ModifyingProcess: Optional[ProcessDetails] = None
    ModifiedAt: Optional[datetime] = None
    ScriptPath: Optional[str] = None
    LibraryPath: Optional[str] = None
    LdPreloadValue: Optional[str] = None
    SocketPath: Optional[str] = None
    RuncBinaryPath: Optional[str] = None
    ReleaseAgentPath: Optional[str] = None
    MountSource: Optional[str] = None
    MountTarget: Optional[str] = None
    FileSystemType: Optional[str] = None
    Flags: Optional[List[str]] = None
    ModuleName: Optional[str] = None
    ModuleFilePath: Optional[str] = None
    ModuleSha256: Optional[str] = None
    ShellHistoryFilePath: Optional[str] = None
    TargetProcess: Optional[ProcessDetails] = None
    AddressFamily: Optional[str] = None
    IanaProtocolNumber: Optional[int] = None
    MemoryRegions: Optional[List[str]] = None
    ToolName: Optional[str] = None
    ToolCategory: Optional[str] = None
    ServiceName: Optional[str] = None
    CommandLineExample: Optional[str] = None
    ThreatFilePath: Optional[str] = None


class DataSourceConfigurations(BaseValidatorModel):
    S3Logs: Optional[S3LogsConfiguration] = None
    Kubernetes: Optional[KubernetesConfiguration] = None
    MalwareProtection: Optional[MalwareProtectionConfiguration] = None


class GetMalwareProtectionPlanResponse(BaseValidatorModel):
    Arn: str
    Role: str
    ProtectedResource: CreateProtectedResourceOutput
    Actions: MalwareProtectionPlanActions
    CreatedAt: datetime
    Status: MalwareProtectionPlanStatusType
    StatusReasons: List[MalwareProtectionPlanStatusReason]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class OrganizationMalwareProtectionConfigurationResult(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[OrganizationScanEc2InstanceWithFindingsResult] = None


class OrganizationMalwareProtectionConfiguration(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[OrganizationScanEc2InstanceWithFindings] = None


class OrganizationStatistics(BaseValidatorModel):
    TotalAccountsCount: Optional[int] = None
    MemberAccountsCount: Optional[int] = None
    ActiveAccountsCount: Optional[int] = None
    EnabledAccountsCount: Optional[int] = None
    CountByFeature: Optional[List[OrganizationFeatureStatistics]] = None


class AwsApiCallAction(BaseValidatorModel):
    Api: Optional[str] = None
    CallerType: Optional[str] = None
    DomainDetails: Optional[DomainDetails] = None
    ErrorCode: Optional[str] = None
    UserAgent: Optional[str] = None
    RemoteIpDetails: Optional[RemoteIpDetails] = None
    ServiceName: Optional[str] = None
    RemoteAccountDetails: Optional[RemoteAccountDetails] = None
    AffectedResources: Optional[Dict[str, str]] = None


class KubernetesApiCallAction(BaseValidatorModel):
    RequestUri: Optional[str] = None
    Verb: Optional[str] = None
    SourceIps: Optional[List[str]] = None
    UserAgent: Optional[str] = None
    RemoteIpDetails: Optional[RemoteIpDetails] = None
    StatusCode: Optional[int] = None
    Parameters: Optional[str] = None
    Resource: Optional[str] = None
    Subresource: Optional[str] = None
    Namespace: Optional[str] = None
    ResourceName: Optional[str] = None


class NetworkConnectionAction(BaseValidatorModel):
    Blocked: Optional[bool] = None
    ConnectionDirection: Optional[str] = None
    LocalPortDetails: Optional[LocalPortDetails] = None
    Protocol: Optional[str] = None
    LocalIpDetails: Optional[LocalIpDetails] = None
    LocalNetworkInterface: Optional[str] = None
    RemoteIpDetails: Optional[RemoteIpDetails] = None
    RemotePortDetails: Optional[RemotePortDetails] = None


class PortProbeDetail(BaseValidatorModel):
    LocalPortDetails: Optional[LocalPortDetails] = None
    LocalIpDetails: Optional[LocalIpDetails] = None
    RemoteIpDetails: Optional[RemoteIpDetails] = None


class RdsLoginAttemptAction(BaseValidatorModel):
    RemoteIpDetails: Optional[RemoteIpDetails] = None
    LoginAttributes: Optional[List[LoginAttribute]] = None


class ResourceData(BaseValidatorModel):
    S3Bucket: Optional[S3Bucket] = None
    Ec2Instance: Optional[Ec2Instance] = None
    AccessKey: Optional[AccessKey] = None
    Ec2NetworkInterface: Optional[Ec2NetworkInterface] = None
    S3Object: Optional[S3Object] = None


class ScanResourceCriteriaOutput(BaseValidatorModel):
    Include: Optional[Dict[Literal['EC2_INSTANCE_TAG'], ScanConditionOutput]] = None
    Exclude: Optional[Dict[Literal['EC2_INSTANCE_TAG'], ScanConditionOutput]] = None


class ScanResourceCriteria(BaseValidatorModel):
    Include: Optional[Dict[Literal['EC2_INSTANCE_TAG'], ScanCondition]] = None
    Exclude: Optional[Dict[Literal['EC2_INSTANCE_TAG'], ScanCondition]] = None


class ThreatDetectedByName(BaseValidatorModel):
    ItemCount: Optional[int] = None
    UniqueThreatNameCount: Optional[int] = None
    Shortened: Optional[bool] = None
    ThreatNames: Optional[List[ScanThreatName]] = None


class DescribeMalwareScansResponse(BaseValidatorModel):
    Scans: List[Scan]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UsageTopAccountsResult(BaseValidatorModel):
    Feature: Optional[UsageFeatureType] = None
    Accounts: Optional[List[UsageTopAccountResult]] = None


class UpdateMalwareProtectionPlanRequest(BaseValidatorModel):
    MalwareProtectionPlanId: str
    Role: Optional[str] = None
    Actions: Optional[MalwareProtectionPlanActions] = None
    ProtectedResource: Optional[UpdateProtectedResource] = None


class Anomaly(BaseValidatorModel):
    Profiles: Optional[Dict[str, Dict[str, List[AnomalyObject]]]] = None
    Unusual: Optional[AnomalyUnusual] = None


class PublicAccess(BaseValidatorModel):
    PermissionConfiguration: Optional[PermissionConfiguration] = None
    EffectivePermission: Optional[str] = None


class CreateFilterRequest(BaseValidatorModel):
    DetectorId: str
    Name: str
    FindingCriteria: FindingCriteriaUnion
    Description: Optional[str] = None
    Action: Optional[FilterActionType] = None
    Rank: Optional[int] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class GetFindingsStatisticsRequest(BaseValidatorModel):
    DetectorId: str
    FindingStatisticTypes: Optional[List[Literal['COUNT_BY_SEVERITY']]] = None
    FindingCriteria: Optional[FindingCriteriaUnion] = None
    GroupBy: Optional[GroupByTypeType] = None
    OrderBy: Optional[OrderByType] = None
    MaxResults: Optional[int] = None


class ListFindingsRequestPaginate(BaseValidatorModel):
    DetectorId: str
    FindingCriteria: Optional[FindingCriteriaUnion] = None
    SortCriteria: Optional[SortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingsRequest(BaseValidatorModel):
    DetectorId: str
    FindingCriteria: Optional[FindingCriteriaUnion] = None
    SortCriteria: Optional[SortCriteria] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class UpdateFilterRequest(BaseValidatorModel):
    DetectorId: str
    FilterName: str
    Description: Optional[str] = None
    Action: Optional[FilterActionType] = None
    Rank: Optional[int] = None
    FindingCriteria: Optional[FindingCriteriaUnion] = None


class CoverageResource(BaseValidatorModel):
    ResourceId: Optional[str] = None
    DetectorId: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceDetails: Optional[CoverageResourceDetails] = None
    CoverageStatus: Optional[CoverageStatusType] = None
    Issue: Optional[str] = None
    UpdatedAt: Optional[datetime] = None


class GetCoverageStatisticsRequest(BaseValidatorModel):
    DetectorId: str
    StatisticsType: List[CoverageStatisticsTypeType]
    FilterCriteria: Optional[CoverageFilterCriteria] = None


class ListCoverageRequestPaginate(BaseValidatorModel):
    DetectorId: str
    FilterCriteria: Optional[CoverageFilterCriteria] = None
    SortCriteria: Optional[CoverageSortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCoverageRequest(BaseValidatorModel):
    DetectorId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FilterCriteria: Optional[CoverageFilterCriteria] = None
    SortCriteria: Optional[CoverageSortCriteria] = None


class CreateMalwareProtectionPlanRequest(BaseValidatorModel):
    Role: str
    ProtectedResource: CreateProtectedResourceUnion
    ClientToken: Optional[str] = None
    Actions: Optional[MalwareProtectionPlanActions] = None
    Tags: Optional[Dict[str, str]] = None


class AccountFreeTrialInfo(BaseValidatorModel):
    AccountId: Optional[str] = None
    DataSources: Optional[DataSourcesFreeTrial] = None
    Features: Optional[List[FreeTrialFeatureConfigurationResult]] = None


class DataSourceConfigurationsResult(BaseValidatorModel):
    CloudTrail: CloudTrailConfigurationResult
    DNSLogs: DNSLogsConfigurationResult
    FlowLogs: FlowLogsConfigurationResult
    S3Logs: S3LogsConfigurationResult
    Kubernetes: Optional[KubernetesConfigurationResult] = None
    MalwareProtection: Optional[MalwareProtectionConfigurationResult] = None


class UnprocessedDataSourcesResult(BaseValidatorModel):
    MalwareProtection: Optional[MalwareProtectionConfigurationResult] = None


class DescribeMalwareScansRequestPaginate(BaseValidatorModel):
    DetectorId: str
    FilterCriteria: Optional[FilterCriteria] = None
    SortCriteria: Optional[SortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMalwareScansRequest(BaseValidatorModel):
    DetectorId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FilterCriteria: Optional[FilterCriteria] = None
    SortCriteria: Optional[SortCriteria] = None


class EcsClusterDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Status: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Tags: Optional[List[Tag]] = None
    TaskDetails: Optional[EcsTaskDetails] = None


class KubernetesDetails(BaseValidatorModel):
    KubernetesUserDetails: Optional[KubernetesUserDetails] = None
    KubernetesWorkloadDetails: Optional[KubernetesWorkloadDetails] = None


class RuntimeDetails(BaseValidatorModel):
    Process: Optional[ProcessDetails] = None
    Context: Optional[RuntimeContext] = None


class CreateDetectorRequest(BaseValidatorModel):
    Enable: bool
    ClientToken: Optional[str] = None
    FindingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    DataSources: Optional[DataSourceConfigurations] = None
    Tags: Optional[Dict[str, str]] = None
    Features: Optional[List[DetectorFeatureConfiguration]] = None


class UpdateDetectorRequest(BaseValidatorModel):
    DetectorId: str
    Enable: Optional[bool] = None
    FindingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    DataSources: Optional[DataSourceConfigurations] = None
    Features: Optional[List[DetectorFeatureConfiguration]] = None


class UpdateMemberDetectorsRequest(BaseValidatorModel):
    DetectorId: str
    AccountIds: List[str]
    DataSources: Optional[DataSourceConfigurations] = None
    Features: Optional[List[MemberFeaturesConfiguration]] = None


class OrganizationDataSourceConfigurationsResult(BaseValidatorModel):
    S3Logs: OrganizationS3LogsConfigurationResult
    Kubernetes: Optional[OrganizationKubernetesConfigurationResult] = None
    MalwareProtection: Optional[OrganizationMalwareProtectionConfigurationResult] = None


class OrganizationDataSourceConfigurations(BaseValidatorModel):
    S3Logs: Optional[OrganizationS3LogsConfiguration] = None
    Kubernetes: Optional[OrganizationKubernetesConfiguration] = None
    MalwareProtection: Optional[OrganizationMalwareProtectionConfiguration] = None


class OrganizationDetails(BaseValidatorModel):
    UpdatedAt: Optional[datetime] = None
    OrganizationStatistics: Optional[OrganizationStatistics] = None


class PortProbeAction(BaseValidatorModel):
    Blocked: Optional[bool] = None
    PortProbeDetails: Optional[List[PortProbeDetail]] = None


class ResourceV2(BaseValidatorModel):
    Uid: str
    ResourceType: FindingResourceTypeType
    Name: Optional[str] = None
    AccountId: Optional[str] = None
    Region: Optional[str] = None
    Service: Optional[str] = None
    CloudPartition: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Data: Optional[ResourceData] = None


class GetMalwareScanSettingsResponse(BaseValidatorModel):
    ScanResourceCriteria: ScanResourceCriteriaOutput
    EbsSnapshotPreservation: EbsSnapshotPreservationType
    ResponseMetadata: ResponseMetadata

ScanResourceCriteriaUnion = Union[ScanResourceCriteria, ScanResourceCriteriaOutput]


class ScanDetections(BaseValidatorModel):
    ScannedItemCount: Optional[ScannedItemCount] = None
    ThreatsDetectedItemCount: Optional[ThreatsDetectedItemCount] = None
    HighestSeverityThreatDetails: Optional[HighestSeverityThreatDetails] = None
    ThreatDetectedByName: Optional[ThreatDetectedByName] = None


class UsageStatistics(BaseValidatorModel):
    SumByAccount: Optional[List[UsageAccountResult]] = None
    TopAccountsByFeature: Optional[List[UsageTopAccountsResult]] = None
    SumByDataSource: Optional[List[UsageDataSourceResult]] = None
    SumByResource: Optional[List[UsageResourceResult]] = None
    TopResources: Optional[List[UsageResourceResult]] = None
    SumByFeature: Optional[List[UsageFeatureResult]] = None


class S3BucketDetail(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Owner: Optional[Owner] = None
    Tags: Optional[List[Tag]] = None
    DefaultServerSideEncryption: Optional[DefaultServerSideEncryption] = None
    PublicAccess: Optional[PublicAccess] = None
    S3ObjectDetails: Optional[List[S3ObjectDetail]] = None


class ListCoverageResponse(BaseValidatorModel):
    Resources: List[CoverageResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetRemainingFreeTrialDaysResponse(BaseValidatorModel):
    Accounts: List[AccountFreeTrialInfo]
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class GetDetectorResponse(BaseValidatorModel):
    CreatedAt: str
    FindingPublishingFrequency: FindingPublishingFrequencyType
    ServiceRole: str
    Status: DetectorStatusType
    UpdatedAt: str
    DataSources: DataSourceConfigurationsResult
    Tags: Dict[str, str]
    Features: List[DetectorFeatureConfigurationResult]
    ResponseMetadata: ResponseMetadata


class MemberDataSourceConfiguration(BaseValidatorModel):
    AccountId: str
    DataSources: Optional[DataSourceConfigurationsResult] = None
    Features: Optional[List[MemberFeaturesConfigurationResult]] = None


class CreateDetectorResponse(BaseValidatorModel):
    DetectorId: str
    UnprocessedDataSources: UnprocessedDataSourcesResult
    ResponseMetadata: ResponseMetadata


class DescribeOrganizationConfigurationResponse(BaseValidatorModel):
    AutoEnable: bool
    MemberAccountLimitReached: bool
    DataSources: OrganizationDataSourceConfigurationsResult
    Features: List[OrganizationFeatureConfigurationResult]
    AutoEnableOrganizationMembers: AutoEnableMembersType
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateOrganizationConfigurationRequest(BaseValidatorModel):
    DetectorId: str
    AutoEnable: Optional[bool] = None
    DataSources: Optional[OrganizationDataSourceConfigurations] = None
    Features: Optional[List[OrganizationFeatureConfiguration]] = None
    AutoEnableOrganizationMembers: Optional[AutoEnableMembersType] = None


class GetOrganizationStatisticsResponse(BaseValidatorModel):
    OrganizationDetails: OrganizationDetails
    ResponseMetadata: ResponseMetadata


class Action(BaseValidatorModel):
    ActionType: Optional[str] = None
    AwsApiCallAction: Optional[AwsApiCallAction] = None
    DnsRequestAction: Optional[DnsRequestAction] = None
    NetworkConnectionAction: Optional[NetworkConnectionAction] = None
    PortProbeAction: Optional[PortProbeAction] = None
    KubernetesApiCallAction: Optional[KubernetesApiCallAction] = None
    RdsLoginAttemptAction: Optional[RdsLoginAttemptAction] = None
    KubernetesPermissionCheckedDetails: Optional[KubernetesPermissionCheckedDetails] = None
    KubernetesRoleBindingDetails: Optional[KubernetesRoleBindingDetails] = None
    KubernetesRoleDetails: Optional[KubernetesRoleDetails] = None


class Sequence(BaseValidatorModel):
    Uid: str
    Description: str
    Signals: List[Signal]
    Actors: Optional[List[Actor]] = None
    Resources: Optional[List[ResourceV2]] = None
    Endpoints: Optional[List[NetworkEndpoint]] = None
    SequenceIndicators: Optional[List[Indicator]] = None


class UpdateMalwareScanSettingsRequest(BaseValidatorModel):
    DetectorId: str
    ScanResourceCriteria: Optional[ScanResourceCriteriaUnion] = None
    EbsSnapshotPreservation: Optional[EbsSnapshotPreservationType] = None


class EbsVolumeScanDetails(BaseValidatorModel):
    ScanId: Optional[str] = None
    ScanStartedAt: Optional[datetime] = None
    ScanCompletedAt: Optional[datetime] = None
    TriggerFindingId: Optional[str] = None
    Sources: Optional[List[str]] = None
    ScanDetections: Optional[ScanDetections] = None
    ScanType: Optional[ScanTypeType] = None


class GetUsageStatisticsResponse(BaseValidatorModel):
    UsageStatistics: UsageStatistics
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Resource(BaseValidatorModel):
    AccessKeyDetails: Optional[AccessKeyDetails] = None
    S3BucketDetails: Optional[List[S3BucketDetail]] = None
    InstanceDetails: Optional[InstanceDetails] = None
    EksClusterDetails: Optional[EksClusterDetails] = None
    KubernetesDetails: Optional[KubernetesDetails] = None
    ResourceType: Optional[str] = None
    EbsVolumeDetails: Optional[EbsVolumeDetails] = None
    EcsClusterDetails: Optional[EcsClusterDetails] = None
    ContainerDetails: Optional[Container] = None
    RdsDbInstanceDetails: Optional[RdsDbInstanceDetails] = None
    RdsLimitlessDbDetails: Optional[RdsLimitlessDbDetails] = None
    RdsDbUserDetails: Optional[RdsDbUserDetails] = None
    LambdaDetails: Optional[LambdaDetails] = None


class GetMemberDetectorsResponse(BaseValidatorModel):
    MemberDataSourceConfigurations: List[MemberDataSourceConfiguration]
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class Detection(BaseValidatorModel):
    Anomaly: Optional[Anomaly] = None
    Sequence: Optional[Sequence] = None


class Service(BaseValidatorModel):
    Action: Optional[Action] = None
    Evidence: Optional[Evidence] = None
    Archived: Optional[bool] = None
    Count: Optional[int] = None
    DetectorId: Optional[str] = None
    EventFirstSeen: Optional[str] = None
    EventLastSeen: Optional[str] = None
    ResourceRole: Optional[str] = None
    ServiceName: Optional[str] = None
    UserFeedback: Optional[str] = None
    AdditionalInfo: Optional[ServiceAdditionalInfo] = None
    FeatureName: Optional[str] = None
    EbsVolumeScanDetails: Optional[EbsVolumeScanDetails] = None
    RuntimeDetails: Optional[RuntimeDetails] = None
    Detection: Optional[Detection] = None
    MalwareScanDetails: Optional[MalwareScanDetails] = None


class Finding(BaseValidatorModel):
    AccountId: str
    Arn: str
    CreatedAt: str
    Id: str
    Region: str
    Resource: Resource
    SchemaVersion: str
    Severity: float
    Type: str
    UpdatedAt: str
    Confidence: Optional[float] = None
    Description: Optional[str] = None
    Partition: Optional[str] = None
    Service: Optional[Service] = None
    Title: Optional[str] = None
    AssociatedAttackSequenceArn: Optional[str] = None


class GetFindingsResponse(BaseValidatorModel):
    Findings: List[Finding]
    ResponseMetadata: ResponseMetadata
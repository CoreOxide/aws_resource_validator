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
from aws_resource_validator.pydantic_models.guardduty_constants import *

class AcceptAdministratorInvitationRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AdministratorId: str
    InvitationId: str


class AcceptInvitationRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    MasterId: str
    InvitationId: str


class AccessControlListTypeDef(BaseValidatorModel):
    AllowsPublicReadAccess: Optional[bool] = None
    AllowsPublicWriteAccess: Optional[bool] = None


class AccessKeyDetailsTypeDef(BaseValidatorModel):
    AccessKeyId: Optional[str] = None
    PrincipalId: Optional[str] = None
    UserName: Optional[str] = None
    UserType: Optional[str] = None


class AccessKeyTypeDef(BaseValidatorModel):
    PrincipalId: Optional[str] = None
    UserName: Optional[str] = None
    UserType: Optional[str] = None


class AccountDetailTypeDef(BaseValidatorModel):
    AccountId: str
    Email: str


class FreeTrialFeatureConfigurationResultTypeDef(BaseValidatorModel):
    Name: Optional[FreeTrialFeatureResultType] = None
    FreeTrialDaysRemaining: Optional[int] = None


class BlockPublicAccessTypeDef(BaseValidatorModel):
    IgnorePublicAcls: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None
    BlockPublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None


class AccountStatisticsTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    LastGeneratedAt: Optional[datetime] = None
    TotalFindings: Optional[int] = None


class AccountTypeDef(BaseValidatorModel):
    Uid: str
    Name: Optional[str] = None


class KubernetesPermissionCheckedDetailsTypeDef(BaseValidatorModel):
    Verb: Optional[str] = None
    Resource: Optional[str] = None
    Namespace: Optional[str] = None
    Allowed: Optional[bool] = None


class KubernetesRoleBindingDetailsTypeDef(BaseValidatorModel):
    Kind: Optional[str] = None
    Name: Optional[str] = None
    Uid: Optional[str] = None
    RoleRefName: Optional[str] = None
    RoleRefKind: Optional[str] = None


class KubernetesRoleDetailsTypeDef(BaseValidatorModel):
    Kind: Optional[str] = None
    Name: Optional[str] = None
    Uid: Optional[str] = None


class SessionTypeDef(BaseValidatorModel):
    Uid: Optional[str] = None
    MfaStatus: Optional[MfaStatusType] = None
    CreatedTime: Optional[datetime] = None
    Issuer: Optional[str] = None


class AddonDetailsTypeDef(BaseValidatorModel):
    AddonVersion: Optional[str] = None
    AddonStatus: Optional[str] = None


class AdminAccountTypeDef(BaseValidatorModel):
    AdminAccountId: Optional[str] = None
    AdminStatus: Optional[AdminStatusType] = None


class AdministratorTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    RelationshipStatus: Optional[str] = None
    InvitedAt: Optional[str] = None


class AgentDetailsTypeDef(BaseValidatorModel):
    Version: Optional[str] = None


class ArchiveFindingsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FindingIds: Sequence[str]


class AutonomousSystemTypeDef(BaseValidatorModel):
    Name: str
    Number: int


class DomainDetailsTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None


class RemoteAccountDetailsTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Affiliated: Optional[bool] = None


class BucketPolicyTypeDef(BaseValidatorModel):
    AllowsPublicReadAccess: Optional[bool] = None
    AllowsPublicWriteAccess: Optional[bool] = None


class CityTypeDef(BaseValidatorModel):
    CityName: Optional[str] = None


class CloudTrailConfigurationResultTypeDef(BaseValidatorModel):
    Status: DataSourceStatusType


class ConditionOutputTypeDef(BaseValidatorModel):
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


class ConditionTypeDef(BaseValidatorModel):
    Eq: Optional[Sequence[str]] = None
    Neq: Optional[Sequence[str]] = None
    Gt: Optional[int] = None
    Gte: Optional[int] = None
    Lt: Optional[int] = None
    Lte: Optional[int] = None
    Equals: Optional[Sequence[str]] = None
    NotEquals: Optional[Sequence[str]] = None
    GreaterThan: Optional[int] = None
    GreaterThanOrEqual: Optional[int] = None
    LessThan: Optional[int] = None
    LessThanOrEqual: Optional[int] = None


class ContainerInstanceDetailsTypeDef(BaseValidatorModel):
    CoveredContainerInstances: Optional[int] = None
    CompatibleContainerInstances: Optional[int] = None


class SecurityContextTypeDef(BaseValidatorModel):
    Privileged: Optional[bool] = None
    AllowPrivilegeEscalation: Optional[bool] = None


class VolumeMountTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    MountPath: Optional[str] = None


class CountryTypeDef(BaseValidatorModel):
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None


class FargateDetailsTypeDef(BaseValidatorModel):
    Issues: Optional[List[str]] = None
    ManagementType: Optional[ManagementTypeType] = None


class CoverageFilterConditionTypeDef(BaseValidatorModel):
    Equals: Optional[Sequence[str]] = None
    NotEquals: Optional[Sequence[str]] = None


class CoverageSortCriteriaTypeDef(BaseValidatorModel):
    AttributeName: Optional[CoverageSortKeyType] = None
    OrderBy: Optional[OrderByType] = None


class CoverageStatisticsTypeDef(BaseValidatorModel):
    CountByResourceType: Optional[Dict[ResourceTypeType, int]] = None
    CountByCoverageStatus: Optional[Dict[CoverageStatusType, int]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateIPSetRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    Name: str
    Format: IpSetFormatType
    Location: str
    Activate: bool
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UnprocessedAccountTypeDef(BaseValidatorModel):
    AccountId: str
    Result: str


class CreateS3BucketResourceOutputTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectPrefixes: Optional[List[str]] = None


class CreateS3BucketResourceTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectPrefixes: Optional[Sequence[str]] = None


class DestinationPropertiesTypeDef(BaseValidatorModel):
    DestinationArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class CreateSampleFindingsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FindingTypes: Optional[Sequence[str]] = None


class CreateThreatIntelSetRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    Name: str
    Format: ThreatIntelSetFormatType
    Location: str
    Activate: bool
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class DNSLogsConfigurationResultTypeDef(BaseValidatorModel):
    Status: DataSourceStatusType


class FlowLogsConfigurationResultTypeDef(BaseValidatorModel):
    Status: DataSourceStatusType


class S3LogsConfigurationResultTypeDef(BaseValidatorModel):
    Status: DataSourceStatusType


class S3LogsConfigurationTypeDef(BaseValidatorModel):
    Enable: bool


class DataSourceFreeTrialTypeDef(BaseValidatorModel):
    FreeTrialDaysRemaining: Optional[int] = None


class DateStatisticsTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    LastGeneratedAt: Optional[datetime] = None
    Severity: Optional[float] = None
    TotalFindings: Optional[int] = None


class DeclineInvitationsRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]


class DefaultServerSideEncryptionTypeDef(BaseValidatorModel):
    EncryptionType: Optional[str] = None
    KmsMasterKeyArn: Optional[str] = None


class DeleteDetectorRequestTypeDef(BaseValidatorModel):
    DetectorId: str


class DeleteFilterRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FilterName: str


class DeleteIPSetRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    IpSetId: str


class DeleteInvitationsRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]


class DeleteMalwareProtectionPlanRequestTypeDef(BaseValidatorModel):
    MalwareProtectionPlanId: str


class DeleteMembersRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountIds: Sequence[str]


class DeletePublishingDestinationRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    DestinationId: str


class DeleteThreatIntelSetRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    ThreatIntelSetId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class SortCriteriaTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    OrderBy: Optional[OrderByType] = None


class DescribeOrganizationConfigurationRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePublishingDestinationRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    DestinationId: str


class DestinationTypeDef(BaseValidatorModel):
    DestinationId: str
    DestinationType: Literal["S3"]
    Status: PublishingStatusType


class DetectorAdditionalConfigurationResultTypeDef(BaseValidatorModel):
    Name: Optional[FeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None


class DetectorAdditionalConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[FeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None


class DisableOrganizationAdminAccountRequestTypeDef(BaseValidatorModel):
    AdminAccountId: str


class DisassociateFromAdministratorAccountRequestTypeDef(BaseValidatorModel):
    DetectorId: str


class DisassociateFromMasterAccountRequestTypeDef(BaseValidatorModel):
    DetectorId: str


class DisassociateMembersRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountIds: Sequence[str]


class VolumeDetailTypeDef(BaseValidatorModel):
    VolumeArn: Optional[str] = None
    VolumeType: Optional[str] = None
    DeviceName: Optional[str] = None
    VolumeSizeInGB: Optional[int] = None
    EncryptionType: Optional[str] = None
    SnapshotArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class EbsVolumesResultTypeDef(BaseValidatorModel):
    Status: Optional[DataSourceStatusType] = None
    Reason: Optional[str] = None


class IamInstanceProfileTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None


class ProductCodeTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    ProductType: Optional[str] = None


class PrivateIpAddressDetailsTypeDef(BaseValidatorModel):
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None


class SecurityGroupTypeDef(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class EnableOrganizationAdminAccountRequestTypeDef(BaseValidatorModel):
    AdminAccountId: str


class ThreatIntelligenceDetailTypeDef(BaseValidatorModel):
    ThreatListName: Optional[str] = None
    ThreatNames: Optional[List[str]] = None
    ThreatFileSha256: Optional[str] = None


class FilterConditionTypeDef(BaseValidatorModel):
    EqualsValue: Optional[str] = None
    GreaterThan: Optional[int] = None
    LessThan: Optional[int] = None


class FindingTypeStatisticsTypeDef(BaseValidatorModel):
    FindingType: Optional[str] = None
    LastGeneratedAt: Optional[datetime] = None
    TotalFindings: Optional[int] = None


class ResourceStatisticsTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    LastGeneratedAt: Optional[datetime] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    TotalFindings: Optional[int] = None


class SeverityStatisticsTypeDef(BaseValidatorModel):
    LastGeneratedAt: Optional[datetime] = None
    Severity: Optional[float] = None
    TotalFindings: Optional[int] = None


class GeoLocationTypeDef(BaseValidatorModel):
    Lat: Optional[float] = None
    Lon: Optional[float] = None


class GetAdministratorAccountRequestTypeDef(BaseValidatorModel):
    DetectorId: str


class GetDetectorRequestTypeDef(BaseValidatorModel):
    DetectorId: str


class GetFilterRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FilterName: str


class GetIPSetRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    IpSetId: str


class GetMalwareProtectionPlanRequestTypeDef(BaseValidatorModel):
    MalwareProtectionPlanId: str


class MalwareProtectionPlanStatusReasonTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class GetMalwareScanSettingsRequestTypeDef(BaseValidatorModel):
    DetectorId: str


class GetMasterAccountRequestTypeDef(BaseValidatorModel):
    DetectorId: str


class MasterTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    RelationshipStatus: Optional[str] = None
    InvitedAt: Optional[str] = None


class GetMemberDetectorsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountIds: Sequence[str]


class GetMembersRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountIds: Sequence[str]


class MemberTypeDef(BaseValidatorModel):
    AccountId: str
    MasterId: str
    Email: str
    RelationshipStatus: str
    UpdatedAt: str
    DetectorId: Optional[str] = None
    InvitedAt: Optional[str] = None
    AdministratorId: Optional[str] = None


class GetRemainingFreeTrialDaysRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountIds: Optional[Sequence[str]] = None


class GetThreatIntelSetRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    ThreatIntelSetId: str


class UsageCriteriaTypeDef(BaseValidatorModel):
    AccountIds: Optional[Sequence[str]] = None
    DataSources: Optional[Sequence[DataSourceType]] = None
    Resources: Optional[Sequence[str]] = None
    Features: Optional[Sequence[UsageFeatureType]] = None


class HighestSeverityThreatDetailsTypeDef(BaseValidatorModel):
    Severity: Optional[str] = None
    ThreatName: Optional[str] = None
    Count: Optional[int] = None


class HostPathTypeDef(BaseValidatorModel):
    Path: Optional[str] = None


class ImpersonatedUserTypeDef(BaseValidatorModel):
    Username: Optional[str] = None
    Groups: Optional[List[str]] = None


class IndicatorTypeDef(BaseValidatorModel):
    Key: IndicatorTypeType
    Values: Optional[List[str]] = None
    Title: Optional[str] = None


class InvitationTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    RelationshipStatus: Optional[str] = None
    InvitedAt: Optional[str] = None


class InviteMembersRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountIds: Sequence[str]
    DisableEmailNotification: Optional[bool] = None
    Message: Optional[str] = None


class ItemPathTypeDef(BaseValidatorModel):
    NestedItemPath: Optional[str] = None
    Hash: Optional[str] = None


class KubernetesAuditLogsConfigurationResultTypeDef(BaseValidatorModel):
    Status: DataSourceStatusType


class KubernetesAuditLogsConfigurationTypeDef(BaseValidatorModel):
    Enable: bool


class LineageObjectTypeDef(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    NamespacePid: Optional[int] = None
    UserId: Optional[int] = None
    Name: Optional[str] = None
    Pid: Optional[int] = None
    Uuid: Optional[str] = None
    ExecutablePath: Optional[str] = None
    Euid: Optional[int] = None
    ParentUuid: Optional[str] = None


class ListDetectorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFiltersRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListIPSetsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInvitationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMalwareProtectionPlansRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class MalwareProtectionPlanSummaryTypeDef(BaseValidatorModel):
    MalwareProtectionPlanId: Optional[str] = None


class ListMembersRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OnlyAssociated: Optional[str] = None


class ListOrganizationAdminAccountsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPublishingDestinationsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListThreatIntelSetsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LocalIpDetailsTypeDef(BaseValidatorModel):
    IpAddressV4: Optional[str] = None
    IpAddressV6: Optional[str] = None


class LocalPortDetailsTypeDef(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None


class LoginAttributeTypeDef(BaseValidatorModel):
    User: Optional[str] = None
    Application: Optional[str] = None
    FailedLoginAttempts: Optional[int] = None
    SuccessfulLoginAttempts: Optional[int] = None


class ScanEc2InstanceWithFindingsTypeDef(BaseValidatorModel):
    EbsVolumes: Optional[bool] = None


class MalwareProtectionPlanTaggingActionTypeDef(BaseValidatorModel):
    Status: Optional[MalwareProtectionPlanTaggingActionStatusType] = None


class MemberAdditionalConfigurationResultTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None


class MemberAdditionalConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None


class RemotePortDetailsTypeDef(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None


class NetworkConnectionTypeDef(BaseValidatorModel):
    Direction: NetworkDirectionType


class NetworkGeoLocationTypeDef(BaseValidatorModel):
    City: str
    Country: str
    Latitude: float
    Longitude: float


class OrganizationAdditionalConfigurationResultTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None


class OrganizationAdditionalConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None


class OrganizationS3LogsConfigurationResultTypeDef(BaseValidatorModel):
    AutoEnable: bool


class OrganizationS3LogsConfigurationTypeDef(BaseValidatorModel):
    AutoEnable: bool


class OrganizationEbsVolumesResultTypeDef(BaseValidatorModel):
    AutoEnable: Optional[bool] = None


class OrganizationEbsVolumesTypeDef(BaseValidatorModel):
    AutoEnable: Optional[bool] = None


class OrganizationFeatureStatisticsAdditionalConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    EnabledAccountsCount: Optional[int] = None


class OrganizationKubernetesAuditLogsConfigurationResultTypeDef(BaseValidatorModel):
    AutoEnable: bool


class OrganizationKubernetesAuditLogsConfigurationTypeDef(BaseValidatorModel):
    AutoEnable: bool


class OrganizationTypeDef(BaseValidatorModel):
    Asn: Optional[str] = None
    AsnOrg: Optional[str] = None
    Isp: Optional[str] = None
    Org: Optional[str] = None


class OwnerTypeDef(BaseValidatorModel):
    Id: Optional[str] = None


class PublicAccessConfigurationTypeDef(BaseValidatorModel):
    PublicAclAccess: Optional[PublicAccessStatusType] = None
    PublicPolicyAccess: Optional[PublicAccessStatusType] = None
    PublicAclIgnoreBehavior: Optional[PublicAclIgnoreBehaviorType] = None
    PublicBucketRestrictBehavior: Optional[PublicBucketRestrictBehaviorType] = None


class RdsDbUserDetailsTypeDef(BaseValidatorModel):
    User: Optional[str] = None
    Application: Optional[str] = None
    Database: Optional[str] = None
    Ssl: Optional[str] = None
    AuthMethod: Optional[str] = None


class S3ObjectTypeDef(BaseValidatorModel):
    ETag: Optional[str] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None


class ResourceDetailsTypeDef(BaseValidatorModel):
    InstanceArn: Optional[str] = None


class S3ObjectDetailTypeDef(BaseValidatorModel):
    ObjectArn: Optional[str] = None
    Key: Optional[str] = None
    ETag: Optional[str] = None
    Hash: Optional[str] = None
    VersionId: Optional[str] = None


class ScanConditionPairTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class ScannedItemCountTypeDef(BaseValidatorModel):
    TotalGb: Optional[int] = None
    Files: Optional[int] = None
    Volumes: Optional[int] = None


class ThreatsDetectedItemCountTypeDef(BaseValidatorModel):
    Files: Optional[int] = None


class ScanFilePathTypeDef(BaseValidatorModel):
    FilePath: Optional[str] = None
    VolumeArn: Optional[str] = None
    Hash: Optional[str] = None
    FileName: Optional[str] = None


class ScanResultDetailsTypeDef(BaseValidatorModel):
    ScanResult: Optional[ScanResultType] = None


class TriggerDetailsTypeDef(BaseValidatorModel):
    GuardDutyFindingId: Optional[str] = None
    Description: Optional[str] = None


class StartMalwareScanRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class StartMonitoringMembersRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountIds: Sequence[str]


class StopMonitoringMembersRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountIds: Sequence[str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class TotalTypeDef(BaseValidatorModel):
    Amount: Optional[str] = None
    Unit: Optional[str] = None


class UnarchiveFindingsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FindingIds: Sequence[str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateFindingsFeedbackRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FindingIds: Sequence[str]
    Feedback: FeedbackType
    Comments: Optional[str] = None


class UpdateIPSetRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    IpSetId: str
    Name: Optional[str] = None
    Location: Optional[str] = None
    Activate: Optional[bool] = None


class UpdateS3BucketResourceTypeDef(BaseValidatorModel):
    ObjectPrefixes: Optional[Sequence[str]] = None


class UpdateThreatIntelSetRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    ThreatIntelSetId: str
    Name: Optional[str] = None
    Location: Optional[str] = None
    Activate: Optional[bool] = None


class CreateMembersRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountDetails: Sequence[AccountDetailTypeDef]


class AccountLevelPermissionsTypeDef(BaseValidatorModel):
    BlockPublicAccess: Optional[BlockPublicAccessTypeDef] = None


class CoverageEksClusterDetailsTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    CoveredNodes: Optional[int] = None
    CompatibleNodes: Optional[int] = None
    AddonDetails: Optional[AddonDetailsTypeDef] = None
    ManagementType: Optional[ManagementTypeType] = None


class CoverageEc2InstanceDetailsTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    ClusterArn: Optional[str] = None
    AgentDetails: Optional[AgentDetailsTypeDef] = None
    ManagementType: Optional[ManagementTypeType] = None


class ObservationsTypeDef(BaseValidatorModel):
    pass


class AnomalyObjectTypeDef(BaseValidatorModel):
    ProfileType: Optional[Literal["FREQUENCY"]] = None
    ProfileSubtype: Optional[ProfileSubtypeType] = None
    Observations: Optional[ObservationsTypeDef] = None


class BucketLevelPermissionsTypeDef(BaseValidatorModel):
    AccessControlList: Optional[AccessControlListTypeDef] = None
    BucketPolicy: Optional[BucketPolicyTypeDef] = None
    BlockPublicAccess: Optional[BlockPublicAccessTypeDef] = None


class FindingCriteriaOutputTypeDef(BaseValidatorModel):
    Criterion: Optional[Dict[str, ConditionOutputTypeDef]] = None


class FindingCriteriaTypeDef(BaseValidatorModel):
    Criterion: Optional[Mapping[str, ConditionTypeDef]] = None


class ContainerTypeDef(BaseValidatorModel):
    ContainerRuntime: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Image: Optional[str] = None
    ImagePrefix: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMountTypeDef]] = None
    SecurityContext: Optional[SecurityContextTypeDef] = None


class CoverageEcsClusterDetailsTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    FargateDetails: Optional[FargateDetailsTypeDef] = None
    ContainerInstanceDetails: Optional[ContainerInstanceDetailsTypeDef] = None


class CoverageFilterCriterionTypeDef(BaseValidatorModel):
    CriterionKey: Optional[CoverageFilterCriterionKeyType] = None
    FilterCondition: Optional[CoverageFilterConditionTypeDef] = None


class CreateFilterResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIPSetResponseTypeDef(BaseValidatorModel):
    IpSetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMalwareProtectionPlanResponseTypeDef(BaseValidatorModel):
    MalwareProtectionPlanId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePublishingDestinationResponseTypeDef(BaseValidatorModel):
    DestinationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateThreatIntelSetResponseTypeDef(BaseValidatorModel):
    ThreatIntelSetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAdministratorAccountResponseTypeDef(BaseValidatorModel):
    Administrator: AdministratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCoverageStatisticsResponseTypeDef(BaseValidatorModel):
    CoverageStatistics: CoverageStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIPSetResponseTypeDef(BaseValidatorModel):
    Name: str
    Format: IpSetFormatType
    Location: str
    Status: IpSetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetInvitationsCountResponseTypeDef(BaseValidatorModel):
    InvitationsCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetThreatIntelSetResponseTypeDef(BaseValidatorModel):
    Name: str
    Format: ThreatIntelSetFormatType
    Location: str
    Status: ThreatIntelSetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDetectorsResponseTypeDef(BaseValidatorModel):
    DetectorIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFiltersResponseTypeDef(BaseValidatorModel):
    FilterNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFindingsResponseTypeDef(BaseValidatorModel):
    FindingIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListIPSetsResponseTypeDef(BaseValidatorModel):
    IpSetIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListOrganizationAdminAccountsResponseTypeDef(BaseValidatorModel):
    AdminAccounts: List[AdminAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListThreatIntelSetsResponseTypeDef(BaseValidatorModel):
    ThreatIntelSetIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StartMalwareScanResponseTypeDef(BaseValidatorModel):
    ScanId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFilterResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMembersResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeclineInvitationsResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInvitationsResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMembersResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateMembersResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class InviteMembersResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartMonitoringMembersResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StopMonitoringMembersResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMemberDetectorsResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProtectedResourceOutputTypeDef(BaseValidatorModel):
    S3Bucket: Optional[CreateS3BucketResourceOutputTypeDef] = None


class CreateProtectedResourceTypeDef(BaseValidatorModel):
    S3Bucket: Optional[CreateS3BucketResourceTypeDef] = None


class CreatePublishingDestinationRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    DestinationType: Literal["S3"]
    DestinationProperties: DestinationPropertiesTypeDef
    ClientToken: Optional[str] = None


class DescribePublishingDestinationResponseTypeDef(BaseValidatorModel):
    DestinationId: str
    DestinationType: Literal["S3"]
    Status: PublishingStatusType
    PublishingFailureStartTimestamp: int
    DestinationProperties: DestinationPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePublishingDestinationRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    DestinationId: str
    DestinationProperties: Optional[DestinationPropertiesTypeDef] = None


class KubernetesDataSourceFreeTrialTypeDef(BaseValidatorModel):
    AuditLogs: Optional[DataSourceFreeTrialTypeDef] = None


class MalwareProtectionDataSourceFreeTrialTypeDef(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[DataSourceFreeTrialTypeDef] = None


class ListDetectorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFiltersRequestPaginateTypeDef(BaseValidatorModel):
    DetectorId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIPSetsRequestPaginateTypeDef(BaseValidatorModel):
    DetectorId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInvitationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMembersRequestPaginateTypeDef(BaseValidatorModel):
    DetectorId: str
    OnlyAssociated: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrganizationAdminAccountsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThreatIntelSetsRequestPaginateTypeDef(BaseValidatorModel):
    DetectorId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetFindingsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FindingIds: Sequence[str]
    SortCriteria: Optional[SortCriteriaTypeDef] = None


class ListPublishingDestinationsResponseTypeDef(BaseValidatorModel):
    Destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DetectorFeatureConfigurationResultTypeDef(BaseValidatorModel):
    Name: Optional[DetectorFeatureResultType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None
    AdditionalConfiguration: Optional[List[DetectorAdditionalConfigurationResultTypeDef]] = None


class DetectorFeatureConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[DetectorFeatureType] = None
    Status: Optional[FeatureStatusType] = None
    AdditionalConfiguration: Optional[Sequence[DetectorAdditionalConfigurationTypeDef]] = None


class EbsVolumeDetailsTypeDef(BaseValidatorModel):
    ScannedVolumeDetails: Optional[List[VolumeDetailTypeDef]] = None
    SkippedVolumeDetails: Optional[List[VolumeDetailTypeDef]] = None


class ScanEc2InstanceWithFindingsResultTypeDef(BaseValidatorModel):
    EbsVolumes: Optional[EbsVolumesResultTypeDef] = None


class Ec2InstanceTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    ImageDescription: Optional[str] = None
    InstanceState: Optional[str] = None
    IamInstanceProfile: Optional[IamInstanceProfileTypeDef] = None
    InstanceType: Optional[str] = None
    OutpostArn: Optional[str] = None
    Platform: Optional[str] = None
    ProductCodes: Optional[List[ProductCodeTypeDef]] = None
    Ec2NetworkInterfaceUids: Optional[List[str]] = None


class Ec2NetworkInterfaceTypeDef(BaseValidatorModel):
    Ipv6Addresses: Optional[List[str]] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressDetailsTypeDef]] = None
    PublicIp: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroupTypeDef]] = None
    SubNetId: Optional[str] = None
    VpcId: Optional[str] = None


class NetworkInterfaceTypeDef(BaseValidatorModel):
    Ipv6Addresses: Optional[List[str]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressDetailsTypeDef]] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroupTypeDef]] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None


class VpcConfigTypeDef(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroupTypeDef]] = None


class EksClusterDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    VpcId: Optional[str] = None
    Status: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    CreatedAt: Optional[datetime] = None


class RdsDbInstanceDetailsTypeDef(BaseValidatorModel):
    DbInstanceIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None
    DbInstanceArn: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class RdsLimitlessDbDetailsTypeDef(BaseValidatorModel):
    DbShardGroupIdentifier: Optional[str] = None
    DbShardGroupResourceId: Optional[str] = None
    DbShardGroupArn: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class EvidenceTypeDef(BaseValidatorModel):
    ThreatIntelligenceDetails: Optional[List[ThreatIntelligenceDetailTypeDef]] = None


class FilterCriterionTypeDef(BaseValidatorModel):
    CriterionKey: Optional[CriterionKeyType] = None
    FilterCondition: Optional[FilterConditionTypeDef] = None


class FindingStatisticsTypeDef(BaseValidatorModel):
    CountBySeverity: Optional[Dict[str, int]] = None
    GroupedByAccount: Optional[List[AccountStatisticsTypeDef]] = None
    GroupedByDate: Optional[List[DateStatisticsTypeDef]] = None
    GroupedByFindingType: Optional[List[FindingTypeStatisticsTypeDef]] = None
    GroupedByResource: Optional[List[ResourceStatisticsTypeDef]] = None
    GroupedBySeverity: Optional[List[SeverityStatisticsTypeDef]] = None


class GetMasterAccountResponseTypeDef(BaseValidatorModel):
    Master: MasterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMembersResponseTypeDef(BaseValidatorModel):
    Members: List[MemberTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListMembersResponseTypeDef(BaseValidatorModel):
    Members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetUsageStatisticsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    UsageStatisticType: UsageStatisticTypeType
    UsageCriteria: UsageCriteriaTypeDef
    Unit: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class VolumeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    HostPath: Optional[HostPathTypeDef] = None


class KubernetesUserDetailsTypeDef(BaseValidatorModel):
    Username: Optional[str] = None
    Uid: Optional[str] = None
    Groups: Optional[List[str]] = None
    SessionName: Optional[List[str]] = None
    ImpersonatedUser: Optional[ImpersonatedUserTypeDef] = None


class ListInvitationsResponseTypeDef(BaseValidatorModel):
    Invitations: List[InvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ThreatTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Source: Optional[str] = None
    ItemPaths: Optional[List[ItemPathTypeDef]] = None


class KubernetesConfigurationResultTypeDef(BaseValidatorModel):
    AuditLogs: KubernetesAuditLogsConfigurationResultTypeDef


class KubernetesConfigurationTypeDef(BaseValidatorModel):
    AuditLogs: KubernetesAuditLogsConfigurationTypeDef


class ProcessDetailsTypeDef(BaseValidatorModel):
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
    Lineage: Optional[List[LineageObjectTypeDef]] = None


class ListMalwareProtectionPlansResponseTypeDef(BaseValidatorModel):
    MalwareProtectionPlans: List[MalwareProtectionPlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MalwareProtectionConfigurationTypeDef(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[ScanEc2InstanceWithFindingsTypeDef] = None


class MalwareProtectionPlanActionsTypeDef(BaseValidatorModel):
    Tagging: Optional[MalwareProtectionPlanTaggingActionTypeDef] = None


class MemberFeaturesConfigurationResultTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None
    AdditionalConfiguration: Optional[List[MemberAdditionalConfigurationResultTypeDef]] = None


class MemberFeaturesConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    Status: Optional[FeatureStatusType] = None
    AdditionalConfiguration: Optional[Sequence[MemberAdditionalConfigurationTypeDef]] = None


class NetworkEndpointTypeDef(BaseValidatorModel):
    Id: str
    Ip: Optional[str] = None
    Domain: Optional[str] = None
    Port: Optional[int] = None
    Location: Optional[NetworkGeoLocationTypeDef] = None
    AutonomousSystem: Optional[AutonomousSystemTypeDef] = None
    Connection: Optional[NetworkConnectionTypeDef] = None


class OrganizationFeatureConfigurationResultTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None
    AdditionalConfiguration: Optional[List[OrganizationAdditionalConfigurationResultTypeDef]] = None


class OrganizationFeatureConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None
    AdditionalConfiguration: Optional[Sequence[OrganizationAdditionalConfigurationTypeDef]] = None


class OrganizationScanEc2InstanceWithFindingsResultTypeDef(BaseValidatorModel):
    EbsVolumes: Optional[OrganizationEbsVolumesResultTypeDef] = None


class OrganizationScanEc2InstanceWithFindingsTypeDef(BaseValidatorModel):
    EbsVolumes: Optional[OrganizationEbsVolumesTypeDef] = None


class OrganizationFeatureStatisticsTypeDef(BaseValidatorModel):
    Name: Optional[OrgFeatureType] = None
    EnabledAccountsCount: Optional[int] = None
    AdditionalConfiguration: Optional[ List[OrganizationFeatureStatisticsAdditionalConfigurationTypeDef] ] = None


class OrganizationKubernetesConfigurationResultTypeDef(BaseValidatorModel):
    AuditLogs: OrganizationKubernetesAuditLogsConfigurationResultTypeDef


class OrganizationKubernetesConfigurationTypeDef(BaseValidatorModel):
    AuditLogs: OrganizationKubernetesAuditLogsConfigurationTypeDef


class RemoteIpDetailsTypeDef(BaseValidatorModel):
    City: Optional[CityTypeDef] = None
    Country: Optional[CountryTypeDef] = None
    GeoLocation: Optional[GeoLocationTypeDef] = None
    IpAddressV4: Optional[str] = None
    IpAddressV6: Optional[str] = None
    Organization: Optional[OrganizationTypeDef] = None


class S3BucketTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    EncryptionType: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    EffectivePermission: Optional[str] = None
    PublicReadAccess: Optional[PublicAccessStatusType] = None
    PublicWriteAccess: Optional[PublicAccessStatusType] = None
    AccountPublicAccess: Optional[PublicAccessConfigurationTypeDef] = None
    BucketPublicAccess: Optional[PublicAccessConfigurationTypeDef] = None
    S3ObjectUids: Optional[List[str]] = None


class ScanConditionOutputTypeDef(BaseValidatorModel):
    MapEquals: List[ScanConditionPairTypeDef]


class ScanConditionTypeDef(BaseValidatorModel):
    MapEquals: Sequence[ScanConditionPairTypeDef]


class ScanThreatNameTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[ScanFilePathTypeDef]] = None


class ScanTypeDef(BaseValidatorModel):
    DetectorId: Optional[str] = None
    AdminDetectorId: Optional[str] = None
    ScanId: Optional[str] = None
    ScanStatus: Optional[ScanStatusType] = None
    FailureReason: Optional[str] = None
    ScanStartTime: Optional[datetime] = None
    ScanEndTime: Optional[datetime] = None
    TriggerDetails: Optional[TriggerDetailsTypeDef] = None
    ResourceDetails: Optional[ResourceDetailsTypeDef] = None
    ScanResultDetails: Optional[ScanResultDetailsTypeDef] = None
    AccountId: Optional[str] = None
    TotalBytes: Optional[int] = None
    FileCount: Optional[int] = None
    AttachedVolumes: Optional[List[VolumeDetailTypeDef]] = None
    ScanType: Optional[ScanTypeType] = None


class UsageAccountResultTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Total: Optional[TotalTypeDef] = None


class UsageDataSourceResultTypeDef(BaseValidatorModel):
    DataSource: Optional[DataSourceType] = None
    Total: Optional[TotalTypeDef] = None


class UsageFeatureResultTypeDef(BaseValidatorModel):
    Feature: Optional[UsageFeatureType] = None
    Total: Optional[TotalTypeDef] = None


class UsageResourceResultTypeDef(BaseValidatorModel):
    Resource: Optional[str] = None
    Total: Optional[TotalTypeDef] = None


class UsageTopAccountResultTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Total: Optional[TotalTypeDef] = None


class UpdateProtectedResourceTypeDef(BaseValidatorModel):
    S3Bucket: Optional[UpdateS3BucketResourceTypeDef] = None


class UserTypeDef(BaseValidatorModel):
    pass


class ActorTypeDef(BaseValidatorModel):
    Id: str
    User: Optional[UserTypeDef] = None
    Session: Optional[SessionTypeDef] = None


class AnomalyUnusualTypeDef(BaseValidatorModel):
    Behavior: Optional[Dict[str, Dict[str, AnomalyObjectTypeDef]]] = None


class PermissionConfigurationTypeDef(BaseValidatorModel):
    BucketLevelPermissions: Optional[BucketLevelPermissionsTypeDef] = None
    AccountLevelPermissions: Optional[AccountLevelPermissionsTypeDef] = None


class GetFilterResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    Action: FilterActionType
    Rank: int
    FindingCriteria: FindingCriteriaOutputTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CoverageResourceDetailsTypeDef(BaseValidatorModel):
    EksClusterDetails: Optional[CoverageEksClusterDetailsTypeDef] = None
    ResourceType: Optional[ResourceTypeType] = None
    EcsClusterDetails: Optional[CoverageEcsClusterDetailsTypeDef] = None
    Ec2InstanceDetails: Optional[CoverageEc2InstanceDetailsTypeDef] = None


class CoverageFilterCriteriaTypeDef(BaseValidatorModel):
    FilterCriterion: Optional[Sequence[CoverageFilterCriterionTypeDef]] = None


class DataSourcesFreeTrialTypeDef(BaseValidatorModel):
    CloudTrail: Optional[DataSourceFreeTrialTypeDef] = None
    DnsLogs: Optional[DataSourceFreeTrialTypeDef] = None
    FlowLogs: Optional[DataSourceFreeTrialTypeDef] = None
    S3Logs: Optional[DataSourceFreeTrialTypeDef] = None
    Kubernetes: Optional[KubernetesDataSourceFreeTrialTypeDef] = None
    MalwareProtection: Optional[MalwareProtectionDataSourceFreeTrialTypeDef] = None


class MalwareProtectionConfigurationResultTypeDef(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[ScanEc2InstanceWithFindingsResultTypeDef] = None
    ServiceRole: Optional[str] = None


class InstanceDetailsTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    IamInstanceProfile: Optional[IamInstanceProfileTypeDef] = None
    ImageDescription: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceState: Optional[str] = None
    InstanceType: Optional[str] = None
    OutpostArn: Optional[str] = None
    LaunchTime: Optional[str] = None
    NetworkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    Platform: Optional[str] = None
    ProductCodes: Optional[List[ProductCodeTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None


class LambdaDetailsTypeDef(BaseValidatorModel):
    FunctionArn: Optional[str] = None
    FunctionName: Optional[str] = None
    Description: Optional[str] = None
    LastModifiedAt: Optional[datetime] = None
    RevisionId: Optional[str] = None
    FunctionVersion: Optional[str] = None
    Role: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None


class FilterCriteriaTypeDef(BaseValidatorModel):
    FilterCriterion: Optional[Sequence[FilterCriterionTypeDef]] = None


class GetFindingsStatisticsResponseTypeDef(BaseValidatorModel):
    FindingStatistics: FindingStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EcsTaskDetailsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    DefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    TaskCreatedAt: Optional[datetime] = None
    StartedAt: Optional[datetime] = None
    StartedBy: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    Volumes: Optional[List[VolumeTypeDef]] = None
    Containers: Optional[List[ContainerTypeDef]] = None
    Group: Optional[str] = None
    LaunchType: Optional[str] = None


class MalwareScanDetailsTypeDef(BaseValidatorModel):
    Threats: Optional[List[ThreatTypeDef]] = None


class DataSourceConfigurationsTypeDef(BaseValidatorModel):
    S3Logs: Optional[S3LogsConfigurationTypeDef] = None
    Kubernetes: Optional[KubernetesConfigurationTypeDef] = None
    MalwareProtection: Optional[MalwareProtectionConfigurationTypeDef] = None


class GetMalwareProtectionPlanResponseTypeDef(BaseValidatorModel):
    Arn: str
    Role: str
    ProtectedResource: CreateProtectedResourceOutputTypeDef
    Actions: MalwareProtectionPlanActionsTypeDef
    CreatedAt: datetime
    Status: MalwareProtectionPlanStatusType
    StatusReasons: List[MalwareProtectionPlanStatusReasonTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class OrganizationMalwareProtectionConfigurationResultTypeDef(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[OrganizationScanEc2InstanceWithFindingsResultTypeDef] = None


class OrganizationMalwareProtectionConfigurationTypeDef(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[OrganizationScanEc2InstanceWithFindingsTypeDef] = None


class OrganizationStatisticsTypeDef(BaseValidatorModel):
    TotalAccountsCount: Optional[int] = None
    MemberAccountsCount: Optional[int] = None
    ActiveAccountsCount: Optional[int] = None
    EnabledAccountsCount: Optional[int] = None
    CountByFeature: Optional[List[OrganizationFeatureStatisticsTypeDef]] = None


class KubernetesApiCallActionTypeDef(BaseValidatorModel):
    RequestUri: Optional[str] = None
    Verb: Optional[str] = None
    SourceIps: Optional[List[str]] = None
    UserAgent: Optional[str] = None
    RemoteIpDetails: Optional[RemoteIpDetailsTypeDef] = None
    StatusCode: Optional[int] = None
    Parameters: Optional[str] = None
    Resource: Optional[str] = None
    Subresource: Optional[str] = None
    Namespace: Optional[str] = None
    ResourceName: Optional[str] = None


class PortProbeDetailTypeDef(BaseValidatorModel):
    LocalPortDetails: Optional[LocalPortDetailsTypeDef] = None
    LocalIpDetails: Optional[LocalIpDetailsTypeDef] = None
    RemoteIpDetails: Optional[RemoteIpDetailsTypeDef] = None


class RdsLoginAttemptActionTypeDef(BaseValidatorModel):
    RemoteIpDetails: Optional[RemoteIpDetailsTypeDef] = None
    LoginAttributes: Optional[List[LoginAttributeTypeDef]] = None


class ResourceDataTypeDef(BaseValidatorModel):
    S3Bucket: Optional[S3BucketTypeDef] = None
    Ec2Instance: Optional[Ec2InstanceTypeDef] = None
    AccessKey: Optional[AccessKeyTypeDef] = None
    Ec2NetworkInterface: Optional[Ec2NetworkInterfaceTypeDef] = None
    S3Object: Optional[S3ObjectTypeDef] = None


class ScanResourceCriteriaOutputTypeDef(BaseValidatorModel):
    Include: Optional[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionOutputTypeDef]] = None
    Exclude: Optional[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionOutputTypeDef]] = None


class ScanResourceCriteriaTypeDef(BaseValidatorModel):
    Include: Optional[Mapping[Literal["EC2_INSTANCE_TAG"], ScanConditionTypeDef]] = None
    Exclude: Optional[Mapping[Literal["EC2_INSTANCE_TAG"], ScanConditionTypeDef]] = None


class ThreatDetectedByNameTypeDef(BaseValidatorModel):
    ItemCount: Optional[int] = None
    UniqueThreatNameCount: Optional[int] = None
    Shortened: Optional[bool] = None
    ThreatNames: Optional[List[ScanThreatNameTypeDef]] = None


class DescribeMalwareScansResponseTypeDef(BaseValidatorModel):
    Scans: List[ScanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UsageTopAccountsResultTypeDef(BaseValidatorModel):
    Feature: Optional[UsageFeatureType] = None
    Accounts: Optional[List[UsageTopAccountResultTypeDef]] = None


class UpdateMalwareProtectionPlanRequestTypeDef(BaseValidatorModel):
    MalwareProtectionPlanId: str
    Role: Optional[str] = None
    Actions: Optional[MalwareProtectionPlanActionsTypeDef] = None
    ProtectedResource: Optional[UpdateProtectedResourceTypeDef] = None


class AnomalyTypeDef(BaseValidatorModel):
    Profiles: Optional[Dict[str, Dict[str, List[AnomalyObjectTypeDef]]]] = None
    Unusual: Optional[AnomalyUnusualTypeDef] = None


class PublicAccessTypeDef(BaseValidatorModel):
    PermissionConfiguration: Optional[PermissionConfigurationTypeDef] = None
    EffectivePermission: Optional[str] = None


class FindingCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class CreateFilterRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    Name: str
    FindingCriteria: FindingCriteriaUnionTypeDef
    Description: Optional[str] = None
    Action: Optional[FilterActionType] = None
    Rank: Optional[int] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class GetFindingsStatisticsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FindingStatisticTypes: Optional[Sequence[Literal["COUNT_BY_SEVERITY"]]] = None
    FindingCriteria: Optional[FindingCriteriaUnionTypeDef] = None
    GroupBy: Optional[GroupByTypeType] = None
    OrderBy: Optional[OrderByType] = None
    MaxResults: Optional[int] = None


class ListFindingsRequestPaginateTypeDef(BaseValidatorModel):
    DetectorId: str
    FindingCriteria: Optional[FindingCriteriaUnionTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFindingsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FindingCriteria: Optional[FindingCriteriaUnionTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class UpdateFilterRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    FilterName: str
    Description: Optional[str] = None
    Action: Optional[FilterActionType] = None
    Rank: Optional[int] = None
    FindingCriteria: Optional[FindingCriteriaUnionTypeDef] = None


class CoverageResourceTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    DetectorId: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceDetails: Optional[CoverageResourceDetailsTypeDef] = None
    CoverageStatus: Optional[CoverageStatusType] = None
    Issue: Optional[str] = None
    UpdatedAt: Optional[datetime] = None


class GetCoverageStatisticsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    StatisticsType: Sequence[CoverageStatisticsTypeType]
    FilterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None


class ListCoverageRequestPaginateTypeDef(BaseValidatorModel):
    DetectorId: str
    FilterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    SortCriteria: Optional[CoverageSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCoverageRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FilterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    SortCriteria: Optional[CoverageSortCriteriaTypeDef] = None


class CreateProtectedResourceUnionTypeDef(BaseValidatorModel):
    pass


class CreateMalwareProtectionPlanRequestTypeDef(BaseValidatorModel):
    Role: str
    ProtectedResource: CreateProtectedResourceUnionTypeDef
    ClientToken: Optional[str] = None
    Actions: Optional[MalwareProtectionPlanActionsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class AccountFreeTrialInfoTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    DataSources: Optional[DataSourcesFreeTrialTypeDef] = None
    Features: Optional[List[FreeTrialFeatureConfigurationResultTypeDef]] = None


class DataSourceConfigurationsResultTypeDef(BaseValidatorModel):
    CloudTrail: CloudTrailConfigurationResultTypeDef
    DNSLogs: DNSLogsConfigurationResultTypeDef
    FlowLogs: FlowLogsConfigurationResultTypeDef
    S3Logs: S3LogsConfigurationResultTypeDef
    Kubernetes: Optional[KubernetesConfigurationResultTypeDef] = None
    MalwareProtection: Optional[MalwareProtectionConfigurationResultTypeDef] = None


class UnprocessedDataSourcesResultTypeDef(BaseValidatorModel):
    MalwareProtection: Optional[MalwareProtectionConfigurationResultTypeDef] = None


class DescribeMalwareScansRequestPaginateTypeDef(BaseValidatorModel):
    DetectorId: str
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMalwareScansRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None


class EcsClusterDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Status: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None
    TaskDetails: Optional[EcsTaskDetailsTypeDef] = None


class KubernetesWorkloadDetailsTypeDef(BaseValidatorModel):
    pass


class KubernetesDetailsTypeDef(BaseValidatorModel):
    KubernetesUserDetails: Optional[KubernetesUserDetailsTypeDef] = None
    KubernetesWorkloadDetails: Optional[KubernetesWorkloadDetailsTypeDef] = None


class RuntimeContextTypeDef(BaseValidatorModel):
    pass


class RuntimeDetailsTypeDef(BaseValidatorModel):
    Process: Optional[ProcessDetailsTypeDef] = None
    Context: Optional[RuntimeContextTypeDef] = None


class CreateDetectorRequestTypeDef(BaseValidatorModel):
    Enable: bool
    ClientToken: Optional[str] = None
    FindingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    DataSources: Optional[DataSourceConfigurationsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Features: Optional[Sequence[DetectorFeatureConfigurationTypeDef]] = None


class UpdateDetectorRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    Enable: Optional[bool] = None
    FindingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    DataSources: Optional[DataSourceConfigurationsTypeDef] = None
    Features: Optional[Sequence[DetectorFeatureConfigurationTypeDef]] = None


class UpdateMemberDetectorsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AccountIds: Sequence[str]
    DataSources: Optional[DataSourceConfigurationsTypeDef] = None
    Features: Optional[Sequence[MemberFeaturesConfigurationTypeDef]] = None


class OrganizationDataSourceConfigurationsResultTypeDef(BaseValidatorModel):
    S3Logs: OrganizationS3LogsConfigurationResultTypeDef
    Kubernetes: Optional[OrganizationKubernetesConfigurationResultTypeDef] = None
    MalwareProtection: Optional[OrganizationMalwareProtectionConfigurationResultTypeDef] = None


class OrganizationDataSourceConfigurationsTypeDef(BaseValidatorModel):
    S3Logs: Optional[OrganizationS3LogsConfigurationTypeDef] = None
    Kubernetes: Optional[OrganizationKubernetesConfigurationTypeDef] = None
    MalwareProtection: Optional[OrganizationMalwareProtectionConfigurationTypeDef] = None


class OrganizationDetailsTypeDef(BaseValidatorModel):
    UpdatedAt: Optional[datetime] = None
    OrganizationStatistics: Optional[OrganizationStatisticsTypeDef] = None


class PortProbeActionTypeDef(BaseValidatorModel):
    Blocked: Optional[bool] = None
    PortProbeDetails: Optional[List[PortProbeDetailTypeDef]] = None


class ResourceV2TypeDef(BaseValidatorModel):
    Uid: str
    ResourceType: FindingResourceTypeType
    Name: Optional[str] = None
    AccountId: Optional[str] = None
    Region: Optional[str] = None
    Service: Optional[str] = None
    CloudPartition: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    Data: Optional[ResourceDataTypeDef] = None


class GetMalwareScanSettingsResponseTypeDef(BaseValidatorModel):
    ScanResourceCriteria: ScanResourceCriteriaOutputTypeDef
    EbsSnapshotPreservation: EbsSnapshotPreservationType
    ResponseMetadata: ResponseMetadataTypeDef


class ScanDetectionsTypeDef(BaseValidatorModel):
    ScannedItemCount: Optional[ScannedItemCountTypeDef] = None
    ThreatsDetectedItemCount: Optional[ThreatsDetectedItemCountTypeDef] = None
    HighestSeverityThreatDetails: Optional[HighestSeverityThreatDetailsTypeDef] = None
    ThreatDetectedByName: Optional[ThreatDetectedByNameTypeDef] = None


class UsageStatisticsTypeDef(BaseValidatorModel):
    SumByAccount: Optional[List[UsageAccountResultTypeDef]] = None
    TopAccountsByFeature: Optional[List[UsageTopAccountsResultTypeDef]] = None
    SumByDataSource: Optional[List[UsageDataSourceResultTypeDef]] = None
    SumByResource: Optional[List[UsageResourceResultTypeDef]] = None
    TopResources: Optional[List[UsageResourceResultTypeDef]] = None
    SumByFeature: Optional[List[UsageFeatureResultTypeDef]] = None


class ListCoverageResponseTypeDef(BaseValidatorModel):
    Resources: List[CoverageResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetRemainingFreeTrialDaysResponseTypeDef(BaseValidatorModel):
    Accounts: List[AccountFreeTrialInfoTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDetectorResponseTypeDef(BaseValidatorModel):
    CreatedAt: str
    FindingPublishingFrequency: FindingPublishingFrequencyType
    ServiceRole: str
    Status: DetectorStatusType
    UpdatedAt: str
    DataSources: DataSourceConfigurationsResultTypeDef
    Tags: Dict[str, str]
    Features: List[DetectorFeatureConfigurationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class MemberDataSourceConfigurationTypeDef(BaseValidatorModel):
    AccountId: str
    DataSources: Optional[DataSourceConfigurationsResultTypeDef] = None
    Features: Optional[List[MemberFeaturesConfigurationResultTypeDef]] = None


class CreateDetectorResponseTypeDef(BaseValidatorModel):
    DetectorId: str
    UnprocessedDataSources: UnprocessedDataSourcesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeOrganizationConfigurationResponseTypeDef(BaseValidatorModel):
    AutoEnable: bool
    MemberAccountLimitReached: bool
    DataSources: OrganizationDataSourceConfigurationsResultTypeDef
    Features: List[OrganizationFeatureConfigurationResultTypeDef]
    AutoEnableOrganizationMembers: AutoEnableMembersType
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateOrganizationConfigurationRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    AutoEnable: Optional[bool] = None
    DataSources: Optional[OrganizationDataSourceConfigurationsTypeDef] = None
    Features: Optional[Sequence[OrganizationFeatureConfigurationTypeDef]] = None
    AutoEnableOrganizationMembers: Optional[AutoEnableMembersType] = None


class GetOrganizationStatisticsResponseTypeDef(BaseValidatorModel):
    OrganizationDetails: OrganizationDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DnsRequestActionTypeDef(BaseValidatorModel):
    pass


class AwsApiCallActionTypeDef(BaseValidatorModel):
    pass


class NetworkConnectionActionTypeDef(BaseValidatorModel):
    pass


class ActionTypeDef(BaseValidatorModel):
    ActionType: Optional[str] = None
    AwsApiCallAction: Optional[AwsApiCallActionTypeDef] = None
    DnsRequestAction: Optional[DnsRequestActionTypeDef] = None
    NetworkConnectionAction: Optional[NetworkConnectionActionTypeDef] = None
    PortProbeAction: Optional[PortProbeActionTypeDef] = None
    KubernetesApiCallAction: Optional[KubernetesApiCallActionTypeDef] = None
    RdsLoginAttemptAction: Optional[RdsLoginAttemptActionTypeDef] = None
    KubernetesPermissionCheckedDetails: Optional[KubernetesPermissionCheckedDetailsTypeDef] = None
    KubernetesRoleBindingDetails: Optional[KubernetesRoleBindingDetailsTypeDef] = None
    KubernetesRoleDetails: Optional[KubernetesRoleDetailsTypeDef] = None


class SignalTypeDef(BaseValidatorModel):
    pass


class SequenceTypeDef(BaseValidatorModel):
    Uid: str
    Description: str
    Signals: List[SignalTypeDef]
    Actors: Optional[List[ActorTypeDef]] = None
    Resources: Optional[List[ResourceV2TypeDef]] = None
    Endpoints: Optional[List[NetworkEndpointTypeDef]] = None
    SequenceIndicators: Optional[List[IndicatorTypeDef]] = None


class ScanResourceCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class UpdateMalwareScanSettingsRequestTypeDef(BaseValidatorModel):
    DetectorId: str
    ScanResourceCriteria: Optional[ScanResourceCriteriaUnionTypeDef] = None
    EbsSnapshotPreservation: Optional[EbsSnapshotPreservationType] = None


class EbsVolumeScanDetailsTypeDef(BaseValidatorModel):
    ScanId: Optional[str] = None
    ScanStartedAt: Optional[datetime] = None
    ScanCompletedAt: Optional[datetime] = None
    TriggerFindingId: Optional[str] = None
    Sources: Optional[List[str]] = None
    ScanDetections: Optional[ScanDetectionsTypeDef] = None
    ScanType: Optional[ScanTypeType] = None


class GetUsageStatisticsResponseTypeDef(BaseValidatorModel):
    UsageStatistics: UsageStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class S3BucketDetailTypeDef(BaseValidatorModel):
    pass


class ResourceTypeDef(BaseValidatorModel):
    AccessKeyDetails: Optional[AccessKeyDetailsTypeDef] = None
    S3BucketDetails: Optional[List[S3BucketDetailTypeDef]] = None
    InstanceDetails: Optional[InstanceDetailsTypeDef] = None
    EksClusterDetails: Optional[EksClusterDetailsTypeDef] = None
    KubernetesDetails: Optional[KubernetesDetailsTypeDef] = None
    ResourceType: Optional[str] = None
    EbsVolumeDetails: Optional[EbsVolumeDetailsTypeDef] = None
    EcsClusterDetails: Optional[EcsClusterDetailsTypeDef] = None
    ContainerDetails: Optional[ContainerTypeDef] = None
    RdsDbInstanceDetails: Optional[RdsDbInstanceDetailsTypeDef] = None
    RdsLimitlessDbDetails: Optional[RdsLimitlessDbDetailsTypeDef] = None
    RdsDbUserDetails: Optional[RdsDbUserDetailsTypeDef] = None
    LambdaDetails: Optional[LambdaDetailsTypeDef] = None


class GetMemberDetectorsResponseTypeDef(BaseValidatorModel):
    MemberDataSourceConfigurations: List[MemberDataSourceConfigurationTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FindingTypeDef(BaseValidatorModel):
    pass


class GetFindingsResponseTypeDef(BaseValidatorModel):
    Findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef



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
from aws_resource_validator.pydantic_models.guardduty_constants import *

class AcceptAdministratorInvitationRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AdministratorId: str
    InvitationId: str

class AcceptInvitationRequestRequestTypeDef(BaseModel):
    DetectorId: str
    MasterId: str
    InvitationId: str

class AccessControlListTypeDef(BaseModel):
    AllowsPublicReadAccess: Optional[bool] = None
    AllowsPublicWriteAccess: Optional[bool] = None

class AccessKeyDetailsTypeDef(BaseModel):
    AccessKeyId: Optional[str] = None
    PrincipalId: Optional[str] = None
    UserName: Optional[str] = None
    UserType: Optional[str] = None

class AccountDetailTypeDef(BaseModel):
    AccountId: str
    Email: str

class FreeTrialFeatureConfigurationResultTypeDef(BaseModel):
    Name: Optional[FreeTrialFeatureResultType] = None
    FreeTrialDaysRemaining: Optional[int] = None

class BlockPublicAccessTypeDef(BaseModel):
    IgnorePublicAcls: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None
    BlockPublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None

class DnsRequestActionTypeDef(BaseModel):
    Domain: Optional[str] = None
    Protocol: Optional[str] = None
    Blocked: Optional[bool] = None
    DomainWithSuffix: Optional[str] = None

class KubernetesPermissionCheckedDetailsTypeDef(BaseModel):
    Verb: Optional[str] = None
    Resource: Optional[str] = None
    Namespace: Optional[str] = None
    Allowed: Optional[bool] = None

class KubernetesRoleBindingDetailsTypeDef(BaseModel):
    Kind: Optional[str] = None
    Name: Optional[str] = None
    Uid: Optional[str] = None
    RoleRefName: Optional[str] = None
    RoleRefKind: Optional[str] = None

class KubernetesRoleDetailsTypeDef(BaseModel):
    Kind: Optional[str] = None
    Name: Optional[str] = None
    Uid: Optional[str] = None

class AddonDetailsTypeDef(BaseModel):
    AddonVersion: Optional[str] = None
    AddonStatus: Optional[str] = None

class AdminAccountTypeDef(BaseModel):
    AdminAccountId: Optional[str] = None
    AdminStatus: Optional[AdminStatusType] = None

class AdministratorTypeDef(BaseModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    RelationshipStatus: Optional[str] = None
    InvitedAt: Optional[str] = None

class AgentDetailsTypeDef(BaseModel):
    Version: Optional[str] = None

class ObservationsTypeDef(BaseModel):
    Text: Optional[List[str]] = None

class ArchiveFindingsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FindingIds: Sequence[str]

class DomainDetailsTypeDef(BaseModel):
    Domain: Optional[str] = None

class RemoteAccountDetailsTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Affiliated: Optional[bool] = None

class BucketPolicyTypeDef(BaseModel):
    AllowsPublicReadAccess: Optional[bool] = None
    AllowsPublicWriteAccess: Optional[bool] = None

class CityTypeDef(BaseModel):
    CityName: Optional[str] = None

class CloudTrailConfigurationResultTypeDef(BaseModel):
    Status: DataSourceStatusType

class ConditionOutputTypeDef(BaseModel):
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

class ConditionTypeDef(BaseModel):
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

class ContainerInstanceDetailsTypeDef(BaseModel):
    CoveredContainerInstances: Optional[int] = None
    CompatibleContainerInstances: Optional[int] = None

class SecurityContextTypeDef(BaseModel):
    Privileged: Optional[bool] = None
    AllowPrivilegeEscalation: Optional[bool] = None

class VolumeMountTypeDef(BaseModel):
    Name: Optional[str] = None
    MountPath: Optional[str] = None

class CountryTypeDef(BaseModel):
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None

class FargateDetailsTypeDef(BaseModel):
    Issues: Optional[List[str]] = None
    ManagementType: Optional[ManagementTypeType] = None

class CoverageFilterConditionTypeDef(BaseModel):
    Equals: Optional[Sequence[str]] = None
    NotEquals: Optional[Sequence[str]] = None

class CoverageSortCriteriaTypeDef(BaseModel):
    AttributeName: Optional[CoverageSortKeyType] = None
    OrderBy: Optional[OrderByType] = None

class CoverageStatisticsTypeDef(BaseModel):
    CountByResourceType: Optional[Dict[ResourceTypeType, int]] = None
    CountByCoverageStatus: Optional[Dict[CoverageStatusType, int]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateIPSetRequestRequestTypeDef(BaseModel):
    DetectorId: str
    Name: str
    Format: IpSetFormatType
    Location: str
    Activate: bool
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UnprocessedAccountTypeDef(BaseModel):
    AccountId: str
    Result: str

class CreateS3BucketResourceOutputTypeDef(BaseModel):
    BucketName: Optional[str] = None
    ObjectPrefixes: Optional[List[str]] = None

class CreateS3BucketResourceTypeDef(BaseModel):
    BucketName: Optional[str] = None
    ObjectPrefixes: Optional[Sequence[str]] = None

class DestinationPropertiesTypeDef(BaseModel):
    DestinationArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None

class CreateSampleFindingsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FindingTypes: Optional[Sequence[str]] = None

class CreateThreatIntelSetRequestRequestTypeDef(BaseModel):
    DetectorId: str
    Name: str
    Format: ThreatIntelSetFormatType
    Location: str
    Activate: bool
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class DNSLogsConfigurationResultTypeDef(BaseModel):
    Status: DataSourceStatusType

class FlowLogsConfigurationResultTypeDef(BaseModel):
    Status: DataSourceStatusType

class S3LogsConfigurationResultTypeDef(BaseModel):
    Status: DataSourceStatusType

class S3LogsConfigurationTypeDef(BaseModel):
    Enable: bool

class DataSourceFreeTrialTypeDef(BaseModel):
    FreeTrialDaysRemaining: Optional[int] = None

class DeclineInvitationsRequestRequestTypeDef(BaseModel):
    AccountIds: Sequence[str]

class DefaultServerSideEncryptionTypeDef(BaseModel):
    EncryptionType: Optional[str] = None
    KmsMasterKeyArn: Optional[str] = None

class DeleteDetectorRequestRequestTypeDef(BaseModel):
    DetectorId: str

class DeleteFilterRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FilterName: str

class DeleteIPSetRequestRequestTypeDef(BaseModel):
    DetectorId: str
    IpSetId: str

class DeleteInvitationsRequestRequestTypeDef(BaseModel):
    AccountIds: Sequence[str]

class DeleteMalwareProtectionPlanRequestRequestTypeDef(BaseModel):
    MalwareProtectionPlanId: str

class DeleteMembersRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountIds: Sequence[str]

class DeletePublishingDestinationRequestRequestTypeDef(BaseModel):
    DetectorId: str
    DestinationId: str

class DeleteThreatIntelSetRequestRequestTypeDef(BaseModel):
    DetectorId: str
    ThreatIntelSetId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SortCriteriaTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    OrderBy: Optional[OrderByType] = None

class DescribeOrganizationConfigurationRequestRequestTypeDef(BaseModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePublishingDestinationRequestRequestTypeDef(BaseModel):
    DetectorId: str
    DestinationId: str

class DestinationTypeDef(BaseModel):
    DestinationId: str
    DestinationType: Literal["S3"]
    Status: PublishingStatusType

class DetectorAdditionalConfigurationResultTypeDef(BaseModel):
    Name: Optional[FeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None

class DetectorAdditionalConfigurationTypeDef(BaseModel):
    Name: Optional[FeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None

class DisableOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    AdminAccountId: str

class DisassociateFromAdministratorAccountRequestRequestTypeDef(BaseModel):
    DetectorId: str

class DisassociateFromMasterAccountRequestRequestTypeDef(BaseModel):
    DetectorId: str

class DisassociateMembersRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountIds: Sequence[str]

class VolumeDetailTypeDef(BaseModel):
    VolumeArn: Optional[str] = None
    VolumeType: Optional[str] = None
    DeviceName: Optional[str] = None
    VolumeSizeInGB: Optional[int] = None
    EncryptionType: Optional[str] = None
    SnapshotArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None

class EbsVolumesResultTypeDef(BaseModel):
    Status: Optional[DataSourceStatusType] = None
    Reason: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class EnableOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    AdminAccountId: str

class ThreatIntelligenceDetailTypeDef(BaseModel):
    ThreatListName: Optional[str] = None
    ThreatNames: Optional[List[str]] = None
    ThreatFileSha256: Optional[str] = None

class FilterConditionTypeDef(BaseModel):
    EqualsValue: Optional[str] = None
    GreaterThan: Optional[int] = None
    LessThan: Optional[int] = None

class FindingStatisticsTypeDef(BaseModel):
    CountBySeverity: Optional[Dict[str, int]] = None

class GeoLocationTypeDef(BaseModel):
    Lat: Optional[float] = None
    Lon: Optional[float] = None

class GetAdministratorAccountRequestRequestTypeDef(BaseModel):
    DetectorId: str

class GetDetectorRequestRequestTypeDef(BaseModel):
    DetectorId: str

class GetFilterRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FilterName: str

class GetIPSetRequestRequestTypeDef(BaseModel):
    DetectorId: str
    IpSetId: str

class GetMalwareProtectionPlanRequestRequestTypeDef(BaseModel):
    MalwareProtectionPlanId: str

class MalwareProtectionPlanStatusReasonTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class GetMalwareScanSettingsRequestRequestTypeDef(BaseModel):
    DetectorId: str

class GetMasterAccountRequestRequestTypeDef(BaseModel):
    DetectorId: str

class MasterTypeDef(BaseModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    RelationshipStatus: Optional[str] = None
    InvitedAt: Optional[str] = None

class GetMemberDetectorsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountIds: Sequence[str]

class GetMembersRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountIds: Sequence[str]

class MemberTypeDef(BaseModel):
    AccountId: str
    MasterId: str
    Email: str
    RelationshipStatus: str
    UpdatedAt: str
    DetectorId: Optional[str] = None
    InvitedAt: Optional[str] = None
    AdministratorId: Optional[str] = None

class GetRemainingFreeTrialDaysRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountIds: Optional[Sequence[str]] = None

class GetThreatIntelSetRequestRequestTypeDef(BaseModel):
    DetectorId: str
    ThreatIntelSetId: str

class UsageCriteriaTypeDef(BaseModel):
    AccountIds: Optional[Sequence[str]] = None
    DataSources: Optional[Sequence[DataSourceType]] = None
    Resources: Optional[Sequence[str]] = None
    Features: Optional[Sequence[UsageFeatureType]] = None

class HighestSeverityThreatDetailsTypeDef(BaseModel):
    Severity: Optional[str] = None
    ThreatName: Optional[str] = None
    Count: Optional[int] = None

class HostPathTypeDef(BaseModel):
    Path: Optional[str] = None

class IamInstanceProfileTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None

class ImpersonatedUserTypeDef(BaseModel):
    Username: Optional[str] = None
    Groups: Optional[List[str]] = None

class ProductCodeTypeDef(BaseModel):
    Code: Optional[str] = None
    ProductType: Optional[str] = None

class InvitationTypeDef(BaseModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    RelationshipStatus: Optional[str] = None
    InvitedAt: Optional[str] = None

class InviteMembersRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountIds: Sequence[str]
    DisableEmailNotification: Optional[bool] = None
    Message: Optional[str] = None

class ItemPathTypeDef(BaseModel):
    NestedItemPath: Optional[str] = None
    Hash: Optional[str] = None

class KubernetesAuditLogsConfigurationResultTypeDef(BaseModel):
    Status: DataSourceStatusType

class KubernetesAuditLogsConfigurationTypeDef(BaseModel):
    Enable: bool

class LineageObjectTypeDef(BaseModel):
    StartTime: Optional[datetime] = None
    NamespacePid: Optional[int] = None
    UserId: Optional[int] = None
    Name: Optional[str] = None
    Pid: Optional[int] = None
    Uuid: Optional[str] = None
    ExecutablePath: Optional[str] = None
    Euid: Optional[int] = None
    ParentUuid: Optional[str] = None

class ListDetectorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFiltersRequestRequestTypeDef(BaseModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListIPSetsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInvitationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMalwareProtectionPlansRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class MalwareProtectionPlanSummaryTypeDef(BaseModel):
    MalwareProtectionPlanId: Optional[str] = None

class ListMembersRequestRequestTypeDef(BaseModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OnlyAssociated: Optional[str] = None

class ListOrganizationAdminAccountsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPublishingDestinationsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListThreatIntelSetsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LocalIpDetailsTypeDef(BaseModel):
    IpAddressV4: Optional[str] = None
    IpAddressV6: Optional[str] = None

class LocalPortDetailsTypeDef(BaseModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None

class LoginAttributeTypeDef(BaseModel):
    User: Optional[str] = None
    Application: Optional[str] = None
    FailedLoginAttempts: Optional[int] = None
    SuccessfulLoginAttempts: Optional[int] = None

class ScanEc2InstanceWithFindingsTypeDef(BaseModel):
    EbsVolumes: Optional[bool] = None

class MalwareProtectionPlanTaggingActionTypeDef(BaseModel):
    Status: Optional[MalwareProtectionPlanTaggingActionStatusType] = None

class MemberAdditionalConfigurationResultTypeDef(BaseModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None

class MemberAdditionalConfigurationTypeDef(BaseModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    Status: Optional[FeatureStatusType] = None

class RemotePortDetailsTypeDef(BaseModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None

class PrivateIpAddressDetailsTypeDef(BaseModel):
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class SecurityGroupTypeDef(BaseModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None

class OrganizationAdditionalConfigurationResultTypeDef(BaseModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None

class OrganizationAdditionalConfigurationTypeDef(BaseModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None

class OrganizationS3LogsConfigurationResultTypeDef(BaseModel):
    AutoEnable: bool

class OrganizationS3LogsConfigurationTypeDef(BaseModel):
    AutoEnable: bool

class OrganizationEbsVolumesResultTypeDef(BaseModel):
    AutoEnable: Optional[bool] = None

class OrganizationEbsVolumesTypeDef(BaseModel):
    AutoEnable: Optional[bool] = None

class OrganizationFeatureStatisticsAdditionalConfigurationTypeDef(BaseModel):
    Name: Optional[OrgFeatureAdditionalConfigurationType] = None
    EnabledAccountsCount: Optional[int] = None

class OrganizationKubernetesAuditLogsConfigurationResultTypeDef(BaseModel):
    AutoEnable: bool

class OrganizationKubernetesAuditLogsConfigurationTypeDef(BaseModel):
    AutoEnable: bool

class OrganizationTypeDef(BaseModel):
    Asn: Optional[str] = None
    AsnOrg: Optional[str] = None
    Isp: Optional[str] = None
    Org: Optional[str] = None

class OwnerTypeDef(BaseModel):
    Id: Optional[str] = None

class RdsDbUserDetailsTypeDef(BaseModel):
    User: Optional[str] = None
    Application: Optional[str] = None
    Database: Optional[str] = None
    Ssl: Optional[str] = None
    AuthMethod: Optional[str] = None

class ResourceDetailsTypeDef(BaseModel):
    InstanceArn: Optional[str] = None

class S3ObjectDetailTypeDef(BaseModel):
    ObjectArn: Optional[str] = None
    Key: Optional[str] = None
    ETag: Optional[str] = None
    Hash: Optional[str] = None
    VersionId: Optional[str] = None

class ScanConditionPairTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class ScannedItemCountTypeDef(BaseModel):
    TotalGb: Optional[int] = None
    Files: Optional[int] = None
    Volumes: Optional[int] = None

class ThreatsDetectedItemCountTypeDef(BaseModel):
    Files: Optional[int] = None

class ScanFilePathTypeDef(BaseModel):
    FilePath: Optional[str] = None
    VolumeArn: Optional[str] = None
    Hash: Optional[str] = None
    FileName: Optional[str] = None

class ScanResultDetailsTypeDef(BaseModel):
    ScanResult: Optional[ScanResultType] = None

class TriggerDetailsTypeDef(BaseModel):
    GuardDutyFindingId: Optional[str] = None
    Description: Optional[str] = None

class ServiceAdditionalInfoTypeDef(BaseModel):
    Value: Optional[str] = None
    Type: Optional[str] = None

class StartMalwareScanRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class StartMonitoringMembersRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountIds: Sequence[str]

class StopMonitoringMembersRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountIds: Sequence[str]

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class TotalTypeDef(BaseModel):
    Amount: Optional[str] = None
    Unit: Optional[str] = None

class UnarchiveFindingsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FindingIds: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateFindingsFeedbackRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FindingIds: Sequence[str]
    Feedback: FeedbackType
    Comments: Optional[str] = None

class UpdateIPSetRequestRequestTypeDef(BaseModel):
    DetectorId: str
    IpSetId: str
    Name: Optional[str] = None
    Location: Optional[str] = None
    Activate: Optional[bool] = None

class UpdateS3BucketResourceTypeDef(BaseModel):
    ObjectPrefixes: Optional[Sequence[str]] = None

class UpdateThreatIntelSetRequestRequestTypeDef(BaseModel):
    DetectorId: str
    ThreatIntelSetId: str
    Name: Optional[str] = None
    Location: Optional[str] = None
    Activate: Optional[bool] = None

class CreateMembersRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountDetails: Sequence[AccountDetailTypeDef]

class AccountLevelPermissionsTypeDef(BaseModel):
    BlockPublicAccess: Optional[BlockPublicAccessTypeDef] = None

class CoverageEksClusterDetailsTypeDef(BaseModel):
    ClusterName: Optional[str] = None
    CoveredNodes: Optional[int] = None
    CompatibleNodes: Optional[int] = None
    AddonDetails: Optional[AddonDetailsTypeDef] = None
    ManagementType: Optional[ManagementTypeType] = None

class CoverageEc2InstanceDetailsTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    ClusterArn: Optional[str] = None
    AgentDetails: Optional[AgentDetailsTypeDef] = None
    ManagementType: Optional[ManagementTypeType] = None

class AnomalyObjectTypeDef(BaseModel):
    ProfileType: Optional[Literal["FREQUENCY"]] = None
    ProfileSubtype: Optional[ProfileSubtypeType] = None
    Observations: Optional[ObservationsTypeDef] = None

class BucketLevelPermissionsTypeDef(BaseModel):
    AccessControlList: Optional[AccessControlListTypeDef] = None
    BucketPolicy: Optional[BucketPolicyTypeDef] = None
    BlockPublicAccess: Optional[BlockPublicAccessTypeDef] = None

class FindingCriteriaOutputTypeDef(BaseModel):
    Criterion: Optional[Dict[str, ConditionOutputTypeDef]] = None

class FindingCriteriaTypeDef(BaseModel):
    Criterion: Optional[Mapping[str, ConditionTypeDef]] = None

class ContainerTypeDef(BaseModel):
    ContainerRuntime: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Image: Optional[str] = None
    ImagePrefix: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMountTypeDef]] = None
    SecurityContext: Optional[SecurityContextTypeDef] = None

class CoverageEcsClusterDetailsTypeDef(BaseModel):
    ClusterName: Optional[str] = None
    FargateDetails: Optional[FargateDetailsTypeDef] = None
    ContainerInstanceDetails: Optional[ContainerInstanceDetailsTypeDef] = None

class CoverageFilterCriterionTypeDef(BaseModel):
    CriterionKey: Optional[CoverageFilterCriterionKeyType] = None
    FilterCondition: Optional[CoverageFilterConditionTypeDef] = None

class CreateFilterResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIPSetResponseTypeDef(BaseModel):
    IpSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMalwareProtectionPlanResponseTypeDef(BaseModel):
    MalwareProtectionPlanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePublishingDestinationResponseTypeDef(BaseModel):
    DestinationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThreatIntelSetResponseTypeDef(BaseModel):
    ThreatIntelSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAdministratorAccountResponseTypeDef(BaseModel):
    Administrator: AdministratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoverageStatisticsResponseTypeDef(BaseModel):
    CoverageStatistics: CoverageStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIPSetResponseTypeDef(BaseModel):
    Name: str
    Format: IpSetFormatType
    Location: str
    Status: IpSetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvitationsCountResponseTypeDef(BaseModel):
    InvitationsCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetThreatIntelSetResponseTypeDef(BaseModel):
    Name: str
    Format: ThreatIntelSetFormatType
    Location: str
    Status: ThreatIntelSetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDetectorsResponseTypeDef(BaseModel):
    DetectorIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListFiltersResponseTypeDef(BaseModel):
    FilterNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListFindingsResponseTypeDef(BaseModel):
    FindingIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIPSetsResponseTypeDef(BaseModel):
    IpSetIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListOrganizationAdminAccountsResponseTypeDef(BaseModel):
    AdminAccounts: List[AdminAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListThreatIntelSetsResponseTypeDef(BaseModel):
    ThreatIntelSetIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartMalwareScanResponseTypeDef(BaseModel):
    ScanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFilterResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMembersResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeclineInvitationsResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInvitationsResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMembersResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateMembersResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InviteMembersResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMonitoringMembersResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopMonitoringMembersResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMemberDetectorsResponseTypeDef(BaseModel):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProtectedResourceOutputTypeDef(BaseModel):
    S3Bucket: Optional[CreateS3BucketResourceOutputTypeDef] = None

class CreateProtectedResourceTypeDef(BaseModel):
    S3Bucket: Optional[CreateS3BucketResourceTypeDef] = None

class CreatePublishingDestinationRequestRequestTypeDef(BaseModel):
    DetectorId: str
    DestinationType: Literal["S3"]
    DestinationProperties: DestinationPropertiesTypeDef
    ClientToken: Optional[str] = None

class DescribePublishingDestinationResponseTypeDef(BaseModel):
    DestinationId: str
    DestinationType: Literal["S3"]
    Status: PublishingStatusType
    PublishingFailureStartTimestamp: int
    DestinationProperties: DestinationPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePublishingDestinationRequestRequestTypeDef(BaseModel):
    DetectorId: str
    DestinationId: str
    DestinationProperties: Optional[DestinationPropertiesTypeDef] = None

class KubernetesDataSourceFreeTrialTypeDef(BaseModel):
    AuditLogs: Optional[DataSourceFreeTrialTypeDef] = None

class MalwareProtectionDataSourceFreeTrialTypeDef(BaseModel):
    ScanEc2InstanceWithFindings: Optional[DataSourceFreeTrialTypeDef] = None

class ListDetectorsRequestListDetectorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFiltersRequestListFiltersPaginateTypeDef(BaseModel):
    DetectorId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIPSetsRequestListIPSetsPaginateTypeDef(BaseModel):
    DetectorId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInvitationsRequestListInvitationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersRequestListMembersPaginateTypeDef(BaseModel):
    DetectorId: str
    OnlyAssociated: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThreatIntelSetsRequestListThreatIntelSetsPaginateTypeDef(BaseModel):
    DetectorId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetFindingsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FindingIds: Sequence[str]
    SortCriteria: Optional[SortCriteriaTypeDef] = None

class ListPublishingDestinationsResponseTypeDef(BaseModel):
    Destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetectorFeatureConfigurationResultTypeDef(BaseModel):
    Name: Optional[DetectorFeatureResultType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None
    AdditionalConfiguration: Optional[List[DetectorAdditionalConfigurationResultTypeDef]] = None

class DetectorFeatureConfigurationTypeDef(BaseModel):
    Name: Optional[DetectorFeatureType] = None
    Status: Optional[FeatureStatusType] = None
    AdditionalConfiguration: Optional[Sequence[DetectorAdditionalConfigurationTypeDef]] = None

class EbsVolumeDetailsTypeDef(BaseModel):
    ScannedVolumeDetails: Optional[List[VolumeDetailTypeDef]] = None
    SkippedVolumeDetails: Optional[List[VolumeDetailTypeDef]] = None

class ScanEc2InstanceWithFindingsResultTypeDef(BaseModel):
    EbsVolumes: Optional[EbsVolumesResultTypeDef] = None

class EksClusterDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    VpcId: Optional[str] = None
    Status: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    CreatedAt: Optional[datetime] = None

class RdsDbInstanceDetailsTypeDef(BaseModel):
    DbInstanceIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None
    DbInstanceArn: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class EvidenceTypeDef(BaseModel):
    ThreatIntelligenceDetails: Optional[List[ThreatIntelligenceDetailTypeDef]] = None

class FilterCriterionTypeDef(BaseModel):
    CriterionKey: Optional[CriterionKeyType] = None
    FilterCondition: Optional[FilterConditionTypeDef] = None

class GetFindingsStatisticsResponseTypeDef(BaseModel):
    FindingStatistics: FindingStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMasterAccountResponseTypeDef(BaseModel):
    Master: MasterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMembersResponseTypeDef(BaseModel):
    Members: List[MemberTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(BaseModel):
    Members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetUsageStatisticsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    UsageStatisticType: UsageStatisticTypeType
    UsageCriteria: UsageCriteriaTypeDef
    Unit: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class VolumeTypeDef(BaseModel):
    Name: Optional[str] = None
    HostPath: Optional[HostPathTypeDef] = None

class KubernetesUserDetailsTypeDef(BaseModel):
    Username: Optional[str] = None
    Uid: Optional[str] = None
    Groups: Optional[List[str]] = None
    SessionName: Optional[List[str]] = None
    ImpersonatedUser: Optional[ImpersonatedUserTypeDef] = None

class ListInvitationsResponseTypeDef(BaseModel):
    Invitations: List[InvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ThreatTypeDef(BaseModel):
    Name: Optional[str] = None
    Source: Optional[str] = None
    ItemPaths: Optional[List[ItemPathTypeDef]] = None

class KubernetesConfigurationResultTypeDef(BaseModel):
    AuditLogs: KubernetesAuditLogsConfigurationResultTypeDef

class KubernetesConfigurationTypeDef(BaseModel):
    AuditLogs: KubernetesAuditLogsConfigurationTypeDef

class ProcessDetailsTypeDef(BaseModel):
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

class ListMalwareProtectionPlansResponseTypeDef(BaseModel):
    MalwareProtectionPlans: List[MalwareProtectionPlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MalwareProtectionConfigurationTypeDef(BaseModel):
    ScanEc2InstanceWithFindings: Optional[ScanEc2InstanceWithFindingsTypeDef] = None

class MalwareProtectionPlanActionsTypeDef(BaseModel):
    Tagging: Optional[MalwareProtectionPlanTaggingActionTypeDef] = None

class MemberFeaturesConfigurationResultTypeDef(BaseModel):
    Name: Optional[OrgFeatureType] = None
    Status: Optional[FeatureStatusType] = None
    UpdatedAt: Optional[datetime] = None
    AdditionalConfiguration: Optional[List[MemberAdditionalConfigurationResultTypeDef]] = None

class MemberFeaturesConfigurationTypeDef(BaseModel):
    Name: Optional[OrgFeatureType] = None
    Status: Optional[FeatureStatusType] = None
    AdditionalConfiguration: Optional[Sequence[MemberAdditionalConfigurationTypeDef]] = None

class NetworkInterfaceTypeDef(BaseModel):
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

class VpcConfigTypeDef(BaseModel):
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroupTypeDef]] = None

class OrganizationFeatureConfigurationResultTypeDef(BaseModel):
    Name: Optional[OrgFeatureType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None
    AdditionalConfiguration: Optional[       List[OrganizationAdditionalConfigurationResultTypeDef]     ] = None

class OrganizationFeatureConfigurationTypeDef(BaseModel):
    Name: Optional[OrgFeatureType] = None
    AutoEnable: Optional[OrgFeatureStatusType] = None
    AdditionalConfiguration: Optional[       Sequence[OrganizationAdditionalConfigurationTypeDef]     ] = None

class OrganizationScanEc2InstanceWithFindingsResultTypeDef(BaseModel):
    EbsVolumes: Optional[OrganizationEbsVolumesResultTypeDef] = None

class OrganizationScanEc2InstanceWithFindingsTypeDef(BaseModel):
    EbsVolumes: Optional[OrganizationEbsVolumesTypeDef] = None

class OrganizationFeatureStatisticsTypeDef(BaseModel):
    Name: Optional[OrgFeatureType] = None
    EnabledAccountsCount: Optional[int] = None
    AdditionalConfiguration: Optional[       List[OrganizationFeatureStatisticsAdditionalConfigurationTypeDef]     ] = None

class OrganizationKubernetesConfigurationResultTypeDef(BaseModel):
    AuditLogs: OrganizationKubernetesAuditLogsConfigurationResultTypeDef

class OrganizationKubernetesConfigurationTypeDef(BaseModel):
    AuditLogs: OrganizationKubernetesAuditLogsConfigurationTypeDef

class RemoteIpDetailsTypeDef(BaseModel):
    City: Optional[CityTypeDef] = None
    Country: Optional[CountryTypeDef] = None
    GeoLocation: Optional[GeoLocationTypeDef] = None
    IpAddressV4: Optional[str] = None
    IpAddressV6: Optional[str] = None
    Organization: Optional[OrganizationTypeDef] = None

class ScanConditionOutputTypeDef(BaseModel):
    MapEquals: List[ScanConditionPairTypeDef]

class ScanConditionTypeDef(BaseModel):
    MapEquals: Sequence[ScanConditionPairTypeDef]

class ScanThreatNameTypeDef(BaseModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[ScanFilePathTypeDef]] = None

class ScanTypeDef(BaseModel):
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

class UsageAccountResultTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Total: Optional[TotalTypeDef] = None

class UsageDataSourceResultTypeDef(BaseModel):
    DataSource: Optional[DataSourceType] = None
    Total: Optional[TotalTypeDef] = None

class UsageFeatureResultTypeDef(BaseModel):
    Feature: Optional[UsageFeatureType] = None
    Total: Optional[TotalTypeDef] = None

class UsageResourceResultTypeDef(BaseModel):
    Resource: Optional[str] = None
    Total: Optional[TotalTypeDef] = None

class UsageTopAccountResultTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Total: Optional[TotalTypeDef] = None

class UpdateProtectedResourceTypeDef(BaseModel):
    S3Bucket: Optional[UpdateS3BucketResourceTypeDef] = None

class AnomalyUnusualTypeDef(BaseModel):
    Behavior: Optional[Dict[str, Dict[str, AnomalyObjectTypeDef]]] = None

class PermissionConfigurationTypeDef(BaseModel):
    BucketLevelPermissions: Optional[BucketLevelPermissionsTypeDef] = None
    AccountLevelPermissions: Optional[AccountLevelPermissionsTypeDef] = None

class GetFilterResponseTypeDef(BaseModel):
    Name: str
    Description: str
    Action: FilterActionType
    Rank: int
    FindingCriteria: FindingCriteriaOutputTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFilterRequestRequestTypeDef(BaseModel):
    DetectorId: str
    Name: str
    FindingCriteria: FindingCriteriaTypeDef
    Description: Optional[str] = None
    Action: Optional[FilterActionType] = None
    Rank: Optional[int] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class GetFindingsStatisticsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FindingStatisticTypes: Sequence[Literal["COUNT_BY_SEVERITY"]]
    FindingCriteria: Optional[FindingCriteriaTypeDef] = None

class ListFindingsRequestListFindingsPaginateTypeDef(BaseModel):
    DetectorId: str
    FindingCriteria: Optional[FindingCriteriaTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FindingCriteria: Optional[FindingCriteriaTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UpdateFilterRequestRequestTypeDef(BaseModel):
    DetectorId: str
    FilterName: str
    Description: Optional[str] = None
    Action: Optional[FilterActionType] = None
    Rank: Optional[int] = None
    FindingCriteria: Optional[FindingCriteriaTypeDef] = None

class CoverageResourceDetailsTypeDef(BaseModel):
    EksClusterDetails: Optional[CoverageEksClusterDetailsTypeDef] = None
    ResourceType: Optional[ResourceTypeType] = None
    EcsClusterDetails: Optional[CoverageEcsClusterDetailsTypeDef] = None
    Ec2InstanceDetails: Optional[CoverageEc2InstanceDetailsTypeDef] = None

class CoverageFilterCriteriaTypeDef(BaseModel):
    FilterCriterion: Optional[Sequence[CoverageFilterCriterionTypeDef]] = None

class DataSourcesFreeTrialTypeDef(BaseModel):
    CloudTrail: Optional[DataSourceFreeTrialTypeDef] = None
    DnsLogs: Optional[DataSourceFreeTrialTypeDef] = None
    FlowLogs: Optional[DataSourceFreeTrialTypeDef] = None
    S3Logs: Optional[DataSourceFreeTrialTypeDef] = None
    Kubernetes: Optional[KubernetesDataSourceFreeTrialTypeDef] = None
    MalwareProtection: Optional[MalwareProtectionDataSourceFreeTrialTypeDef] = None

class MalwareProtectionConfigurationResultTypeDef(BaseModel):
    ScanEc2InstanceWithFindings: Optional[ScanEc2InstanceWithFindingsResultTypeDef] = None
    ServiceRole: Optional[str] = None

class FilterCriteriaTypeDef(BaseModel):
    FilterCriterion: Optional[Sequence[FilterCriterionTypeDef]] = None

class EcsTaskDetailsTypeDef(BaseModel):
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

class KubernetesWorkloadDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Uid: Optional[str] = None
    Namespace: Optional[str] = None
    HostNetwork: Optional[bool] = None
    Containers: Optional[List[ContainerTypeDef]] = None
    Volumes: Optional[List[VolumeTypeDef]] = None
    ServiceAccountName: Optional[str] = None
    HostIPC: Optional[bool] = None
    HostPID: Optional[bool] = None

class MalwareScanDetailsTypeDef(BaseModel):
    Threats: Optional[List[ThreatTypeDef]] = None

class RuntimeContextTypeDef(BaseModel):
    ModifyingProcess: Optional[ProcessDetailsTypeDef] = None
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
    TargetProcess: Optional[ProcessDetailsTypeDef] = None
    AddressFamily: Optional[str] = None
    IanaProtocolNumber: Optional[int] = None
    MemoryRegions: Optional[List[str]] = None
    ToolName: Optional[str] = None
    ToolCategory: Optional[str] = None
    ServiceName: Optional[str] = None
    CommandLineExample: Optional[str] = None
    ThreatFilePath: Optional[str] = None

class DataSourceConfigurationsTypeDef(BaseModel):
    S3Logs: Optional[S3LogsConfigurationTypeDef] = None
    Kubernetes: Optional[KubernetesConfigurationTypeDef] = None
    MalwareProtection: Optional[MalwareProtectionConfigurationTypeDef] = None

class CreateMalwareProtectionPlanRequestRequestTypeDef(BaseModel):
    Role: str
    ProtectedResource: CreateProtectedResourceTypeDef
    ClientToken: Optional[str] = None
    Actions: Optional[MalwareProtectionPlanActionsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class GetMalwareProtectionPlanResponseTypeDef(BaseModel):
    Arn: str
    Role: str
    ProtectedResource: CreateProtectedResourceOutputTypeDef
    Actions: MalwareProtectionPlanActionsTypeDef
    CreatedAt: datetime
    Status: MalwareProtectionPlanStatusType
    StatusReasons: List[MalwareProtectionPlanStatusReasonTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceDetailsTypeDef(BaseModel):
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

class LambdaDetailsTypeDef(BaseModel):
    FunctionArn: Optional[str] = None
    FunctionName: Optional[str] = None
    Description: Optional[str] = None
    LastModifiedAt: Optional[datetime] = None
    RevisionId: Optional[str] = None
    FunctionVersion: Optional[str] = None
    Role: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class OrganizationMalwareProtectionConfigurationResultTypeDef(BaseModel):
    ScanEc2InstanceWithFindings: Optional[       OrganizationScanEc2InstanceWithFindingsResultTypeDef     ] = None

class OrganizationMalwareProtectionConfigurationTypeDef(BaseModel):
    ScanEc2InstanceWithFindings: Optional[OrganizationScanEc2InstanceWithFindingsTypeDef] = None

class OrganizationStatisticsTypeDef(BaseModel):
    TotalAccountsCount: Optional[int] = None
    MemberAccountsCount: Optional[int] = None
    ActiveAccountsCount: Optional[int] = None
    EnabledAccountsCount: Optional[int] = None
    CountByFeature: Optional[List[OrganizationFeatureStatisticsTypeDef]] = None

class AwsApiCallActionTypeDef(BaseModel):
    Api: Optional[str] = None
    CallerType: Optional[str] = None
    DomainDetails: Optional[DomainDetailsTypeDef] = None
    ErrorCode: Optional[str] = None
    UserAgent: Optional[str] = None
    RemoteIpDetails: Optional[RemoteIpDetailsTypeDef] = None
    ServiceName: Optional[str] = None
    RemoteAccountDetails: Optional[RemoteAccountDetailsTypeDef] = None
    AffectedResources: Optional[Dict[str, str]] = None

class KubernetesApiCallActionTypeDef(BaseModel):
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

class NetworkConnectionActionTypeDef(BaseModel):
    Blocked: Optional[bool] = None
    ConnectionDirection: Optional[str] = None
    LocalPortDetails: Optional[LocalPortDetailsTypeDef] = None
    Protocol: Optional[str] = None
    LocalIpDetails: Optional[LocalIpDetailsTypeDef] = None
    RemoteIpDetails: Optional[RemoteIpDetailsTypeDef] = None
    RemotePortDetails: Optional[RemotePortDetailsTypeDef] = None

class PortProbeDetailTypeDef(BaseModel):
    LocalPortDetails: Optional[LocalPortDetailsTypeDef] = None
    LocalIpDetails: Optional[LocalIpDetailsTypeDef] = None
    RemoteIpDetails: Optional[RemoteIpDetailsTypeDef] = None

class RdsLoginAttemptActionTypeDef(BaseModel):
    RemoteIpDetails: Optional[RemoteIpDetailsTypeDef] = None
    LoginAttributes: Optional[List[LoginAttributeTypeDef]] = None

class ScanResourceCriteriaOutputTypeDef(BaseModel):
    Include: Optional[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionOutputTypeDef]] = None
    Exclude: Optional[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionOutputTypeDef]] = None

class ScanResourceCriteriaTypeDef(BaseModel):
    Include: Optional[Mapping[Literal["EC2_INSTANCE_TAG"], ScanConditionTypeDef]] = None
    Exclude: Optional[Mapping[Literal["EC2_INSTANCE_TAG"], ScanConditionTypeDef]] = None

class ThreatDetectedByNameTypeDef(BaseModel):
    ItemCount: Optional[int] = None
    UniqueThreatNameCount: Optional[int] = None
    Shortened: Optional[bool] = None
    ThreatNames: Optional[List[ScanThreatNameTypeDef]] = None

class DescribeMalwareScansResponseTypeDef(BaseModel):
    Scans: List[ScanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UsageTopAccountsResultTypeDef(BaseModel):
    Feature: Optional[UsageFeatureType] = None
    Accounts: Optional[List[UsageTopAccountResultTypeDef]] = None

class UpdateMalwareProtectionPlanRequestRequestTypeDef(BaseModel):
    MalwareProtectionPlanId: str
    Role: Optional[str] = None
    Actions: Optional[MalwareProtectionPlanActionsTypeDef] = None
    ProtectedResource: Optional[UpdateProtectedResourceTypeDef] = None

class AnomalyTypeDef(BaseModel):
    Profiles: Optional[Dict[str, Dict[str, List[AnomalyObjectTypeDef]]]] = None
    Unusual: Optional[AnomalyUnusualTypeDef] = None

class PublicAccessTypeDef(BaseModel):
    PermissionConfiguration: Optional[PermissionConfigurationTypeDef] = None
    EffectivePermission: Optional[str] = None

class CoverageResourceTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    DetectorId: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceDetails: Optional[CoverageResourceDetailsTypeDef] = None
    CoverageStatus: Optional[CoverageStatusType] = None
    Issue: Optional[str] = None
    UpdatedAt: Optional[datetime] = None

class GetCoverageStatisticsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    StatisticsType: Sequence[CoverageStatisticsTypeType]
    FilterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None

class ListCoverageRequestListCoveragePaginateTypeDef(BaseModel):
    DetectorId: str
    FilterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    SortCriteria: Optional[CoverageSortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoverageRequestRequestTypeDef(BaseModel):
    DetectorId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FilterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    SortCriteria: Optional[CoverageSortCriteriaTypeDef] = None

class AccountFreeTrialInfoTypeDef(BaseModel):
    AccountId: Optional[str] = None
    DataSources: Optional[DataSourcesFreeTrialTypeDef] = None
    Features: Optional[List[FreeTrialFeatureConfigurationResultTypeDef]] = None

class DataSourceConfigurationsResultTypeDef(BaseModel):
    CloudTrail: CloudTrailConfigurationResultTypeDef
    DNSLogs: DNSLogsConfigurationResultTypeDef
    FlowLogs: FlowLogsConfigurationResultTypeDef
    S3Logs: S3LogsConfigurationResultTypeDef
    Kubernetes: Optional[KubernetesConfigurationResultTypeDef] = None
    MalwareProtection: Optional[MalwareProtectionConfigurationResultTypeDef] = None

class UnprocessedDataSourcesResultTypeDef(BaseModel):
    MalwareProtection: Optional[MalwareProtectionConfigurationResultTypeDef] = None

class DescribeMalwareScansRequestDescribeMalwareScansPaginateTypeDef(BaseModel):
    DetectorId: str
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMalwareScansRequestRequestTypeDef(BaseModel):
    DetectorId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None

class EcsClusterDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Status: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None
    TaskDetails: Optional[EcsTaskDetailsTypeDef] = None

class KubernetesDetailsTypeDef(BaseModel):
    KubernetesUserDetails: Optional[KubernetesUserDetailsTypeDef] = None
    KubernetesWorkloadDetails: Optional[KubernetesWorkloadDetailsTypeDef] = None

class RuntimeDetailsTypeDef(BaseModel):
    Process: Optional[ProcessDetailsTypeDef] = None
    Context: Optional[RuntimeContextTypeDef] = None

class CreateDetectorRequestRequestTypeDef(BaseModel):
    Enable: bool
    ClientToken: Optional[str] = None
    FindingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    DataSources: Optional[DataSourceConfigurationsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Features: Optional[Sequence[DetectorFeatureConfigurationTypeDef]] = None

class UpdateDetectorRequestRequestTypeDef(BaseModel):
    DetectorId: str
    Enable: Optional[bool] = None
    FindingPublishingFrequency: Optional[FindingPublishingFrequencyType] = None
    DataSources: Optional[DataSourceConfigurationsTypeDef] = None
    Features: Optional[Sequence[DetectorFeatureConfigurationTypeDef]] = None

class UpdateMemberDetectorsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AccountIds: Sequence[str]
    DataSources: Optional[DataSourceConfigurationsTypeDef] = None
    Features: Optional[Sequence[MemberFeaturesConfigurationTypeDef]] = None

class OrganizationDataSourceConfigurationsResultTypeDef(BaseModel):
    S3Logs: OrganizationS3LogsConfigurationResultTypeDef
    Kubernetes: Optional[OrganizationKubernetesConfigurationResultTypeDef] = None
    MalwareProtection: Optional[OrganizationMalwareProtectionConfigurationResultTypeDef] = None

class OrganizationDataSourceConfigurationsTypeDef(BaseModel):
    S3Logs: Optional[OrganizationS3LogsConfigurationTypeDef] = None
    Kubernetes: Optional[OrganizationKubernetesConfigurationTypeDef] = None
    MalwareProtection: Optional[OrganizationMalwareProtectionConfigurationTypeDef] = None

class OrganizationDetailsTypeDef(BaseModel):
    UpdatedAt: Optional[datetime] = None
    OrganizationStatistics: Optional[OrganizationStatisticsTypeDef] = None

class PortProbeActionTypeDef(BaseModel):
    Blocked: Optional[bool] = None
    PortProbeDetails: Optional[List[PortProbeDetailTypeDef]] = None

class GetMalwareScanSettingsResponseTypeDef(BaseModel):
    ScanResourceCriteria: ScanResourceCriteriaOutputTypeDef
    EbsSnapshotPreservation: EbsSnapshotPreservationType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMalwareScanSettingsRequestRequestTypeDef(BaseModel):
    DetectorId: str
    ScanResourceCriteria: Optional[ScanResourceCriteriaTypeDef] = None
    EbsSnapshotPreservation: Optional[EbsSnapshotPreservationType] = None

class ScanDetectionsTypeDef(BaseModel):
    ScannedItemCount: Optional[ScannedItemCountTypeDef] = None
    ThreatsDetectedItemCount: Optional[ThreatsDetectedItemCountTypeDef] = None
    HighestSeverityThreatDetails: Optional[HighestSeverityThreatDetailsTypeDef] = None
    ThreatDetectedByName: Optional[ThreatDetectedByNameTypeDef] = None

class UsageStatisticsTypeDef(BaseModel):
    SumByAccount: Optional[List[UsageAccountResultTypeDef]] = None
    TopAccountsByFeature: Optional[List[UsageTopAccountsResultTypeDef]] = None
    SumByDataSource: Optional[List[UsageDataSourceResultTypeDef]] = None
    SumByResource: Optional[List[UsageResourceResultTypeDef]] = None
    TopResources: Optional[List[UsageResourceResultTypeDef]] = None
    SumByFeature: Optional[List[UsageFeatureResultTypeDef]] = None

class DetectionTypeDef(BaseModel):
    Anomaly: Optional[AnomalyTypeDef] = None

class S3BucketDetailTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Owner: Optional[OwnerTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    DefaultServerSideEncryption: Optional[DefaultServerSideEncryptionTypeDef] = None
    PublicAccess: Optional[PublicAccessTypeDef] = None
    S3ObjectDetails: Optional[List[S3ObjectDetailTypeDef]] = None

class ListCoverageResponseTypeDef(BaseModel):
    Resources: List[CoverageResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetRemainingFreeTrialDaysResponseTypeDef(BaseModel):
    Accounts: List[AccountFreeTrialInfoTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDetectorResponseTypeDef(BaseModel):
    CreatedAt: str
    FindingPublishingFrequency: FindingPublishingFrequencyType
    ServiceRole: str
    Status: DetectorStatusType
    UpdatedAt: str
    DataSources: DataSourceConfigurationsResultTypeDef
    Tags: Dict[str, str]
    Features: List[DetectorFeatureConfigurationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MemberDataSourceConfigurationTypeDef(BaseModel):
    AccountId: str
    DataSources: Optional[DataSourceConfigurationsResultTypeDef] = None
    Features: Optional[List[MemberFeaturesConfigurationResultTypeDef]] = None

class CreateDetectorResponseTypeDef(BaseModel):
    DetectorId: str
    UnprocessedDataSources: UnprocessedDataSourcesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConfigurationResponseTypeDef(BaseModel):
    AutoEnable: bool
    MemberAccountLimitReached: bool
    DataSources: OrganizationDataSourceConfigurationsResultTypeDef
    Features: List[OrganizationFeatureConfigurationResultTypeDef]
    AutoEnableOrganizationMembers: AutoEnableMembersType
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateOrganizationConfigurationRequestRequestTypeDef(BaseModel):
    DetectorId: str
    AutoEnable: Optional[bool] = None
    DataSources: Optional[OrganizationDataSourceConfigurationsTypeDef] = None
    Features: Optional[Sequence[OrganizationFeatureConfigurationTypeDef]] = None
    AutoEnableOrganizationMembers: Optional[AutoEnableMembersType] = None

class GetOrganizationStatisticsResponseTypeDef(BaseModel):
    OrganizationDetails: OrganizationDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActionTypeDef(BaseModel):
    ActionType: Optional[str] = None
    AwsApiCallAction: Optional[AwsApiCallActionTypeDef] = None
    DnsRequestAction: Optional[DnsRequestActionTypeDef] = None
    NetworkConnectionAction: Optional[NetworkConnectionActionTypeDef] = None
    PortProbeAction: Optional[PortProbeActionTypeDef] = None
    KubernetesApiCallAction: Optional[KubernetesApiCallActionTypeDef] = None
    RdsLoginAttemptAction: Optional[RdsLoginAttemptActionTypeDef] = None
    KubernetesPermissionCheckedDetails: Optional[       KubernetesPermissionCheckedDetailsTypeDef     ] = None
    KubernetesRoleBindingDetails: Optional[KubernetesRoleBindingDetailsTypeDef] = None
    KubernetesRoleDetails: Optional[KubernetesRoleDetailsTypeDef] = None

class EbsVolumeScanDetailsTypeDef(BaseModel):
    ScanId: Optional[str] = None
    ScanStartedAt: Optional[datetime] = None
    ScanCompletedAt: Optional[datetime] = None
    TriggerFindingId: Optional[str] = None
    Sources: Optional[List[str]] = None
    ScanDetections: Optional[ScanDetectionsTypeDef] = None
    ScanType: Optional[ScanTypeType] = None

class GetUsageStatisticsResponseTypeDef(BaseModel):
    UsageStatistics: UsageStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ResourceTypeDef(BaseModel):
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
    RdsDbUserDetails: Optional[RdsDbUserDetailsTypeDef] = None
    LambdaDetails: Optional[LambdaDetailsTypeDef] = None

class GetMemberDetectorsResponseTypeDef(BaseModel):
    MemberDataSourceConfigurations: List[MemberDataSourceConfigurationTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceTypeDef(BaseModel):
    Action: Optional[ActionTypeDef] = None
    Evidence: Optional[EvidenceTypeDef] = None
    Archived: Optional[bool] = None
    Count: Optional[int] = None
    DetectorId: Optional[str] = None
    EventFirstSeen: Optional[str] = None
    EventLastSeen: Optional[str] = None
    ResourceRole: Optional[str] = None
    ServiceName: Optional[str] = None
    UserFeedback: Optional[str] = None
    AdditionalInfo: Optional[ServiceAdditionalInfoTypeDef] = None
    FeatureName: Optional[str] = None
    EbsVolumeScanDetails: Optional[EbsVolumeScanDetailsTypeDef] = None
    RuntimeDetails: Optional[RuntimeDetailsTypeDef] = None
    Detection: Optional[DetectionTypeDef] = None
    MalwareScanDetails: Optional[MalwareScanDetailsTypeDef] = None

class FindingTypeDef(BaseModel):
    AccountId: str
    Arn: str
    CreatedAt: str
    Id: str
    Region: str
    Resource: ResourceTypeDef
    SchemaVersion: str
    Severity: float
    Type: str
    UpdatedAt: str
    Confidence: Optional[float] = None
    Description: Optional[str] = None
    Partition: Optional[str] = None
    Service: Optional[ServiceTypeDef] = None
    Title: Optional[str] = None

class GetFindingsResponseTypeDef(BaseModel):
    Findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


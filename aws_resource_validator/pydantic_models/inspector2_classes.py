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
from aws_resource_validator.pydantic_models.inspector2_constants import *

class SeverityCountsTypeDef(BaseModel):
    all: Optional[int] = None
    critical: Optional[int] = None
    high: Optional[int] = None
    medium: Optional[int] = None

class AccountAggregationTypeDef(BaseModel):
    findingType: Optional[AggregationFindingTypeType] = None
    resourceType: Optional[AggregationResourceTypeType] = None
    sortBy: Optional[AccountSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class StateTypeDef(BaseModel):
    errorCode: ErrorCodeType
    errorMessage: str
    status: StatusType

class ResourceStatusTypeDef(BaseModel):
    ec2: StatusType
    ecr: StatusType
    lambda: Optional[StatusType] = None
    lambdaCode: Optional[StatusType] = None

class FindingTypeAggregationTypeDef(BaseModel):
    findingType: Optional[AggregationFindingTypeType] = None
    resourceType: Optional[AggregationResourceTypeType] = None
    sortBy: Optional[FindingTypeSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class StringFilterTypeDef(BaseModel):
    comparison: StringComparisonType
    value: str

class AssociateMemberRequestRequestTypeDef(BaseModel):
    accountId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AtigDataTypeDef(BaseModel):
    firstSeen: Optional[datetime] = None
    lastSeen: Optional[datetime] = None
    targets: Optional[List[str]] = None
    ttps: Optional[List[str]] = None

class AutoEnableTypeDef(BaseModel):
    ec2: bool
    ecr: bool
    lambda: Optional[bool] = None
    lambdaCode: Optional[bool] = None

class AwsEc2InstanceDetailsTypeDef(BaseModel):
    iamInstanceProfileArn: Optional[str] = None
    imageId: Optional[str] = None
    ipV4Addresses: Optional[List[str]] = None
    ipV6Addresses: Optional[List[str]] = None
    keyName: Optional[str] = None
    launchedAt: Optional[datetime] = None
    platform: Optional[str] = None
    subnetId: Optional[str] = None
    type: Optional[str] = None
    vpcId: Optional[str] = None

class AwsEcrContainerImageDetailsTypeDef(BaseModel):
    imageHash: str
    registry: str
    repositoryName: str
    architecture: Optional[str] = None
    author: Optional[str] = None
    imageTags: Optional[List[str]] = None
    platform: Optional[str] = None
    pushedAt: Optional[datetime] = None

class LambdaVpcConfigTypeDef(BaseModel):
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None

class BatchGetAccountStatusRequestRequestTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None

class BatchGetCodeSnippetRequestRequestTypeDef(BaseModel):
    findingArns: Sequence[str]

class CodeSnippetErrorTypeDef(BaseModel):
    errorCode: CodeSnippetErrorCodeType
    errorMessage: str
    findingArn: str

class BatchGetFindingDetailsRequestRequestTypeDef(BaseModel):
    findingArns: Sequence[str]

class FindingDetailsErrorTypeDef(BaseModel):
    errorCode: FindingDetailsErrorCodeType
    errorMessage: str
    findingArn: str

class BatchGetFreeTrialInfoRequestRequestTypeDef(BaseModel):
    accountIds: Sequence[str]

class FreeTrialInfoErrorTypeDef(BaseModel):
    accountId: str
    code: FreeTrialInfoErrorCodeType
    message: str

class BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None

class FailedMemberAccountEc2DeepInspectionStatusStateTypeDef(BaseModel):
    accountId: str
    ec2ScanStatus: Optional[StatusType] = None
    errorMessage: Optional[str] = None

class MemberAccountEc2DeepInspectionStatusStateTypeDef(BaseModel):
    accountId: str
    errorMessage: Optional[str] = None
    status: Optional[Ec2DeepInspectionStatusType] = None

class MemberAccountEc2DeepInspectionStatusTypeDef(BaseModel):
    accountId: str
    activateDeepInspection: bool

class CancelFindingsReportRequestRequestTypeDef(BaseModel):
    reportId: str

class CancelSbomExportRequestRequestTypeDef(BaseModel):
    reportId: str

class StatusCountsTypeDef(BaseModel):
    failed: Optional[int] = None
    passed: Optional[int] = None
    skipped: Optional[int] = None

class CisFindingStatusFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    value: CisFindingStatusType

class CisNumberFilterTypeDef(BaseModel):
    lowerInclusive: Optional[int] = None
    upperInclusive: Optional[int] = None

class CisResultStatusFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    value: CisResultStatusType

class CisTargetsTypeDef(BaseModel):
    accountIds: Optional[List[str]] = None
    targetResourceTags: Optional[Dict[str, List[str]]] = None

class CisSecurityLevelFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    value: CisSecurityLevelType

class CisStringFilterTypeDef(BaseModel):
    comparison: CisStringComparisonType
    value: str

class CisScanResultDetailsTypeDef(BaseModel):
    scanArn: str
    accountId: Optional[str] = None
    checkDescription: Optional[str] = None
    checkId: Optional[str] = None
    findingArn: Optional[str] = None
    level: Optional[CisSecurityLevelType] = None
    platform: Optional[str] = None
    remediation: Optional[str] = None
    status: Optional[CisFindingStatusType] = None
    statusReason: Optional[str] = None
    targetResourceId: Optional[str] = None
    title: Optional[str] = None

class CisTargetStatusFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    value: CisTargetStatusType

class CisTargetStatusReasonFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    value: CisTargetStatusReasonType

class TagFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    key: str
    value: str

class CisScanStatusFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    value: CisScanStatusType

class CisaDataTypeDef(BaseModel):
    action: Optional[str] = None
    dateAdded: Optional[datetime] = None
    dateDue: Optional[datetime] = None

class CodeFilePathTypeDef(BaseModel):
    endLine: int
    fileName: str
    filePath: str
    startLine: int

class CodeLineTypeDef(BaseModel):
    content: str
    lineNumber: int

class SuggestedFixTypeDef(BaseModel):
    code: Optional[str] = None
    description: Optional[str] = None

class ComputePlatformTypeDef(BaseModel):
    product: Optional[str] = None
    vendor: Optional[str] = None
    version: Optional[str] = None

class CountsTypeDef(BaseModel):
    count: Optional[int] = None
    groupKey: Optional[GroupKeyType] = None

class CoverageMapFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    key: str
    value: Optional[str] = None

class CoverageStringFilterTypeDef(BaseModel):
    comparison: CoverageStringComparisonType
    value: str

class ScanStatusTypeDef(BaseModel):
    reason: ScanStatusReasonType
    statusCode: ScanStatusCodeType

class CreateCisTargetsTypeDef(BaseModel):
    accountIds: Sequence[str]
    targetResourceTags: Mapping[str, Sequence[str]]

class DestinationTypeDef(BaseModel):
    bucketName: str
    kmsKeyArn: str
    keyPrefix: Optional[str] = None

class Cvss2TypeDef(BaseModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None

class Cvss3TypeDef(BaseModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None

class CvssScoreAdjustmentTypeDef(BaseModel):
    metric: str
    reason: str

class CvssScoreTypeDef(BaseModel):
    baseScore: float
    scoringVector: str
    source: str
    version: str

class TimeTypeDef(BaseModel):
    timeOfDay: str
    timezone: str

class DateFilterExtraOutputTypeDef(BaseModel):
    endInclusive: Optional[datetime] = None
    startInclusive: Optional[datetime] = None

class DateFilterOutputTypeDef(BaseModel):
    endInclusive: Optional[datetime] = None
    startInclusive: Optional[datetime] = None

class DelegatedAdminAccountTypeDef(BaseModel):
    accountId: Optional[str] = None
    status: Optional[DelegatedAdminStatusType] = None

class DelegatedAdminTypeDef(BaseModel):
    accountId: Optional[str] = None
    relationshipStatus: Optional[RelationshipStatusType] = None

class DeleteCisScanConfigurationRequestRequestTypeDef(BaseModel):
    scanConfigurationArn: str

class DeleteFilterRequestRequestTypeDef(BaseModel):
    arn: str

class DisableDelegatedAdminAccountRequestRequestTypeDef(BaseModel):
    delegatedAdminAccountId: str

class DisableRequestRequestTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None
    resourceTypes: Optional[Sequence[ResourceScanTypeType]] = None

class DisassociateMemberRequestRequestTypeDef(BaseModel):
    accountId: str

class Ec2ScanModeStateTypeDef(BaseModel):
    scanMode: Optional[Ec2ScanModeType] = None
    scanModeStatus: Optional[Ec2ScanModeStatusType] = None

class Ec2ConfigurationTypeDef(BaseModel):
    scanMode: Ec2ScanModeType

class MapFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    key: str
    value: Optional[str] = None

class Ec2MetadataTypeDef(BaseModel):
    amiId: Optional[str] = None
    platform: Optional[Ec2PlatformType] = None
    tags: Optional[Dict[str, str]] = None

class EcrRescanDurationStateTypeDef(BaseModel):
    pullDateRescanDuration: Optional[EcrPullDateRescanDurationType] = None
    rescanDuration: Optional[EcrRescanDurationType] = None
    status: Optional[EcrRescanDurationStatusType] = None
    updatedAt: Optional[datetime] = None

class EcrConfigurationTypeDef(BaseModel):
    rescanDuration: EcrRescanDurationType
    pullDateRescanDuration: Optional[EcrPullDateRescanDurationType] = None

class EcrContainerImageMetadataTypeDef(BaseModel):
    imagePulledAt: Optional[datetime] = None
    tags: Optional[List[str]] = None

class EcrRepositoryMetadataTypeDef(BaseModel):
    name: Optional[str] = None
    scanFrequency: Optional[EcrScanFrequencyType] = None

class EnableDelegatedAdminAccountRequestRequestTypeDef(BaseModel):
    delegatedAdminAccountId: str
    clientToken: Optional[str] = None

class EnableRequestRequestTypeDef(BaseModel):
    resourceTypes: Sequence[ResourceScanTypeType]
    accountIds: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None

class EpssDetailsTypeDef(BaseModel):
    score: Optional[float] = None

class EpssTypeDef(BaseModel):
    score: Optional[float] = None

class EvidenceTypeDef(BaseModel):
    evidenceDetail: Optional[str] = None
    evidenceRule: Optional[str] = None
    severity: Optional[str] = None

class ExploitObservedTypeDef(BaseModel):
    firstSeen: Optional[datetime] = None
    lastSeen: Optional[datetime] = None

class ExploitabilityDetailsTypeDef(BaseModel):
    lastKnownExploitAt: Optional[datetime] = None

class NumberFilterTypeDef(BaseModel):
    lowerInclusive: Optional[float] = None
    upperInclusive: Optional[float] = None

class PortRangeFilterTypeDef(BaseModel):
    beginInclusive: Optional[int] = None
    endInclusive: Optional[int] = None

class FreeTrialInfoTypeDef(BaseModel):
    end: datetime
    start: datetime
    status: FreeTrialStatusType
    type: FreeTrialTypeType

class GetCisScanReportRequestRequestTypeDef(BaseModel):
    scanArn: str
    reportFormat: Optional[CisReportFormatType] = None
    targetAccounts: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetEncryptionKeyRequestRequestTypeDef(BaseModel):
    resourceType: ResourceTypeType
    scanType: ScanTypeType

class GetFindingsReportStatusRequestRequestTypeDef(BaseModel):
    reportId: Optional[str] = None

class GetMemberRequestRequestTypeDef(BaseModel):
    accountId: str

class MemberTypeDef(BaseModel):
    accountId: Optional[str] = None
    delegatedAdminAccountId: Optional[str] = None
    relationshipStatus: Optional[RelationshipStatusType] = None
    updatedAt: Optional[datetime] = None

class GetSbomExportRequestRequestTypeDef(BaseModel):
    reportId: str

class LambdaFunctionMetadataTypeDef(BaseModel):
    functionName: Optional[str] = None
    functionTags: Optional[Dict[str, str]] = None
    layers: Optional[List[str]] = None
    runtime: Optional[RuntimeType] = None

class ListAccountPermissionsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    service: Optional[ServiceType] = None

class PermissionTypeDef(BaseModel):
    operation: OperationType
    service: ServiceType

class ListDelegatedAdminAccountsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFiltersRequestRequestTypeDef(BaseModel):
    action: Optional[FilterActionType] = None
    arns: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SortCriteriaTypeDef(BaseModel):
    field: SortFieldType
    sortOrder: SortOrderType

class ListMembersRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    onlyAssociated: Optional[bool] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListUsageTotalsRequestRequestTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StepTypeDef(BaseModel):
    componentId: str
    componentType: str

class PortRangeTypeDef(BaseModel):
    begin: int
    end: int

class VulnerablePackageTypeDef(BaseModel):
    name: str
    version: str
    arch: Optional[str] = None
    epoch: Optional[int] = None
    filePath: Optional[str] = None
    fixedInVersion: Optional[str] = None
    packageManager: Optional[PackageManagerType] = None
    release: Optional[str] = None
    remediation: Optional[str] = None
    sourceLambdaLayerArn: Optional[str] = None
    sourceLayerHash: Optional[str] = None

class RecommendationTypeDef(BaseModel):
    Url: Optional[str] = None
    text: Optional[str] = None

class ResetEncryptionKeyRequestRequestTypeDef(BaseModel):
    resourceType: ResourceTypeType
    scanType: ScanTypeType

class ResourceMapFilterTypeDef(BaseModel):
    comparison: Literal["EQUALS"]
    key: str
    value: Optional[str] = None

class ResourceStringFilterTypeDef(BaseModel):
    comparison: ResourceStringComparisonType
    value: str

class SearchVulnerabilitiesFilterCriteriaTypeDef(BaseModel):
    vulnerabilityIds: Sequence[str]

class SendCisSessionHealthRequestRequestTypeDef(BaseModel):
    scanJobId: str
    sessionToken: str

class StartCisSessionMessageTypeDef(BaseModel):
    sessionToken: str

class StopCisMessageProgressTypeDef(BaseModel):
    errorChecks: Optional[int] = None
    failedChecks: Optional[int] = None
    informationalChecks: Optional[int] = None
    notApplicableChecks: Optional[int] = None
    notEvaluatedChecks: Optional[int] = None
    successfulChecks: Optional[int] = None
    totalChecks: Optional[int] = None
    unknownChecks: Optional[int] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateCisTargetsTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None
    targetResourceTags: Optional[Mapping[str, Sequence[str]]] = None

class UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef(BaseModel):
    activateDeepInspection: Optional[bool] = None
    packagePaths: Optional[Sequence[str]] = None

class UpdateEncryptionKeyRequestRequestTypeDef(BaseModel):
    kmsKeyId: str
    resourceType: ResourceTypeType
    scanType: ScanTypeType

class UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef(BaseModel):
    orgPackagePaths: Sequence[str]

class UsageTypeDef(BaseModel):
    currency: Optional[Literal["USD"]] = None
    estimatedMonthlyCost: Optional[float] = None
    total: Optional[float] = None
    type: Optional[UsageTypeType] = None

class AccountAggregationResponseTypeDef(BaseModel):
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class AmiAggregationResponseTypeDef(BaseModel):
    ami: str
    accountId: Optional[str] = None
    affectedInstances: Optional[int] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class AwsEcrContainerAggregationResponseTypeDef(BaseModel):
    resourceId: str
    accountId: Optional[str] = None
    architecture: Optional[str] = None
    imageSha: Optional[str] = None
    imageTags: Optional[List[str]] = None
    repository: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class Ec2InstanceAggregationResponseTypeDef(BaseModel):
    instanceId: str
    accountId: Optional[str] = None
    ami: Optional[str] = None
    instanceTags: Optional[Dict[str, str]] = None
    networkFindings: Optional[int] = None
    operatingSystem: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class FindingTypeAggregationResponseTypeDef(BaseModel):
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class ImageLayerAggregationResponseTypeDef(BaseModel):
    accountId: str
    layerHash: str
    repository: str
    resourceId: str
    severityCounts: Optional[SeverityCountsTypeDef] = None

class LambdaFunctionAggregationResponseTypeDef(BaseModel):
    resourceId: str
    accountId: Optional[str] = None
    functionName: Optional[str] = None
    lambdaTags: Optional[Dict[str, str]] = None
    lastModifiedAt: Optional[datetime] = None
    runtime: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class LambdaLayerAggregationResponseTypeDef(BaseModel):
    accountId: str
    functionName: str
    layerArn: str
    resourceId: str
    severityCounts: Optional[SeverityCountsTypeDef] = None

class PackageAggregationResponseTypeDef(BaseModel):
    packageName: str
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class RepositoryAggregationResponseTypeDef(BaseModel):
    repository: str
    accountId: Optional[str] = None
    affectedImages: Optional[int] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class TitleAggregationResponseTypeDef(BaseModel):
    title: str
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None
    vulnerabilityId: Optional[str] = None

class ResourceStateTypeDef(BaseModel):
    ec2: StateTypeDef
    ecr: StateTypeDef
    lambda: Optional[StateTypeDef] = None
    lambdaCode: Optional[StateTypeDef] = None

class AccountTypeDef(BaseModel):
    accountId: str
    resourceStatus: ResourceStatusTypeDef
    status: StatusType

class FailedAccountTypeDef(BaseModel):
    accountId: str
    errorCode: ErrorCodeType
    errorMessage: str
    resourceStatus: Optional[ResourceStatusTypeDef] = None
    status: Optional[StatusType] = None

class AmiAggregationTypeDef(BaseModel):
    amis: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[AmiSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class AwsEcrContainerAggregationTypeDef(BaseModel):
    architectures: Optional[Sequence[StringFilterTypeDef]] = None
    imageShas: Optional[Sequence[StringFilterTypeDef]] = None
    imageTags: Optional[Sequence[StringFilterTypeDef]] = None
    repositories: Optional[Sequence[StringFilterTypeDef]] = None
    resourceIds: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[AwsEcrContainerSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class ImageLayerAggregationTypeDef(BaseModel):
    layerHashes: Optional[Sequence[StringFilterTypeDef]] = None
    repositories: Optional[Sequence[StringFilterTypeDef]] = None
    resourceIds: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[ImageLayerSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class LambdaLayerAggregationTypeDef(BaseModel):
    functionNames: Optional[Sequence[StringFilterTypeDef]] = None
    layerArns: Optional[Sequence[StringFilterTypeDef]] = None
    resourceIds: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[LambdaLayerSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class PackageAggregationTypeDef(BaseModel):
    packageNames: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[PackageSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class RepositoryAggregationTypeDef(BaseModel):
    repositories: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[RepositorySortByType] = None
    sortOrder: Optional[SortOrderType] = None

class TitleAggregationTypeDef(BaseModel):
    findingType: Optional[AggregationFindingTypeType] = None
    resourceType: Optional[AggregationResourceTypeType] = None
    sortBy: Optional[TitleSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    titles: Optional[Sequence[StringFilterTypeDef]] = None
    vulnerabilityIds: Optional[Sequence[StringFilterTypeDef]] = None

class AssociateMemberResponseTypeDef(BaseModel):
    accountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelFindingsReportResponseTypeDef(BaseModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelSbomExportResponseTypeDef(BaseModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCisScanConfigurationResponseTypeDef(BaseModel):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFilterResponseTypeDef(BaseModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFindingsReportResponseTypeDef(BaseModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSbomExportResponseTypeDef(BaseModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCisScanConfigurationResponseTypeDef(BaseModel):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFilterResponseTypeDef(BaseModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableDelegatedAdminAccountResponseTypeDef(BaseModel):
    delegatedAdminAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateMemberResponseTypeDef(BaseModel):
    accountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableDelegatedAdminAccountResponseTypeDef(BaseModel):
    delegatedAdminAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCisScanReportResponseTypeDef(BaseModel):
    status: CisReportStatusType
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEc2DeepInspectionConfigurationResponseTypeDef(BaseModel):
    errorMessage: str
    orgPackagePaths: List[str]
    packagePaths: List[str]
    status: Ec2DeepInspectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetEncryptionKeyResponseTypeDef(BaseModel):
    kmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCisScanConfigurationResponseTypeDef(BaseModel):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEc2DeepInspectionConfigurationResponseTypeDef(BaseModel):
    errorMessage: str
    orgPackagePaths: List[str]
    packagePaths: List[str]
    status: Ec2DeepInspectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFilterResponseTypeDef(BaseModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConfigurationResponseTypeDef(BaseModel):
    autoEnable: AutoEnableTypeDef
    maxAccountLimitReached: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOrganizationConfigurationRequestRequestTypeDef(BaseModel):
    autoEnable: AutoEnableTypeDef

class UpdateOrganizationConfigurationResponseTypeDef(BaseModel):
    autoEnable: AutoEnableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AwsLambdaFunctionDetailsTypeDef(BaseModel):
    codeSha256: str
    executionRoleArn: str
    functionName: str
    runtime: RuntimeType
    version: str
    architectures: Optional[List[ArchitectureType]] = None
    lastModifiedAt: Optional[datetime] = None
    layers: Optional[List[str]] = None
    packageType: Optional[PackageTypeType] = None
    vpcConfig: Optional[LambdaVpcConfigTypeDef] = None

class BatchGetMemberEc2DeepInspectionStatusResponseTypeDef(BaseModel):
    accountIds: List[MemberAccountEc2DeepInspectionStatusStateTypeDef]
    failedAccountIds: List[FailedMemberAccountEc2DeepInspectionStatusStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef(BaseModel):
    accountIds: List[MemberAccountEc2DeepInspectionStatusStateTypeDef]
    failedAccountIds: List[FailedMemberAccountEc2DeepInspectionStatusStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef(BaseModel):
    accountIds: Sequence[MemberAccountEc2DeepInspectionStatusTypeDef]

class CisSessionMessageTypeDef(BaseModel):
    cisRuleDetails: BlobTypeDef
    ruleId: str
    status: CisRuleStatusType

class CisCheckAggregationTypeDef(BaseModel):
    scanArn: str
    accountId: Optional[str] = None
    checkDescription: Optional[str] = None
    checkId: Optional[str] = None
    level: Optional[CisSecurityLevelType] = None
    platform: Optional[str] = None
    statusCounts: Optional[StatusCountsTypeDef] = None
    title: Optional[str] = None

class CisTargetResourceAggregationTypeDef(BaseModel):
    scanArn: str
    accountId: Optional[str] = None
    platform: Optional[str] = None
    statusCounts: Optional[StatusCountsTypeDef] = None
    targetResourceId: Optional[str] = None
    targetResourceTags: Optional[Dict[str, List[str]]] = None
    targetStatus: Optional[CisTargetStatusType] = None
    targetStatusReason: Optional[CisTargetStatusReasonType] = None

class CisDateFilterTypeDef(BaseModel):
    earliestScanStartTime: Optional[TimestampTypeDef] = None
    latestScanStartTime: Optional[TimestampTypeDef] = None

class CoverageDateFilterTypeDef(BaseModel):
    endInclusive: Optional[TimestampTypeDef] = None
    startInclusive: Optional[TimestampTypeDef] = None

class DateFilterTypeDef(BaseModel):
    endInclusive: Optional[TimestampTypeDef] = None
    startInclusive: Optional[TimestampTypeDef] = None

class CisScanTypeDef(BaseModel):
    scanArn: str
    scanConfigurationArn: str
    failedChecks: Optional[int] = None
    scanDate: Optional[datetime] = None
    scanName: Optional[str] = None
    scheduledBy: Optional[str] = None
    securityLevel: Optional[CisSecurityLevelType] = None
    status: Optional[CisScanStatusType] = None
    targets: Optional[CisTargetsTypeDef] = None
    totalChecks: Optional[int] = None

class CisScanResultDetailsFilterCriteriaTypeDef(BaseModel):
    checkIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    findingArnFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    findingStatusFilters: Optional[Sequence[CisFindingStatusFilterTypeDef]] = None
    securityLevelFilters: Optional[Sequence[CisSecurityLevelFilterTypeDef]] = None
    titleFilters: Optional[Sequence[CisStringFilterTypeDef]] = None

class CisScanResultsAggregatedByChecksFilterCriteriaTypeDef(BaseModel):
    accountIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    checkIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    failedResourcesFilters: Optional[Sequence[CisNumberFilterTypeDef]] = None
    platformFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    securityLevelFilters: Optional[Sequence[CisSecurityLevelFilterTypeDef]] = None
    titleFilters: Optional[Sequence[CisStringFilterTypeDef]] = None

class GetCisScanResultDetailsResponseTypeDef(BaseModel):
    nextToken: str
    scanResultDetails: List[CisScanResultDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef(BaseModel):
    accountIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    checkIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    failedChecksFilters: Optional[Sequence[CisNumberFilterTypeDef]] = None
    platformFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    statusFilters: Optional[Sequence[CisResultStatusFilterTypeDef]] = None
    targetResourceIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    targetResourceTagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    targetStatusFilters: Optional[Sequence[CisTargetStatusFilterTypeDef]] = None
    targetStatusReasonFilters: Optional[Sequence[CisTargetStatusReasonFilterTypeDef]] = None

class ListCisScanConfigurationsFilterCriteriaTypeDef(BaseModel):
    scanConfigurationArnFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    scanNameFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    targetResourceTagFilters: Optional[Sequence[TagFilterTypeDef]] = None

class CodeVulnerabilityDetailsTypeDef(BaseModel):
    cwes: List[str]
    detectorId: str
    detectorName: str
    filePath: CodeFilePathTypeDef
    detectorTags: Optional[List[str]] = None
    referenceUrls: Optional[List[str]] = None
    ruleId: Optional[str] = None
    sourceLambdaLayerArn: Optional[str] = None

class CodeSnippetResultTypeDef(BaseModel):
    codeSnippet: Optional[List[CodeLineTypeDef]] = None
    endLine: Optional[int] = None
    findingArn: Optional[str] = None
    startLine: Optional[int] = None
    suggestedFixes: Optional[List[SuggestedFixTypeDef]] = None

class ListCoverageStatisticsResponseTypeDef(BaseModel):
    countsByGroup: List[CountsTypeDef]
    nextToken: str
    totalCounts: int
    ResponseMetadata: ResponseMetadataTypeDef

class CvssScoreDetailsTypeDef(BaseModel):
    score: float
    scoreSource: str
    scoringVector: str
    version: str
    adjustments: Optional[List[CvssScoreAdjustmentTypeDef]] = None
    cvssSource: Optional[str] = None

class DailyScheduleTypeDef(BaseModel):
    startTime: TimeTypeDef

class MonthlyScheduleTypeDef(BaseModel):
    day: DayType
    startTime: TimeTypeDef

class WeeklyScheduleExtraOutputTypeDef(BaseModel):
    days: List[DayType]
    startTime: TimeTypeDef

class WeeklyScheduleOutputTypeDef(BaseModel):
    days: List[DayType]
    startTime: TimeTypeDef

class WeeklyScheduleTypeDef(BaseModel):
    days: Sequence[DayType]
    startTime: TimeTypeDef

class ListDelegatedAdminAccountsResponseTypeDef(BaseModel):
    delegatedAdminAccounts: List[DelegatedAdminAccountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDelegatedAdminAccountResponseTypeDef(BaseModel):
    delegatedAdmin: DelegatedAdminTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class Ec2ConfigurationStateTypeDef(BaseModel):
    scanModeState: Optional[Ec2ScanModeStateTypeDef] = None

class Ec2InstanceAggregationTypeDef(BaseModel):
    amis: Optional[Sequence[StringFilterTypeDef]] = None
    instanceIds: Optional[Sequence[StringFilterTypeDef]] = None
    instanceTags: Optional[Sequence[MapFilterTypeDef]] = None
    operatingSystems: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[Ec2InstanceSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class LambdaFunctionAggregationTypeDef(BaseModel):
    functionNames: Optional[Sequence[StringFilterTypeDef]] = None
    functionTags: Optional[Sequence[MapFilterTypeDef]] = None
    resourceIds: Optional[Sequence[StringFilterTypeDef]] = None
    runtimes: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[LambdaFunctionSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class EcrConfigurationStateTypeDef(BaseModel):
    rescanDurationState: Optional[EcrRescanDurationStateTypeDef] = None

class UpdateConfigurationRequestRequestTypeDef(BaseModel):
    ec2Configuration: Optional[Ec2ConfigurationTypeDef] = None
    ecrConfiguration: Optional[EcrConfigurationTypeDef] = None

class FindingDetailTypeDef(BaseModel):
    cisaData: Optional[CisaDataTypeDef] = None
    cwes: Optional[List[str]] = None
    epssScore: Optional[float] = None
    evidences: Optional[List[EvidenceTypeDef]] = None
    exploitObserved: Optional[ExploitObservedTypeDef] = None
    findingArn: Optional[str] = None
    referenceUrls: Optional[List[str]] = None
    riskScore: Optional[int] = None
    tools: Optional[List[str]] = None
    ttps: Optional[List[str]] = None

class VulnerabilityTypeDef(BaseModel):
    id: str
    atigData: Optional[AtigDataTypeDef] = None
    cisaData: Optional[CisaDataTypeDef] = None
    cvss2: Optional[Cvss2TypeDef] = None
    cvss3: Optional[Cvss3TypeDef] = None
    cwes: Optional[List[str]] = None
    description: Optional[str] = None
    detectionPlatforms: Optional[List[str]] = None
    epss: Optional[EpssTypeDef] = None
    exploitObserved: Optional[ExploitObservedTypeDef] = None
    referenceUrls: Optional[List[str]] = None
    relatedVulnerabilities: Optional[List[str]] = None
    source: Optional[Literal["NVD"]] = None
    sourceUrl: Optional[str] = None
    vendorCreatedAt: Optional[datetime] = None
    vendorSeverity: Optional[str] = None
    vendorUpdatedAt: Optional[datetime] = None

class PackageFilterTypeDef(BaseModel):
    architecture: Optional[StringFilterTypeDef] = None
    epoch: Optional[NumberFilterTypeDef] = None
    name: Optional[StringFilterTypeDef] = None
    release: Optional[StringFilterTypeDef] = None
    sourceLambdaLayerArn: Optional[StringFilterTypeDef] = None
    sourceLayerHash: Optional[StringFilterTypeDef] = None
    version: Optional[StringFilterTypeDef] = None

class FreeTrialAccountInfoTypeDef(BaseModel):
    accountId: str
    freeTrialInfo: List[FreeTrialInfoTypeDef]

class ListAccountPermissionsRequestListAccountPermissionsPaginateTypeDef(BaseModel):
    service: Optional[ServiceType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDelegatedAdminAccountsRequestListDelegatedAdminAccountsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFiltersRequestListFiltersPaginateTypeDef(BaseModel):
    action: Optional[FilterActionType] = None
    arns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersRequestListMembersPaginateTypeDef(BaseModel):
    onlyAssociated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsageTotalsRequestListUsageTotalsPaginateTypeDef(BaseModel):
    accountIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetMemberResponseTypeDef(BaseModel):
    member: MemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(BaseModel):
    members: List[MemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceScanMetadataTypeDef(BaseModel):
    ec2: Optional[Ec2MetadataTypeDef] = None
    ecrImage: Optional[EcrContainerImageMetadataTypeDef] = None
    ecrRepository: Optional[EcrRepositoryMetadataTypeDef] = None
    lambdaFunction: Optional[LambdaFunctionMetadataTypeDef] = None

class ListAccountPermissionsResponseTypeDef(BaseModel):
    nextToken: str
    permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkPathTypeDef(BaseModel):
    steps: Optional[List[StepTypeDef]] = None

class PackageVulnerabilityDetailsTypeDef(BaseModel):
    source: str
    vulnerabilityId: str
    cvss: Optional[List[CvssScoreTypeDef]] = None
    referenceUrls: Optional[List[str]] = None
    relatedVulnerabilities: Optional[List[str]] = None
    sourceUrl: Optional[str] = None
    vendorCreatedAt: Optional[datetime] = None
    vendorSeverity: Optional[str] = None
    vendorUpdatedAt: Optional[datetime] = None
    vulnerablePackages: Optional[List[VulnerablePackageTypeDef]] = None

class RemediationTypeDef(BaseModel):
    recommendation: Optional[RecommendationTypeDef] = None

class ResourceFilterCriteriaOutputTypeDef(BaseModel):
    accountId: Optional[List[ResourceStringFilterTypeDef]] = None
    ec2InstanceTags: Optional[List[ResourceMapFilterTypeDef]] = None
    ecrImageTags: Optional[List[ResourceStringFilterTypeDef]] = None
    ecrRepositoryName: Optional[List[ResourceStringFilterTypeDef]] = None
    lambdaFunctionName: Optional[List[ResourceStringFilterTypeDef]] = None
    lambdaFunctionTags: Optional[List[ResourceMapFilterTypeDef]] = None
    resourceId: Optional[List[ResourceStringFilterTypeDef]] = None
    resourceType: Optional[List[ResourceStringFilterTypeDef]] = None

class ResourceFilterCriteriaTypeDef(BaseModel):
    accountId: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    ec2InstanceTags: Optional[Sequence[ResourceMapFilterTypeDef]] = None
    ecrImageTags: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    ecrRepositoryName: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    lambdaFunctionName: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    lambdaFunctionTags: Optional[Sequence[ResourceMapFilterTypeDef]] = None
    resourceId: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    resourceType: Optional[Sequence[ResourceStringFilterTypeDef]] = None

class SearchVulnerabilitiesRequestRequestTypeDef(BaseModel):
    filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef
    nextToken: Optional[str] = None

class SearchVulnerabilitiesRequestSearchVulnerabilitiesPaginateTypeDef(BaseModel):
    filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class StartCisSessionRequestRequestTypeDef(BaseModel):
    message: StartCisSessionMessageTypeDef
    scanJobId: str

class StopCisSessionMessageTypeDef(BaseModel):
    progress: StopCisMessageProgressTypeDef
    status: StopCisSessionStatusType
    benchmarkProfile: Optional[str] = None
    benchmarkVersion: Optional[str] = None
    computePlatform: Optional[ComputePlatformTypeDef] = None
    reason: Optional[str] = None

class UsageTotalTypeDef(BaseModel):
    accountId: Optional[str] = None
    usage: Optional[List[UsageTypeDef]] = None

class AggregationResponseTypeDef(BaseModel):
    accountAggregation: Optional[AccountAggregationResponseTypeDef] = None
    amiAggregation: Optional[AmiAggregationResponseTypeDef] = None
    awsEcrContainerAggregation: Optional[AwsEcrContainerAggregationResponseTypeDef] = None
    ec2InstanceAggregation: Optional[Ec2InstanceAggregationResponseTypeDef] = None
    findingTypeAggregation: Optional[FindingTypeAggregationResponseTypeDef] = None
    imageLayerAggregation: Optional[ImageLayerAggregationResponseTypeDef] = None
    lambdaFunctionAggregation: Optional[LambdaFunctionAggregationResponseTypeDef] = None
    lambdaLayerAggregation: Optional[LambdaLayerAggregationResponseTypeDef] = None
    packageAggregation: Optional[PackageAggregationResponseTypeDef] = None
    repositoryAggregation: Optional[RepositoryAggregationResponseTypeDef] = None
    titleAggregation: Optional[TitleAggregationResponseTypeDef] = None

class AccountStateTypeDef(BaseModel):
    accountId: str
    resourceState: ResourceStateTypeDef
    state: StateTypeDef

class DisableResponseTypeDef(BaseModel):
    accounts: List[AccountTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnableResponseTypeDef(BaseModel):
    accounts: List[AccountTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceDetailsTypeDef(BaseModel):
    awsEc2Instance: Optional[AwsEc2InstanceDetailsTypeDef] = None
    awsEcrContainerImage: Optional[AwsEcrContainerImageDetailsTypeDef] = None
    awsLambdaFunction: Optional[AwsLambdaFunctionDetailsTypeDef] = None

class SendCisSessionTelemetryRequestRequestTypeDef(BaseModel):
    messages: Sequence[CisSessionMessageTypeDef]
    scanJobId: str
    sessionToken: str

class ListCisScanResultsAggregatedByChecksResponseTypeDef(BaseModel):
    checkAggregations: List[CisCheckAggregationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCisScanResultsAggregatedByTargetResourceResponseTypeDef(BaseModel):
    nextToken: str
    targetResourceAggregations: List[CisTargetResourceAggregationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCisScansFilterCriteriaTypeDef(BaseModel):
    failedChecksFilters: Optional[Sequence[CisNumberFilterTypeDef]] = None
    scanArnFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    scanAtFilters: Optional[Sequence[CisDateFilterTypeDef]] = None
    scanConfigurationArnFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    scanNameFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    scanStatusFilters: Optional[Sequence[CisScanStatusFilterTypeDef]] = None
    scheduledByFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    targetAccountIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    targetResourceIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    targetResourceTagFilters: Optional[Sequence[TagFilterTypeDef]] = None

class CoverageFilterCriteriaTypeDef(BaseModel):
    accountId: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    ec2InstanceTags: Optional[Sequence[CoverageMapFilterTypeDef]] = None
    ecrImageTags: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    ecrRepositoryName: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    imagePulledAt: Optional[Sequence[CoverageDateFilterTypeDef]] = None
    lambdaFunctionName: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    lambdaFunctionRuntime: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    lambdaFunctionTags: Optional[Sequence[CoverageMapFilterTypeDef]] = None
    lastScannedAt: Optional[Sequence[CoverageDateFilterTypeDef]] = None
    resourceId: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    resourceType: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    scanMode: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    scanStatusCode: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    scanStatusReason: Optional[Sequence[CoverageStringFilterTypeDef]] = None
    scanType: Optional[Sequence[CoverageStringFilterTypeDef]] = None

class ListCisScansResponseTypeDef(BaseModel):
    nextToken: str
    scans: List[CisScanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCisScanResultDetailsRequestGetCisScanResultDetailsPaginateTypeDef(BaseModel):
    accountId: str
    scanArn: str
    targetResourceId: str
    filterCriteria: Optional[CisScanResultDetailsFilterCriteriaTypeDef] = None
    sortBy: Optional[CisScanResultDetailsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCisScanResultDetailsRequestRequestTypeDef(BaseModel):
    accountId: str
    scanArn: str
    targetResourceId: str
    filterCriteria: Optional[CisScanResultDetailsFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanResultDetailsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None

class ListCisScanResultsAggregatedByChecksRequestListCisScanResultsAggregatedByChecksPaginateTypeDef(BaseModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef] = None
    sortBy: Optional[CisScanResultsAggregatedByChecksSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCisScanResultsAggregatedByChecksRequestRequestTypeDef(BaseModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanResultsAggregatedByChecksSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None

class ListCisScanResultsAggregatedByTargetResourceRequestListCisScanResultsAggregatedByTargetResourcePaginateTypeDef(BaseModel):
    scanArn: str
    filterCriteria: Optional[       CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef     ] = None
    sortBy: Optional[CisScanResultsAggregatedByTargetResourceSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef(BaseModel):
    scanArn: str
    filterCriteria: Optional[       CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef     ] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanResultsAggregatedByTargetResourceSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None

class ListCisScanConfigurationsRequestListCisScanConfigurationsPaginateTypeDef(BaseModel):
    filterCriteria: Optional[ListCisScanConfigurationsFilterCriteriaTypeDef] = None
    sortBy: Optional[CisScanConfigurationsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCisScanConfigurationsRequestRequestTypeDef(BaseModel):
    filterCriteria: Optional[ListCisScanConfigurationsFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanConfigurationsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None

class BatchGetCodeSnippetResponseTypeDef(BaseModel):
    codeSnippetResults: List[CodeSnippetResultTypeDef]
    errors: List[CodeSnippetErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InspectorScoreDetailsTypeDef(BaseModel):
    adjustedCvss: Optional[CvssScoreDetailsTypeDef] = None

class ScheduleExtraOutputTypeDef(BaseModel):
    daily: Optional[DailyScheduleTypeDef] = None
    monthly: Optional[MonthlyScheduleTypeDef] = None
    oneTime: Optional[Dict[str, Any]] = None
    weekly: Optional[WeeklyScheduleExtraOutputTypeDef] = None

class ScheduleOutputTypeDef(BaseModel):
    daily: Optional[DailyScheduleTypeDef] = None
    monthly: Optional[MonthlyScheduleTypeDef] = None
    oneTime: Optional[Dict[str, Any]] = None
    weekly: Optional[WeeklyScheduleOutputTypeDef] = None

class ScheduleTypeDef(BaseModel):
    daily: Optional[DailyScheduleTypeDef] = None
    monthly: Optional[MonthlyScheduleTypeDef] = None
    oneTime: Optional[Mapping[str, Any]] = None
    weekly: Optional[WeeklyScheduleTypeDef] = None

class AggregationRequestTypeDef(BaseModel):
    accountAggregation: Optional[AccountAggregationTypeDef] = None
    amiAggregation: Optional[AmiAggregationTypeDef] = None
    awsEcrContainerAggregation: Optional[AwsEcrContainerAggregationTypeDef] = None
    ec2InstanceAggregation: Optional[Ec2InstanceAggregationTypeDef] = None
    findingTypeAggregation: Optional[FindingTypeAggregationTypeDef] = None
    imageLayerAggregation: Optional[ImageLayerAggregationTypeDef] = None
    lambdaFunctionAggregation: Optional[LambdaFunctionAggregationTypeDef] = None
    lambdaLayerAggregation: Optional[LambdaLayerAggregationTypeDef] = None
    packageAggregation: Optional[PackageAggregationTypeDef] = None
    repositoryAggregation: Optional[RepositoryAggregationTypeDef] = None
    titleAggregation: Optional[TitleAggregationTypeDef] = None

class GetConfigurationResponseTypeDef(BaseModel):
    ec2Configuration: Ec2ConfigurationStateTypeDef
    ecrConfiguration: EcrConfigurationStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetFindingDetailsResponseTypeDef(BaseModel):
    errors: List[FindingDetailsErrorTypeDef]
    findingDetails: List[FindingDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchVulnerabilitiesResponseTypeDef(BaseModel):
    nextToken: str
    vulnerabilities: List[VulnerabilityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FilterCriteriaExtraOutputTypeDef(BaseModel):
    awsAccountId: Optional[List[StringFilterTypeDef]] = None
    codeVulnerabilityDetectorName: Optional[List[StringFilterTypeDef]] = None
    codeVulnerabilityDetectorTags: Optional[List[StringFilterTypeDef]] = None
    codeVulnerabilityFilePath: Optional[List[StringFilterTypeDef]] = None
    componentId: Optional[List[StringFilterTypeDef]] = None
    componentType: Optional[List[StringFilterTypeDef]] = None
    ec2InstanceImageId: Optional[List[StringFilterTypeDef]] = None
    ec2InstanceSubnetId: Optional[List[StringFilterTypeDef]] = None
    ec2InstanceVpcId: Optional[List[StringFilterTypeDef]] = None
    ecrImageArchitecture: Optional[List[StringFilterTypeDef]] = None
    ecrImageHash: Optional[List[StringFilterTypeDef]] = None
    ecrImagePushedAt: Optional[List[DateFilterExtraOutputTypeDef]] = None
    ecrImageRegistry: Optional[List[StringFilterTypeDef]] = None
    ecrImageRepositoryName: Optional[List[StringFilterTypeDef]] = None
    ecrImageTags: Optional[List[StringFilterTypeDef]] = None
    epssScore: Optional[List[NumberFilterTypeDef]] = None
    exploitAvailable: Optional[List[StringFilterTypeDef]] = None
    findingArn: Optional[List[StringFilterTypeDef]] = None
    findingStatus: Optional[List[StringFilterTypeDef]] = None
    findingType: Optional[List[StringFilterTypeDef]] = None
    firstObservedAt: Optional[List[DateFilterExtraOutputTypeDef]] = None
    fixAvailable: Optional[List[StringFilterTypeDef]] = None
    inspectorScore: Optional[List[NumberFilterTypeDef]] = None
    lambdaFunctionExecutionRoleArn: Optional[List[StringFilterTypeDef]] = None
    lambdaFunctionLastModifiedAt: Optional[List[DateFilterExtraOutputTypeDef]] = None
    lambdaFunctionLayers: Optional[List[StringFilterTypeDef]] = None
    lambdaFunctionName: Optional[List[StringFilterTypeDef]] = None
    lambdaFunctionRuntime: Optional[List[StringFilterTypeDef]] = None
    lastObservedAt: Optional[List[DateFilterExtraOutputTypeDef]] = None
    networkProtocol: Optional[List[StringFilterTypeDef]] = None
    portRange: Optional[List[PortRangeFilterTypeDef]] = None
    relatedVulnerabilities: Optional[List[StringFilterTypeDef]] = None
    resourceId: Optional[List[StringFilterTypeDef]] = None
    resourceTags: Optional[List[MapFilterTypeDef]] = None
    resourceType: Optional[List[StringFilterTypeDef]] = None
    severity: Optional[List[StringFilterTypeDef]] = None
    title: Optional[List[StringFilterTypeDef]] = None
    updatedAt: Optional[List[DateFilterExtraOutputTypeDef]] = None
    vendorSeverity: Optional[List[StringFilterTypeDef]] = None
    vulnerabilityId: Optional[List[StringFilterTypeDef]] = None
    vulnerabilitySource: Optional[List[StringFilterTypeDef]] = None
    vulnerablePackages: Optional[List[PackageFilterTypeDef]] = None

class FilterCriteriaOutputTypeDef(BaseModel):
    awsAccountId: Optional[List[StringFilterTypeDef]] = None
    codeVulnerabilityDetectorName: Optional[List[StringFilterTypeDef]] = None
    codeVulnerabilityDetectorTags: Optional[List[StringFilterTypeDef]] = None
    codeVulnerabilityFilePath: Optional[List[StringFilterTypeDef]] = None
    componentId: Optional[List[StringFilterTypeDef]] = None
    componentType: Optional[List[StringFilterTypeDef]] = None
    ec2InstanceImageId: Optional[List[StringFilterTypeDef]] = None
    ec2InstanceSubnetId: Optional[List[StringFilterTypeDef]] = None
    ec2InstanceVpcId: Optional[List[StringFilterTypeDef]] = None
    ecrImageArchitecture: Optional[List[StringFilterTypeDef]] = None
    ecrImageHash: Optional[List[StringFilterTypeDef]] = None
    ecrImagePushedAt: Optional[List[DateFilterOutputTypeDef]] = None
    ecrImageRegistry: Optional[List[StringFilterTypeDef]] = None
    ecrImageRepositoryName: Optional[List[StringFilterTypeDef]] = None
    ecrImageTags: Optional[List[StringFilterTypeDef]] = None
    epssScore: Optional[List[NumberFilterTypeDef]] = None
    exploitAvailable: Optional[List[StringFilterTypeDef]] = None
    findingArn: Optional[List[StringFilterTypeDef]] = None
    findingStatus: Optional[List[StringFilterTypeDef]] = None
    findingType: Optional[List[StringFilterTypeDef]] = None
    firstObservedAt: Optional[List[DateFilterOutputTypeDef]] = None
    fixAvailable: Optional[List[StringFilterTypeDef]] = None
    inspectorScore: Optional[List[NumberFilterTypeDef]] = None
    lambdaFunctionExecutionRoleArn: Optional[List[StringFilterTypeDef]] = None
    lambdaFunctionLastModifiedAt: Optional[List[DateFilterOutputTypeDef]] = None
    lambdaFunctionLayers: Optional[List[StringFilterTypeDef]] = None
    lambdaFunctionName: Optional[List[StringFilterTypeDef]] = None
    lambdaFunctionRuntime: Optional[List[StringFilterTypeDef]] = None
    lastObservedAt: Optional[List[DateFilterOutputTypeDef]] = None
    networkProtocol: Optional[List[StringFilterTypeDef]] = None
    portRange: Optional[List[PortRangeFilterTypeDef]] = None
    relatedVulnerabilities: Optional[List[StringFilterTypeDef]] = None
    resourceId: Optional[List[StringFilterTypeDef]] = None
    resourceTags: Optional[List[MapFilterTypeDef]] = None
    resourceType: Optional[List[StringFilterTypeDef]] = None
    severity: Optional[List[StringFilterTypeDef]] = None
    title: Optional[List[StringFilterTypeDef]] = None
    updatedAt: Optional[List[DateFilterOutputTypeDef]] = None
    vendorSeverity: Optional[List[StringFilterTypeDef]] = None
    vulnerabilityId: Optional[List[StringFilterTypeDef]] = None
    vulnerabilitySource: Optional[List[StringFilterTypeDef]] = None
    vulnerablePackages: Optional[List[PackageFilterTypeDef]] = None

class FilterCriteriaTypeDef(BaseModel):
    awsAccountId: Optional[Sequence[StringFilterTypeDef]] = None
    codeVulnerabilityDetectorName: Optional[Sequence[StringFilterTypeDef]] = None
    codeVulnerabilityDetectorTags: Optional[Sequence[StringFilterTypeDef]] = None
    codeVulnerabilityFilePath: Optional[Sequence[StringFilterTypeDef]] = None
    componentId: Optional[Sequence[StringFilterTypeDef]] = None
    componentType: Optional[Sequence[StringFilterTypeDef]] = None
    ec2InstanceImageId: Optional[Sequence[StringFilterTypeDef]] = None
    ec2InstanceSubnetId: Optional[Sequence[StringFilterTypeDef]] = None
    ec2InstanceVpcId: Optional[Sequence[StringFilterTypeDef]] = None
    ecrImageArchitecture: Optional[Sequence[StringFilterTypeDef]] = None
    ecrImageHash: Optional[Sequence[StringFilterTypeDef]] = None
    ecrImagePushedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ecrImageRegistry: Optional[Sequence[StringFilterTypeDef]] = None
    ecrImageRepositoryName: Optional[Sequence[StringFilterTypeDef]] = None
    ecrImageTags: Optional[Sequence[StringFilterTypeDef]] = None
    epssScore: Optional[Sequence[NumberFilterTypeDef]] = None
    exploitAvailable: Optional[Sequence[StringFilterTypeDef]] = None
    findingArn: Optional[Sequence[StringFilterTypeDef]] = None
    findingStatus: Optional[Sequence[StringFilterTypeDef]] = None
    findingType: Optional[Sequence[StringFilterTypeDef]] = None
    firstObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    fixAvailable: Optional[Sequence[StringFilterTypeDef]] = None
    inspectorScore: Optional[Sequence[NumberFilterTypeDef]] = None
    lambdaFunctionExecutionRoleArn: Optional[Sequence[StringFilterTypeDef]] = None
    lambdaFunctionLastModifiedAt: Optional[Sequence[DateFilterTypeDef]] = None
    lambdaFunctionLayers: Optional[Sequence[StringFilterTypeDef]] = None
    lambdaFunctionName: Optional[Sequence[StringFilterTypeDef]] = None
    lambdaFunctionRuntime: Optional[Sequence[StringFilterTypeDef]] = None
    lastObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    networkProtocol: Optional[Sequence[StringFilterTypeDef]] = None
    portRange: Optional[Sequence[PortRangeFilterTypeDef]] = None
    relatedVulnerabilities: Optional[Sequence[StringFilterTypeDef]] = None
    resourceId: Optional[Sequence[StringFilterTypeDef]] = None
    resourceTags: Optional[Sequence[MapFilterTypeDef]] = None
    resourceType: Optional[Sequence[StringFilterTypeDef]] = None
    severity: Optional[Sequence[StringFilterTypeDef]] = None
    title: Optional[Sequence[StringFilterTypeDef]] = None
    updatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    vendorSeverity: Optional[Sequence[StringFilterTypeDef]] = None
    vulnerabilityId: Optional[Sequence[StringFilterTypeDef]] = None
    vulnerabilitySource: Optional[Sequence[StringFilterTypeDef]] = None
    vulnerablePackages: Optional[Sequence[PackageFilterTypeDef]] = None

class BatchGetFreeTrialInfoResponseTypeDef(BaseModel):
    accounts: List[FreeTrialAccountInfoTypeDef]
    failedAccounts: List[FreeTrialInfoErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CoveredResourceTypeDef(BaseModel):
    accountId: str
    resourceId: str
    resourceType: CoverageResourceTypeType
    scanType: ScanTypeType
    lastScannedAt: Optional[datetime] = None
    resourceMetadata: Optional[ResourceScanMetadataTypeDef] = None
    scanMode: Optional[ScanModeType] = None
    scanStatus: Optional[ScanStatusTypeDef] = None

class NetworkReachabilityDetailsTypeDef(BaseModel):
    networkPath: NetworkPathTypeDef
    openPortRange: PortRangeTypeDef
    protocol: NetworkProtocolType

class GetSbomExportResponseTypeDef(BaseModel):
    errorCode: ReportingErrorCodeType
    errorMessage: str
    filterCriteria: ResourceFilterCriteriaOutputTypeDef
    format: SbomReportFormatType
    reportId: str
    s3Destination: DestinationTypeDef
    status: ExternalReportStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSbomExportRequestRequestTypeDef(BaseModel):
    reportFormat: SbomReportFormatType
    s3Destination: DestinationTypeDef
    resourceFilterCriteria: Optional[ResourceFilterCriteriaTypeDef] = None

class StopCisSessionRequestRequestTypeDef(BaseModel):
    message: StopCisSessionMessageTypeDef
    scanJobId: str
    sessionToken: str

class ListUsageTotalsResponseTypeDef(BaseModel):
    nextToken: str
    totals: List[UsageTotalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingAggregationsResponseTypeDef(BaseModel):
    aggregationType: AggregationTypeType
    nextToken: str
    responses: List[AggregationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAccountStatusResponseTypeDef(BaseModel):
    accounts: List[AccountStateTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceTypeDef(BaseModel):
    id: str
    type: ResourceTypeType
    details: Optional[ResourceDetailsTypeDef] = None
    partition: Optional[str] = None
    region: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListCisScansRequestListCisScansPaginateTypeDef(BaseModel):
    detailLevel: Optional[ListCisScansDetailLevelType] = None
    filterCriteria: Optional[ListCisScansFilterCriteriaTypeDef] = None
    sortBy: Optional[ListCisScansSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCisScansRequestRequestTypeDef(BaseModel):
    detailLevel: Optional[ListCisScansDetailLevelType] = None
    filterCriteria: Optional[ListCisScansFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[ListCisScansSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None

class ListCoverageRequestListCoveragePaginateTypeDef(BaseModel):
    filterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoverageRequestRequestTypeDef(BaseModel):
    filterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListCoverageStatisticsRequestListCoverageStatisticsPaginateTypeDef(BaseModel):
    filterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    groupBy: Optional[GroupKeyType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoverageStatisticsRequestRequestTypeDef(BaseModel):
    filterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    groupBy: Optional[GroupKeyType] = None
    nextToken: Optional[str] = None

class CisScanConfigurationTypeDef(BaseModel):
    scanConfigurationArn: str
    ownerId: Optional[str] = None
    scanName: Optional[str] = None
    schedule: Optional[ScheduleOutputTypeDef] = None
    securityLevel: Optional[CisSecurityLevelType] = None
    tags: Optional[Dict[str, str]] = None
    targets: Optional[CisTargetsTypeDef] = None

class CreateCisScanConfigurationRequestRequestTypeDef(BaseModel):
    scanName: str
    schedule: ScheduleTypeDef
    securityLevel: CisSecurityLevelType
    targets: CreateCisTargetsTypeDef
    tags: Optional[Mapping[str, str]] = None

class UpdateCisScanConfigurationRequestRequestTypeDef(BaseModel):
    scanConfigurationArn: str
    scanName: Optional[str] = None
    schedule: Optional[ScheduleTypeDef] = None
    securityLevel: Optional[CisSecurityLevelType] = None
    targets: Optional[UpdateCisTargetsTypeDef] = None

class ListFindingAggregationsRequestListFindingAggregationsPaginateTypeDef(BaseModel):
    aggregationType: AggregationTypeType
    accountIds: Optional[Sequence[StringFilterTypeDef]] = None
    aggregationRequest: Optional[AggregationRequestTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingAggregationsRequestRequestTypeDef(BaseModel):
    aggregationType: AggregationTypeType
    accountIds: Optional[Sequence[StringFilterTypeDef]] = None
    aggregationRequest: Optional[AggregationRequestTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class FilterTypeDef(BaseModel):
    action: FilterActionType
    arn: str
    createdAt: datetime
    criteria: FilterCriteriaOutputTypeDef
    name: str
    ownerId: str
    updatedAt: datetime
    description: Optional[str] = None
    reason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GetFindingsReportStatusResponseTypeDef(BaseModel):
    destination: DestinationTypeDef
    errorCode: ReportingErrorCodeType
    errorMessage: str
    filterCriteria: FilterCriteriaOutputTypeDef
    reportId: str
    status: ExternalReportStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFilterRequestRequestTypeDef(BaseModel):
    action: FilterActionType
    filterCriteria: FilterCriteriaTypeDef
    name: str
    description: Optional[str] = None
    reason: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateFindingsReportRequestRequestTypeDef(BaseModel):
    reportFormat: ReportFormatType
    s3Destination: DestinationTypeDef
    filterCriteria: Optional[FilterCriteriaTypeDef] = None

class ListFindingsRequestListFindingsPaginateTypeDef(BaseModel):
    filterCriteria: Optional[FilterCriteriaTypeDef] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsRequestRequestTypeDef(BaseModel):
    filterCriteria: Optional[FilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None

class UpdateFilterRequestRequestTypeDef(BaseModel):
    filterArn: str
    action: Optional[FilterActionType] = None
    description: Optional[str] = None
    filterCriteria: Optional[FilterCriteriaTypeDef] = None
    name: Optional[str] = None
    reason: Optional[str] = None

class ListCoverageResponseTypeDef(BaseModel):
    coveredResources: List[CoveredResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FindingTypeDef(BaseModel):
    awsAccountId: str
    description: str
    findingArn: str
    firstObservedAt: datetime
    lastObservedAt: datetime
    remediation: RemediationTypeDef
    resources: List[ResourceTypeDef]
    severity: SeverityType
    status: FindingStatusType
    type: FindingTypeType
    codeVulnerabilityDetails: Optional[CodeVulnerabilityDetailsTypeDef] = None
    epss: Optional[EpssDetailsTypeDef] = None
    exploitAvailable: Optional[ExploitAvailableType] = None
    exploitabilityDetails: Optional[ExploitabilityDetailsTypeDef] = None
    fixAvailable: Optional[FixAvailableType] = None
    inspectorScore: Optional[float] = None
    inspectorScoreDetails: Optional[InspectorScoreDetailsTypeDef] = None
    networkReachabilityDetails: Optional[NetworkReachabilityDetailsTypeDef] = None
    packageVulnerabilityDetails: Optional[PackageVulnerabilityDetailsTypeDef] = None
    title: Optional[str] = None
    updatedAt: Optional[datetime] = None

class ListCisScanConfigurationsResponseTypeDef(BaseModel):
    nextToken: str
    scanConfigurations: List[CisScanConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFiltersResponseTypeDef(BaseModel):
    filters: List[FilterTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingsResponseTypeDef(BaseModel):
    findings: List[FindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


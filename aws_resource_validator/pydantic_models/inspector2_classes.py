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
from aws_resource_validator.pydantic_models.inspector2_constants import *

class AccountAggregationTypeDef(BaseValidatorModel):
    findingType: Optional[AggregationFindingTypeType] = None
    resourceType: Optional[AggregationResourceTypeType] = None
    sortBy: Optional[AccountSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class StateTypeDef(BaseValidatorModel):
    errorCode: ErrorCodeType
    errorMessage: str
    status: StatusType


class FindingTypeAggregationTypeDef(BaseValidatorModel):
    findingType: Optional[AggregationFindingTypeType] = None
    resourceType: Optional[AggregationResourceTypeType] = None
    sortBy: Optional[FindingTypeSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class StringFilterTypeDef(BaseValidatorModel):
    comparison: StringComparisonType
    value: str


class AssociateMemberRequestTypeDef(BaseValidatorModel):
    accountId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AtigDataTypeDef(BaseValidatorModel):
    firstSeen: Optional[datetime] = None
    lastSeen: Optional[datetime] = None
    targets: Optional[List[str]] = None
    ttps: Optional[List[str]] = None


class AwsEcrContainerImageDetailsTypeDef(BaseValidatorModel):
    imageHash: str
    registry: str
    repositoryName: str
    architecture: Optional[str] = None
    author: Optional[str] = None
    imageTags: Optional[List[str]] = None
    platform: Optional[str] = None
    pushedAt: Optional[datetime] = None


class LambdaVpcConfigTypeDef(BaseValidatorModel):
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None


class BatchGetAccountStatusRequestTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None


class BatchGetCodeSnippetRequestTypeDef(BaseValidatorModel):
    findingArns: Sequence[str]


class CodeSnippetErrorTypeDef(BaseValidatorModel):
    errorCode: CodeSnippetErrorCodeType
    errorMessage: str
    findingArn: str


class BatchGetFindingDetailsRequestTypeDef(BaseValidatorModel):
    findingArns: Sequence[str]


class FindingDetailsErrorTypeDef(BaseValidatorModel):
    errorCode: FindingDetailsErrorCodeType
    errorMessage: str
    findingArn: str


class BatchGetFreeTrialInfoRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]


class FreeTrialInfoErrorTypeDef(BaseValidatorModel):
    accountId: str
    code: FreeTrialInfoErrorCodeType
    message: str


class BatchGetMemberEc2DeepInspectionStatusRequestTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None


class FailedMemberAccountEc2DeepInspectionStatusStateTypeDef(BaseValidatorModel):
    accountId: str
    ec2ScanStatus: Optional[StatusType] = None
    errorMessage: Optional[str] = None


class MemberAccountEc2DeepInspectionStatusStateTypeDef(BaseValidatorModel):
    accountId: str
    errorMessage: Optional[str] = None
    status: Optional[Ec2DeepInspectionStatusType] = None


class MemberAccountEc2DeepInspectionStatusTypeDef(BaseValidatorModel):
    accountId: str
    activateDeepInspection: bool


class CancelFindingsReportRequestTypeDef(BaseValidatorModel):
    reportId: str


class CancelSbomExportRequestTypeDef(BaseValidatorModel):
    reportId: str


class StatusCountsTypeDef(BaseValidatorModel):
    failed: Optional[int] = None
    passed: Optional[int] = None
    skipped: Optional[int] = None


class CisFindingStatusFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    value: CisFindingStatusType


class CisNumberFilterTypeDef(BaseValidatorModel):
    lowerInclusive: Optional[int] = None
    upperInclusive: Optional[int] = None


class CisResultStatusFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    value: CisResultStatusType


class CisTargetsTypeDef(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    targetResourceTags: Optional[Dict[str, List[str]]] = None


class CisSecurityLevelFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    value: CisSecurityLevelType


class CisStringFilterTypeDef(BaseValidatorModel):
    comparison: CisStringComparisonType
    value: str


class CisScanResultDetailsTypeDef(BaseValidatorModel):
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


class CisTargetStatusFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    value: CisTargetStatusType


class CisTargetStatusReasonFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    value: CisTargetStatusReasonType


class TagFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    key: str
    value: str


class CisScanStatusFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    value: CisScanStatusType


class CisaDataTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    dateAdded: Optional[datetime] = None
    dateDue: Optional[datetime] = None


class CodeFilePathTypeDef(BaseValidatorModel):
    endLine: int
    fileName: str
    filePath: str
    startLine: int


class CodeLineTypeDef(BaseValidatorModel):
    content: str
    lineNumber: int


class SuggestedFixTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    description: Optional[str] = None


class ComputePlatformTypeDef(BaseValidatorModel):
    product: Optional[str] = None
    vendor: Optional[str] = None
    version: Optional[str] = None


class CountsTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    groupKey: Optional[GroupKeyType] = None


class CoverageMapFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    key: str
    value: Optional[str] = None


class CoverageStringFilterTypeDef(BaseValidatorModel):
    comparison: CoverageStringComparisonType
    value: str


class ScanStatusTypeDef(BaseValidatorModel):
    reason: ScanStatusReasonType
    statusCode: ScanStatusCodeType


class CreateCisTargetsTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]
    targetResourceTags: Mapping[str, Sequence[str]]


class DestinationTypeDef(BaseValidatorModel):
    bucketName: str
    kmsKeyArn: str
    keyPrefix: Optional[str] = None


class Cvss2TypeDef(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None


class Cvss3TypeDef(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None


class CvssScoreAdjustmentTypeDef(BaseValidatorModel):
    metric: str
    reason: str


class CvssScoreTypeDef(BaseValidatorModel):
    baseScore: float
    scoringVector: str
    source: str
    version: str


class TimeTypeDef(BaseValidatorModel):
    timeOfDay: str
    timezone: str


class DateFilterOutputTypeDef(BaseValidatorModel):
    endInclusive: Optional[datetime] = None
    startInclusive: Optional[datetime] = None


class DelegatedAdminAccountTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[DelegatedAdminStatusType] = None


class DelegatedAdminTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    relationshipStatus: Optional[RelationshipStatusType] = None


class DeleteCisScanConfigurationRequestTypeDef(BaseValidatorModel):
    scanConfigurationArn: str


class DeleteFilterRequestTypeDef(BaseValidatorModel):
    arn: str


class DisableDelegatedAdminAccountRequestTypeDef(BaseValidatorModel):
    delegatedAdminAccountId: str


class DisableRequestTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    resourceTypes: Optional[Sequence[ResourceScanTypeType]] = None


class DisassociateMemberRequestTypeDef(BaseValidatorModel):
    accountId: str


class Ec2ScanModeStateTypeDef(BaseValidatorModel):
    scanMode: Optional[Ec2ScanModeType] = None
    scanModeStatus: Optional[Ec2ScanModeStatusType] = None


class Ec2ConfigurationTypeDef(BaseValidatorModel):
    scanMode: Ec2ScanModeType


class MapFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    key: str
    value: Optional[str] = None


class Ec2MetadataTypeDef(BaseValidatorModel):
    amiId: Optional[str] = None
    platform: Optional[Ec2PlatformType] = None
    tags: Optional[Dict[str, str]] = None


class EcrRescanDurationStateTypeDef(BaseValidatorModel):
    pullDateRescanDuration: Optional[EcrPullDateRescanDurationType] = None
    rescanDuration: Optional[EcrRescanDurationType] = None
    status: Optional[EcrRescanDurationStatusType] = None
    updatedAt: Optional[datetime] = None


class EcrConfigurationTypeDef(BaseValidatorModel):
    rescanDuration: EcrRescanDurationType
    pullDateRescanDuration: Optional[EcrPullDateRescanDurationType] = None


class EcrContainerImageMetadataTypeDef(BaseValidatorModel):
    imagePulledAt: Optional[datetime] = None
    tags: Optional[List[str]] = None


class EcrRepositoryMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    scanFrequency: Optional[EcrScanFrequencyType] = None


class EnableDelegatedAdminAccountRequestTypeDef(BaseValidatorModel):
    delegatedAdminAccountId: str
    clientToken: Optional[str] = None


class EnableRequestTypeDef(BaseValidatorModel):
    resourceTypes: Sequence[ResourceScanTypeType]
    accountIds: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None


class EpssDetailsTypeDef(BaseValidatorModel):
    score: Optional[float] = None


class EpssTypeDef(BaseValidatorModel):
    score: Optional[float] = None


class EvidenceTypeDef(BaseValidatorModel):
    evidenceDetail: Optional[str] = None
    evidenceRule: Optional[str] = None
    severity: Optional[str] = None


class ExploitObservedTypeDef(BaseValidatorModel):
    firstSeen: Optional[datetime] = None
    lastSeen: Optional[datetime] = None


class ExploitabilityDetailsTypeDef(BaseValidatorModel):
    lastKnownExploitAt: Optional[datetime] = None


class NumberFilterTypeDef(BaseValidatorModel):
    lowerInclusive: Optional[float] = None
    upperInclusive: Optional[float] = None


class PortRangeFilterTypeDef(BaseValidatorModel):
    beginInclusive: Optional[int] = None
    endInclusive: Optional[int] = None


class GetCisScanReportRequestTypeDef(BaseValidatorModel):
    scanArn: str
    reportFormat: Optional[CisReportFormatType] = None
    targetAccounts: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetEncryptionKeyRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    scanType: ScanTypeType


class GetFindingsReportStatusRequestTypeDef(BaseValidatorModel):
    reportId: Optional[str] = None


class GetMemberRequestTypeDef(BaseValidatorModel):
    accountId: str


class MemberTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    delegatedAdminAccountId: Optional[str] = None
    relationshipStatus: Optional[RelationshipStatusType] = None
    updatedAt: Optional[datetime] = None


class GetSbomExportRequestTypeDef(BaseValidatorModel):
    reportId: str


class LambdaFunctionMetadataTypeDef(BaseValidatorModel):
    functionName: Optional[str] = None
    functionTags: Optional[Dict[str, str]] = None
    layers: Optional[List[str]] = None
    runtime: Optional[RuntimeType] = None


class ListAccountPermissionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    service: Optional[ServiceType] = None


class PermissionTypeDef(BaseValidatorModel):
    operation: OperationType
    service: ServiceType


class ListDelegatedAdminAccountsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFiltersRequestTypeDef(BaseValidatorModel):
    action: Optional[FilterActionType] = None
    arns: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SortCriteriaTypeDef(BaseValidatorModel):
    field: SortFieldType
    sortOrder: SortOrderType


class ListMembersRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    onlyAssociated: Optional[bool] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListUsageTotalsRequestTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class StepTypeDef(BaseValidatorModel):
    componentId: str
    componentType: str


class PortRangeTypeDef(BaseValidatorModel):
    begin: int
    end: int


class VulnerablePackageTypeDef(BaseValidatorModel):
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


class RecommendationTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    text: Optional[str] = None


class ResetEncryptionKeyRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    scanType: ScanTypeType


class ResourceMapFilterTypeDef(BaseValidatorModel):
    comparison: Literal["EQUALS"]
    key: str
    value: Optional[str] = None


class ResourceStringFilterTypeDef(BaseValidatorModel):
    comparison: ResourceStringComparisonType
    value: str


class SearchVulnerabilitiesFilterCriteriaTypeDef(BaseValidatorModel):
    vulnerabilityIds: Sequence[str]


class SendCisSessionHealthRequestTypeDef(BaseValidatorModel):
    scanJobId: str
    sessionToken: str


class StartCisSessionMessageTypeDef(BaseValidatorModel):
    sessionToken: str


class StopCisMessageProgressTypeDef(BaseValidatorModel):
    errorChecks: Optional[int] = None
    failedChecks: Optional[int] = None
    informationalChecks: Optional[int] = None
    notApplicableChecks: Optional[int] = None
    notEvaluatedChecks: Optional[int] = None
    successfulChecks: Optional[int] = None
    totalChecks: Optional[int] = None
    unknownChecks: Optional[int] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateCisTargetsTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    targetResourceTags: Optional[Mapping[str, Sequence[str]]] = None


class UpdateEc2DeepInspectionConfigurationRequestTypeDef(BaseValidatorModel):
    activateDeepInspection: Optional[bool] = None
    packagePaths: Optional[Sequence[str]] = None


class UpdateEncryptionKeyRequestTypeDef(BaseValidatorModel):
    kmsKeyId: str
    resourceType: ResourceTypeType
    scanType: ScanTypeType


class UpdateOrgEc2DeepInspectionConfigurationRequestTypeDef(BaseValidatorModel):
    orgPackagePaths: Sequence[str]


class SeverityCountsTypeDef(BaseValidatorModel):
    pass


class AccountAggregationResponseTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    exploitAvailableCount: Optional[int] = None
    fixAvailableCount: Optional[int] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class AmiAggregationResponseTypeDef(BaseValidatorModel):
    ami: str
    accountId: Optional[str] = None
    affectedInstances: Optional[int] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class AwsEcrContainerAggregationResponseTypeDef(BaseValidatorModel):
    resourceId: str
    accountId: Optional[str] = None
    architecture: Optional[str] = None
    imageSha: Optional[str] = None
    imageTags: Optional[List[str]] = None
    repository: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class Ec2InstanceAggregationResponseTypeDef(BaseValidatorModel):
    instanceId: str
    accountId: Optional[str] = None
    ami: Optional[str] = None
    instanceTags: Optional[Dict[str, str]] = None
    networkFindings: Optional[int] = None
    operatingSystem: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class FindingTypeAggregationResponseTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    exploitAvailableCount: Optional[int] = None
    fixAvailableCount: Optional[int] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class ImageLayerAggregationResponseTypeDef(BaseValidatorModel):
    accountId: str
    layerHash: str
    repository: str
    resourceId: str
    severityCounts: Optional[SeverityCountsTypeDef] = None


class LambdaFunctionAggregationResponseTypeDef(BaseValidatorModel):
    resourceId: str
    accountId: Optional[str] = None
    functionName: Optional[str] = None
    lambdaTags: Optional[Dict[str, str]] = None
    lastModifiedAt: Optional[datetime] = None
    runtime: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class LambdaLayerAggregationResponseTypeDef(BaseValidatorModel):
    accountId: str
    functionName: str
    layerArn: str
    resourceId: str
    severityCounts: Optional[SeverityCountsTypeDef] = None


class PackageAggregationResponseTypeDef(BaseValidatorModel):
    packageName: str
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class RepositoryAggregationResponseTypeDef(BaseValidatorModel):
    repository: str
    accountId: Optional[str] = None
    affectedImages: Optional[int] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class TitleAggregationResponseTypeDef(BaseValidatorModel):
    title: str
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None
    vulnerabilityId: Optional[str] = None


class ResourceStatusTypeDef(BaseValidatorModel):
    pass


class AccountTypeDef(BaseValidatorModel):
    accountId: str
    resourceStatus: ResourceStatusTypeDef
    status: StatusType


class FailedAccountTypeDef(BaseValidatorModel):
    accountId: str
    errorCode: ErrorCodeType
    errorMessage: str
    resourceStatus: Optional[ResourceStatusTypeDef] = None
    status: Optional[StatusType] = None


class AmiAggregationTypeDef(BaseValidatorModel):
    amis: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[AmiSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class AwsEcrContainerAggregationTypeDef(BaseValidatorModel):
    architectures: Optional[Sequence[StringFilterTypeDef]] = None
    imageShas: Optional[Sequence[StringFilterTypeDef]] = None
    imageTags: Optional[Sequence[StringFilterTypeDef]] = None
    repositories: Optional[Sequence[StringFilterTypeDef]] = None
    resourceIds: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[AwsEcrContainerSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class ImageLayerAggregationTypeDef(BaseValidatorModel):
    layerHashes: Optional[Sequence[StringFilterTypeDef]] = None
    repositories: Optional[Sequence[StringFilterTypeDef]] = None
    resourceIds: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[ImageLayerSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class LambdaLayerAggregationTypeDef(BaseValidatorModel):
    functionNames: Optional[Sequence[StringFilterTypeDef]] = None
    layerArns: Optional[Sequence[StringFilterTypeDef]] = None
    resourceIds: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[LambdaLayerSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class PackageAggregationTypeDef(BaseValidatorModel):
    packageNames: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[PackageSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class RepositoryAggregationTypeDef(BaseValidatorModel):
    repositories: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[RepositorySortByType] = None
    sortOrder: Optional[SortOrderType] = None


class TitleAggregationTypeDef(BaseValidatorModel):
    findingType: Optional[AggregationFindingTypeType] = None
    resourceType: Optional[AggregationResourceTypeType] = None
    sortBy: Optional[TitleSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    titles: Optional[Sequence[StringFilterTypeDef]] = None
    vulnerabilityIds: Optional[Sequence[StringFilterTypeDef]] = None


class AssociateMemberResponseTypeDef(BaseValidatorModel):
    accountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CancelFindingsReportResponseTypeDef(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CancelSbomExportResponseTypeDef(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCisScanConfigurationResponseTypeDef(BaseValidatorModel):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFilterResponseTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFindingsReportResponseTypeDef(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSbomExportResponseTypeDef(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCisScanConfigurationResponseTypeDef(BaseValidatorModel):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFilterResponseTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisableDelegatedAdminAccountResponseTypeDef(BaseValidatorModel):
    delegatedAdminAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateMemberResponseTypeDef(BaseValidatorModel):
    accountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EnableDelegatedAdminAccountResponseTypeDef(BaseValidatorModel):
    delegatedAdminAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCisScanReportResponseTypeDef(BaseValidatorModel):
    status: CisReportStatusType
    url: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetEc2DeepInspectionConfigurationResponseTypeDef(BaseValidatorModel):
    errorMessage: str
    orgPackagePaths: List[str]
    packagePaths: List[str]
    status: Ec2DeepInspectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetEncryptionKeyResponseTypeDef(BaseValidatorModel):
    kmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCisScanConfigurationResponseTypeDef(BaseValidatorModel):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEc2DeepInspectionConfigurationResponseTypeDef(BaseValidatorModel):
    errorMessage: str
    orgPackagePaths: List[str]
    packagePaths: List[str]
    status: Ec2DeepInspectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFilterResponseTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AutoEnableTypeDef(BaseValidatorModel):
    pass


class DescribeOrganizationConfigurationResponseTypeDef(BaseValidatorModel):
    autoEnable: AutoEnableTypeDef
    maxAccountLimitReached: bool
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateOrganizationConfigurationRequestTypeDef(BaseValidatorModel):
    autoEnable: AutoEnableTypeDef


class UpdateOrganizationConfigurationResponseTypeDef(BaseValidatorModel):
    autoEnable: AutoEnableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AwsLambdaFunctionDetailsTypeDef(BaseValidatorModel):
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


class BatchGetMemberEc2DeepInspectionStatusResponseTypeDef(BaseValidatorModel):
    accountIds: List[MemberAccountEc2DeepInspectionStatusStateTypeDef]
    failedAccountIds: List[FailedMemberAccountEc2DeepInspectionStatusStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef(BaseValidatorModel):
    accountIds: List[MemberAccountEc2DeepInspectionStatusStateTypeDef]
    failedAccountIds: List[FailedMemberAccountEc2DeepInspectionStatusStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdateMemberEc2DeepInspectionStatusRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[MemberAccountEc2DeepInspectionStatusTypeDef]


class BlobTypeDef(BaseValidatorModel):
    pass


class CisSessionMessageTypeDef(BaseValidatorModel):
    cisRuleDetails: BlobTypeDef
    ruleId: str
    status: CisRuleStatusType


class CisCheckAggregationTypeDef(BaseValidatorModel):
    scanArn: str
    accountId: Optional[str] = None
    checkDescription: Optional[str] = None
    checkId: Optional[str] = None
    level: Optional[CisSecurityLevelType] = None
    platform: Optional[str] = None
    statusCounts: Optional[StatusCountsTypeDef] = None
    title: Optional[str] = None


class CisTargetResourceAggregationTypeDef(BaseValidatorModel):
    scanArn: str
    accountId: Optional[str] = None
    platform: Optional[str] = None
    statusCounts: Optional[StatusCountsTypeDef] = None
    targetResourceId: Optional[str] = None
    targetResourceTags: Optional[Dict[str, List[str]]] = None
    targetStatus: Optional[CisTargetStatusType] = None
    targetStatusReason: Optional[CisTargetStatusReasonType] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class CisDateFilterTypeDef(BaseValidatorModel):
    earliestScanStartTime: Optional[TimestampTypeDef] = None
    latestScanStartTime: Optional[TimestampTypeDef] = None


class CoverageDateFilterTypeDef(BaseValidatorModel):
    endInclusive: Optional[TimestampTypeDef] = None
    startInclusive: Optional[TimestampTypeDef] = None


class DateFilterTypeDef(BaseValidatorModel):
    endInclusive: Optional[TimestampTypeDef] = None
    startInclusive: Optional[TimestampTypeDef] = None


class CisScanTypeDef(BaseValidatorModel):
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


class CisScanResultDetailsFilterCriteriaTypeDef(BaseValidatorModel):
    checkIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    findingArnFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    findingStatusFilters: Optional[Sequence[CisFindingStatusFilterTypeDef]] = None
    securityLevelFilters: Optional[Sequence[CisSecurityLevelFilterTypeDef]] = None
    titleFilters: Optional[Sequence[CisStringFilterTypeDef]] = None


class CisScanResultsAggregatedByChecksFilterCriteriaTypeDef(BaseValidatorModel):
    accountIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    checkIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    failedResourcesFilters: Optional[Sequence[CisNumberFilterTypeDef]] = None
    platformFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    securityLevelFilters: Optional[Sequence[CisSecurityLevelFilterTypeDef]] = None
    titleFilters: Optional[Sequence[CisStringFilterTypeDef]] = None


class GetCisScanResultDetailsResponseTypeDef(BaseValidatorModel):
    scanResultDetails: List[CisScanResultDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef(BaseValidatorModel):
    accountIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    checkIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    failedChecksFilters: Optional[Sequence[CisNumberFilterTypeDef]] = None
    platformFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    statusFilters: Optional[Sequence[CisResultStatusFilterTypeDef]] = None
    targetResourceIdFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    targetResourceTagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    targetStatusFilters: Optional[Sequence[CisTargetStatusFilterTypeDef]] = None
    targetStatusReasonFilters: Optional[Sequence[CisTargetStatusReasonFilterTypeDef]] = None


class ListCisScanConfigurationsFilterCriteriaTypeDef(BaseValidatorModel):
    scanConfigurationArnFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    scanNameFilters: Optional[Sequence[CisStringFilterTypeDef]] = None
    targetResourceTagFilters: Optional[Sequence[TagFilterTypeDef]] = None


class CodeVulnerabilityDetailsTypeDef(BaseValidatorModel):
    cwes: List[str]
    detectorId: str
    detectorName: str
    filePath: CodeFilePathTypeDef
    detectorTags: Optional[List[str]] = None
    referenceUrls: Optional[List[str]] = None
    ruleId: Optional[str] = None
    sourceLambdaLayerArn: Optional[str] = None


class CodeSnippetResultTypeDef(BaseValidatorModel):
    codeSnippet: Optional[List[CodeLineTypeDef]] = None
    endLine: Optional[int] = None
    findingArn: Optional[str] = None
    startLine: Optional[int] = None
    suggestedFixes: Optional[List[SuggestedFixTypeDef]] = None


class ListCoverageStatisticsResponseTypeDef(BaseValidatorModel):
    countsByGroup: List[CountsTypeDef]
    totalCounts: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CvssScoreDetailsTypeDef(BaseValidatorModel):
    score: float
    scoreSource: str
    scoringVector: str
    version: str
    adjustments: Optional[List[CvssScoreAdjustmentTypeDef]] = None
    cvssSource: Optional[str] = None


class DailyScheduleTypeDef(BaseValidatorModel):
    startTime: TimeTypeDef


class MonthlyScheduleTypeDef(BaseValidatorModel):
    day: DayType
    startTime: TimeTypeDef


class WeeklyScheduleOutputTypeDef(BaseValidatorModel):
    days: List[DayType]
    startTime: TimeTypeDef


class WeeklyScheduleTypeDef(BaseValidatorModel):
    days: Sequence[DayType]
    startTime: TimeTypeDef


class ListDelegatedAdminAccountsResponseTypeDef(BaseValidatorModel):
    delegatedAdminAccounts: List[DelegatedAdminAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetDelegatedAdminAccountResponseTypeDef(BaseValidatorModel):
    delegatedAdmin: DelegatedAdminTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class Ec2ConfigurationStateTypeDef(BaseValidatorModel):
    scanModeState: Optional[Ec2ScanModeStateTypeDef] = None


class Ec2InstanceAggregationTypeDef(BaseValidatorModel):
    amis: Optional[Sequence[StringFilterTypeDef]] = None
    instanceIds: Optional[Sequence[StringFilterTypeDef]] = None
    instanceTags: Optional[Sequence[MapFilterTypeDef]] = None
    operatingSystems: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[Ec2InstanceSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class LambdaFunctionAggregationTypeDef(BaseValidatorModel):
    functionNames: Optional[Sequence[StringFilterTypeDef]] = None
    functionTags: Optional[Sequence[MapFilterTypeDef]] = None
    resourceIds: Optional[Sequence[StringFilterTypeDef]] = None
    runtimes: Optional[Sequence[StringFilterTypeDef]] = None
    sortBy: Optional[LambdaFunctionSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class EcrConfigurationStateTypeDef(BaseValidatorModel):
    rescanDurationState: Optional[EcrRescanDurationStateTypeDef] = None


class UpdateConfigurationRequestTypeDef(BaseValidatorModel):
    ec2Configuration: Optional[Ec2ConfigurationTypeDef] = None
    ecrConfiguration: Optional[EcrConfigurationTypeDef] = None


class FindingDetailTypeDef(BaseValidatorModel):
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


class PackageFilterTypeDef(BaseValidatorModel):
    architecture: Optional[StringFilterTypeDef] = None
    epoch: Optional[NumberFilterTypeDef] = None
    filePath: Optional[StringFilterTypeDef] = None
    name: Optional[StringFilterTypeDef] = None
    release: Optional[StringFilterTypeDef] = None
    sourceLambdaLayerArn: Optional[StringFilterTypeDef] = None
    sourceLayerHash: Optional[StringFilterTypeDef] = None
    version: Optional[StringFilterTypeDef] = None


class FreeTrialInfoTypeDef(BaseValidatorModel):
    pass


class FreeTrialAccountInfoTypeDef(BaseValidatorModel):
    accountId: str
    freeTrialInfo: List[FreeTrialInfoTypeDef]


class ListAccountPermissionsRequestPaginateTypeDef(BaseValidatorModel):
    service: Optional[ServiceType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDelegatedAdminAccountsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFiltersRequestPaginateTypeDef(BaseValidatorModel):
    action: Optional[FilterActionType] = None
    arns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMembersRequestPaginateTypeDef(BaseValidatorModel):
    onlyAssociated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsageTotalsRequestPaginateTypeDef(BaseValidatorModel):
    accountIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetMemberResponseTypeDef(BaseValidatorModel):
    member: MemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListMembersResponseTypeDef(BaseValidatorModel):
    members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ResourceScanMetadataTypeDef(BaseValidatorModel):
    ec2: Optional[Ec2MetadataTypeDef] = None
    ecrImage: Optional[EcrContainerImageMetadataTypeDef] = None
    ecrRepository: Optional[EcrRepositoryMetadataTypeDef] = None
    lambdaFunction: Optional[LambdaFunctionMetadataTypeDef] = None


class ListAccountPermissionsResponseTypeDef(BaseValidatorModel):
    permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class NetworkPathTypeDef(BaseValidatorModel):
    steps: Optional[List[StepTypeDef]] = None


class PackageVulnerabilityDetailsTypeDef(BaseValidatorModel):
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


class RemediationTypeDef(BaseValidatorModel):
    recommendation: Optional[RecommendationTypeDef] = None


class ResourceFilterCriteriaOutputTypeDef(BaseValidatorModel):
    accountId: Optional[List[ResourceStringFilterTypeDef]] = None
    ec2InstanceTags: Optional[List[ResourceMapFilterTypeDef]] = None
    ecrImageTags: Optional[List[ResourceStringFilterTypeDef]] = None
    ecrRepositoryName: Optional[List[ResourceStringFilterTypeDef]] = None
    lambdaFunctionName: Optional[List[ResourceStringFilterTypeDef]] = None
    lambdaFunctionTags: Optional[List[ResourceMapFilterTypeDef]] = None
    resourceId: Optional[List[ResourceStringFilterTypeDef]] = None
    resourceType: Optional[List[ResourceStringFilterTypeDef]] = None


class ResourceFilterCriteriaTypeDef(BaseValidatorModel):
    accountId: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    ec2InstanceTags: Optional[Sequence[ResourceMapFilterTypeDef]] = None
    ecrImageTags: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    ecrRepositoryName: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    lambdaFunctionName: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    lambdaFunctionTags: Optional[Sequence[ResourceMapFilterTypeDef]] = None
    resourceId: Optional[Sequence[ResourceStringFilterTypeDef]] = None
    resourceType: Optional[Sequence[ResourceStringFilterTypeDef]] = None


class SearchVulnerabilitiesRequestPaginateTypeDef(BaseValidatorModel):
    filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchVulnerabilitiesRequestTypeDef(BaseValidatorModel):
    filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef
    nextToken: Optional[str] = None


class StartCisSessionRequestTypeDef(BaseValidatorModel):
    message: StartCisSessionMessageTypeDef
    scanJobId: str


class StopCisSessionMessageTypeDef(BaseValidatorModel):
    progress: StopCisMessageProgressTypeDef
    status: StopCisSessionStatusType
    benchmarkProfile: Optional[str] = None
    benchmarkVersion: Optional[str] = None
    computePlatform: Optional[ComputePlatformTypeDef] = None
    reason: Optional[str] = None


class UsageTypeDef(BaseValidatorModel):
    pass


class UsageTotalTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    usage: Optional[List[UsageTypeDef]] = None


class AggregationResponseTypeDef(BaseValidatorModel):
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


class ResourceStateTypeDef(BaseValidatorModel):
    pass


class AccountStateTypeDef(BaseValidatorModel):
    accountId: str
    resourceState: ResourceStateTypeDef
    state: StateTypeDef


class DisableResponseTypeDef(BaseValidatorModel):
    accounts: List[AccountTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EnableResponseTypeDef(BaseValidatorModel):
    accounts: List[AccountTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AwsEc2InstanceDetailsTypeDef(BaseValidatorModel):
    pass


class ResourceDetailsTypeDef(BaseValidatorModel):
    awsEc2Instance: Optional[AwsEc2InstanceDetailsTypeDef] = None
    awsEcrContainerImage: Optional[AwsEcrContainerImageDetailsTypeDef] = None
    awsLambdaFunction: Optional[AwsLambdaFunctionDetailsTypeDef] = None


class SendCisSessionTelemetryRequestTypeDef(BaseValidatorModel):
    messages: Sequence[CisSessionMessageTypeDef]
    scanJobId: str
    sessionToken: str


class ListCisScanResultsAggregatedByChecksResponseTypeDef(BaseValidatorModel):
    checkAggregations: List[CisCheckAggregationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCisScanResultsAggregatedByTargetResourceResponseTypeDef(BaseValidatorModel):
    targetResourceAggregations: List[CisTargetResourceAggregationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCisScansFilterCriteriaTypeDef(BaseValidatorModel):
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


class CoverageFilterCriteriaTypeDef(BaseValidatorModel):
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


class ListCisScansResponseTypeDef(BaseValidatorModel):
    scans: List[CisScanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetCisScanResultDetailsRequestPaginateTypeDef(BaseValidatorModel):
    accountId: str
    scanArn: str
    targetResourceId: str
    filterCriteria: Optional[CisScanResultDetailsFilterCriteriaTypeDef] = None
    sortBy: Optional[CisScanResultDetailsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetCisScanResultDetailsRequestTypeDef(BaseValidatorModel):
    accountId: str
    scanArn: str
    targetResourceId: str
    filterCriteria: Optional[CisScanResultDetailsFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanResultDetailsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class ListCisScanResultsAggregatedByChecksRequestPaginateTypeDef(BaseValidatorModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef] = None
    sortBy: Optional[CisScanResultsAggregatedByChecksSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCisScanResultsAggregatedByChecksRequestTypeDef(BaseValidatorModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanResultsAggregatedByChecksSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class ListCisScanResultsAggregatedByTargetResourceRequestPaginateTypeDef(BaseValidatorModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef] = None
    sortBy: Optional[CisScanResultsAggregatedByTargetResourceSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCisScanResultsAggregatedByTargetResourceRequestTypeDef(BaseValidatorModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanResultsAggregatedByTargetResourceSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class ListCisScanConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    filterCriteria: Optional[ListCisScanConfigurationsFilterCriteriaTypeDef] = None
    sortBy: Optional[CisScanConfigurationsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCisScanConfigurationsRequestTypeDef(BaseValidatorModel):
    filterCriteria: Optional[ListCisScanConfigurationsFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanConfigurationsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class BatchGetCodeSnippetResponseTypeDef(BaseValidatorModel):
    codeSnippetResults: List[CodeSnippetResultTypeDef]
    errors: List[CodeSnippetErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class InspectorScoreDetailsTypeDef(BaseValidatorModel):
    adjustedCvss: Optional[CvssScoreDetailsTypeDef] = None


class ScheduleOutputTypeDef(BaseValidatorModel):
    daily: Optional[DailyScheduleTypeDef] = None
    monthly: Optional[MonthlyScheduleTypeDef] = None
    oneTime: Optional[Dict[str, Any]] = None
    weekly: Optional[WeeklyScheduleOutputTypeDef] = None


class ScheduleTypeDef(BaseValidatorModel):
    daily: Optional[DailyScheduleTypeDef] = None
    monthly: Optional[MonthlyScheduleTypeDef] = None
    oneTime: Optional[Mapping[str, Any]] = None
    weekly: Optional[WeeklyScheduleTypeDef] = None


class AggregationRequestTypeDef(BaseValidatorModel):
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


class GetConfigurationResponseTypeDef(BaseValidatorModel):
    ec2Configuration: Ec2ConfigurationStateTypeDef
    ecrConfiguration: EcrConfigurationStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetFindingDetailsResponseTypeDef(BaseValidatorModel):
    errors: List[FindingDetailsErrorTypeDef]
    findingDetails: List[FindingDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class VulnerabilityTypeDef(BaseValidatorModel):
    pass


class SearchVulnerabilitiesResponseTypeDef(BaseValidatorModel):
    vulnerabilities: List[VulnerabilityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FilterCriteriaOutputTypeDef(BaseValidatorModel):
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


class FilterCriteriaTypeDef(BaseValidatorModel):
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


class BatchGetFreeTrialInfoResponseTypeDef(BaseValidatorModel):
    accounts: List[FreeTrialAccountInfoTypeDef]
    failedAccounts: List[FreeTrialInfoErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CoveredResourceTypeDef(BaseValidatorModel):
    accountId: str
    resourceId: str
    resourceType: CoverageResourceTypeType
    scanType: ScanTypeType
    lastScannedAt: Optional[datetime] = None
    resourceMetadata: Optional[ResourceScanMetadataTypeDef] = None
    scanMode: Optional[ScanModeType] = None
    scanStatus: Optional[ScanStatusTypeDef] = None


class NetworkReachabilityDetailsTypeDef(BaseValidatorModel):
    networkPath: NetworkPathTypeDef
    openPortRange: PortRangeTypeDef
    protocol: NetworkProtocolType


class StopCisSessionRequestTypeDef(BaseValidatorModel):
    message: StopCisSessionMessageTypeDef
    scanJobId: str
    sessionToken: str


class ListUsageTotalsResponseTypeDef(BaseValidatorModel):
    totals: List[UsageTotalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListFindingAggregationsResponseTypeDef(BaseValidatorModel):
    aggregationType: AggregationTypeType
    responses: List[AggregationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchGetAccountStatusResponseTypeDef(BaseValidatorModel):
    accounts: List[AccountStateTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListCisScansRequestPaginateTypeDef(BaseValidatorModel):
    detailLevel: Optional[ListCisScansDetailLevelType] = None
    filterCriteria: Optional[ListCisScansFilterCriteriaTypeDef] = None
    sortBy: Optional[ListCisScansSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCisScansRequestTypeDef(BaseValidatorModel):
    detailLevel: Optional[ListCisScansDetailLevelType] = None
    filterCriteria: Optional[ListCisScansFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[ListCisScansSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class ListCoverageRequestPaginateTypeDef(BaseValidatorModel):
    filterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCoverageRequestTypeDef(BaseValidatorModel):
    filterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListCoverageStatisticsRequestPaginateTypeDef(BaseValidatorModel):
    filterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    groupBy: Optional[GroupKeyType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCoverageStatisticsRequestTypeDef(BaseValidatorModel):
    filterCriteria: Optional[CoverageFilterCriteriaTypeDef] = None
    groupBy: Optional[GroupKeyType] = None
    nextToken: Optional[str] = None


class CisScanConfigurationTypeDef(BaseValidatorModel):
    scanConfigurationArn: str
    ownerId: Optional[str] = None
    scanName: Optional[str] = None
    schedule: Optional[ScheduleOutputTypeDef] = None
    securityLevel: Optional[CisSecurityLevelType] = None
    tags: Optional[Dict[str, str]] = None
    targets: Optional[CisTargetsTypeDef] = None


class ListFindingAggregationsRequestPaginateTypeDef(BaseValidatorModel):
    aggregationType: AggregationTypeType
    accountIds: Optional[Sequence[StringFilterTypeDef]] = None
    aggregationRequest: Optional[AggregationRequestTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFindingAggregationsRequestTypeDef(BaseValidatorModel):
    aggregationType: AggregationTypeType
    accountIds: Optional[Sequence[StringFilterTypeDef]] = None
    aggregationRequest: Optional[AggregationRequestTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
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


class GetFindingsReportStatusResponseTypeDef(BaseValidatorModel):
    destination: DestinationTypeDef
    errorCode: ReportingErrorCodeType
    errorMessage: str
    filterCriteria: FilterCriteriaOutputTypeDef
    reportId: str
    status: ExternalReportStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListCoverageResponseTypeDef(BaseValidatorModel):
    coveredResources: List[CoveredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ResourceFilterCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class CreateSbomExportRequestTypeDef(BaseValidatorModel):
    reportFormat: SbomReportFormatType
    s3Destination: DestinationTypeDef
    resourceFilterCriteria: Optional[ResourceFilterCriteriaUnionTypeDef] = None


class ListCisScanConfigurationsResponseTypeDef(BaseValidatorModel):
    scanConfigurations: List[CisScanConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ScheduleUnionTypeDef(BaseValidatorModel):
    pass


class CreateCisScanConfigurationRequestTypeDef(BaseValidatorModel):
    scanName: str
    schedule: ScheduleUnionTypeDef
    securityLevel: CisSecurityLevelType
    targets: CreateCisTargetsTypeDef
    tags: Optional[Mapping[str, str]] = None


class UpdateCisScanConfigurationRequestTypeDef(BaseValidatorModel):
    scanConfigurationArn: str
    scanName: Optional[str] = None
    schedule: Optional[ScheduleUnionTypeDef] = None
    securityLevel: Optional[CisSecurityLevelType] = None
    targets: Optional[UpdateCisTargetsTypeDef] = None


class ListFiltersResponseTypeDef(BaseValidatorModel):
    filters: List[FilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FilterCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class CreateFilterRequestTypeDef(BaseValidatorModel):
    action: FilterActionType
    filterCriteria: FilterCriteriaUnionTypeDef
    name: str
    description: Optional[str] = None
    reason: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateFindingsReportRequestTypeDef(BaseValidatorModel):
    reportFormat: ReportFormatType
    s3Destination: DestinationTypeDef
    filterCriteria: Optional[FilterCriteriaUnionTypeDef] = None


class ListFindingsRequestPaginateTypeDef(BaseValidatorModel):
    filterCriteria: Optional[FilterCriteriaUnionTypeDef] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFindingsRequestTypeDef(BaseValidatorModel):
    filterCriteria: Optional[FilterCriteriaUnionTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SortCriteriaTypeDef] = None


class UpdateFilterRequestTypeDef(BaseValidatorModel):
    filterArn: str
    action: Optional[FilterActionType] = None
    description: Optional[str] = None
    filterCriteria: Optional[FilterCriteriaUnionTypeDef] = None
    name: Optional[str] = None
    reason: Optional[str] = None


class FindingTypeDef(BaseValidatorModel):
    pass


class ListFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None



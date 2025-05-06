from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.inspector2.inspector2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class SeverityCounts(BaseValidatorModel):
    all: Optional[int] = None
    critical: Optional[int] = None
    high: Optional[int] = None
    medium: Optional[int] = None


class AccountAggregation(BaseValidatorModel):
    findingType: Optional[AggregationFindingTypeType] = None
    resourceType: Optional[AggregationResourceTypeType] = None
    sortBy: Optional[AccountSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class State(BaseValidatorModel):
    errorCode: ErrorCodeType
    errorMessage: str
    status: StatusType


class ResourceStatus(BaseValidatorModel):
    ec2: StatusType
    ecr: StatusType
    lambda_:Optional[StatusType] = None
    lambdaCode: Optional[StatusType] = None


class FindingTypeAggregation(BaseValidatorModel):
    findingType: Optional[AggregationFindingTypeType] = None
    resourceType: Optional[AggregationResourceTypeType] = None
    sortBy: Optional[FindingTypeSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class StringFilter(BaseValidatorModel):
    comparison: StringComparisonType
    value: str


class AssociateMemberRequest(BaseValidatorModel):
    accountId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AtigData(BaseValidatorModel):
    firstSeen: Optional[datetime] = None
    lastSeen: Optional[datetime] = None
    targets: Optional[List[str]] = None
    ttps: Optional[List[str]] = None


class AutoEnable(BaseValidatorModel):
    ec2: bool
    ecr: bool
    lambda_:Optional[bool] = None
    lambdaCode: Optional[bool] = None


class AwsEc2InstanceDetails(BaseValidatorModel):
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


class AwsEcrContainerImageDetails(BaseValidatorModel):
    imageHash: str
    registry: str
    repositoryName: str
    architecture: Optional[str] = None
    author: Optional[str] = None
    imageTags: Optional[List[str]] = None
    platform: Optional[str] = None
    pushedAt: Optional[datetime] = None


class LambdaVpcConfig(BaseValidatorModel):
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None


class BatchGetAccountStatusRequest(BaseValidatorModel):
    accountIds: Optional[List[str]] = None


class BatchGetCodeSnippetRequest(BaseValidatorModel):
    findingArns: List[str]


class CodeSnippetError(BaseValidatorModel):
    errorCode: CodeSnippetErrorCodeType
    errorMessage: str
    findingArn: str


class BatchGetFindingDetailsRequest(BaseValidatorModel):
    findingArns: List[str]


class FindingDetailsError(BaseValidatorModel):
    errorCode: FindingDetailsErrorCodeType
    errorMessage: str
    findingArn: str


class BatchGetFreeTrialInfoRequest(BaseValidatorModel):
    accountIds: List[str]


class FreeTrialInfoError(BaseValidatorModel):
    accountId: str
    code: FreeTrialInfoErrorCodeType
    message: str


class BatchGetMemberEc2DeepInspectionStatusRequest(BaseValidatorModel):
    accountIds: Optional[List[str]] = None


class FailedMemberAccountEc2DeepInspectionStatusState(BaseValidatorModel):
    accountId: str
    ec2ScanStatus: Optional[StatusType] = None
    errorMessage: Optional[str] = None


class MemberAccountEc2DeepInspectionStatusState(BaseValidatorModel):
    accountId: str
    errorMessage: Optional[str] = None
    status: Optional[Ec2DeepInspectionStatusType] = None


class MemberAccountEc2DeepInspectionStatus(BaseValidatorModel):
    accountId: str
    activateDeepInspection: bool

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelFindingsReportRequest(BaseValidatorModel):
    reportId: str


class CancelSbomExportRequest(BaseValidatorModel):
    reportId: str


class StatusCounts(BaseValidatorModel):
    failed: Optional[int] = None
    passed: Optional[int] = None
    skipped: Optional[int] = None

Timestamp = Union[datetime, str]


class CisFindingStatusFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    value: CisFindingStatusType


class CisNumberFilter(BaseValidatorModel):
    lowerInclusive: Optional[int] = None
    upperInclusive: Optional[int] = None


class CisResultStatusFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    value: CisResultStatusType


class CisTargets(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    targetResourceTags: Optional[Dict[str, List[str]]] = None


class CisSecurityLevelFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    value: CisSecurityLevelType


class CisStringFilter(BaseValidatorModel):
    comparison: CisStringComparisonType
    value: str


class CisScanResultDetails(BaseValidatorModel):
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


class CisTargetStatusFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    value: CisTargetStatusType


class CisTargetStatusReasonFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    value: CisTargetStatusReasonType


class TagFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    key: str
    value: str


class CisScanStatusFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    value: CisScanStatusType


class CisaData(BaseValidatorModel):
    action: Optional[str] = None
    dateAdded: Optional[datetime] = None
    dateDue: Optional[datetime] = None


class CodeFilePath(BaseValidatorModel):
    endLine: int
    fileName: str
    filePath: str
    startLine: int


class CodeLine(BaseValidatorModel):
    content: str
    lineNumber: int


class SuggestedFix(BaseValidatorModel):
    code: Optional[str] = None
    description: Optional[str] = None


class ComputePlatform(BaseValidatorModel):
    product: Optional[str] = None
    vendor: Optional[str] = None
    version: Optional[str] = None


class Counts(BaseValidatorModel):
    count: Optional[int] = None
    groupKey: Optional[GroupKeyType] = None


class CoverageMapFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    key: str
    value: Optional[str] = None


class CoverageStringFilter(BaseValidatorModel):
    comparison: CoverageStringComparisonType
    value: str


class ScanStatus(BaseValidatorModel):
    reason: ScanStatusReasonType
    statusCode: ScanStatusCodeType


class CreateCisTargets(BaseValidatorModel):
    accountIds: List[str]
    targetResourceTags: Dict[str, List[str]]


class Destination(BaseValidatorModel):
    bucketName: str
    kmsKeyArn: str
    keyPrefix: Optional[str] = None


class Cvss2(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None


class Cvss3(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None


class CvssScoreAdjustment(BaseValidatorModel):
    metric: str
    reason: str


class CvssScore(BaseValidatorModel):
    baseScore: float
    scoringVector: str
    source: str
    version: str


class Time(BaseValidatorModel):
    timeOfDay: str
    timezone: str


class DateFilterOutput(BaseValidatorModel):
    endInclusive: Optional[datetime] = None
    startInclusive: Optional[datetime] = None


class DelegatedAdminAccount(BaseValidatorModel):
    accountId: Optional[str] = None
    status: Optional[DelegatedAdminStatusType] = None


class DelegatedAdmin(BaseValidatorModel):
    accountId: Optional[str] = None
    relationshipStatus: Optional[RelationshipStatusType] = None


class DeleteCisScanConfigurationRequest(BaseValidatorModel):
    scanConfigurationArn: str


class DeleteFilterRequest(BaseValidatorModel):
    arn: str


class DisableDelegatedAdminAccountRequest(BaseValidatorModel):
    delegatedAdminAccountId: str


class DisableRequest(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    resourceTypes: Optional[List[ResourceScanTypeType]] = None


class DisassociateMemberRequest(BaseValidatorModel):
    accountId: str


class Ec2ScanModeState(BaseValidatorModel):
    scanMode: Optional[Ec2ScanModeType] = None
    scanModeStatus: Optional[Ec2ScanModeStatusType] = None


class Ec2Configuration(BaseValidatorModel):
    scanMode: Ec2ScanModeType


class MapFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    key: str
    value: Optional[str] = None


class Ec2Metadata(BaseValidatorModel):
    amiId: Optional[str] = None
    platform: Optional[Ec2PlatformType] = None
    tags: Optional[Dict[str, str]] = None


class EcrRescanDurationState(BaseValidatorModel):
    pullDateRescanDuration: Optional[EcrPullDateRescanDurationType] = None
    rescanDuration: Optional[EcrRescanDurationType] = None
    status: Optional[EcrRescanDurationStatusType] = None
    updatedAt: Optional[datetime] = None


class EcrConfiguration(BaseValidatorModel):
    rescanDuration: EcrRescanDurationType
    pullDateRescanDuration: Optional[EcrPullDateRescanDurationType] = None


class EcrContainerImageMetadata(BaseValidatorModel):
    imagePulledAt: Optional[datetime] = None
    tags: Optional[List[str]] = None


class EcrRepositoryMetadata(BaseValidatorModel):
    name: Optional[str] = None
    scanFrequency: Optional[EcrScanFrequencyType] = None


class EnableDelegatedAdminAccountRequest(BaseValidatorModel):
    delegatedAdminAccountId: str
    clientToken: Optional[str] = None


class EnableRequest(BaseValidatorModel):
    resourceTypes: List[ResourceScanTypeType]
    accountIds: Optional[List[str]] = None
    clientToken: Optional[str] = None


class EpssDetails(BaseValidatorModel):
    score: Optional[float] = None


class Epss(BaseValidatorModel):
    score: Optional[float] = None


class Evidence(BaseValidatorModel):
    evidenceDetail: Optional[str] = None
    evidenceRule: Optional[str] = None
    severity: Optional[str] = None


class ExploitObserved(BaseValidatorModel):
    firstSeen: Optional[datetime] = None
    lastSeen: Optional[datetime] = None


class ExploitabilityDetails(BaseValidatorModel):
    lastKnownExploitAt: Optional[datetime] = None


class NumberFilter(BaseValidatorModel):
    lowerInclusive: Optional[float] = None
    upperInclusive: Optional[float] = None


class PortRangeFilter(BaseValidatorModel):
    beginInclusive: Optional[int] = None
    endInclusive: Optional[int] = None


class FreeTrialInfo(BaseValidatorModel):
    end: datetime
    start: datetime
    status: FreeTrialStatusType
    type: FreeTrialTypeType


class GetCisScanReportRequest(BaseValidatorModel):
    scanArn: str
    reportFormat: Optional[CisReportFormatType] = None
    targetAccounts: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetEncryptionKeyRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    scanType: ScanTypeType


class GetFindingsReportStatusRequest(BaseValidatorModel):
    reportId: Optional[str] = None


class GetMemberRequest(BaseValidatorModel):
    accountId: str


class Member(BaseValidatorModel):
    accountId: Optional[str] = None
    delegatedAdminAccountId: Optional[str] = None
    relationshipStatus: Optional[RelationshipStatusType] = None
    updatedAt: Optional[datetime] = None


class GetSbomExportRequest(BaseValidatorModel):
    reportId: str


class LambdaFunctionMetadata(BaseValidatorModel):
    functionName: Optional[str] = None
    functionTags: Optional[Dict[str, str]] = None
    layers: Optional[List[str]] = None
    runtime: Optional[RuntimeType] = None


class ListAccountPermissionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    service: Optional[ServiceType] = None


class Permission(BaseValidatorModel):
    operation: OperationType
    service: ServiceType


class ListDelegatedAdminAccountsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListFiltersRequest(BaseValidatorModel):
    action: Optional[FilterActionType] = None
    arns: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SortCriteria(BaseValidatorModel):
    field: SortFieldType
    sortOrder: SortOrderType


class ListMembersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    onlyAssociated: Optional[bool] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListUsageTotalsRequest(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class Step(BaseValidatorModel):
    componentId: str
    componentType: str


class PortRange(BaseValidatorModel):
    begin: int
    end: int


class VulnerablePackage(BaseValidatorModel):
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


class Recommendation(BaseValidatorModel):
    Url: Optional[str] = None
    text: Optional[str] = None


class ResetEncryptionKeyRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    scanType: ScanTypeType


class ResourceMapFilter(BaseValidatorModel):
    comparison: Literal['EQUALS']
    key: str
    value: Optional[str] = None


class ResourceStringFilter(BaseValidatorModel):
    comparison: ResourceStringComparisonType
    value: str


class SearchVulnerabilitiesFilterCriteria(BaseValidatorModel):
    vulnerabilityIds: List[str]


class SendCisSessionHealthRequest(BaseValidatorModel):
    scanJobId: str
    sessionToken: str


class StartCisSessionMessage(BaseValidatorModel):
    sessionToken: str


class StopCisMessageProgress(BaseValidatorModel):
    errorChecks: Optional[int] = None
    failedChecks: Optional[int] = None
    informationalChecks: Optional[int] = None
    notApplicableChecks: Optional[int] = None
    notEvaluatedChecks: Optional[int] = None
    successfulChecks: Optional[int] = None
    totalChecks: Optional[int] = None
    unknownChecks: Optional[int] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateCisTargets(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    targetResourceTags: Optional[Dict[str, List[str]]] = None


class UpdateEc2DeepInspectionConfigurationRequest(BaseValidatorModel):
    activateDeepInspection: Optional[bool] = None
    packagePaths: Optional[List[str]] = None


class UpdateEncryptionKeyRequest(BaseValidatorModel):
    kmsKeyId: str
    resourceType: ResourceTypeType
    scanType: ScanTypeType


class UpdateOrgEc2DeepInspectionConfigurationRequest(BaseValidatorModel):
    orgPackagePaths: List[str]


class Usage(BaseValidatorModel):
    currency: Optional[Literal['USD']] = None
    estimatedMonthlyCost: Optional[float] = None
    total: Optional[float] = None
    type: Optional[UsageTypeType] = None


class AccountAggregationResponse(BaseValidatorModel):
    accountId: Optional[str] = None
    exploitAvailableCount: Optional[int] = None
    fixAvailableCount: Optional[int] = None
    severityCounts: Optional[SeverityCounts] = None


class AmiAggregationResponse(BaseValidatorModel):
    ami: str
    accountId: Optional[str] = None
    affectedInstances: Optional[int] = None
    severityCounts: Optional[SeverityCounts] = None


class AwsEcrContainerAggregationResponse(BaseValidatorModel):
    resourceId: str
    accountId: Optional[str] = None
    architecture: Optional[str] = None
    imageSha: Optional[str] = None
    imageTags: Optional[List[str]] = None
    repository: Optional[str] = None
    severityCounts: Optional[SeverityCounts] = None


class Ec2InstanceAggregationResponse(BaseValidatorModel):
    instanceId: str
    accountId: Optional[str] = None
    ami: Optional[str] = None
    instanceTags: Optional[Dict[str, str]] = None
    networkFindings: Optional[int] = None
    operatingSystem: Optional[str] = None
    severityCounts: Optional[SeverityCounts] = None


class FindingTypeAggregationResponse(BaseValidatorModel):
    accountId: Optional[str] = None
    exploitAvailableCount: Optional[int] = None
    fixAvailableCount: Optional[int] = None
    severityCounts: Optional[SeverityCounts] = None


class ImageLayerAggregationResponse(BaseValidatorModel):
    accountId: str
    layerHash: str
    repository: str
    resourceId: str
    severityCounts: Optional[SeverityCounts] = None


class LambdaFunctionAggregationResponse(BaseValidatorModel):
    resourceId: str
    accountId: Optional[str] = None
    functionName: Optional[str] = None
    lambdaTags: Optional[Dict[str, str]] = None
    lastModifiedAt: Optional[datetime] = None
    runtime: Optional[str] = None
    severityCounts: Optional[SeverityCounts] = None


class LambdaLayerAggregationResponse(BaseValidatorModel):
    accountId: str
    functionName: str
    layerArn: str
    resourceId: str
    severityCounts: Optional[SeverityCounts] = None


class PackageAggregationResponse(BaseValidatorModel):
    packageName: str
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCounts] = None


class RepositoryAggregationResponse(BaseValidatorModel):
    repository: str
    accountId: Optional[str] = None
    affectedImages: Optional[int] = None
    severityCounts: Optional[SeverityCounts] = None


class TitleAggregationResponse(BaseValidatorModel):
    title: str
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCounts] = None
    vulnerabilityId: Optional[str] = None


class ResourceState(BaseValidatorModel):
    ec2: State
    ecr: State
    lambda_:Optional[State] = None
    lambdaCode: Optional[State] = None


class Account(BaseValidatorModel):
    accountId: str
    resourceStatus: ResourceStatus
    status: StatusType


class FailedAccount(BaseValidatorModel):
    accountId: str
    errorCode: ErrorCodeType
    errorMessage: str
    resourceStatus: Optional[ResourceStatus] = None
    status: Optional[StatusType] = None


class AmiAggregation(BaseValidatorModel):
    amis: Optional[List[StringFilter]] = None
    sortBy: Optional[AmiSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class AwsEcrContainerAggregation(BaseValidatorModel):
    architectures: Optional[List[StringFilter]] = None
    imageShas: Optional[List[StringFilter]] = None
    imageTags: Optional[List[StringFilter]] = None
    repositories: Optional[List[StringFilter]] = None
    resourceIds: Optional[List[StringFilter]] = None
    sortBy: Optional[AwsEcrContainerSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class ImageLayerAggregation(BaseValidatorModel):
    layerHashes: Optional[List[StringFilter]] = None
    repositories: Optional[List[StringFilter]] = None
    resourceIds: Optional[List[StringFilter]] = None
    sortBy: Optional[ImageLayerSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class LambdaLayerAggregation(BaseValidatorModel):
    functionNames: Optional[List[StringFilter]] = None
    layerArns: Optional[List[StringFilter]] = None
    resourceIds: Optional[List[StringFilter]] = None
    sortBy: Optional[LambdaLayerSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class PackageAggregation(BaseValidatorModel):
    packageNames: Optional[List[StringFilter]] = None
    sortBy: Optional[PackageSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class RepositoryAggregation(BaseValidatorModel):
    repositories: Optional[List[StringFilter]] = None
    sortBy: Optional[RepositorySortByType] = None
    sortOrder: Optional[SortOrderType] = None


class TitleAggregation(BaseValidatorModel):
    findingType: Optional[AggregationFindingTypeType] = None
    resourceType: Optional[AggregationResourceTypeType] = None
    sortBy: Optional[TitleSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    titles: Optional[List[StringFilter]] = None
    vulnerabilityIds: Optional[List[StringFilter]] = None


class AssociateMemberResponse(BaseValidatorModel):
    accountId: str
    ResponseMetadata: ResponseMetadata


class CancelFindingsReportResponse(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


class CancelSbomExportResponse(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


class CreateCisScanConfigurationResponse(BaseValidatorModel):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadata


class CreateFilterResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class CreateFindingsReportResponse(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


class CreateSbomExportResponse(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


class DeleteCisScanConfigurationResponse(BaseValidatorModel):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadata


class DeleteFilterResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class DisableDelegatedAdminAccountResponse(BaseValidatorModel):
    delegatedAdminAccountId: str
    ResponseMetadata: ResponseMetadata


class DisassociateMemberResponse(BaseValidatorModel):
    accountId: str
    ResponseMetadata: ResponseMetadata


class EnableDelegatedAdminAccountResponse(BaseValidatorModel):
    delegatedAdminAccountId: str
    ResponseMetadata: ResponseMetadata


class GetCisScanReportResponse(BaseValidatorModel):
    status: CisReportStatusType
    url: str
    ResponseMetadata: ResponseMetadata


class GetEc2DeepInspectionConfigurationResponse(BaseValidatorModel):
    errorMessage: str
    orgPackagePaths: List[str]
    packagePaths: List[str]
    status: Ec2DeepInspectionStatusType
    ResponseMetadata: ResponseMetadata


class GetEncryptionKeyResponse(BaseValidatorModel):
    kmsKeyId: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateCisScanConfigurationResponse(BaseValidatorModel):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateEc2DeepInspectionConfigurationResponse(BaseValidatorModel):
    errorMessage: str
    orgPackagePaths: List[str]
    packagePaths: List[str]
    status: Ec2DeepInspectionStatusType
    ResponseMetadata: ResponseMetadata


class UpdateFilterResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class DescribeOrganizationConfigurationResponse(BaseValidatorModel):
    autoEnable: AutoEnable
    maxAccountLimitReached: bool
    ResponseMetadata: ResponseMetadata


class UpdateOrganizationConfigurationRequest(BaseValidatorModel):
    autoEnable: AutoEnable


class UpdateOrganizationConfigurationResponse(BaseValidatorModel):
    autoEnable: AutoEnable
    ResponseMetadata: ResponseMetadata


class AwsLambdaFunctionDetails(BaseValidatorModel):
    codeSha256: str
    executionRoleArn: str
    functionName: str
    runtime: RuntimeType
    version: str
    architectures: Optional[List[ArchitectureType]] = None
    lastModifiedAt: Optional[datetime] = None
    layers: Optional[List[str]] = None
    packageType: Optional[PackageTypeType] = None
    vpcConfig: Optional[LambdaVpcConfig] = None


class BatchGetMemberEc2DeepInspectionStatusResponse(BaseValidatorModel):
    accountIds: List[MemberAccountEc2DeepInspectionStatusState]
    failedAccountIds: List[FailedMemberAccountEc2DeepInspectionStatusState]
    ResponseMetadata: ResponseMetadata


class BatchUpdateMemberEc2DeepInspectionStatusResponse(BaseValidatorModel):
    accountIds: List[MemberAccountEc2DeepInspectionStatusState]
    failedAccountIds: List[FailedMemberAccountEc2DeepInspectionStatusState]
    ResponseMetadata: ResponseMetadata


class BatchUpdateMemberEc2DeepInspectionStatusRequest(BaseValidatorModel):
    accountIds: List[MemberAccountEc2DeepInspectionStatus]


class CisSessionMessage(BaseValidatorModel):
    cisRuleDetails: Blob
    ruleId: str
    status: CisRuleStatusType


class CisCheckAggregation(BaseValidatorModel):
    scanArn: str
    accountId: Optional[str] = None
    checkDescription: Optional[str] = None
    checkId: Optional[str] = None
    level: Optional[CisSecurityLevelType] = None
    platform: Optional[str] = None
    statusCounts: Optional[StatusCounts] = None
    title: Optional[str] = None


class CisTargetResourceAggregation(BaseValidatorModel):
    scanArn: str
    accountId: Optional[str] = None
    platform: Optional[str] = None
    statusCounts: Optional[StatusCounts] = None
    targetResourceId: Optional[str] = None
    targetResourceTags: Optional[Dict[str, List[str]]] = None
    targetStatus: Optional[CisTargetStatusType] = None
    targetStatusReason: Optional[CisTargetStatusReasonType] = None


class CisDateFilter(BaseValidatorModel):
    earliestScanStartTime: Optional[Timestamp] = None
    latestScanStartTime: Optional[Timestamp] = None


class CoverageDateFilter(BaseValidatorModel):
    endInclusive: Optional[Timestamp] = None
    startInclusive: Optional[Timestamp] = None


class DateFilter(BaseValidatorModel):
    endInclusive: Optional[Timestamp] = None
    startInclusive: Optional[Timestamp] = None


class CisScan(BaseValidatorModel):
    scanArn: str
    scanConfigurationArn: str
    failedChecks: Optional[int] = None
    scanDate: Optional[datetime] = None
    scanName: Optional[str] = None
    scheduledBy: Optional[str] = None
    securityLevel: Optional[CisSecurityLevelType] = None
    status: Optional[CisScanStatusType] = None
    targets: Optional[CisTargets] = None
    totalChecks: Optional[int] = None


class CisScanResultDetailsFilterCriteria(BaseValidatorModel):
    checkIdFilters: Optional[List[CisStringFilter]] = None
    findingArnFilters: Optional[List[CisStringFilter]] = None
    findingStatusFilters: Optional[List[CisFindingStatusFilter]] = None
    securityLevelFilters: Optional[List[CisSecurityLevelFilter]] = None
    titleFilters: Optional[List[CisStringFilter]] = None


class CisScanResultsAggregatedByChecksFilterCriteria(BaseValidatorModel):
    accountIdFilters: Optional[List[CisStringFilter]] = None
    checkIdFilters: Optional[List[CisStringFilter]] = None
    failedResourcesFilters: Optional[List[CisNumberFilter]] = None
    platformFilters: Optional[List[CisStringFilter]] = None
    securityLevelFilters: Optional[List[CisSecurityLevelFilter]] = None
    titleFilters: Optional[List[CisStringFilter]] = None


class GetCisScanResultDetailsResponse(BaseValidatorModel):
    scanResultDetails: List[CisScanResultDetails]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CisScanResultsAggregatedByTargetResourceFilterCriteria(BaseValidatorModel):
    accountIdFilters: Optional[List[CisStringFilter]] = None
    checkIdFilters: Optional[List[CisStringFilter]] = None
    failedChecksFilters: Optional[List[CisNumberFilter]] = None
    platformFilters: Optional[List[CisStringFilter]] = None
    statusFilters: Optional[List[CisResultStatusFilter]] = None
    targetResourceIdFilters: Optional[List[CisStringFilter]] = None
    targetResourceTagFilters: Optional[List[TagFilter]] = None
    targetStatusFilters: Optional[List[CisTargetStatusFilter]] = None
    targetStatusReasonFilters: Optional[List[CisTargetStatusReasonFilter]] = None


class ListCisScanConfigurationsFilterCriteria(BaseValidatorModel):
    scanConfigurationArnFilters: Optional[List[CisStringFilter]] = None
    scanNameFilters: Optional[List[CisStringFilter]] = None
    targetResourceTagFilters: Optional[List[TagFilter]] = None


class CodeVulnerabilityDetails(BaseValidatorModel):
    cwes: List[str]
    detectorId: str
    detectorName: str
    filePath: CodeFilePath
    detectorTags: Optional[List[str]] = None
    referenceUrls: Optional[List[str]] = None
    ruleId: Optional[str] = None
    sourceLambdaLayerArn: Optional[str] = None


class CodeSnippetResult(BaseValidatorModel):
    codeSnippet: Optional[List[CodeLine]] = None
    endLine: Optional[int] = None
    findingArn: Optional[str] = None
    startLine: Optional[int] = None
    suggestedFixes: Optional[List[SuggestedFix]] = None


class ListCoverageStatisticsResponse(BaseValidatorModel):
    countsByGroup: List[Counts]
    totalCounts: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CvssScoreDetails(BaseValidatorModel):
    score: float
    scoreSource: str
    scoringVector: str
    version: str
    adjustments: Optional[List[CvssScoreAdjustment]] = None
    cvssSource: Optional[str] = None


class DailySchedule(BaseValidatorModel):
    startTime: Time


class MonthlySchedule(BaseValidatorModel):
    day: DayType
    startTime: Time


class WeeklyScheduleOutput(BaseValidatorModel):
    days: List[DayType]
    startTime: Time


class WeeklySchedule(BaseValidatorModel):
    days: List[DayType]
    startTime: Time


class ListDelegatedAdminAccountsResponse(BaseValidatorModel):
    delegatedAdminAccounts: List[DelegatedAdminAccount]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetDelegatedAdminAccountResponse(BaseValidatorModel):
    delegatedAdmin: DelegatedAdmin
    ResponseMetadata: ResponseMetadata


class Ec2ConfigurationState(BaseValidatorModel):
    scanModeState: Optional[Ec2ScanModeState] = None


class Ec2InstanceAggregation(BaseValidatorModel):
    amis: Optional[List[StringFilter]] = None
    instanceIds: Optional[List[StringFilter]] = None
    instanceTags: Optional[List[MapFilter]] = None
    operatingSystems: Optional[List[StringFilter]] = None
    sortBy: Optional[Ec2InstanceSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class LambdaFunctionAggregation(BaseValidatorModel):
    functionNames: Optional[List[StringFilter]] = None
    functionTags: Optional[List[MapFilter]] = None
    resourceIds: Optional[List[StringFilter]] = None
    runtimes: Optional[List[StringFilter]] = None
    sortBy: Optional[LambdaFunctionSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class EcrConfigurationState(BaseValidatorModel):
    rescanDurationState: Optional[EcrRescanDurationState] = None


class UpdateConfigurationRequest(BaseValidatorModel):
    ec2Configuration: Optional[Ec2Configuration] = None
    ecrConfiguration: Optional[EcrConfiguration] = None


class FindingDetail(BaseValidatorModel):
    cisaData: Optional[CisaData] = None
    cwes: Optional[List[str]] = None
    epssScore: Optional[float] = None
    evidences: Optional[List[Evidence]] = None
    exploitObserved: Optional[ExploitObserved] = None
    findingArn: Optional[str] = None
    referenceUrls: Optional[List[str]] = None
    riskScore: Optional[int] = None
    tools: Optional[List[str]] = None
    ttps: Optional[List[str]] = None


class Vulnerability(BaseValidatorModel):
    id: str
    atigData: Optional[AtigData] = None
    cisaData: Optional[CisaData] = None
    cvss2: Optional[Cvss2] = None
    cvss3: Optional[Cvss3] = None
    cwes: Optional[List[str]] = None
    description: Optional[str] = None
    detectionPlatforms: Optional[List[str]] = None
    epss: Optional[Epss] = None
    exploitObserved: Optional[ExploitObserved] = None
    referenceUrls: Optional[List[str]] = None
    relatedVulnerabilities: Optional[List[str]] = None
    source: Optional[Literal['NVD']] = None
    sourceUrl: Optional[str] = None
    vendorCreatedAt: Optional[datetime] = None
    vendorSeverity: Optional[str] = None
    vendorUpdatedAt: Optional[datetime] = None


class PackageFilter(BaseValidatorModel):
    architecture: Optional[StringFilter] = None
    epoch: Optional[NumberFilter] = None
    filePath: Optional[StringFilter] = None
    name: Optional[StringFilter] = None
    release: Optional[StringFilter] = None
    sourceLambdaLayerArn: Optional[StringFilter] = None
    sourceLayerHash: Optional[StringFilter] = None
    version: Optional[StringFilter] = None


class FreeTrialAccountInfo(BaseValidatorModel):
    accountId: str
    freeTrialInfo: List[FreeTrialInfo]


class ListAccountPermissionsRequestPaginate(BaseValidatorModel):
    service: Optional[ServiceType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDelegatedAdminAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFiltersRequestPaginate(BaseValidatorModel):
    action: Optional[FilterActionType] = None
    arns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembersRequestPaginate(BaseValidatorModel):
    onlyAssociated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsageTotalsRequestPaginate(BaseValidatorModel):
    accountIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetMemberResponse(BaseValidatorModel):
    member: Member
    ResponseMetadata: ResponseMetadata


class ListMembersResponse(BaseValidatorModel):
    members: List[Member]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ResourceScanMetadata(BaseValidatorModel):
    ec2: Optional[Ec2Metadata] = None
    ecrImage: Optional[EcrContainerImageMetadata] = None
    ecrRepository: Optional[EcrRepositoryMetadata] = None
    lambdaFunction: Optional[LambdaFunctionMetadata] = None


class ListAccountPermissionsResponse(BaseValidatorModel):
    permissions: List[Permission]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class NetworkPath(BaseValidatorModel):
    steps: Optional[List[Step]] = None


class PackageVulnerabilityDetails(BaseValidatorModel):
    source: str
    vulnerabilityId: str
    cvss: Optional[List[CvssScore]] = None
    referenceUrls: Optional[List[str]] = None
    relatedVulnerabilities: Optional[List[str]] = None
    sourceUrl: Optional[str] = None
    vendorCreatedAt: Optional[datetime] = None
    vendorSeverity: Optional[str] = None
    vendorUpdatedAt: Optional[datetime] = None
    vulnerablePackages: Optional[List[VulnerablePackage]] = None


class Remediation(BaseValidatorModel):
    recommendation: Optional[Recommendation] = None


class ResourceFilterCriteriaOutput(BaseValidatorModel):
    accountId: Optional[List[ResourceStringFilter]] = None
    ec2InstanceTags: Optional[List[ResourceMapFilter]] = None
    ecrImageTags: Optional[List[ResourceStringFilter]] = None
    ecrRepositoryName: Optional[List[ResourceStringFilter]] = None
    lambdaFunctionName: Optional[List[ResourceStringFilter]] = None
    lambdaFunctionTags: Optional[List[ResourceMapFilter]] = None
    resourceId: Optional[List[ResourceStringFilter]] = None
    resourceType: Optional[List[ResourceStringFilter]] = None


class ResourceFilterCriteria(BaseValidatorModel):
    accountId: Optional[List[ResourceStringFilter]] = None
    ec2InstanceTags: Optional[List[ResourceMapFilter]] = None
    ecrImageTags: Optional[List[ResourceStringFilter]] = None
    ecrRepositoryName: Optional[List[ResourceStringFilter]] = None
    lambdaFunctionName: Optional[List[ResourceStringFilter]] = None
    lambdaFunctionTags: Optional[List[ResourceMapFilter]] = None
    resourceId: Optional[List[ResourceStringFilter]] = None
    resourceType: Optional[List[ResourceStringFilter]] = None


class SearchVulnerabilitiesRequestPaginate(BaseValidatorModel):
    filterCriteria: SearchVulnerabilitiesFilterCriteria
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchVulnerabilitiesRequest(BaseValidatorModel):
    filterCriteria: SearchVulnerabilitiesFilterCriteria
    nextToken: Optional[str] = None


class StartCisSessionRequest(BaseValidatorModel):
    message: StartCisSessionMessage
    scanJobId: str


class StopCisSessionMessage(BaseValidatorModel):
    progress: StopCisMessageProgress
    status: StopCisSessionStatusType
    benchmarkProfile: Optional[str] = None
    benchmarkVersion: Optional[str] = None
    computePlatform: Optional[ComputePlatform] = None
    reason: Optional[str] = None


class UsageTotal(BaseValidatorModel):
    accountId: Optional[str] = None
    usage: Optional[List[Usage]] = None


class AggregationResponse(BaseValidatorModel):
    accountAggregation: Optional[AccountAggregationResponse] = None
    amiAggregation: Optional[AmiAggregationResponse] = None
    awsEcrContainerAggregation: Optional[AwsEcrContainerAggregationResponse] = None
    ec2InstanceAggregation: Optional[Ec2InstanceAggregationResponse] = None
    findingTypeAggregation: Optional[FindingTypeAggregationResponse] = None
    imageLayerAggregation: Optional[ImageLayerAggregationResponse] = None
    lambdaFunctionAggregation: Optional[LambdaFunctionAggregationResponse] = None
    lambdaLayerAggregation: Optional[LambdaLayerAggregationResponse] = None
    packageAggregation: Optional[PackageAggregationResponse] = None
    repositoryAggregation: Optional[RepositoryAggregationResponse] = None
    titleAggregation: Optional[TitleAggregationResponse] = None


class AccountState(BaseValidatorModel):
    accountId: str
    resourceState: ResourceState
    state: State


class DisableResponse(BaseValidatorModel):
    accounts: List[Account]
    failedAccounts: List[FailedAccount]
    ResponseMetadata: ResponseMetadata


class EnableResponse(BaseValidatorModel):
    accounts: List[Account]
    failedAccounts: List[FailedAccount]
    ResponseMetadata: ResponseMetadata


class ResourceDetails(BaseValidatorModel):
    awsEc2Instance: Optional[AwsEc2InstanceDetails] = None
    awsEcrContainerImage: Optional[AwsEcrContainerImageDetails] = None
    awsLambdaFunction: Optional[AwsLambdaFunctionDetails] = None


class SendCisSessionTelemetryRequest(BaseValidatorModel):
    messages: List[CisSessionMessage]
    scanJobId: str
    sessionToken: str


class ListCisScanResultsAggregatedByChecksResponse(BaseValidatorModel):
    checkAggregations: List[CisCheckAggregation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListCisScanResultsAggregatedByTargetResourceResponse(BaseValidatorModel):
    targetResourceAggregations: List[CisTargetResourceAggregation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListCisScansFilterCriteria(BaseValidatorModel):
    failedChecksFilters: Optional[List[CisNumberFilter]] = None
    scanArnFilters: Optional[List[CisStringFilter]] = None
    scanAtFilters: Optional[List[CisDateFilter]] = None
    scanConfigurationArnFilters: Optional[List[CisStringFilter]] = None
    scanNameFilters: Optional[List[CisStringFilter]] = None
    scanStatusFilters: Optional[List[CisScanStatusFilter]] = None
    scheduledByFilters: Optional[List[CisStringFilter]] = None
    targetAccountIdFilters: Optional[List[CisStringFilter]] = None
    targetResourceIdFilters: Optional[List[CisStringFilter]] = None
    targetResourceTagFilters: Optional[List[TagFilter]] = None


class CoverageFilterCriteria(BaseValidatorModel):
    accountId: Optional[List[CoverageStringFilter]] = None
    ec2InstanceTags: Optional[List[CoverageMapFilter]] = None
    ecrImageTags: Optional[List[CoverageStringFilter]] = None
    ecrRepositoryName: Optional[List[CoverageStringFilter]] = None
    imagePulledAt: Optional[List[CoverageDateFilter]] = None
    lambdaFunctionName: Optional[List[CoverageStringFilter]] = None
    lambdaFunctionRuntime: Optional[List[CoverageStringFilter]] = None
    lambdaFunctionTags: Optional[List[CoverageMapFilter]] = None
    lastScannedAt: Optional[List[CoverageDateFilter]] = None
    resourceId: Optional[List[CoverageStringFilter]] = None
    resourceType: Optional[List[CoverageStringFilter]] = None
    scanMode: Optional[List[CoverageStringFilter]] = None
    scanStatusCode: Optional[List[CoverageStringFilter]] = None
    scanStatusReason: Optional[List[CoverageStringFilter]] = None
    scanType: Optional[List[CoverageStringFilter]] = None


class ListCisScansResponse(BaseValidatorModel):
    scans: List[CisScan]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetCisScanResultDetailsRequestPaginate(BaseValidatorModel):
    accountId: str
    scanArn: str
    targetResourceId: str
    filterCriteria: Optional[CisScanResultDetailsFilterCriteria] = None
    sortBy: Optional[CisScanResultDetailsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCisScanResultDetailsRequest(BaseValidatorModel):
    accountId: str
    scanArn: str
    targetResourceId: str
    filterCriteria: Optional[CisScanResultDetailsFilterCriteria] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanResultDetailsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class ListCisScanResultsAggregatedByChecksRequestPaginate(BaseValidatorModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByChecksFilterCriteria] = None
    sortBy: Optional[CisScanResultsAggregatedByChecksSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCisScanResultsAggregatedByChecksRequest(BaseValidatorModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByChecksFilterCriteria] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanResultsAggregatedByChecksSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class ListCisScanResultsAggregatedByTargetResourceRequestPaginate(BaseValidatorModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByTargetResourceFilterCriteria] = None
    sortBy: Optional[CisScanResultsAggregatedByTargetResourceSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCisScanResultsAggregatedByTargetResourceRequest(BaseValidatorModel):
    scanArn: str
    filterCriteria: Optional[CisScanResultsAggregatedByTargetResourceFilterCriteria] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanResultsAggregatedByTargetResourceSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class ListCisScanConfigurationsRequestPaginate(BaseValidatorModel):
    filterCriteria: Optional[ListCisScanConfigurationsFilterCriteria] = None
    sortBy: Optional[CisScanConfigurationsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCisScanConfigurationsRequest(BaseValidatorModel):
    filterCriteria: Optional[ListCisScanConfigurationsFilterCriteria] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[CisScanConfigurationsSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class BatchGetCodeSnippetResponse(BaseValidatorModel):
    codeSnippetResults: List[CodeSnippetResult]
    errors: List[CodeSnippetError]
    ResponseMetadata: ResponseMetadata


class InspectorScoreDetails(BaseValidatorModel):
    adjustedCvss: Optional[CvssScoreDetails] = None


class ScheduleOutput(BaseValidatorModel):
    daily: Optional[DailySchedule] = None
    monthly: Optional[MonthlySchedule] = None
    oneTime: Optional[Dict[str, Any]] = None
    weekly: Optional[WeeklyScheduleOutput] = None


class Schedule(BaseValidatorModel):
    daily: Optional[DailySchedule] = None
    monthly: Optional[MonthlySchedule] = None
    oneTime: Optional[Dict[str, Any]] = None
    weekly: Optional[WeeklySchedule] = None


class AggregationRequest(BaseValidatorModel):
    accountAggregation: Optional[AccountAggregation] = None
    amiAggregation: Optional[AmiAggregation] = None
    awsEcrContainerAggregation: Optional[AwsEcrContainerAggregation] = None
    ec2InstanceAggregation: Optional[Ec2InstanceAggregation] = None
    findingTypeAggregation: Optional[FindingTypeAggregation] = None
    imageLayerAggregation: Optional[ImageLayerAggregation] = None
    lambdaFunctionAggregation: Optional[LambdaFunctionAggregation] = None
    lambdaLayerAggregation: Optional[LambdaLayerAggregation] = None
    packageAggregation: Optional[PackageAggregation] = None
    repositoryAggregation: Optional[RepositoryAggregation] = None
    titleAggregation: Optional[TitleAggregation] = None


class GetConfigurationResponse(BaseValidatorModel):
    ec2Configuration: Ec2ConfigurationState
    ecrConfiguration: EcrConfigurationState
    ResponseMetadata: ResponseMetadata


class BatchGetFindingDetailsResponse(BaseValidatorModel):
    errors: List[FindingDetailsError]
    findingDetails: List[FindingDetail]
    ResponseMetadata: ResponseMetadata


class SearchVulnerabilitiesResponse(BaseValidatorModel):
    vulnerabilities: List[Vulnerability]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FilterCriteriaOutput(BaseValidatorModel):
    awsAccountId: Optional[List[StringFilter]] = None
    codeVulnerabilityDetectorName: Optional[List[StringFilter]] = None
    codeVulnerabilityDetectorTags: Optional[List[StringFilter]] = None
    codeVulnerabilityFilePath: Optional[List[StringFilter]] = None
    componentId: Optional[List[StringFilter]] = None
    componentType: Optional[List[StringFilter]] = None
    ec2InstanceImageId: Optional[List[StringFilter]] = None
    ec2InstanceSubnetId: Optional[List[StringFilter]] = None
    ec2InstanceVpcId: Optional[List[StringFilter]] = None
    ecrImageArchitecture: Optional[List[StringFilter]] = None
    ecrImageHash: Optional[List[StringFilter]] = None
    ecrImagePushedAt: Optional[List[DateFilterOutput]] = None
    ecrImageRegistry: Optional[List[StringFilter]] = None
    ecrImageRepositoryName: Optional[List[StringFilter]] = None
    ecrImageTags: Optional[List[StringFilter]] = None
    epssScore: Optional[List[NumberFilter]] = None
    exploitAvailable: Optional[List[StringFilter]] = None
    findingArn: Optional[List[StringFilter]] = None
    findingStatus: Optional[List[StringFilter]] = None
    findingType: Optional[List[StringFilter]] = None
    firstObservedAt: Optional[List[DateFilterOutput]] = None
    fixAvailable: Optional[List[StringFilter]] = None
    inspectorScore: Optional[List[NumberFilter]] = None
    lambdaFunctionExecutionRoleArn: Optional[List[StringFilter]] = None
    lambdaFunctionLastModifiedAt: Optional[List[DateFilterOutput]] = None
    lambdaFunctionLayers: Optional[List[StringFilter]] = None
    lambdaFunctionName: Optional[List[StringFilter]] = None
    lambdaFunctionRuntime: Optional[List[StringFilter]] = None
    lastObservedAt: Optional[List[DateFilterOutput]] = None
    networkProtocol: Optional[List[StringFilter]] = None
    portRange: Optional[List[PortRangeFilter]] = None
    relatedVulnerabilities: Optional[List[StringFilter]] = None
    resourceId: Optional[List[StringFilter]] = None
    resourceTags: Optional[List[MapFilter]] = None
    resourceType: Optional[List[StringFilter]] = None
    severity: Optional[List[StringFilter]] = None
    title: Optional[List[StringFilter]] = None
    updatedAt: Optional[List[DateFilterOutput]] = None
    vendorSeverity: Optional[List[StringFilter]] = None
    vulnerabilityId: Optional[List[StringFilter]] = None
    vulnerabilitySource: Optional[List[StringFilter]] = None
    vulnerablePackages: Optional[List[PackageFilter]] = None


class FilterCriteria(BaseValidatorModel):
    awsAccountId: Optional[List[StringFilter]] = None
    codeVulnerabilityDetectorName: Optional[List[StringFilter]] = None
    codeVulnerabilityDetectorTags: Optional[List[StringFilter]] = None
    codeVulnerabilityFilePath: Optional[List[StringFilter]] = None
    componentId: Optional[List[StringFilter]] = None
    componentType: Optional[List[StringFilter]] = None
    ec2InstanceImageId: Optional[List[StringFilter]] = None
    ec2InstanceSubnetId: Optional[List[StringFilter]] = None
    ec2InstanceVpcId: Optional[List[StringFilter]] = None
    ecrImageArchitecture: Optional[List[StringFilter]] = None
    ecrImageHash: Optional[List[StringFilter]] = None
    ecrImagePushedAt: Optional[List[DateFilter]] = None
    ecrImageRegistry: Optional[List[StringFilter]] = None
    ecrImageRepositoryName: Optional[List[StringFilter]] = None
    ecrImageTags: Optional[List[StringFilter]] = None
    epssScore: Optional[List[NumberFilter]] = None
    exploitAvailable: Optional[List[StringFilter]] = None
    findingArn: Optional[List[StringFilter]] = None
    findingStatus: Optional[List[StringFilter]] = None
    findingType: Optional[List[StringFilter]] = None
    firstObservedAt: Optional[List[DateFilter]] = None
    fixAvailable: Optional[List[StringFilter]] = None
    inspectorScore: Optional[List[NumberFilter]] = None
    lambdaFunctionExecutionRoleArn: Optional[List[StringFilter]] = None
    lambdaFunctionLastModifiedAt: Optional[List[DateFilter]] = None
    lambdaFunctionLayers: Optional[List[StringFilter]] = None
    lambdaFunctionName: Optional[List[StringFilter]] = None
    lambdaFunctionRuntime: Optional[List[StringFilter]] = None
    lastObservedAt: Optional[List[DateFilter]] = None
    networkProtocol: Optional[List[StringFilter]] = None
    portRange: Optional[List[PortRangeFilter]] = None
    relatedVulnerabilities: Optional[List[StringFilter]] = None
    resourceId: Optional[List[StringFilter]] = None
    resourceTags: Optional[List[MapFilter]] = None
    resourceType: Optional[List[StringFilter]] = None
    severity: Optional[List[StringFilter]] = None
    title: Optional[List[StringFilter]] = None
    updatedAt: Optional[List[DateFilter]] = None
    vendorSeverity: Optional[List[StringFilter]] = None
    vulnerabilityId: Optional[List[StringFilter]] = None
    vulnerabilitySource: Optional[List[StringFilter]] = None
    vulnerablePackages: Optional[List[PackageFilter]] = None


class BatchGetFreeTrialInfoResponse(BaseValidatorModel):
    accounts: List[FreeTrialAccountInfo]
    failedAccounts: List[FreeTrialInfoError]
    ResponseMetadata: ResponseMetadata


class CoveredResource(BaseValidatorModel):
    accountId: str
    resourceId: str
    resourceType: CoverageResourceTypeType
    scanType: ScanTypeType
    lastScannedAt: Optional[datetime] = None
    resourceMetadata: Optional[ResourceScanMetadata] = None
    scanMode: Optional[ScanModeType] = None
    scanStatus: Optional[ScanStatus] = None


class NetworkReachabilityDetails(BaseValidatorModel):
    networkPath: NetworkPath
    openPortRange: PortRange
    protocol: NetworkProtocolType


class GetSbomExportResponse(BaseValidatorModel):
    errorCode: ReportingErrorCodeType
    errorMessage: str
    filterCriteria: ResourceFilterCriteriaOutput
    format: SbomReportFormatType
    reportId: str
    s3Destination: Destination
    status: ExternalReportStatusType
    ResponseMetadata: ResponseMetadata

ResourceFilterCriteriaUnion = Union[ResourceFilterCriteria, ResourceFilterCriteriaOutput]


class StopCisSessionRequest(BaseValidatorModel):
    message: StopCisSessionMessage
    scanJobId: str
    sessionToken: str


class ListUsageTotalsResponse(BaseValidatorModel):
    totals: List[UsageTotal]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFindingAggregationsResponse(BaseValidatorModel):
    aggregationType: AggregationTypeType
    responses: List[AggregationResponse]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchGetAccountStatusResponse(BaseValidatorModel):
    accounts: List[AccountState]
    failedAccounts: List[FailedAccount]
    ResponseMetadata: ResponseMetadata


class Resource(BaseValidatorModel):
    id: str
    type: ResourceTypeType
    details: Optional[ResourceDetails] = None
    partition: Optional[str] = None
    region: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListCisScansRequestPaginate(BaseValidatorModel):
    detailLevel: Optional[ListCisScansDetailLevelType] = None
    filterCriteria: Optional[ListCisScansFilterCriteria] = None
    sortBy: Optional[ListCisScansSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCisScansRequest(BaseValidatorModel):
    detailLevel: Optional[ListCisScansDetailLevelType] = None
    filterCriteria: Optional[ListCisScansFilterCriteria] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[ListCisScansSortByType] = None
    sortOrder: Optional[CisSortOrderType] = None


class ListCoverageRequestPaginate(BaseValidatorModel):
    filterCriteria: Optional[CoverageFilterCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCoverageRequest(BaseValidatorModel):
    filterCriteria: Optional[CoverageFilterCriteria] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListCoverageStatisticsRequestPaginate(BaseValidatorModel):
    filterCriteria: Optional[CoverageFilterCriteria] = None
    groupBy: Optional[GroupKeyType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCoverageStatisticsRequest(BaseValidatorModel):
    filterCriteria: Optional[CoverageFilterCriteria] = None
    groupBy: Optional[GroupKeyType] = None
    nextToken: Optional[str] = None


class CisScanConfiguration(BaseValidatorModel):
    scanConfigurationArn: str
    ownerId: Optional[str] = None
    scanName: Optional[str] = None
    schedule: Optional[ScheduleOutput] = None
    securityLevel: Optional[CisSecurityLevelType] = None
    tags: Optional[Dict[str, str]] = None
    targets: Optional[CisTargets] = None

ScheduleUnion = Union[Schedule, ScheduleOutput]


class ListFindingAggregationsRequestPaginate(BaseValidatorModel):
    aggregationType: AggregationTypeType
    accountIds: Optional[List[StringFilter]] = None
    aggregationRequest: Optional[AggregationRequest] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingAggregationsRequest(BaseValidatorModel):
    aggregationType: AggregationTypeType
    accountIds: Optional[List[StringFilter]] = None
    aggregationRequest: Optional[AggregationRequest] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class Filter(BaseValidatorModel):
    action: FilterActionType
    arn: str
    createdAt: datetime
    criteria: FilterCriteriaOutput
    name: str
    ownerId: str
    updatedAt: datetime
    description: Optional[str] = None
    reason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class GetFindingsReportStatusResponse(BaseValidatorModel):
    destination: Destination
    errorCode: ReportingErrorCodeType
    errorMessage: str
    filterCriteria: FilterCriteriaOutput
    reportId: str
    status: ExternalReportStatusType
    ResponseMetadata: ResponseMetadata

FilterCriteriaUnion = Union[FilterCriteria, FilterCriteriaOutput]


class ListCoverageResponse(BaseValidatorModel):
    coveredResources: List[CoveredResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateSbomExportRequest(BaseValidatorModel):
    reportFormat: SbomReportFormatType
    s3Destination: Destination
    resourceFilterCriteria: Optional[ResourceFilterCriteriaUnion] = None


class Finding(BaseValidatorModel):
    awsAccountId: str
    description: str
    findingArn: str
    firstObservedAt: datetime
    lastObservedAt: datetime
    remediation: Remediation
    resources: List[Resource]
    severity: SeverityType
    status: FindingStatusType
    type: FindingTypeType
    codeVulnerabilityDetails: Optional[CodeVulnerabilityDetails] = None
    epss: Optional[EpssDetails] = None
    exploitAvailable: Optional[ExploitAvailableType] = None
    exploitabilityDetails: Optional[ExploitabilityDetails] = None
    fixAvailable: Optional[FixAvailableType] = None
    inspectorScore: Optional[float] = None
    inspectorScoreDetails: Optional[InspectorScoreDetails] = None
    networkReachabilityDetails: Optional[NetworkReachabilityDetails] = None
    packageVulnerabilityDetails: Optional[PackageVulnerabilityDetails] = None
    title: Optional[str] = None
    updatedAt: Optional[datetime] = None


class ListCisScanConfigurationsResponse(BaseValidatorModel):
    scanConfigurations: List[CisScanConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateCisScanConfigurationRequest(BaseValidatorModel):
    scanName: str
    schedule: ScheduleUnion
    securityLevel: CisSecurityLevelType
    targets: CreateCisTargets
    tags: Optional[Dict[str, str]] = None


class UpdateCisScanConfigurationRequest(BaseValidatorModel):
    scanConfigurationArn: str
    scanName: Optional[str] = None
    schedule: Optional[ScheduleUnion] = None
    securityLevel: Optional[CisSecurityLevelType] = None
    targets: Optional[UpdateCisTargets] = None


class ListFiltersResponse(BaseValidatorModel):
    filters: List[Filter]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateFilterRequest(BaseValidatorModel):
    action: FilterActionType
    filterCriteria: FilterCriteriaUnion
    name: str
    description: Optional[str] = None
    reason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateFindingsReportRequest(BaseValidatorModel):
    reportFormat: ReportFormatType
    s3Destination: Destination
    filterCriteria: Optional[FilterCriteriaUnion] = None


class ListFindingsRequestPaginate(BaseValidatorModel):
    filterCriteria: Optional[FilterCriteriaUnion] = None
    sortCriteria: Optional[SortCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingsRequest(BaseValidatorModel):
    filterCriteria: Optional[FilterCriteriaUnion] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortCriteria: Optional[SortCriteria] = None


class UpdateFilterRequest(BaseValidatorModel):
    filterArn: str
    action: Optional[FilterActionType] = None
    description: Optional[str] = None
    filterCriteria: Optional[FilterCriteriaUnion] = None
    name: Optional[str] = None
    reason: Optional[str] = None


class ListFindingsResponse(BaseValidatorModel):
    findings: List[Finding]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None
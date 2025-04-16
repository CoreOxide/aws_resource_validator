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
from aws_resource_validator.pydantic_models.codebuild_constants import *

class AutoRetryConfig(BaseValidatorModel):
    autoRetryLimit: Optional[int] = None
    autoRetryNumber: Optional[int] = None
    nextAutoRetry: Optional[str] = None
    previousAutoRetry: Optional[str] = None


class BatchDeleteBuildsInput(BaseValidatorModel):
    ids: Sequence[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetBuildBatchesInput(BaseValidatorModel):
    ids: Sequence[str]


class BatchGetBuildsInput(BaseValidatorModel):
    ids: Sequence[str]


class BatchGetFleetsInput(BaseValidatorModel):
    names: Sequence[str]


class BatchGetProjectsInput(BaseValidatorModel):
    names: Sequence[str]


class BatchGetReportGroupsInput(BaseValidatorModel):
    reportGroupArns: Sequence[str]


class BatchGetReportsInput(BaseValidatorModel):
    reportArns: Sequence[str]


class BatchRestrictionsOutput(BaseValidatorModel):
    maximumBuildsAllowed: Optional[int] = None
    computeTypesAllowed: Optional[List[str]] = None
    fleetsAllowed: Optional[List[str]] = None


class BatchRestrictions(BaseValidatorModel):
    maximumBuildsAllowed: Optional[int] = None
    computeTypesAllowed: Optional[Sequence[str]] = None
    fleetsAllowed: Optional[Sequence[str]] = None


class BuildArtifacts(BaseValidatorModel):
    location: Optional[str] = None
    sha256sum: Optional[str] = None
    md5sum: Optional[str] = None
    overrideArtifactName: Optional[bool] = None
    encryptionDisabled: Optional[bool] = None
    artifactIdentifier: Optional[str] = None
    bucketOwnerAccess: Optional[BucketOwnerAccessType] = None


class BuildBatchFilter(BaseValidatorModel):
    status: Optional[StatusTypeType] = None


class PhaseContext(BaseValidatorModel):
    statusCode: Optional[str] = None
    message: Optional[str] = None


class ProjectSourceVersion(BaseValidatorModel):
    sourceIdentifier: str
    sourceVersion: str


class VpcConfigOutput(BaseValidatorModel):
    vpcId: Optional[str] = None
    subnets: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None


class BuildStatusConfig(BaseValidatorModel):
    context: Optional[str] = None
    targetUrl: Optional[str] = None


class DebugSession(BaseValidatorModel):
    sessionEnabled: Optional[bool] = None
    sessionTarget: Optional[str] = None


class ExportedEnvironmentVariable(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class NetworkInterface(BaseValidatorModel):
    subnetId: Optional[str] = None
    networkInterfaceId: Optional[str] = None


class CloudWatchLogsConfig(BaseValidatorModel):
    status: LogsConfigStatusTypeType
    groupName: Optional[str] = None
    streamName: Optional[str] = None


class CodeCoverageReportSummary(BaseValidatorModel):
    lineCoveragePercentage: Optional[float] = None
    linesCovered: Optional[int] = None
    linesMissed: Optional[int] = None
    branchCoveragePercentage: Optional[float] = None
    branchesCovered: Optional[int] = None
    branchesMissed: Optional[int] = None


class ComputeConfiguration(BaseValidatorModel):
    vCpu: Optional[int] = None
    memory: Optional[int] = None
    disk: Optional[int] = None
    machineType: Optional[MachineTypeType] = None


class Tag(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ScopeConfiguration(BaseValidatorModel):
    name: str
    scope: WebhookScopeTypeType
    domain: Optional[str] = None


class DeleteFleetInput(BaseValidatorModel):
    arn: str


class DeleteProjectInput(BaseValidatorModel):
    name: str


class DeleteReportGroupInput(BaseValidatorModel):
    arn: str
    deleteReports: Optional[bool] = None


class DeleteReportInput(BaseValidatorModel):
    arn: str


class DeleteResourcePolicyInput(BaseValidatorModel):
    resourceArn: str


class DeleteSourceCredentialsInput(BaseValidatorModel):
    arn: str


class DeleteWebhookInput(BaseValidatorModel):
    projectName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeCodeCoveragesInput(BaseValidatorModel):
    reportArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportCodeCoverageSortByTypeType] = None
    minLineCoveragePercentage: Optional[float] = None
    maxLineCoveragePercentage: Optional[float] = None


class TestCaseFilter(BaseValidatorModel):
    status: Optional[str] = None
    keyword: Optional[str] = None


class TestCase(BaseValidatorModel):
    reportArn: Optional[str] = None
    testRawDataPath: Optional[str] = None
    prefix: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    durationInNanoSeconds: Optional[int] = None
    message: Optional[str] = None
    expired: Optional[datetime] = None
    testSuiteName: Optional[str] = None


class EnvironmentImage(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    versions: Optional[List[str]] = None


class FleetStatus(BaseValidatorModel):
    statusCode: Optional[FleetStatusCodeType] = None
    context: Optional[FleetContextCodeType] = None
    message: Optional[str] = None


class GetReportGroupTrendInput(BaseValidatorModel):
    reportGroupArn: str
    trendField: ReportGroupTrendFieldTypeType
    numOfReports: Optional[int] = None


class ReportWithRawData(BaseValidatorModel):
    reportArn: Optional[str] = None
    data: Optional[str] = None


class GetResourcePolicyInput(BaseValidatorModel):
    resourceArn: str


class GitSubmodulesConfig(BaseValidatorModel):
    fetchSubmodules: bool


class ImportSourceCredentialsInput(BaseValidatorModel):
    token: str
    serverType: ServerTypeType
    authType: AuthTypeType
    username: Optional[str] = None
    shouldOverwrite: Optional[bool] = None


class InvalidateProjectCacheInput(BaseValidatorModel):
    projectName: str


class ListBuildsForProjectInput(BaseValidatorModel):
    projectName: str
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None


class ListBuildsInput(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None


class ListFleetsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[FleetSortByTypeType] = None


class ListProjectsInput(BaseValidatorModel):
    sortBy: Optional[ProjectSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None


class ListReportGroupsInput(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportGroupSortByTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ReportFilter(BaseValidatorModel):
    status: Optional[ReportStatusTypeType] = None


class ListSharedProjectsInput(BaseValidatorModel):
    sortBy: Optional[SharedResourceSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSharedReportGroupsInput(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[SharedResourceSortByTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SourceCredentialsInfo(BaseValidatorModel):
    arn: Optional[str] = None
    serverType: Optional[ServerTypeType] = None
    authType: Optional[AuthTypeType] = None
    resource: Optional[str] = None


class S3LogsConfig(BaseValidatorModel):
    status: LogsConfigStatusTypeType
    location: Optional[str] = None
    encryptionDisabled: Optional[bool] = None
    bucketOwnerAccess: Optional[BucketOwnerAccessType] = None


class ProjectBadge(BaseValidatorModel):
    badgeEnabled: Optional[bool] = None
    badgeRequestUrl: Optional[str] = None


class ProjectFleet(BaseValidatorModel):
    fleetArn: Optional[str] = None


class RegistryCredential(BaseValidatorModel):
    credential: str
    credentialProvider: Literal["SECRETS_MANAGER"]


class PutResourcePolicyInput(BaseValidatorModel):
    policy: str
    resourceArn: str


class S3ReportExportConfig(BaseValidatorModel):
    bucket: Optional[str] = None
    bucketOwner: Optional[str] = None
    path: Optional[str] = None
    packaging: Optional[ReportPackagingTypeType] = None
    encryptionKey: Optional[str] = None
    encryptionDisabled: Optional[bool] = None


class TestReportSummary(BaseValidatorModel):
    total: int
    statusCounts: Dict[str, int]
    durationInNanoSeconds: int


class TargetTrackingScalingConfiguration(BaseValidatorModel):
    metricType: Optional[Literal["FLEET_UTILIZATION_RATE"]] = None
    targetValue: Optional[float] = None


class UpdateProjectVisibilityInput(BaseValidatorModel):
    projectArn: str
    projectVisibility: ProjectVisibilityTypeType
    resourceAccessRole: Optional[str] = None


class VpcConfig(BaseValidatorModel):
    vpcId: Optional[str] = None
    subnets: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None


class BuildNotDeleted(BaseValidatorModel):
    pass


class BatchDeleteBuildsOutput(BaseValidatorModel):
    buildsDeleted: List[str]
    buildsNotDeleted: List[BuildNotDeleted]
    ResponseMetadata: ResponseMetadata


class DeleteBuildBatchOutput(BaseValidatorModel):
    statusCode: str
    buildsDeleted: List[str]
    buildsNotDeleted: List[BuildNotDeleted]
    ResponseMetadata: ResponseMetadata


class DeleteSourceCredentialsOutput(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyOutput(BaseValidatorModel):
    policy: str
    ResponseMetadata: ResponseMetadata


class ImportSourceCredentialsOutput(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class ListBuildBatchesForProjectOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBuildBatchesOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBuildsForProjectOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBuildsOutput(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFleetsOutput(BaseValidatorModel):
    fleets: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListProjectsOutput(BaseValidatorModel):
    projects: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListReportGroupsOutput(BaseValidatorModel):
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListReportsForReportGroupOutput(BaseValidatorModel):
    reports: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListReportsOutput(BaseValidatorModel):
    reports: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSharedProjectsOutput(BaseValidatorModel):
    projects: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSharedReportGroupsOutput(BaseValidatorModel):
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PutResourcePolicyOutput(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadata


class UpdateProjectVisibilityOutput(BaseValidatorModel):
    projectArn: str
    publicProjectAlias: str
    projectVisibility: ProjectVisibilityTypeType
    ResponseMetadata: ResponseMetadata


class ProjectBuildBatchConfigOutput(BaseValidatorModel):
    serviceRole: Optional[str] = None
    combineArtifacts: Optional[bool] = None
    restrictions: Optional[BatchRestrictionsOutput] = None
    timeoutInMins: Optional[int] = None
    batchReportMode: Optional[BatchReportModeTypeType] = None


class ProjectBuildBatchConfig(BaseValidatorModel):
    serviceRole: Optional[str] = None
    combineArtifacts: Optional[bool] = None
    restrictions: Optional[BatchRestrictions] = None
    timeoutInMins: Optional[int] = None
    batchReportMode: Optional[BatchReportModeTypeType] = None


class BuildBatchPhase(BaseValidatorModel):
    phaseType: Optional[BuildBatchPhaseTypeType] = None
    phaseStatus: Optional[StatusTypeType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    durationInSeconds: Optional[int] = None
    contexts: Optional[List[PhaseContext]] = None


class BuildPhase(BaseValidatorModel):
    phaseType: Optional[BuildPhaseTypeType] = None
    phaseStatus: Optional[StatusTypeType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    durationInSeconds: Optional[int] = None
    contexts: Optional[List[PhaseContext]] = None


class ResolvedArtifact(BaseValidatorModel):
    pass


class BuildSummary(BaseValidatorModel):
    arn: Optional[str] = None
    requestedOn: Optional[datetime] = None
    buildStatus: Optional[StatusTypeType] = None
    primaryArtifact: Optional[ResolvedArtifact] = None
    secondaryArtifacts: Optional[List[ResolvedArtifact]] = None


class CodeCoverage(BaseValidatorModel):
    pass


class DescribeCodeCoveragesOutput(BaseValidatorModel):
    codeCoverages: List[CodeCoverage]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WebhookFilter(BaseValidatorModel):
    pass


class CreateWebhookInput(BaseValidatorModel):
    projectName: str
    branchFilter: Optional[str] = None
    filterGroups: Optional[Sequence[Sequence[WebhookFilter]]] = None
    buildType: Optional[WebhookBuildTypeType] = None
    manualCreation: Optional[bool] = None
    scopeConfiguration: Optional[ScopeConfiguration] = None


class UpdateWebhookInput(BaseValidatorModel):
    projectName: str
    branchFilter: Optional[str] = None
    rotateSecret: Optional[bool] = None
    filterGroups: Optional[Sequence[Sequence[WebhookFilter]]] = None
    buildType: Optional[WebhookBuildTypeType] = None


class Webhook(BaseValidatorModel):
    url: Optional[str] = None
    payloadUrl: Optional[str] = None
    secret: Optional[str] = None
    branchFilter: Optional[str] = None
    filterGroups: Optional[List[List[WebhookFilter]]] = None
    buildType: Optional[WebhookBuildTypeType] = None
    manualCreation: Optional[bool] = None
    lastModifiedSecret: Optional[datetime] = None
    scopeConfiguration: Optional[ScopeConfiguration] = None
    status: Optional[WebhookStatusType] = None
    statusMessage: Optional[str] = None


class DescribeCodeCoveragesInputPaginate(BaseValidatorModel):
    reportArn: str
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportCodeCoverageSortByTypeType] = None
    minLineCoveragePercentage: Optional[float] = None
    maxLineCoveragePercentage: Optional[float] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBuildsForProjectInputPaginate(BaseValidatorModel):
    projectName: str
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBuildsInputPaginate(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsInputPaginate(BaseValidatorModel):
    sortBy: Optional[ProjectSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReportGroupsInputPaginate(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportGroupSortByTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSharedProjectsInputPaginate(BaseValidatorModel):
    sortBy: Optional[SharedResourceSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSharedReportGroupsInputPaginate(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[SharedResourceSortByTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTestCasesOutput(BaseValidatorModel):
    testCases: List[TestCase]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EnvironmentLanguage(BaseValidatorModel):
    language: Optional[LanguageTypeType] = None
    images: Optional[List[EnvironmentImage]] = None


class FleetProxyRuleOutput(BaseValidatorModel):
    pass


class ProxyConfigurationOutput(BaseValidatorModel):
    defaultBehavior: Optional[FleetProxyRuleBehaviorType] = None
    orderedProxyRules: Optional[List[FleetProxyRuleOutput]] = None


class FleetProxyRule(BaseValidatorModel):
    pass


class ProxyConfiguration(BaseValidatorModel):
    defaultBehavior: Optional[FleetProxyRuleBehaviorType] = None
    orderedProxyRules: Optional[Sequence[FleetProxyRule]] = None


class ReportGroupTrendStats(BaseValidatorModel):
    pass


class GetReportGroupTrendOutput(BaseValidatorModel):
    stats: ReportGroupTrendStats
    rawData: List[ReportWithRawData]
    ResponseMetadata: ResponseMetadata


class ListSourceCredentialsOutput(BaseValidatorModel):
    sourceCredentialsInfos: List[SourceCredentialsInfo]
    ResponseMetadata: ResponseMetadata


class LogsConfig(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsConfig] = None
    s3Logs: Optional[S3LogsConfig] = None


class LogsLocation(BaseValidatorModel):
    groupName: Optional[str] = None
    streamName: Optional[str] = None
    deepLink: Optional[str] = None
    s3DeepLink: Optional[str] = None
    cloudWatchLogsArn: Optional[str] = None
    s3LogsArn: Optional[str] = None
    cloudWatchLogs: Optional[CloudWatchLogsConfig] = None
    s3Logs: Optional[S3LogsConfig] = None


class ReportExportConfig(BaseValidatorModel):
    exportConfigType: Optional[ReportExportConfigTypeType] = None
    s3Destination: Optional[S3ReportExportConfig] = None


class ScalingConfigurationInput(BaseValidatorModel):
    scalingType: Optional[Literal["TARGET_TRACKING_SCALING"]] = None
    targetTrackingScalingConfigs: Optional[Sequence[TargetTrackingScalingConfiguration]] = None
    maxCapacity: Optional[int] = None


class ScalingConfigurationOutput(BaseValidatorModel):
    scalingType: Optional[Literal["TARGET_TRACKING_SCALING"]] = None
    targetTrackingScalingConfigs: Optional[List[TargetTrackingScalingConfiguration]] = None
    maxCapacity: Optional[int] = None
    desiredCapacity: Optional[int] = None


class BuildGroup(BaseValidatorModel):
    identifier: Optional[str] = None
    dependsOn: Optional[List[str]] = None
    ignoreFailure: Optional[bool] = None
    currentBuildSummary: Optional[BuildSummary] = None
    priorBuildSummaryList: Optional[List[BuildSummary]] = None


class CreateWebhookOutput(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


class UpdateWebhookOutput(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


class EnvironmentPlatform(BaseValidatorModel):
    platform: Optional[PlatformTypeType] = None
    languages: Optional[List[EnvironmentLanguage]] = None


class ProjectSource(BaseValidatorModel):
    pass


class ProjectEnvironmentOutput(BaseValidatorModel):
    pass


class ProjectCacheOutput(BaseValidatorModel):
    pass


class ProjectArtifacts(BaseValidatorModel):
    pass


class ProjectFileSystemLocation(BaseValidatorModel):
    pass


class Project(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    source: Optional[ProjectSource] = None
    secondarySources: Optional[List[ProjectSource]] = None
    sourceVersion: Optional[str] = None
    secondarySourceVersions: Optional[List[ProjectSourceVersion]] = None
    artifacts: Optional[ProjectArtifacts] = None
    secondaryArtifacts: Optional[List[ProjectArtifacts]] = None
    cache: Optional[ProjectCacheOutput] = None
    environment: Optional[ProjectEnvironmentOutput] = None
    serviceRole: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    encryptionKey: Optional[str] = None
    tags: Optional[List[Tag]] = None
    created: Optional[datetime] = None
    lastModified: Optional[datetime] = None
    webhook: Optional[Webhook] = None
    vpcConfig: Optional[VpcConfigOutput] = None
    badge: Optional[ProjectBadge] = None
    logsConfig: Optional[LogsConfig] = None
    fileSystemLocations: Optional[List[ProjectFileSystemLocation]] = None
    buildBatchConfig: Optional[ProjectBuildBatchConfigOutput] = None
    concurrentBuildLimit: Optional[int] = None
    projectVisibility: Optional[ProjectVisibilityTypeType] = None
    publicProjectAlias: Optional[str] = None
    resourceAccessRole: Optional[str] = None
    autoRetryLimit: Optional[int] = None


class EnvironmentVariable(BaseValidatorModel):
    pass


class SourceAuth(BaseValidatorModel):
    pass


class ProjectCacheUnion(BaseValidatorModel):
    pass


class StartBuildInput(BaseValidatorModel):
    projectName: str
    secondarySourcesOverride: Optional[Sequence[ProjectSource]] = None
    secondarySourcesVersionOverride: Optional[Sequence[ProjectSourceVersion]] = None
    sourceVersion: Optional[str] = None
    artifactsOverride: Optional[ProjectArtifacts] = None
    secondaryArtifactsOverride: Optional[Sequence[ProjectArtifacts]] = None
    environmentVariablesOverride: Optional[Sequence[EnvironmentVariable]] = None
    sourceTypeOverride: Optional[SourceTypeType] = None
    sourceLocationOverride: Optional[str] = None
    sourceAuthOverride: Optional[SourceAuth] = None
    gitCloneDepthOverride: Optional[int] = None
    gitSubmodulesConfigOverride: Optional[GitSubmodulesConfig] = None
    buildspecOverride: Optional[str] = None
    insecureSslOverride: Optional[bool] = None
    reportBuildStatusOverride: Optional[bool] = None
    buildStatusConfigOverride: Optional[BuildStatusConfig] = None
    environmentTypeOverride: Optional[EnvironmentTypeType] = None
    imageOverride: Optional[str] = None
    computeTypeOverride: Optional[ComputeTypeType] = None
    certificateOverride: Optional[str] = None
    cacheOverride: Optional[ProjectCacheUnion] = None
    serviceRoleOverride: Optional[str] = None
    privilegedModeOverride: Optional[bool] = None
    timeoutInMinutesOverride: Optional[int] = None
    queuedTimeoutInMinutesOverride: Optional[int] = None
    encryptionKeyOverride: Optional[str] = None
    idempotencyToken: Optional[str] = None
    logsConfigOverride: Optional[LogsConfig] = None
    registryCredentialOverride: Optional[RegistryCredential] = None
    imagePullCredentialsTypeOverride: Optional[ImagePullCredentialsTypeType] = None
    debugSessionEnabled: Optional[bool] = None
    fleetOverride: Optional[ProjectFleet] = None
    autoRetryLimitOverride: Optional[int] = None


class UpdateReportGroupInput(BaseValidatorModel):
    arn: str
    exportConfig: Optional[ReportExportConfig] = None
    tags: Optional[Sequence[Tag]] = None


class ProjectBuildBatchConfigUnion(BaseValidatorModel):
    pass


class StartBuildBatchInput(BaseValidatorModel):
    projectName: str
    secondarySourcesOverride: Optional[Sequence[ProjectSource]] = None
    secondarySourcesVersionOverride: Optional[Sequence[ProjectSourceVersion]] = None
    sourceVersion: Optional[str] = None
    artifactsOverride: Optional[ProjectArtifacts] = None
    secondaryArtifactsOverride: Optional[Sequence[ProjectArtifacts]] = None
    environmentVariablesOverride: Optional[Sequence[EnvironmentVariable]] = None
    sourceTypeOverride: Optional[SourceTypeType] = None
    sourceLocationOverride: Optional[str] = None
    sourceAuthOverride: Optional[SourceAuth] = None
    gitCloneDepthOverride: Optional[int] = None
    gitSubmodulesConfigOverride: Optional[GitSubmodulesConfig] = None
    buildspecOverride: Optional[str] = None
    insecureSslOverride: Optional[bool] = None
    reportBuildBatchStatusOverride: Optional[bool] = None
    environmentTypeOverride: Optional[EnvironmentTypeType] = None
    imageOverride: Optional[str] = None
    computeTypeOverride: Optional[ComputeTypeType] = None
    certificateOverride: Optional[str] = None
    cacheOverride: Optional[ProjectCacheUnion] = None
    serviceRoleOverride: Optional[str] = None
    privilegedModeOverride: Optional[bool] = None
    buildTimeoutInMinutesOverride: Optional[int] = None
    queuedTimeoutInMinutesOverride: Optional[int] = None
    encryptionKeyOverride: Optional[str] = None
    idempotencyToken: Optional[str] = None
    logsConfigOverride: Optional[LogsConfig] = None
    registryCredentialOverride: Optional[RegistryCredential] = None
    imagePullCredentialsTypeOverride: Optional[ImagePullCredentialsTypeType] = None
    buildBatchConfigOverride: Optional[ProjectBuildBatchConfigUnion] = None
    debugSessionEnabled: Optional[bool] = None


class ListCuratedEnvironmentImagesOutput(BaseValidatorModel):
    platforms: List[EnvironmentPlatform]
    ResponseMetadata: ResponseMetadata


class ProxyConfigurationUnion(BaseValidatorModel):
    pass


class VpcConfigUnion(BaseValidatorModel):
    pass


class CreateFleetInput(BaseValidatorModel):
    name: str
    baseCapacity: int
    environmentType: EnvironmentTypeType
    computeType: ComputeTypeType
    computeConfiguration: Optional[ComputeConfiguration] = None
    scalingConfiguration: Optional[ScalingConfigurationInput] = None
    overflowBehavior: Optional[FleetOverflowBehaviorType] = None
    vpcConfig: Optional[VpcConfigUnion] = None
    proxyConfiguration: Optional[ProxyConfigurationUnion] = None
    imageId: Optional[str] = None
    fleetServiceRole: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class UpdateFleetInput(BaseValidatorModel):
    arn: str
    baseCapacity: Optional[int] = None
    environmentType: Optional[EnvironmentTypeType] = None
    computeType: Optional[ComputeTypeType] = None
    computeConfiguration: Optional[ComputeConfiguration] = None
    scalingConfiguration: Optional[ScalingConfigurationInput] = None
    overflowBehavior: Optional[FleetOverflowBehaviorType] = None
    vpcConfig: Optional[VpcConfigUnion] = None
    proxyConfiguration: Optional[ProxyConfigurationUnion] = None
    imageId: Optional[str] = None
    fleetServiceRole: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class ProjectEnvironmentUnion(BaseValidatorModel):
    pass


class CreateProjectInput(BaseValidatorModel):
    name: str
    source: ProjectSource
    artifacts: ProjectArtifacts
    environment: ProjectEnvironmentUnion
    serviceRole: str
    description: Optional[str] = None
    secondarySources: Optional[Sequence[ProjectSource]] = None
    sourceVersion: Optional[str] = None
    secondarySourceVersions: Optional[Sequence[ProjectSourceVersion]] = None
    secondaryArtifacts: Optional[Sequence[ProjectArtifacts]] = None
    cache: Optional[ProjectCacheUnion] = None
    timeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    vpcConfig: Optional[VpcConfigUnion] = None
    badgeEnabled: Optional[bool] = None
    logsConfig: Optional[LogsConfig] = None
    fileSystemLocations: Optional[Sequence[ProjectFileSystemLocation]] = None
    buildBatchConfig: Optional[ProjectBuildBatchConfigUnion] = None
    concurrentBuildLimit: Optional[int] = None
    autoRetryLimit: Optional[int] = None


class UpdateProjectInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    source: Optional[ProjectSource] = None
    secondarySources: Optional[Sequence[ProjectSource]] = None
    sourceVersion: Optional[str] = None
    secondarySourceVersions: Optional[Sequence[ProjectSourceVersion]] = None
    artifacts: Optional[ProjectArtifacts] = None
    secondaryArtifacts: Optional[Sequence[ProjectArtifacts]] = None
    cache: Optional[ProjectCacheUnion] = None
    environment: Optional[ProjectEnvironmentUnion] = None
    serviceRole: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    vpcConfig: Optional[VpcConfigUnion] = None
    badgeEnabled: Optional[bool] = None
    logsConfig: Optional[LogsConfig] = None
    fileSystemLocations: Optional[Sequence[ProjectFileSystemLocation]] = None
    buildBatchConfig: Optional[ProjectBuildBatchConfigUnion] = None
    concurrentBuildLimit: Optional[int] = None
    autoRetryLimit: Optional[int] = None


class Build(BaseValidatorModel):
    pass


class BatchGetBuildsOutput(BaseValidatorModel):
    builds: List[Build]
    buildsNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class RetryBuildOutput(BaseValidatorModel):
    build: Build
    ResponseMetadata: ResponseMetadata


class StartBuildOutput(BaseValidatorModel):
    build: Build
    ResponseMetadata: ResponseMetadata


class StopBuildOutput(BaseValidatorModel):
    build: Build
    ResponseMetadata: ResponseMetadata


class BatchGetProjectsOutput(BaseValidatorModel):
    projects: List[Project]
    projectsNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class CreateProjectOutput(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class UpdateProjectOutput(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class ReportGroup(BaseValidatorModel):
    pass


class BatchGetReportGroupsOutput(BaseValidatorModel):
    reportGroups: List[ReportGroup]
    reportGroupsNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class CreateReportGroupOutput(BaseValidatorModel):
    reportGroup: ReportGroup
    ResponseMetadata: ResponseMetadata


class UpdateReportGroupOutput(BaseValidatorModel):
    reportGroup: ReportGroup
    ResponseMetadata: ResponseMetadata


class Report(BaseValidatorModel):
    pass


class BatchGetReportsOutput(BaseValidatorModel):
    reports: List[Report]
    reportsNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class Fleet(BaseValidatorModel):
    pass


class BatchGetFleetsOutput(BaseValidatorModel):
    fleets: List[Fleet]
    fleetsNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class CreateFleetOutput(BaseValidatorModel):
    fleet: Fleet
    ResponseMetadata: ResponseMetadata


class UpdateFleetOutput(BaseValidatorModel):
    fleet: Fleet
    ResponseMetadata: ResponseMetadata


class BuildBatch(BaseValidatorModel):
    pass


class BatchGetBuildBatchesOutput(BaseValidatorModel):
    buildBatches: List[BuildBatch]
    buildBatchesNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class RetryBuildBatchOutput(BaseValidatorModel):
    buildBatch: BuildBatch
    ResponseMetadata: ResponseMetadata


class StartBuildBatchOutput(BaseValidatorModel):
    buildBatch: BuildBatch
    ResponseMetadata: ResponseMetadata


class StopBuildBatchOutput(BaseValidatorModel):
    buildBatch: BuildBatch
    ResponseMetadata: ResponseMetadata



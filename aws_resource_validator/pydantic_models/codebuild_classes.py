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

class AutoRetryConfigTypeDef(BaseValidatorModel):
    autoRetryLimit: Optional[int] = None
    autoRetryNumber: Optional[int] = None
    nextAutoRetry: Optional[str] = None
    previousAutoRetry: Optional[str] = None


class BatchDeleteBuildsInputTypeDef(BaseValidatorModel):
    ids: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetBuildBatchesInputTypeDef(BaseValidatorModel):
    ids: Sequence[str]


class BatchGetBuildsInputTypeDef(BaseValidatorModel):
    ids: Sequence[str]


class BatchGetFleetsInputTypeDef(BaseValidatorModel):
    names: Sequence[str]


class BatchGetProjectsInputTypeDef(BaseValidatorModel):
    names: Sequence[str]


class BatchGetReportGroupsInputTypeDef(BaseValidatorModel):
    reportGroupArns: Sequence[str]


class BatchGetReportsInputTypeDef(BaseValidatorModel):
    reportArns: Sequence[str]


class BatchRestrictionsOutputTypeDef(BaseValidatorModel):
    maximumBuildsAllowed: Optional[int] = None
    computeTypesAllowed: Optional[List[str]] = None
    fleetsAllowed: Optional[List[str]] = None


class BatchRestrictionsTypeDef(BaseValidatorModel):
    maximumBuildsAllowed: Optional[int] = None
    computeTypesAllowed: Optional[Sequence[str]] = None
    fleetsAllowed: Optional[Sequence[str]] = None


class BuildArtifactsTypeDef(BaseValidatorModel):
    location: Optional[str] = None
    sha256sum: Optional[str] = None
    md5sum: Optional[str] = None
    overrideArtifactName: Optional[bool] = None
    encryptionDisabled: Optional[bool] = None
    artifactIdentifier: Optional[str] = None
    bucketOwnerAccess: Optional[BucketOwnerAccessType] = None


class BuildBatchFilterTypeDef(BaseValidatorModel):
    status: Optional[StatusTypeType] = None


class PhaseContextTypeDef(BaseValidatorModel):
    statusCode: Optional[str] = None
    message: Optional[str] = None


class ProjectSourceVersionTypeDef(BaseValidatorModel):
    sourceIdentifier: str
    sourceVersion: str


class VpcConfigOutputTypeDef(BaseValidatorModel):
    vpcId: Optional[str] = None
    subnets: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None


class BuildStatusConfigTypeDef(BaseValidatorModel):
    context: Optional[str] = None
    targetUrl: Optional[str] = None


class DebugSessionTypeDef(BaseValidatorModel):
    sessionEnabled: Optional[bool] = None
    sessionTarget: Optional[str] = None


class ExportedEnvironmentVariableTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class NetworkInterfaceTypeDef(BaseValidatorModel):
    subnetId: Optional[str] = None
    networkInterfaceId: Optional[str] = None


class CloudWatchLogsConfigTypeDef(BaseValidatorModel):
    status: LogsConfigStatusTypeType
    groupName: Optional[str] = None
    streamName: Optional[str] = None


class CodeCoverageReportSummaryTypeDef(BaseValidatorModel):
    lineCoveragePercentage: Optional[float] = None
    linesCovered: Optional[int] = None
    linesMissed: Optional[int] = None
    branchCoveragePercentage: Optional[float] = None
    branchesCovered: Optional[int] = None
    branchesMissed: Optional[int] = None


class ComputeConfigurationTypeDef(BaseValidatorModel):
    vCpu: Optional[int] = None
    memory: Optional[int] = None
    disk: Optional[int] = None
    machineType: Optional[MachineTypeType] = None


class TagTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ScopeConfigurationTypeDef(BaseValidatorModel):
    name: str
    scope: WebhookScopeTypeType
    domain: Optional[str] = None


class DeleteFleetInputTypeDef(BaseValidatorModel):
    arn: str


class DeleteProjectInputTypeDef(BaseValidatorModel):
    name: str


class DeleteReportGroupInputTypeDef(BaseValidatorModel):
    arn: str
    deleteReports: Optional[bool] = None


class DeleteReportInputTypeDef(BaseValidatorModel):
    arn: str


class DeleteResourcePolicyInputTypeDef(BaseValidatorModel):
    resourceArn: str


class DeleteSourceCredentialsInputTypeDef(BaseValidatorModel):
    arn: str


class DeleteWebhookInputTypeDef(BaseValidatorModel):
    projectName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeCodeCoveragesInputTypeDef(BaseValidatorModel):
    reportArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportCodeCoverageSortByTypeType] = None
    minLineCoveragePercentage: Optional[float] = None
    maxLineCoveragePercentage: Optional[float] = None


class TestCaseFilterTypeDef(BaseValidatorModel):
    status: Optional[str] = None
    keyword: Optional[str] = None


class TestCaseTypeDef(BaseValidatorModel):
    reportArn: Optional[str] = None
    testRawDataPath: Optional[str] = None
    prefix: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    durationInNanoSeconds: Optional[int] = None
    message: Optional[str] = None
    expired: Optional[datetime] = None
    testSuiteName: Optional[str] = None


class EnvironmentImageTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    versions: Optional[List[str]] = None


class FleetStatusTypeDef(BaseValidatorModel):
    statusCode: Optional[FleetStatusCodeType] = None
    context: Optional[FleetContextCodeType] = None
    message: Optional[str] = None


class GetReportGroupTrendInputTypeDef(BaseValidatorModel):
    reportGroupArn: str
    trendField: ReportGroupTrendFieldTypeType
    numOfReports: Optional[int] = None


class ReportWithRawDataTypeDef(BaseValidatorModel):
    reportArn: Optional[str] = None
    data: Optional[str] = None


class GetResourcePolicyInputTypeDef(BaseValidatorModel):
    resourceArn: str


class GitSubmodulesConfigTypeDef(BaseValidatorModel):
    fetchSubmodules: bool


class ImportSourceCredentialsInputTypeDef(BaseValidatorModel):
    token: str
    serverType: ServerTypeType
    authType: AuthTypeType
    username: Optional[str] = None
    shouldOverwrite: Optional[bool] = None


class InvalidateProjectCacheInputTypeDef(BaseValidatorModel):
    projectName: str


class ListBuildsForProjectInputTypeDef(BaseValidatorModel):
    projectName: str
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None


class ListBuildsInputTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None


class ListFleetsInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[FleetSortByTypeType] = None


class ListProjectsInputTypeDef(BaseValidatorModel):
    sortBy: Optional[ProjectSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None


class ListReportGroupsInputTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportGroupSortByTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ReportFilterTypeDef(BaseValidatorModel):
    status: Optional[ReportStatusTypeType] = None


class ListSharedProjectsInputTypeDef(BaseValidatorModel):
    sortBy: Optional[SharedResourceSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSharedReportGroupsInputTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[SharedResourceSortByTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SourceCredentialsInfoTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    serverType: Optional[ServerTypeType] = None
    authType: Optional[AuthTypeType] = None
    resource: Optional[str] = None


class S3LogsConfigTypeDef(BaseValidatorModel):
    status: LogsConfigStatusTypeType
    location: Optional[str] = None
    encryptionDisabled: Optional[bool] = None
    bucketOwnerAccess: Optional[BucketOwnerAccessType] = None


class ProjectBadgeTypeDef(BaseValidatorModel):
    badgeEnabled: Optional[bool] = None
    badgeRequestUrl: Optional[str] = None


class ProjectFleetTypeDef(BaseValidatorModel):
    fleetArn: Optional[str] = None


class RegistryCredentialTypeDef(BaseValidatorModel):
    credential: str
    credentialProvider: Literal["SECRETS_MANAGER"]


class PutResourcePolicyInputTypeDef(BaseValidatorModel):
    policy: str
    resourceArn: str


class S3ReportExportConfigTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    bucketOwner: Optional[str] = None
    path: Optional[str] = None
    packaging: Optional[ReportPackagingTypeType] = None
    encryptionKey: Optional[str] = None
    encryptionDisabled: Optional[bool] = None


class TestReportSummaryTypeDef(BaseValidatorModel):
    total: int
    statusCounts: Dict[str, int]
    durationInNanoSeconds: int


class TargetTrackingScalingConfigurationTypeDef(BaseValidatorModel):
    metricType: Optional[Literal["FLEET_UTILIZATION_RATE"]] = None
    targetValue: Optional[float] = None


class UpdateProjectVisibilityInputTypeDef(BaseValidatorModel):
    projectArn: str
    projectVisibility: ProjectVisibilityTypeType
    resourceAccessRole: Optional[str] = None


class VpcConfigTypeDef(BaseValidatorModel):
    vpcId: Optional[str] = None
    subnets: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None


class BuildNotDeletedTypeDef(BaseValidatorModel):
    pass


class BatchDeleteBuildsOutputTypeDef(BaseValidatorModel):
    buildsDeleted: List[str]
    buildsNotDeleted: List[BuildNotDeletedTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBuildBatchOutputTypeDef(BaseValidatorModel):
    statusCode: str
    buildsDeleted: List[str]
    buildsNotDeleted: List[BuildNotDeletedTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSourceCredentialsOutputTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyOutputTypeDef(BaseValidatorModel):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportSourceCredentialsOutputTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListBuildBatchesForProjectOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListBuildBatchesOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListBuildsForProjectOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListBuildsOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListFleetsOutputTypeDef(BaseValidatorModel):
    fleets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListProjectsOutputTypeDef(BaseValidatorModel):
    projects: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListReportGroupsOutputTypeDef(BaseValidatorModel):
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListReportsForReportGroupOutputTypeDef(BaseValidatorModel):
    reports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListReportsOutputTypeDef(BaseValidatorModel):
    reports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSharedProjectsOutputTypeDef(BaseValidatorModel):
    projects: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSharedReportGroupsOutputTypeDef(BaseValidatorModel):
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutResourcePolicyOutputTypeDef(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProjectVisibilityOutputTypeDef(BaseValidatorModel):
    projectArn: str
    publicProjectAlias: str
    projectVisibility: ProjectVisibilityTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class ProjectBuildBatchConfigOutputTypeDef(BaseValidatorModel):
    serviceRole: Optional[str] = None
    combineArtifacts: Optional[bool] = None
    restrictions: Optional[BatchRestrictionsOutputTypeDef] = None
    timeoutInMins: Optional[int] = None
    batchReportMode: Optional[BatchReportModeTypeType] = None


class ProjectBuildBatchConfigTypeDef(BaseValidatorModel):
    serviceRole: Optional[str] = None
    combineArtifacts: Optional[bool] = None
    restrictions: Optional[BatchRestrictionsTypeDef] = None
    timeoutInMins: Optional[int] = None
    batchReportMode: Optional[BatchReportModeTypeType] = None


class BuildBatchPhaseTypeDef(BaseValidatorModel):
    phaseType: Optional[BuildBatchPhaseTypeType] = None
    phaseStatus: Optional[StatusTypeType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    durationInSeconds: Optional[int] = None
    contexts: Optional[List[PhaseContextTypeDef]] = None


class BuildPhaseTypeDef(BaseValidatorModel):
    phaseType: Optional[BuildPhaseTypeType] = None
    phaseStatus: Optional[StatusTypeType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    durationInSeconds: Optional[int] = None
    contexts: Optional[List[PhaseContextTypeDef]] = None


class ResolvedArtifactTypeDef(BaseValidatorModel):
    pass


class BuildSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    requestedOn: Optional[datetime] = None
    buildStatus: Optional[StatusTypeType] = None
    primaryArtifact: Optional[ResolvedArtifactTypeDef] = None
    secondaryArtifacts: Optional[List[ResolvedArtifactTypeDef]] = None


class CodeCoverageTypeDef(BaseValidatorModel):
    pass


class DescribeCodeCoveragesOutputTypeDef(BaseValidatorModel):
    codeCoverages: List[CodeCoverageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WebhookFilterTypeDef(BaseValidatorModel):
    pass


class CreateWebhookInputTypeDef(BaseValidatorModel):
    projectName: str
    branchFilter: Optional[str] = None
    filterGroups: Optional[Sequence[Sequence[WebhookFilterTypeDef]]] = None
    buildType: Optional[WebhookBuildTypeType] = None
    manualCreation: Optional[bool] = None
    scopeConfiguration: Optional[ScopeConfigurationTypeDef] = None


class UpdateWebhookInputTypeDef(BaseValidatorModel):
    projectName: str
    branchFilter: Optional[str] = None
    rotateSecret: Optional[bool] = None
    filterGroups: Optional[Sequence[Sequence[WebhookFilterTypeDef]]] = None
    buildType: Optional[WebhookBuildTypeType] = None


class WebhookTypeDef(BaseValidatorModel):
    url: Optional[str] = None
    payloadUrl: Optional[str] = None
    secret: Optional[str] = None
    branchFilter: Optional[str] = None
    filterGroups: Optional[List[List[WebhookFilterTypeDef]]] = None
    buildType: Optional[WebhookBuildTypeType] = None
    manualCreation: Optional[bool] = None
    lastModifiedSecret: Optional[datetime] = None
    scopeConfiguration: Optional[ScopeConfigurationTypeDef] = None
    status: Optional[WebhookStatusType] = None
    statusMessage: Optional[str] = None


class DescribeCodeCoveragesInputPaginateTypeDef(BaseValidatorModel):
    reportArn: str
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportCodeCoverageSortByTypeType] = None
    minLineCoveragePercentage: Optional[float] = None
    maxLineCoveragePercentage: Optional[float] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBuildsForProjectInputPaginateTypeDef(BaseValidatorModel):
    projectName: str
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBuildsInputPaginateTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsInputPaginateTypeDef(BaseValidatorModel):
    sortBy: Optional[ProjectSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListReportGroupsInputPaginateTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportGroupSortByTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSharedProjectsInputPaginateTypeDef(BaseValidatorModel):
    sortBy: Optional[SharedResourceSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSharedReportGroupsInputPaginateTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[SharedResourceSortByTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeTestCasesOutputTypeDef(BaseValidatorModel):
    testCases: List[TestCaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EnvironmentLanguageTypeDef(BaseValidatorModel):
    language: Optional[LanguageTypeType] = None
    images: Optional[List[EnvironmentImageTypeDef]] = None


class FleetProxyRuleOutputTypeDef(BaseValidatorModel):
    pass


class ProxyConfigurationOutputTypeDef(BaseValidatorModel):
    defaultBehavior: Optional[FleetProxyRuleBehaviorType] = None
    orderedProxyRules: Optional[List[FleetProxyRuleOutputTypeDef]] = None


class FleetProxyRuleTypeDef(BaseValidatorModel):
    pass


class ProxyConfigurationTypeDef(BaseValidatorModel):
    defaultBehavior: Optional[FleetProxyRuleBehaviorType] = None
    orderedProxyRules: Optional[Sequence[FleetProxyRuleTypeDef]] = None


class ReportGroupTrendStatsTypeDef(BaseValidatorModel):
    pass


class GetReportGroupTrendOutputTypeDef(BaseValidatorModel):
    stats: ReportGroupTrendStatsTypeDef
    rawData: List[ReportWithRawDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListSourceCredentialsOutputTypeDef(BaseValidatorModel):
    sourceCredentialsInfos: List[SourceCredentialsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LogsConfigTypeDef(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsConfigTypeDef] = None
    s3Logs: Optional[S3LogsConfigTypeDef] = None


class LogsLocationTypeDef(BaseValidatorModel):
    groupName: Optional[str] = None
    streamName: Optional[str] = None
    deepLink: Optional[str] = None
    s3DeepLink: Optional[str] = None
    cloudWatchLogsArn: Optional[str] = None
    s3LogsArn: Optional[str] = None
    cloudWatchLogs: Optional[CloudWatchLogsConfigTypeDef] = None
    s3Logs: Optional[S3LogsConfigTypeDef] = None


class ReportExportConfigTypeDef(BaseValidatorModel):
    exportConfigType: Optional[ReportExportConfigTypeType] = None
    s3Destination: Optional[S3ReportExportConfigTypeDef] = None


class ScalingConfigurationInputTypeDef(BaseValidatorModel):
    scalingType: Optional[Literal["TARGET_TRACKING_SCALING"]] = None
    targetTrackingScalingConfigs: Optional[Sequence[TargetTrackingScalingConfigurationTypeDef]] = None
    maxCapacity: Optional[int] = None


class ScalingConfigurationOutputTypeDef(BaseValidatorModel):
    scalingType: Optional[Literal["TARGET_TRACKING_SCALING"]] = None
    targetTrackingScalingConfigs: Optional[List[TargetTrackingScalingConfigurationTypeDef]] = None
    maxCapacity: Optional[int] = None
    desiredCapacity: Optional[int] = None


class BuildGroupTypeDef(BaseValidatorModel):
    identifier: Optional[str] = None
    dependsOn: Optional[List[str]] = None
    ignoreFailure: Optional[bool] = None
    currentBuildSummary: Optional[BuildSummaryTypeDef] = None
    priorBuildSummaryList: Optional[List[BuildSummaryTypeDef]] = None


class CreateWebhookOutputTypeDef(BaseValidatorModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWebhookOutputTypeDef(BaseValidatorModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EnvironmentPlatformTypeDef(BaseValidatorModel):
    platform: Optional[PlatformTypeType] = None
    languages: Optional[List[EnvironmentLanguageTypeDef]] = None


class ProjectSourceTypeDef(BaseValidatorModel):
    pass


class ProjectEnvironmentOutputTypeDef(BaseValidatorModel):
    pass


class ProjectCacheOutputTypeDef(BaseValidatorModel):
    pass


class ProjectArtifactsTypeDef(BaseValidatorModel):
    pass


class ProjectFileSystemLocationTypeDef(BaseValidatorModel):
    pass


class ProjectTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    source: Optional[ProjectSourceTypeDef] = None
    secondarySources: Optional[List[ProjectSourceTypeDef]] = None
    sourceVersion: Optional[str] = None
    secondarySourceVersions: Optional[List[ProjectSourceVersionTypeDef]] = None
    artifacts: Optional[ProjectArtifactsTypeDef] = None
    secondaryArtifacts: Optional[List[ProjectArtifactsTypeDef]] = None
    cache: Optional[ProjectCacheOutputTypeDef] = None
    environment: Optional[ProjectEnvironmentOutputTypeDef] = None
    serviceRole: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    encryptionKey: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None
    created: Optional[datetime] = None
    lastModified: Optional[datetime] = None
    webhook: Optional[WebhookTypeDef] = None
    vpcConfig: Optional[VpcConfigOutputTypeDef] = None
    badge: Optional[ProjectBadgeTypeDef] = None
    logsConfig: Optional[LogsConfigTypeDef] = None
    fileSystemLocations: Optional[List[ProjectFileSystemLocationTypeDef]] = None
    buildBatchConfig: Optional[ProjectBuildBatchConfigOutputTypeDef] = None
    concurrentBuildLimit: Optional[int] = None
    projectVisibility: Optional[ProjectVisibilityTypeType] = None
    publicProjectAlias: Optional[str] = None
    resourceAccessRole: Optional[str] = None
    autoRetryLimit: Optional[int] = None


class EnvironmentVariableTypeDef(BaseValidatorModel):
    pass


class SourceAuthTypeDef(BaseValidatorModel):
    pass


class ProjectCacheUnionTypeDef(BaseValidatorModel):
    pass


class StartBuildInputTypeDef(BaseValidatorModel):
    projectName: str
    secondarySourcesOverride: Optional[Sequence[ProjectSourceTypeDef]] = None
    secondarySourcesVersionOverride: Optional[Sequence[ProjectSourceVersionTypeDef]] = None
    sourceVersion: Optional[str] = None
    artifactsOverride: Optional[ProjectArtifactsTypeDef] = None
    secondaryArtifactsOverride: Optional[Sequence[ProjectArtifactsTypeDef]] = None
    environmentVariablesOverride: Optional[Sequence[EnvironmentVariableTypeDef]] = None
    sourceTypeOverride: Optional[SourceTypeType] = None
    sourceLocationOverride: Optional[str] = None
    sourceAuthOverride: Optional[SourceAuthTypeDef] = None
    gitCloneDepthOverride: Optional[int] = None
    gitSubmodulesConfigOverride: Optional[GitSubmodulesConfigTypeDef] = None
    buildspecOverride: Optional[str] = None
    insecureSslOverride: Optional[bool] = None
    reportBuildStatusOverride: Optional[bool] = None
    buildStatusConfigOverride: Optional[BuildStatusConfigTypeDef] = None
    environmentTypeOverride: Optional[EnvironmentTypeType] = None
    imageOverride: Optional[str] = None
    computeTypeOverride: Optional[ComputeTypeType] = None
    certificateOverride: Optional[str] = None
    cacheOverride: Optional[ProjectCacheUnionTypeDef] = None
    serviceRoleOverride: Optional[str] = None
    privilegedModeOverride: Optional[bool] = None
    timeoutInMinutesOverride: Optional[int] = None
    queuedTimeoutInMinutesOverride: Optional[int] = None
    encryptionKeyOverride: Optional[str] = None
    idempotencyToken: Optional[str] = None
    logsConfigOverride: Optional[LogsConfigTypeDef] = None
    registryCredentialOverride: Optional[RegistryCredentialTypeDef] = None
    imagePullCredentialsTypeOverride: Optional[ImagePullCredentialsTypeType] = None
    debugSessionEnabled: Optional[bool] = None
    fleetOverride: Optional[ProjectFleetTypeDef] = None
    autoRetryLimitOverride: Optional[int] = None


class UpdateReportGroupInputTypeDef(BaseValidatorModel):
    arn: str
    exportConfig: Optional[ReportExportConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ProjectBuildBatchConfigUnionTypeDef(BaseValidatorModel):
    pass


class StartBuildBatchInputTypeDef(BaseValidatorModel):
    projectName: str
    secondarySourcesOverride: Optional[Sequence[ProjectSourceTypeDef]] = None
    secondarySourcesVersionOverride: Optional[Sequence[ProjectSourceVersionTypeDef]] = None
    sourceVersion: Optional[str] = None
    artifactsOverride: Optional[ProjectArtifactsTypeDef] = None
    secondaryArtifactsOverride: Optional[Sequence[ProjectArtifactsTypeDef]] = None
    environmentVariablesOverride: Optional[Sequence[EnvironmentVariableTypeDef]] = None
    sourceTypeOverride: Optional[SourceTypeType] = None
    sourceLocationOverride: Optional[str] = None
    sourceAuthOverride: Optional[SourceAuthTypeDef] = None
    gitCloneDepthOverride: Optional[int] = None
    gitSubmodulesConfigOverride: Optional[GitSubmodulesConfigTypeDef] = None
    buildspecOverride: Optional[str] = None
    insecureSslOverride: Optional[bool] = None
    reportBuildBatchStatusOverride: Optional[bool] = None
    environmentTypeOverride: Optional[EnvironmentTypeType] = None
    imageOverride: Optional[str] = None
    computeTypeOverride: Optional[ComputeTypeType] = None
    certificateOverride: Optional[str] = None
    cacheOverride: Optional[ProjectCacheUnionTypeDef] = None
    serviceRoleOverride: Optional[str] = None
    privilegedModeOverride: Optional[bool] = None
    buildTimeoutInMinutesOverride: Optional[int] = None
    queuedTimeoutInMinutesOverride: Optional[int] = None
    encryptionKeyOverride: Optional[str] = None
    idempotencyToken: Optional[str] = None
    logsConfigOverride: Optional[LogsConfigTypeDef] = None
    registryCredentialOverride: Optional[RegistryCredentialTypeDef] = None
    imagePullCredentialsTypeOverride: Optional[ImagePullCredentialsTypeType] = None
    buildBatchConfigOverride: Optional[ProjectBuildBatchConfigUnionTypeDef] = None
    debugSessionEnabled: Optional[bool] = None


class ListCuratedEnvironmentImagesOutputTypeDef(BaseValidatorModel):
    platforms: List[EnvironmentPlatformTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ProxyConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class VpcConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateFleetInputTypeDef(BaseValidatorModel):
    name: str
    baseCapacity: int
    environmentType: EnvironmentTypeType
    computeType: ComputeTypeType
    computeConfiguration: Optional[ComputeConfigurationTypeDef] = None
    scalingConfiguration: Optional[ScalingConfigurationInputTypeDef] = None
    overflowBehavior: Optional[FleetOverflowBehaviorType] = None
    vpcConfig: Optional[VpcConfigUnionTypeDef] = None
    proxyConfiguration: Optional[ProxyConfigurationUnionTypeDef] = None
    imageId: Optional[str] = None
    fleetServiceRole: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateFleetInputTypeDef(BaseValidatorModel):
    arn: str
    baseCapacity: Optional[int] = None
    environmentType: Optional[EnvironmentTypeType] = None
    computeType: Optional[ComputeTypeType] = None
    computeConfiguration: Optional[ComputeConfigurationTypeDef] = None
    scalingConfiguration: Optional[ScalingConfigurationInputTypeDef] = None
    overflowBehavior: Optional[FleetOverflowBehaviorType] = None
    vpcConfig: Optional[VpcConfigUnionTypeDef] = None
    proxyConfiguration: Optional[ProxyConfigurationUnionTypeDef] = None
    imageId: Optional[str] = None
    fleetServiceRole: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ProjectEnvironmentUnionTypeDef(BaseValidatorModel):
    pass


class CreateProjectInputTypeDef(BaseValidatorModel):
    name: str
    source: ProjectSourceTypeDef
    artifacts: ProjectArtifactsTypeDef
    environment: ProjectEnvironmentUnionTypeDef
    serviceRole: str
    description: Optional[str] = None
    secondarySources: Optional[Sequence[ProjectSourceTypeDef]] = None
    sourceVersion: Optional[str] = None
    secondarySourceVersions: Optional[Sequence[ProjectSourceVersionTypeDef]] = None
    secondaryArtifacts: Optional[Sequence[ProjectArtifactsTypeDef]] = None
    cache: Optional[ProjectCacheUnionTypeDef] = None
    timeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    vpcConfig: Optional[VpcConfigUnionTypeDef] = None
    badgeEnabled: Optional[bool] = None
    logsConfig: Optional[LogsConfigTypeDef] = None
    fileSystemLocations: Optional[Sequence[ProjectFileSystemLocationTypeDef]] = None
    buildBatchConfig: Optional[ProjectBuildBatchConfigUnionTypeDef] = None
    concurrentBuildLimit: Optional[int] = None
    autoRetryLimit: Optional[int] = None


class UpdateProjectInputTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    source: Optional[ProjectSourceTypeDef] = None
    secondarySources: Optional[Sequence[ProjectSourceTypeDef]] = None
    sourceVersion: Optional[str] = None
    secondarySourceVersions: Optional[Sequence[ProjectSourceVersionTypeDef]] = None
    artifacts: Optional[ProjectArtifactsTypeDef] = None
    secondaryArtifacts: Optional[Sequence[ProjectArtifactsTypeDef]] = None
    cache: Optional[ProjectCacheUnionTypeDef] = None
    environment: Optional[ProjectEnvironmentUnionTypeDef] = None
    serviceRole: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    vpcConfig: Optional[VpcConfigUnionTypeDef] = None
    badgeEnabled: Optional[bool] = None
    logsConfig: Optional[LogsConfigTypeDef] = None
    fileSystemLocations: Optional[Sequence[ProjectFileSystemLocationTypeDef]] = None
    buildBatchConfig: Optional[ProjectBuildBatchConfigUnionTypeDef] = None
    concurrentBuildLimit: Optional[int] = None
    autoRetryLimit: Optional[int] = None


class BuildTypeDef(BaseValidatorModel):
    pass


class BatchGetBuildsOutputTypeDef(BaseValidatorModel):
    builds: List[BuildTypeDef]
    buildsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class RetryBuildOutputTypeDef(BaseValidatorModel):
    build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartBuildOutputTypeDef(BaseValidatorModel):
    build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopBuildOutputTypeDef(BaseValidatorModel):
    build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetProjectsOutputTypeDef(BaseValidatorModel):
    projects: List[ProjectTypeDef]
    projectsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProjectOutputTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProjectOutputTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReportGroupTypeDef(BaseValidatorModel):
    pass


class BatchGetReportGroupsOutputTypeDef(BaseValidatorModel):
    reportGroups: List[ReportGroupTypeDef]
    reportGroupsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateReportGroupOutputTypeDef(BaseValidatorModel):
    reportGroup: ReportGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateReportGroupOutputTypeDef(BaseValidatorModel):
    reportGroup: ReportGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReportTypeDef(BaseValidatorModel):
    pass


class BatchGetReportsOutputTypeDef(BaseValidatorModel):
    reports: List[ReportTypeDef]
    reportsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class FleetTypeDef(BaseValidatorModel):
    pass


class BatchGetFleetsOutputTypeDef(BaseValidatorModel):
    fleets: List[FleetTypeDef]
    fleetsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFleetOutputTypeDef(BaseValidatorModel):
    fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFleetOutputTypeDef(BaseValidatorModel):
    fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BuildBatchTypeDef(BaseValidatorModel):
    pass


class BatchGetBuildBatchesOutputTypeDef(BaseValidatorModel):
    buildBatches: List[BuildBatchTypeDef]
    buildBatchesNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class RetryBuildBatchOutputTypeDef(BaseValidatorModel):
    buildBatch: BuildBatchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartBuildBatchOutputTypeDef(BaseValidatorModel):
    buildBatch: BuildBatchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopBuildBatchOutputTypeDef(BaseValidatorModel):
    buildBatch: BuildBatchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



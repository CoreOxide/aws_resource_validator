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
from aws_resource_validator.pydantic_models.codebuild_constants import *

class BatchDeleteBuildsInputRequestTypeDef(BaseModel):
    ids: Sequence[str]

class BuildNotDeletedTypeDef(BaseModel):
    id: Optional[str] = None
    statusCode: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchGetBuildBatchesInputRequestTypeDef(BaseModel):
    ids: Sequence[str]

class BatchGetBuildsInputRequestTypeDef(BaseModel):
    ids: Sequence[str]

class BatchGetFleetsInputRequestTypeDef(BaseModel):
    names: Sequence[str]

class BatchGetProjectsInputRequestTypeDef(BaseModel):
    names: Sequence[str]

class BatchGetReportGroupsInputRequestTypeDef(BaseModel):
    reportGroupArns: Sequence[str]

class BatchGetReportsInputRequestTypeDef(BaseModel):
    reportArns: Sequence[str]

class BatchRestrictionsOutputTypeDef(BaseModel):
    maximumBuildsAllowed: Optional[int] = None
    computeTypesAllowed: Optional[List[str]] = None

class BatchRestrictionsTypeDef(BaseModel):
    maximumBuildsAllowed: Optional[int] = None
    computeTypesAllowed: Optional[Sequence[str]] = None

class BuildArtifactsTypeDef(BaseModel):
    location: Optional[str] = None
    sha256sum: Optional[str] = None
    md5sum: Optional[str] = None
    overrideArtifactName: Optional[bool] = None
    encryptionDisabled: Optional[bool] = None
    artifactIdentifier: Optional[str] = None
    bucketOwnerAccess: Optional[BucketOwnerAccessType] = None

class BuildBatchFilterTypeDef(BaseModel):
    status: Optional[StatusTypeType] = None

class PhaseContextTypeDef(BaseModel):
    statusCode: Optional[str] = None
    message: Optional[str] = None

class ProjectCacheOutputTypeDef(BaseModel):
    type: CacheTypeType
    location: Optional[str] = None
    modes: Optional[List[CacheModeType]] = None

class ProjectFileSystemLocationTypeDef(BaseModel):
    type: Optional[Literal["EFS"]] = None
    location: Optional[str] = None
    mountPoint: Optional[str] = None
    identifier: Optional[str] = None
    mountOptions: Optional[str] = None

class ProjectSourceVersionTypeDef(BaseModel):
    sourceIdentifier: str
    sourceVersion: str

class VpcConfigOutputTypeDef(BaseModel):
    vpcId: Optional[str] = None
    subnets: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None

class BuildStatusConfigTypeDef(BaseModel):
    context: Optional[str] = None
    targetUrl: Optional[str] = None

class ResolvedArtifactTypeDef(BaseModel):
    type: Optional[ArtifactsTypeType] = None
    location: Optional[str] = None
    identifier: Optional[str] = None

class DebugSessionTypeDef(BaseModel):
    sessionEnabled: Optional[bool] = None
    sessionTarget: Optional[str] = None

class ExportedEnvironmentVariableTypeDef(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class NetworkInterfaceTypeDef(BaseModel):
    subnetId: Optional[str] = None
    networkInterfaceId: Optional[str] = None

class CloudWatchLogsConfigTypeDef(BaseModel):
    status: LogsConfigStatusTypeType
    groupName: Optional[str] = None
    streamName: Optional[str] = None

class CodeCoverageReportSummaryTypeDef(BaseModel):
    lineCoveragePercentage: Optional[float] = None
    linesCovered: Optional[int] = None
    linesMissed: Optional[int] = None
    branchCoveragePercentage: Optional[float] = None
    branchesCovered: Optional[int] = None
    branchesMissed: Optional[int] = None

class CodeCoverageTypeDef(BaseModel):
    id: Optional[str] = None
    reportARN: Optional[str] = None
    filePath: Optional[str] = None
    lineCoveragePercentage: Optional[float] = None
    linesCovered: Optional[int] = None
    linesMissed: Optional[int] = None
    branchCoveragePercentage: Optional[float] = None
    branchesCovered: Optional[int] = None
    branchesMissed: Optional[int] = None
    expired: Optional[datetime] = None

class TagTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class VpcConfigTypeDef(BaseModel):
    vpcId: Optional[str] = None
    subnets: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None

class ProjectArtifactsTypeDef(BaseModel):
    type: ArtifactsTypeType
    location: Optional[str] = None
    path: Optional[str] = None
    namespaceType: Optional[ArtifactNamespaceType] = None
    name: Optional[str] = None
    packaging: Optional[ArtifactPackagingType] = None
    overrideArtifactName: Optional[bool] = None
    encryptionDisabled: Optional[bool] = None
    artifactIdentifier: Optional[str] = None
    bucketOwnerAccess: Optional[BucketOwnerAccessType] = None

class ProjectCacheTypeDef(BaseModel):
    type: CacheTypeType
    location: Optional[str] = None
    modes: Optional[Sequence[CacheModeType]] = None

class ScopeConfigurationTypeDef(BaseModel):
    name: str
    scope: WebhookScopeTypeType
    domain: Optional[str] = None

class WebhookFilterTypeDef(BaseModel):
    type: WebhookFilterTypeType
    pattern: str
    excludeMatchedPattern: Optional[bool] = None

class DeleteBuildBatchInputRequestTypeDef(BaseModel):
    id: str

class DeleteFleetInputRequestTypeDef(BaseModel):
    arn: str

class DeleteProjectInputRequestTypeDef(BaseModel):
    name: str

class DeleteReportGroupInputRequestTypeDef(BaseModel):
    arn: str
    deleteReports: Optional[bool] = None

class DeleteReportInputRequestTypeDef(BaseModel):
    arn: str

class DeleteResourcePolicyInputRequestTypeDef(BaseModel):
    resourceArn: str

class DeleteSourceCredentialsInputRequestTypeDef(BaseModel):
    arn: str

class DeleteWebhookInputRequestTypeDef(BaseModel):
    projectName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeCodeCoveragesInputRequestTypeDef(BaseModel):
    reportArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportCodeCoverageSortByTypeType] = None
    minLineCoveragePercentage: Optional[float] = None
    maxLineCoveragePercentage: Optional[float] = None

class TestCaseFilterTypeDef(BaseModel):
    status: Optional[str] = None
    keyword: Optional[str] = None

class TestCaseTypeDef(BaseModel):
    reportArn: Optional[str] = None
    testRawDataPath: Optional[str] = None
    prefix: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    durationInNanoSeconds: Optional[int] = None
    message: Optional[str] = None
    expired: Optional[datetime] = None

class EnvironmentImageTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    versions: Optional[List[str]] = None

class EnvironmentVariableTypeDef(BaseModel):
    name: str
    value: str
    type: Optional[EnvironmentVariableTypeType] = None

class FleetStatusTypeDef(BaseModel):
    statusCode: Optional[FleetStatusCodeType] = None
    context: Optional[FleetContextCodeType] = None
    message: Optional[str] = None

class GetReportGroupTrendInputRequestTypeDef(BaseModel):
    reportGroupArn: str
    trendField: ReportGroupTrendFieldTypeType
    numOfReports: Optional[int] = None

class ReportGroupTrendStatsTypeDef(BaseModel):
    average: Optional[str] = None
    max: Optional[str] = None
    min: Optional[str] = None

class ReportWithRawDataTypeDef(BaseModel):
    reportArn: Optional[str] = None
    data: Optional[str] = None

class GetResourcePolicyInputRequestTypeDef(BaseModel):
    resourceArn: str

class GitSubmodulesConfigTypeDef(BaseModel):
    fetchSubmodules: bool

class ImportSourceCredentialsInputRequestTypeDef(BaseModel):
    token: str
    serverType: ServerTypeType
    authType: AuthTypeType
    username: Optional[str] = None
    shouldOverwrite: Optional[bool] = None

class InvalidateProjectCacheInputRequestTypeDef(BaseModel):
    projectName: str

class ListBuildsForProjectInputRequestTypeDef(BaseModel):
    projectName: str
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

class ListBuildsInputRequestTypeDef(BaseModel):
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

class ListFleetsInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[FleetSortByTypeType] = None

class ListProjectsInputRequestTypeDef(BaseModel):
    sortBy: Optional[ProjectSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

class ListReportGroupsInputRequestTypeDef(BaseModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportGroupSortByTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ReportFilterTypeDef(BaseModel):
    status: Optional[ReportStatusTypeType] = None

class ListSharedProjectsInputRequestTypeDef(BaseModel):
    sortBy: Optional[SharedResourceSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSharedReportGroupsInputRequestTypeDef(BaseModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[SharedResourceSortByTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SourceCredentialsInfoTypeDef(BaseModel):
    arn: Optional[str] = None
    serverType: Optional[ServerTypeType] = None
    authType: Optional[AuthTypeType] = None
    resource: Optional[str] = None

class S3LogsConfigTypeDef(BaseModel):
    status: LogsConfigStatusTypeType
    location: Optional[str] = None
    encryptionDisabled: Optional[bool] = None
    bucketOwnerAccess: Optional[BucketOwnerAccessType] = None

class ProjectBadgeTypeDef(BaseModel):
    badgeEnabled: Optional[bool] = None
    badgeRequestUrl: Optional[str] = None

class ProjectFleetTypeDef(BaseModel):
    fleetArn: Optional[str] = None

class RegistryCredentialTypeDef(BaseModel):
    credential: str
    credentialProvider: Literal["SECRETS_MANAGER"]

class SourceAuthTypeDef(BaseModel):
    type: SourceAuthTypeType
    resource: Optional[str] = None

class PutResourcePolicyInputRequestTypeDef(BaseModel):
    policy: str
    resourceArn: str

class S3ReportExportConfigTypeDef(BaseModel):
    bucket: Optional[str] = None
    bucketOwner: Optional[str] = None
    path: Optional[str] = None
    packaging: Optional[ReportPackagingTypeType] = None
    encryptionKey: Optional[str] = None
    encryptionDisabled: Optional[bool] = None

class TestReportSummaryTypeDef(BaseModel):
    total: int
    statusCounts: Dict[str, int]
    durationInNanoSeconds: int

class RetryBuildBatchInputRequestTypeDef(BaseModel):
    id: Optional[str] = None
    idempotencyToken: Optional[str] = None
    retryType: Optional[RetryBuildBatchTypeType] = None

class RetryBuildInputRequestTypeDef(BaseModel):
    id: Optional[str] = None
    idempotencyToken: Optional[str] = None

class TargetTrackingScalingConfigurationTypeDef(BaseModel):
    metricType: Optional[Literal["FLEET_UTILIZATION_RATE"]] = None
    targetValue: Optional[float] = None

class StopBuildBatchInputRequestTypeDef(BaseModel):
    id: str

class StopBuildInputRequestTypeDef(BaseModel):
    id: str

class UpdateProjectVisibilityInputRequestTypeDef(BaseModel):
    projectArn: str
    projectVisibility: ProjectVisibilityTypeType
    resourceAccessRole: Optional[str] = None

class BatchDeleteBuildsOutputTypeDef(BaseModel):
    buildsDeleted: List[str]
    buildsNotDeleted: List[BuildNotDeletedTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBuildBatchOutputTypeDef(BaseModel):
    statusCode: str
    buildsDeleted: List[str]
    buildsNotDeleted: List[BuildNotDeletedTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSourceCredentialsOutputTypeDef(BaseModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyOutputTypeDef(BaseModel):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSourceCredentialsOutputTypeDef(BaseModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildBatchesForProjectOutputTypeDef(BaseModel):
    ids: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildBatchesOutputTypeDef(BaseModel):
    ids: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildsForProjectOutputTypeDef(BaseModel):
    ids: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildsOutputTypeDef(BaseModel):
    ids: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsOutputTypeDef(BaseModel):
    nextToken: str
    fleets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsOutputTypeDef(BaseModel):
    nextToken: str
    projects: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportGroupsOutputTypeDef(BaseModel):
    nextToken: str
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportsForReportGroupOutputTypeDef(BaseModel):
    nextToken: str
    reports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportsOutputTypeDef(BaseModel):
    nextToken: str
    reports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSharedProjectsOutputTypeDef(BaseModel):
    nextToken: str
    projects: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSharedReportGroupsOutputTypeDef(BaseModel):
    nextToken: str
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyOutputTypeDef(BaseModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectVisibilityOutputTypeDef(BaseModel):
    projectArn: str
    publicProjectAlias: str
    projectVisibility: ProjectVisibilityTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ProjectBuildBatchConfigOutputTypeDef(BaseModel):
    serviceRole: Optional[str] = None
    combineArtifacts: Optional[bool] = None
    restrictions: Optional[BatchRestrictionsOutputTypeDef] = None
    timeoutInMins: Optional[int] = None
    batchReportMode: Optional[BatchReportModeTypeType] = None

class ProjectBuildBatchConfigTypeDef(BaseModel):
    serviceRole: Optional[str] = None
    combineArtifacts: Optional[bool] = None
    restrictions: Optional[BatchRestrictionsTypeDef] = None
    timeoutInMins: Optional[int] = None
    batchReportMode: Optional[BatchReportModeTypeType] = None

class ListBuildBatchesForProjectInputRequestTypeDef(BaseModel):
    projectName: Optional[str] = None
    filter: Optional[BuildBatchFilterTypeDef] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

class ListBuildBatchesInputRequestTypeDef(BaseModel):
    filter: Optional[BuildBatchFilterTypeDef] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

class BuildBatchPhaseTypeDef(BaseModel):
    phaseType: Optional[BuildBatchPhaseTypeType] = None
    phaseStatus: Optional[StatusTypeType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    durationInSeconds: Optional[int] = None
    contexts: Optional[List[PhaseContextTypeDef]] = None

class BuildPhaseTypeDef(BaseModel):
    phaseType: Optional[BuildPhaseTypeType] = None
    phaseStatus: Optional[StatusTypeType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    durationInSeconds: Optional[int] = None
    contexts: Optional[List[PhaseContextTypeDef]] = None

class BuildSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    requestedOn: Optional[datetime] = None
    buildStatus: Optional[StatusTypeType] = None
    primaryArtifact: Optional[ResolvedArtifactTypeDef] = None
    secondaryArtifacts: Optional[List[ResolvedArtifactTypeDef]] = None

class DescribeCodeCoveragesOutputTypeDef(BaseModel):
    nextToken: str
    codeCoverages: List[CodeCoverageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWebhookInputRequestTypeDef(BaseModel):
    projectName: str
    branchFilter: Optional[str] = None
    filterGroups: Optional[Sequence[Sequence[WebhookFilterTypeDef]]] = None
    buildType: Optional[WebhookBuildTypeType] = None
    manualCreation: Optional[bool] = None
    scopeConfiguration: Optional[ScopeConfigurationTypeDef] = None

class UpdateWebhookInputRequestTypeDef(BaseModel):
    projectName: str
    branchFilter: Optional[str] = None
    rotateSecret: Optional[bool] = None
    filterGroups: Optional[Sequence[Sequence[WebhookFilterTypeDef]]] = None
    buildType: Optional[WebhookBuildTypeType] = None

class WebhookTypeDef(BaseModel):
    url: Optional[str] = None
    payloadUrl: Optional[str] = None
    secret: Optional[str] = None
    branchFilter: Optional[str] = None
    filterGroups: Optional[List[List[WebhookFilterTypeDef]]] = None
    buildType: Optional[WebhookBuildTypeType] = None
    manualCreation: Optional[bool] = None
    lastModifiedSecret: Optional[datetime] = None
    scopeConfiguration: Optional[ScopeConfigurationTypeDef] = None

class DescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef(BaseModel):
    reportArn: str
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportCodeCoverageSortByTypeType] = None
    minLineCoveragePercentage: Optional[float] = None
    maxLineCoveragePercentage: Optional[float] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildBatchesForProjectInputListBuildBatchesForProjectPaginateTypeDef(BaseModel):
    projectName: Optional[str] = None
    filter: Optional[BuildBatchFilterTypeDef] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildBatchesInputListBuildBatchesPaginateTypeDef(BaseModel):
    filter: Optional[BuildBatchFilterTypeDef] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildsForProjectInputListBuildsForProjectPaginateTypeDef(BaseModel):
    projectName: str
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildsInputListBuildsPaginateTypeDef(BaseModel):
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsInputListProjectsPaginateTypeDef(BaseModel):
    sortBy: Optional[ProjectSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportGroupsInputListReportGroupsPaginateTypeDef(BaseModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportGroupSortByTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSharedProjectsInputListSharedProjectsPaginateTypeDef(BaseModel):
    sortBy: Optional[SharedResourceSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSharedReportGroupsInputListSharedReportGroupsPaginateTypeDef(BaseModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[SharedResourceSortByTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTestCasesInputDescribeTestCasesPaginateTypeDef(BaseModel):
    reportArn: str
    filter: Optional[TestCaseFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTestCasesInputRequestTypeDef(BaseModel):
    reportArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[TestCaseFilterTypeDef] = None

class DescribeTestCasesOutputTypeDef(BaseModel):
    nextToken: str
    testCases: List[TestCaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentLanguageTypeDef(BaseModel):
    language: Optional[LanguageTypeType] = None
    images: Optional[List[EnvironmentImageTypeDef]] = None

class GetReportGroupTrendOutputTypeDef(BaseModel):
    stats: ReportGroupTrendStatsTypeDef
    rawData: List[ReportWithRawDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef(BaseModel):
    reportGroupArn: str
    sortOrder: Optional[SortOrderTypeType] = None
    filter: Optional[ReportFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportsForReportGroupInputRequestTypeDef(BaseModel):
    reportGroupArn: str
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderTypeType] = None
    maxResults: Optional[int] = None
    filter: Optional[ReportFilterTypeDef] = None

class ListReportsInputListReportsPaginateTypeDef(BaseModel):
    sortOrder: Optional[SortOrderTypeType] = None
    filter: Optional[ReportFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportsInputRequestTypeDef(BaseModel):
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ReportFilterTypeDef] = None

class ListSourceCredentialsOutputTypeDef(BaseModel):
    sourceCredentialsInfos: List[SourceCredentialsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LogsConfigTypeDef(BaseModel):
    cloudWatchLogs: Optional[CloudWatchLogsConfigTypeDef] = None
    s3Logs: Optional[S3LogsConfigTypeDef] = None

class LogsLocationTypeDef(BaseModel):
    groupName: Optional[str] = None
    streamName: Optional[str] = None
    deepLink: Optional[str] = None
    s3DeepLink: Optional[str] = None
    cloudWatchLogsArn: Optional[str] = None
    s3LogsArn: Optional[str] = None
    cloudWatchLogs: Optional[CloudWatchLogsConfigTypeDef] = None
    s3Logs: Optional[S3LogsConfigTypeDef] = None

class ProjectEnvironmentOutputTypeDef(BaseModel):
    type: EnvironmentTypeType
    image: str
    computeType: ComputeTypeType
    fleet: Optional[ProjectFleetTypeDef] = None
    environmentVariables: Optional[List[EnvironmentVariableTypeDef]] = None
    privilegedMode: Optional[bool] = None
    certificate: Optional[str] = None
    registryCredential: Optional[RegistryCredentialTypeDef] = None
    imagePullCredentialsType: Optional[ImagePullCredentialsTypeType] = None

class ProjectEnvironmentTypeDef(BaseModel):
    type: EnvironmentTypeType
    image: str
    computeType: ComputeTypeType
    fleet: Optional[ProjectFleetTypeDef] = None
    environmentVariables: Optional[Sequence[EnvironmentVariableTypeDef]] = None
    privilegedMode: Optional[bool] = None
    certificate: Optional[str] = None
    registryCredential: Optional[RegistryCredentialTypeDef] = None
    imagePullCredentialsType: Optional[ImagePullCredentialsTypeType] = None

class ProjectSourceTypeDef(BaseModel):
    type: SourceTypeType
    location: Optional[str] = None
    gitCloneDepth: Optional[int] = None
    gitSubmodulesConfig: Optional[GitSubmodulesConfigTypeDef] = None
    buildspec: Optional[str] = None
    auth: Optional[SourceAuthTypeDef] = None
    reportBuildStatus: Optional[bool] = None
    buildStatusConfig: Optional[BuildStatusConfigTypeDef] = None
    insecureSsl: Optional[bool] = None
    sourceIdentifier: Optional[str] = None

class ReportExportConfigTypeDef(BaseModel):
    exportConfigType: Optional[ReportExportConfigTypeType] = None
    s3Destination: Optional[S3ReportExportConfigTypeDef] = None

class ScalingConfigurationInputTypeDef(BaseModel):
    scalingType: Optional[Literal["TARGET_TRACKING_SCALING"]] = None
    targetTrackingScalingConfigs: Optional[       Sequence[TargetTrackingScalingConfigurationTypeDef]     ] = None
    maxCapacity: Optional[int] = None

class ScalingConfigurationOutputTypeDef(BaseModel):
    scalingType: Optional[Literal["TARGET_TRACKING_SCALING"]] = None
    targetTrackingScalingConfigs: Optional[       List[TargetTrackingScalingConfigurationTypeDef]     ] = None
    maxCapacity: Optional[int] = None
    desiredCapacity: Optional[int] = None

class BuildGroupTypeDef(BaseModel):
    identifier: Optional[str] = None
    dependsOn: Optional[List[str]] = None
    ignoreFailure: Optional[bool] = None
    currentBuildSummary: Optional[BuildSummaryTypeDef] = None
    priorBuildSummaryList: Optional[List[BuildSummaryTypeDef]] = None

class CreateWebhookOutputTypeDef(BaseModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebhookOutputTypeDef(BaseModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentPlatformTypeDef(BaseModel):
    platform: Optional[PlatformTypeType] = None
    languages: Optional[List[EnvironmentLanguageTypeDef]] = None

class BuildTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    buildNumber: Optional[int] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    currentPhase: Optional[str] = None
    buildStatus: Optional[StatusTypeType] = None
    sourceVersion: Optional[str] = None
    resolvedSourceVersion: Optional[str] = None
    projectName: Optional[str] = None
    phases: Optional[List[BuildPhaseTypeDef]] = None
    source: Optional[ProjectSourceTypeDef] = None
    secondarySources: Optional[List[ProjectSourceTypeDef]] = None
    secondarySourceVersions: Optional[List[ProjectSourceVersionTypeDef]] = None
    artifacts: Optional[BuildArtifactsTypeDef] = None
    secondaryArtifacts: Optional[List[BuildArtifactsTypeDef]] = None
    cache: Optional[ProjectCacheOutputTypeDef] = None
    environment: Optional[ProjectEnvironmentOutputTypeDef] = None
    serviceRole: Optional[str] = None
    logs: Optional[LogsLocationTypeDef] = None
    timeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    buildComplete: Optional[bool] = None
    initiator: Optional[str] = None
    vpcConfig: Optional[VpcConfigOutputTypeDef] = None
    networkInterface: Optional[NetworkInterfaceTypeDef] = None
    encryptionKey: Optional[str] = None
    exportedEnvironmentVariables: Optional[List[ExportedEnvironmentVariableTypeDef]] = None
    reportArns: Optional[List[str]] = None
    fileSystemLocations: Optional[List[ProjectFileSystemLocationTypeDef]] = None
    debugSession: Optional[DebugSessionTypeDef] = None
    buildBatchArn: Optional[str] = None

class CreateProjectInputRequestTypeDef(BaseModel):
    name: str
    source: ProjectSourceTypeDef
    artifacts: ProjectArtifactsTypeDef
    environment: ProjectEnvironmentTypeDef
    serviceRole: str
    description: Optional[str] = None
    secondarySources: Optional[Sequence[ProjectSourceTypeDef]] = None
    sourceVersion: Optional[str] = None
    secondarySourceVersions: Optional[Sequence[ProjectSourceVersionTypeDef]] = None
    secondaryArtifacts: Optional[Sequence[ProjectArtifactsTypeDef]] = None
    cache: Optional[ProjectCacheTypeDef] = None
    timeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None
    badgeEnabled: Optional[bool] = None
    logsConfig: Optional[LogsConfigTypeDef] = None
    fileSystemLocations: Optional[Sequence[ProjectFileSystemLocationTypeDef]] = None
    buildBatchConfig: Optional[ProjectBuildBatchConfigTypeDef] = None
    concurrentBuildLimit: Optional[int] = None

class ProjectTypeDef(BaseModel):
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

class StartBuildBatchInputRequestTypeDef(BaseModel):
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
    cacheOverride: Optional[ProjectCacheTypeDef] = None
    serviceRoleOverride: Optional[str] = None
    privilegedModeOverride: Optional[bool] = None
    buildTimeoutInMinutesOverride: Optional[int] = None
    queuedTimeoutInMinutesOverride: Optional[int] = None
    encryptionKeyOverride: Optional[str] = None
    idempotencyToken: Optional[str] = None
    logsConfigOverride: Optional[LogsConfigTypeDef] = None
    registryCredentialOverride: Optional[RegistryCredentialTypeDef] = None
    imagePullCredentialsTypeOverride: Optional[ImagePullCredentialsTypeType] = None
    buildBatchConfigOverride: Optional[ProjectBuildBatchConfigTypeDef] = None
    debugSessionEnabled: Optional[bool] = None

class StartBuildInputRequestTypeDef(BaseModel):
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
    cacheOverride: Optional[ProjectCacheTypeDef] = None
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

class UpdateProjectInputRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    source: Optional[ProjectSourceTypeDef] = None
    secondarySources: Optional[Sequence[ProjectSourceTypeDef]] = None
    sourceVersion: Optional[str] = None
    secondarySourceVersions: Optional[Sequence[ProjectSourceVersionTypeDef]] = None
    artifacts: Optional[ProjectArtifactsTypeDef] = None
    secondaryArtifacts: Optional[Sequence[ProjectArtifactsTypeDef]] = None
    cache: Optional[ProjectCacheTypeDef] = None
    environment: Optional[ProjectEnvironmentTypeDef] = None
    serviceRole: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None
    badgeEnabled: Optional[bool] = None
    logsConfig: Optional[LogsConfigTypeDef] = None
    fileSystemLocations: Optional[Sequence[ProjectFileSystemLocationTypeDef]] = None
    buildBatchConfig: Optional[ProjectBuildBatchConfigTypeDef] = None
    concurrentBuildLimit: Optional[int] = None

class CreateReportGroupInputRequestTypeDef(BaseModel):
    name: str
    type: ReportTypeType
    exportConfig: ReportExportConfigTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None

class ReportGroupTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[ReportTypeType] = None
    exportConfig: Optional[ReportExportConfigTypeDef] = None
    created: Optional[datetime] = None
    lastModified: Optional[datetime] = None
    tags: Optional[List[TagTypeDef]] = None
    status: Optional[ReportGroupStatusTypeType] = None

class ReportTypeDef(BaseModel):
    arn: Optional[str] = None
    type: Optional[ReportTypeType] = None
    name: Optional[str] = None
    reportGroupArn: Optional[str] = None
    executionId: Optional[str] = None
    status: Optional[ReportStatusTypeType] = None
    created: Optional[datetime] = None
    expired: Optional[datetime] = None
    exportConfig: Optional[ReportExportConfigTypeDef] = None
    truncated: Optional[bool] = None
    testSummary: Optional[TestReportSummaryTypeDef] = None
    codeCoverageSummary: Optional[CodeCoverageReportSummaryTypeDef] = None

class UpdateReportGroupInputRequestTypeDef(BaseModel):
    arn: str
    exportConfig: Optional[ReportExportConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateFleetInputRequestTypeDef(BaseModel):
    name: str
    baseCapacity: int
    environmentType: EnvironmentTypeType
    computeType: ComputeTypeType
    scalingConfiguration: Optional[ScalingConfigurationInputTypeDef] = None
    overflowBehavior: Optional[FleetOverflowBehaviorType] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None
    fleetServiceRole: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateFleetInputRequestTypeDef(BaseModel):
    arn: str
    baseCapacity: Optional[int] = None
    environmentType: Optional[EnvironmentTypeType] = None
    computeType: Optional[ComputeTypeType] = None
    scalingConfiguration: Optional[ScalingConfigurationInputTypeDef] = None
    overflowBehavior: Optional[FleetOverflowBehaviorType] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None
    fleetServiceRole: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class FleetTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    id: Optional[str] = None
    created: Optional[datetime] = None
    lastModified: Optional[datetime] = None
    status: Optional[FleetStatusTypeDef] = None
    baseCapacity: Optional[int] = None
    environmentType: Optional[EnvironmentTypeType] = None
    computeType: Optional[ComputeTypeType] = None
    scalingConfiguration: Optional[ScalingConfigurationOutputTypeDef] = None
    overflowBehavior: Optional[FleetOverflowBehaviorType] = None
    vpcConfig: Optional[VpcConfigOutputTypeDef] = None
    fleetServiceRole: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None

class BuildBatchTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    currentPhase: Optional[str] = None
    buildBatchStatus: Optional[StatusTypeType] = None
    sourceVersion: Optional[str] = None
    resolvedSourceVersion: Optional[str] = None
    projectName: Optional[str] = None
    phases: Optional[List[BuildBatchPhaseTypeDef]] = None
    source: Optional[ProjectSourceTypeDef] = None
    secondarySources: Optional[List[ProjectSourceTypeDef]] = None
    secondarySourceVersions: Optional[List[ProjectSourceVersionTypeDef]] = None
    artifacts: Optional[BuildArtifactsTypeDef] = None
    secondaryArtifacts: Optional[List[BuildArtifactsTypeDef]] = None
    cache: Optional[ProjectCacheOutputTypeDef] = None
    environment: Optional[ProjectEnvironmentOutputTypeDef] = None
    serviceRole: Optional[str] = None
    logConfig: Optional[LogsConfigTypeDef] = None
    buildTimeoutInMinutes: Optional[int] = None
    queuedTimeoutInMinutes: Optional[int] = None
    complete: Optional[bool] = None
    initiator: Optional[str] = None
    vpcConfig: Optional[VpcConfigOutputTypeDef] = None
    encryptionKey: Optional[str] = None
    buildBatchNumber: Optional[int] = None
    fileSystemLocations: Optional[List[ProjectFileSystemLocationTypeDef]] = None
    buildBatchConfig: Optional[ProjectBuildBatchConfigOutputTypeDef] = None
    buildGroups: Optional[List[BuildGroupTypeDef]] = None
    debugSessionEnabled: Optional[bool] = None

class ListCuratedEnvironmentImagesOutputTypeDef(BaseModel):
    platforms: List[EnvironmentPlatformTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetBuildsOutputTypeDef(BaseModel):
    builds: List[BuildTypeDef]
    buildsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RetryBuildOutputTypeDef(BaseModel):
    build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartBuildOutputTypeDef(BaseModel):
    build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopBuildOutputTypeDef(BaseModel):
    build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetProjectsOutputTypeDef(BaseModel):
    projects: List[ProjectTypeDef]
    projectsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectOutputTypeDef(BaseModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectOutputTypeDef(BaseModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetReportGroupsOutputTypeDef(BaseModel):
    reportGroups: List[ReportGroupTypeDef]
    reportGroupsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReportGroupOutputTypeDef(BaseModel):
    reportGroup: ReportGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReportGroupOutputTypeDef(BaseModel):
    reportGroup: ReportGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetReportsOutputTypeDef(BaseModel):
    reports: List[ReportTypeDef]
    reportsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetFleetsOutputTypeDef(BaseModel):
    fleets: List[FleetTypeDef]
    fleetsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetOutputTypeDef(BaseModel):
    fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetOutputTypeDef(BaseModel):
    fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetBuildBatchesOutputTypeDef(BaseModel):
    buildBatches: List[BuildBatchTypeDef]
    buildBatchesNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RetryBuildBatchOutputTypeDef(BaseModel):
    buildBatch: BuildBatchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartBuildBatchOutputTypeDef(BaseModel):
    buildBatch: BuildBatchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopBuildBatchOutputTypeDef(BaseModel):
    buildBatch: BuildBatchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


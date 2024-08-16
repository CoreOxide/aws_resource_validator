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
from aws_resource_validator.pydantic_models.codebuild_constants import *

class BatchDeleteBuildsInputRequestTypeDef(BaseValidatorModel):
    ids: Sequence[str]

class BuildNotDeletedTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    statusCode: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchGetBuildBatchesInputRequestTypeDef(BaseValidatorModel):
    ids: Sequence[str]

class BatchGetBuildsInputRequestTypeDef(BaseValidatorModel):
    ids: Sequence[str]

class BatchGetFleetsInputRequestTypeDef(BaseValidatorModel):
    names: Sequence[str]

class BatchGetProjectsInputRequestTypeDef(BaseValidatorModel):
    names: Sequence[str]

class BatchGetReportGroupsInputRequestTypeDef(BaseValidatorModel):
    reportGroupArns: Sequence[str]

class BatchGetReportsInputRequestTypeDef(BaseValidatorModel):
    reportArns: Sequence[str]

class BatchRestrictionsOutputTypeDef(BaseValidatorModel):
    maximumBuildsAllowed: Optional[int] = None
    computeTypesAllowed: Optional[List[str]] = None

class BatchRestrictionsTypeDef(BaseValidatorModel):
    maximumBuildsAllowed: Optional[int] = None
    computeTypesAllowed: Optional[Sequence[str]] = None

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

class ProjectCacheOutputTypeDef(BaseValidatorModel):
    type: CacheTypeType
    location: Optional[str] = None
    modes: Optional[List[CacheModeType]] = None

class ProjectFileSystemLocationTypeDef(BaseValidatorModel):
    type: Optional[Literal["EFS"]] = None
    location: Optional[str] = None
    mountPoint: Optional[str] = None
    identifier: Optional[str] = None
    mountOptions: Optional[str] = None

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

class ResolvedArtifactTypeDef(BaseValidatorModel):
    type: Optional[ArtifactsTypeType] = None
    location: Optional[str] = None
    identifier: Optional[str] = None

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

class CodeCoverageTypeDef(BaseValidatorModel):
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

class TagTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None

class VpcConfigTypeDef(BaseValidatorModel):
    vpcId: Optional[str] = None
    subnets: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None

class ProjectArtifactsTypeDef(BaseValidatorModel):
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

class ProjectCacheTypeDef(BaseValidatorModel):
    type: CacheTypeType
    location: Optional[str] = None
    modes: Optional[Sequence[CacheModeType]] = None

class ScopeConfigurationTypeDef(BaseValidatorModel):
    name: str
    scope: WebhookScopeTypeType
    domain: Optional[str] = None

class WebhookFilterTypeDef(BaseValidatorModel):
    type: WebhookFilterTypeType
    pattern: str
    excludeMatchedPattern: Optional[bool] = None

class DeleteBuildBatchInputRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteFleetInputRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteProjectInputRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteReportGroupInputRequestTypeDef(BaseValidatorModel):
    arn: str
    deleteReports: Optional[bool] = None

class DeleteReportInputRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class DeleteSourceCredentialsInputRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteWebhookInputRequestTypeDef(BaseValidatorModel):
    projectName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeCodeCoveragesInputRequestTypeDef(BaseValidatorModel):
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

class EnvironmentImageTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    versions: Optional[List[str]] = None

class EnvironmentVariableTypeDef(BaseValidatorModel):
    name: str
    value: str
    type: Optional[EnvironmentVariableTypeType] = None

class FleetStatusTypeDef(BaseValidatorModel):
    statusCode: Optional[FleetStatusCodeType] = None
    context: Optional[FleetContextCodeType] = None
    message: Optional[str] = None

class GetReportGroupTrendInputRequestTypeDef(BaseValidatorModel):
    reportGroupArn: str
    trendField: ReportGroupTrendFieldTypeType
    numOfReports: Optional[int] = None

class ReportGroupTrendStatsTypeDef(BaseValidatorModel):
    average: Optional[str] = None
    max: Optional[str] = None
    min: Optional[str] = None

class ReportWithRawDataTypeDef(BaseValidatorModel):
    reportArn: Optional[str] = None
    data: Optional[str] = None

class GetResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class GitSubmodulesConfigTypeDef(BaseValidatorModel):
    fetchSubmodules: bool

class ImportSourceCredentialsInputRequestTypeDef(BaseValidatorModel):
    token: str
    serverType: ServerTypeType
    authType: AuthTypeType
    username: Optional[str] = None
    shouldOverwrite: Optional[bool] = None

class InvalidateProjectCacheInputRequestTypeDef(BaseValidatorModel):
    projectName: str

class ListBuildsForProjectInputRequestTypeDef(BaseValidatorModel):
    projectName: str
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

class ListBuildsInputRequestTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

class ListFleetsInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[FleetSortByTypeType] = None

class ListProjectsInputRequestTypeDef(BaseValidatorModel):
    sortBy: Optional[ProjectSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

class ListReportGroupsInputRequestTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportGroupSortByTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ReportFilterTypeDef(BaseValidatorModel):
    status: Optional[ReportStatusTypeType] = None

class ListSharedProjectsInputRequestTypeDef(BaseValidatorModel):
    sortBy: Optional[SharedResourceSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSharedReportGroupsInputRequestTypeDef(BaseValidatorModel):
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

class SourceAuthTypeDef(BaseValidatorModel):
    type: SourceAuthTypeType
    resource: Optional[str] = None

class PutResourcePolicyInputRequestTypeDef(BaseValidatorModel):
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

class RetryBuildBatchInputRequestTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    idempotencyToken: Optional[str] = None
    retryType: Optional[RetryBuildBatchTypeType] = None

class RetryBuildInputRequestTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    idempotencyToken: Optional[str] = None

class TargetTrackingScalingConfigurationTypeDef(BaseValidatorModel):
    metricType: Optional[Literal["FLEET_UTILIZATION_RATE"]] = None
    targetValue: Optional[float] = None

class StopBuildBatchInputRequestTypeDef(BaseValidatorModel):
    id: str

class StopBuildInputRequestTypeDef(BaseValidatorModel):
    id: str

class UpdateProjectVisibilityInputRequestTypeDef(BaseValidatorModel):
    projectArn: str
    projectVisibility: ProjectVisibilityTypeType
    resourceAccessRole: Optional[str] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildBatchesOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildsForProjectOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildsOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    fleets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    projects: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportGroupsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportsForReportGroupOutputTypeDef(BaseValidatorModel):
    nextToken: str
    reports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    reports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSharedProjectsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    projects: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSharedReportGroupsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListBuildBatchesForProjectInputRequestTypeDef(BaseValidatorModel):
    projectName: Optional[str] = None
    filter: Optional[BuildBatchFilterTypeDef] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

class ListBuildBatchesInputRequestTypeDef(BaseValidatorModel):
    filter: Optional[BuildBatchFilterTypeDef] = None
    maxResults: Optional[int] = None
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None

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

class BuildSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    requestedOn: Optional[datetime] = None
    buildStatus: Optional[StatusTypeType] = None
    primaryArtifact: Optional[ResolvedArtifactTypeDef] = None
    secondaryArtifacts: Optional[List[ResolvedArtifactTypeDef]] = None

class DescribeCodeCoveragesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    codeCoverages: List[CodeCoverageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWebhookInputRequestTypeDef(BaseValidatorModel):
    projectName: str
    branchFilter: Optional[str] = None
    filterGroups: Optional[Sequence[Sequence[WebhookFilterTypeDef]]] = None
    buildType: Optional[WebhookBuildTypeType] = None
    manualCreation: Optional[bool] = None
    scopeConfiguration: Optional[ScopeConfigurationTypeDef] = None

class UpdateWebhookInputRequestTypeDef(BaseValidatorModel):
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

class DescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef(BaseValidatorModel):
    reportArn: str
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportCodeCoverageSortByTypeType] = None
    minLineCoveragePercentage: Optional[float] = None
    maxLineCoveragePercentage: Optional[float] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildBatchesForProjectInputListBuildBatchesForProjectPaginateTypeDef(BaseValidatorModel):
    projectName: Optional[str] = None
    filter: Optional[BuildBatchFilterTypeDef] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildBatchesInputListBuildBatchesPaginateTypeDef(BaseValidatorModel):
    filter: Optional[BuildBatchFilterTypeDef] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildsForProjectInputListBuildsForProjectPaginateTypeDef(BaseValidatorModel):
    projectName: str
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBuildsInputListBuildsPaginateTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsInputListProjectsPaginateTypeDef(BaseValidatorModel):
    sortBy: Optional[ProjectSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportGroupsInputListReportGroupsPaginateTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[ReportGroupSortByTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSharedProjectsInputListSharedProjectsPaginateTypeDef(BaseValidatorModel):
    sortBy: Optional[SharedResourceSortByTypeType] = None
    sortOrder: Optional[SortOrderTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSharedReportGroupsInputListSharedReportGroupsPaginateTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    sortBy: Optional[SharedResourceSortByTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTestCasesInputDescribeTestCasesPaginateTypeDef(BaseValidatorModel):
    reportArn: str
    filter: Optional[TestCaseFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTestCasesInputRequestTypeDef(BaseValidatorModel):
    reportArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[TestCaseFilterTypeDef] = None

class DescribeTestCasesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    testCases: List[TestCaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentLanguageTypeDef(BaseValidatorModel):
    language: Optional[LanguageTypeType] = None
    images: Optional[List[EnvironmentImageTypeDef]] = None

class GetReportGroupTrendOutputTypeDef(BaseValidatorModel):
    stats: ReportGroupTrendStatsTypeDef
    rawData: List[ReportWithRawDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef(BaseValidatorModel):
    reportGroupArn: str
    sortOrder: Optional[SortOrderTypeType] = None
    filter: Optional[ReportFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportsForReportGroupInputRequestTypeDef(BaseValidatorModel):
    reportGroupArn: str
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderTypeType] = None
    maxResults: Optional[int] = None
    filter: Optional[ReportFilterTypeDef] = None

class ListReportsInputListReportsPaginateTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    filter: Optional[ReportFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportsInputRequestTypeDef(BaseValidatorModel):
    sortOrder: Optional[SortOrderTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ReportFilterTypeDef] = None

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

class ProjectEnvironmentOutputTypeDef(BaseValidatorModel):
    type: EnvironmentTypeType
    image: str
    computeType: ComputeTypeType
    fleet: Optional[ProjectFleetTypeDef] = None
    environmentVariables: Optional[List[EnvironmentVariableTypeDef]] = None
    privilegedMode: Optional[bool] = None
    certificate: Optional[str] = None
    registryCredential: Optional[RegistryCredentialTypeDef] = None
    imagePullCredentialsType: Optional[ImagePullCredentialsTypeType] = None

class ProjectEnvironmentTypeDef(BaseValidatorModel):
    type: EnvironmentTypeType
    image: str
    computeType: ComputeTypeType
    fleet: Optional[ProjectFleetTypeDef] = None
    environmentVariables: Optional[Sequence[EnvironmentVariableTypeDef]] = None
    privilegedMode: Optional[bool] = None
    certificate: Optional[str] = None
    registryCredential: Optional[RegistryCredentialTypeDef] = None
    imagePullCredentialsType: Optional[ImagePullCredentialsTypeType] = None

class ProjectSourceTypeDef(BaseValidatorModel):
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

class ReportExportConfigTypeDef(BaseValidatorModel):
    exportConfigType: Optional[ReportExportConfigTypeType] = None
    s3Destination: Optional[S3ReportExportConfigTypeDef] = None

class ScalingConfigurationInputTypeDef(BaseValidatorModel):
    scalingType: Optional[Literal["TARGET_TRACKING_SCALING"]] = None
    targetTrackingScalingConfigs: Optional[       Sequence[TargetTrackingScalingConfigurationTypeDef]     ] = None
    maxCapacity: Optional[int] = None

class ScalingConfigurationOutputTypeDef(BaseValidatorModel):
    scalingType: Optional[Literal["TARGET_TRACKING_SCALING"]] = None
    targetTrackingScalingConfigs: Optional[       List[TargetTrackingScalingConfigurationTypeDef]     ] = None
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

class BuildTypeDef(BaseValidatorModel):
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

class CreateProjectInputRequestTypeDef(BaseValidatorModel):
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

class StartBuildBatchInputRequestTypeDef(BaseValidatorModel):
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

class StartBuildInputRequestTypeDef(BaseValidatorModel):
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

class UpdateProjectInputRequestTypeDef(BaseValidatorModel):
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

class CreateReportGroupInputRequestTypeDef(BaseValidatorModel):
    name: str
    type: ReportTypeType
    exportConfig: ReportExportConfigTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None

class ReportGroupTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[ReportTypeType] = None
    exportConfig: Optional[ReportExportConfigTypeDef] = None
    created: Optional[datetime] = None
    lastModified: Optional[datetime] = None
    tags: Optional[List[TagTypeDef]] = None
    status: Optional[ReportGroupStatusTypeType] = None

class ReportTypeDef(BaseValidatorModel):
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

class UpdateReportGroupInputRequestTypeDef(BaseValidatorModel):
    arn: str
    exportConfig: Optional[ReportExportConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateFleetInputRequestTypeDef(BaseValidatorModel):
    name: str
    baseCapacity: int
    environmentType: EnvironmentTypeType
    computeType: ComputeTypeType
    scalingConfiguration: Optional[ScalingConfigurationInputTypeDef] = None
    overflowBehavior: Optional[FleetOverflowBehaviorType] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None
    fleetServiceRole: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateFleetInputRequestTypeDef(BaseValidatorModel):
    arn: str
    baseCapacity: Optional[int] = None
    environmentType: Optional[EnvironmentTypeType] = None
    computeType: Optional[ComputeTypeType] = None
    scalingConfiguration: Optional[ScalingConfigurationInputTypeDef] = None
    overflowBehavior: Optional[FleetOverflowBehaviorType] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None
    fleetServiceRole: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class FleetTypeDef(BaseValidatorModel):
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

class BuildBatchTypeDef(BaseValidatorModel):
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

class ListCuratedEnvironmentImagesOutputTypeDef(BaseValidatorModel):
    platforms: List[EnvironmentPlatformTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class BatchGetReportsOutputTypeDef(BaseValidatorModel):
    reports: List[ReportTypeDef]
    reportsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

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


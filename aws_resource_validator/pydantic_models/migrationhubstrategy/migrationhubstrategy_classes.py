from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AnalysisStatusUnion(BaseValidatorModel):
    runtimeAnalysisStatus: Optional[RuntimeAnalysisStatusType] = None
    srcCodeOrDbAnalysisStatus: Optional[SrcCodeOrDbAnalysisStatusType] = None


class AnalyzableServerSummary(BaseValidatorModel):
    hostname: Optional[str] = None
    ipAddress: Optional[str] = None
    source: Optional[str] = None
    vmId: Optional[str] = None


class AnalyzerNameUnion(BaseValidatorModel):
    binaryAnalyzerName: Optional[BinaryAnalyzerNameType] = None
    runTimeAnalyzerName: Optional[RunTimeAnalyzerNameType] = None
    sourceCodeAnalyzerName: Optional[SourceCodeAnalyzerNameType] = None


class S3Object(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3key: Optional[str] = None


class AntipatternSeveritySummary(BaseValidatorModel):
    count: Optional[int] = None
    severity: Optional[SeverityType] = None


class AppUnitError(BaseValidatorModel):
    appUnitErrorCategory: Optional[AppUnitErrorCategoryType] = None


class DatabaseConfigDetail(BaseValidatorModel):
    secretName: Optional[str] = None


class SourceCodeRepository(BaseValidatorModel):
    branch: Optional[str] = None
    projectName: Optional[str] = None
    repository: Optional[str] = None
    versionControlType: Optional[str] = None


class ApplicationComponentStatusSummary(BaseValidatorModel):
    count: Optional[int] = None
    srcCodeOrDbAnalysisStatus: Optional[SrcCodeOrDbAnalysisStatusType] = None


class ApplicationComponentSummary(BaseValidatorModel):
    appType: Optional[AppTypeType] = None
    count: Optional[int] = None


class ServerStatusSummary(BaseValidatorModel):
    count: Optional[int] = None
    runTimeAssessmentStatus: Optional[RunTimeAssessmentStatusType] = None


class ServerSummary(BaseValidatorModel):
    ServerOsType: Optional[ServerOsTypeType] = None
    count: Optional[int] = None


class StrategySummary(BaseValidatorModel):
    count: Optional[int] = None
    strategy: Optional[StrategyType] = None


class AssessmentTargetOutput(BaseValidatorModel):
    condition: ConditionType
    name: str
    values: List[str]


class AssessmentTarget(BaseValidatorModel):
    condition: ConditionType
    name: str
    values: List[str]


class AssociatedApplication(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None


class AwsManagedResourcesOutput(BaseValidatorModel):
    targetDestination: List[AwsManagedTargetDestinationType]


class AwsManagedResources(BaseValidatorModel):
    targetDestination: List[AwsManagedTargetDestinationType]


class BusinessGoals(BaseValidatorModel):
    licenseCostReduction: Optional[int] = None
    modernizeInfrastructureWithCloudNativeTechnologies: Optional[int] = None
    reduceOperationalOverheadWithManagedServices: Optional[int] = None
    speedOfMigration: Optional[int] = None


class IPAddressBasedRemoteInfo(BaseValidatorModel):
    authType: Optional[AuthTypeType] = None
    ipAddressConfigurationTimeStamp: Optional[str] = None
    osType: Optional[OSTypeType] = None


class PipelineInfo(BaseValidatorModel):
    pipelineConfigurationTimeStamp: Optional[str] = None
    pipelineType: Optional[Literal['AZURE_DEVOPS']] = None


class RemoteSourceCodeAnalysisServerInfo(BaseValidatorModel):
    remoteSourceCodeAnalysisServerConfigurationTimestamp: Optional[str] = None


class VcenterBasedRemoteInfo(BaseValidatorModel):
    osType: Optional[OSTypeType] = None
    vcenterConfigurationTimeStamp: Optional[str] = None


class VersionControlInfo(BaseValidatorModel):
    versionControlConfigurationTimeStamp: Optional[str] = None
    versionControlType: Optional[VersionControlTypeType] = None


class DataCollectionDetails(BaseValidatorModel):
    completionTime: Optional[datetime] = None
    failed: Optional[int] = None
    inProgress: Optional[int] = None
    servers: Optional[int] = None
    startTime: Optional[datetime] = None
    status: Optional[AssessmentStatusType] = None
    statusMessage: Optional[str] = None
    success: Optional[int] = None


class HeterogeneousOutput(BaseValidatorModel):
    targetDatabaseEngine: List[HeterogeneousTargetDatabaseEngineType]


class HomogeneousOutput(BaseValidatorModel):
    targetDatabaseEngine: Optional[List[Literal['None specified']]] = None


class NoDatabaseMigrationPreferenceOutput(BaseValidatorModel):
    targetDatabaseEngine: List[TargetDatabaseEngineType]


class Heterogeneous(BaseValidatorModel):
    targetDatabaseEngine: List[HeterogeneousTargetDatabaseEngineType]


class Homogeneous(BaseValidatorModel):
    targetDatabaseEngine: Optional[List[Literal['None specified']]] = None


class NoDatabaseMigrationPreference(BaseValidatorModel):
    targetDatabaseEngine: List[TargetDatabaseEngineType]


class GetApplicationComponentDetailsRequest(BaseValidatorModel):
    applicationComponentId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetApplicationComponentStrategiesRequest(BaseValidatorModel):
    applicationComponentId: str


class GetAssessmentRequest(BaseValidatorModel):
    id: str


class GetImportFileTaskRequest(BaseValidatorModel):
    id: str


class GetRecommendationReportDetailsRequest(BaseValidatorModel):
    id: str


class RecommendationReportDetails(BaseValidatorModel):
    completionTime: Optional[datetime] = None
    s3Bucket: Optional[str] = None
    s3Keys: Optional[List[str]] = None
    startTime: Optional[datetime] = None
    status: Optional[RecommendationReportStatusType] = None
    statusMessage: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetServerDetailsRequest(BaseValidatorModel):
    serverId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetServerStrategiesRequest(BaseValidatorModel):
    serverId: str


class Group(BaseValidatorModel):
    name: Optional[GroupNameType] = None
    value: Optional[str] = None


class ImportFileTaskInformation(BaseValidatorModel):
    completionTime: Optional[datetime] = None
    id: Optional[str] = None
    importName: Optional[str] = None
    inputS3Bucket: Optional[str] = None
    inputS3Key: Optional[str] = None
    numberOfRecordsFailed: Optional[int] = None
    numberOfRecordsSuccess: Optional[int] = None
    startTime: Optional[datetime] = None
    status: Optional[ImportFileTaskStatusType] = None
    statusReportS3Bucket: Optional[str] = None
    statusReportS3Key: Optional[str] = None


class ListAnalyzableServersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortOrderType] = None


class ListCollectorsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImportFileTaskRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NoManagementPreferenceOutput(BaseValidatorModel):
    targetDestination: List[NoPreferenceTargetDestinationType]


class SelfManageResourcesOutput(BaseValidatorModel):
    targetDestination: List[SelfManageTargetDestinationType]


class NoManagementPreference(BaseValidatorModel):
    targetDestination: List[NoPreferenceTargetDestinationType]


class SelfManageResources(BaseValidatorModel):
    targetDestination: List[SelfManageTargetDestinationType]


class NetworkInfo(BaseValidatorModel):
    interfaceName: str
    ipAddress: str
    macAddress: str
    netMask: str


class OSInfo(BaseValidatorModel):
    type: Optional[OSTypeType] = None
    version: Optional[str] = None


class TransformationTool(BaseValidatorModel):
    description: Optional[str] = None
    name: Optional[TransformationToolNameType] = None
    tranformationToolInstallationLink: Optional[str] = None


class ServerError(BaseValidatorModel):
    serverErrorCategory: Optional[ServerErrorCategoryType] = None


class SourceCode(BaseValidatorModel):
    location: Optional[str] = None
    projectName: Optional[str] = None
    sourceVersion: Optional[str] = None
    versionControl: Optional[VersionControlType] = None


class StopAssessmentRequest(BaseValidatorModel):
    assessmentId: str


class StrategyOption(BaseValidatorModel):
    isPreferred: Optional[bool] = None
    strategy: Optional[StrategyType] = None
    targetDestination: Optional[TargetDestinationType] = None
    toolName: Optional[TransformationToolNameType] = None


class AntipatternReportResult(BaseValidatorModel):
    analyzerName: Optional[AnalyzerNameUnion] = None
    antiPatternReportS3Object: Optional[S3Object] = None
    antipatternReportStatus: Optional[AntipatternReportStatusType] = None
    antipatternReportStatusMessage: Optional[str] = None


class AssessmentSummary(BaseValidatorModel):
    antipatternReportS3Object: Optional[S3Object] = None
    antipatternReportStatus: Optional[AntipatternReportStatusType] = None
    antipatternReportStatusMessage: Optional[str] = None
    lastAnalyzedTimestamp: Optional[datetime] = None
    listAntipatternSeveritySummary: Optional[List[AntipatternSeveritySummary]] = None
    listApplicationComponentStatusSummary: Optional[List[ApplicationComponentStatusSummary]] = None
    listApplicationComponentStrategySummary: Optional[List[StrategySummary]] = None
    listApplicationComponentSummary: Optional[List[ApplicationComponentSummary]] = None
    listServerStatusSummary: Optional[List[ServerStatusSummary]] = None
    listServerStrategySummary: Optional[List[StrategySummary]] = None
    listServerSummary: Optional[List[ServerSummary]] = None

AssessmentTargetUnion = Union[AssessmentTarget, AssessmentTargetOutput]


class PrioritizeBusinessGoals(BaseValidatorModel):
    businessGoals: Optional[BusinessGoals] = None


class ConfigurationSummary(BaseValidatorModel):
    ipAddressBasedRemoteInfoList: Optional[List[IPAddressBasedRemoteInfo]] = None
    pipelineInfoList: Optional[List[PipelineInfo]] = None
    remoteSourceCodeAnalysisServerInfo: Optional[RemoteSourceCodeAnalysisServerInfo] = None
    vcenterBasedRemoteInfoList: Optional[List[VcenterBasedRemoteInfo]] = None
    versionControlInfoList: Optional[List[VersionControlInfo]] = None


class DatabaseMigrationPreferenceOutput(BaseValidatorModel):
    heterogeneous: Optional[HeterogeneousOutput] = None
    homogeneous: Optional[HomogeneousOutput] = None
    noPreference: Optional[NoDatabaseMigrationPreferenceOutput] = None


class DatabaseMigrationPreference(BaseValidatorModel):
    heterogeneous: Optional[Heterogeneous] = None
    homogeneous: Optional[Homogeneous] = None
    noPreference: Optional[NoDatabaseMigrationPreference] = None


class GetAssessmentResponse(BaseValidatorModel):
    assessmentTargets: List[AssessmentTargetOutput]
    dataCollectionDetails: DataCollectionDetails
    id: str
    ResponseMetadata: ResponseMetadata


class GetImportFileTaskResponse(BaseValidatorModel):
    completionTime: datetime
    id: str
    importName: str
    inputS3Bucket: str
    inputS3Key: str
    numberOfRecordsFailed: int
    numberOfRecordsSuccess: int
    startTime: datetime
    status: ImportFileTaskStatusType
    statusReportS3Bucket: str
    statusReportS3Key: str
    ResponseMetadata: ResponseMetadata


class GetLatestAssessmentIdResponse(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadata


class ListAnalyzableServersResponse(BaseValidatorModel):
    analyzableServers: List[AnalyzableServerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartAssessmentResponse(BaseValidatorModel):
    assessmentId: str
    ResponseMetadata: ResponseMetadata


class StartImportFileTaskResponse(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadata


class StartRecommendationReportGenerationResponse(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadata


class GetRecommendationReportDetailsResponse(BaseValidatorModel):
    id: str
    recommendationReportDetails: RecommendationReportDetails
    ResponseMetadata: ResponseMetadata


class GetServerDetailsRequestPaginate(BaseValidatorModel):
    serverId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnalyzableServersRequestPaginate(BaseValidatorModel):
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollectorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImportFileTaskRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationComponentsRequestPaginate(BaseValidatorModel):
    applicationComponentCriteria: Optional[ApplicationComponentCriteriaType] = None
    filterValue: Optional[str] = None
    groupIdFilter: Optional[List[Group]] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationComponentsRequest(BaseValidatorModel):
    applicationComponentCriteria: Optional[ApplicationComponentCriteriaType] = None
    filterValue: Optional[str] = None
    groupIdFilter: Optional[List[Group]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortOrderType] = None


class ListServersRequestPaginate(BaseValidatorModel):
    filterValue: Optional[str] = None
    groupIdFilter: Optional[List[Group]] = None
    serverCriteria: Optional[ServerCriteriaType] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServersRequest(BaseValidatorModel):
    filterValue: Optional[str] = None
    groupIdFilter: Optional[List[Group]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serverCriteria: Optional[ServerCriteriaType] = None
    sort: Optional[SortOrderType] = None


class StartImportFileTaskRequest(BaseValidatorModel):
    S3Bucket: str
    name: str
    s3key: str
    dataSourceType: Optional[DataSourceTypeType] = None
    groupId: Optional[List[Group]] = None
    s3bucketForReportData: Optional[str] = None


class StartRecommendationReportGenerationRequest(BaseValidatorModel):
    groupIdFilter: Optional[List[Group]] = None
    outputFormat: Optional[OutputFormatType] = None


class ListImportFileTaskResponse(BaseValidatorModel):
    taskInfos: List[ImportFileTaskInformation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ManagementPreferenceOutput(BaseValidatorModel):
    awsManagedResources: Optional[AwsManagedResourcesOutput] = None
    noPreference: Optional[NoManagementPreferenceOutput] = None
    selfManageResources: Optional[SelfManageResourcesOutput] = None


class ManagementPreference(BaseValidatorModel):
    awsManagedResources: Optional[AwsManagedResources] = None
    noPreference: Optional[NoManagementPreference] = None
    selfManageResources: Optional[SelfManageResources] = None


class SystemInfo(BaseValidatorModel):
    cpuArchitecture: Optional[str] = None
    fileSystemType: Optional[str] = None
    networkInfoList: Optional[List[NetworkInfo]] = None
    osInfo: Optional[OSInfo] = None


class RecommendationSet(BaseValidatorModel):
    strategy: Optional[StrategyType] = None
    targetDestination: Optional[TargetDestinationType] = None
    transformationTool: Optional[TransformationTool] = None


class UpdateApplicationComponentConfigRequest(BaseValidatorModel):
    applicationComponentId: str
    appType: Optional[AppTypeType] = None
    configureOnly: Optional[bool] = None
    inclusionStatus: Optional[InclusionStatusType] = None
    secretsManagerKey: Optional[str] = None
    sourceCodeList: Optional[List[SourceCode]] = None
    strategyOption: Optional[StrategyOption] = None


class UpdateServerConfigRequest(BaseValidatorModel):
    serverId: str
    strategyOption: Optional[StrategyOption] = None


class Result(BaseValidatorModel):
    analysisStatus: Optional[AnalysisStatusUnion] = None
    analysisType: Optional[AnalysisTypeType] = None
    antipatternReportResultList: Optional[List[AntipatternReportResult]] = None
    statusMessage: Optional[str] = None


class GetPortfolioSummaryResponse(BaseValidatorModel):
    assessmentSummary: AssessmentSummary
    ResponseMetadata: ResponseMetadata


class StartAssessmentRequest(BaseValidatorModel):
    assessmentDataSourceType: Optional[AssessmentDataSourceTypeType] = None
    assessmentTargets: Optional[List[AssessmentTargetUnion]] = None
    s3bucketForAnalysisData: Optional[str] = None
    s3bucketForReportData: Optional[str] = None


class Collector(BaseValidatorModel):
    collectorHealth: Optional[CollectorHealthType] = None
    collectorId: Optional[str] = None
    collectorVersion: Optional[str] = None
    configurationSummary: Optional[ConfigurationSummary] = None
    hostName: Optional[str] = None
    ipAddress: Optional[str] = None
    lastActivityTimeStamp: Optional[str] = None
    registeredTimeStamp: Optional[str] = None


class DatabasePreferencesOutput(BaseValidatorModel):
    databaseManagementPreference: Optional[DatabaseManagementPreferenceType] = None
    databaseMigrationPreference: Optional[DatabaseMigrationPreferenceOutput] = None


class DatabasePreferences(BaseValidatorModel):
    databaseManagementPreference: Optional[DatabaseManagementPreferenceType] = None
    databaseMigrationPreference: Optional[DatabaseMigrationPreference] = None


class ApplicationPreferencesOutput(BaseValidatorModel):
    managementPreference: Optional[ManagementPreferenceOutput] = None


class ApplicationPreferences(BaseValidatorModel):
    managementPreference: Optional[ManagementPreference] = None


class ApplicationComponentStrategy(BaseValidatorModel):
    isPreferred: Optional[bool] = None
    recommendation: Optional[RecommendationSet] = None
    status: Optional[StrategyRecommendationType] = None


class ServerDetail(BaseValidatorModel):
    antipatternReportS3Object: Optional[S3Object] = None
    antipatternReportStatus: Optional[AntipatternReportStatusType] = None
    antipatternReportStatusMessage: Optional[str] = None
    applicationComponentStrategySummary: Optional[List[StrategySummary]] = None
    dataCollectionStatus: Optional[RunTimeAssessmentStatusType] = None
    id: Optional[str] = None
    lastAnalyzedTimestamp: Optional[datetime] = None
    listAntipatternSeveritySummary: Optional[List[AntipatternSeveritySummary]] = None
    name: Optional[str] = None
    recommendationSet: Optional[RecommendationSet] = None
    serverError: Optional[ServerError] = None
    serverType: Optional[str] = None
    statusMessage: Optional[str] = None
    systemInfo: Optional[SystemInfo] = None


class ServerStrategy(BaseValidatorModel):
    isPreferred: Optional[bool] = None
    numberOfApplicationComponents: Optional[int] = None
    recommendation: Optional[RecommendationSet] = None
    status: Optional[StrategyRecommendationType] = None


class ApplicationComponentDetail(BaseValidatorModel):
    analysisStatus: Optional[SrcCodeOrDbAnalysisStatusType] = None
    antipatternReportS3Object: Optional[S3Object] = None
    antipatternReportStatus: Optional[AntipatternReportStatusType] = None
    antipatternReportStatusMessage: Optional[str] = None
    appType: Optional[AppTypeType] = None
    appUnitError: Optional[AppUnitError] = None
    associatedServerId: Optional[str] = None
    databaseConfigDetail: Optional[DatabaseConfigDetail] = None
    id: Optional[str] = None
    inclusionStatus: Optional[InclusionStatusType] = None
    lastAnalyzedTimestamp: Optional[datetime] = None
    listAntipatternSeveritySummary: Optional[List[AntipatternSeveritySummary]] = None
    moreServerAssociationExists: Optional[bool] = None
    name: Optional[str] = None
    osDriver: Optional[str] = None
    osVersion: Optional[str] = None
    recommendationSet: Optional[RecommendationSet] = None
    resourceSubType: Optional[ResourceSubTypeType] = None
    resultList: Optional[List[Result]] = None
    runtimeStatus: Optional[RuntimeAnalysisStatusType] = None
    runtimeStatusMessage: Optional[str] = None
    sourceCodeRepositories: Optional[List[SourceCodeRepository]] = None
    statusMessage: Optional[str] = None


class ListCollectorsResponse(BaseValidatorModel):
    Collectors: List[Collector]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

DatabasePreferencesUnion = Union[DatabasePreferences, DatabasePreferencesOutput]


class GetPortfolioPreferencesResponse(BaseValidatorModel):
    applicationMode: ApplicationModeType
    applicationPreferences: ApplicationPreferencesOutput
    databasePreferences: DatabasePreferencesOutput
    prioritizeBusinessGoals: PrioritizeBusinessGoals
    ResponseMetadata: ResponseMetadata

ApplicationPreferencesUnion = Union[ApplicationPreferences, ApplicationPreferencesOutput]


class GetApplicationComponentStrategiesResponse(BaseValidatorModel):
    applicationComponentStrategies: List[ApplicationComponentStrategy]
    ResponseMetadata: ResponseMetadata


class GetServerDetailsResponse(BaseValidatorModel):
    associatedApplications: List[AssociatedApplication]
    serverDetail: ServerDetail
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServersResponse(BaseValidatorModel):
    serverInfos: List[ServerDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetServerStrategiesResponse(BaseValidatorModel):
    serverStrategies: List[ServerStrategy]
    ResponseMetadata: ResponseMetadata


class GetApplicationComponentDetailsResponse(BaseValidatorModel):
    applicationComponentDetail: ApplicationComponentDetail
    associatedApplications: List[AssociatedApplication]
    associatedServerIds: List[str]
    moreApplicationResource: bool
    ResponseMetadata: ResponseMetadata


class ListApplicationComponentsResponse(BaseValidatorModel):
    applicationComponentInfos: List[ApplicationComponentDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PutPortfolioPreferencesRequest(BaseValidatorModel):
    applicationMode: Optional[ApplicationModeType] = None
    applicationPreferences: Optional[ApplicationPreferencesUnion] = None
    databasePreferences: Optional[DatabasePreferencesUnion] = None
    prioritizeBusinessGoals: Optional[PrioritizeBusinessGoals] = None
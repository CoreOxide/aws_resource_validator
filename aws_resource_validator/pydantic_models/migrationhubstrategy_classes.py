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
from aws_resource_validator.pydantic_models.migrationhubstrategy_constants import *

class AnalysisStatusUnionTypeDef(BaseModel):
    runtimeAnalysisStatus: Optional[RuntimeAnalysisStatusType] = None
    srcCodeOrDbAnalysisStatus: Optional[SrcCodeOrDbAnalysisStatusType] = None

class AnalyzableServerSummaryTypeDef(BaseModel):
    hostname: Optional[str] = None
    ipAddress: Optional[str] = None
    source: Optional[str] = None
    vmId: Optional[str] = None

class AnalyzerNameUnionTypeDef(BaseModel):
    binaryAnalyzerName: Optional[BinaryAnalyzerNameType] = None
    runTimeAnalyzerName: Optional[RunTimeAnalyzerNameType] = None
    sourceCodeAnalyzerName: Optional[SourceCodeAnalyzerNameType] = None

class S3ObjectTypeDef(BaseModel):
    s3Bucket: Optional[str] = None
    s3key: Optional[str] = None

class AntipatternSeveritySummaryTypeDef(BaseModel):
    count: Optional[int] = None
    severity: Optional[SeverityType] = None

class AppUnitErrorTypeDef(BaseModel):
    appUnitErrorCategory: Optional[AppUnitErrorCategoryType] = None

class DatabaseConfigDetailTypeDef(BaseModel):
    secretName: Optional[str] = None

class SourceCodeRepositoryTypeDef(BaseModel):
    branch: Optional[str] = None
    projectName: Optional[str] = None
    repository: Optional[str] = None
    versionControlType: Optional[str] = None

class ApplicationComponentStatusSummaryTypeDef(BaseModel):
    count: Optional[int] = None
    srcCodeOrDbAnalysisStatus: Optional[SrcCodeOrDbAnalysisStatusType] = None

class ApplicationComponentSummaryTypeDef(BaseModel):
    appType: Optional[AppTypeType] = None
    count: Optional[int] = None

class ServerStatusSummaryTypeDef(BaseModel):
    count: Optional[int] = None
    runTimeAssessmentStatus: Optional[RunTimeAssessmentStatusType] = None

class ServerSummaryTypeDef(BaseModel):
    ServerOsType: Optional[ServerOsTypeType] = None
    count: Optional[int] = None

class StrategySummaryTypeDef(BaseModel):
    count: Optional[int] = None
    strategy: Optional[StrategyType] = None

class AssessmentTargetTypeDef(BaseModel):
    condition: ConditionType
    name: str
    values: List[str]

class AssociatedApplicationTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class AwsManagedResourcesTypeDef(BaseModel):
    targetDestination: List[AwsManagedTargetDestinationType]

class BusinessGoalsTypeDef(BaseModel):
    licenseCostReduction: Optional[int] = None
    modernizeInfrastructureWithCloudNativeTechnologies: Optional[int] = None
    reduceOperationalOverheadWithManagedServices: Optional[int] = None
    speedOfMigration: Optional[int] = None

class IPAddressBasedRemoteInfoTypeDef(BaseModel):
    authType: Optional[AuthTypeType] = None
    ipAddressConfigurationTimeStamp: Optional[str] = None
    osType: Optional[OSTypeType] = None

class PipelineInfoTypeDef(BaseModel):
    pipelineConfigurationTimeStamp: Optional[str] = None
    pipelineType: Optional[Literal["AZURE_DEVOPS"]] = None

class RemoteSourceCodeAnalysisServerInfoTypeDef(BaseModel):
    remoteSourceCodeAnalysisServerConfigurationTimestamp: Optional[str] = None

class VcenterBasedRemoteInfoTypeDef(BaseModel):
    osType: Optional[OSTypeType] = None
    vcenterConfigurationTimeStamp: Optional[str] = None

class VersionControlInfoTypeDef(BaseModel):
    versionControlConfigurationTimeStamp: Optional[str] = None
    versionControlType: Optional[VersionControlTypeType] = None

class DataCollectionDetailsTypeDef(BaseModel):
    completionTime: Optional[datetime] = None
    failed: Optional[int] = None
    inProgress: Optional[int] = None
    servers: Optional[int] = None
    startTime: Optional[datetime] = None
    status: Optional[AssessmentStatusType] = None
    statusMessage: Optional[str] = None
    success: Optional[int] = None

class HeterogeneousTypeDef(BaseModel):
    targetDatabaseEngine: List[HeterogeneousTargetDatabaseEngineType]

class HomogeneousTypeDef(BaseModel):
    targetDatabaseEngine: Optional[List[Literal["None specified"]]] = None

class NoDatabaseMigrationPreferenceTypeDef(BaseModel):
    targetDatabaseEngine: List[TargetDatabaseEngineType]

class GetApplicationComponentDetailsRequestRequestTypeDef(BaseModel):
    applicationComponentId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetApplicationComponentStrategiesRequestRequestTypeDef(BaseModel):
    applicationComponentId: str

class GetAssessmentRequestRequestTypeDef(BaseModel):
    id: str

class GetImportFileTaskRequestRequestTypeDef(BaseModel):
    id: str

class GetRecommendationReportDetailsRequestRequestTypeDef(BaseModel):
    id: str

class RecommendationReportDetailsTypeDef(BaseModel):
    completionTime: Optional[datetime] = None
    s3Bucket: Optional[str] = None
    s3Keys: Optional[List[str]] = None
    startTime: Optional[datetime] = None
    status: Optional[RecommendationReportStatusType] = None
    statusMessage: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetServerDetailsRequestRequestTypeDef(BaseModel):
    serverId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetServerStrategiesRequestRequestTypeDef(BaseModel):
    serverId: str

class GroupTypeDef(BaseModel):
    name: Optional[GroupNameType] = None
    value: Optional[str] = None

class ImportFileTaskInformationTypeDef(BaseModel):
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

class ListAnalyzableServersRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortOrderType] = None

class ListCollectorsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImportFileTaskRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class NoManagementPreferenceTypeDef(BaseModel):
    targetDestination: List[NoPreferenceTargetDestinationType]

class SelfManageResourcesTypeDef(BaseModel):
    targetDestination: List[SelfManageTargetDestinationType]

class NetworkInfoTypeDef(BaseModel):
    interfaceName: str
    ipAddress: str
    macAddress: str
    netMask: str

class OSInfoTypeDef(BaseModel):
    type: Optional[OSTypeType] = None
    version: Optional[str] = None

class TransformationToolTypeDef(BaseModel):
    description: Optional[str] = None
    name: Optional[TransformationToolNameType] = None
    tranformationToolInstallationLink: Optional[str] = None

class ServerErrorTypeDef(BaseModel):
    serverErrorCategory: Optional[ServerErrorCategoryType] = None

class SourceCodeTypeDef(BaseModel):
    location: Optional[str] = None
    projectName: Optional[str] = None
    sourceVersion: Optional[str] = None
    versionControl: Optional[VersionControlType] = None

class StopAssessmentRequestRequestTypeDef(BaseModel):
    assessmentId: str

class StrategyOptionTypeDef(BaseModel):
    isPreferred: Optional[bool] = None
    strategy: Optional[StrategyType] = None
    targetDestination: Optional[TargetDestinationType] = None
    toolName: Optional[TransformationToolNameType] = None

class AntipatternReportResultTypeDef(BaseModel):
    analyzerName: Optional[AnalyzerNameUnionTypeDef] = None
    antiPatternReportS3Object: Optional[S3ObjectTypeDef] = None
    antipatternReportStatus: Optional[AntipatternReportStatusType] = None
    antipatternReportStatusMessage: Optional[str] = None

class AssessmentSummaryTypeDef(BaseModel):
    antipatternReportS3Object: Optional[S3ObjectTypeDef] = None
    antipatternReportStatus: Optional[AntipatternReportStatusType] = None
    antipatternReportStatusMessage: Optional[str] = None
    lastAnalyzedTimestamp: Optional[datetime] = None
    listAntipatternSeveritySummary: Optional[List[AntipatternSeveritySummaryTypeDef]] = None
    listApplicationComponentStatusSummary: Optional[       List[ApplicationComponentStatusSummaryTypeDef]     ] = None
    listApplicationComponentStrategySummary: Optional[List[StrategySummaryTypeDef]] = None
    listApplicationComponentSummary: Optional[List[ApplicationComponentSummaryTypeDef]] = None
    listServerStatusSummary: Optional[List[ServerStatusSummaryTypeDef]] = None
    listServerStrategySummary: Optional[List[StrategySummaryTypeDef]] = None
    listServerSummary: Optional[List[ServerSummaryTypeDef]] = None

class StartAssessmentRequestRequestTypeDef(BaseModel):
    assessmentDataSourceType: Optional[AssessmentDataSourceTypeType] = None
    assessmentTargets: Optional[Sequence[AssessmentTargetTypeDef]] = None
    s3bucketForAnalysisData: Optional[str] = None
    s3bucketForReportData: Optional[str] = None

class PrioritizeBusinessGoalsTypeDef(BaseModel):
    businessGoals: Optional[BusinessGoalsTypeDef] = None

class ConfigurationSummaryTypeDef(BaseModel):
    ipAddressBasedRemoteInfoList: Optional[List[IPAddressBasedRemoteInfoTypeDef]] = None
    pipelineInfoList: Optional[List[PipelineInfoTypeDef]] = None
    remoteSourceCodeAnalysisServerInfo: Optional[       RemoteSourceCodeAnalysisServerInfoTypeDef     ] = None
    vcenterBasedRemoteInfoList: Optional[List[VcenterBasedRemoteInfoTypeDef]] = None
    versionControlInfoList: Optional[List[VersionControlInfoTypeDef]] = None

class DatabaseMigrationPreferenceTypeDef(BaseModel):
    heterogeneous: Optional[HeterogeneousTypeDef] = None
    homogeneous: Optional[HomogeneousTypeDef] = None
    noPreference: Optional[NoDatabaseMigrationPreferenceTypeDef] = None

class GetAssessmentResponseTypeDef(BaseModel):
    assessmentTargets: List[AssessmentTargetTypeDef]
    dataCollectionDetails: DataCollectionDetailsTypeDef
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImportFileTaskResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class GetLatestAssessmentIdResponseTypeDef(BaseModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalyzableServersResponseTypeDef(BaseModel):
    analyzableServers: List[AnalyzableServerSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssessmentResponseTypeDef(BaseModel):
    assessmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportFileTaskResponseTypeDef(BaseModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartRecommendationReportGenerationResponseTypeDef(BaseModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationReportDetailsResponseTypeDef(BaseModel):
    id: str
    recommendationReportDetails: RecommendationReportDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerDetailsRequestGetServerDetailsPaginateTypeDef(BaseModel):
    serverId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnalyzableServersRequestListAnalyzableServersPaginateTypeDef(BaseModel):
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollectorsRequestListCollectorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportFileTaskRequestListImportFileTaskPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef(BaseModel):
    applicationComponentCriteria: Optional[ApplicationComponentCriteriaType] = None
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationComponentsRequestRequestTypeDef(BaseModel):
    applicationComponentCriteria: Optional[ApplicationComponentCriteriaType] = None
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortOrderType] = None

class ListServersRequestListServersPaginateTypeDef(BaseModel):
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    serverCriteria: Optional[ServerCriteriaType] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServersRequestRequestTypeDef(BaseModel):
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serverCriteria: Optional[ServerCriteriaType] = None
    sort: Optional[SortOrderType] = None

class StartImportFileTaskRequestRequestTypeDef(BaseModel):
    S3Bucket: str
    name: str
    s3key: str
    dataSourceType: Optional[DataSourceTypeType] = None
    groupId: Optional[Sequence[GroupTypeDef]] = None
    s3bucketForReportData: Optional[str] = None

class StartRecommendationReportGenerationRequestRequestTypeDef(BaseModel):
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    outputFormat: Optional[OutputFormatType] = None

class ListImportFileTaskResponseTypeDef(BaseModel):
    nextToken: str
    taskInfos: List[ImportFileTaskInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ManagementPreferenceTypeDef(BaseModel):
    awsManagedResources: Optional[AwsManagedResourcesTypeDef] = None
    noPreference: Optional[NoManagementPreferenceTypeDef] = None
    selfManageResources: Optional[SelfManageResourcesTypeDef] = None

class SystemInfoTypeDef(BaseModel):
    cpuArchitecture: Optional[str] = None
    fileSystemType: Optional[str] = None
    networkInfoList: Optional[List[NetworkInfoTypeDef]] = None
    osInfo: Optional[OSInfoTypeDef] = None

class RecommendationSetTypeDef(BaseModel):
    strategy: Optional[StrategyType] = None
    targetDestination: Optional[TargetDestinationType] = None
    transformationTool: Optional[TransformationToolTypeDef] = None

class UpdateApplicationComponentConfigRequestRequestTypeDef(BaseModel):
    applicationComponentId: str
    appType: Optional[AppTypeType] = None
    configureOnly: Optional[bool] = None
    inclusionStatus: Optional[InclusionStatusType] = None
    secretsManagerKey: Optional[str] = None
    sourceCodeList: Optional[Sequence[SourceCodeTypeDef]] = None
    strategyOption: Optional[StrategyOptionTypeDef] = None

class UpdateServerConfigRequestRequestTypeDef(BaseModel):
    serverId: str
    strategyOption: Optional[StrategyOptionTypeDef] = None

class ResultTypeDef(BaseModel):
    analysisStatus: Optional[AnalysisStatusUnionTypeDef] = None
    analysisType: Optional[AnalysisTypeType] = None
    antipatternReportResultList: Optional[List[AntipatternReportResultTypeDef]] = None
    statusMessage: Optional[str] = None

class GetPortfolioSummaryResponseTypeDef(BaseModel):
    assessmentSummary: AssessmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CollectorTypeDef(BaseModel):
    collectorHealth: Optional[CollectorHealthType] = None
    collectorId: Optional[str] = None
    collectorVersion: Optional[str] = None
    configurationSummary: Optional[ConfigurationSummaryTypeDef] = None
    hostName: Optional[str] = None
    ipAddress: Optional[str] = None
    lastActivityTimeStamp: Optional[str] = None
    registeredTimeStamp: Optional[str] = None

class DatabasePreferencesTypeDef(BaseModel):
    databaseManagementPreference: Optional[DatabaseManagementPreferenceType] = None
    databaseMigrationPreference: Optional[DatabaseMigrationPreferenceTypeDef] = None

class ApplicationPreferencesTypeDef(BaseModel):
    managementPreference: Optional[ManagementPreferenceTypeDef] = None

class ApplicationComponentStrategyTypeDef(BaseModel):
    isPreferred: Optional[bool] = None
    recommendation: Optional[RecommendationSetTypeDef] = None
    status: Optional[StrategyRecommendationType] = None

class ServerDetailTypeDef(BaseModel):
    antipatternReportS3Object: Optional[S3ObjectTypeDef] = None
    antipatternReportStatus: Optional[AntipatternReportStatusType] = None
    antipatternReportStatusMessage: Optional[str] = None
    applicationComponentStrategySummary: Optional[List[StrategySummaryTypeDef]] = None
    dataCollectionStatus: Optional[RunTimeAssessmentStatusType] = None
    id: Optional[str] = None
    lastAnalyzedTimestamp: Optional[datetime] = None
    listAntipatternSeveritySummary: Optional[List[AntipatternSeveritySummaryTypeDef]] = None
    name: Optional[str] = None
    recommendationSet: Optional[RecommendationSetTypeDef] = None
    serverError: Optional[ServerErrorTypeDef] = None
    serverType: Optional[str] = None
    statusMessage: Optional[str] = None
    systemInfo: Optional[SystemInfoTypeDef] = None

class ServerStrategyTypeDef(BaseModel):
    isPreferred: Optional[bool] = None
    numberOfApplicationComponents: Optional[int] = None
    recommendation: Optional[RecommendationSetTypeDef] = None
    status: Optional[StrategyRecommendationType] = None

class ApplicationComponentDetailTypeDef(BaseModel):
    analysisStatus: Optional[SrcCodeOrDbAnalysisStatusType] = None
    antipatternReportS3Object: Optional[S3ObjectTypeDef] = None
    antipatternReportStatus: Optional[AntipatternReportStatusType] = None
    antipatternReportStatusMessage: Optional[str] = None
    appType: Optional[AppTypeType] = None
    appUnitError: Optional[AppUnitErrorTypeDef] = None
    associatedServerId: Optional[str] = None
    databaseConfigDetail: Optional[DatabaseConfigDetailTypeDef] = None
    id: Optional[str] = None
    inclusionStatus: Optional[InclusionStatusType] = None
    lastAnalyzedTimestamp: Optional[datetime] = None
    listAntipatternSeveritySummary: Optional[List[AntipatternSeveritySummaryTypeDef]] = None
    moreServerAssociationExists: Optional[bool] = None
    name: Optional[str] = None
    osDriver: Optional[str] = None
    osVersion: Optional[str] = None
    recommendationSet: Optional[RecommendationSetTypeDef] = None
    resourceSubType: Optional[ResourceSubTypeType] = None
    resultList: Optional[List[ResultTypeDef]] = None
    runtimeStatus: Optional[RuntimeAnalysisStatusType] = None
    runtimeStatusMessage: Optional[str] = None
    sourceCodeRepositories: Optional[List[SourceCodeRepositoryTypeDef]] = None
    statusMessage: Optional[str] = None

class ListCollectorsResponseTypeDef(BaseModel):
    Collectors: List[CollectorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPortfolioPreferencesResponseTypeDef(BaseModel):
    applicationMode: ApplicationModeType
    applicationPreferences: ApplicationPreferencesTypeDef
    databasePreferences: DatabasePreferencesTypeDef
    prioritizeBusinessGoals: PrioritizeBusinessGoalsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutPortfolioPreferencesRequestRequestTypeDef(BaseModel):
    applicationMode: Optional[ApplicationModeType] = None
    applicationPreferences: Optional[ApplicationPreferencesTypeDef] = None
    databasePreferences: Optional[DatabasePreferencesTypeDef] = None
    prioritizeBusinessGoals: Optional[PrioritizeBusinessGoalsTypeDef] = None

class GetApplicationComponentStrategiesResponseTypeDef(BaseModel):
    applicationComponentStrategies: List[ApplicationComponentStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerDetailsResponseTypeDef(BaseModel):
    associatedApplications: List[AssociatedApplicationTypeDef]
    nextToken: str
    serverDetail: ServerDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListServersResponseTypeDef(BaseModel):
    nextToken: str
    serverInfos: List[ServerDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerStrategiesResponseTypeDef(BaseModel):
    serverStrategies: List[ServerStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationComponentDetailsResponseTypeDef(BaseModel):
    applicationComponentDetail: ApplicationComponentDetailTypeDef
    associatedApplications: List[AssociatedApplicationTypeDef]
    associatedServerIds: List[str]
    moreApplicationResource: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationComponentsResponseTypeDef(BaseModel):
    applicationComponentInfos: List[ApplicationComponentDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


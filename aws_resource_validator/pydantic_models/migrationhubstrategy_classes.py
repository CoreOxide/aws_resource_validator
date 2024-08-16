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
from aws_resource_validator.pydantic_models.migrationhubstrategy_constants import *

class AnalysisStatusUnionTypeDef(BaseValidatorModel):
    runtimeAnalysisStatus: Optional[RuntimeAnalysisStatusType] = None
    srcCodeOrDbAnalysisStatus: Optional[SrcCodeOrDbAnalysisStatusType] = None

class AnalyzableServerSummaryTypeDef(BaseValidatorModel):
    hostname: Optional[str] = None
    ipAddress: Optional[str] = None
    source: Optional[str] = None
    vmId: Optional[str] = None

class AnalyzerNameUnionTypeDef(BaseValidatorModel):
    binaryAnalyzerName: Optional[BinaryAnalyzerNameType] = None
    runTimeAnalyzerName: Optional[RunTimeAnalyzerNameType] = None
    sourceCodeAnalyzerName: Optional[SourceCodeAnalyzerNameType] = None

class S3ObjectTypeDef(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3key: Optional[str] = None

class AntipatternSeveritySummaryTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    severity: Optional[SeverityType] = None

class AppUnitErrorTypeDef(BaseValidatorModel):
    appUnitErrorCategory: Optional[AppUnitErrorCategoryType] = None

class DatabaseConfigDetailTypeDef(BaseValidatorModel):
    secretName: Optional[str] = None

class SourceCodeRepositoryTypeDef(BaseValidatorModel):
    branch: Optional[str] = None
    projectName: Optional[str] = None
    repository: Optional[str] = None
    versionControlType: Optional[str] = None

class ApplicationComponentStatusSummaryTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    srcCodeOrDbAnalysisStatus: Optional[SrcCodeOrDbAnalysisStatusType] = None

class ApplicationComponentSummaryTypeDef(BaseValidatorModel):
    appType: Optional[AppTypeType] = None
    count: Optional[int] = None

class ServerStatusSummaryTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    runTimeAssessmentStatus: Optional[RunTimeAssessmentStatusType] = None

class ServerSummaryTypeDef(BaseValidatorModel):
    ServerOsType: Optional[ServerOsTypeType] = None
    count: Optional[int] = None

class StrategySummaryTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    strategy: Optional[StrategyType] = None

class AssessmentTargetTypeDef(BaseValidatorModel):
    condition: ConditionType
    name: str
    values: List[str]

class AssociatedApplicationTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None

class AwsManagedResourcesTypeDef(BaseValidatorModel):
    targetDestination: List[AwsManagedTargetDestinationType]

class BusinessGoalsTypeDef(BaseValidatorModel):
    licenseCostReduction: Optional[int] = None
    modernizeInfrastructureWithCloudNativeTechnologies: Optional[int] = None
    reduceOperationalOverheadWithManagedServices: Optional[int] = None
    speedOfMigration: Optional[int] = None

class IPAddressBasedRemoteInfoTypeDef(BaseValidatorModel):
    authType: Optional[AuthTypeType] = None
    ipAddressConfigurationTimeStamp: Optional[str] = None
    osType: Optional[OSTypeType] = None

class PipelineInfoTypeDef(BaseValidatorModel):
    pipelineConfigurationTimeStamp: Optional[str] = None
    pipelineType: Optional[Literal["AZURE_DEVOPS"]] = None

class RemoteSourceCodeAnalysisServerInfoTypeDef(BaseValidatorModel):
    remoteSourceCodeAnalysisServerConfigurationTimestamp: Optional[str] = None

class VcenterBasedRemoteInfoTypeDef(BaseValidatorModel):
    osType: Optional[OSTypeType] = None
    vcenterConfigurationTimeStamp: Optional[str] = None

class VersionControlInfoTypeDef(BaseValidatorModel):
    versionControlConfigurationTimeStamp: Optional[str] = None
    versionControlType: Optional[VersionControlTypeType] = None

class DataCollectionDetailsTypeDef(BaseValidatorModel):
    completionTime: Optional[datetime] = None
    failed: Optional[int] = None
    inProgress: Optional[int] = None
    servers: Optional[int] = None
    startTime: Optional[datetime] = None
    status: Optional[AssessmentStatusType] = None
    statusMessage: Optional[str] = None
    success: Optional[int] = None

class HeterogeneousTypeDef(BaseValidatorModel):
    targetDatabaseEngine: List[HeterogeneousTargetDatabaseEngineType]

class HomogeneousTypeDef(BaseValidatorModel):
    targetDatabaseEngine: Optional[List[Literal["None specified"]]] = None

class NoDatabaseMigrationPreferenceTypeDef(BaseValidatorModel):
    targetDatabaseEngine: List[TargetDatabaseEngineType]

class GetApplicationComponentDetailsRequestRequestTypeDef(BaseValidatorModel):
    applicationComponentId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetApplicationComponentStrategiesRequestRequestTypeDef(BaseValidatorModel):
    applicationComponentId: str

class GetAssessmentRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetImportFileTaskRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetRecommendationReportDetailsRequestRequestTypeDef(BaseValidatorModel):
    id: str

class RecommendationReportDetailsTypeDef(BaseValidatorModel):
    completionTime: Optional[datetime] = None
    s3Bucket: Optional[str] = None
    s3Keys: Optional[List[str]] = None
    startTime: Optional[datetime] = None
    status: Optional[RecommendationReportStatusType] = None
    statusMessage: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetServerDetailsRequestRequestTypeDef(BaseValidatorModel):
    serverId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetServerStrategiesRequestRequestTypeDef(BaseValidatorModel):
    serverId: str

class GroupTypeDef(BaseValidatorModel):
    name: Optional[GroupNameType] = None
    value: Optional[str] = None

class ImportFileTaskInformationTypeDef(BaseValidatorModel):
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

class ListAnalyzableServersRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortOrderType] = None

class ListCollectorsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImportFileTaskRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class NoManagementPreferenceTypeDef(BaseValidatorModel):
    targetDestination: List[NoPreferenceTargetDestinationType]

class SelfManageResourcesTypeDef(BaseValidatorModel):
    targetDestination: List[SelfManageTargetDestinationType]

class NetworkInfoTypeDef(BaseValidatorModel):
    interfaceName: str
    ipAddress: str
    macAddress: str
    netMask: str

class OSInfoTypeDef(BaseValidatorModel):
    type: Optional[OSTypeType] = None
    version: Optional[str] = None

class TransformationToolTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    name: Optional[TransformationToolNameType] = None
    tranformationToolInstallationLink: Optional[str] = None

class ServerErrorTypeDef(BaseValidatorModel):
    serverErrorCategory: Optional[ServerErrorCategoryType] = None

class SourceCodeTypeDef(BaseValidatorModel):
    location: Optional[str] = None
    projectName: Optional[str] = None
    sourceVersion: Optional[str] = None
    versionControl: Optional[VersionControlType] = None

class StopAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str

class StrategyOptionTypeDef(BaseValidatorModel):
    isPreferred: Optional[bool] = None
    strategy: Optional[StrategyType] = None
    targetDestination: Optional[TargetDestinationType] = None
    toolName: Optional[TransformationToolNameType] = None

class AntipatternReportResultTypeDef(BaseValidatorModel):
    analyzerName: Optional[AnalyzerNameUnionTypeDef] = None
    antiPatternReportS3Object: Optional[S3ObjectTypeDef] = None
    antipatternReportStatus: Optional[AntipatternReportStatusType] = None
    antipatternReportStatusMessage: Optional[str] = None

class AssessmentSummaryTypeDef(BaseValidatorModel):
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

class StartAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentDataSourceType: Optional[AssessmentDataSourceTypeType] = None
    assessmentTargets: Optional[Sequence[AssessmentTargetTypeDef]] = None
    s3bucketForAnalysisData: Optional[str] = None
    s3bucketForReportData: Optional[str] = None

class PrioritizeBusinessGoalsTypeDef(BaseValidatorModel):
    businessGoals: Optional[BusinessGoalsTypeDef] = None

class ConfigurationSummaryTypeDef(BaseValidatorModel):
    ipAddressBasedRemoteInfoList: Optional[List[IPAddressBasedRemoteInfoTypeDef]] = None
    pipelineInfoList: Optional[List[PipelineInfoTypeDef]] = None
    remoteSourceCodeAnalysisServerInfo: Optional[       RemoteSourceCodeAnalysisServerInfoTypeDef     ] = None
    vcenterBasedRemoteInfoList: Optional[List[VcenterBasedRemoteInfoTypeDef]] = None
    versionControlInfoList: Optional[List[VersionControlInfoTypeDef]] = None

class DatabaseMigrationPreferenceTypeDef(BaseValidatorModel):
    heterogeneous: Optional[HeterogeneousTypeDef] = None
    homogeneous: Optional[HomogeneousTypeDef] = None
    noPreference: Optional[NoDatabaseMigrationPreferenceTypeDef] = None

class GetAssessmentResponseTypeDef(BaseValidatorModel):
    assessmentTargets: List[AssessmentTargetTypeDef]
    dataCollectionDetails: DataCollectionDetailsTypeDef
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImportFileTaskResponseTypeDef(BaseValidatorModel):
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

class GetLatestAssessmentIdResponseTypeDef(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnalyzableServersResponseTypeDef(BaseValidatorModel):
    analyzableServers: List[AnalyzableServerSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssessmentResponseTypeDef(BaseValidatorModel):
    assessmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportFileTaskResponseTypeDef(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartRecommendationReportGenerationResponseTypeDef(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationReportDetailsResponseTypeDef(BaseValidatorModel):
    id: str
    recommendationReportDetails: RecommendationReportDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerDetailsRequestGetServerDetailsPaginateTypeDef(BaseValidatorModel):
    serverId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnalyzableServersRequestListAnalyzableServersPaginateTypeDef(BaseValidatorModel):
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollectorsRequestListCollectorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportFileTaskRequestListImportFileTaskPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef(BaseValidatorModel):
    applicationComponentCriteria: Optional[ApplicationComponentCriteriaType] = None
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationComponentsRequestRequestTypeDef(BaseValidatorModel):
    applicationComponentCriteria: Optional[ApplicationComponentCriteriaType] = None
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortOrderType] = None

class ListServersRequestListServersPaginateTypeDef(BaseValidatorModel):
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    serverCriteria: Optional[ServerCriteriaType] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServersRequestRequestTypeDef(BaseValidatorModel):
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serverCriteria: Optional[ServerCriteriaType] = None
    sort: Optional[SortOrderType] = None

class StartImportFileTaskRequestRequestTypeDef(BaseValidatorModel):
    S3Bucket: str
    name: str
    s3key: str
    dataSourceType: Optional[DataSourceTypeType] = None
    groupId: Optional[Sequence[GroupTypeDef]] = None
    s3bucketForReportData: Optional[str] = None

class StartRecommendationReportGenerationRequestRequestTypeDef(BaseValidatorModel):
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    outputFormat: Optional[OutputFormatType] = None

class ListImportFileTaskResponseTypeDef(BaseValidatorModel):
    nextToken: str
    taskInfos: List[ImportFileTaskInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ManagementPreferenceTypeDef(BaseValidatorModel):
    awsManagedResources: Optional[AwsManagedResourcesTypeDef] = None
    noPreference: Optional[NoManagementPreferenceTypeDef] = None
    selfManageResources: Optional[SelfManageResourcesTypeDef] = None

class SystemInfoTypeDef(BaseValidatorModel):
    cpuArchitecture: Optional[str] = None
    fileSystemType: Optional[str] = None
    networkInfoList: Optional[List[NetworkInfoTypeDef]] = None
    osInfo: Optional[OSInfoTypeDef] = None

class RecommendationSetTypeDef(BaseValidatorModel):
    strategy: Optional[StrategyType] = None
    targetDestination: Optional[TargetDestinationType] = None
    transformationTool: Optional[TransformationToolTypeDef] = None

class UpdateApplicationComponentConfigRequestRequestTypeDef(BaseValidatorModel):
    applicationComponentId: str
    appType: Optional[AppTypeType] = None
    configureOnly: Optional[bool] = None
    inclusionStatus: Optional[InclusionStatusType] = None
    secretsManagerKey: Optional[str] = None
    sourceCodeList: Optional[Sequence[SourceCodeTypeDef]] = None
    strategyOption: Optional[StrategyOptionTypeDef] = None

class UpdateServerConfigRequestRequestTypeDef(BaseValidatorModel):
    serverId: str
    strategyOption: Optional[StrategyOptionTypeDef] = None

class ResultTypeDef(BaseValidatorModel):
    analysisStatus: Optional[AnalysisStatusUnionTypeDef] = None
    analysisType: Optional[AnalysisTypeType] = None
    antipatternReportResultList: Optional[List[AntipatternReportResultTypeDef]] = None
    statusMessage: Optional[str] = None

class GetPortfolioSummaryResponseTypeDef(BaseValidatorModel):
    assessmentSummary: AssessmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CollectorTypeDef(BaseValidatorModel):
    collectorHealth: Optional[CollectorHealthType] = None
    collectorId: Optional[str] = None
    collectorVersion: Optional[str] = None
    configurationSummary: Optional[ConfigurationSummaryTypeDef] = None
    hostName: Optional[str] = None
    ipAddress: Optional[str] = None
    lastActivityTimeStamp: Optional[str] = None
    registeredTimeStamp: Optional[str] = None

class DatabasePreferencesTypeDef(BaseValidatorModel):
    databaseManagementPreference: Optional[DatabaseManagementPreferenceType] = None
    databaseMigrationPreference: Optional[DatabaseMigrationPreferenceTypeDef] = None

class ApplicationPreferencesTypeDef(BaseValidatorModel):
    managementPreference: Optional[ManagementPreferenceTypeDef] = None

class ApplicationComponentStrategyTypeDef(BaseValidatorModel):
    isPreferred: Optional[bool] = None
    recommendation: Optional[RecommendationSetTypeDef] = None
    status: Optional[StrategyRecommendationType] = None

class ServerDetailTypeDef(BaseValidatorModel):
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

class ServerStrategyTypeDef(BaseValidatorModel):
    isPreferred: Optional[bool] = None
    numberOfApplicationComponents: Optional[int] = None
    recommendation: Optional[RecommendationSetTypeDef] = None
    status: Optional[StrategyRecommendationType] = None

class ApplicationComponentDetailTypeDef(BaseValidatorModel):
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

class ListCollectorsResponseTypeDef(BaseValidatorModel):
    Collectors: List[CollectorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPortfolioPreferencesResponseTypeDef(BaseValidatorModel):
    applicationMode: ApplicationModeType
    applicationPreferences: ApplicationPreferencesTypeDef
    databasePreferences: DatabasePreferencesTypeDef
    prioritizeBusinessGoals: PrioritizeBusinessGoalsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutPortfolioPreferencesRequestRequestTypeDef(BaseValidatorModel):
    applicationMode: Optional[ApplicationModeType] = None
    applicationPreferences: Optional[ApplicationPreferencesTypeDef] = None
    databasePreferences: Optional[DatabasePreferencesTypeDef] = None
    prioritizeBusinessGoals: Optional[PrioritizeBusinessGoalsTypeDef] = None

class GetApplicationComponentStrategiesResponseTypeDef(BaseValidatorModel):
    applicationComponentStrategies: List[ApplicationComponentStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerDetailsResponseTypeDef(BaseValidatorModel):
    associatedApplications: List[AssociatedApplicationTypeDef]
    nextToken: str
    serverDetail: ServerDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListServersResponseTypeDef(BaseValidatorModel):
    nextToken: str
    serverInfos: List[ServerDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServerStrategiesResponseTypeDef(BaseValidatorModel):
    serverStrategies: List[ServerStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationComponentDetailsResponseTypeDef(BaseValidatorModel):
    applicationComponentDetail: ApplicationComponentDetailTypeDef
    associatedApplications: List[AssociatedApplicationTypeDef]
    associatedServerIds: List[str]
    moreApplicationResource: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationComponentsResponseTypeDef(BaseValidatorModel):
    applicationComponentInfos: List[ApplicationComponentDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


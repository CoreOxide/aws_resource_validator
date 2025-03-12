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


class AssessmentTargetOutputTypeDef(BaseValidatorModel):
    condition: ConditionType
    name: str
    values: List[str]


class AssessmentTargetTypeDef(BaseValidatorModel):
    condition: ConditionType
    name: str
    values: Sequence[str]


class AwsManagedResourcesOutputTypeDef(BaseValidatorModel):
    targetDestination: List[AwsManagedTargetDestinationType]


class AwsManagedResourcesTypeDef(BaseValidatorModel):
    targetDestination: Sequence[AwsManagedTargetDestinationType]


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


class HeterogeneousOutputTypeDef(BaseValidatorModel):
    targetDatabaseEngine: List[HeterogeneousTargetDatabaseEngineType]


class HomogeneousOutputTypeDef(BaseValidatorModel):
    targetDatabaseEngine: Optional[List[Literal["None specified"]]] = None


class NoDatabaseMigrationPreferenceOutputTypeDef(BaseValidatorModel):
    targetDatabaseEngine: List[TargetDatabaseEngineType]


class HeterogeneousTypeDef(BaseValidatorModel):
    targetDatabaseEngine: Sequence[HeterogeneousTargetDatabaseEngineType]


class HomogeneousTypeDef(BaseValidatorModel):
    targetDatabaseEngine: Optional[Sequence[Literal["None specified"]]] = None


class NoDatabaseMigrationPreferenceTypeDef(BaseValidatorModel):
    targetDatabaseEngine: Sequence[TargetDatabaseEngineType]


class GetApplicationComponentDetailsRequestTypeDef(BaseValidatorModel):
    applicationComponentId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetApplicationComponentStrategiesRequestTypeDef(BaseValidatorModel):
    applicationComponentId: str


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


class GetServerDetailsRequestTypeDef(BaseValidatorModel):
    serverId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetServerStrategiesRequestTypeDef(BaseValidatorModel):
    serverId: str


class GroupTypeDef(BaseValidatorModel):
    name: Optional[GroupNameType] = None
    value: Optional[str] = None


class ListAnalyzableServersRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortOrderType] = None


class ListCollectorsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImportFileTaskRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NoManagementPreferenceOutputTypeDef(BaseValidatorModel):
    targetDestination: List[NoPreferenceTargetDestinationType]


class SelfManageResourcesOutputTypeDef(BaseValidatorModel):
    targetDestination: List[SelfManageTargetDestinationType]


class NoManagementPreferenceTypeDef(BaseValidatorModel):
    targetDestination: Sequence[NoPreferenceTargetDestinationType]


class SelfManageResourcesTypeDef(BaseValidatorModel):
    targetDestination: Sequence[SelfManageTargetDestinationType]


class NetworkInfoTypeDef(BaseValidatorModel):
    interfaceName: str
    ipAddress: str
    macAddress: str
    netMask: str


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


class StopAssessmentRequestTypeDef(BaseValidatorModel):
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
    listApplicationComponentStatusSummary: Optional[ List[ApplicationComponentStatusSummaryTypeDef] ] = None
    listApplicationComponentStrategySummary: Optional[List[StrategySummaryTypeDef]] = None
    listApplicationComponentSummary: Optional[List[ApplicationComponentSummaryTypeDef]] = None
    listServerStatusSummary: Optional[List[ServerStatusSummaryTypeDef]] = None
    listServerStrategySummary: Optional[List[StrategySummaryTypeDef]] = None
    listServerSummary: Optional[List[ServerSummaryTypeDef]] = None


class PrioritizeBusinessGoalsTypeDef(BaseValidatorModel):
    businessGoals: Optional[BusinessGoalsTypeDef] = None


class ConfigurationSummaryTypeDef(BaseValidatorModel):
    ipAddressBasedRemoteInfoList: Optional[List[IPAddressBasedRemoteInfoTypeDef]] = None
    pipelineInfoList: Optional[List[PipelineInfoTypeDef]] = None
    remoteSourceCodeAnalysisServerInfo: Optional[RemoteSourceCodeAnalysisServerInfoTypeDef] = None
    vcenterBasedRemoteInfoList: Optional[List[VcenterBasedRemoteInfoTypeDef]] = None
    versionControlInfoList: Optional[List[VersionControlInfoTypeDef]] = None


class DatabaseMigrationPreferenceOutputTypeDef(BaseValidatorModel):
    heterogeneous: Optional[HeterogeneousOutputTypeDef] = None
    homogeneous: Optional[HomogeneousOutputTypeDef] = None
    noPreference: Optional[NoDatabaseMigrationPreferenceOutputTypeDef] = None


class DatabaseMigrationPreferenceTypeDef(BaseValidatorModel):
    heterogeneous: Optional[HeterogeneousTypeDef] = None
    homogeneous: Optional[HomogeneousTypeDef] = None
    noPreference: Optional[NoDatabaseMigrationPreferenceTypeDef] = None


class ListAnalyzableServersResponseTypeDef(BaseValidatorModel):
    analyzableServers: List[AnalyzableServerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartAssessmentResponseTypeDef(BaseValidatorModel):
    assessmentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetServerDetailsRequestPaginateTypeDef(BaseValidatorModel):
    serverId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAnalyzableServersRequestPaginateTypeDef(BaseValidatorModel):
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollectorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListImportFileTaskRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationComponentsRequestPaginateTypeDef(BaseValidatorModel):
    applicationComponentCriteria: Optional[ApplicationComponentCriteriaType] = None
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationComponentsRequestTypeDef(BaseValidatorModel):
    applicationComponentCriteria: Optional[ApplicationComponentCriteriaType] = None
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortOrderType] = None


class ListServersRequestPaginateTypeDef(BaseValidatorModel):
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    serverCriteria: Optional[ServerCriteriaType] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServersRequestTypeDef(BaseValidatorModel):
    filterValue: Optional[str] = None
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serverCriteria: Optional[ServerCriteriaType] = None
    sort: Optional[SortOrderType] = None


class StartImportFileTaskRequestTypeDef(BaseValidatorModel):
    S3Bucket: str
    name: str
    s3key: str
    dataSourceType: Optional[DataSourceTypeType] = None
    groupId: Optional[Sequence[GroupTypeDef]] = None
    s3bucketForReportData: Optional[str] = None


class StartRecommendationReportGenerationRequestTypeDef(BaseValidatorModel):
    groupIdFilter: Optional[Sequence[GroupTypeDef]] = None
    outputFormat: Optional[OutputFormatType] = None


class ImportFileTaskInformationTypeDef(BaseValidatorModel):
    pass


class ListImportFileTaskResponseTypeDef(BaseValidatorModel):
    taskInfos: List[ImportFileTaskInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ManagementPreferenceOutputTypeDef(BaseValidatorModel):
    awsManagedResources: Optional[AwsManagedResourcesOutputTypeDef] = None
    noPreference: Optional[NoManagementPreferenceOutputTypeDef] = None
    selfManageResources: Optional[SelfManageResourcesOutputTypeDef] = None


class ManagementPreferenceTypeDef(BaseValidatorModel):
    awsManagedResources: Optional[AwsManagedResourcesTypeDef] = None
    noPreference: Optional[NoManagementPreferenceTypeDef] = None
    selfManageResources: Optional[SelfManageResourcesTypeDef] = None


class OSInfoTypeDef(BaseValidatorModel):
    pass


class SystemInfoTypeDef(BaseValidatorModel):
    cpuArchitecture: Optional[str] = None
    fileSystemType: Optional[str] = None
    networkInfoList: Optional[List[NetworkInfoTypeDef]] = None
    osInfo: Optional[OSInfoTypeDef] = None


class RecommendationSetTypeDef(BaseValidatorModel):
    strategy: Optional[StrategyType] = None
    targetDestination: Optional[TargetDestinationType] = None
    transformationTool: Optional[TransformationToolTypeDef] = None


class UpdateApplicationComponentConfigRequestTypeDef(BaseValidatorModel):
    applicationComponentId: str
    appType: Optional[AppTypeType] = None
    configureOnly: Optional[bool] = None
    inclusionStatus: Optional[InclusionStatusType] = None
    secretsManagerKey: Optional[str] = None
    sourceCodeList: Optional[Sequence[SourceCodeTypeDef]] = None
    strategyOption: Optional[StrategyOptionTypeDef] = None


class UpdateServerConfigRequestTypeDef(BaseValidatorModel):
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


class AssessmentTargetUnionTypeDef(BaseValidatorModel):
    pass


class StartAssessmentRequestTypeDef(BaseValidatorModel):
    assessmentDataSourceType: Optional[AssessmentDataSourceTypeType] = None
    assessmentTargets: Optional[Sequence[AssessmentTargetUnionTypeDef]] = None
    s3bucketForAnalysisData: Optional[str] = None
    s3bucketForReportData: Optional[str] = None


class CollectorTypeDef(BaseValidatorModel):
    collectorHealth: Optional[CollectorHealthType] = None
    collectorId: Optional[str] = None
    collectorVersion: Optional[str] = None
    configurationSummary: Optional[ConfigurationSummaryTypeDef] = None
    hostName: Optional[str] = None
    ipAddress: Optional[str] = None
    lastActivityTimeStamp: Optional[str] = None
    registeredTimeStamp: Optional[str] = None


class DatabasePreferencesOutputTypeDef(BaseValidatorModel):
    databaseManagementPreference: Optional[DatabaseManagementPreferenceType] = None
    databaseMigrationPreference: Optional[DatabaseMigrationPreferenceOutputTypeDef] = None


class DatabasePreferencesTypeDef(BaseValidatorModel):
    databaseManagementPreference: Optional[DatabaseManagementPreferenceType] = None
    databaseMigrationPreference: Optional[DatabaseMigrationPreferenceTypeDef] = None


class ApplicationPreferencesOutputTypeDef(BaseValidatorModel):
    managementPreference: Optional[ManagementPreferenceOutputTypeDef] = None


class ApplicationPreferencesTypeDef(BaseValidatorModel):
    managementPreference: Optional[ManagementPreferenceTypeDef] = None


class ApplicationComponentStrategyTypeDef(BaseValidatorModel):
    isPreferred: Optional[bool] = None
    recommendation: Optional[RecommendationSetTypeDef] = None
    status: Optional[StrategyRecommendationType] = None


class ServerStrategyTypeDef(BaseValidatorModel):
    isPreferred: Optional[bool] = None
    numberOfApplicationComponents: Optional[int] = None
    recommendation: Optional[RecommendationSetTypeDef] = None
    status: Optional[StrategyRecommendationType] = None


class ListCollectorsResponseTypeDef(BaseValidatorModel):
    Collectors: List[CollectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetPortfolioPreferencesResponseTypeDef(BaseValidatorModel):
    applicationMode: ApplicationModeType
    applicationPreferences: ApplicationPreferencesOutputTypeDef
    databasePreferences: DatabasePreferencesOutputTypeDef
    prioritizeBusinessGoals: PrioritizeBusinessGoalsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetApplicationComponentStrategiesResponseTypeDef(BaseValidatorModel):
    applicationComponentStrategies: List[ApplicationComponentStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AssociatedApplicationTypeDef(BaseValidatorModel):
    pass


class ServerDetailTypeDef(BaseValidatorModel):
    pass


class GetServerDetailsResponseTypeDef(BaseValidatorModel):
    associatedApplications: List[AssociatedApplicationTypeDef]
    serverDetail: ServerDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServersResponseTypeDef(BaseValidatorModel):
    serverInfos: List[ServerDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetServerStrategiesResponseTypeDef(BaseValidatorModel):
    serverStrategies: List[ServerStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ApplicationComponentDetailTypeDef(BaseValidatorModel):
    pass


class GetApplicationComponentDetailsResponseTypeDef(BaseValidatorModel):
    applicationComponentDetail: ApplicationComponentDetailTypeDef
    associatedApplications: List[AssociatedApplicationTypeDef]
    associatedServerIds: List[str]
    moreApplicationResource: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ListApplicationComponentsResponseTypeDef(BaseValidatorModel):
    applicationComponentInfos: List[ApplicationComponentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ApplicationPreferencesUnionTypeDef(BaseValidatorModel):
    pass


class DatabasePreferencesUnionTypeDef(BaseValidatorModel):
    pass


class PutPortfolioPreferencesRequestTypeDef(BaseValidatorModel):
    applicationMode: Optional[ApplicationModeType] = None
    applicationPreferences: Optional[ApplicationPreferencesUnionTypeDef] = None
    databasePreferences: Optional[DatabasePreferencesUnionTypeDef] = None
    prioritizeBusinessGoals: Optional[PrioritizeBusinessGoalsTypeDef] = None



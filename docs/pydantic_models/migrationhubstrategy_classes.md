# Migrationhubstrategy Classes

# AnalysisStatusUnionTypeDef

### runtimeAnalysisStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED']]

### srcCodeOrDbAnalysisStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_PARTIAL_SUCCESS', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED', 'CONFIGURED', 'UNCONFIGURED']]


# AnalyzableServerSummaryTypeDef

### hostname
- **Type**: typing.Optional[str]

### ipAddress
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]

### vmId
- **Type**: typing.Optional[str]


# AnalyzerNameUnionTypeDef

### binaryAnalyzerName
- **Type**: typing.Optional[typing.Literal['BYTECODE_ANALYZER', 'DLL_ANALYZER']]

### runTimeAnalyzerName
- **Type**: typing.Optional[typing.Literal['A2C_ANALYZER', 'DATABASE_ANALYZER', 'EMP_PA_ANALYZER', 'REHOST_ANALYZER', 'SCT_ANALYZER']]

### sourceCodeAnalyzerName
- **Type**: typing.Optional[typing.Literal['BYTECODE_ANALYZER', 'CSHARP_ANALYZER', 'JAVA_ANALYZER', 'PORTING_ASSISTANT']]


# AntipatternReportResultTypeDef

### analyzerName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AnalyzerNameUnionTypeDef]

### antiPatternReportS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.S3ObjectTypeDef]

### antipatternReportStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### antipatternReportStatusMessage
- **Type**: typing.Optional[str]


# AntipatternSeveritySummaryTypeDef

### count
- **Type**: typing.Optional[int]

### severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# AppUnitErrorTypeDef

### appUnitErrorCategory
- **Type**: typing.Optional[typing.Literal['CONNECTIVITY_ERROR', 'CREDENTIAL_ERROR', 'OTHER_ERROR', 'PERMISSION_ERROR', 'UNSUPPORTED_ERROR']]


# ApplicationComponentDetailTypeDef

### analysisStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_PARTIAL_SUCCESS', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED', 'CONFIGURED', 'UNCONFIGURED']]

### antipatternReportS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.S3ObjectTypeDef]

### antipatternReportStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### antipatternReportStatusMessage
- **Type**: typing.Optional[str]

### appType
- **Type**: typing.Optional[typing.Literal['Cassandra', 'DB2', 'DotNetFramework', 'Dotnet', 'DotnetCore', 'IBM WebSphere', 'IIS', 'JBoss', 'Java', 'Maria DB', 'Mongo DB', 'MySQL', 'Oracle', 'Oracle WebLogic', 'Other', 'PostgreSQLServer', 'SQLServer', 'Spring', 'Sybase', 'Tomcat', 'Unknown', 'Visual Basic']]

### appUnitError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AppUnitErrorTypeDef]

### associatedServerId
- **Type**: typing.Optional[str]

### databaseConfigDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.DatabaseConfigDetailTypeDef]

### id
- **Type**: typing.Optional[str]

### inclusionStatus
- **Type**: typing.Optional[typing.Literal['excludeFromAssessment', 'includeInAssessment']]

### lastAnalyzedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### listAntipatternSeveritySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AntipatternSeveritySummaryTypeDef]]

### moreServerAssociationExists
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### osDriver
- **Type**: typing.Optional[str]

### osVersion
- **Type**: typing.Optional[str]

### recommendationSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.RecommendationSetTypeDef]

### resourceSubType
- **Type**: typing.Optional[typing.Literal['Database', 'DatabaseProcess', 'Process']]

### resultList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResultTypeDef]]

### runtimeStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED']]

### runtimeStatusMessage
- **Type**: typing.Optional[str]

### sourceCodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.SourceCodeRepositoryTypeDef]]

### statusMessage
- **Type**: typing.Optional[str]


# ApplicationComponentStatusSummaryTypeDef

### count
- **Type**: typing.Optional[int]

### srcCodeOrDbAnalysisStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_PARTIAL_SUCCESS', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED', 'CONFIGURED', 'UNCONFIGURED']]


# ApplicationComponentStrategyTypeDef

### isPreferred
- **Type**: typing.Optional[bool]

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.RecommendationSetTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['notRecommended', 'potential', 'recommended', 'viableOption']]


# ApplicationComponentSummaryTypeDef

### appType
- **Type**: typing.Optional[typing.Literal['Cassandra', 'DB2', 'DotNetFramework', 'Dotnet', 'DotnetCore', 'IBM WebSphere', 'IIS', 'JBoss', 'Java', 'Maria DB', 'Mongo DB', 'MySQL', 'Oracle', 'Oracle WebLogic', 'Other', 'PostgreSQLServer', 'SQLServer', 'Spring', 'Sybase', 'Tomcat', 'Unknown', 'Visual Basic']]

### count
- **Type**: typing.Optional[int]


# ApplicationPreferencesTypeDef

### managementPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ManagementPreferenceTypeDef]


# AssessmentSummaryTypeDef

### antipatternReportS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.S3ObjectTypeDef]

### antipatternReportStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### antipatternReportStatusMessage
- **Type**: typing.Optional[str]

### lastAnalyzedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### listAntipatternSeveritySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AntipatternSeveritySummaryTypeDef]]

### listApplicationComponentStatusSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ApplicationComponentStatusSummaryTypeDef]]

### listApplicationComponentStrategySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.StrategySummaryTypeDef]]

### listApplicationComponentSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ApplicationComponentSummaryTypeDef]]

### listServerStatusSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ServerStatusSummaryTypeDef]]

### listServerStrategySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.StrategySummaryTypeDef]]

### listServerSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ServerSummaryTypeDef]]


# AssessmentTargetTypeDef

### condition
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# AssociatedApplicationTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AwsManagedResourcesTypeDef

### targetDestination
- **Type**: typing.List[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'None specified']]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BusinessGoalsTypeDef

### licenseCostReduction
- **Type**: typing.Optional[int]

### modernizeInfrastructureWithCloudNativeTechnologies
- **Type**: typing.Optional[int]

### reduceOperationalOverheadWithManagedServices
- **Type**: typing.Optional[int]

### speedOfMigration
- **Type**: typing.Optional[int]


# CollectorTypeDef

### collectorHealth
- **Type**: typing.Optional[typing.Literal['COLLECTOR_HEALTHY', 'COLLECTOR_UNHEALTHY']]

### collectorId
- **Type**: typing.Optional[str]

### collectorVersion
- **Type**: typing.Optional[str]

### configurationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ConfigurationSummaryTypeDef]

### hostName
- **Type**: typing.Optional[str]

### ipAddress
- **Type**: typing.Optional[str]

### lastActivityTimeStamp
- **Type**: typing.Optional[str]

### registeredTimeStamp
- **Type**: typing.Optional[str]


# ConfigurationSummaryTypeDef

### ipAddressBasedRemoteInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.IPAddressBasedRemoteInfoTypeDef]]

### pipelineInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.PipelineInfoTypeDef]]

### remoteSourceCodeAnalysisServerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.RemoteSourceCodeAnalysisServerInfoTypeDef]

### vcenterBasedRemoteInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.VcenterBasedRemoteInfoTypeDef]]

### versionControlInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.VersionControlInfoTypeDef]]


# DataCollectionDetailsTypeDef

### completionTime
- **Type**: typing.Optional[datetime.datetime]

### failed
- **Type**: typing.Optional[int]

### inProgress
- **Type**: typing.Optional[int]

### servers
- **Type**: typing.Optional[int]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS', 'STOPPED']]

### statusMessage
- **Type**: typing.Optional[str]

### success
- **Type**: typing.Optional[int]


# DatabaseConfigDetailTypeDef

### secretName
- **Type**: typing.Optional[str]


# DatabaseMigrationPreferenceTypeDef

### heterogeneous
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.HeterogeneousTypeDef]

### homogeneous
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.HomogeneousTypeDef]

### noPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.NoDatabaseMigrationPreferenceTypeDef]


# DatabasePreferencesTypeDef

### databaseManagementPreference
- **Type**: typing.Optional[typing.Literal['AWS-managed', 'No preference', 'Self-manage']]

### databaseMigrationPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.DatabaseMigrationPreferenceTypeDef]


# GetApplicationComponentDetailsRequestRequestTypeDef

### applicationComponentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationComponentDetailsResponseTypeDef

### applicationComponentDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ApplicationComponentDetailTypeDef'>
- **Required**: Yes

### associatedApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AssociatedApplicationTypeDef]
- **Required**: Yes

### associatedServerIds
- **Type**: typing.List[str]
- **Required**: Yes

### moreApplicationResource
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationComponentStrategiesRequestRequestTypeDef

### applicationComponentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationComponentStrategiesResponseTypeDef

### applicationComponentStrategies
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ApplicationComponentStrategyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssessmentRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssessmentResponseTypeDef

### assessmentTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AssessmentTargetTypeDef]
- **Required**: Yes

### dataCollectionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.DataCollectionDetailsTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImportFileTaskRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportFileTaskResponseTypeDef

### completionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### importName
- **Type**: <class 'str'>
- **Required**: Yes

### inputS3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### inputS3Key
- **Type**: <class 'str'>
- **Required**: Yes

### numberOfRecordsFailed
- **Type**: <class 'int'>
- **Required**: Yes

### numberOfRecordsSuccess
- **Type**: <class 'int'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DeleteFailed', 'DeleteInProgress', 'DeletePartialSuccess', 'DeleteSuccess', 'ImportFailed', 'ImportInProgress', 'ImportPartialSuccess', 'ImportSuccess']
- **Required**: Yes

### statusReportS3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### statusReportS3Key
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLatestAssessmentIdResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPortfolioPreferencesResponseTypeDef

### applicationMode
- **Type**: typing.Literal['ALL', 'KNOWN', 'UNKNOWN']
- **Required**: Yes

### applicationPreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ApplicationPreferencesTypeDef'>
- **Required**: Yes

### databasePreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.DatabasePreferencesTypeDef'>
- **Required**: Yes

### prioritizeBusinessGoals
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.PrioritizeBusinessGoalsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPortfolioSummaryResponseTypeDef

### assessmentSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AssessmentSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecommendationReportDetailsRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecommendationReportDetailsResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationReportDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.RecommendationReportDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServerDetailsRequestGetServerDetailsPaginateTypeDef

### serverId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.PaginatorConfigTypeDef]


# GetServerDetailsRequestRequestTypeDef

### serverId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetServerDetailsResponseTypeDef

### associatedApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AssociatedApplicationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### serverDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ServerDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServerStrategiesRequestRequestTypeDef

### serverId
- **Type**: <class 'str'>
- **Required**: Yes


# GetServerStrategiesResponseTypeDef

### serverStrategies
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ServerStrategyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupTypeDef

### name
- **Type**: typing.Optional[typing.Literal['ExternalId', 'ExternalSourceType']]

### value
- **Type**: typing.Optional[str]


# HeterogeneousTypeDef

### targetDatabaseEngine
- **Type**: typing.List[typing.Literal['AWS PostgreSQL', 'Amazon Aurora', 'Db2 LUW', 'MariaDB', 'Microsoft SQL Server', 'MongoDB', 'MySQL', 'None specified', 'Oracle Database', 'SAP']]
- **Required**: Yes


# HomogeneousTypeDef

### targetDatabaseEngine
- **Type**: typing.Optional[typing.List[typing.Literal['None specified']]]


# IPAddressBasedRemoteInfoTypeDef

### authType
- **Type**: typing.Optional[typing.Literal['CERT', 'NTLM', 'SSH']]

### ipAddressConfigurationTimeStamp
- **Type**: typing.Optional[str]

### osType
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]


# ImportFileTaskInformationTypeDef

### completionTime
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### importName
- **Type**: typing.Optional[str]

### inputS3Bucket
- **Type**: typing.Optional[str]

### inputS3Key
- **Type**: typing.Optional[str]

### numberOfRecordsFailed
- **Type**: typing.Optional[int]

### numberOfRecordsSuccess
- **Type**: typing.Optional[int]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['DeleteFailed', 'DeleteInProgress', 'DeletePartialSuccess', 'DeleteSuccess', 'ImportFailed', 'ImportInProgress', 'ImportPartialSuccess', 'ImportSuccess']]

### statusReportS3Bucket
- **Type**: typing.Optional[str]

### statusReportS3Key
- **Type**: typing.Optional[str]


# ListAnalyzableServersRequestListAnalyzableServersPaginateTypeDef

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.PaginatorConfigTypeDef]


# ListAnalyzableServersRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListAnalyzableServersResponseTypeDef

### analyzableServers
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AnalyzableServerSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef

### applicationComponentCriteria
- **Type**: typing.Optional[typing.Literal['ANALYSIS_STATUS', 'APP_NAME', 'APP_TYPE', 'DESTINATION', 'ERROR_CATEGORY', 'NOT_DEFINED', 'SERVER_ID', 'STRATEGY']]

### filterValue
- **Type**: typing.Optional[str]

### groupIdFilter
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.GroupTypeDef]]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.PaginatorConfigTypeDef]


# ListApplicationComponentsRequestRequestTypeDef

### applicationComponentCriteria
- **Type**: typing.Optional[typing.Literal['ANALYSIS_STATUS', 'APP_NAME', 'APP_TYPE', 'DESTINATION', 'ERROR_CATEGORY', 'NOT_DEFINED', 'SERVER_ID', 'STRATEGY']]

### filterValue
- **Type**: typing.Optional[str]

### groupIdFilter
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.GroupTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListApplicationComponentsResponseTypeDef

### applicationComponentInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ApplicationComponentDetailTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCollectorsRequestListCollectorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.PaginatorConfigTypeDef]


# ListCollectorsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCollectorsResponseTypeDef

### Collectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.CollectorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImportFileTaskRequestListImportFileTaskPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.PaginatorConfigTypeDef]


# ListImportFileTaskRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImportFileTaskResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### taskInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ImportFileTaskInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServersRequestListServersPaginateTypeDef

### filterValue
- **Type**: typing.Optional[str]

### groupIdFilter
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.GroupTypeDef]]

### serverCriteria
- **Type**: typing.Optional[typing.Literal['ANALYSIS_STATUS', 'DESTINATION', 'ERROR_CATEGORY', 'NOT_DEFINED', 'OS_NAME', 'SERVER_ID', 'STRATEGY']]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.PaginatorConfigTypeDef]


# ListServersRequestRequestTypeDef

### filterValue
- **Type**: typing.Optional[str]

### groupIdFilter
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.GroupTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### serverCriteria
- **Type**: typing.Optional[typing.Literal['ANALYSIS_STATUS', 'DESTINATION', 'ERROR_CATEGORY', 'NOT_DEFINED', 'OS_NAME', 'SERVER_ID', 'STRATEGY']]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListServersResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### serverInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ServerDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManagementPreferenceTypeDef

### awsManagedResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AwsManagedResourcesTypeDef]

### noPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.NoManagementPreferenceTypeDef]

### selfManageResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.SelfManageResourcesTypeDef]


# NetworkInfoTypeDef

### interfaceName
- **Type**: <class 'str'>
- **Required**: Yes

### ipAddress
- **Type**: <class 'str'>
- **Required**: Yes

### macAddress
- **Type**: <class 'str'>
- **Required**: Yes

### netMask
- **Type**: <class 'str'>
- **Required**: Yes


# NoDatabaseMigrationPreferenceTypeDef

### targetDatabaseEngine
- **Type**: typing.List[typing.Literal['AWS PostgreSQL', 'Amazon Aurora', 'Db2 LUW', 'MariaDB', 'Microsoft SQL Server', 'MongoDB', 'MySQL', 'None specified', 'Oracle Database', 'SAP']]
- **Required**: Yes


# NoManagementPreferenceTypeDef

### targetDestination
- **Type**: typing.List[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'None specified']]
- **Required**: Yes


# OSInfoTypeDef

### type
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]

### version
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PipelineInfoTypeDef

### pipelineConfigurationTimeStamp
- **Type**: typing.Optional[str]

### pipelineType
- **Type**: typing.Optional[typing.Literal['AZURE_DEVOPS']]


# PrioritizeBusinessGoalsTypeDef

### businessGoals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.BusinessGoalsTypeDef]


# PutPortfolioPreferencesRequestRequestTypeDef

### applicationMode
- **Type**: typing.Optional[typing.Literal['ALL', 'KNOWN', 'UNKNOWN']]

### applicationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ApplicationPreferencesTypeDef]

### databasePreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.DatabasePreferencesTypeDef]

### prioritizeBusinessGoals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.PrioritizeBusinessGoalsTypeDef]


# RecommendationReportDetailsTypeDef

### completionTime
- **Type**: typing.Optional[datetime.datetime]

### s3Bucket
- **Type**: typing.Optional[str]

### s3Keys
- **Type**: typing.Optional[typing.List[str]]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### statusMessage
- **Type**: typing.Optional[str]


# RecommendationSetTypeDef

### strategy
- **Type**: typing.Optional[typing.Literal['Refactor', 'Rehost', 'Relocate', 'Replatform', 'Repurchase', 'Retain', 'Retirement']]

### targetDestination
- **Type**: typing.Optional[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'Amazon DocumentDB', 'Amazon DynamoDB', 'Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'Amazon Relational Database Service', 'Amazon Relational Database Service on MySQL', 'Amazon Relational Database Service on PostgreSQL', 'Aurora MySQL', 'Aurora PostgreSQL', 'Babelfish for Aurora PostgreSQL', 'None specified']]

### transformationTool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.TransformationToolTypeDef]


# RemoteSourceCodeAnalysisServerInfoTypeDef

### remoteSourceCodeAnalysisServerConfigurationTimestamp
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# ResultTypeDef

### analysisStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AnalysisStatusUnionTypeDef]

### analysisType
- **Type**: typing.Optional[typing.Literal['BINARY_ANALYSIS', 'DATABASE_ANALYSIS', 'RUNTIME_ANALYSIS', 'SOURCE_CODE_ANALYSIS']]

### antipatternReportResultList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AntipatternReportResultTypeDef]]

### statusMessage
- **Type**: typing.Optional[str]


# S3ObjectTypeDef

### s3Bucket
- **Type**: typing.Optional[str]

### s3key
- **Type**: typing.Optional[str]


# SelfManageResourcesTypeDef

### targetDestination
- **Type**: typing.List[typing.Literal['Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'None specified']]
- **Required**: Yes


# ServerDetailTypeDef

### antipatternReportS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.S3ObjectTypeDef]

### antipatternReportStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### antipatternReportStatusMessage
- **Type**: typing.Optional[str]

### applicationComponentStrategySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.StrategySummaryTypeDef]]

### dataCollectionStatus
- **Type**: typing.Optional[typing.Literal['dataCollectionTaskFailed', 'dataCollectionTaskPartialSuccess', 'dataCollectionTaskScheduled', 'dataCollectionTaskStarted', 'dataCollectionTaskStopped', 'dataCollectionTaskSuccess', 'dataCollectionTaskToBeScheduled']]

### id
- **Type**: typing.Optional[str]

### lastAnalyzedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### listAntipatternSeveritySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AntipatternSeveritySummaryTypeDef]]

### name
- **Type**: typing.Optional[str]

### recommendationSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.RecommendationSetTypeDef]

### serverError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ServerErrorTypeDef]

### serverType
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]

### systemInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.SystemInfoTypeDef]


# ServerErrorTypeDef

### serverErrorCategory
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_ERROR', 'CONNECTIVITY_ERROR', 'CREDENTIAL_ERROR', 'OTHER_ERROR', 'PERMISSION_ERROR']]


# ServerStatusSummaryTypeDef

### count
- **Type**: typing.Optional[int]

### runTimeAssessmentStatus
- **Type**: typing.Optional[typing.Literal['dataCollectionTaskFailed', 'dataCollectionTaskPartialSuccess', 'dataCollectionTaskScheduled', 'dataCollectionTaskStarted', 'dataCollectionTaskStopped', 'dataCollectionTaskSuccess', 'dataCollectionTaskToBeScheduled']]


# ServerStrategyTypeDef

### isPreferred
- **Type**: typing.Optional[bool]

### numberOfApplicationComponents
- **Type**: typing.Optional[int]

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.RecommendationSetTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['notRecommended', 'potential', 'recommended', 'viableOption']]


# ServerSummaryTypeDef

### ServerOsType
- **Type**: typing.Optional[typing.Literal['AmazonLinux', 'EndOfSupportWindowsServer', 'Other', 'Redhat', 'WindowsServer']]

### count
- **Type**: typing.Optional[int]


# SourceCodeRepositoryTypeDef

### branch
- **Type**: typing.Optional[str]

### projectName
- **Type**: typing.Optional[str]

### repository
- **Type**: typing.Optional[str]

### versionControlType
- **Type**: typing.Optional[str]


# SourceCodeTypeDef

### location
- **Type**: typing.Optional[str]

### projectName
- **Type**: typing.Optional[str]

### sourceVersion
- **Type**: typing.Optional[str]

### versionControl
- **Type**: typing.Optional[typing.Literal['AZURE_DEVOPS_GIT', 'GITHUB', 'GITHUB_ENTERPRISE']]


# StartAssessmentRequestRequestTypeDef

### assessmentDataSourceType
- **Type**: typing.Optional[typing.Literal['ApplicationDiscoveryService', 'ManualImport', 'StrategyRecommendationsApplicationDataCollector']]

### assessmentTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.AssessmentTargetTypeDef]]

### s3bucketForAnalysisData
- **Type**: typing.Optional[str]

### s3bucketForReportData
- **Type**: typing.Optional[str]


# StartAssessmentResponseTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartImportFileTaskRequestRequestTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### s3key
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceType
- **Type**: typing.Optional[typing.Literal['ApplicationDiscoveryService', 'Import', 'MPA', 'StrategyRecommendationsApplicationDataCollector']]

### groupId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.GroupTypeDef]]

### s3bucketForReportData
- **Type**: typing.Optional[str]


# StartImportFileTaskResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartRecommendationReportGenerationRequestRequestTypeDef

### groupIdFilter
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.GroupTypeDef]]

### outputFormat
- **Type**: typing.Optional[typing.Literal['Excel', 'Json']]


# StartRecommendationReportGenerationResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopAssessmentRequestRequestTypeDef

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# StrategyOptionTypeDef

### isPreferred
- **Type**: typing.Optional[bool]

### strategy
- **Type**: typing.Optional[typing.Literal['Refactor', 'Rehost', 'Relocate', 'Replatform', 'Repurchase', 'Retain', 'Retirement']]

### targetDestination
- **Type**: typing.Optional[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'Amazon DocumentDB', 'Amazon DynamoDB', 'Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'Amazon Relational Database Service', 'Amazon Relational Database Service on MySQL', 'Amazon Relational Database Service on PostgreSQL', 'Aurora MySQL', 'Aurora PostgreSQL', 'Babelfish for Aurora PostgreSQL', 'None specified']]

### toolName
- **Type**: typing.Optional[typing.Literal['App2Container', 'Application Migration Service', 'Database Migration Service', 'End of Support Migration', 'In Place Operating System Upgrade', 'Native SQL Server Backup/Restore', 'Porting Assistant For .NET', 'Schema Conversion Tool', 'Strategy Recommendation Support', 'Windows Web Application Migration Assistant']]


# StrategySummaryTypeDef

### count
- **Type**: typing.Optional[int]

### strategy
- **Type**: typing.Optional[typing.Literal['Refactor', 'Rehost', 'Relocate', 'Replatform', 'Repurchase', 'Retain', 'Retirement']]


# SystemInfoTypeDef

### cpuArchitecture
- **Type**: typing.Optional[str]

### fileSystemType
- **Type**: typing.Optional[str]

### networkInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.NetworkInfoTypeDef]]

### osInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.OSInfoTypeDef]


# TransformationToolTypeDef

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[typing.Literal['App2Container', 'Application Migration Service', 'Database Migration Service', 'End of Support Migration', 'In Place Operating System Upgrade', 'Native SQL Server Backup/Restore', 'Porting Assistant For .NET', 'Schema Conversion Tool', 'Strategy Recommendation Support', 'Windows Web Application Migration Assistant']]

### tranformationToolInstallationLink
- **Type**: typing.Optional[str]


# UpdateApplicationComponentConfigRequestRequestTypeDef

### applicationComponentId
- **Type**: <class 'str'>
- **Required**: Yes

### appType
- **Type**: typing.Optional[typing.Literal['Cassandra', 'DB2', 'DotNetFramework', 'Dotnet', 'DotnetCore', 'IBM WebSphere', 'IIS', 'JBoss', 'Java', 'Maria DB', 'Mongo DB', 'MySQL', 'Oracle', 'Oracle WebLogic', 'Other', 'PostgreSQLServer', 'SQLServer', 'Spring', 'Sybase', 'Tomcat', 'Unknown', 'Visual Basic']]

### configureOnly
- **Type**: typing.Optional[bool]

### inclusionStatus
- **Type**: typing.Optional[typing.Literal['excludeFromAssessment', 'includeInAssessment']]

### secretsManagerKey
- **Type**: typing.Optional[str]

### sourceCodeList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.SourceCodeTypeDef]]

### strategyOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.StrategyOptionTypeDef]


# UpdateServerConfigRequestRequestTypeDef

### serverId
- **Type**: <class 'str'>
- **Required**: Yes

### strategyOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy_classes.StrategyOptionTypeDef]


# VcenterBasedRemoteInfoTypeDef

### osType
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]

### vcenterConfigurationTimeStamp
- **Type**: typing.Optional[str]


# VersionControlInfoTypeDef

### versionControlConfigurationTimeStamp
- **Type**: typing.Optional[str]

### versionControlType
- **Type**: typing.Optional[typing.Literal['AZURE_DEVOPS_GIT', 'GITHUB', 'GITHUB_ENTERPRISE']]



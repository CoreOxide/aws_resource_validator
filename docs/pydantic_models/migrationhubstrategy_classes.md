# Migrationhubstrategy Classes

# AnalysisStatusUnion

### runtimeAnalysisStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED']]

### srcCodeOrDbAnalysisStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_PARTIAL_SUCCESS', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED', 'CONFIGURED', 'UNCONFIGURED']]


# AnalyzableServerSummary

### hostname
- **Type**: typing.Optional[str]

### ipAddress
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]

### vmId
- **Type**: typing.Optional[str]


# AnalyzerNameUnion

### binaryAnalyzerName
- **Type**: typing.Optional[typing.Literal['BYTECODE_ANALYZER', 'DLL_ANALYZER']]

### runTimeAnalyzerName
- **Type**: typing.Optional[typing.Literal['A2C_ANALYZER', 'DATABASE_ANALYZER', 'EMP_PA_ANALYZER', 'REHOST_ANALYZER', 'SCT_ANALYZER']]

### sourceCodeAnalyzerName
- **Type**: typing.Optional[typing.Literal['BYTECODE_ANALYZER', 'CSHARP_ANALYZER', 'JAVA_ANALYZER', 'PORTING_ASSISTANT']]


# AntipatternReportResult

### analyzerName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AnalyzerNameUnion]

### antiPatternReportS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.S3Object]

### antipatternReportStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### antipatternReportStatusMessage
- **Type**: typing.Optional[str]


# AntipatternSeveritySummary

### count
- **Type**: typing.Optional[int]

### severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# AppUnitError

### appUnitErrorCategory
- **Type**: typing.Optional[typing.Literal['CONNECTIVITY_ERROR', 'CREDENTIAL_ERROR', 'OTHER_ERROR', 'PERMISSION_ERROR', 'UNSUPPORTED_ERROR']]


# ApplicationComponentDetail

### analysisStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_PARTIAL_SUCCESS', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED', 'CONFIGURED', 'UNCONFIGURED']]

### antipatternReportS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.S3Object]

### antipatternReportStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### antipatternReportStatusMessage
- **Type**: typing.Optional[str]

### appType
- **Type**: typing.Optional[typing.Literal['Cassandra', 'DB2', 'DotNetFramework', 'Dotnet', 'DotnetCore', 'IBM WebSphere', 'IIS', 'JBoss', 'Java', 'Maria DB', 'Mongo DB', 'MySQL', 'Oracle', 'Oracle WebLogic', 'Other', 'PostgreSQLServer', 'SQLServer', 'Spring', 'Sybase', 'Tomcat', 'Unknown', 'Visual Basic']]

### appUnitError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AppUnitError]

### associatedServerId
- **Type**: typing.Optional[str]

### databaseConfigDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.DatabaseConfigDetail]

### id
- **Type**: typing.Optional[str]

### inclusionStatus
- **Type**: typing.Optional[typing.Literal['excludeFromAssessment', 'includeInAssessment']]

### lastAnalyzedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### listAntipatternSeveritySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AntipatternSeveritySummary]]

### moreServerAssociationExists
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### osDriver
- **Type**: typing.Optional[str]

### osVersion
- **Type**: typing.Optional[str]

### recommendationSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.RecommendationSet]

### resourceSubType
- **Type**: typing.Optional[typing.Literal['Database', 'DatabaseProcess', 'Process']]

### resultList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Result]]

### runtimeStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED']]

### runtimeStatusMessage
- **Type**: typing.Optional[str]

### sourceCodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.SourceCodeRepository]]

### statusMessage
- **Type**: typing.Optional[str]


# ApplicationComponentStatusSummary

### count
- **Type**: typing.Optional[int]

### srcCodeOrDbAnalysisStatus
- **Type**: typing.Optional[typing.Literal['ANALYSIS_FAILED', 'ANALYSIS_PARTIAL_SUCCESS', 'ANALYSIS_STARTED', 'ANALYSIS_SUCCESS', 'ANALYSIS_TO_BE_SCHEDULED', 'CONFIGURED', 'UNCONFIGURED']]


# ApplicationComponentStrategy

### isPreferred
- **Type**: typing.Optional[bool]

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.RecommendationSet]

### status
- **Type**: typing.Optional[typing.Literal['notRecommended', 'potential', 'recommended', 'viableOption']]


# ApplicationComponentSummary

### appType
- **Type**: typing.Optional[typing.Literal['Cassandra', 'DB2', 'DotNetFramework', 'Dotnet', 'DotnetCore', 'IBM WebSphere', 'IIS', 'JBoss', 'Java', 'Maria DB', 'Mongo DB', 'MySQL', 'Oracle', 'Oracle WebLogic', 'Other', 'PostgreSQLServer', 'SQLServer', 'Spring', 'Sybase', 'Tomcat', 'Unknown', 'Visual Basic']]

### count
- **Type**: typing.Optional[int]


# ApplicationPreferences

### managementPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ManagementPreference]


# ApplicationPreferencesOutput

### managementPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ManagementPreferenceOutput]


# AssessmentSummary

### antipatternReportS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.S3Object]

### antipatternReportStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### antipatternReportStatusMessage
- **Type**: typing.Optional[str]

### lastAnalyzedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### listAntipatternSeveritySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AntipatternSeveritySummary]]

### listApplicationComponentStatusSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ApplicationComponentStatusSummary]]

### listApplicationComponentStrategySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.StrategySummary]]

### listApplicationComponentSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ApplicationComponentSummary]]

### listServerStatusSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ServerStatusSummary]]

### listServerStrategySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.StrategySummary]]

### listServerSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ServerSummary]]


# AssessmentTarget

### condition
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# AssessmentTargetOutput

### condition
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# AssociatedApplication

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AwsManagedResources

### targetDestination
- **Type**: typing.List[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'None specified']]
- **Required**: Yes


# AwsManagedResourcesOutput

### targetDestination
- **Type**: typing.List[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'None specified']]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BusinessGoals

### licenseCostReduction
- **Type**: typing.Optional[int]

### modernizeInfrastructureWithCloudNativeTechnologies
- **Type**: typing.Optional[int]

### reduceOperationalOverheadWithManagedServices
- **Type**: typing.Optional[int]

### speedOfMigration
- **Type**: typing.Optional[int]


# Collector

### collectorHealth
- **Type**: typing.Optional[typing.Literal['COLLECTOR_HEALTHY', 'COLLECTOR_UNHEALTHY']]

### collectorId
- **Type**: typing.Optional[str]

### collectorVersion
- **Type**: typing.Optional[str]

### configurationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ConfigurationSummary]

### hostName
- **Type**: typing.Optional[str]

### ipAddress
- **Type**: typing.Optional[str]

### lastActivityTimeStamp
- **Type**: typing.Optional[str]

### registeredTimeStamp
- **Type**: typing.Optional[str]


# ConfigurationSummary

### ipAddressBasedRemoteInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.IPAddressBasedRemoteInfo]]

### pipelineInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.PipelineInfo]]

### remoteSourceCodeAnalysisServerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.RemoteSourceCodeAnalysisServerInfo]

### vcenterBasedRemoteInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.VcenterBasedRemoteInfo]]

### versionControlInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.VersionControlInfo]]


# DataCollectionDetails

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


# DatabaseConfigDetail

### secretName
- **Type**: typing.Optional[str]


# DatabaseMigrationPreference

### heterogeneous
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Heterogeneous]

### homogeneous
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Homogeneous]

### noPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.NoDatabaseMigrationPreference]


# DatabaseMigrationPreferenceOutput

### heterogeneous
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.HeterogeneousOutput]

### homogeneous
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.HomogeneousOutput]

### noPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.NoDatabaseMigrationPreferenceOutput]


# DatabasePreferences

### databaseManagementPreference
- **Type**: typing.Optional[typing.Literal['AWS-managed', 'No preference', 'Self-manage']]

### databaseMigrationPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.DatabaseMigrationPreference]


# DatabasePreferencesOutput

### databaseManagementPreference
- **Type**: typing.Optional[typing.Literal['AWS-managed', 'No preference', 'Self-manage']]

### databaseMigrationPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.DatabaseMigrationPreferenceOutput]


# GetApplicationComponentDetailsRequest

### applicationComponentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationComponentDetailsResponse

### applicationComponentDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ApplicationComponentDetail'>
- **Required**: Yes

### associatedApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AssociatedApplication]
- **Required**: Yes

### associatedServerIds
- **Type**: typing.List[str]
- **Required**: Yes

### moreApplicationResource
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationComponentStrategiesRequest

### applicationComponentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationComponentStrategiesResponse

### applicationComponentStrategies
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ApplicationComponentStrategy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssessmentRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssessmentResponse

### assessmentTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AssessmentTargetOutput]
- **Required**: Yes

### dataCollectionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.DataCollectionDetails'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# GetImportFileTaskRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportFileTaskResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# GetLatestAssessmentIdResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# GetPortfolioPreferencesResponse

### applicationMode
- **Type**: typing.Literal['ALL', 'KNOWN', 'UNKNOWN']
- **Required**: Yes

### applicationPreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ApplicationPreferencesOutput'>
- **Required**: Yes

### databasePreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.DatabasePreferencesOutput'>
- **Required**: Yes

### prioritizeBusinessGoals
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.PrioritizeBusinessGoals'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# GetPortfolioSummaryResponse

### assessmentSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AssessmentSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecommendationReportDetailsRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecommendationReportDetailsResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationReportDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.RecommendationReportDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# GetServerDetailsRequest

### serverId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetServerDetailsRequestPaginate

### serverId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.PaginatorConfig]


# GetServerDetailsResponse

### associatedApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AssociatedApplication]
- **Required**: Yes

### serverDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ServerDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetServerStrategiesRequest

### serverId
- **Type**: <class 'str'>
- **Required**: Yes


# GetServerStrategiesResponse

### serverStrategies
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ServerStrategy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# Group

### name
- **Type**: typing.Optional[typing.Literal['ExternalId', 'ExternalSourceType']]

### value
- **Type**: typing.Optional[str]


# Heterogeneous

### targetDatabaseEngine
- **Type**: typing.List[typing.Literal['AWS PostgreSQL', 'Amazon Aurora', 'Db2 LUW', 'MariaDB', 'Microsoft SQL Server', 'MongoDB', 'MySQL', 'None specified', 'Oracle Database', 'SAP']]
- **Required**: Yes


# HeterogeneousOutput

### targetDatabaseEngine
- **Type**: typing.List[typing.Literal['AWS PostgreSQL', 'Amazon Aurora', 'Db2 LUW', 'MariaDB', 'Microsoft SQL Server', 'MongoDB', 'MySQL', 'None specified', 'Oracle Database', 'SAP']]
- **Required**: Yes


# Homogeneous

### targetDatabaseEngine
- **Type**: typing.Optional[typing.List[typing.Literal['None specified']]]


# HomogeneousOutput

### targetDatabaseEngine
- **Type**: typing.Optional[typing.List[typing.Literal['None specified']]]


# IPAddressBasedRemoteInfo

### authType
- **Type**: typing.Optional[typing.Literal['CERT', 'NTLM', 'SSH']]

### ipAddressConfigurationTimeStamp
- **Type**: typing.Optional[str]

### osType
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]


# ImportFileTaskInformation

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


# ListAnalyzableServersRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListAnalyzableServersRequestPaginate

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.PaginatorConfig]


# ListAnalyzableServersResponse

### analyzableServers
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AnalyzableServerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationComponentsRequest

### applicationComponentCriteria
- **Type**: typing.Optional[typing.Literal['ANALYSIS_STATUS', 'APP_NAME', 'APP_TYPE', 'DESTINATION', 'ERROR_CATEGORY', 'NOT_DEFINED', 'SERVER_ID', 'STRATEGY']]

### filterValue
- **Type**: typing.Optional[str]

### groupIdFilter
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Group]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListApplicationComponentsRequestPaginate

### applicationComponentCriteria
- **Type**: typing.Optional[typing.Literal['ANALYSIS_STATUS', 'APP_NAME', 'APP_TYPE', 'DESTINATION', 'ERROR_CATEGORY', 'NOT_DEFINED', 'SERVER_ID', 'STRATEGY']]

### filterValue
- **Type**: typing.Optional[str]

### groupIdFilter
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Group]]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.PaginatorConfig]


# ListApplicationComponentsResponse

### applicationComponentInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ApplicationComponentDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollectorsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCollectorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.PaginatorConfig]


# ListCollectorsResponse

### Collectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Collector]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportFileTaskRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImportFileTaskRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.PaginatorConfig]


# ListImportFileTaskResponse

### taskInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ImportFileTaskInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServersRequest

### filterValue
- **Type**: typing.Optional[str]

### groupIdFilter
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Group]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### serverCriteria
- **Type**: typing.Optional[typing.Literal['ANALYSIS_STATUS', 'DESTINATION', 'ERROR_CATEGORY', 'NOT_DEFINED', 'OS_NAME', 'SERVER_ID', 'STRATEGY']]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListServersRequestPaginate

### filterValue
- **Type**: typing.Optional[str]

### groupIdFilter
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Group]]

### serverCriteria
- **Type**: typing.Optional[typing.Literal['ANALYSIS_STATUS', 'DESTINATION', 'ERROR_CATEGORY', 'NOT_DEFINED', 'OS_NAME', 'SERVER_ID', 'STRATEGY']]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.PaginatorConfig]


# ListServersResponse

### serverInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ServerDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ManagementPreference

### awsManagedResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AwsManagedResources]

### noPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.NoManagementPreference]

### selfManageResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.SelfManageResources]


# ManagementPreferenceOutput

### awsManagedResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AwsManagedResourcesOutput]

### noPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.NoManagementPreferenceOutput]

### selfManageResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.SelfManageResourcesOutput]


# NetworkInfo

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


# NoDatabaseMigrationPreference

### targetDatabaseEngine
- **Type**: typing.List[typing.Literal['AWS PostgreSQL', 'Amazon Aurora', 'Db2 LUW', 'MariaDB', 'Microsoft SQL Server', 'MongoDB', 'MySQL', 'None specified', 'Oracle Database', 'SAP']]
- **Required**: Yes


# NoDatabaseMigrationPreferenceOutput

### targetDatabaseEngine
- **Type**: typing.List[typing.Literal['AWS PostgreSQL', 'Amazon Aurora', 'Db2 LUW', 'MariaDB', 'Microsoft SQL Server', 'MongoDB', 'MySQL', 'None specified', 'Oracle Database', 'SAP']]
- **Required**: Yes


# NoManagementPreference

### targetDestination
- **Type**: typing.List[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'None specified']]
- **Required**: Yes


# NoManagementPreferenceOutput

### targetDestination
- **Type**: typing.List[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'None specified']]
- **Required**: Yes


# OSInfo

### type
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]

### version
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PipelineInfo

### pipelineConfigurationTimeStamp
- **Type**: typing.Optional[str]

### pipelineType
- **Type**: typing.Optional[typing.Literal['AZURE_DEVOPS']]


# PrioritizeBusinessGoals

### businessGoals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.BusinessGoals]


# PutPortfolioPreferencesRequest

### applicationMode
- **Type**: typing.Optional[typing.Literal['ALL', 'KNOWN', 'UNKNOWN']]

### applicationPreferences
- **Type**: typing.Union[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ApplicationPreferences, aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ApplicationPreferencesOutput, NoneType]

### databasePreferences
- **Type**: typing.Union[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.DatabasePreferences, aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.DatabasePreferencesOutput, NoneType]

### prioritizeBusinessGoals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.PrioritizeBusinessGoals]


# RecommendationReportDetails

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


# RecommendationSet

### strategy
- **Type**: typing.Optional[typing.Literal['Refactor', 'Rehost', 'Relocate', 'Replatform', 'Repurchase', 'Retain', 'Retirement']]

### targetDestination
- **Type**: typing.Optional[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'Amazon DocumentDB', 'Amazon DynamoDB', 'Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'Amazon Relational Database Service', 'Amazon Relational Database Service on MySQL', 'Amazon Relational Database Service on PostgreSQL', 'Aurora MySQL', 'Aurora PostgreSQL', 'Babelfish for Aurora PostgreSQL', 'None specified']]

### transformationTool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.TransformationTool]


# RemoteSourceCodeAnalysisServerInfo

### remoteSourceCodeAnalysisServerConfigurationTimestamp
- **Type**: typing.Optional[str]


# ResponseMetadata

### RequestId
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

### HostId
- **Type**: typing.Optional[str]


# Result

### analysisStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AnalysisStatusUnion]

### analysisType
- **Type**: typing.Optional[typing.Literal['BINARY_ANALYSIS', 'DATABASE_ANALYSIS', 'RUNTIME_ANALYSIS', 'SOURCE_CODE_ANALYSIS']]

### antipatternReportResultList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AntipatternReportResult]]

### statusMessage
- **Type**: typing.Optional[str]


# S3Object

### s3Bucket
- **Type**: typing.Optional[str]

### s3key
- **Type**: typing.Optional[str]


# SelfManageResources

### targetDestination
- **Type**: typing.List[typing.Literal['Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'None specified']]
- **Required**: Yes


# SelfManageResourcesOutput

### targetDestination
- **Type**: typing.List[typing.Literal['Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'None specified']]
- **Required**: Yes


# ServerDetail

### antipatternReportS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.S3Object]

### antipatternReportStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### antipatternReportStatusMessage
- **Type**: typing.Optional[str]

### applicationComponentStrategySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.StrategySummary]]

### dataCollectionStatus
- **Type**: typing.Optional[typing.Literal['dataCollectionTaskFailed', 'dataCollectionTaskPartialSuccess', 'dataCollectionTaskScheduled', 'dataCollectionTaskStarted', 'dataCollectionTaskStopped', 'dataCollectionTaskSuccess', 'dataCollectionTaskToBeScheduled']]

### id
- **Type**: typing.Optional[str]

### lastAnalyzedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### listAntipatternSeveritySummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AntipatternSeveritySummary]]

### name
- **Type**: typing.Optional[str]

### recommendationSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.RecommendationSet]

### serverError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ServerError]

### serverType
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]

### systemInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.SystemInfo]


# ServerError

### serverErrorCategory
- **Type**: typing.Optional[typing.Literal['ARCHITECTURE_ERROR', 'CONNECTIVITY_ERROR', 'CREDENTIAL_ERROR', 'OTHER_ERROR', 'PERMISSION_ERROR']]


# ServerStatusSummary

### count
- **Type**: typing.Optional[int]

### runTimeAssessmentStatus
- **Type**: typing.Optional[typing.Literal['dataCollectionTaskFailed', 'dataCollectionTaskPartialSuccess', 'dataCollectionTaskScheduled', 'dataCollectionTaskStarted', 'dataCollectionTaskStopped', 'dataCollectionTaskSuccess', 'dataCollectionTaskToBeScheduled']]


# ServerStrategy

### isPreferred
- **Type**: typing.Optional[bool]

### numberOfApplicationComponents
- **Type**: typing.Optional[int]

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.RecommendationSet]

### status
- **Type**: typing.Optional[typing.Literal['notRecommended', 'potential', 'recommended', 'viableOption']]


# ServerSummary

### ServerOsType
- **Type**: typing.Optional[typing.Literal['AmazonLinux', 'EndOfSupportWindowsServer', 'Other', 'Redhat', 'WindowsServer']]

### count
- **Type**: typing.Optional[int]


# SourceCode

### location
- **Type**: typing.Optional[str]

### projectName
- **Type**: typing.Optional[str]

### sourceVersion
- **Type**: typing.Optional[str]

### versionControl
- **Type**: typing.Optional[typing.Literal['AZURE_DEVOPS_GIT', 'GITHUB', 'GITHUB_ENTERPRISE']]


# SourceCodeRepository

### branch
- **Type**: typing.Optional[str]

### projectName
- **Type**: typing.Optional[str]

### repository
- **Type**: typing.Optional[str]

### versionControlType
- **Type**: typing.Optional[str]


# StartAssessmentRequest

### assessmentDataSourceType
- **Type**: typing.Optional[typing.Literal['ApplicationDiscoveryService', 'ManualImport', 'StrategyRecommendationsApplicationDataCollector']]

### assessmentTargets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AssessmentTarget, aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.AssessmentTargetOutput]]]

### s3bucketForAnalysisData
- **Type**: typing.Optional[str]

### s3bucketForReportData
- **Type**: typing.Optional[str]


# StartAssessmentResponse

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# StartImportFileTaskRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Group]]

### s3bucketForReportData
- **Type**: typing.Optional[str]


# StartImportFileTaskResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# StartRecommendationReportGenerationRequest

### groupIdFilter
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.Group]]

### outputFormat
- **Type**: typing.Optional[typing.Literal['Excel', 'Json']]


# StartRecommendationReportGenerationResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.ResponseMetadata'>
- **Required**: Yes


# StopAssessmentRequest

### assessmentId
- **Type**: <class 'str'>
- **Required**: Yes


# StrategyOption

### isPreferred
- **Type**: typing.Optional[bool]

### strategy
- **Type**: typing.Optional[typing.Literal['Refactor', 'Rehost', 'Relocate', 'Replatform', 'Repurchase', 'Retain', 'Retirement']]

### targetDestination
- **Type**: typing.Optional[typing.Literal['AWS Elastic BeanStalk', 'AWS Fargate', 'Amazon DocumentDB', 'Amazon DynamoDB', 'Amazon Elastic Cloud Compute (EC2)', 'Amazon Elastic Container Service (ECS)', 'Amazon Elastic Kubernetes Service (EKS)', 'Amazon Relational Database Service', 'Amazon Relational Database Service on MySQL', 'Amazon Relational Database Service on PostgreSQL', 'Aurora MySQL', 'Aurora PostgreSQL', 'Babelfish for Aurora PostgreSQL', 'None specified']]

### toolName
- **Type**: typing.Optional[typing.Literal['App2Container', 'Application Migration Service', 'Database Migration Service', 'End of Support Migration', 'In Place Operating System Upgrade', 'Native SQL Server Backup/Restore', 'Porting Assistant For .NET', 'Schema Conversion Tool', 'Strategy Recommendation Support', 'Windows Web Application Migration Assistant']]


# StrategySummary

### count
- **Type**: typing.Optional[int]

### strategy
- **Type**: typing.Optional[typing.Literal['Refactor', 'Rehost', 'Relocate', 'Replatform', 'Repurchase', 'Retain', 'Retirement']]


# SystemInfo

### cpuArchitecture
- **Type**: typing.Optional[str]

### fileSystemType
- **Type**: typing.Optional[str]

### networkInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.NetworkInfo]]

### osInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.OSInfo]


# TransformationTool

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[typing.Literal['App2Container', 'Application Migration Service', 'Database Migration Service', 'End of Support Migration', 'In Place Operating System Upgrade', 'Native SQL Server Backup/Restore', 'Porting Assistant For .NET', 'Schema Conversion Tool', 'Strategy Recommendation Support', 'Windows Web Application Migration Assistant']]

### tranformationToolInstallationLink
- **Type**: typing.Optional[str]


# UpdateApplicationComponentConfigRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.SourceCode]]

### strategyOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.StrategyOption]


# UpdateServerConfigRequest

### serverId
- **Type**: <class 'str'>
- **Required**: Yes

### strategyOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhubstrategy.migrationhubstrategy_classes.StrategyOption]


# VcenterBasedRemoteInfo

### osType
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]

### vcenterConfigurationTimeStamp
- **Type**: typing.Optional[str]


# VersionControlInfo

### versionControlConfigurationTimeStamp
- **Type**: typing.Optional[str]

### versionControlType
- **Type**: typing.Optional[typing.Literal['AZURE_DEVOPS_GIT', 'GITHUB', 'GITHUB_ENTERPRISE']]



# apptest_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchOutputTypeDef

### batchJobName
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]


# BatchStepInputTypeDef

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.MainframeResourceSummaryTypeDef'>
- **Required**: Yes

### batchJobName
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.MainframeActionPropertiesTypeDef]


# BatchStepOutputTypeDef

### dataSetExportLocation
- **Type**: typing.Optional[str]

### dmsOutputLocation
- **Type**: typing.Optional[str]

### dataSetDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apptest_classes.DataSetTypeDef]]


# BatchSummaryTypeDef

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.BatchStepInputTypeDef'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.BatchStepOutputTypeDef]


# BatchTypeDef

### batchJobName
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### exportDataSetNames
- **Type**: typing.Optional[typing.Sequence[str]]


# CloudFormationActionTypeDef

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: typing.Optional[typing.Literal['Create', 'Delete']]


# CloudFormationOutputTypeDef

### templateLocation
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# CloudFormationStepSummaryTypeDef

### createCloudformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CreateCloudFormationSummaryTypeDef]

### deleteCloudformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.DeleteCloudFormationSummaryTypeDef]


# CloudFormationTypeDef

### templateLocation
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CompareActionOutputTypeDef

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.InputOutputTypeDef'>
- **Required**: Yes

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.OutputTypeDef]


# CompareActionSummaryTypeDef

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.FileTypeDef'>
- **Required**: Yes


# CompareActionTypeDef

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.InputTypeDef'>
- **Required**: Yes

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.OutputTypeDef]


# CompareDataSetsStepInputTypeDef

### sourceLocation
- **Type**: <class 'str'>
- **Required**: Yes

### targetLocation
- **Type**: <class 'str'>
- **Required**: Yes

### sourceDataSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.DataSetTypeDef]
- **Required**: Yes

### targetDataSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.DataSetTypeDef]
- **Required**: Yes


# CompareDataSetsStepOutputTypeDef

### comparisonOutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### comparisonStatus
- **Type**: typing.Literal['Different', 'Equal', 'Equivalent']
- **Required**: Yes


# CompareDataSetsSummaryTypeDef

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.CompareDataSetsStepInputTypeDef'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CompareDataSetsStepOutputTypeDef]


# CompareDatabaseCDCStepInputTypeDef

### sourceLocation
- **Type**: <class 'str'>
- **Required**: Yes

### targetLocation
- **Type**: <class 'str'>
- **Required**: Yes

### sourceMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.SourceDatabaseMetadataTypeDef'>
- **Required**: Yes

### targetMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.TargetDatabaseMetadataTypeDef'>
- **Required**: Yes

### outputLocation
- **Type**: typing.Optional[str]


# CompareDatabaseCDCStepOutputTypeDef

### comparisonOutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### comparisonStatus
- **Type**: typing.Literal['Different', 'Equal', 'Equivalent']
- **Required**: Yes


# CompareDatabaseCDCSummaryTypeDef

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.CompareDatabaseCDCStepInputTypeDef'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CompareDatabaseCDCStepOutputTypeDef]


# CompareFileTypeTypeDef

### datasets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CompareDataSetsSummaryTypeDef]

### databaseCDC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CompareDatabaseCDCSummaryTypeDef]


# CreateCloudFormationStepInputTypeDef

### templateLocation
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCloudFormationStepOutputTypeDef

### stackId
- **Type**: <class 'str'>
- **Required**: Yes

### exports
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCloudFormationSummaryTypeDef

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.CreateCloudFormationStepInputTypeDef'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CreateCloudFormationStepOutputTypeDef]


# CreateTestCaseRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### steps
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.apptest_classes.StepTypeDef, aws_resource_validator.pydantic_models.apptest_classes.StepOutputTypeDef]]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTestCaseResponseTypeDef

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTestConfigurationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resources
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.apptest_classes.ResourceTypeDef, aws_resource_validator.pydantic_models.apptest_classes.ResourceOutputTypeDef]]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### serviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.ServiceSettingsTypeDef]


# CreateTestConfigurationResponseTypeDef

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### testConfigurationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTestSuiteRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### testCases
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.TestCasesTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### beforeSteps
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.apptest_classes.StepTypeDef, aws_resource_validator.pydantic_models.apptest_classes.StepOutputTypeDef]]]

### afterSteps
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.apptest_classes.StepTypeDef, aws_resource_validator.pydantic_models.apptest_classes.StepOutputTypeDef]]]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTestSuiteResponseTypeDef

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSetTypeDef

### type
- **Type**: typing.Literal['PS']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ccsid
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['FIXED', 'LINE_SEQUENTIAL', 'VARIABLE']
- **Required**: Yes

### length
- **Type**: <class 'int'>
- **Required**: Yes


# DatabaseCDCTypeDef

### sourceMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.SourceDatabaseMetadataTypeDef'>
- **Required**: Yes

### targetMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.TargetDatabaseMetadataTypeDef'>
- **Required**: Yes


# DeleteCloudFormationStepInputTypeDef

### stackId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCloudFormationSummaryTypeDef

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.DeleteCloudFormationStepInputTypeDef'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# DeleteTestCaseRequestRequestTypeDef

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTestConfigurationRequestRequestTypeDef

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTestRunRequestRequestTypeDef

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTestSuiteRequestRequestTypeDef

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes


# FileMetadataOutputTypeDef

### dataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apptest_classes.DataSetTypeDef]]

### databaseCDC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.DatabaseCDCTypeDef]


# FileMetadataTypeDef

### dataSets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apptest_classes.DataSetTypeDef]]

### databaseCDC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.DatabaseCDCTypeDef]


# FileTypeDef

### fileType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CompareFileTypeTypeDef]


# GetTestCaseRequestRequestTypeDef

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseVersion
- **Type**: typing.Optional[int]


# GetTestCaseResponseTypeDef

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.TestCaseLatestVersionTypeDef'>
- **Required**: Yes

### testCaseVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.StepOutputTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTestConfigurationRequestRequestTypeDef

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### testConfigurationVersion
- **Type**: typing.Optional[int]


# GetTestConfigurationResponseTypeDef

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### testConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.TestConfigurationLatestVersionTypeDef'>
- **Required**: Yes

### testConfigurationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.ResourceOutputTypeDef]
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### serviceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ServiceSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTestRunStepRequestRequestTypeDef

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### stepName
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseId
- **Type**: typing.Optional[str]

### testSuiteId
- **Type**: typing.Optional[str]


# GetTestRunStepResponseTypeDef

### stepName
- **Type**: <class 'str'>
- **Required**: Yes

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseVersion
- **Type**: <class 'int'>
- **Required**: Yes

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteVersion
- **Type**: <class 'int'>
- **Required**: Yes

### beforeStep
- **Type**: <class 'bool'>
- **Required**: Yes

### afterStep
- **Type**: <class 'bool'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'Running', 'Success']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### runStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### runEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stepRunSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.StepRunSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTestSuiteRequestRequestTypeDef

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteVersion
- **Type**: typing.Optional[int]


# GetTestSuiteResponseTypeDef

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.TestSuiteLatestVersionTypeDef'>
- **Required**: Yes

### testSuiteVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Creating', 'Deleting', 'Failed', 'Updating']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### beforeSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.StepOutputTypeDef]
- **Required**: Yes

### afterSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.StepOutputTypeDef]
- **Required**: Yes

### testCases
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.TestCasesOutputTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputFileOutputTypeDef

### sourceLocation
- **Type**: <class 'str'>
- **Required**: Yes

### targetLocation
- **Type**: <class 'str'>
- **Required**: Yes

### fileMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.FileMetadataOutputTypeDef'>
- **Required**: Yes


# InputFileTypeDef

### sourceLocation
- **Type**: <class 'str'>
- **Required**: Yes

### targetLocation
- **Type**: <class 'str'>
- **Required**: Yes

### fileMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.FileMetadataTypeDef'>
- **Required**: Yes


# InputOutputTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.InputFileOutputTypeDef]


# InputTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.InputFileTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestCasesRequestListTestCasesPaginateTypeDef

### testCaseIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.PaginatorConfigTypeDef]


# ListTestCasesRequestRequestTypeDef

### testCaseIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestCasesResponseTypeDef

### testCases
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.TestCaseSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestConfigurationsRequestListTestConfigurationsPaginateTypeDef

### testConfigurationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.PaginatorConfigTypeDef]


# ListTestConfigurationsRequestRequestTypeDef

### testConfigurationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestConfigurationsResponseTypeDef

### testConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.TestConfigurationSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestRunStepsRequestListTestRunStepsPaginateTypeDef

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseId
- **Type**: typing.Optional[str]

### testSuiteId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.PaginatorConfigTypeDef]


# ListTestRunStepsRequestRequestTypeDef

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseId
- **Type**: typing.Optional[str]

### testSuiteId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestRunStepsResponseTypeDef

### testRunSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.TestRunStepSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestRunTestCasesRequestListTestRunTestCasesPaginateTypeDef

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.PaginatorConfigTypeDef]


# ListTestRunTestCasesRequestRequestTypeDef

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestRunTestCasesResponseTypeDef

### testRunTestCases
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.TestCaseRunSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestRunsRequestListTestRunsPaginateTypeDef

### testSuiteId
- **Type**: typing.Optional[str]

### testRunIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.PaginatorConfigTypeDef]


# ListTestRunsRequestRequestTypeDef

### testSuiteId
- **Type**: typing.Optional[str]

### testRunIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestRunsResponseTypeDef

### testRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.TestRunSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestSuitesRequestListTestSuitesPaginateTypeDef

### testSuiteIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.PaginatorConfigTypeDef]


# ListTestSuitesRequestRequestTypeDef

### testSuiteIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestSuitesResponseTypeDef

### testSuites
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest_classes.TestSuiteSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# M2ManagedActionPropertiesTypeDef

### forceStop
- **Type**: typing.Optional[bool]

### importDataSetLocation
- **Type**: typing.Optional[str]


# M2ManagedApplicationActionTypeDef

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: typing.Literal['Configure', 'Deconfigure']
- **Required**: Yes

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2ManagedActionPropertiesTypeDef]


# M2ManagedApplicationStepInputTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### runtime
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: typing.Literal['Configure', 'Deconfigure']
- **Required**: Yes

### vpcEndpointServiceName
- **Type**: typing.Optional[str]

### listenerPort
- **Type**: typing.Optional[int]

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2ManagedActionPropertiesTypeDef]


# M2ManagedApplicationStepOutputTypeDef

### importDataSetSummary
- **Type**: typing.Optional[typing.Dict[str, str]]


# M2ManagedApplicationStepSummaryTypeDef

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.M2ManagedApplicationStepInputTypeDef'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2ManagedApplicationStepOutputTypeDef]


# M2ManagedApplicationSummaryTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### runtime
- **Type**: typing.Literal['MicroFocus']
- **Required**: Yes

### listenerPort
- **Type**: typing.Optional[int]


# M2ManagedApplicationTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### runtime
- **Type**: typing.Literal['MicroFocus']
- **Required**: Yes

### vpcEndpointServiceName
- **Type**: typing.Optional[str]

### listenerPort
- **Type**: typing.Optional[str]


# M2NonManagedApplicationActionTypeDef

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: typing.Literal['Configure', 'Deconfigure']
- **Required**: Yes


# M2NonManagedApplicationStepInputTypeDef

### vpcEndpointServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### listenerPort
- **Type**: <class 'int'>
- **Required**: Yes

### runtime
- **Type**: typing.Literal['BluAge']
- **Required**: Yes

### actionType
- **Type**: typing.Literal['Configure', 'Deconfigure']
- **Required**: Yes

### webAppName
- **Type**: typing.Optional[str]


# M2NonManagedApplicationStepSummaryTypeDef

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.M2NonManagedApplicationStepInputTypeDef'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# M2NonManagedApplicationSummaryTypeDef

### vpcEndpointServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### listenerPort
- **Type**: <class 'int'>
- **Required**: Yes

### runtime
- **Type**: typing.Literal['BluAge']
- **Required**: Yes

### webAppName
- **Type**: typing.Optional[str]


# M2NonManagedApplicationTypeDef

### vpcEndpointServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### listenerPort
- **Type**: <class 'str'>
- **Required**: Yes

### runtime
- **Type**: typing.Literal['BluAge']
- **Required**: Yes

### webAppName
- **Type**: typing.Optional[str]


# MainframeActionOutputTypeDef

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.MainframeActionTypeOutputTypeDef'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.MainframeActionPropertiesTypeDef]


# MainframeActionPropertiesTypeDef

### dmsTaskArn
- **Type**: typing.Optional[str]


# MainframeActionSummaryTypeDef

### batch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.BatchSummaryTypeDef]

### tn3270
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.TN3270SummaryTypeDef]


# MainframeActionTypeDef

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.MainframeActionTypeTypeDef'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.MainframeActionPropertiesTypeDef]


# MainframeActionTypeOutputTypeDef

### batch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.BatchOutputTypeDef]

### tn3270
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.TN3270OutputTypeDef]


# MainframeActionTypeTypeDef

### batch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.BatchTypeDef]

### tn3270
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.TN3270TypeDef]


# MainframeResourceSummaryTypeDef

### m2ManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2ManagedApplicationSummaryTypeDef]

### m2NonManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2NonManagedApplicationSummaryTypeDef]


# OutputFileTypeDef

### fileLocation
- **Type**: typing.Optional[str]


# OutputTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.OutputFileTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceActionSummaryTypeDef

### cloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CloudFormationStepSummaryTypeDef]

### m2ManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2ManagedApplicationStepSummaryTypeDef]

### m2NonManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2NonManagedApplicationStepSummaryTypeDef]


# ResourceActionTypeDef

### m2ManagedApplicationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2ManagedApplicationActionTypeDef]

### m2NonManagedApplicationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2NonManagedApplicationActionTypeDef]

### cloudFormationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CloudFormationActionTypeDef]


# ResourceOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResourceTypeOutputTypeDef'>
- **Required**: Yes


# ResourceTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResourceTypeTypeDef'>
- **Required**: Yes


# ResourceTypeOutputTypeDef

### cloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CloudFormationOutputTypeDef]

### m2ManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2ManagedApplicationTypeDef]

### m2NonManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2NonManagedApplicationTypeDef]


# ResourceTypeTypeDef

### cloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CloudFormationTypeDef]

### m2ManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2ManagedApplicationTypeDef]

### m2NonManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.M2NonManagedApplicationTypeDef]


# ResponseMetadataTypeDef

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


# ScriptSummaryTypeDef

### scriptLocation
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Selenium']
- **Required**: Yes


# ScriptTypeDef

### scriptLocation
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Selenium']
- **Required**: Yes


# ServiceSettingsTypeDef

### kmsKeyId
- **Type**: typing.Optional[str]


# SourceDatabaseMetadataTypeDef

### type
- **Type**: typing.Literal['z/OS-DB2']
- **Required**: Yes

### captureTool
- **Type**: typing.Literal['AWS DMS', 'Precisely']
- **Required**: Yes


# StartTestRunRequestRequestTypeDef

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testConfigurationId
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartTestRunResponseTypeDef

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### testRunStatus
- **Type**: typing.Literal['Deleting', 'Failed', 'Running', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StepActionOutputTypeDef

### resourceAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.ResourceActionTypeDef]

### mainframeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.MainframeActionOutputTypeDef]

### compareAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CompareActionOutputTypeDef]


# StepActionTypeDef

### resourceAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.ResourceActionTypeDef]

### mainframeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.MainframeActionTypeDef]

### compareAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CompareActionTypeDef]


# StepOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.StepActionOutputTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StepRunSummaryTypeDef

### mainframeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.MainframeActionSummaryTypeDef]

### compareAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.CompareActionSummaryTypeDef]

### resourceAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.ResourceActionSummaryTypeDef]


# StepTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.StepActionTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# TN3270OutputTypeDef

### script
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ScriptTypeDef'>
- **Required**: Yes

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]


# TN3270StepInputTypeDef

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.MainframeResourceSummaryTypeDef'>
- **Required**: Yes

### script
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ScriptSummaryTypeDef'>
- **Required**: Yes

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.MainframeActionPropertiesTypeDef]


# TN3270StepOutputTypeDef

### scriptOutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### dataSetExportLocation
- **Type**: typing.Optional[str]

### dmsOutputLocation
- **Type**: typing.Optional[str]

### dataSetDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apptest_classes.DataSetTypeDef]]


# TN3270SummaryTypeDef

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.TN3270StepInputTypeDef'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.TN3270StepOutputTypeDef]


# TN3270TypeDef

### script
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ScriptTypeDef'>
- **Required**: Yes

### exportDataSetNames
- **Type**: typing.Optional[typing.Sequence[str]]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetDatabaseMetadataTypeDef

### type
- **Type**: typing.Literal['PostgreSQL']
- **Required**: Yes

### captureTool
- **Type**: typing.Literal['AWS DMS', 'Precisely']
- **Required**: Yes


# TestCaseLatestVersionTypeDef

### version
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# TestCaseRunSummaryTypeDef

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseVersion
- **Type**: <class 'int'>
- **Required**: Yes

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'Running', 'Success']
- **Required**: Yes

### runStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]

### runEndTime
- **Type**: typing.Optional[datetime.datetime]


# TestCaseSummaryTypeDef

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# TestCasesOutputTypeDef

### sequential
- **Type**: typing.Optional[typing.List[str]]


# TestCasesTypeDef

### sequential
- **Type**: typing.Optional[typing.Sequence[str]]


# TestConfigurationLatestVersionTypeDef

### version
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# TestConfigurationSummaryTypeDef

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersion
- **Type**: <class 'int'>
- **Required**: Yes

### testConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# TestRunStepSummaryTypeDef

### stepName
- **Type**: <class 'str'>
- **Required**: Yes

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'Running', 'Success']
- **Required**: Yes

### runStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### testCaseId
- **Type**: typing.Optional[str]

### testCaseVersion
- **Type**: typing.Optional[int]

### testSuiteId
- **Type**: typing.Optional[str]

### testSuiteVersion
- **Type**: typing.Optional[int]

### beforeStep
- **Type**: typing.Optional[bool]

### afterStep
- **Type**: typing.Optional[bool]

### statusReason
- **Type**: typing.Optional[str]

### runEndTime
- **Type**: typing.Optional[datetime.datetime]


# TestRunSummaryTypeDef

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### testRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Deleting', 'Failed', 'Running', 'Success']
- **Required**: Yes

### runStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### testConfigurationId
- **Type**: typing.Optional[str]

### testConfigurationVersion
- **Type**: typing.Optional[int]

### statusReason
- **Type**: typing.Optional[str]

### runEndTime
- **Type**: typing.Optional[datetime.datetime]


# TestSuiteLatestVersionTypeDef

### version
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Creating', 'Deleting', 'Failed', 'Updating']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# TestSuiteSummaryTypeDef

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersion
- **Type**: <class 'int'>
- **Required**: Yes

### testSuiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Creating', 'Deleting', 'Failed', 'Updating']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateTestCaseRequestRequestTypeDef

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### steps
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.apptest_classes.StepTypeDef, aws_resource_validator.pydantic_models.apptest_classes.StepOutputTypeDef]]]


# UpdateTestCaseResponseTypeDef

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTestConfigurationRequestRequestTypeDef

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### resources
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.apptest_classes.ResourceTypeDef, aws_resource_validator.pydantic_models.apptest_classes.ResourceOutputTypeDef]]]

### properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### serviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.ServiceSettingsTypeDef]


# UpdateTestConfigurationResponseTypeDef

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### testConfigurationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTestSuiteRequestRequestTypeDef

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### beforeSteps
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.apptest_classes.StepTypeDef, aws_resource_validator.pydantic_models.apptest_classes.StepOutputTypeDef]]]

### afterSteps
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.apptest_classes.StepTypeDef, aws_resource_validator.pydantic_models.apptest_classes.StepOutputTypeDef]]]

### testCases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest_classes.TestCasesTypeDef]


# UpdateTestSuiteResponseTypeDef

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



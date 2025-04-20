# Apptest Apptest Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Batch

### batchJobName
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]


# BatchOutput

### batchJobName
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]


# BatchStepInput

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeResourceSummary'>
- **Required**: Yes

### batchJobName
- **Type**: <class 'str'>
- **Required**: Yes

### batchJobParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionProperties]


# BatchStepOutput

### dataSetExportLocation
- **Type**: typing.Optional[str]

### dmsOutputLocation
- **Type**: typing.Optional[str]

### dataSetDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.DataSet]]


# BatchSummary

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.BatchStepInput'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.BatchStepOutput]


# CloudFormation

### templateLocation
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# CloudFormationAction

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: typing.Optional[typing.Literal['Create', 'Delete']]


# CloudFormationOutput

### templateLocation
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# CloudFormationStepSummary

### createCloudformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CreateCloudFormationSummary]

### deleteCloudformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.DeleteCloudFormationSummary]


# CompareAction

### input
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Input, aws_resource_validator.pydantic_models.apptest.apptest_classes.InputOutput]
- **Required**: Yes

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.Output]


# CompareActionOutput

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.InputOutput'>
- **Required**: Yes

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.Output]


# CompareActionSummary

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.File'>
- **Required**: Yes


# CompareDataSetsStepInput

### sourceLocation
- **Type**: <class 'str'>
- **Required**: Yes

### targetLocation
- **Type**: <class 'str'>
- **Required**: Yes

### sourceDataSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.DataSet]
- **Required**: Yes

### targetDataSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.DataSet]
- **Required**: Yes


# CompareDataSetsStepOutput

### comparisonOutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### comparisonStatus
- **Type**: typing.Literal['Different', 'Equal', 'Equivalent']
- **Required**: Yes


# CompareDataSetsSummary

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareDataSetsStepInput'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareDataSetsStepOutput]


# CompareDatabaseCDCStepInput

### sourceLocation
- **Type**: <class 'str'>
- **Required**: Yes

### targetLocation
- **Type**: <class 'str'>
- **Required**: Yes

### sourceMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.SourceDatabaseMetadata'>
- **Required**: Yes

### targetMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.TargetDatabaseMetadata'>
- **Required**: Yes

### outputLocation
- **Type**: typing.Optional[str]


# CompareDatabaseCDCStepOutput

### comparisonOutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### comparisonStatus
- **Type**: typing.Literal['Different', 'Equal', 'Equivalent']
- **Required**: Yes


# CompareDatabaseCDCSummary

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareDatabaseCDCStepInput'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareDatabaseCDCStepOutput]


# CompareFileType

### datasets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareDataSetsSummary]

### databaseCDC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareDatabaseCDCSummary]


# CreateCloudFormationStepInput

### templateLocation
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCloudFormationStepOutput

### stackId
- **Type**: <class 'str'>
- **Required**: Yes

### exports
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCloudFormationSummary

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.CreateCloudFormationStepInput'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CreateCloudFormationStepOutput]


# CreateTestCaseRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### steps
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Step, aws_resource_validator.pydantic_models.apptest.apptest_classes.StepOutput]]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateTestCaseResponse

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTestConfigurationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resources
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Resource, aws_resource_validator.pydantic_models.apptest.apptest_classes.ResourceOutput]]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### serviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.ServiceSettings]


# CreateTestConfigurationResponse

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### testConfigurationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTestSuiteRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### testCases
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.TestCases, aws_resource_validator.pydantic_models.apptest.apptest_classes.TestCasesOutput]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### beforeSteps
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Step, aws_resource_validator.pydantic_models.apptest.apptest_classes.StepOutput]]]

### afterSteps
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Step, aws_resource_validator.pydantic_models.apptest.apptest_classes.StepOutput]]]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateTestSuiteResponse

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# DataSet

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


# DatabaseCDC

### sourceMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.SourceDatabaseMetadata'>
- **Required**: Yes

### targetMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.TargetDatabaseMetadata'>
- **Required**: Yes


# DeleteCloudFormationStepInput

### stackId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCloudFormationSummary

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.DeleteCloudFormationStepInput'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# DeleteTestCaseRequest

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTestConfigurationRequest

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTestRunRequest

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTestSuiteRequest

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes


# File

### fileType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareFileType]


# FileMetadata

### dataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.DataSet]]

### databaseCDC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.DatabaseCDC]


# FileMetadataOutput

### dataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.DataSet]]

### databaseCDC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.DatabaseCDC]


# GetTestCaseRequest

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseVersion
- **Type**: typing.Optional[int]


# GetTestCaseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.TestCaseLatestVersion'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.StepOutput]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# GetTestConfigurationRequest

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### testConfigurationVersion
- **Type**: typing.Optional[int]


# GetTestConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.TestConfigurationLatestVersion'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.ResourceOutput]
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### serviceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ServiceSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# GetTestRunStepRequest

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


# GetTestRunStepResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.StepRunSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# GetTestSuiteRequest

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteVersion
- **Type**: typing.Optional[int]


# GetTestSuiteResponse

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.TestSuiteLatestVersion'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.StepOutput]
- **Required**: Yes

### afterSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.StepOutput]
- **Required**: Yes

### testCases
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.TestCasesOutput'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# Input

### file
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.InputFile, aws_resource_validator.pydantic_models.apptest.apptest_classes.InputFileOutput, NoneType]


# InputFile

### sourceLocation
- **Type**: <class 'str'>
- **Required**: Yes

### targetLocation
- **Type**: <class 'str'>
- **Required**: Yes

### fileMetadata
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.FileMetadata, aws_resource_validator.pydantic_models.apptest.apptest_classes.FileMetadataOutput]
- **Required**: Yes


# InputFileOutput

### sourceLocation
- **Type**: <class 'str'>
- **Required**: Yes

### targetLocation
- **Type**: <class 'str'>
- **Required**: Yes

### fileMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.FileMetadataOutput'>
- **Required**: Yes


# InputOutput

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.InputFileOutput]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# ListTestCasesRequest

### testCaseIds
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestCasesRequestPaginate

### testCaseIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.PaginatorConfig]


# ListTestCasesResponse

### testCases
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.TestCaseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestConfigurationsRequest

### testConfigurationIds
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestConfigurationsRequestPaginate

### testConfigurationIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.PaginatorConfig]


# ListTestConfigurationsResponse

### testConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.TestConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestRunStepsRequest

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


# ListTestRunStepsRequestPaginate

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseId
- **Type**: typing.Optional[str]

### testSuiteId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.PaginatorConfig]


# ListTestRunStepsResponse

### testRunSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.TestRunStepSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestRunTestCasesRequest

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestRunTestCasesRequestPaginate

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.PaginatorConfig]


# ListTestRunTestCasesResponse

### testRunTestCases
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.TestCaseRunSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestRunsRequest

### testSuiteId
- **Type**: typing.Optional[str]

### testRunIds
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestRunsRequestPaginate

### testSuiteId
- **Type**: typing.Optional[str]

### testRunIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.PaginatorConfig]


# ListTestRunsResponse

### testRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.TestRunSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestSuitesRequest

### testSuiteIds
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTestSuitesRequestPaginate

### testSuiteIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.PaginatorConfig]


# ListTestSuitesResponse

### testSuites
- **Type**: typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.TestSuiteSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# M2ManagedActionProperties

### forceStop
- **Type**: typing.Optional[bool]

### importDataSetLocation
- **Type**: typing.Optional[str]


# M2ManagedApplication

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


# M2ManagedApplicationAction

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: typing.Literal['Configure', 'Deconfigure']
- **Required**: Yes

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2ManagedActionProperties]


# M2ManagedApplicationStepInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2ManagedActionProperties]


# M2ManagedApplicationStepOutput

### importDataSetSummary
- **Type**: typing.Optional[typing.Dict[str, str]]


# M2ManagedApplicationStepSummary

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.M2ManagedApplicationStepInput'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2ManagedApplicationStepOutput]


# M2ManagedApplicationSummary

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### runtime
- **Type**: typing.Literal['MicroFocus']
- **Required**: Yes

### listenerPort
- **Type**: typing.Optional[int]


# M2NonManagedApplication

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


# M2NonManagedApplicationAction

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: typing.Literal['Configure', 'Deconfigure']
- **Required**: Yes


# M2NonManagedApplicationStepInput

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


# M2NonManagedApplicationStepSummary

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.M2NonManagedApplicationStepInput'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# M2NonManagedApplicationSummary

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


# MainframeAction

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionType, aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionTypeOutput]
- **Required**: Yes

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionProperties]


# MainframeActionOutput

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionTypeOutput'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionProperties]


# MainframeActionProperties

### dmsTaskArn
- **Type**: typing.Optional[str]


# MainframeActionSummary

### batch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.BatchSummary]

### tn3270
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.TN3270Summary]


# MainframeActionType

### batch
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Batch, aws_resource_validator.pydantic_models.apptest.apptest_classes.BatchOutput, NoneType]

### tn3270
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.TN3270, aws_resource_validator.pydantic_models.apptest.apptest_classes.TN3270Output, NoneType]


# MainframeActionTypeOutput

### batch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.BatchOutput]

### tn3270
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.TN3270Output]


# MainframeResourceSummary

### m2ManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2ManagedApplicationSummary]

### m2NonManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2NonManagedApplicationSummary]


# Output

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.OutputFile]


# OutputFile

### fileLocation
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Resource

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.ResourceType, aws_resource_validator.pydantic_models.apptest.apptest_classes.ResourceTypeOutput]
- **Required**: Yes


# ResourceAction

### m2ManagedApplicationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2ManagedApplicationAction]

### m2NonManagedApplicationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2NonManagedApplicationAction]

### cloudFormationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CloudFormationAction]


# ResourceActionSummary

### cloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CloudFormationStepSummary]

### m2ManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2ManagedApplicationStepSummary]

### m2NonManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2NonManagedApplicationStepSummary]


# ResourceOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResourceTypeOutput'>
- **Required**: Yes


# ResourceType

### cloudFormation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.CloudFormation, aws_resource_validator.pydantic_models.apptest.apptest_classes.CloudFormationOutput, NoneType]

### m2ManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2ManagedApplication]

### m2NonManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2NonManagedApplication]


# ResourceTypeOutput

### cloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CloudFormationOutput]

### m2ManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2ManagedApplication]

### m2NonManagedApplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.M2NonManagedApplication]


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


# Script

### scriptLocation
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Selenium']
- **Required**: Yes


# ScriptSummary

### scriptLocation
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Selenium']
- **Required**: Yes


# ServiceSettings

### kmsKeyId
- **Type**: typing.Optional[str]


# SourceDatabaseMetadata

### type
- **Type**: typing.Literal['z/OS-DB2']
- **Required**: Yes

### captureTool
- **Type**: typing.Literal['AWS DMS', 'Precisely']
- **Required**: Yes


# StartTestRunRequest

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testConfigurationId
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartTestRunResponse

### testRunId
- **Type**: <class 'str'>
- **Required**: Yes

### testRunStatus
- **Type**: typing.Literal['Deleting', 'Failed', 'Running', 'Success']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# Step

### name
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.StepAction, aws_resource_validator.pydantic_models.apptest.apptest_classes.StepActionOutput]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StepAction

### resourceAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.ResourceAction]

### mainframeAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeAction, aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionOutput, NoneType]

### compareAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareAction, aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareActionOutput, NoneType]


# StepActionOutput

### resourceAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.ResourceAction]

### mainframeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionOutput]

### compareAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareActionOutput]


# StepOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.StepActionOutput'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StepRunSummary

### mainframeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionSummary]

### compareAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.CompareActionSummary]

### resourceAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.ResourceActionSummary]


# TN3270

### script
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.Script'>
- **Required**: Yes

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]


# TN3270Output

### script
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.Script'>
- **Required**: Yes

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]


# TN3270StepInput

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeResourceSummary'>
- **Required**: Yes

### script
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ScriptSummary'>
- **Required**: Yes

### exportDataSetNames
- **Type**: typing.Optional[typing.List[str]]

### properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.MainframeActionProperties]


# TN3270StepOutput

### scriptOutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### dataSetExportLocation
- **Type**: typing.Optional[str]

### dmsOutputLocation
- **Type**: typing.Optional[str]

### dataSetDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apptest.apptest_classes.DataSet]]


# TN3270Summary

### stepInput
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.TN3270StepInput'>
- **Required**: Yes

### stepOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.TN3270StepOutput]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TargetDatabaseMetadata

### type
- **Type**: typing.Literal['PostgreSQL']
- **Required**: Yes

### captureTool
- **Type**: typing.Literal['AWS DMS', 'Precisely']
- **Required**: Yes


# TestCaseLatestVersion

### version
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# TestCaseRunSummary

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


# TestCaseSummary

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


# TestCases

### sequential
- **Type**: typing.Optional[typing.List[str]]


# TestCasesOutput

### sequential
- **Type**: typing.Optional[typing.List[str]]


# TestConfigurationLatestVersion

### version
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# TestConfigurationSummary

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


# TestRunStepSummary

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


# TestRunSummary

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


# TestSuiteLatestVersion

### version
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Active', 'Creating', 'Deleting', 'Failed', 'Updating']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# TestSuiteSummary

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


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateTestCaseRequest

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### steps
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Step, aws_resource_validator.pydantic_models.apptest.apptest_classes.StepOutput]]]


# UpdateTestCaseResponse

### testCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### testCaseVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTestConfigurationRequest

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### resources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Resource, aws_resource_validator.pydantic_models.apptest.apptest_classes.ResourceOutput]]]

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### serviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apptest.apptest_classes.ServiceSettings]


# UpdateTestConfigurationResponse

### testConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### testConfigurationVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTestSuiteRequest

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### beforeSteps
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Step, aws_resource_validator.pydantic_models.apptest.apptest_classes.StepOutput]]]

### afterSteps
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.Step, aws_resource_validator.pydantic_models.apptest.apptest_classes.StepOutput]]]

### testCases
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apptest.apptest_classes.TestCases, aws_resource_validator.pydantic_models.apptest.apptest_classes.TestCasesOutput, NoneType]


# UpdateTestSuiteResponse

### testSuiteId
- **Type**: <class 'str'>
- **Required**: Yes

### testSuiteVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apptest.apptest_classes.ResponseMetadata'>
- **Required**: Yes



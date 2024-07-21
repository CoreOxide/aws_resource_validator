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
from aws_resource_validator.pydantic_models.apptest_constants import *

class BatchOutputTypeDef(BaseModel):
    batchJobName: str
    batchJobParameters: Optional[Dict[str, str]] = None
    exportDataSetNames: Optional[List[str]] = None

class MainframeActionPropertiesTypeDef(BaseModel):
    dmsTaskArn: Optional[str] = None

class DataSetTypeDef(BaseModel):
    type: Literal["PS"]
    name: str
    ccsid: str
    format: FormatType
    length: int

class BatchTypeDef(BaseModel):
    batchJobName: str
    batchJobParameters: Optional[Mapping[str, str]] = None
    exportDataSetNames: Optional[Sequence[str]] = None

class CloudFormationActionTypeDef(BaseModel):
    resource: str
    actionType: Optional[CloudFormationActionTypeType] = None

class CloudFormationOutputTypeDef(BaseModel):
    templateLocation: str
    parameters: Optional[Dict[str, str]] = None

class CloudFormationTypeDef(BaseModel):
    templateLocation: str
    parameters: Optional[Mapping[str, str]] = None

class CompareDataSetsStepOutputTypeDef(BaseModel):
    comparisonOutputLocation: str
    comparisonStatus: ComparisonStatusEnumType

class SourceDatabaseMetadataTypeDef(BaseModel):
    type: Literal["z/OS-DB2"]
    captureTool: CaptureToolType

class TargetDatabaseMetadataTypeDef(BaseModel):
    type: Literal["PostgreSQL"]
    captureTool: CaptureToolType

class CompareDatabaseCDCStepOutputTypeDef(BaseModel):
    comparisonOutputLocation: str
    comparisonStatus: ComparisonStatusEnumType

class CreateCloudFormationStepInputTypeDef(BaseModel):
    templateLocation: str
    parameters: Optional[Dict[str, str]] = None

class CreateCloudFormationStepOutputTypeDef(BaseModel):
    stackId: str
    exports: Optional[Dict[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ServiceSettingsTypeDef(BaseModel):
    kmsKeyId: Optional[str] = None

class TestCasesTypeDef(BaseModel):
    sequential: Optional[Sequence[str]] = None

class DeleteCloudFormationStepInputTypeDef(BaseModel):
    stackId: str

class DeleteTestCaseRequestRequestTypeDef(BaseModel):
    testCaseId: str

class DeleteTestConfigurationRequestRequestTypeDef(BaseModel):
    testConfigurationId: str

class DeleteTestRunRequestRequestTypeDef(BaseModel):
    testRunId: str

class DeleteTestSuiteRequestRequestTypeDef(BaseModel):
    testSuiteId: str

class GetTestCaseRequestRequestTypeDef(BaseModel):
    testCaseId: str
    testCaseVersion: Optional[int] = None

class TestCaseLatestVersionTypeDef(BaseModel):
    version: int
    status: TestCaseLifecycleType
    statusReason: Optional[str] = None

class GetTestConfigurationRequestRequestTypeDef(BaseModel):
    testConfigurationId: str
    testConfigurationVersion: Optional[int] = None

class TestConfigurationLatestVersionTypeDef(BaseModel):
    version: int
    status: TestConfigurationLifecycleType
    statusReason: Optional[str] = None

class GetTestRunStepRequestRequestTypeDef(BaseModel):
    testRunId: str
    stepName: str
    testCaseId: Optional[str] = None
    testSuiteId: Optional[str] = None

class GetTestSuiteRequestRequestTypeDef(BaseModel):
    testSuiteId: str
    testSuiteVersion: Optional[int] = None

class TestCasesOutputTypeDef(BaseModel):
    sequential: Optional[List[str]] = None

class TestSuiteLatestVersionTypeDef(BaseModel):
    version: int
    status: TestSuiteLifecycleType
    statusReason: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTestCasesRequestRequestTypeDef(BaseModel):
    testCaseIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TestCaseSummaryTypeDef(BaseModel):
    testCaseId: str
    testCaseArn: str
    name: str
    latestVersion: int
    status: TestCaseLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: Optional[str] = None

class ListTestConfigurationsRequestRequestTypeDef(BaseModel):
    testConfigurationIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TestConfigurationSummaryTypeDef(BaseModel):
    testConfigurationId: str
    name: str
    latestVersion: int
    testConfigurationArn: str
    status: TestConfigurationLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: Optional[str] = None

class ListTestRunStepsRequestRequestTypeDef(BaseModel):
    testRunId: str
    testCaseId: Optional[str] = None
    testSuiteId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TestRunStepSummaryTypeDef(BaseModel):
    stepName: str
    testRunId: str
    status: StepRunStatusType
    runStartTime: datetime
    testCaseId: Optional[str] = None
    testCaseVersion: Optional[int] = None
    testSuiteId: Optional[str] = None
    testSuiteVersion: Optional[int] = None
    beforeStep: Optional[bool] = None
    afterStep: Optional[bool] = None
    statusReason: Optional[str] = None
    runEndTime: Optional[datetime] = None

class ListTestRunTestCasesRequestRequestTypeDef(BaseModel):
    testRunId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TestCaseRunSummaryTypeDef(BaseModel):
    testCaseId: str
    testCaseVersion: int
    testRunId: str
    status: TestCaseRunStatusType
    runStartTime: datetime
    statusReason: Optional[str] = None
    runEndTime: Optional[datetime] = None

class ListTestRunsRequestRequestTypeDef(BaseModel):
    testSuiteId: Optional[str] = None
    testRunIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TestRunSummaryTypeDef(BaseModel):
    testRunId: str
    testRunArn: str
    testSuiteId: str
    testSuiteVersion: int
    status: TestRunStatusType
    runStartTime: datetime
    testConfigurationId: Optional[str] = None
    testConfigurationVersion: Optional[int] = None
    statusReason: Optional[str] = None
    runEndTime: Optional[datetime] = None

class ListTestSuitesRequestRequestTypeDef(BaseModel):
    testSuiteIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TestSuiteSummaryTypeDef(BaseModel):
    testSuiteId: str
    name: str
    latestVersion: int
    testSuiteArn: str
    status: TestSuiteLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: Optional[str] = None

class M2ManagedActionPropertiesTypeDef(BaseModel):
    forceStop: Optional[bool] = None
    importDataSetLocation: Optional[str] = None

class M2ManagedApplicationStepOutputTypeDef(BaseModel):
    importDataSetSummary: Optional[Dict[str, str]] = None

class M2ManagedApplicationSummaryTypeDef(BaseModel):
    applicationId: str
    runtime: Literal["MicroFocus"]
    listenerPort: Optional[int] = None

class M2ManagedApplicationTypeDef(BaseModel):
    applicationId: str
    runtime: Literal["MicroFocus"]
    vpcEndpointServiceName: Optional[str] = None
    listenerPort: Optional[str] = None

class M2NonManagedApplicationActionTypeDef(BaseModel):
    resource: str
    actionType: M2NonManagedActionTypeType

class M2NonManagedApplicationStepInputTypeDef(BaseModel):
    vpcEndpointServiceName: str
    listenerPort: int
    runtime: Literal["BluAge"]
    actionType: M2NonManagedActionTypeType
    webAppName: Optional[str] = None

class M2NonManagedApplicationSummaryTypeDef(BaseModel):
    vpcEndpointServiceName: str
    listenerPort: int
    runtime: Literal["BluAge"]
    webAppName: Optional[str] = None

class M2NonManagedApplicationTypeDef(BaseModel):
    vpcEndpointServiceName: str
    listenerPort: str
    runtime: Literal["BluAge"]
    webAppName: Optional[str] = None

class OutputFileTypeDef(BaseModel):
    fileLocation: Optional[str] = None

class ScriptSummaryTypeDef(BaseModel):
    scriptLocation: str
    type: Literal["Selenium"]

class ScriptTypeDef(BaseModel):
    scriptLocation: str
    type: Literal["Selenium"]

class StartTestRunRequestRequestTypeDef(BaseModel):
    testSuiteId: str
    testConfigurationId: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchStepOutputTypeDef(BaseModel):
    dataSetExportLocation: Optional[str] = None
    dmsOutputLocation: Optional[str] = None
    dataSetDetails: Optional[List[DataSetTypeDef]] = None

class CompareDataSetsStepInputTypeDef(BaseModel):
    sourceLocation: str
    targetLocation: str
    sourceDataSets: List[DataSetTypeDef]
    targetDataSets: List[DataSetTypeDef]

class TN3270StepOutputTypeDef(BaseModel):
    scriptOutputLocation: str
    dataSetExportLocation: Optional[str] = None
    dmsOutputLocation: Optional[str] = None
    dataSetDetails: Optional[List[DataSetTypeDef]] = None

class CompareDatabaseCDCStepInputTypeDef(BaseModel):
    sourceLocation: str
    targetLocation: str
    sourceMetadata: SourceDatabaseMetadataTypeDef
    targetMetadata: TargetDatabaseMetadataTypeDef
    outputLocation: Optional[str] = None

class DatabaseCDCTypeDef(BaseModel):
    sourceMetadata: SourceDatabaseMetadataTypeDef
    targetMetadata: TargetDatabaseMetadataTypeDef

class CreateCloudFormationSummaryTypeDef(BaseModel):
    stepInput: CreateCloudFormationStepInputTypeDef
    stepOutput: Optional[CreateCloudFormationStepOutputTypeDef] = None

class CreateTestCaseResponseTypeDef(BaseModel):
    testCaseId: str
    testCaseVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTestConfigurationResponseTypeDef(BaseModel):
    testConfigurationId: str
    testConfigurationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTestSuiteResponseTypeDef(BaseModel):
    testSuiteId: str
    testSuiteVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTestRunResponseTypeDef(BaseModel):
    testRunId: str
    testRunStatus: TestRunStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTestCaseResponseTypeDef(BaseModel):
    testCaseId: str
    testCaseVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTestConfigurationResponseTypeDef(BaseModel):
    testConfigurationId: str
    testConfigurationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTestSuiteResponseTypeDef(BaseModel):
    testSuiteId: str
    testSuiteVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCloudFormationSummaryTypeDef(BaseModel):
    stepInput: DeleteCloudFormationStepInputTypeDef
    stepOutput: Optional[Dict[str, Any]] = None

class ListTestCasesRequestListTestCasesPaginateTypeDef(BaseModel):
    testCaseIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTestConfigurationsRequestListTestConfigurationsPaginateTypeDef(BaseModel):
    testConfigurationIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTestRunStepsRequestListTestRunStepsPaginateTypeDef(BaseModel):
    testRunId: str
    testCaseId: Optional[str] = None
    testSuiteId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTestRunTestCasesRequestListTestRunTestCasesPaginateTypeDef(BaseModel):
    testRunId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTestRunsRequestListTestRunsPaginateTypeDef(BaseModel):
    testSuiteId: Optional[str] = None
    testRunIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTestSuitesRequestListTestSuitesPaginateTypeDef(BaseModel):
    testSuiteIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTestCasesResponseTypeDef(BaseModel):
    testCases: List[TestCaseSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestConfigurationsResponseTypeDef(BaseModel):
    testConfigurations: List[TestConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestRunStepsResponseTypeDef(BaseModel):
    testRunSteps: List[TestRunStepSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestRunTestCasesResponseTypeDef(BaseModel):
    testRunTestCases: List[TestCaseRunSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestRunsResponseTypeDef(BaseModel):
    testRuns: List[TestRunSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestSuitesResponseTypeDef(BaseModel):
    testSuites: List[TestSuiteSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class M2ManagedApplicationActionTypeDef(BaseModel):
    resource: str
    actionType: M2ManagedActionTypeType
    properties: Optional[M2ManagedActionPropertiesTypeDef] = None

class M2ManagedApplicationStepInputTypeDef(BaseModel):
    applicationId: str
    runtime: str
    actionType: M2ManagedActionTypeType
    vpcEndpointServiceName: Optional[str] = None
    listenerPort: Optional[int] = None
    properties: Optional[M2ManagedActionPropertiesTypeDef] = None

class M2NonManagedApplicationStepSummaryTypeDef(BaseModel):
    stepInput: M2NonManagedApplicationStepInputTypeDef
    stepOutput: Optional[Dict[str, Any]] = None

class MainframeResourceSummaryTypeDef(BaseModel):
    m2ManagedApplication: Optional[M2ManagedApplicationSummaryTypeDef] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationSummaryTypeDef] = None

class ResourceTypeOutputTypeDef(BaseModel):
    cloudFormation: Optional[CloudFormationOutputTypeDef] = None
    m2ManagedApplication: Optional[M2ManagedApplicationTypeDef] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationTypeDef] = None

class ResourceTypeTypeDef(BaseModel):
    cloudFormation: Optional[CloudFormationTypeDef] = None
    m2ManagedApplication: Optional[M2ManagedApplicationTypeDef] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationTypeDef] = None

class OutputTypeDef(BaseModel):
    file: Optional[OutputFileTypeDef] = None

class TN3270OutputTypeDef(BaseModel):
    script: ScriptTypeDef
    exportDataSetNames: Optional[List[str]] = None

class TN3270TypeDef(BaseModel):
    script: ScriptTypeDef
    exportDataSetNames: Optional[Sequence[str]] = None

class CompareDataSetsSummaryTypeDef(BaseModel):
    stepInput: CompareDataSetsStepInputTypeDef
    stepOutput: Optional[CompareDataSetsStepOutputTypeDef] = None

class CompareDatabaseCDCSummaryTypeDef(BaseModel):
    stepInput: CompareDatabaseCDCStepInputTypeDef
    stepOutput: Optional[CompareDatabaseCDCStepOutputTypeDef] = None

class FileMetadataOutputTypeDef(BaseModel):
    dataSets: Optional[List[DataSetTypeDef]] = None
    databaseCDC: Optional[DatabaseCDCTypeDef] = None

class FileMetadataTypeDef(BaseModel):
    dataSets: Optional[Sequence[DataSetTypeDef]] = None
    databaseCDC: Optional[DatabaseCDCTypeDef] = None

class CloudFormationStepSummaryTypeDef(BaseModel):
    createCloudformation: Optional[CreateCloudFormationSummaryTypeDef] = None
    deleteCloudformation: Optional[DeleteCloudFormationSummaryTypeDef] = None

class ResourceActionTypeDef(BaseModel):
    m2ManagedApplicationAction: Optional[M2ManagedApplicationActionTypeDef] = None
    m2NonManagedApplicationAction: Optional[M2NonManagedApplicationActionTypeDef] = None
    cloudFormationAction: Optional[CloudFormationActionTypeDef] = None

class M2ManagedApplicationStepSummaryTypeDef(BaseModel):
    stepInput: M2ManagedApplicationStepInputTypeDef
    stepOutput: Optional[M2ManagedApplicationStepOutputTypeDef] = None

class BatchStepInputTypeDef(BaseModel):
    resource: MainframeResourceSummaryTypeDef
    batchJobName: str
    batchJobParameters: Optional[Dict[str, str]] = None
    exportDataSetNames: Optional[List[str]] = None
    properties: Optional[MainframeActionPropertiesTypeDef] = None

class TN3270StepInputTypeDef(BaseModel):
    resource: MainframeResourceSummaryTypeDef
    script: ScriptSummaryTypeDef
    exportDataSetNames: Optional[List[str]] = None
    properties: Optional[MainframeActionPropertiesTypeDef] = None

class ResourceOutputTypeDef(BaseModel):
    name: str
    type: ResourceTypeOutputTypeDef

class ResourceTypeDef(BaseModel):
    name: str
    type: ResourceTypeTypeDef

class MainframeActionTypeOutputTypeDef(BaseModel):
    batch: Optional[BatchOutputTypeDef] = None
    tn3270: Optional[TN3270OutputTypeDef] = None

class MainframeActionTypeTypeDef(BaseModel):
    batch: Optional[BatchTypeDef] = None
    tn3270: Optional[TN3270TypeDef] = None

class CompareFileTypeTypeDef(BaseModel):
    datasets: Optional[CompareDataSetsSummaryTypeDef] = None
    databaseCDC: Optional[CompareDatabaseCDCSummaryTypeDef] = None

class InputFileOutputTypeDef(BaseModel):
    sourceLocation: str
    targetLocation: str
    fileMetadata: FileMetadataOutputTypeDef

class InputFileTypeDef(BaseModel):
    sourceLocation: str
    targetLocation: str
    fileMetadata: FileMetadataTypeDef

class ResourceActionSummaryTypeDef(BaseModel):
    cloudFormation: Optional[CloudFormationStepSummaryTypeDef] = None
    m2ManagedApplication: Optional[M2ManagedApplicationStepSummaryTypeDef] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationStepSummaryTypeDef] = None

class BatchSummaryTypeDef(BaseModel):
    stepInput: BatchStepInputTypeDef
    stepOutput: Optional[BatchStepOutputTypeDef] = None

class TN3270SummaryTypeDef(BaseModel):
    stepInput: TN3270StepInputTypeDef
    stepOutput: Optional[TN3270StepOutputTypeDef] = None

class GetTestConfigurationResponseTypeDef(BaseModel):
    testConfigurationId: str
    name: str
    testConfigurationArn: str
    latestVersion: TestConfigurationLatestVersionTypeDef
    testConfigurationVersion: int
    status: TestConfigurationLifecycleType
    statusReason: str
    creationTime: datetime
    lastUpdateTime: datetime
    description: str
    resources: List[ResourceOutputTypeDef]
    properties: Dict[str, str]
    tags: Dict[str, str]
    serviceSettings: ServiceSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MainframeActionOutputTypeDef(BaseModel):
    resource: str
    actionType: MainframeActionTypeOutputTypeDef
    properties: Optional[MainframeActionPropertiesTypeDef] = None

class MainframeActionTypeDef(BaseModel):
    resource: str
    actionType: MainframeActionTypeTypeDef
    properties: Optional[MainframeActionPropertiesTypeDef] = None

class FileTypeDef(BaseModel):
    fileType: Optional[CompareFileTypeTypeDef] = None

class InputOutputTypeDef(BaseModel):
    file: Optional[InputFileOutputTypeDef] = None

class InputTypeDef(BaseModel):
    file: Optional[InputFileTypeDef] = None

class MainframeActionSummaryTypeDef(BaseModel):
    batch: Optional[BatchSummaryTypeDef] = None
    tn3270: Optional[TN3270SummaryTypeDef] = None

class CreateTestConfigurationRequestRequestTypeDef(BaseModel):
    name: str
    resources: Sequence[ResourceUnionTypeDef]
    description: Optional[str] = None
    properties: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    serviceSettings: Optional[ServiceSettingsTypeDef] = None

class UpdateTestConfigurationRequestRequestTypeDef(BaseModel):
    testConfigurationId: str
    description: Optional[str] = None
    resources: Optional[Sequence[ResourceUnionTypeDef]] = None
    properties: Optional[Mapping[str, str]] = None
    serviceSettings: Optional[ServiceSettingsTypeDef] = None

class CompareActionSummaryTypeDef(BaseModel):
    type: FileTypeDef

class CompareActionOutputTypeDef(BaseModel):
    input: InputOutputTypeDef
    output: Optional[OutputTypeDef] = None

class CompareActionTypeDef(BaseModel):
    input: InputTypeDef
    output: Optional[OutputTypeDef] = None

class StepRunSummaryTypeDef(BaseModel):
    mainframeAction: Optional[MainframeActionSummaryTypeDef] = None
    compareAction: Optional[CompareActionSummaryTypeDef] = None
    resourceAction: Optional[ResourceActionSummaryTypeDef] = None

class StepActionOutputTypeDef(BaseModel):
    resourceAction: Optional[ResourceActionTypeDef] = None
    mainframeAction: Optional[MainframeActionOutputTypeDef] = None
    compareAction: Optional[CompareActionOutputTypeDef] = None

class StepActionTypeDef(BaseModel):
    resourceAction: Optional[ResourceActionTypeDef] = None
    mainframeAction: Optional[MainframeActionTypeDef] = None
    compareAction: Optional[CompareActionTypeDef] = None

class GetTestRunStepResponseTypeDef(BaseModel):
    stepName: str
    testRunId: str
    testCaseId: str
    testCaseVersion: int
    testSuiteId: str
    testSuiteVersion: int
    beforeStep: bool
    afterStep: bool
    status: StepRunStatusType
    statusReason: str
    runStartTime: datetime
    runEndTime: datetime
    stepRunSummary: StepRunSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StepOutputTypeDef(BaseModel):
    name: str
    action: StepActionOutputTypeDef
    description: Optional[str] = None

class StepTypeDef(BaseModel):
    name: str
    action: StepActionTypeDef
    description: Optional[str] = None

class GetTestCaseResponseTypeDef(BaseModel):
    testCaseId: str
    testCaseArn: str
    name: str
    description: str
    latestVersion: TestCaseLatestVersionTypeDef
    testCaseVersion: int
    status: TestCaseLifecycleType
    statusReason: str
    creationTime: datetime
    lastUpdateTime: datetime
    steps: List[StepOutputTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTestSuiteResponseTypeDef(BaseModel):
    testSuiteId: str
    name: str
    latestVersion: TestSuiteLatestVersionTypeDef
    testSuiteVersion: int
    status: TestSuiteLifecycleType
    statusReason: str
    testSuiteArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    description: str
    beforeSteps: List[StepOutputTypeDef]
    afterSteps: List[StepOutputTypeDef]
    testCases: TestCasesOutputTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTestCaseRequestRequestTypeDef(BaseModel):
    name: str
    steps: Sequence[StepUnionTypeDef]
    description: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateTestSuiteRequestRequestTypeDef(BaseModel):
    name: str
    testCases: TestCasesTypeDef
    description: Optional[str] = None
    beforeSteps: Optional[Sequence[StepUnionTypeDef]] = None
    afterSteps: Optional[Sequence[StepUnionTypeDef]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateTestCaseRequestRequestTypeDef(BaseModel):
    testCaseId: str
    description: Optional[str] = None
    steps: Optional[Sequence[StepUnionTypeDef]] = None

class UpdateTestSuiteRequestRequestTypeDef(BaseModel):
    testSuiteId: str
    description: Optional[str] = None
    beforeSteps: Optional[Sequence[StepUnionTypeDef]] = None
    afterSteps: Optional[Sequence[StepUnionTypeDef]] = None
    testCases: Optional[TestCasesTypeDef] = None


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
from aws_resource_validator.pydantic_models.apptest_constants import *

class BatchOutput(BaseValidatorModel):
    batchJobName: str
    batchJobParameters: Optional[Dict[str, str]] = None
    exportDataSetNames: Optional[List[str]] = None


class MainframeActionProperties(BaseValidatorModel):
    dmsTaskArn: Optional[str] = None


class Batch(BaseValidatorModel):
    batchJobName: str
    batchJobParameters: Optional[Mapping[str, str]] = None
    exportDataSetNames: Optional[Sequence[str]] = None


class CloudFormationAction(BaseValidatorModel):
    resource: str
    actionType: Optional[CloudFormationActionTypeType] = None


class CloudFormationOutput(BaseValidatorModel):
    templateLocation: str
    parameters: Optional[Dict[str, str]] = None


class CloudFormation(BaseValidatorModel):
    templateLocation: str
    parameters: Optional[Mapping[str, str]] = None


class CompareDataSetsStepOutput(BaseValidatorModel):
    comparisonOutputLocation: str
    comparisonStatus: ComparisonStatusEnumType


class CompareDatabaseCDCStepOutput(BaseValidatorModel):
    comparisonOutputLocation: str
    comparisonStatus: ComparisonStatusEnumType


class CreateCloudFormationStepInput(BaseValidatorModel):
    templateLocation: str
    parameters: Optional[Dict[str, str]] = None


class CreateCloudFormationStepOutput(BaseValidatorModel):
    stackId: str
    exports: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ServiceSettings(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class DeleteCloudFormationStepInput(BaseValidatorModel):
    stackId: str


class DeleteTestCaseRequest(BaseValidatorModel):
    testCaseId: str


class DeleteTestConfigurationRequest(BaseValidatorModel):
    testConfigurationId: str


class DeleteTestRunRequest(BaseValidatorModel):
    testRunId: str


class DeleteTestSuiteRequest(BaseValidatorModel):
    testSuiteId: str


class GetTestCaseRequest(BaseValidatorModel):
    testCaseId: str
    testCaseVersion: Optional[int] = None


class TestCaseLatestVersion(BaseValidatorModel):
    version: int
    status: TestCaseLifecycleType
    statusReason: Optional[str] = None


class GetTestConfigurationRequest(BaseValidatorModel):
    testConfigurationId: str
    testConfigurationVersion: Optional[int] = None


class TestConfigurationLatestVersion(BaseValidatorModel):
    version: int
    status: TestConfigurationLifecycleType
    statusReason: Optional[str] = None


class GetTestRunStepRequest(BaseValidatorModel):
    testRunId: str
    stepName: str
    testCaseId: Optional[str] = None
    testSuiteId: Optional[str] = None


class GetTestSuiteRequest(BaseValidatorModel):
    testSuiteId: str
    testSuiteVersion: Optional[int] = None


class TestCasesOutput(BaseValidatorModel):
    sequential: Optional[List[str]] = None


class TestSuiteLatestVersion(BaseValidatorModel):
    version: int
    status: TestSuiteLifecycleType
    statusReason: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTestCasesRequest(BaseValidatorModel):
    testCaseIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestCaseSummary(BaseValidatorModel):
    testCaseId: str
    testCaseArn: str
    name: str
    latestVersion: int
    status: TestCaseLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: Optional[str] = None


class ListTestConfigurationsRequest(BaseValidatorModel):
    testConfigurationIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestConfigurationSummary(BaseValidatorModel):
    testConfigurationId: str
    name: str
    latestVersion: int
    testConfigurationArn: str
    status: TestConfigurationLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: Optional[str] = None


class ListTestRunStepsRequest(BaseValidatorModel):
    testRunId: str
    testCaseId: Optional[str] = None
    testSuiteId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestRunStepSummary(BaseValidatorModel):
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


class ListTestRunTestCasesRequest(BaseValidatorModel):
    testRunId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestCaseRunSummary(BaseValidatorModel):
    testCaseId: str
    testCaseVersion: int
    testRunId: str
    status: TestCaseRunStatusType
    runStartTime: datetime
    statusReason: Optional[str] = None
    runEndTime: Optional[datetime] = None


class ListTestRunsRequest(BaseValidatorModel):
    testSuiteId: Optional[str] = None
    testRunIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestRunSummary(BaseValidatorModel):
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


class ListTestSuitesRequest(BaseValidatorModel):
    testSuiteIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestSuiteSummary(BaseValidatorModel):
    testSuiteId: str
    name: str
    latestVersion: int
    testSuiteArn: str
    status: TestSuiteLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: Optional[str] = None


class M2ManagedActionProperties(BaseValidatorModel):
    forceStop: Optional[bool] = None
    importDataSetLocation: Optional[str] = None


class M2ManagedApplicationStepOutput(BaseValidatorModel):
    importDataSetSummary: Optional[Dict[str, str]] = None


class M2ManagedApplicationSummary(BaseValidatorModel):
    applicationId: str
    runtime: Literal["MicroFocus"]
    listenerPort: Optional[int] = None


class M2ManagedApplication(BaseValidatorModel):
    applicationId: str
    runtime: Literal["MicroFocus"]
    vpcEndpointServiceName: Optional[str] = None
    listenerPort: Optional[str] = None


class M2NonManagedApplicationAction(BaseValidatorModel):
    resource: str
    actionType: M2NonManagedActionTypeType


class M2NonManagedApplicationStepInput(BaseValidatorModel):
    vpcEndpointServiceName: str
    listenerPort: int
    runtime: Literal["BluAge"]
    actionType: M2NonManagedActionTypeType
    webAppName: Optional[str] = None


class M2NonManagedApplicationSummary(BaseValidatorModel):
    vpcEndpointServiceName: str
    listenerPort: int
    runtime: Literal["BluAge"]
    webAppName: Optional[str] = None


class M2NonManagedApplication(BaseValidatorModel):
    vpcEndpointServiceName: str
    listenerPort: str
    runtime: Literal["BluAge"]
    webAppName: Optional[str] = None


class OutputFile(BaseValidatorModel):
    fileLocation: Optional[str] = None


class StartTestRunRequest(BaseValidatorModel):
    testSuiteId: str
    testConfigurationId: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TestCases(BaseValidatorModel):
    sequential: Optional[Sequence[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class DataSet(BaseValidatorModel):
    pass


class BatchStepOutput(BaseValidatorModel):
    dataSetExportLocation: Optional[str] = None
    dmsOutputLocation: Optional[str] = None
    dataSetDetails: Optional[List[DataSet]] = None


class CompareDataSetsStepInput(BaseValidatorModel):
    sourceLocation: str
    targetLocation: str
    sourceDataSets: List[DataSet]
    targetDataSets: List[DataSet]


class TN3270StepOutput(BaseValidatorModel):
    scriptOutputLocation: str
    dataSetExportLocation: Optional[str] = None
    dmsOutputLocation: Optional[str] = None
    dataSetDetails: Optional[List[DataSet]] = None


class TargetDatabaseMetadata(BaseValidatorModel):
    pass


class SourceDatabaseMetadata(BaseValidatorModel):
    pass


class CompareDatabaseCDCStepInput(BaseValidatorModel):
    sourceLocation: str
    targetLocation: str
    sourceMetadata: SourceDatabaseMetadata
    targetMetadata: TargetDatabaseMetadata
    outputLocation: Optional[str] = None


class DatabaseCDC(BaseValidatorModel):
    sourceMetadata: SourceDatabaseMetadata
    targetMetadata: TargetDatabaseMetadata


class CreateCloudFormationSummary(BaseValidatorModel):
    stepInput: CreateCloudFormationStepInput
    stepOutput: Optional[CreateCloudFormationStepOutput] = None


class CreateTestCaseResponse(BaseValidatorModel):
    testCaseId: str
    testCaseVersion: int
    ResponseMetadata: ResponseMetadata


class CreateTestConfigurationResponse(BaseValidatorModel):
    testConfigurationId: str
    testConfigurationVersion: int
    ResponseMetadata: ResponseMetadata


class CreateTestSuiteResponse(BaseValidatorModel):
    testSuiteId: str
    testSuiteVersion: int
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartTestRunResponse(BaseValidatorModel):
    testRunId: str
    testRunStatus: TestRunStatusType
    ResponseMetadata: ResponseMetadata


class UpdateTestCaseResponse(BaseValidatorModel):
    testCaseId: str
    testCaseVersion: int
    ResponseMetadata: ResponseMetadata


class UpdateTestConfigurationResponse(BaseValidatorModel):
    testConfigurationId: str
    testConfigurationVersion: int
    ResponseMetadata: ResponseMetadata


class UpdateTestSuiteResponse(BaseValidatorModel):
    testSuiteId: str
    testSuiteVersion: int
    ResponseMetadata: ResponseMetadata


class DeleteCloudFormationSummary(BaseValidatorModel):
    stepInput: DeleteCloudFormationStepInput
    stepOutput: Optional[Dict[str, Any]] = None


class ListTestCasesRequestPaginate(BaseValidatorModel):
    testCaseIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTestConfigurationsRequestPaginate(BaseValidatorModel):
    testConfigurationIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTestRunStepsRequestPaginate(BaseValidatorModel):
    testRunId: str
    testCaseId: Optional[str] = None
    testSuiteId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTestRunTestCasesRequestPaginate(BaseValidatorModel):
    testRunId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTestRunsRequestPaginate(BaseValidatorModel):
    testSuiteId: Optional[str] = None
    testRunIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTestSuitesRequestPaginate(BaseValidatorModel):
    testSuiteIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTestCasesResponse(BaseValidatorModel):
    testCases: List[TestCaseSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTestConfigurationsResponse(BaseValidatorModel):
    testConfigurations: List[TestConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTestRunStepsResponse(BaseValidatorModel):
    testRunSteps: List[TestRunStepSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTestRunTestCasesResponse(BaseValidatorModel):
    testRunTestCases: List[TestCaseRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTestRunsResponse(BaseValidatorModel):
    testRuns: List[TestRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTestSuitesResponse(BaseValidatorModel):
    testSuites: List[TestSuiteSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class M2ManagedApplicationAction(BaseValidatorModel):
    resource: str
    actionType: M2ManagedActionTypeType
    properties: Optional[M2ManagedActionProperties] = None


class M2ManagedApplicationStepInput(BaseValidatorModel):
    applicationId: str
    runtime: str
    actionType: M2ManagedActionTypeType
    vpcEndpointServiceName: Optional[str] = None
    listenerPort: Optional[int] = None
    properties: Optional[M2ManagedActionProperties] = None


class M2NonManagedApplicationStepSummary(BaseValidatorModel):
    stepInput: M2NonManagedApplicationStepInput
    stepOutput: Optional[Dict[str, Any]] = None


class MainframeResourceSummary(BaseValidatorModel):
    m2ManagedApplication: Optional[M2ManagedApplicationSummary] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationSummary] = None


class ResourceTypeOutput(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationOutput] = None
    m2ManagedApplication: Optional[M2ManagedApplication] = None
    m2NonManagedApplication: Optional[M2NonManagedApplication] = None


class Output(BaseValidatorModel):
    file: Optional[OutputFile] = None


class Script(BaseValidatorModel):
    pass


class TN3270Output(BaseValidatorModel):
    script: Script
    exportDataSetNames: Optional[List[str]] = None


class TN3270(BaseValidatorModel):
    script: Script
    exportDataSetNames: Optional[Sequence[str]] = None


class CompareDataSetsSummary(BaseValidatorModel):
    stepInput: CompareDataSetsStepInput
    stepOutput: Optional[CompareDataSetsStepOutput] = None


class CloudFormationUnion(BaseValidatorModel):
    pass


class ResourceType(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationUnion] = None
    m2ManagedApplication: Optional[M2ManagedApplication] = None
    m2NonManagedApplication: Optional[M2NonManagedApplication] = None


class CompareDatabaseCDCSummary(BaseValidatorModel):
    stepInput: CompareDatabaseCDCStepInput
    stepOutput: Optional[CompareDatabaseCDCStepOutput] = None


class FileMetadataOutput(BaseValidatorModel):
    dataSets: Optional[List[DataSet]] = None
    databaseCDC: Optional[DatabaseCDC] = None


class FileMetadata(BaseValidatorModel):
    dataSets: Optional[Sequence[DataSet]] = None
    databaseCDC: Optional[DatabaseCDC] = None


class CloudFormationStepSummary(BaseValidatorModel):
    createCloudformation: Optional[CreateCloudFormationSummary] = None
    deleteCloudformation: Optional[DeleteCloudFormationSummary] = None


class ResourceAction(BaseValidatorModel):
    m2ManagedApplicationAction: Optional[M2ManagedApplicationAction] = None
    m2NonManagedApplicationAction: Optional[M2NonManagedApplicationAction] = None
    cloudFormationAction: Optional[CloudFormationAction] = None


class M2ManagedApplicationStepSummary(BaseValidatorModel):
    stepInput: M2ManagedApplicationStepInput
    stepOutput: Optional[M2ManagedApplicationStepOutput] = None


class BatchStepInput(BaseValidatorModel):
    resource: MainframeResourceSummary
    batchJobName: str
    batchJobParameters: Optional[Dict[str, str]] = None
    exportDataSetNames: Optional[List[str]] = None
    properties: Optional[MainframeActionProperties] = None


class ScriptSummary(BaseValidatorModel):
    pass


class TN3270StepInput(BaseValidatorModel):
    resource: MainframeResourceSummary
    script: ScriptSummary
    exportDataSetNames: Optional[List[str]] = None
    properties: Optional[MainframeActionProperties] = None


class MainframeActionTypeOutput(BaseValidatorModel):
    batch: Optional[BatchOutput] = None
    tn3270: Optional[TN3270Output] = None


class CompareFileType(BaseValidatorModel):
    datasets: Optional[CompareDataSetsSummary] = None
    databaseCDC: Optional[CompareDatabaseCDCSummary] = None


class InputFileOutput(BaseValidatorModel):
    sourceLocation: str
    targetLocation: str
    fileMetadata: FileMetadataOutput


class ResourceActionSummary(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationStepSummary] = None
    m2ManagedApplication: Optional[M2ManagedApplicationStepSummary] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationStepSummary] = None


class BatchSummary(BaseValidatorModel):
    stepInput: BatchStepInput
    stepOutput: Optional[BatchStepOutput] = None


class TN3270Summary(BaseValidatorModel):
    stepInput: TN3270StepInput
    stepOutput: Optional[TN3270StepOutput] = None


class ResourceOutput(BaseValidatorModel):
    pass


class GetTestConfigurationResponse(BaseValidatorModel):
    testConfigurationId: str
    name: str
    testConfigurationArn: str
    latestVersion: TestConfigurationLatestVersion
    testConfigurationVersion: int
    status: TestConfigurationLifecycleType
    statusReason: str
    creationTime: datetime
    lastUpdateTime: datetime
    description: str
    resources: List[ResourceOutput]
    properties: Dict[str, str]
    tags: Dict[str, str]
    serviceSettings: ServiceSettings
    ResponseMetadata: ResponseMetadata


class MainframeActionOutput(BaseValidatorModel):
    resource: str
    actionType: MainframeActionTypeOutput
    properties: Optional[MainframeActionProperties] = None


class TN3270Union(BaseValidatorModel):
    pass


class BatchUnion(BaseValidatorModel):
    pass


class MainframeActionType(BaseValidatorModel):
    batch: Optional[BatchUnion] = None
    tn3270: Optional[TN3270Union] = None


class File(BaseValidatorModel):
    fileType: Optional[CompareFileType] = None


class InputOutput(BaseValidatorModel):
    file: Optional[InputFileOutput] = None


class FileMetadataUnion(BaseValidatorModel):
    pass


class InputFile(BaseValidatorModel):
    sourceLocation: str
    targetLocation: str
    fileMetadata: FileMetadataUnion


class MainframeActionSummary(BaseValidatorModel):
    batch: Optional[BatchSummary] = None
    tn3270: Optional[TN3270Summary] = None


class MainframeActionTypeUnion(BaseValidatorModel):
    pass


class MainframeAction(BaseValidatorModel):
    resource: str
    actionType: MainframeActionTypeUnion
    properties: Optional[MainframeActionProperties] = None


class ResourceUnion(BaseValidatorModel):
    pass


class CreateTestConfigurationRequest(BaseValidatorModel):
    name: str
    resources: Sequence[ResourceUnion]
    description: Optional[str] = None
    properties: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    serviceSettings: Optional[ServiceSettings] = None


class UpdateTestConfigurationRequest(BaseValidatorModel):
    testConfigurationId: str
    description: Optional[str] = None
    resources: Optional[Sequence[ResourceUnion]] = None
    properties: Optional[Mapping[str, str]] = None
    serviceSettings: Optional[ServiceSettings] = None


class CompareActionSummary(BaseValidatorModel):
    pass


class StepRunSummary(BaseValidatorModel):
    mainframeAction: Optional[MainframeActionSummary] = None
    compareAction: Optional[CompareActionSummary] = None
    resourceAction: Optional[ResourceActionSummary] = None


class CompareActionOutput(BaseValidatorModel):
    pass


class StepActionOutput(BaseValidatorModel):
    resourceAction: Optional[ResourceAction] = None
    mainframeAction: Optional[MainframeActionOutput] = None
    compareAction: Optional[CompareActionOutput] = None


class InputFileUnion(BaseValidatorModel):
    pass


class Input(BaseValidatorModel):
    file: Optional[InputFileUnion] = None


class GetTestRunStepResponse(BaseValidatorModel):
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
    stepRunSummary: StepRunSummary
    ResponseMetadata: ResponseMetadata


class StepOutput(BaseValidatorModel):
    name: str
    action: StepActionOutput
    description: Optional[str] = None


class GetTestCaseResponse(BaseValidatorModel):
    testCaseId: str
    testCaseArn: str
    name: str
    description: str
    latestVersion: TestCaseLatestVersion
    testCaseVersion: int
    status: TestCaseLifecycleType
    statusReason: str
    creationTime: datetime
    lastUpdateTime: datetime
    steps: List[StepOutput]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetTestSuiteResponse(BaseValidatorModel):
    testSuiteId: str
    name: str
    latestVersion: TestSuiteLatestVersion
    testSuiteVersion: int
    status: TestSuiteLifecycleType
    statusReason: str
    testSuiteArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    description: str
    beforeSteps: List[StepOutput]
    afterSteps: List[StepOutput]
    testCases: TestCasesOutput
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class MainframeActionUnion(BaseValidatorModel):
    pass


class CompareActionUnion(BaseValidatorModel):
    pass


class StepAction(BaseValidatorModel):
    resourceAction: Optional[ResourceAction] = None
    mainframeAction: Optional[MainframeActionUnion] = None
    compareAction: Optional[CompareActionUnion] = None


class StepActionUnion(BaseValidatorModel):
    pass


class Step(BaseValidatorModel):
    name: str
    action: StepActionUnion
    description: Optional[str] = None


class StepUnion(BaseValidatorModel):
    pass


class CreateTestCaseRequest(BaseValidatorModel):
    name: str
    steps: Sequence[StepUnion]
    description: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class TestCasesUnion(BaseValidatorModel):
    pass


class CreateTestSuiteRequest(BaseValidatorModel):
    name: str
    testCases: TestCasesUnion
    description: Optional[str] = None
    beforeSteps: Optional[Sequence[StepUnion]] = None
    afterSteps: Optional[Sequence[StepUnion]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateTestCaseRequest(BaseValidatorModel):
    testCaseId: str
    description: Optional[str] = None
    steps: Optional[Sequence[StepUnion]] = None


class UpdateTestSuiteRequest(BaseValidatorModel):
    testSuiteId: str
    description: Optional[str] = None
    beforeSteps: Optional[Sequence[StepUnion]] = None
    afterSteps: Optional[Sequence[StepUnion]] = None
    testCases: Optional[TestCasesUnion] = None



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

class BatchOutputTypeDef(BaseValidatorModel):
    batchJobName: str
    batchJobParameters: Optional[Dict[str, str]] = None
    exportDataSetNames: Optional[List[str]] = None


class MainframeActionPropertiesTypeDef(BaseValidatorModel):
    dmsTaskArn: Optional[str] = None


class BatchTypeDef(BaseValidatorModel):
    batchJobName: str
    batchJobParameters: Optional[Mapping[str, str]] = None
    exportDataSetNames: Optional[Sequence[str]] = None


class CloudFormationActionTypeDef(BaseValidatorModel):
    resource: str
    actionType: Optional[CloudFormationActionTypeType] = None


class CloudFormationOutputTypeDef(BaseValidatorModel):
    templateLocation: str
    parameters: Optional[Dict[str, str]] = None


class CloudFormationTypeDef(BaseValidatorModel):
    templateLocation: str
    parameters: Optional[Mapping[str, str]] = None


class CompareDataSetsStepOutputTypeDef(BaseValidatorModel):
    comparisonOutputLocation: str
    comparisonStatus: ComparisonStatusEnumType


class CompareDatabaseCDCStepOutputTypeDef(BaseValidatorModel):
    comparisonOutputLocation: str
    comparisonStatus: ComparisonStatusEnumType


class CreateCloudFormationStepInputTypeDef(BaseValidatorModel):
    templateLocation: str
    parameters: Optional[Dict[str, str]] = None


class CreateCloudFormationStepOutputTypeDef(BaseValidatorModel):
    stackId: str
    exports: Optional[Dict[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ServiceSettingsTypeDef(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class DeleteCloudFormationStepInputTypeDef(BaseValidatorModel):
    stackId: str


class DeleteTestCaseRequestTypeDef(BaseValidatorModel):
    testCaseId: str


class DeleteTestConfigurationRequestTypeDef(BaseValidatorModel):
    testConfigurationId: str


class DeleteTestRunRequestTypeDef(BaseValidatorModel):
    testRunId: str


class DeleteTestSuiteRequestTypeDef(BaseValidatorModel):
    testSuiteId: str


class GetTestCaseRequestTypeDef(BaseValidatorModel):
    testCaseId: str
    testCaseVersion: Optional[int] = None


class TestCaseLatestVersionTypeDef(BaseValidatorModel):
    version: int
    status: TestCaseLifecycleType
    statusReason: Optional[str] = None


class GetTestConfigurationRequestTypeDef(BaseValidatorModel):
    testConfigurationId: str
    testConfigurationVersion: Optional[int] = None


class TestConfigurationLatestVersionTypeDef(BaseValidatorModel):
    version: int
    status: TestConfigurationLifecycleType
    statusReason: Optional[str] = None


class GetTestRunStepRequestTypeDef(BaseValidatorModel):
    testRunId: str
    stepName: str
    testCaseId: Optional[str] = None
    testSuiteId: Optional[str] = None


class GetTestSuiteRequestTypeDef(BaseValidatorModel):
    testSuiteId: str
    testSuiteVersion: Optional[int] = None


class TestCasesOutputTypeDef(BaseValidatorModel):
    sequential: Optional[List[str]] = None


class TestSuiteLatestVersionTypeDef(BaseValidatorModel):
    version: int
    status: TestSuiteLifecycleType
    statusReason: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTestCasesRequestTypeDef(BaseValidatorModel):
    testCaseIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestCaseSummaryTypeDef(BaseValidatorModel):
    testCaseId: str
    testCaseArn: str
    name: str
    latestVersion: int
    status: TestCaseLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: Optional[str] = None


class ListTestConfigurationsRequestTypeDef(BaseValidatorModel):
    testConfigurationIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestConfigurationSummaryTypeDef(BaseValidatorModel):
    testConfigurationId: str
    name: str
    latestVersion: int
    testConfigurationArn: str
    status: TestConfigurationLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: Optional[str] = None


class ListTestRunStepsRequestTypeDef(BaseValidatorModel):
    testRunId: str
    testCaseId: Optional[str] = None
    testSuiteId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestRunStepSummaryTypeDef(BaseValidatorModel):
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


class ListTestRunTestCasesRequestTypeDef(BaseValidatorModel):
    testRunId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestCaseRunSummaryTypeDef(BaseValidatorModel):
    testCaseId: str
    testCaseVersion: int
    testRunId: str
    status: TestCaseRunStatusType
    runStartTime: datetime
    statusReason: Optional[str] = None
    runEndTime: Optional[datetime] = None


class ListTestRunsRequestTypeDef(BaseValidatorModel):
    testSuiteId: Optional[str] = None
    testRunIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestRunSummaryTypeDef(BaseValidatorModel):
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


class ListTestSuitesRequestTypeDef(BaseValidatorModel):
    testSuiteIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestSuiteSummaryTypeDef(BaseValidatorModel):
    testSuiteId: str
    name: str
    latestVersion: int
    testSuiteArn: str
    status: TestSuiteLifecycleType
    creationTime: datetime
    lastUpdateTime: datetime
    statusReason: Optional[str] = None


class M2ManagedActionPropertiesTypeDef(BaseValidatorModel):
    forceStop: Optional[bool] = None
    importDataSetLocation: Optional[str] = None


class M2ManagedApplicationStepOutputTypeDef(BaseValidatorModel):
    importDataSetSummary: Optional[Dict[str, str]] = None


class M2ManagedApplicationSummaryTypeDef(BaseValidatorModel):
    applicationId: str
    runtime: Literal["MicroFocus"]
    listenerPort: Optional[int] = None


class M2ManagedApplicationTypeDef(BaseValidatorModel):
    applicationId: str
    runtime: Literal["MicroFocus"]
    vpcEndpointServiceName: Optional[str] = None
    listenerPort: Optional[str] = None


class M2NonManagedApplicationActionTypeDef(BaseValidatorModel):
    resource: str
    actionType: M2NonManagedActionTypeType


class M2NonManagedApplicationStepInputTypeDef(BaseValidatorModel):
    vpcEndpointServiceName: str
    listenerPort: int
    runtime: Literal["BluAge"]
    actionType: M2NonManagedActionTypeType
    webAppName: Optional[str] = None


class M2NonManagedApplicationSummaryTypeDef(BaseValidatorModel):
    vpcEndpointServiceName: str
    listenerPort: int
    runtime: Literal["BluAge"]
    webAppName: Optional[str] = None


class M2NonManagedApplicationTypeDef(BaseValidatorModel):
    vpcEndpointServiceName: str
    listenerPort: str
    runtime: Literal["BluAge"]
    webAppName: Optional[str] = None


class OutputFileTypeDef(BaseValidatorModel):
    fileLocation: Optional[str] = None


class StartTestRunRequestTypeDef(BaseValidatorModel):
    testSuiteId: str
    testConfigurationId: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TestCasesTypeDef(BaseValidatorModel):
    sequential: Optional[Sequence[str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class DataSetTypeDef(BaseValidatorModel):
    pass


class BatchStepOutputTypeDef(BaseValidatorModel):
    dataSetExportLocation: Optional[str] = None
    dmsOutputLocation: Optional[str] = None
    dataSetDetails: Optional[List[DataSetTypeDef]] = None


class CompareDataSetsStepInputTypeDef(BaseValidatorModel):
    sourceLocation: str
    targetLocation: str
    sourceDataSets: List[DataSetTypeDef]
    targetDataSets: List[DataSetTypeDef]


class TN3270StepOutputTypeDef(BaseValidatorModel):
    scriptOutputLocation: str
    dataSetExportLocation: Optional[str] = None
    dmsOutputLocation: Optional[str] = None
    dataSetDetails: Optional[List[DataSetTypeDef]] = None


class TargetDatabaseMetadataTypeDef(BaseValidatorModel):
    pass


class SourceDatabaseMetadataTypeDef(BaseValidatorModel):
    pass


class CompareDatabaseCDCStepInputTypeDef(BaseValidatorModel):
    sourceLocation: str
    targetLocation: str
    sourceMetadata: SourceDatabaseMetadataTypeDef
    targetMetadata: TargetDatabaseMetadataTypeDef
    outputLocation: Optional[str] = None


class DatabaseCDCTypeDef(BaseValidatorModel):
    sourceMetadata: SourceDatabaseMetadataTypeDef
    targetMetadata: TargetDatabaseMetadataTypeDef


class CreateCloudFormationSummaryTypeDef(BaseValidatorModel):
    stepInput: CreateCloudFormationStepInputTypeDef
    stepOutput: Optional[CreateCloudFormationStepOutputTypeDef] = None


class CreateTestCaseResponseTypeDef(BaseValidatorModel):
    testCaseId: str
    testCaseVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTestConfigurationResponseTypeDef(BaseValidatorModel):
    testConfigurationId: str
    testConfigurationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTestSuiteResponseTypeDef(BaseValidatorModel):
    testSuiteId: str
    testSuiteVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartTestRunResponseTypeDef(BaseValidatorModel):
    testRunId: str
    testRunStatus: TestRunStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTestCaseResponseTypeDef(BaseValidatorModel):
    testCaseId: str
    testCaseVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTestConfigurationResponseTypeDef(BaseValidatorModel):
    testConfigurationId: str
    testConfigurationVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTestSuiteResponseTypeDef(BaseValidatorModel):
    testSuiteId: str
    testSuiteVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCloudFormationSummaryTypeDef(BaseValidatorModel):
    stepInput: DeleteCloudFormationStepInputTypeDef
    stepOutput: Optional[Dict[str, Any]] = None


class ListTestCasesRequestPaginateTypeDef(BaseValidatorModel):
    testCaseIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTestConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    testConfigurationIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTestRunStepsRequestPaginateTypeDef(BaseValidatorModel):
    testRunId: str
    testCaseId: Optional[str] = None
    testSuiteId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTestRunTestCasesRequestPaginateTypeDef(BaseValidatorModel):
    testRunId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTestRunsRequestPaginateTypeDef(BaseValidatorModel):
    testSuiteId: Optional[str] = None
    testRunIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTestSuitesRequestPaginateTypeDef(BaseValidatorModel):
    testSuiteIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTestCasesResponseTypeDef(BaseValidatorModel):
    testCases: List[TestCaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTestConfigurationsResponseTypeDef(BaseValidatorModel):
    testConfigurations: List[TestConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTestRunStepsResponseTypeDef(BaseValidatorModel):
    testRunSteps: List[TestRunStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTestRunTestCasesResponseTypeDef(BaseValidatorModel):
    testRunTestCases: List[TestCaseRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTestRunsResponseTypeDef(BaseValidatorModel):
    testRuns: List[TestRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTestSuitesResponseTypeDef(BaseValidatorModel):
    testSuites: List[TestSuiteSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class M2ManagedApplicationActionTypeDef(BaseValidatorModel):
    resource: str
    actionType: M2ManagedActionTypeType
    properties: Optional[M2ManagedActionPropertiesTypeDef] = None


class M2ManagedApplicationStepInputTypeDef(BaseValidatorModel):
    applicationId: str
    runtime: str
    actionType: M2ManagedActionTypeType
    vpcEndpointServiceName: Optional[str] = None
    listenerPort: Optional[int] = None
    properties: Optional[M2ManagedActionPropertiesTypeDef] = None


class M2NonManagedApplicationStepSummaryTypeDef(BaseValidatorModel):
    stepInput: M2NonManagedApplicationStepInputTypeDef
    stepOutput: Optional[Dict[str, Any]] = None


class MainframeResourceSummaryTypeDef(BaseValidatorModel):
    m2ManagedApplication: Optional[M2ManagedApplicationSummaryTypeDef] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationSummaryTypeDef] = None


class ResourceTypeOutputTypeDef(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationOutputTypeDef] = None
    m2ManagedApplication: Optional[M2ManagedApplicationTypeDef] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationTypeDef] = None


class OutputTypeDef(BaseValidatorModel):
    file: Optional[OutputFileTypeDef] = None


class ScriptTypeDef(BaseValidatorModel):
    pass


class TN3270OutputTypeDef(BaseValidatorModel):
    script: ScriptTypeDef
    exportDataSetNames: Optional[List[str]] = None


class TN3270TypeDef(BaseValidatorModel):
    script: ScriptTypeDef
    exportDataSetNames: Optional[Sequence[str]] = None


class CompareDataSetsSummaryTypeDef(BaseValidatorModel):
    stepInput: CompareDataSetsStepInputTypeDef
    stepOutput: Optional[CompareDataSetsStepOutputTypeDef] = None


class CloudFormationUnionTypeDef(BaseValidatorModel):
    pass


class ResourceTypeTypeDef(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationUnionTypeDef] = None
    m2ManagedApplication: Optional[M2ManagedApplicationTypeDef] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationTypeDef] = None


class CompareDatabaseCDCSummaryTypeDef(BaseValidatorModel):
    stepInput: CompareDatabaseCDCStepInputTypeDef
    stepOutput: Optional[CompareDatabaseCDCStepOutputTypeDef] = None


class FileMetadataOutputTypeDef(BaseValidatorModel):
    dataSets: Optional[List[DataSetTypeDef]] = None
    databaseCDC: Optional[DatabaseCDCTypeDef] = None


class FileMetadataTypeDef(BaseValidatorModel):
    dataSets: Optional[Sequence[DataSetTypeDef]] = None
    databaseCDC: Optional[DatabaseCDCTypeDef] = None


class CloudFormationStepSummaryTypeDef(BaseValidatorModel):
    createCloudformation: Optional[CreateCloudFormationSummaryTypeDef] = None
    deleteCloudformation: Optional[DeleteCloudFormationSummaryTypeDef] = None


class ResourceActionTypeDef(BaseValidatorModel):
    m2ManagedApplicationAction: Optional[M2ManagedApplicationActionTypeDef] = None
    m2NonManagedApplicationAction: Optional[M2NonManagedApplicationActionTypeDef] = None
    cloudFormationAction: Optional[CloudFormationActionTypeDef] = None


class M2ManagedApplicationStepSummaryTypeDef(BaseValidatorModel):
    stepInput: M2ManagedApplicationStepInputTypeDef
    stepOutput: Optional[M2ManagedApplicationStepOutputTypeDef] = None


class BatchStepInputTypeDef(BaseValidatorModel):
    resource: MainframeResourceSummaryTypeDef
    batchJobName: str
    batchJobParameters: Optional[Dict[str, str]] = None
    exportDataSetNames: Optional[List[str]] = None
    properties: Optional[MainframeActionPropertiesTypeDef] = None


class ScriptSummaryTypeDef(BaseValidatorModel):
    pass


class TN3270StepInputTypeDef(BaseValidatorModel):
    resource: MainframeResourceSummaryTypeDef
    script: ScriptSummaryTypeDef
    exportDataSetNames: Optional[List[str]] = None
    properties: Optional[MainframeActionPropertiesTypeDef] = None


class MainframeActionTypeOutputTypeDef(BaseValidatorModel):
    batch: Optional[BatchOutputTypeDef] = None
    tn3270: Optional[TN3270OutputTypeDef] = None


class CompareFileTypeTypeDef(BaseValidatorModel):
    datasets: Optional[CompareDataSetsSummaryTypeDef] = None
    databaseCDC: Optional[CompareDatabaseCDCSummaryTypeDef] = None


class InputFileOutputTypeDef(BaseValidatorModel):
    sourceLocation: str
    targetLocation: str
    fileMetadata: FileMetadataOutputTypeDef


class ResourceActionSummaryTypeDef(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationStepSummaryTypeDef] = None
    m2ManagedApplication: Optional[M2ManagedApplicationStepSummaryTypeDef] = None
    m2NonManagedApplication: Optional[M2NonManagedApplicationStepSummaryTypeDef] = None


class BatchSummaryTypeDef(BaseValidatorModel):
    stepInput: BatchStepInputTypeDef
    stepOutput: Optional[BatchStepOutputTypeDef] = None


class TN3270SummaryTypeDef(BaseValidatorModel):
    stepInput: TN3270StepInputTypeDef
    stepOutput: Optional[TN3270StepOutputTypeDef] = None


class ResourceOutputTypeDef(BaseValidatorModel):
    pass


class GetTestConfigurationResponseTypeDef(BaseValidatorModel):
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


class MainframeActionOutputTypeDef(BaseValidatorModel):
    resource: str
    actionType: MainframeActionTypeOutputTypeDef
    properties: Optional[MainframeActionPropertiesTypeDef] = None


class TN3270UnionTypeDef(BaseValidatorModel):
    pass


class BatchUnionTypeDef(BaseValidatorModel):
    pass


class MainframeActionTypeTypeDef(BaseValidatorModel):
    batch: Optional[BatchUnionTypeDef] = None
    tn3270: Optional[TN3270UnionTypeDef] = None


class FileTypeDef(BaseValidatorModel):
    fileType: Optional[CompareFileTypeTypeDef] = None


class InputOutputTypeDef(BaseValidatorModel):
    file: Optional[InputFileOutputTypeDef] = None


class FileMetadataUnionTypeDef(BaseValidatorModel):
    pass


class InputFileTypeDef(BaseValidatorModel):
    sourceLocation: str
    targetLocation: str
    fileMetadata: FileMetadataUnionTypeDef


class MainframeActionSummaryTypeDef(BaseValidatorModel):
    batch: Optional[BatchSummaryTypeDef] = None
    tn3270: Optional[TN3270SummaryTypeDef] = None


class MainframeActionTypeUnionTypeDef(BaseValidatorModel):
    pass


class MainframeActionTypeDef(BaseValidatorModel):
    resource: str
    actionType: MainframeActionTypeUnionTypeDef
    properties: Optional[MainframeActionPropertiesTypeDef] = None


class ResourceUnionTypeDef(BaseValidatorModel):
    pass


class CreateTestConfigurationRequestTypeDef(BaseValidatorModel):
    name: str
    resources: Sequence[ResourceUnionTypeDef]
    description: Optional[str] = None
    properties: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    serviceSettings: Optional[ServiceSettingsTypeDef] = None


class UpdateTestConfigurationRequestTypeDef(BaseValidatorModel):
    testConfigurationId: str
    description: Optional[str] = None
    resources: Optional[Sequence[ResourceUnionTypeDef]] = None
    properties: Optional[Mapping[str, str]] = None
    serviceSettings: Optional[ServiceSettingsTypeDef] = None


class CompareActionSummaryTypeDef(BaseValidatorModel):
    pass


class StepRunSummaryTypeDef(BaseValidatorModel):
    mainframeAction: Optional[MainframeActionSummaryTypeDef] = None
    compareAction: Optional[CompareActionSummaryTypeDef] = None
    resourceAction: Optional[ResourceActionSummaryTypeDef] = None


class CompareActionOutputTypeDef(BaseValidatorModel):
    pass


class StepActionOutputTypeDef(BaseValidatorModel):
    resourceAction: Optional[ResourceActionTypeDef] = None
    mainframeAction: Optional[MainframeActionOutputTypeDef] = None
    compareAction: Optional[CompareActionOutputTypeDef] = None


class InputFileUnionTypeDef(BaseValidatorModel):
    pass


class InputTypeDef(BaseValidatorModel):
    file: Optional[InputFileUnionTypeDef] = None


class GetTestRunStepResponseTypeDef(BaseValidatorModel):
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


class StepOutputTypeDef(BaseValidatorModel):
    name: str
    action: StepActionOutputTypeDef
    description: Optional[str] = None


class GetTestCaseResponseTypeDef(BaseValidatorModel):
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


class GetTestSuiteResponseTypeDef(BaseValidatorModel):
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


class MainframeActionUnionTypeDef(BaseValidatorModel):
    pass


class CompareActionUnionTypeDef(BaseValidatorModel):
    pass


class StepActionTypeDef(BaseValidatorModel):
    resourceAction: Optional[ResourceActionTypeDef] = None
    mainframeAction: Optional[MainframeActionUnionTypeDef] = None
    compareAction: Optional[CompareActionUnionTypeDef] = None


class StepActionUnionTypeDef(BaseValidatorModel):
    pass


class StepTypeDef(BaseValidatorModel):
    name: str
    action: StepActionUnionTypeDef
    description: Optional[str] = None


class StepUnionTypeDef(BaseValidatorModel):
    pass


class CreateTestCaseRequestTypeDef(BaseValidatorModel):
    name: str
    steps: Sequence[StepUnionTypeDef]
    description: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class TestCasesUnionTypeDef(BaseValidatorModel):
    pass


class CreateTestSuiteRequestTypeDef(BaseValidatorModel):
    name: str
    testCases: TestCasesUnionTypeDef
    description: Optional[str] = None
    beforeSteps: Optional[Sequence[StepUnionTypeDef]] = None
    afterSteps: Optional[Sequence[StepUnionTypeDef]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateTestCaseRequestTypeDef(BaseValidatorModel):
    testCaseId: str
    description: Optional[str] = None
    steps: Optional[Sequence[StepUnionTypeDef]] = None


class UpdateTestSuiteRequestTypeDef(BaseValidatorModel):
    testSuiteId: str
    description: Optional[str] = None
    beforeSteps: Optional[Sequence[StepUnionTypeDef]] = None
    afterSteps: Optional[Sequence[StepUnionTypeDef]] = None
    testCases: Optional[TestCasesUnionTypeDef] = None



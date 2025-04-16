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
from aws_resource_validator.pydantic_models.iotdeviceadvisor_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteSuiteDefinitionRequest(BaseValidatorModel):
    suiteDefinitionId: str


class DeviceUnderTest(BaseValidatorModel):
    thingArn: Optional[str] = None
    certificateArn: Optional[str] = None
    deviceRoleArn: Optional[str] = None


class GetEndpointRequest(BaseValidatorModel):
    thingArn: Optional[str] = None
    certificateArn: Optional[str] = None
    deviceRoleArn: Optional[str] = None
    authenticationMethod: Optional[AuthenticationMethodType] = None


class GetSuiteDefinitionRequest(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionVersion: Optional[str] = None


class GetSuiteRunReportRequest(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunId: str


class GetSuiteRunRequest(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunId: str


class ListSuiteDefinitionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSuiteRunsRequest(BaseValidatorModel):
    suiteDefinitionId: Optional[str] = None
    suiteDefinitionVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SuiteRunInformation(BaseValidatorModel):
    suiteDefinitionId: Optional[str] = None
    suiteDefinitionVersion: Optional[str] = None
    suiteDefinitionName: Optional[str] = None
    suiteRunId: Optional[str] = None
    createdAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    endAt: Optional[datetime] = None
    status: Optional[SuiteRunStatusType] = None
    passed: Optional[int] = None
    failed: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class StopSuiteRunRequest(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunId: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TestCaseScenario(BaseValidatorModel):
    testCaseScenarioId: Optional[str] = None
    testCaseScenarioType: Optional[TestCaseScenarioTypeType] = None
    status: Optional[TestCaseScenarioStatusType] = None
    failure: Optional[str] = None
    systemMessage: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateSuiteDefinitionResponse(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionName: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


class GetEndpointResponse(BaseValidatorModel):
    endpoint: str
    ResponseMetadata: ResponseMetadata


class GetSuiteRunReportResponse(BaseValidatorModel):
    qualificationReportDownloadUrl: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartSuiteRunResponse(BaseValidatorModel):
    suiteRunId: str
    suiteRunArn: str
    createdAt: datetime
    endpoint: str
    ResponseMetadata: ResponseMetadata


class UpdateSuiteDefinitionResponse(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionName: str
    suiteDefinitionVersion: str
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class SuiteDefinitionConfigurationOutput(BaseValidatorModel):
    suiteDefinitionName: str
    rootGroup: str
    devicePermissionRoleArn: str
    devices: Optional[List[DeviceUnderTest]] = None
    intendedForQualification: Optional[bool] = None
    isLongDurationTest: Optional[bool] = None
    protocol: Optional[ProtocolType] = None


class SuiteDefinitionConfiguration(BaseValidatorModel):
    suiteDefinitionName: str
    rootGroup: str
    devicePermissionRoleArn: str
    devices: Optional[Sequence[DeviceUnderTest]] = None
    intendedForQualification: Optional[bool] = None
    isLongDurationTest: Optional[bool] = None
    protocol: Optional[ProtocolType] = None


class SuiteDefinitionInformation(BaseValidatorModel):
    suiteDefinitionId: Optional[str] = None
    suiteDefinitionName: Optional[str] = None
    defaultDevices: Optional[List[DeviceUnderTest]] = None
    intendedForQualification: Optional[bool] = None
    isLongDurationTest: Optional[bool] = None
    protocol: Optional[ProtocolType] = None
    createdAt: Optional[datetime] = None


class SuiteRunConfigurationOutput(BaseValidatorModel):
    primaryDevice: DeviceUnderTest
    selectedTestList: Optional[List[str]] = None
    parallelRun: Optional[bool] = None


class SuiteRunConfiguration(BaseValidatorModel):
    primaryDevice: DeviceUnderTest
    selectedTestList: Optional[Sequence[str]] = None
    parallelRun: Optional[bool] = None


class ListSuiteRunsResponse(BaseValidatorModel):
    suiteRunsList: List[SuiteRunInformation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TestCaseRun(BaseValidatorModel):
    testCaseRunId: Optional[str] = None
    testCaseDefinitionId: Optional[str] = None
    testCaseDefinitionName: Optional[str] = None
    status: Optional[StatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    logUrl: Optional[str] = None
    warnings: Optional[str] = None
    failure: Optional[str] = None
    testScenarios: Optional[List[TestCaseScenario]] = None


class GetSuiteDefinitionResponse(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionVersion: str
    latestVersion: str
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationOutput
    createdAt: datetime
    lastModifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListSuiteDefinitionsResponse(BaseValidatorModel):
    suiteDefinitionInformationList: List[SuiteDefinitionInformation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GroupResult(BaseValidatorModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None
    tests: Optional[List[TestCaseRun]] = None


class SuiteDefinitionConfigurationUnion(BaseValidatorModel):
    pass


class CreateSuiteDefinitionRequest(BaseValidatorModel):
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationUnion
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class UpdateSuiteDefinitionRequest(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationUnion


class SuiteRunConfigurationUnion(BaseValidatorModel):
    pass


class StartSuiteRunRequest(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunConfiguration: SuiteRunConfigurationUnion
    suiteDefinitionVersion: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class TestResult(BaseValidatorModel):
    groups: Optional[List[GroupResult]] = None


class GetSuiteRunResponse(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionVersion: str
    suiteRunId: str
    suiteRunArn: str
    suiteRunConfiguration: SuiteRunConfigurationOutput
    testResult: TestResult
    startTime: datetime
    endTime: datetime
    status: SuiteRunStatusType
    errorReason: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata



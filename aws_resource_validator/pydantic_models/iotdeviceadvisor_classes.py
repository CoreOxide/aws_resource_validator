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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteSuiteDefinitionRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str


class DeviceUnderTestTypeDef(BaseValidatorModel):
    thingArn: Optional[str] = None
    certificateArn: Optional[str] = None
    deviceRoleArn: Optional[str] = None


class GetEndpointRequestTypeDef(BaseValidatorModel):
    thingArn: Optional[str] = None
    certificateArn: Optional[str] = None
    deviceRoleArn: Optional[str] = None
    authenticationMethod: Optional[AuthenticationMethodType] = None


class GetSuiteDefinitionRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionVersion: Optional[str] = None


class GetSuiteRunReportRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunId: str


class GetSuiteRunRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunId: str


class ListSuiteDefinitionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSuiteRunsRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: Optional[str] = None
    suiteDefinitionVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SuiteRunInformationTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class StopSuiteRunRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TestCaseScenarioTypeDef(BaseValidatorModel):
    testCaseScenarioId: Optional[str] = None
    testCaseScenarioType: Optional[TestCaseScenarioTypeType] = None
    status: Optional[TestCaseScenarioStatusType] = None
    failure: Optional[str] = None
    systemMessage: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CreateSuiteDefinitionResponseTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionName: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetEndpointResponseTypeDef(BaseValidatorModel):
    endpoint: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSuiteRunReportResponseTypeDef(BaseValidatorModel):
    qualificationReportDownloadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartSuiteRunResponseTypeDef(BaseValidatorModel):
    suiteRunId: str
    suiteRunArn: str
    createdAt: datetime
    endpoint: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSuiteDefinitionResponseTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionName: str
    suiteDefinitionVersion: str
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class SuiteDefinitionConfigurationOutputTypeDef(BaseValidatorModel):
    suiteDefinitionName: str
    rootGroup: str
    devicePermissionRoleArn: str
    devices: Optional[List[DeviceUnderTestTypeDef]] = None
    intendedForQualification: Optional[bool] = None
    isLongDurationTest: Optional[bool] = None
    protocol: Optional[ProtocolType] = None


class SuiteDefinitionConfigurationTypeDef(BaseValidatorModel):
    suiteDefinitionName: str
    rootGroup: str
    devicePermissionRoleArn: str
    devices: Optional[Sequence[DeviceUnderTestTypeDef]] = None
    intendedForQualification: Optional[bool] = None
    isLongDurationTest: Optional[bool] = None
    protocol: Optional[ProtocolType] = None


class SuiteDefinitionInformationTypeDef(BaseValidatorModel):
    suiteDefinitionId: Optional[str] = None
    suiteDefinitionName: Optional[str] = None
    defaultDevices: Optional[List[DeviceUnderTestTypeDef]] = None
    intendedForQualification: Optional[bool] = None
    isLongDurationTest: Optional[bool] = None
    protocol: Optional[ProtocolType] = None
    createdAt: Optional[datetime] = None


class SuiteRunConfigurationOutputTypeDef(BaseValidatorModel):
    primaryDevice: DeviceUnderTestTypeDef
    selectedTestList: Optional[List[str]] = None
    parallelRun: Optional[bool] = None


class SuiteRunConfigurationTypeDef(BaseValidatorModel):
    primaryDevice: DeviceUnderTestTypeDef
    selectedTestList: Optional[Sequence[str]] = None
    parallelRun: Optional[bool] = None


class ListSuiteRunsResponseTypeDef(BaseValidatorModel):
    suiteRunsList: List[SuiteRunInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TestCaseRunTypeDef(BaseValidatorModel):
    testCaseRunId: Optional[str] = None
    testCaseDefinitionId: Optional[str] = None
    testCaseDefinitionName: Optional[str] = None
    status: Optional[StatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    logUrl: Optional[str] = None
    warnings: Optional[str] = None
    failure: Optional[str] = None
    testScenarios: Optional[List[TestCaseScenarioTypeDef]] = None


class GetSuiteDefinitionResponseTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionVersion: str
    latestVersion: str
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationOutputTypeDef
    createdAt: datetime
    lastModifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListSuiteDefinitionsResponseTypeDef(BaseValidatorModel):
    suiteDefinitionInformationList: List[SuiteDefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GroupResultTypeDef(BaseValidatorModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None
    tests: Optional[List[TestCaseRunTypeDef]] = None


class SuiteDefinitionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateSuiteDefinitionRequestTypeDef(BaseValidatorModel):
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationUnionTypeDef
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class UpdateSuiteDefinitionRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationUnionTypeDef


class SuiteRunConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class StartSuiteRunRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunConfiguration: SuiteRunConfigurationUnionTypeDef
    suiteDefinitionVersion: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class TestResultTypeDef(BaseValidatorModel):
    groups: Optional[List[GroupResultTypeDef]] = None


class GetSuiteRunResponseTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionVersion: str
    suiteRunId: str
    suiteRunArn: str
    suiteRunConfiguration: SuiteRunConfigurationOutputTypeDef
    testResult: TestResultTypeDef
    startTime: datetime
    endTime: datetime
    status: SuiteRunStatusType
    errorReason: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef



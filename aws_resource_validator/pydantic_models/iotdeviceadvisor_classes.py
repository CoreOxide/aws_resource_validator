from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteSuiteDefinitionRequestRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str

class DeviceUnderTestTypeDef(BaseValidatorModel):
    thingArn: Optional[str] = None
    certificateArn: Optional[str] = None
    deviceRoleArn: Optional[str] = None

class GetEndpointRequestRequestTypeDef(BaseValidatorModel):
    thingArn: Optional[str] = None
    certificateArn: Optional[str] = None
    deviceRoleArn: Optional[str] = None
    authenticationMethod: Optional[AuthenticationMethodType] = None

class GetSuiteDefinitionRequestRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionVersion: Optional[str] = None

class GetSuiteRunReportRequestRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunId: str

class GetSuiteRunRequestRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunId: str

class ListSuiteDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSuiteRunsRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class StopSuiteRunRequestRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TestCaseScenarioTypeDef(BaseValidatorModel):
    testCaseScenarioId: Optional[str] = None
    testCaseScenarioType: Optional[TestCaseScenarioTypeType] = None
    status: Optional[TestCaseScenarioStatusType] = None
    failure: Optional[str] = None
    systemMessage: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
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

class SuiteRunConfigurationTypeDef(BaseValidatorModel):
    primaryDevice: DeviceUnderTestTypeDef
    selectedTestList: Optional[List[str]] = None
    parallelRun: Optional[bool] = None

class ListSuiteRunsResponseTypeDef(BaseValidatorModel):
    suiteRunsList: List[SuiteRunInformationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class CreateSuiteDefinitionRequestRequestTypeDef(BaseValidatorModel):
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationTypeDef
    tags: Optional[Mapping[str, str]] = None

class GetSuiteDefinitionResponseTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionVersion: str
    latestVersion: str
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationTypeDef
    createdAt: datetime
    lastModifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSuiteDefinitionRequestRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationTypeDef

class ListSuiteDefinitionsResponseTypeDef(BaseValidatorModel):
    suiteDefinitionInformationList: List[SuiteDefinitionInformationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSuiteRunRequestRequestTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteRunConfiguration: SuiteRunConfigurationTypeDef
    suiteDefinitionVersion: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GroupResultTypeDef(BaseValidatorModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None
    tests: Optional[List[TestCaseRunTypeDef]] = None

class TestResultTypeDef(BaseValidatorModel):
    groups: Optional[List[GroupResultTypeDef]] = None

class GetSuiteRunResponseTypeDef(BaseValidatorModel):
    suiteDefinitionId: str
    suiteDefinitionVersion: str
    suiteRunId: str
    suiteRunArn: str
    suiteRunConfiguration: SuiteRunConfigurationTypeDef
    testResult: TestResultTypeDef
    startTime: datetime
    endTime: datetime
    status: SuiteRunStatusType
    errorReason: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


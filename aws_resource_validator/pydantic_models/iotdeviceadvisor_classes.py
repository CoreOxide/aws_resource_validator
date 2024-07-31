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
from aws_resource_validator.pydantic_models.iotdeviceadvisor_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteSuiteDefinitionRequestRequestTypeDef(BaseModel):
    suiteDefinitionId: str

class DeviceUnderTestTypeDef(BaseModel):
    thingArn: Optional[str] = None
    certificateArn: Optional[str] = None
    deviceRoleArn: Optional[str] = None

class GetEndpointRequestRequestTypeDef(BaseModel):
    thingArn: Optional[str] = None
    certificateArn: Optional[str] = None
    deviceRoleArn: Optional[str] = None
    authenticationMethod: Optional[AuthenticationMethodType] = None

class GetSuiteDefinitionRequestRequestTypeDef(BaseModel):
    suiteDefinitionId: str
    suiteDefinitionVersion: Optional[str] = None

class GetSuiteRunReportRequestRequestTypeDef(BaseModel):
    suiteDefinitionId: str
    suiteRunId: str

class GetSuiteRunRequestRequestTypeDef(BaseModel):
    suiteDefinitionId: str
    suiteRunId: str

class ListSuiteDefinitionsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSuiteRunsRequestRequestTypeDef(BaseModel):
    suiteDefinitionId: Optional[str] = None
    suiteDefinitionVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SuiteRunInformationTypeDef(BaseModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class StopSuiteRunRequestRequestTypeDef(BaseModel):
    suiteDefinitionId: str
    suiteRunId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TestCaseScenarioTypeDef(BaseModel):
    testCaseScenarioId: Optional[str] = None
    testCaseScenarioType: Optional[TestCaseScenarioTypeType] = None
    status: Optional[TestCaseScenarioStatusType] = None
    failure: Optional[str] = None
    systemMessage: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateSuiteDefinitionResponseTypeDef(BaseModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionName: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetEndpointResponseTypeDef(BaseModel):
    endpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSuiteRunReportResponseTypeDef(BaseModel):
    qualificationReportDownloadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSuiteRunResponseTypeDef(BaseModel):
    suiteRunId: str
    suiteRunArn: str
    createdAt: datetime
    endpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSuiteDefinitionResponseTypeDef(BaseModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionName: str
    suiteDefinitionVersion: str
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SuiteDefinitionConfigurationTypeDef(BaseModel):
    suiteDefinitionName: str
    rootGroup: str
    devicePermissionRoleArn: str
    devices: Optional[Sequence[DeviceUnderTestTypeDef]] = None
    intendedForQualification: Optional[bool] = None
    isLongDurationTest: Optional[bool] = None
    protocol: Optional[ProtocolType] = None

class SuiteDefinitionInformationTypeDef(BaseModel):
    suiteDefinitionId: Optional[str] = None
    suiteDefinitionName: Optional[str] = None
    defaultDevices: Optional[List[DeviceUnderTestTypeDef]] = None
    intendedForQualification: Optional[bool] = None
    isLongDurationTest: Optional[bool] = None
    protocol: Optional[ProtocolType] = None
    createdAt: Optional[datetime] = None

class SuiteRunConfigurationTypeDef(BaseModel):
    primaryDevice: DeviceUnderTestTypeDef
    selectedTestList: Optional[List[str]] = None
    parallelRun: Optional[bool] = None

class ListSuiteRunsResponseTypeDef(BaseModel):
    suiteRunsList: List[SuiteRunInformationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestCaseRunTypeDef(BaseModel):
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

class CreateSuiteDefinitionRequestRequestTypeDef(BaseModel):
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationTypeDef
    tags: Optional[Mapping[str, str]] = None

class GetSuiteDefinitionResponseTypeDef(BaseModel):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionVersion: str
    latestVersion: str
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationTypeDef
    createdAt: datetime
    lastModifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSuiteDefinitionRequestRequestTypeDef(BaseModel):
    suiteDefinitionId: str
    suiteDefinitionConfiguration: SuiteDefinitionConfigurationTypeDef

class ListSuiteDefinitionsResponseTypeDef(BaseModel):
    suiteDefinitionInformationList: List[SuiteDefinitionInformationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSuiteRunRequestRequestTypeDef(BaseModel):
    suiteDefinitionId: str
    suiteRunConfiguration: SuiteRunConfigurationTypeDef
    suiteDefinitionVersion: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GroupResultTypeDef(BaseModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None
    tests: Optional[List[TestCaseRunTypeDef]] = None

class TestResultTypeDef(BaseModel):
    groups: Optional[List[GroupResultTypeDef]] = None

class GetSuiteRunResponseTypeDef(BaseModel):
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


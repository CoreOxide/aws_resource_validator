# iotdeviceadvisor_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateSuiteDefinitionRequestRequestTypeDef

### suiteDefinitionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteDefinitionConfigurationTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSuiteDefinitionResponseTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSuiteDefinitionRequestRequestTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeviceUnderTestTypeDef

### thingArn
- **Type**: typing.Optional[str]

### certificateArn
- **Type**: typing.Optional[str]

### deviceRoleArn
- **Type**: typing.Optional[str]


# GetEndpointRequestRequestTypeDef

### thingArn
- **Type**: typing.Optional[str]

### certificateArn
- **Type**: typing.Optional[str]

### deviceRoleArn
- **Type**: typing.Optional[str]

### authenticationMethod
- **Type**: typing.Optional[typing.Literal['SignatureVersion4', 'X509ClientCertificate']]


# GetEndpointResponseTypeDef

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSuiteDefinitionRequestRequestTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionVersion
- **Type**: typing.Optional[str]


# GetSuiteDefinitionResponseTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionVersion
- **Type**: <class 'str'>
- **Required**: Yes

### latestVersion
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteDefinitionConfigurationTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSuiteRunReportRequestRequestTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSuiteRunReportResponseTypeDef

### qualificationReportDownloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSuiteRunRequestRequestTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSuiteRunResponseTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionVersion
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteRunConfigurationTypeDef'>
- **Required**: Yes

### testResult
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.TestResultTypeDef'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELED', 'ERROR', 'FAIL', 'PASS', 'PASS_WITH_WARNINGS', 'PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### errorReason
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupResultTypeDef

### groupId
- **Type**: typing.Optional[str]

### groupName
- **Type**: typing.Optional[str]

### tests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.TestCaseRunTypeDef]]


# ListSuiteDefinitionsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSuiteDefinitionsResponseTypeDef

### suiteDefinitionInformationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteDefinitionInformationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSuiteRunsRequestRequestTypeDef

### suiteDefinitionId
- **Type**: typing.Optional[str]

### suiteDefinitionVersion
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSuiteRunsResponseTypeDef

### suiteRunsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteRunInformationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# StartSuiteRunRequestRequestTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteRunConfigurationTypeDef'>
- **Required**: Yes

### suiteDefinitionVersion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartSuiteRunResponseTypeDef

### suiteRunId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopSuiteRunRequestRequestTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunId
- **Type**: <class 'str'>
- **Required**: Yes


# SuiteDefinitionConfigurationTypeDef

### suiteDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### rootGroup
- **Type**: <class 'str'>
- **Required**: Yes

### devicePermissionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.DeviceUnderTestTypeDef]]

### intendedForQualification
- **Type**: typing.Optional[bool]

### isLongDurationTest
- **Type**: typing.Optional[bool]

### protocol
- **Type**: typing.Optional[typing.Literal['MqttV3_1_1', 'MqttV3_1_1_OverWebSocket', 'MqttV5', 'MqttV5_OverWebSocket']]


# SuiteDefinitionInformationTypeDef

### suiteDefinitionId
- **Type**: typing.Optional[str]

### suiteDefinitionName
- **Type**: typing.Optional[str]

### defaultDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.DeviceUnderTestTypeDef]]

### intendedForQualification
- **Type**: typing.Optional[bool]

### isLongDurationTest
- **Type**: typing.Optional[bool]

### protocol
- **Type**: typing.Optional[typing.Literal['MqttV3_1_1', 'MqttV3_1_1_OverWebSocket', 'MqttV5', 'MqttV5_OverWebSocket']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# SuiteRunConfigurationTypeDef

### primaryDevice
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.DeviceUnderTestTypeDef'>
- **Required**: Yes

### selectedTestList
- **Type**: typing.Optional[typing.List[str]]

### parallelRun
- **Type**: typing.Optional[bool]


# SuiteRunInformationTypeDef

### suiteDefinitionId
- **Type**: typing.Optional[str]

### suiteDefinitionVersion
- **Type**: typing.Optional[str]

### suiteDefinitionName
- **Type**: typing.Optional[str]

### suiteRunId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'ERROR', 'FAIL', 'PASS', 'PASS_WITH_WARNINGS', 'PENDING', 'RUNNING', 'STOPPED', 'STOPPING']]

### passed
- **Type**: typing.Optional[int]

### failed
- **Type**: typing.Optional[int]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TestCaseRunTypeDef

### testCaseRunId
- **Type**: typing.Optional[str]

### testCaseDefinitionId
- **Type**: typing.Optional[str]

### testCaseDefinitionName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'ERROR', 'FAIL', 'PASS', 'PASS_WITH_WARNINGS', 'PENDING', 'RUNNING', 'STOPPED', 'STOPPING']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### logUrl
- **Type**: typing.Optional[str]

### warnings
- **Type**: typing.Optional[str]

### failure
- **Type**: typing.Optional[str]

### testScenarios
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.TestCaseScenarioTypeDef]]


# TestCaseScenarioTypeDef

### testCaseScenarioId
- **Type**: typing.Optional[str]

### testCaseScenarioType
- **Type**: typing.Optional[typing.Literal['Advanced', 'Basic']]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'ERROR', 'FAIL', 'PASS', 'PASS_WITH_WARNINGS', 'PENDING', 'RUNNING', 'STOPPED', 'STOPPING']]

### failure
- **Type**: typing.Optional[str]

### systemMessage
- **Type**: typing.Optional[str]


# TestResultTypeDef

### groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.GroupResultTypeDef]]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateSuiteDefinitionRequestRequestTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteDefinitionConfigurationTypeDef'>
- **Required**: Yes


# UpdateSuiteDefinitionResponseTypeDef

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionVersion
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



# Iotdeviceadvisor Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateSuiteDefinitionRequest

### suiteDefinitionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteDefinitionConfigurationUnion'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateSuiteDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSuiteDefinitionRequest

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeviceUnderTest

### thingArn
- **Type**: typing.Optional[str]

### certificateArn
- **Type**: typing.Optional[str]

### deviceRoleArn
- **Type**: typing.Optional[str]


# GetEndpointRequest

### thingArn
- **Type**: typing.Optional[str]

### certificateArn
- **Type**: typing.Optional[str]

### deviceRoleArn
- **Type**: typing.Optional[str]

### authenticationMethod
- **Type**: typing.Optional[typing.Literal['SignatureVersion4', 'X509ClientCertificate']]


# GetEndpointResponse

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# GetSuiteDefinitionRequest

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionVersion
- **Type**: typing.Optional[str]


# GetSuiteDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteDefinitionConfigurationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# GetSuiteRunReportRequest

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSuiteRunReportResponse

### qualificationReportDownloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# GetSuiteRunRequest

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSuiteRunResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteRunConfigurationOutput'>
- **Required**: Yes

### testResult
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.TestResult'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# GroupResult

### groupId
- **Type**: typing.Optional[str]

### groupName
- **Type**: typing.Optional[str]

### tests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.TestCaseRun]]


# ListSuiteDefinitionsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSuiteDefinitionsResponse

### suiteDefinitionInformationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteDefinitionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSuiteRunsRequest

### suiteDefinitionId
- **Type**: typing.Optional[str]

### suiteDefinitionVersion
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSuiteRunsResponse

### suiteRunsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteRunInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes


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


# StartSuiteRunRequest

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteRunConfigurationUnion'>
- **Required**: Yes

### suiteDefinitionVersion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartSuiteRunResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# StopSuiteRunRequest

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteRunId
- **Type**: <class 'str'>
- **Required**: Yes


# SuiteDefinitionConfiguration

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.DeviceUnderTest]]

### intendedForQualification
- **Type**: typing.Optional[bool]

### isLongDurationTest
- **Type**: typing.Optional[bool]

### protocol
- **Type**: typing.Optional[typing.Literal['MqttV3_1_1', 'MqttV3_1_1_OverWebSocket', 'MqttV5', 'MqttV5_OverWebSocket']]


# SuiteDefinitionConfigurationOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.DeviceUnderTest]]

### intendedForQualification
- **Type**: typing.Optional[bool]

### isLongDurationTest
- **Type**: typing.Optional[bool]

### protocol
- **Type**: typing.Optional[typing.Literal['MqttV3_1_1', 'MqttV3_1_1_OverWebSocket', 'MqttV5', 'MqttV5_OverWebSocket']]


# SuiteDefinitionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SuiteDefinitionInformation

### suiteDefinitionId
- **Type**: typing.Optional[str]

### suiteDefinitionName
- **Type**: typing.Optional[str]

### defaultDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.DeviceUnderTest]]

### intendedForQualification
- **Type**: typing.Optional[bool]

### isLongDurationTest
- **Type**: typing.Optional[bool]

### protocol
- **Type**: typing.Optional[typing.Literal['MqttV3_1_1', 'MqttV3_1_1_OverWebSocket', 'MqttV5', 'MqttV5_OverWebSocket']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# SuiteRunConfiguration

### primaryDevice
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.DeviceUnderTest'>
- **Required**: Yes

### selectedTestList
- **Type**: typing.Optional[typing.Sequence[str]]

### parallelRun
- **Type**: typing.Optional[bool]


# SuiteRunConfigurationOutput

### primaryDevice
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.DeviceUnderTest'>
- **Required**: Yes

### selectedTestList
- **Type**: typing.Optional[typing.List[str]]

### parallelRun
- **Type**: typing.Optional[bool]


# SuiteRunConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SuiteRunInformation

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


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TestCaseRun

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.TestCaseScenario]]


# TestCaseScenario

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


# TestResult

### groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.GroupResult]]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateSuiteDefinitionRequest

### suiteDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### suiteDefinitionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.SuiteDefinitionConfigurationUnion'>
- **Required**: Yes


# UpdateSuiteDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotdeviceadvisor_classes.ResponseMetadata'>
- **Required**: Yes



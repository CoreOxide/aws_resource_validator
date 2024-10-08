# Pydantic Models in devicefarm_classes

# AccountSettingsTypeDef

### awsAccountNumber
- **Type**: typing.Optional[str]

### unmeteredDevices
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANDROID', 'IOS'], int]]

### unmeteredRemoteAccessDevices
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANDROID', 'IOS'], int]]

### maxJobTimeoutMinutes
- **Type**: typing.Optional[int]

### trialMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TrialMinutesTypeDef]

### maxSlots
- **Type**: typing.Optional[typing.Dict[str, int]]

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### skipAppResign
- **Type**: typing.Optional[bool]


# ArtifactTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_OUTPUT', 'APPIUM_JAVA_XML_OUTPUT', 'APPIUM_PYTHON_OUTPUT', 'APPIUM_PYTHON_XML_OUTPUT', 'APPIUM_SERVER_OUTPUT', 'APPLICATION_CRASH_REPORT', 'AUTOMATION_OUTPUT', 'CALABASH_JAVA_XML_OUTPUT', 'CALABASH_JSON_OUTPUT', 'CALABASH_PRETTY_OUTPUT', 'CALABASH_STANDARD_OUTPUT', 'CUSTOMER_ARTIFACT', 'CUSTOMER_ARTIFACT_LOG', 'DEVICE_LOG', 'EXERCISER_MONKEY_OUTPUT', 'EXPLORER_EVENT_LOG', 'EXPLORER_SUMMARY_LOG', 'INSTRUMENTATION_OUTPUT', 'MESSAGE_LOG', 'RESULT_LOG', 'SCREENSHOT', 'SERVICE_LOG', 'TESTSPEC_OUTPUT', 'UNKNOWN', 'VIDEO', 'VIDEO_LOG', 'WEBKIT_LOG', 'XCTEST_LOG']]

### extension
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CPUTypeDef

### frequency
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[str]

### clock
- **Type**: typing.Optional[float]


# CountersTypeDef

### total
- **Type**: typing.Optional[int]

### passed
- **Type**: typing.Optional[int]

### failed
- **Type**: typing.Optional[int]

### warned
- **Type**: typing.Optional[int]

### errored
- **Type**: typing.Optional[int]

### stopped
- **Type**: typing.Optional[int]

### skipped
- **Type**: typing.Optional[int]


# CreateDevicePoolRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.RuleTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### maxDevices
- **Type**: typing.Optional[int]


# CreateDevicePoolResultTypeDef

### devicePool
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DevicePoolTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstanceProfileRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### packageCleanup
- **Type**: typing.Optional[bool]

### excludeAppPackagesFromCleanup
- **Type**: typing.Optional[typing.Sequence[str]]

### rebootAfterUse
- **Type**: typing.Optional[bool]


# CreateInstanceProfileResultTypeDef

### instanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNetworkProfileRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### uplinkBandwidthBits
- **Type**: typing.Optional[int]

### downlinkBandwidthBits
- **Type**: typing.Optional[int]

### uplinkDelayMs
- **Type**: typing.Optional[int]

### downlinkDelayMs
- **Type**: typing.Optional[int]

### uplinkJitterMs
- **Type**: typing.Optional[int]

### downlinkJitterMs
- **Type**: typing.Optional[int]

### uplinkLossPercent
- **Type**: typing.Optional[int]

### downlinkLossPercent
- **Type**: typing.Optional[int]


# CreateNetworkProfileResultTypeDef

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigTypeDef]


# CreateProjectResultTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRemoteAccessSessionConfigurationTypeDef

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]

### vpceConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateRemoteAccessSessionRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### deviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### instanceArn
- **Type**: typing.Optional[str]

### sshPublicKey
- **Type**: typing.Optional[str]

### remoteDebugEnabled
- **Type**: typing.Optional[bool]

### remoteRecordEnabled
- **Type**: typing.Optional[bool]

### remoteRecordAppArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### clientId
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CreateRemoteAccessSessionConfigurationTypeDef]

### interactionMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'NO_VIDEO', 'VIDEO_ONLY']]

### skipAppResign
- **Type**: typing.Optional[bool]


# CreateRemoteAccessSessionResultTypeDef

### remoteAccessSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.RemoteAccessSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTestGridProjectRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridVpcConfigTypeDef]


# CreateTestGridProjectResultTypeDef

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTestGridUrlRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### expiresInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# CreateTestGridUrlResultTypeDef

### url
- **Type**: <class 'str'>
- **Required**: Yes

### expires
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUploadRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ANDROID_APP', 'APPIUM_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_JAVA_JUNIT_TEST_SPEC', 'APPIUM_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_JAVA_TESTNG_TEST_SPEC', 'APPIUM_NODE_TEST_PACKAGE', 'APPIUM_NODE_TEST_SPEC', 'APPIUM_PYTHON_TEST_PACKAGE', 'APPIUM_PYTHON_TEST_SPEC', 'APPIUM_RUBY_TEST_PACKAGE', 'APPIUM_RUBY_TEST_SPEC', 'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC', 'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC', 'APPIUM_WEB_NODE_TEST_PACKAGE', 'APPIUM_WEB_NODE_TEST_SPEC', 'APPIUM_WEB_PYTHON_TEST_PACKAGE', 'APPIUM_WEB_PYTHON_TEST_SPEC', 'APPIUM_WEB_RUBY_TEST_PACKAGE', 'APPIUM_WEB_RUBY_TEST_SPEC', 'CALABASH_TEST_PACKAGE', 'EXTERNAL_DATA', 'INSTRUMENTATION_TEST_PACKAGE', 'INSTRUMENTATION_TEST_SPEC', 'IOS_APP', 'UIAUTOMATION_TEST_PACKAGE', 'UIAUTOMATOR_TEST_PACKAGE', 'WEB_APP', 'XCTEST_TEST_PACKAGE', 'XCTEST_UI_TEST_PACKAGE', 'XCTEST_UI_TEST_SPEC']
- **Required**: Yes

### contentType
- **Type**: typing.Optional[str]


# CreateUploadResultTypeDef

### upload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.UploadTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVPCEConfigurationRequestRequestTypeDef

### vpceConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### vpceServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceDnsName
- **Type**: <class 'str'>
- **Required**: Yes

### vpceConfigurationDescription
- **Type**: typing.Optional[str]


# CreateVPCEConfigurationResultTypeDef

### vpceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.VPCEConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerArtifactPathsOutputTypeDef

### iosPaths
- **Type**: typing.Optional[typing.List[str]]

### androidPaths
- **Type**: typing.Optional[typing.List[str]]

### deviceHostPaths
- **Type**: typing.Optional[typing.List[str]]


# CustomerArtifactPathsTypeDef

### iosPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### androidPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### deviceHostPaths
- **Type**: typing.Optional[typing.Sequence[str]]


# DeleteDevicePoolRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceProfileRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkProfileRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRemoteAccessSessionRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRunRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTestGridProjectRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUploadRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVPCEConfigurationRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeviceFilterExtraOutputTypeDef

### attribute
- **Type**: typing.Literal['ARN', 'AVAILABILITY', 'FLEET_TYPE', 'FORM_FACTOR', 'INSTANCE_ARN', 'INSTANCE_LABELS', 'MANUFACTURER', 'MODEL', 'OS_VERSION', 'PLATFORM', 'REMOTE_ACCESS_ENABLED', 'REMOTE_DEBUG_ENABLED']
- **Required**: Yes

### operator
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'IN', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_IN']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# DeviceFilterOutputTypeDef

### attribute
- **Type**: typing.Literal['ARN', 'AVAILABILITY', 'FLEET_TYPE', 'FORM_FACTOR', 'INSTANCE_ARN', 'INSTANCE_LABELS', 'MANUFACTURER', 'MODEL', 'OS_VERSION', 'PLATFORM', 'REMOTE_ACCESS_ENABLED', 'REMOTE_DEBUG_ENABLED']
- **Required**: Yes

### operator
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'IN', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_IN']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# DeviceFilterTypeDef

### attribute
- **Type**: typing.Literal['ARN', 'AVAILABILITY', 'FLEET_TYPE', 'FORM_FACTOR', 'INSTANCE_ARN', 'INSTANCE_LABELS', 'MANUFACTURER', 'MODEL', 'OS_VERSION', 'PLATFORM', 'REMOTE_ACCESS_ENABLED', 'REMOTE_DEBUG_ENABLED']
- **Required**: Yes

### operator
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'IN', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_IN']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeviceInstanceTypeDef

### arn
- **Type**: typing.Optional[str]

### deviceArn
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'IN_USE', 'NOT_AVAILABLE', 'PREPARING']]

### udid
- **Type**: typing.Optional[str]

### instanceProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfileTypeDef]


# DeviceMinutesTypeDef

### total
- **Type**: typing.Optional[float]

### metered
- **Type**: typing.Optional[float]

### unmetered
- **Type**: typing.Optional[float]


# DevicePoolCompatibilityResultTypeDef

### device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceTypeDef]

### compatible
- **Type**: typing.Optional[bool]

### incompatibilityMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.IncompatibilityMessageTypeDef]]


# DevicePoolTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.RuleTypeDef]]

### maxDevices
- **Type**: typing.Optional[int]


# DeviceSelectionConfigurationTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterTypeDef]
- **Required**: Yes

### maxDevices
- **Type**: <class 'int'>
- **Required**: Yes


# DeviceSelectionResultTypeDef

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterOutputTypeDef]]

### matchedDevicesCount
- **Type**: typing.Optional[int]

### maxDevices
- **Type**: typing.Optional[int]


# DeviceTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### manufacturer
- **Type**: typing.Optional[str]

### model
- **Type**: typing.Optional[str]

### modelId
- **Type**: typing.Optional[str]

### formFactor
- **Type**: typing.Optional[typing.Literal['PHONE', 'TABLET']]

### platform
- **Type**: typing.Optional[typing.Literal['ANDROID', 'IOS']]

### os
- **Type**: typing.Optional[str]

### cpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CPUTypeDef]

### resolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ResolutionTypeDef]

### heapSize
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### image
- **Type**: typing.Optional[str]

### carrier
- **Type**: typing.Optional[str]

### radio
- **Type**: typing.Optional[str]

### remoteAccessEnabled
- **Type**: typing.Optional[bool]

### remoteDebugEnabled
- **Type**: typing.Optional[bool]

### fleetType
- **Type**: typing.Optional[str]

### fleetName
- **Type**: typing.Optional[str]

### instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceInstanceTypeDef]]

### availability
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'BUSY', 'HIGHLY_AVAILABLE', 'TEMPORARY_NOT_AVAILABLE']]


# ExecutionConfigurationTypeDef

### jobTimeoutMinutes
- **Type**: typing.Optional[int]

### accountsCleanup
- **Type**: typing.Optional[bool]

### appPackagesCleanup
- **Type**: typing.Optional[bool]

### videoCapture
- **Type**: typing.Optional[bool]

### skipAppResign
- **Type**: typing.Optional[bool]


# GetAccountSettingsResultTypeDef

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeviceInstanceRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceInstanceResultTypeDef

### deviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DeviceInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDevicePoolCompatibilityRequestRequestTypeDef

### devicePoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: typing.Optional[str]

### testType
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_EXPLORER', 'BUILTIN_FUZZ', 'CALABASH', 'INSTRUMENTATION', 'REMOTE_ACCESS_RECORD', 'REMOTE_ACCESS_REPLAY', 'UIAUTOMATION', 'UIAUTOMATOR', 'WEB_PERFORMANCE_PROFILE', 'XCTEST', 'XCTEST_UI']]

### test
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ScheduleRunTestTypeDef]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ScheduleRunConfigurationTypeDef]


# GetDevicePoolCompatibilityResultTypeDef

### compatibleDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DevicePoolCompatibilityResultTypeDef]
- **Required**: Yes

### incompatibleDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DevicePoolCompatibilityResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDevicePoolRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevicePoolResultTypeDef

### devicePool
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DevicePoolTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeviceRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceResultTypeDef

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DeviceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceProfileRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceProfileResultTypeDef

### instanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResultTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNetworkProfileRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkProfileResultTypeDef

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOfferingStatusRequestGetOfferingStatusPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# GetOfferingStatusRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# GetOfferingStatusResultTypeDef

### current
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.devicefarm_classes.OfferingStatusTypeDef]
- **Required**: Yes

### nextPeriod
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.devicefarm_classes.OfferingStatusTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProjectRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectResultTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRemoteAccessSessionRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRemoteAccessSessionResultTypeDef

### remoteAccessSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.RemoteAccessSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRunRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRunResultTypeDef

### run
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.RunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSuiteRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSuiteResultTypeDef

### suite
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.SuiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTestGridProjectRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTestGridProjectResultTypeDef

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTestGridSessionRequestRequestTypeDef

### projectArn
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### sessionArn
- **Type**: typing.Optional[str]


# GetTestGridSessionResultTypeDef

### testGridSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTestRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTestResultTypeDef

### test
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUploadRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetUploadResultTypeDef

### upload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.UploadTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVPCEConfigurationRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetVPCEConfigurationResultTypeDef

### vpceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.VPCEConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IncompatibilityMessageTypeDef

### message
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_VERSION', 'ARN', 'AVAILABILITY', 'FLEET_TYPE', 'FORM_FACTOR', 'INSTANCE_ARN', 'INSTANCE_LABELS', 'MANUFACTURER', 'MODEL', 'OS_VERSION', 'PLATFORM', 'REMOTE_ACCESS_ENABLED', 'REMOTE_DEBUG_ENABLED']]


# InstallToRemoteAccessSessionRequestRequestTypeDef

### remoteAccessSessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes


# InstallToRemoteAccessSessionResultTypeDef

### appUpload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.UploadTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceProfileTypeDef

### arn
- **Type**: typing.Optional[str]

### packageCleanup
- **Type**: typing.Optional[bool]

### excludeAppPackagesFromCleanup
- **Type**: typing.Optional[typing.List[str]]

### rebootAfterUse
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# JobTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_EXPLORER', 'BUILTIN_FUZZ', 'CALABASH', 'INSTRUMENTATION', 'REMOTE_ACCESS_RECORD', 'REMOTE_ACCESS_REPLAY', 'UIAUTOMATION', 'UIAUTOMATOR', 'WEB_PERFORMANCE_PROFILE', 'XCTEST', 'XCTEST_UI']]

### created
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'PENDING', 'PENDING_CONCURRENCY', 'PENDING_DEVICE', 'PREPARING', 'PROCESSING', 'RUNNING', 'SCHEDULING', 'STOPPING']]

### result
- **Type**: typing.Optional[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED']]

### started
- **Type**: typing.Optional[datetime.datetime]

### stopped
- **Type**: typing.Optional[datetime.datetime]

### counters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CountersTypeDef]

### message
- **Type**: typing.Optional[str]

### device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceTypeDef]

### instanceArn
- **Type**: typing.Optional[str]

### deviceMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceMinutesTypeDef]

### videoEndpoint
- **Type**: typing.Optional[str]

### videoCapture
- **Type**: typing.Optional[bool]


# ListArtifactsRequestListArtifactsPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['FILE', 'LOG', 'SCREENSHOT']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListArtifactsRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['FILE', 'LOG', 'SCREENSHOT']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListArtifactsResultTypeDef

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.ArtifactTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeviceInstancesRequestListDeviceInstancesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListDeviceInstancesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeviceInstancesResultTypeDef

### deviceInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceInstanceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDevicePoolsRequestListDevicePoolsPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListDevicePoolsRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### nextToken
- **Type**: typing.Optional[str]


# ListDevicePoolsResultTypeDef

### devicePools
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DevicePoolTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDevicesRequestListDevicesPaginateTypeDef

### arn
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterTypeDef, aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterExtraOutputTypeDef]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListDevicesRequestRequestTypeDef

### arn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterTypeDef, aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterExtraOutputTypeDef]]]


# ListDevicesResultTypeDef

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListInstanceProfilesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInstanceProfilesResultTypeDef

### instanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfileTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsRequestListJobsPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListJobsRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsResultTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.JobTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNetworkProfilesRequestListNetworkProfilesPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListNetworkProfilesRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkProfilesResultTypeDef

### networkProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfileTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOfferingPromotionsRequestListOfferingPromotionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListOfferingPromotionsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingPromotionsResultTypeDef

### offeringPromotions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingPromotionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOfferingTransactionsRequestListOfferingTransactionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListOfferingTransactionsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingTransactionsResultTypeDef

### offeringTransactions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTransactionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOfferingsRequestListOfferingsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListOfferingsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingsResultTypeDef

### offerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsRequestListProjectsPaginateTypeDef

### arn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListProjectsRequestRequestTypeDef

### arn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsResultTypeDef

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.ProjectTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListRemoteAccessSessionsRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRemoteAccessSessionsResultTypeDef

### remoteAccessSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.RemoteAccessSessionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRunsRequestListRunsPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListRunsRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunsResultTypeDef

### runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.RunTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSamplesRequestListSamplesPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListSamplesRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSamplesResultTypeDef

### samples
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.SampleTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSuitesRequestListSuitesPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListSuitesRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSuitesResultTypeDef

### suites
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.SuiteTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestGridProjectsRequestRequestTypeDef

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridProjectsResultTypeDef

### testGridProjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProjectTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestGridSessionActionsRequestRequestTypeDef

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionActionsResultTypeDef

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSessionActionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestGridSessionArtifactsRequestRequestTypeDef

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['LOG', 'VIDEO']]

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionArtifactsResultTypeDef

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSessionArtifactTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestGridSessionsRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CLOSED', 'ERRORED']]

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionsResultTypeDef

### testGridSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSessionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTestsRequestListTestsPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListTestsRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestsResultTypeDef

### tests
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUniqueProblemsRequestListUniqueProblemsPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListUniqueProblemsRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUniqueProblemsResultTypeDef

### uniqueProblems
- **Type**: typing.Dict[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED'], typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.UniqueProblemTypeDef]]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUploadsRequestListUploadsPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['ANDROID_APP', 'APPIUM_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_JAVA_JUNIT_TEST_SPEC', 'APPIUM_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_JAVA_TESTNG_TEST_SPEC', 'APPIUM_NODE_TEST_PACKAGE', 'APPIUM_NODE_TEST_SPEC', 'APPIUM_PYTHON_TEST_PACKAGE', 'APPIUM_PYTHON_TEST_SPEC', 'APPIUM_RUBY_TEST_PACKAGE', 'APPIUM_RUBY_TEST_SPEC', 'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC', 'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC', 'APPIUM_WEB_NODE_TEST_PACKAGE', 'APPIUM_WEB_NODE_TEST_SPEC', 'APPIUM_WEB_PYTHON_TEST_PACKAGE', 'APPIUM_WEB_PYTHON_TEST_SPEC', 'APPIUM_WEB_RUBY_TEST_PACKAGE', 'APPIUM_WEB_RUBY_TEST_SPEC', 'CALABASH_TEST_PACKAGE', 'EXTERNAL_DATA', 'INSTRUMENTATION_TEST_PACKAGE', 'INSTRUMENTATION_TEST_SPEC', 'IOS_APP', 'UIAUTOMATION_TEST_PACKAGE', 'UIAUTOMATOR_TEST_PACKAGE', 'WEB_APP', 'XCTEST_TEST_PACKAGE', 'XCTEST_UI_TEST_PACKAGE', 'XCTEST_UI_TEST_SPEC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListUploadsRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['ANDROID_APP', 'APPIUM_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_JAVA_JUNIT_TEST_SPEC', 'APPIUM_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_JAVA_TESTNG_TEST_SPEC', 'APPIUM_NODE_TEST_PACKAGE', 'APPIUM_NODE_TEST_SPEC', 'APPIUM_PYTHON_TEST_PACKAGE', 'APPIUM_PYTHON_TEST_SPEC', 'APPIUM_RUBY_TEST_PACKAGE', 'APPIUM_RUBY_TEST_SPEC', 'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC', 'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC', 'APPIUM_WEB_NODE_TEST_PACKAGE', 'APPIUM_WEB_NODE_TEST_SPEC', 'APPIUM_WEB_PYTHON_TEST_PACKAGE', 'APPIUM_WEB_PYTHON_TEST_SPEC', 'APPIUM_WEB_RUBY_TEST_PACKAGE', 'APPIUM_WEB_RUBY_TEST_SPEC', 'CALABASH_TEST_PACKAGE', 'EXTERNAL_DATA', 'INSTRUMENTATION_TEST_PACKAGE', 'INSTRUMENTATION_TEST_SPEC', 'IOS_APP', 'UIAUTOMATION_TEST_PACKAGE', 'UIAUTOMATOR_TEST_PACKAGE', 'WEB_APP', 'XCTEST_TEST_PACKAGE', 'XCTEST_UI_TEST_PACKAGE', 'XCTEST_UI_TEST_SPEC']]

### nextToken
- **Type**: typing.Optional[str]


# ListUploadsResultTypeDef

### uploads
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.UploadTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListVPCEConfigurationsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListVPCEConfigurationsResultTypeDef

### vpceConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.VPCEConfigurationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LocationTypeDef

### latitude
- **Type**: <class 'float'>
- **Required**: Yes

### longitude
- **Type**: <class 'float'>
- **Required**: Yes


# MonetaryAmountTypeDef

### amount
- **Type**: typing.Optional[float]

### currencyCode
- **Type**: typing.Optional[typing.Literal['USD']]


# NetworkProfileTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### uplinkBandwidthBits
- **Type**: typing.Optional[int]

### downlinkBandwidthBits
- **Type**: typing.Optional[int]

### uplinkDelayMs
- **Type**: typing.Optional[int]

### downlinkDelayMs
- **Type**: typing.Optional[int]

### uplinkJitterMs
- **Type**: typing.Optional[int]

### downlinkJitterMs
- **Type**: typing.Optional[int]

### uplinkLossPercent
- **Type**: typing.Optional[int]

### downlinkLossPercent
- **Type**: typing.Optional[int]


# OfferingPromotionTypeDef

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# OfferingStatusTypeDef

### type
- **Type**: typing.Optional[typing.Literal['PURCHASE', 'RENEW', 'SYSTEM']]

### offering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTypeDef]

### quantity
- **Type**: typing.Optional[int]

### effectiveOn
- **Type**: typing.Optional[datetime.datetime]


# OfferingTransactionTypeDef

### offeringStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingStatusTypeDef]

### transactionId
- **Type**: typing.Optional[str]

### offeringPromotionId
- **Type**: typing.Optional[str]

### createdOn
- **Type**: typing.Optional[datetime.datetime]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.MonetaryAmountTypeDef]


# OfferingTypeDef

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['RECURRING']]

### platform
- **Type**: typing.Optional[typing.Literal['ANDROID', 'IOS']]

### recurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.RecurringChargeTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProblemDetailTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# ProblemTypeDef

### run
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ProblemDetailTypeDef]

### job
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ProblemDetailTypeDef]

### suite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ProblemDetailTypeDef]

### test
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ProblemDetailTypeDef]

### device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceTypeDef]

### result
- **Type**: typing.Optional[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED']]

### message
- **Type**: typing.Optional[str]


# ProjectTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### created
- **Type**: typing.Optional[datetime.datetime]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigOutputTypeDef]


# PurchaseOfferingRequestRequestTypeDef

### offeringId
- **Type**: <class 'str'>
- **Required**: Yes

### quantity
- **Type**: <class 'int'>
- **Required**: Yes

### offeringPromotionId
- **Type**: typing.Optional[str]


# PurchaseOfferingResultTypeDef

### offeringTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTransactionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RadiosTypeDef

### wifi
- **Type**: typing.Optional[bool]

### bluetooth
- **Type**: typing.Optional[bool]

### nfc
- **Type**: typing.Optional[bool]

### gps
- **Type**: typing.Optional[bool]


# RecurringChargeTypeDef

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.MonetaryAmountTypeDef]

### frequency
- **Type**: typing.Optional[typing.Literal['MONTHLY']]


# RemoteAccessSessionTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### created
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'PENDING', 'PENDING_CONCURRENCY', 'PENDING_DEVICE', 'PREPARING', 'PROCESSING', 'RUNNING', 'SCHEDULING', 'STOPPING']]

### result
- **Type**: typing.Optional[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED']]

### message
- **Type**: typing.Optional[str]

### started
- **Type**: typing.Optional[datetime.datetime]

### stopped
- **Type**: typing.Optional[datetime.datetime]

### device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceTypeDef]

### instanceArn
- **Type**: typing.Optional[str]

### remoteDebugEnabled
- **Type**: typing.Optional[bool]

### remoteRecordEnabled
- **Type**: typing.Optional[bool]

### remoteRecordAppArn
- **Type**: typing.Optional[str]

### hostAddress
- **Type**: typing.Optional[str]

### clientId
- **Type**: typing.Optional[str]

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]

### deviceMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceMinutesTypeDef]

### endpoint
- **Type**: typing.Optional[str]

### deviceUdid
- **Type**: typing.Optional[str]

### interactionMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'NO_VIDEO', 'VIDEO_ONLY']]

### skipAppResign
- **Type**: typing.Optional[bool]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigOutputTypeDef]


# RenewOfferingRequestRequestTypeDef

### offeringId
- **Type**: <class 'str'>
- **Required**: Yes

### quantity
- **Type**: <class 'int'>
- **Required**: Yes


# RenewOfferingResultTypeDef

### offeringTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTransactionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResolutionTypeDef

### width
- **Type**: typing.Optional[int]

### height
- **Type**: typing.Optional[int]


# ResponseMetadataTypeDef

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


# RuleTypeDef

### attribute
- **Type**: typing.Optional[typing.Literal['APPIUM_VERSION', 'ARN', 'AVAILABILITY', 'FLEET_TYPE', 'FORM_FACTOR', 'INSTANCE_ARN', 'INSTANCE_LABELS', 'MANUFACTURER', 'MODEL', 'OS_VERSION', 'PLATFORM', 'REMOTE_ACCESS_ENABLED', 'REMOTE_DEBUG_ENABLED']]

### operator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'IN', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_IN']]

### value
- **Type**: typing.Optional[str]


# RunTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_EXPLORER', 'BUILTIN_FUZZ', 'CALABASH', 'INSTRUMENTATION', 'REMOTE_ACCESS_RECORD', 'REMOTE_ACCESS_REPLAY', 'UIAUTOMATION', 'UIAUTOMATOR', 'WEB_PERFORMANCE_PROFILE', 'XCTEST', 'XCTEST_UI']]

### platform
- **Type**: typing.Optional[typing.Literal['ANDROID', 'IOS']]

### created
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'PENDING', 'PENDING_CONCURRENCY', 'PENDING_DEVICE', 'PREPARING', 'PROCESSING', 'RUNNING', 'SCHEDULING', 'STOPPING']]

### result
- **Type**: typing.Optional[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED']]

### started
- **Type**: typing.Optional[datetime.datetime]

### stopped
- **Type**: typing.Optional[datetime.datetime]

### counters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CountersTypeDef]

### message
- **Type**: typing.Optional[str]

### totalJobs
- **Type**: typing.Optional[int]

### completedJobs
- **Type**: typing.Optional[int]

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]

### deviceMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceMinutesTypeDef]

### networkProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfileTypeDef]

### parsingResultUrl
- **Type**: typing.Optional[str]

### resultCode
- **Type**: typing.Optional[typing.Literal['PARSING_FAILED', 'VPC_ENDPOINT_SETUP_FAILED']]

### seed
- **Type**: typing.Optional[int]

### appUpload
- **Type**: typing.Optional[str]

### eventCount
- **Type**: typing.Optional[int]

### jobTimeoutMinutes
- **Type**: typing.Optional[int]

### devicePoolArn
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]

### radios
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.RadiosTypeDef]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.LocationTypeDef]

### customerArtifactPaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CustomerArtifactPathsOutputTypeDef]

### webUrl
- **Type**: typing.Optional[str]

### skipAppResign
- **Type**: typing.Optional[bool]

### testSpecArn
- **Type**: typing.Optional[str]

### deviceSelectionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceSelectionResultTypeDef]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigOutputTypeDef]


# SampleTypeDef

### arn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CPU', 'MEMORY', 'NATIVE_AVG_DRAWTIME', 'NATIVE_FPS', 'NATIVE_FRAMES', 'NATIVE_MAX_DRAWTIME', 'NATIVE_MIN_DRAWTIME', 'OPENGL_AVG_DRAWTIME', 'OPENGL_FPS', 'OPENGL_FRAMES', 'OPENGL_MAX_DRAWTIME', 'OPENGL_MIN_DRAWTIME', 'RX', 'RX_RATE', 'THREADS', 'TX', 'TX_RATE']]

### url
- **Type**: typing.Optional[str]


# ScheduleRunConfigurationTypeDef

### extraDataPackageArn
- **Type**: typing.Optional[str]

### networkProfileArn
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.LocationTypeDef]

### vpceConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### customerArtifactPaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CustomerArtifactPathsTypeDef]

### radios
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.RadiosTypeDef]

### auxiliaryApps
- **Type**: typing.Optional[typing.Sequence[str]]

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]


# ScheduleRunRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### test
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ScheduleRunTestTypeDef'>
- **Required**: Yes

### appArn
- **Type**: typing.Optional[str]

### devicePoolArn
- **Type**: typing.Optional[str]

### deviceSelectionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceSelectionConfigurationTypeDef]

### name
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ScheduleRunConfigurationTypeDef]

### executionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ExecutionConfigurationTypeDef]


# ScheduleRunResultTypeDef

### run
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.RunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ScheduleRunTestTypeDef

### type
- **Type**: typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_EXPLORER', 'BUILTIN_FUZZ', 'CALABASH', 'INSTRUMENTATION', 'REMOTE_ACCESS_RECORD', 'REMOTE_ACCESS_REPLAY', 'UIAUTOMATION', 'UIAUTOMATOR', 'WEB_PERFORMANCE_PROFILE', 'XCTEST', 'XCTEST_UI']
- **Required**: Yes

### testPackageArn
- **Type**: typing.Optional[str]

### testSpecArn
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StopJobRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopJobResultTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopRemoteAccessSessionRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopRemoteAccessSessionResultTypeDef

### remoteAccessSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.RemoteAccessSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopRunRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopRunResultTypeDef

### run
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.RunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SuiteTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_EXPLORER', 'BUILTIN_FUZZ', 'CALABASH', 'INSTRUMENTATION', 'REMOTE_ACCESS_RECORD', 'REMOTE_ACCESS_REPLAY', 'UIAUTOMATION', 'UIAUTOMATOR', 'WEB_PERFORMANCE_PROFILE', 'XCTEST', 'XCTEST_UI']]

### created
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'PENDING', 'PENDING_CONCURRENCY', 'PENDING_DEVICE', 'PREPARING', 'PROCESSING', 'RUNNING', 'SCHEDULING', 'STOPPING']]

### result
- **Type**: typing.Optional[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED']]

### started
- **Type**: typing.Optional[datetime.datetime]

### stopped
- **Type**: typing.Optional[datetime.datetime]

### counters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CountersTypeDef]

### message
- **Type**: typing.Optional[str]

### deviceMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceMinutesTypeDef]


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TestGridProjectTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridVpcConfigOutputTypeDef]

### created
- **Type**: typing.Optional[datetime.datetime]


# TestGridSessionActionTypeDef

### action
- **Type**: typing.Optional[str]

### started
- **Type**: typing.Optional[datetime.datetime]

### duration
- **Type**: typing.Optional[int]

### statusCode
- **Type**: typing.Optional[str]

### requestMethod
- **Type**: typing.Optional[str]


# TestGridSessionArtifactTypeDef

### filename
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['SELENIUM_LOG', 'UNKNOWN', 'VIDEO']]

### url
- **Type**: typing.Optional[str]


# TestGridSessionTypeDef

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CLOSED', 'ERRORED']]

### created
- **Type**: typing.Optional[datetime.datetime]

### ended
- **Type**: typing.Optional[datetime.datetime]

### billingMinutes
- **Type**: typing.Optional[float]

### seleniumProperties
- **Type**: typing.Optional[str]


# TestGridVpcConfigOutputTypeDef

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# TestGridVpcConfigTypeDef

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# TestTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_EXPLORER', 'BUILTIN_FUZZ', 'CALABASH', 'INSTRUMENTATION', 'REMOTE_ACCESS_RECORD', 'REMOTE_ACCESS_REPLAY', 'UIAUTOMATION', 'UIAUTOMATOR', 'WEB_PERFORMANCE_PROFILE', 'XCTEST', 'XCTEST_UI']]

### created
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'PENDING', 'PENDING_CONCURRENCY', 'PENDING_DEVICE', 'PREPARING', 'PROCESSING', 'RUNNING', 'SCHEDULING', 'STOPPING']]

### result
- **Type**: typing.Optional[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED']]

### started
- **Type**: typing.Optional[datetime.datetime]

### stopped
- **Type**: typing.Optional[datetime.datetime]

### counters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CountersTypeDef]

### message
- **Type**: typing.Optional[str]

### deviceMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceMinutesTypeDef]


# TrialMinutesTypeDef

### total
- **Type**: typing.Optional[float]

### remaining
- **Type**: typing.Optional[float]


# UniqueProblemTypeDef

### message
- **Type**: typing.Optional[str]

### problems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.ProblemTypeDef]]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeviceInstanceRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### profileArn
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateDeviceInstanceResultTypeDef

### deviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DeviceInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDevicePoolRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.RuleTypeDef]]

### maxDevices
- **Type**: typing.Optional[int]

### clearMaxDevices
- **Type**: typing.Optional[bool]


# UpdateDevicePoolResultTypeDef

### devicePool
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DevicePoolTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInstanceProfileRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### packageCleanup
- **Type**: typing.Optional[bool]

### excludeAppPackagesFromCleanup
- **Type**: typing.Optional[typing.Sequence[str]]

### rebootAfterUse
- **Type**: typing.Optional[bool]


# UpdateInstanceProfileResultTypeDef

### instanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNetworkProfileRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### uplinkBandwidthBits
- **Type**: typing.Optional[int]

### downlinkBandwidthBits
- **Type**: typing.Optional[int]

### uplinkDelayMs
- **Type**: typing.Optional[int]

### downlinkDelayMs
- **Type**: typing.Optional[int]

### uplinkJitterMs
- **Type**: typing.Optional[int]

### downlinkJitterMs
- **Type**: typing.Optional[int]

### uplinkLossPercent
- **Type**: typing.Optional[int]

### downlinkLossPercent
- **Type**: typing.Optional[int]


# UpdateNetworkProfileResultTypeDef

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigTypeDef]


# UpdateProjectResultTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTestGridProjectRequestRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridVpcConfigTypeDef]


# UpdateTestGridProjectResultTypeDef

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUploadRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[str]

### editContent
- **Type**: typing.Optional[bool]


# UpdateUploadResultTypeDef

### upload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.UploadTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVPCEConfigurationRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### vpceConfigurationName
- **Type**: typing.Optional[str]

### vpceServiceName
- **Type**: typing.Optional[str]

### serviceDnsName
- **Type**: typing.Optional[str]

### vpceConfigurationDescription
- **Type**: typing.Optional[str]


# UpdateVPCEConfigurationResultTypeDef

### vpceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.VPCEConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UploadTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### created
- **Type**: typing.Optional[datetime.datetime]

### type
- **Type**: typing.Optional[typing.Literal['ANDROID_APP', 'APPIUM_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_JAVA_JUNIT_TEST_SPEC', 'APPIUM_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_JAVA_TESTNG_TEST_SPEC', 'APPIUM_NODE_TEST_PACKAGE', 'APPIUM_NODE_TEST_SPEC', 'APPIUM_PYTHON_TEST_PACKAGE', 'APPIUM_PYTHON_TEST_SPEC', 'APPIUM_RUBY_TEST_PACKAGE', 'APPIUM_RUBY_TEST_SPEC', 'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC', 'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC', 'APPIUM_WEB_NODE_TEST_PACKAGE', 'APPIUM_WEB_NODE_TEST_SPEC', 'APPIUM_WEB_PYTHON_TEST_PACKAGE', 'APPIUM_WEB_PYTHON_TEST_SPEC', 'APPIUM_WEB_RUBY_TEST_PACKAGE', 'APPIUM_WEB_RUBY_TEST_SPEC', 'CALABASH_TEST_PACKAGE', 'EXTERNAL_DATA', 'INSTRUMENTATION_TEST_PACKAGE', 'INSTRUMENTATION_TEST_SPEC', 'IOS_APP', 'UIAUTOMATION_TEST_PACKAGE', 'UIAUTOMATOR_TEST_PACKAGE', 'WEB_APP', 'XCTEST_TEST_PACKAGE', 'XCTEST_UI_TEST_PACKAGE', 'XCTEST_UI_TEST_SPEC']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'INITIALIZED', 'PROCESSING', 'SUCCEEDED']]

### url
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]


# VPCEConfigurationTypeDef

### arn
- **Type**: typing.Optional[str]

### vpceConfigurationName
- **Type**: typing.Optional[str]

### vpceServiceName
- **Type**: typing.Optional[str]

### serviceDnsName
- **Type**: typing.Optional[str]

### vpceConfigurationDescription
- **Type**: typing.Optional[str]


# VpcConfigExtraOutputTypeDef

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# VpcConfigOutputTypeDef

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# VpcConfigTypeDef

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes



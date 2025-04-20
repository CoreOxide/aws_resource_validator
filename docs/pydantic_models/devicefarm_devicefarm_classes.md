# Devicefarm Devicefarm Classes

# AccountSettings

### awsAccountNumber
- **Type**: typing.Optional[str]

### unmeteredDevices
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANDROID', 'IOS'], int]]

### unmeteredRemoteAccessDevices
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANDROID', 'IOS'], int]]

### maxJobTimeoutMinutes
- **Type**: typing.Optional[int]

### trialMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TrialMinutes]

### maxSlots
- **Type**: typing.Optional[typing.Dict[str, int]]

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### skipAppResign
- **Type**: typing.Optional[bool]


# Artifact

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

# CPU

### frequency
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[str]

### clock
- **Type**: typing.Optional[float]


# Counters

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


# CreateDevicePoolRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Rule]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### maxDevices
- **Type**: typing.Optional[int]


# CreateDevicePoolResult

### devicePool
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DevicePool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstanceProfileRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### packageCleanup
- **Type**: typing.Optional[bool]

### excludeAppPackagesFromCleanup
- **Type**: typing.Optional[typing.List[str]]

### rebootAfterUse
- **Type**: typing.Optional[bool]


# CreateInstanceProfileResult

### instanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNetworkProfileRequest

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


# CreateNetworkProfileResult

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.NetworkProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VpcConfig, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VpcConfigOutput, NoneType]


# CreateProjectResult

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRemoteAccessSessionConfiguration

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]

### vpceConfigurationArns
- **Type**: typing.Optional[typing.List[str]]

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceProxy]


# CreateRemoteAccessSessionRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.CreateRemoteAccessSessionConfiguration]

### interactionMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'NO_VIDEO', 'VIDEO_ONLY']]

### skipAppResign
- **Type**: typing.Optional[bool]


# CreateRemoteAccessSessionResult

### remoteAccessSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.RemoteAccessSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTestGridProjectRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridVpcConfig, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridVpcConfigOutput, NoneType]


# CreateTestGridProjectResult

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTestGridUrlRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### expiresInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# CreateTestGridUrlResult

### url
- **Type**: <class 'str'>
- **Required**: Yes

### expires
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUploadRequest

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


# CreateUploadResult

### upload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Upload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVPCEConfigurationRequest

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


# CreateVPCEConfigurationResult

### vpceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VPCEConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerArtifactPaths

### iosPaths
- **Type**: typing.Optional[typing.List[str]]

### androidPaths
- **Type**: typing.Optional[typing.List[str]]

### deviceHostPaths
- **Type**: typing.Optional[typing.List[str]]


# CustomerArtifactPathsOutput

### iosPaths
- **Type**: typing.Optional[typing.List[str]]

### androidPaths
- **Type**: typing.Optional[typing.List[str]]

### deviceHostPaths
- **Type**: typing.Optional[typing.List[str]]


# DeleteDevicePoolRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceProfileRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkProfileRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRemoteAccessSessionRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRunRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTestGridProjectRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUploadRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVPCEConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# Device

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.CPU]

### resolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Resolution]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceInstance]]

### availability
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'BUSY', 'HIGHLY_AVAILABLE', 'TEMPORARY_NOT_AVAILABLE']]


# DeviceFilter

### attribute
- **Type**: typing.Literal['ARN', 'AVAILABILITY', 'FLEET_TYPE', 'FORM_FACTOR', 'INSTANCE_ARN', 'INSTANCE_LABELS', 'MANUFACTURER', 'MODEL', 'OS_VERSION', 'PLATFORM', 'REMOTE_ACCESS_ENABLED', 'REMOTE_DEBUG_ENABLED']
- **Required**: Yes

### operator
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'IN', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_IN']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# DeviceFilterOutput

### attribute
- **Type**: typing.Literal['ARN', 'AVAILABILITY', 'FLEET_TYPE', 'FORM_FACTOR', 'INSTANCE_ARN', 'INSTANCE_LABELS', 'MANUFACTURER', 'MODEL', 'OS_VERSION', 'PLATFORM', 'REMOTE_ACCESS_ENABLED', 'REMOTE_DEBUG_ENABLED']
- **Required**: Yes

### operator
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'IN', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_IN']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# DeviceInstance

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.InstanceProfile]


# DeviceMinutes

### total
- **Type**: typing.Optional[float]

### metered
- **Type**: typing.Optional[float]

### unmetered
- **Type**: typing.Optional[float]


# DevicePool

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Rule]]

### maxDevices
- **Type**: typing.Optional[int]


# DevicePoolCompatibilityResult

### device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Device]

### compatible
- **Type**: typing.Optional[bool]

### incompatibilityMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.IncompatibilityMessage]]


# DeviceProxy

### host
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes


# DeviceSelectionConfiguration

### filters
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceFilter, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceFilterOutput]]
- **Required**: Yes

### maxDevices
- **Type**: <class 'int'>
- **Required**: Yes


# DeviceSelectionResult

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceFilterOutput]]

### matchedDevicesCount
- **Type**: typing.Optional[int]

### maxDevices
- **Type**: typing.Optional[int]


# ExecutionConfiguration

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


# GetAccountSettingsResult

### accountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceInstanceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceInstanceResult

### deviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDevicePoolCompatibilityRequest

### devicePoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: typing.Optional[str]

### testType
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_FUZZ', 'INSTRUMENTATION', 'XCTEST', 'XCTEST_UI']]

### test
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ScheduleRunTest]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ScheduleRunConfiguration]


# GetDevicePoolCompatibilityResult

### compatibleDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DevicePoolCompatibilityResult]
- **Required**: Yes

### incompatibleDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DevicePoolCompatibilityResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDevicePoolRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevicePoolResult

### devicePool
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DevicePool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceResult

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Device'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceProfileRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceProfileResult

### instanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResult

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetNetworkProfileRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkProfileResult

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.NetworkProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetOfferingStatusRequest

### nextToken
- **Type**: typing.Optional[str]


# GetOfferingStatusRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# GetOfferingStatusResult

### current
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.OfferingStatus]
- **Required**: Yes

### nextPeriod
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.OfferingStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetProjectRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectResult

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetRemoteAccessSessionRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRemoteAccessSessionResult

### remoteAccessSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.RemoteAccessSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetRunRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRunResult

### run
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Run'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetSuiteRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSuiteResult

### suite
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Suite'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetTestGridProjectRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTestGridProjectResult

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetTestGridSessionRequest

### projectArn
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### sessionArn
- **Type**: typing.Optional[str]


# GetTestGridSessionResult

### testGridSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetTestRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTestResult

### test
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Test'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetUploadRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetUploadResult

### upload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Upload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetVPCEConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetVPCEConfigurationResult

### vpceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VPCEConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# IncompatibilityMessage

### message
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_VERSION', 'ARN', 'AVAILABILITY', 'FLEET_TYPE', 'FORM_FACTOR', 'INSTANCE_ARN', 'INSTANCE_LABELS', 'MANUFACTURER', 'MODEL', 'OS_VERSION', 'PLATFORM', 'REMOTE_ACCESS_ENABLED', 'REMOTE_DEBUG_ENABLED']]


# InstallToRemoteAccessSessionRequest

### remoteAccessSessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes


# InstallToRemoteAccessSessionResult

### appUpload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Upload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# InstanceProfile

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


# Job

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_FUZZ', 'INSTRUMENTATION', 'XCTEST', 'XCTEST_UI']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Counters]

### message
- **Type**: typing.Optional[str]

### device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Device]

### instanceArn
- **Type**: typing.Optional[str]

### deviceMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceMinutes]

### videoEndpoint
- **Type**: typing.Optional[str]

### videoCapture
- **Type**: typing.Optional[bool]


# ListArtifactsRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['FILE', 'LOG', 'SCREENSHOT']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListArtifactsRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['FILE', 'LOG', 'SCREENSHOT']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListArtifactsResult

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Artifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeviceInstancesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeviceInstancesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListDeviceInstancesResult

### deviceInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevicePoolsRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### nextToken
- **Type**: typing.Optional[str]


# ListDevicePoolsRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListDevicePoolsResult

### devicePools
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DevicePool]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevicesRequest

### arn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceFilter, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceFilterOutput]]]


# ListDevicesRequestPaginate

### arn
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceFilter, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceFilterOutput]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListDevicesResult

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Device]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInstanceProfilesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInstanceProfilesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListInstanceProfilesResult

### instanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.InstanceProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListJobsResult

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkProfilesRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkProfilesRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['CURATED', 'PRIVATE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListNetworkProfilesResult

### networkProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.NetworkProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingPromotionsRequest

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingPromotionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListOfferingPromotionsResult

### offeringPromotions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.OfferingPromotion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingTransactionsRequest

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingTransactionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListOfferingTransactionsResult

### offeringTransactions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.OfferingTransaction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequest

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListOfferingsResult

### offerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Offering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsRequest

### arn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsRequestPaginate

### arn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListProjectsResult

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Project]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRemoteAccessSessionsRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRemoteAccessSessionsRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListRemoteAccessSessionsResult

### remoteAccessSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.RemoteAccessSession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunsRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunsRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListRunsResult

### runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Run]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSamplesRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSamplesRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListSamplesResult

### samples
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Sample]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSuitesRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSuitesRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListSuitesResult

### suites
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Suite]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# ListTestGridProjectsRequest

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridProjectsResult

### testGridProjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridProject]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionActionsRequest

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionActionsResult

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridSessionAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionArtifactsRequest

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['LOG', 'VIDEO']]

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionArtifactsResult

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridSessionArtifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionsRequest

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


# ListTestGridSessionsResult

### testGridSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridSession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestsRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestsRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListTestsResult

### tests
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Test]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUniqueProblemsRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUniqueProblemsRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListUniqueProblemsResult

### uniqueProblems
- **Type**: typing.Dict[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED'], typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.UniqueProblem]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUploadsRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['ANDROID_APP', 'APPIUM_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_JAVA_JUNIT_TEST_SPEC', 'APPIUM_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_JAVA_TESTNG_TEST_SPEC', 'APPIUM_NODE_TEST_PACKAGE', 'APPIUM_NODE_TEST_SPEC', 'APPIUM_PYTHON_TEST_PACKAGE', 'APPIUM_PYTHON_TEST_SPEC', 'APPIUM_RUBY_TEST_PACKAGE', 'APPIUM_RUBY_TEST_SPEC', 'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC', 'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC', 'APPIUM_WEB_NODE_TEST_PACKAGE', 'APPIUM_WEB_NODE_TEST_SPEC', 'APPIUM_WEB_PYTHON_TEST_PACKAGE', 'APPIUM_WEB_PYTHON_TEST_SPEC', 'APPIUM_WEB_RUBY_TEST_PACKAGE', 'APPIUM_WEB_RUBY_TEST_SPEC', 'CALABASH_TEST_PACKAGE', 'EXTERNAL_DATA', 'INSTRUMENTATION_TEST_PACKAGE', 'INSTRUMENTATION_TEST_SPEC', 'IOS_APP', 'UIAUTOMATION_TEST_PACKAGE', 'UIAUTOMATOR_TEST_PACKAGE', 'WEB_APP', 'XCTEST_TEST_PACKAGE', 'XCTEST_UI_TEST_PACKAGE', 'XCTEST_UI_TEST_SPEC']]

### nextToken
- **Type**: typing.Optional[str]


# ListUploadsRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['ANDROID_APP', 'APPIUM_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_JAVA_JUNIT_TEST_SPEC', 'APPIUM_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_JAVA_TESTNG_TEST_SPEC', 'APPIUM_NODE_TEST_PACKAGE', 'APPIUM_NODE_TEST_SPEC', 'APPIUM_PYTHON_TEST_PACKAGE', 'APPIUM_PYTHON_TEST_SPEC', 'APPIUM_RUBY_TEST_PACKAGE', 'APPIUM_RUBY_TEST_SPEC', 'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE', 'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC', 'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE', 'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC', 'APPIUM_WEB_NODE_TEST_PACKAGE', 'APPIUM_WEB_NODE_TEST_SPEC', 'APPIUM_WEB_PYTHON_TEST_PACKAGE', 'APPIUM_WEB_PYTHON_TEST_SPEC', 'APPIUM_WEB_RUBY_TEST_PACKAGE', 'APPIUM_WEB_RUBY_TEST_SPEC', 'CALABASH_TEST_PACKAGE', 'EXTERNAL_DATA', 'INSTRUMENTATION_TEST_PACKAGE', 'INSTRUMENTATION_TEST_SPEC', 'IOS_APP', 'UIAUTOMATION_TEST_PACKAGE', 'UIAUTOMATOR_TEST_PACKAGE', 'WEB_APP', 'XCTEST_TEST_PACKAGE', 'XCTEST_UI_TEST_PACKAGE', 'XCTEST_UI_TEST_SPEC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListUploadsResult

### uploads
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Upload]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVPCEConfigurationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListVPCEConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.PaginatorConfig]


# ListVPCEConfigurationsResult

### vpceConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VPCEConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Location

### latitude
- **Type**: <class 'float'>
- **Required**: Yes

### longitude
- **Type**: <class 'float'>
- **Required**: Yes


# MonetaryAmount

### amount
- **Type**: typing.Optional[float]

### currencyCode
- **Type**: typing.Optional[typing.Literal['USD']]


# NetworkProfile

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


# Offering

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['RECURRING']]

### platform
- **Type**: typing.Optional[typing.Literal['ANDROID', 'IOS']]

### recurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.RecurringCharge]]


# OfferingPromotion

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# OfferingStatus

### type
- **Type**: typing.Optional[typing.Literal['PURCHASE', 'RENEW', 'SYSTEM']]

### offering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Offering]

### quantity
- **Type**: typing.Optional[int]

### effectiveOn
- **Type**: typing.Optional[datetime.datetime]


# OfferingTransaction

### offeringStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.OfferingStatus]

### transactionId
- **Type**: typing.Optional[str]

### offeringPromotionId
- **Type**: typing.Optional[str]

### createdOn
- **Type**: typing.Optional[datetime.datetime]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.MonetaryAmount]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Problem

### run
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ProblemDetail]

### job
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ProblemDetail]

### suite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ProblemDetail]

### test
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ProblemDetail]

### device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Device]

### result
- **Type**: typing.Optional[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED']]

### message
- **Type**: typing.Optional[str]


# ProblemDetail

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# Project

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### created
- **Type**: typing.Optional[datetime.datetime]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VpcConfigOutput]


# PurchaseOfferingRequest

### offeringId
- **Type**: <class 'str'>
- **Required**: Yes

### quantity
- **Type**: <class 'int'>
- **Required**: Yes

### offeringPromotionId
- **Type**: typing.Optional[str]


# PurchaseOfferingResult

### offeringTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.OfferingTransaction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# Radios

### wifi
- **Type**: typing.Optional[bool]

### bluetooth
- **Type**: typing.Optional[bool]

### nfc
- **Type**: typing.Optional[bool]

### gps
- **Type**: typing.Optional[bool]


# RecurringCharge

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.MonetaryAmount]

### frequency
- **Type**: typing.Optional[typing.Literal['MONTHLY']]


# RemoteAccessSession

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Device]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceMinutes]

### endpoint
- **Type**: typing.Optional[str]

### deviceUdid
- **Type**: typing.Optional[str]

### interactionMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'NO_VIDEO', 'VIDEO_ONLY']]

### skipAppResign
- **Type**: typing.Optional[bool]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VpcConfigOutput]

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceProxy]


# RenewOfferingRequest

### offeringId
- **Type**: <class 'str'>
- **Required**: Yes

### quantity
- **Type**: <class 'int'>
- **Required**: Yes


# RenewOfferingResult

### offeringTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.OfferingTransaction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# Resolution

### width
- **Type**: typing.Optional[int]

### height
- **Type**: typing.Optional[int]


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


# Rule

### attribute
- **Type**: typing.Optional[typing.Literal['APPIUM_VERSION', 'ARN', 'AVAILABILITY', 'FLEET_TYPE', 'FORM_FACTOR', 'INSTANCE_ARN', 'INSTANCE_LABELS', 'MANUFACTURER', 'MODEL', 'OS_VERSION', 'PLATFORM', 'REMOTE_ACCESS_ENABLED', 'REMOTE_DEBUG_ENABLED']]

### operator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'IN', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_IN']]

### value
- **Type**: typing.Optional[str]


# Run

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_FUZZ', 'INSTRUMENTATION', 'XCTEST', 'XCTEST_UI']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Counters]

### message
- **Type**: typing.Optional[str]

### totalJobs
- **Type**: typing.Optional[int]

### completedJobs
- **Type**: typing.Optional[int]

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]

### deviceMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceMinutes]

### networkProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.NetworkProfile]

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceProxy]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Radios]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Location]

### customerArtifactPaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.CustomerArtifactPathsOutput]

### webUrl
- **Type**: typing.Optional[str]

### skipAppResign
- **Type**: typing.Optional[bool]

### testSpecArn
- **Type**: typing.Optional[str]

### deviceSelectionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceSelectionResult]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VpcConfigOutput]


# Sample

### arn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CPU', 'MEMORY', 'NATIVE_AVG_DRAWTIME', 'NATIVE_FPS', 'NATIVE_FRAMES', 'NATIVE_MAX_DRAWTIME', 'NATIVE_MIN_DRAWTIME', 'OPENGL_AVG_DRAWTIME', 'OPENGL_FPS', 'OPENGL_FRAMES', 'OPENGL_MAX_DRAWTIME', 'OPENGL_MIN_DRAWTIME', 'RX', 'RX_RATE', 'THREADS', 'TX', 'TX_RATE']]

### url
- **Type**: typing.Optional[str]


# ScheduleRunConfiguration

### extraDataPackageArn
- **Type**: typing.Optional[str]

### networkProfileArn
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Location]

### vpceConfigurationArns
- **Type**: typing.Optional[typing.List[str]]

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceProxy]

### customerArtifactPaths
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.CustomerArtifactPaths, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.CustomerArtifactPathsOutput, NoneType]

### radios
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Radios]

### auxiliaryApps
- **Type**: typing.Optional[typing.List[str]]

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]


# ScheduleRunRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### test
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ScheduleRunTest'>
- **Required**: Yes

### appArn
- **Type**: typing.Optional[str]

### devicePoolArn
- **Type**: typing.Optional[str]

### deviceSelectionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceSelectionConfiguration]

### name
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ScheduleRunConfiguration]

### executionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ExecutionConfiguration]


# ScheduleRunResult

### run
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Run'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# ScheduleRunTest

### type
- **Type**: typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_FUZZ', 'INSTRUMENTATION', 'XCTEST', 'XCTEST_UI']
- **Required**: Yes

### testPackageArn
- **Type**: typing.Optional[str]

### testSpecArn
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# StopJobRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopJobResult

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# StopRemoteAccessSessionRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopRemoteAccessSessionResult

### remoteAccessSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.RemoteAccessSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# StopRunRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopRunResult

### run
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Run'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# Suite

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_FUZZ', 'INSTRUMENTATION', 'XCTEST', 'XCTEST_UI']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Counters]

### message
- **Type**: typing.Optional[str]

### deviceMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceMinutes]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Tag]
- **Required**: Yes


# Test

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_FUZZ', 'INSTRUMENTATION', 'XCTEST', 'XCTEST_UI']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Counters]

### message
- **Type**: typing.Optional[str]

### deviceMinutes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceMinutes]


# TestGridProject

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridVpcConfigOutput]

### created
- **Type**: typing.Optional[datetime.datetime]


# TestGridSession

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


# TestGridSessionAction

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


# TestGridSessionArtifact

### filename
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['SELENIUM_LOG', 'UNKNOWN', 'VIDEO']]

### url
- **Type**: typing.Optional[str]


# TestGridVpcConfig

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# TestGridVpcConfigOutput

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# TrialMinutes

### total
- **Type**: typing.Optional[float]

### remaining
- **Type**: typing.Optional[float]


# UniqueProblem

### message
- **Type**: typing.Optional[str]

### problems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Problem]]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDeviceInstanceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### profileArn
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.List[str]]


# UpdateDeviceInstanceResult

### deviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DeviceInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDevicePoolRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Rule]]

### maxDevices
- **Type**: typing.Optional[int]

### clearMaxDevices
- **Type**: typing.Optional[bool]


# UpdateDevicePoolResult

### devicePool
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.DevicePool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInstanceProfileRequest

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
- **Type**: typing.Optional[typing.List[str]]

### rebootAfterUse
- **Type**: typing.Optional[bool]


# UpdateInstanceProfileResult

### instanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNetworkProfileRequest

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


# UpdateNetworkProfileResult

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.NetworkProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VpcConfig, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VpcConfigOutput, NoneType]


# UpdateProjectResult

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTestGridProjectRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridVpcConfig, aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridVpcConfigOutput, NoneType]


# UpdateTestGridProjectResult

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.TestGridProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUploadRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[str]

### editContent
- **Type**: typing.Optional[bool]


# UpdateUploadResult

### upload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.Upload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVPCEConfigurationRequest

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


# UpdateVPCEConfigurationResult

### vpceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.VPCEConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# Upload

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


# VPCEConfiguration

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


# VpcConfig

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# VpcConfigOutput

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes



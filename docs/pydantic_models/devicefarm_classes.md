# Devicefarm Classes

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TrialMinutes]

### maxSlots
- **Type**: typing.Optional[typing.Dict[str, int]]

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### skipAppResign
- **Type**: typing.Optional[bool]


# Artifact

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.Rule]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### maxDevices
- **Type**: typing.Optional[int]


# CreateDevicePoolResult

### devicePool
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DevicePool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[str]]

### rebootAfterUse
- **Type**: typing.Optional[bool]


# CreateInstanceProfileResult

### instanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNetworkProfileResult

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigUnion]


# CreateProjectResult

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRemoteAccessSessionConfiguration

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]

### vpceConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceProxy]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CreateRemoteAccessSessionConfiguration]

### interactionMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'NO_VIDEO', 'VIDEO_ONLY']]

### skipAppResign
- **Type**: typing.Optional[bool]


# CreateRemoteAccessSessionResult

### remoteAccessSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.RemoteAccessSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTestGridProjectRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridVpcConfigUnion]


# CreateTestGridProjectResult

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUploadResult

### upload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Upload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.VPCEConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerArtifactPaths

### iosPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### androidPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### deviceHostPaths
- **Type**: typing.Optional[typing.Sequence[str]]


# CustomerArtifactPathsOutput

### iosPaths
- **Type**: typing.Optional[typing.List[str]]

### androidPaths
- **Type**: typing.Optional[typing.List[str]]

### deviceHostPaths
- **Type**: typing.Optional[typing.List[str]]


# CustomerArtifactPathsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CPU]

### resolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Resolution]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceInstance]]

### availability
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'BUSY', 'HIGHLY_AVAILABLE', 'TEMPORARY_NOT_AVAILABLE']]


# DeviceFilterOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeviceFilterUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfile]


# DeviceMinutes

### total
- **Type**: typing.Optional[float]

### metered
- **Type**: typing.Optional[float]

### unmetered
- **Type**: typing.Optional[float]


# DevicePool

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DevicePoolCompatibilityResult

### device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Device]

### compatible
- **Type**: typing.Optional[bool]

### incompatibilityMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.IncompatibilityMessage]]


# DeviceProxy

### host
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes


# DeviceSelectionConfiguration

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterUnion]
- **Required**: Yes

### maxDevices
- **Type**: <class 'int'>
- **Required**: Yes


# DeviceSelectionResult

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterOutput]]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceInstanceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceInstanceResult

### deviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DeviceInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ScheduleRunTest]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ScheduleRunConfiguration]


# GetDevicePoolCompatibilityResult

### compatibleDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DevicePoolCompatibilityResult]
- **Required**: Yes

### incompatibleDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DevicePoolCompatibilityResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDevicePoolRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevicePoolResult

### devicePool
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DevicePool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceResult

### device
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Device'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceProfileRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceProfileResult

### instanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResult

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetNetworkProfileRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkProfileResult

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetOfferingStatusRequest

### nextToken
- **Type**: typing.Optional[str]


# GetOfferingStatusRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# GetOfferingStatusResult

### current
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.devicefarm_classes.OfferingStatus]
- **Required**: Yes

### nextPeriod
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.devicefarm_classes.OfferingStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetProjectRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectResult

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetRemoteAccessSessionRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRemoteAccessSessionResult

### remoteAccessSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.RemoteAccessSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetRunRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRunResult

### run
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Run'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetSuiteRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSuiteResult

### suite
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Suite'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetTestGridProjectRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTestGridProjectResult

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetTestRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTestResult

### test
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Test'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetUploadRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetUploadResult

### upload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Upload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# GetVPCEConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetVPCEConfigurationResult

### vpceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.VPCEConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# IncompatibilityMessage

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InstallToRemoteAccessSessionRequest

### remoteAccessSessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes


# InstallToRemoteAccessSessionResult

### appUpload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Upload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListArtifactsResult

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Artifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListDeviceInstancesResult

### deviceInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevicePoolsResult

### devicePools
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DevicePool]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevicesRequest

### arn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterUnion]]


# ListDevicesRequestPaginate

### arn
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterUnion]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListDevicesResult

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Device]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListInstanceProfilesResult

### instanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListJobsResult

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkProfilesResult

### networkProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingPromotionsRequest

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingPromotionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListOfferingPromotionsResult

### offeringPromotions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingPromotion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingTransactionsRequest

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingTransactionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListOfferingTransactionsResult

### offeringTransactions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTransaction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequest

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListOfferingsResult

### offerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Offering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListProjectsResult

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Project]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListRemoteAccessSessionsResult

### remoteAccessSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.RemoteAccessSession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListRunsResult

### runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Run]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListSamplesResult

### samples
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Sample]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListSuitesResult

### suites
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Suite]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# ListTestGridProjectsRequest

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridProjectsResult

### testGridProjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProject]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSessionAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionArtifactsResult

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSessionArtifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Timestamp]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Timestamp]

### endTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Timestamp]

### endTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Timestamp]

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionsResult

### testGridSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListTestsResult

### tests
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Test]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListUniqueProblemsResult

### uniqueProblems
- **Type**: typing.Dict[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED'], typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.UniqueProblem]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUploadsResult

### uploads
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Upload]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfig]


# ListVPCEConfigurationsResult

### vpceConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.VPCEConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Offering

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OfferingPromotion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OfferingStatus

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OfferingTransaction

### offeringStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingStatus]

### transactionId
- **Type**: typing.Optional[str]

### offeringPromotionId
- **Type**: typing.Optional[str]

### createdOn
- **Type**: typing.Optional[datetime.datetime]

### cost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.MonetaryAmount]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Problem

### run
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ProblemDetail]

### job
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ProblemDetail]

### suite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ProblemDetail]

### test
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ProblemDetail]

### device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Device]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigOutput]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTransaction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.MonetaryAmount]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Device]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceMinutes]

### endpoint
- **Type**: typing.Optional[str]

### deviceUdid
- **Type**: typing.Optional[str]

### interactionMode
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'NO_VIDEO', 'VIDEO_ONLY']]

### skipAppResign
- **Type**: typing.Optional[bool]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigOutput]

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceProxy]


# RenewOfferingRequest

### offeringId
- **Type**: <class 'str'>
- **Required**: Yes

### quantity
- **Type**: <class 'int'>
- **Required**: Yes


# RenewOfferingResult

### offeringTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTransaction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Run

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Sample

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScheduleRunConfiguration

### extraDataPackageArn
- **Type**: typing.Optional[str]

### networkProfileArn
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Location]

### vpceConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceProxy]

### customerArtifactPaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CustomerArtifactPathsUnion]

### radios
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.Radios]

### auxiliaryApps
- **Type**: typing.Optional[typing.Sequence[str]]

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]


# ScheduleRunRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### test
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ScheduleRunTest'>
- **Required**: Yes

### appArn
- **Type**: typing.Optional[str]

### devicePoolArn
- **Type**: typing.Optional[str]

### deviceSelectionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceSelectionConfiguration]

### name
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ScheduleRunConfiguration]

### executionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.ExecutionConfiguration]


# ScheduleRunResult

### run
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Run'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# ScheduleRunTest

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StopJobRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopJobResult

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# StopRemoteAccessSessionRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopRemoteAccessSessionResult

### remoteAccessSession
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.RemoteAccessSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# StopRunRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopRunResult

### run
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Run'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# Suite

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.Tag]
- **Required**: Yes


# Test

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TestGridProject

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridVpcConfigOutput]

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TestGridVpcConfig

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
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


# TestGridVpcConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrialMinutes

### total
- **Type**: typing.Optional[float]

### remaining
- **Type**: typing.Optional[float]


# UniqueProblem

### message
- **Type**: typing.Optional[str]

### problems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.Problem]]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeviceInstanceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### profileArn
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateDeviceInstanceResult

### deviceInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DeviceInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.Rule]]

### maxDevices
- **Type**: typing.Optional[int]

### clearMaxDevices
- **Type**: typing.Optional[bool]


# UpdateDevicePoolResult

### devicePool
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.DevicePool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[str]]

### rebootAfterUse
- **Type**: typing.Optional[bool]


# UpdateInstanceProfileResult

### instanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNetworkProfileResult

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigUnion]


# UpdateProjectResult

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridVpcConfigUnion]


# UpdateTestGridProjectResult

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.Upload'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.VPCEConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadata'>
- **Required**: Yes


# Upload

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Sequence[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
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


# VpcConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


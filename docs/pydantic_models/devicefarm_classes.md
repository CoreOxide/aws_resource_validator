# Devicefarm Classes

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# CreateDevicePoolRequestTypeDef

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


# CreateInstanceProfileRequestTypeDef

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


# CreateNetworkProfileResultTypeDef

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigUnionTypeDef]


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

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceProxyTypeDef]


# CreateRemoteAccessSessionRequestTypeDef

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


# CreateTestGridProjectRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridVpcConfigUnionTypeDef]


# CreateTestGridProjectResultTypeDef

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTestGridUrlRequestTypeDef

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


# CreateUploadResultTypeDef

### upload
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.UploadTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVPCEConfigurationRequestTypeDef

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


# CustomerArtifactPathsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteDevicePoolRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceProfileRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkProfileRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRemoteAccessSessionRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRunRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTestGridProjectRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUploadRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVPCEConfigurationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeviceFilterOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeviceFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeviceProxyTypeDef

### host
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes


# DeviceSelectionConfigurationTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterUnionTypeDef]
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


# GetDeviceInstanceRequestTypeDef

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


# GetDevicePoolCompatibilityRequestTypeDef

### devicePoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: typing.Optional[str]

### testType
- **Type**: typing.Optional[typing.Literal['APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_NODE', 'APPIUM_PYTHON', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_NODE', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_RUBY', 'BUILTIN_FUZZ', 'INSTRUMENTATION', 'XCTEST', 'XCTEST_UI']]

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


# GetDevicePoolRequestTypeDef

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


# GetDeviceRequestTypeDef

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


# GetInstanceProfileRequestTypeDef

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


# GetJobRequestTypeDef

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


# GetNetworkProfileRequestTypeDef

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


# GetOfferingStatusRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# GetOfferingStatusRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# GetOfferingStatusResultTypeDef

### current
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.devicefarm_classes.OfferingStatusTypeDef]
- **Required**: Yes

### nextPeriod
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.devicefarm_classes.OfferingStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetProjectRequestTypeDef

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


# GetRemoteAccessSessionRequestTypeDef

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


# GetRunRequestTypeDef

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


# GetSuiteRequestTypeDef

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


# GetTestGridProjectRequestTypeDef

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


# GetTestGridSessionRequestTypeDef

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


# GetTestRequestTypeDef

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


# GetUploadRequestTypeDef

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


# GetVPCEConfigurationRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InstallToRemoteAccessSessionRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListArtifactsResultTypeDef

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.ArtifactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeviceInstancesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListDeviceInstancesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeviceInstancesResultTypeDef

### deviceInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevicePoolsResultTypeDef

### devicePools
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DevicePoolTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevicesRequestPaginateTypeDef

### arn
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterUnionTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListDevicesRequestTypeDef

### arn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceFilterUnionTypeDef]]


# ListDevicesResultTypeDef

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInstanceProfilesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListInstanceProfilesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInstanceProfilesResultTypeDef

### instanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.InstanceProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsRequestPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListJobsRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsResultTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.JobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkProfilesResultTypeDef

### networkProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingPromotionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListOfferingPromotionsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingPromotionsResultTypeDef

### offeringPromotions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingPromotionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingTransactionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListOfferingTransactionsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingTransactionsResultTypeDef

### offeringTransactions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTransactionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListOfferingsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListOfferingsResultTypeDef

### offerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.OfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsRequestPaginateTypeDef

### arn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListProjectsRequestTypeDef

### arn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsResultTypeDef

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.ProjectTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRemoteAccessSessionsRequestPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListRemoteAccessSessionsRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRemoteAccessSessionsResultTypeDef

### remoteAccessSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.RemoteAccessSessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunsRequestPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListRunsRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRunsResultTypeDef

### runs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.RunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSamplesRequestPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListSamplesRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSamplesResultTypeDef

### samples
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.SampleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSuitesRequestPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListSuitesRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSuitesResultTypeDef

### suites
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.SuiteTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

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


# ListTestGridProjectsRequestTypeDef

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridProjectsResultTypeDef

### testGridProjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProjectTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionActionsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionArtifactsResultTypeDef

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSessionArtifactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionsRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CLOSED', 'ERRORED']]

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TimestampTypeDef]

### endTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TimestampTypeDef]

### endTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TimestampTypeDef]

### maxResult
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTestGridSessionsResultTypeDef

### testGridSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridSessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestsRequestPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListTestsRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTestsResultTypeDef

### tests
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.TestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUniqueProblemsRequestPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListUniqueProblemsRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUniqueProblemsResultTypeDef

### uniqueProblems
- **Type**: typing.Dict[typing.Literal['ERRORED', 'FAILED', 'PASSED', 'PENDING', 'SKIPPED', 'STOPPED', 'WARNED'], typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.UniqueProblemTypeDef]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUploadsResultTypeDef

### uploads
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.UploadTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVPCEConfigurationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.PaginatorConfigTypeDef]


# ListVPCEConfigurationsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListVPCEConfigurationsResultTypeDef

### vpceConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.devicefarm_classes.VPCEConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OfferingPromotionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OfferingStatusTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# PurchaseOfferingRequestTypeDef

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

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceProxyTypeDef]


# RenewOfferingRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RunTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SampleTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### deviceProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.DeviceProxyTypeDef]

### customerArtifactPaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.CustomerArtifactPathsUnionTypeDef]

### radios
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.RadiosTypeDef]

### auxiliaryApps
- **Type**: typing.Optional[typing.Sequence[str]]

### billingMethod
- **Type**: typing.Optional[typing.Literal['METERED', 'UNMETERED']]


# ScheduleRunRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StopJobRequestTypeDef

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


# StopRemoteAccessSessionRequestTypeDef

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


# StopRunRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# TestGridVpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TestTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeviceInstanceRequestTypeDef

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


# UpdateDevicePoolRequestTypeDef

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


# UpdateInstanceProfileRequestTypeDef

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


# UpdateNetworkProfileResultTypeDef

### networkProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.NetworkProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### defaultJobTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.VpcConfigUnionTypeDef]


# UpdateProjectResultTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTestGridProjectRequestTypeDef

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devicefarm_classes.TestGridVpcConfigUnionTypeDef]


# UpdateTestGridProjectResultTypeDef

### testGridProject
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.TestGridProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devicefarm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUploadRequestTypeDef

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


# UpdateVPCEConfigurationRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# VpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


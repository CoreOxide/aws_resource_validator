# Greengrassv2 Classes

# AssociateClientDeviceWithCoreDeviceEntry

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateClientDeviceWithCoreDeviceErrorEntry

### thingName
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# AssociateServiceRoleToAccountRequest

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateServiceRoleToAccountResponse

### associatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# AssociatedClientDevice

### thingName
- **Type**: typing.Optional[str]

### associationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateClientDeviceWithCoreDeviceRequest

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.AssociateClientDeviceWithCoreDeviceEntry]]


# BatchAssociateClientDeviceWithCoreDeviceResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.AssociateClientDeviceWithCoreDeviceErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisassociateClientDeviceFromCoreDeviceRequest

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.DisassociateClientDeviceFromCoreDeviceEntry]]


# BatchDisassociateClientDeviceFromCoreDeviceResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.DisassociateClientDeviceFromCoreDeviceErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelDeploymentRequest

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDeploymentResponse

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# CloudComponentStatus

### componentState
- **Type**: typing.Optional[typing.Literal['DEPLOYABLE', 'DEPRECATED', 'FAILED', 'INITIATED', 'REQUESTED']]

### message
- **Type**: typing.Optional[str]

### errors
- **Type**: typing.Optional[typing.Dict[str, str]]

### vendorGuidance
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DISCONTINUED']]

### vendorGuidanceMessage
- **Type**: typing.Optional[str]


# Component

### arn
- **Type**: typing.Optional[str]

### componentName
- **Type**: typing.Optional[str]

### latestVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentLatestVersion]


# ComponentCandidate

### componentName
- **Type**: typing.Optional[str]

### componentVersion
- **Type**: typing.Optional[str]

### versionRequirements
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ComponentConfigurationUpdate

### merge
- **Type**: typing.Optional[str]

### reset
- **Type**: typing.Optional[typing.Sequence[str]]


# ComponentConfigurationUpdateOutput

### merge
- **Type**: typing.Optional[str]

### reset
- **Type**: typing.Optional[typing.List[str]]


# ComponentConfigurationUpdateUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentDependencyRequirement

### versionRequirement
- **Type**: typing.Optional[str]

### dependencyType
- **Type**: typing.Optional[typing.Literal['HARD', 'SOFT']]


# ComponentDeploymentSpecification

### componentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### configurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentConfigurationUpdateUnion]

### runWith
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentRunWith]


# ComponentDeploymentSpecificationOutput

### componentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### configurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentConfigurationUpdateOutput]

### runWith
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentRunWith]


# ComponentDeploymentSpecificationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentLatestVersion

### arn
- **Type**: typing.Optional[str]

### componentVersion
- **Type**: typing.Optional[str]

### creationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### publisher
- **Type**: typing.Optional[str]

### platforms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentPlatformOutput]]


# ComponentPlatform

### name
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ComponentPlatformOutput

### name
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# ComponentPlatformUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentRunWith

### posixUser
- **Type**: typing.Optional[str]

### systemResourceLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.SystemResourceLimits]

### windowsUser
- **Type**: typing.Optional[str]


# ComponentVersionListItem

### componentName
- **Type**: typing.Optional[str]

### componentVersion
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# ConnectivityInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoreDevice

### coreDeviceThingName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### lastStatusUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### platform
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[str]

### runtime
- **Type**: typing.Optional[str]


# CreateComponentVersionRequest

### inlineRecipe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.Blob]

### lambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaFunctionRecipeSource]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateComponentVersionResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### componentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.CloudComponentStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeploymentRequest

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentName
- **Type**: typing.Optional[str]

### components
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentDeploymentSpecificationUnion]]

### iotJobConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentIoTJobConfigurationUnion]

### deploymentPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentPolicies]

### parentTargetArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateDeploymentResponse

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### iotJobId
- **Type**: <class 'str'>
- **Required**: Yes

### iotJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteComponentRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCoreDeviceRequest

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentRequest

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# Deployment

### targetArn
- **Type**: typing.Optional[str]

### revisionId
- **Type**: typing.Optional[str]

### deploymentId
- **Type**: typing.Optional[str]

### deploymentName
- **Type**: typing.Optional[str]

### creationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### deploymentStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELED', 'COMPLETED', 'FAILED', 'INACTIVE']]

### isLatestForTarget
- **Type**: typing.Optional[bool]

### parentTargetArn
- **Type**: typing.Optional[str]


# DeploymentComponentUpdatePolicy

### timeoutInSeconds
- **Type**: typing.Optional[int]

### action
- **Type**: typing.Optional[typing.Literal['NOTIFY_COMPONENTS', 'SKIP_NOTIFY_COMPONENTS']]


# DeploymentConfigurationValidationPolicy

### timeoutInSeconds
- **Type**: typing.Optional[int]


# DeploymentIoTJobConfiguration

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobExecutionsRolloutConfig]

### abortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobAbortConfig]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobTimeoutConfig]


# DeploymentIoTJobConfigurationOutput

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobExecutionsRolloutConfig]

### abortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobAbortConfigOutput]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobTimeoutConfig]


# DeploymentIoTJobConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentPolicies

### failureHandlingPolicy
- **Type**: typing.Optional[typing.Literal['DO_NOTHING', 'ROLLBACK']]

### componentUpdatePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentComponentUpdatePolicy]

### configurationValidationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentConfigurationValidationPolicy]


# DescribeComponentRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeComponentResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### componentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### publisher
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.CloudComponentStatus'>
- **Required**: Yes

### platforms
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentPlatformOutput]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateClientDeviceFromCoreDeviceEntry

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateClientDeviceFromCoreDeviceErrorEntry

### thingName
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# DisassociateServiceRoleFromAccountResponse

### disassociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# EffectiveDeployment

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentName
- **Type**: <class 'str'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### coreDeviceExecutionStatus
- **Type**: typing.Literal['CANCELED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'SUCCEEDED', 'TIMED_OUT']
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### iotJobId
- **Type**: typing.Optional[str]

### iotJobArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### statusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.EffectiveDeploymentStatusDetails]


# EffectiveDeploymentStatusDetails

### errorStack
- **Type**: typing.Optional[typing.List[str]]

### errorTypes
- **Type**: typing.Optional[typing.List[str]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetComponentRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### recipeOutputFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]


# GetComponentResponse

### recipeOutputFormat
- **Type**: typing.Literal['JSON', 'YAML']
- **Required**: Yes

### recipe
- **Type**: <class 'bytes'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetComponentVersionArtifactRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### artifactName
- **Type**: <class 'str'>
- **Required**: Yes

### s3EndpointType
- **Type**: typing.Optional[typing.Literal['GLOBAL', 'REGIONAL']]

### iotEndpointType
- **Type**: typing.Optional[typing.Literal['fips', 'standard']]


# GetComponentVersionArtifactResponse

### preSignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectivityInfoRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectivityInfoResponse

### connectivityInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ConnectivityInfo]
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetCoreDeviceRequest

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCoreDeviceResponse

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### coreVersion
- **Type**: <class 'str'>
- **Required**: Yes

### platform
- **Type**: <class 'str'>
- **Required**: Yes

### architecture
- **Type**: <class 'str'>
- **Required**: Yes

### runtime
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes

### lastStatusUpdateTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentRequest

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentResponse

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentStatus
- **Type**: typing.Literal['ACTIVE', 'CANCELED', 'COMPLETED', 'FAILED', 'INACTIVE']
- **Required**: Yes

### iotJobId
- **Type**: <class 'str'>
- **Required**: Yes

### iotJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### components
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentDeploymentSpecificationOutput]
- **Required**: Yes

### deploymentPolicies
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentPolicies'>
- **Required**: Yes

### iotJobConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentIoTJobConfigurationOutput'>
- **Required**: Yes

### creationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### isLatestForTarget
- **Type**: <class 'bool'>
- **Required**: Yes

### parentTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceRoleForAccountResponse

### associatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# InstalledComponent

### componentName
- **Type**: typing.Optional[str]

### componentVersion
- **Type**: typing.Optional[str]

### lifecycleState
- **Type**: typing.Optional[typing.Literal['BROKEN', 'ERRORED', 'FINISHED', 'INSTALLED', 'NEW', 'RUNNING', 'STARTING', 'STOPPING']]

### lifecycleStateDetails
- **Type**: typing.Optional[str]

### isRoot
- **Type**: typing.Optional[bool]

### lastStatusChangeTimestamp
- **Type**: typing.Optional[datetime.datetime]

### lastReportedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### lastInstallationSource
- **Type**: typing.Optional[str]

### lifecycleStatusCodes
- **Type**: typing.Optional[typing.List[str]]


# IoTJobAbortConfig

### criteriaList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobAbortCriteria]
- **Required**: Yes


# IoTJobAbortConfigOutput

### criteriaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobAbortCriteria]
- **Required**: Yes


# IoTJobAbortCriteria

### failureType
- **Type**: typing.Literal['ALL', 'FAILED', 'REJECTED', 'TIMED_OUT']
- **Required**: Yes

### action
- **Type**: typing.Literal['CANCEL']
- **Required**: Yes

### thresholdPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### minNumberOfExecutedThings
- **Type**: <class 'int'>
- **Required**: Yes


# IoTJobExecutionsRolloutConfig

### exponentialRate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobExponentialRolloutRate]

### maximumPerMinute
- **Type**: typing.Optional[int]


# IoTJobExponentialRolloutRate

### baseRatePerMinute
- **Type**: <class 'int'>
- **Required**: Yes

### incrementFactor
- **Type**: <class 'float'>
- **Required**: Yes

### rateIncreaseCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobRateIncreaseCriteria'>
- **Required**: Yes


# IoTJobRateIncreaseCriteria

### numberOfNotifiedThings
- **Type**: typing.Optional[int]

### numberOfSucceededThings
- **Type**: typing.Optional[int]


# IoTJobTimeoutConfig

### inProgressTimeoutInMinutes
- **Type**: typing.Optional[int]


# LambdaContainerParams

### memorySizeInKB
- **Type**: typing.Optional[int]

### mountROSysfs
- **Type**: typing.Optional[bool]

### volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaVolumeMount]]

### devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaDeviceMount]]


# LambdaDeviceMount

### path
- **Type**: <class 'str'>
- **Required**: Yes

### permission
- **Type**: typing.Optional[typing.Literal['ro', 'rw']]

### addGroupOwner
- **Type**: typing.Optional[bool]


# LambdaEventSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LambdaExecutionParameters

### eventSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaEventSource]]

### maxQueueSize
- **Type**: typing.Optional[int]

### maxInstancesCount
- **Type**: typing.Optional[int]

### maxIdleTimeInSeconds
- **Type**: typing.Optional[int]

### timeoutInSeconds
- **Type**: typing.Optional[int]

### statusTimeoutInSeconds
- **Type**: typing.Optional[int]

### pinned
- **Type**: typing.Optional[bool]

### inputPayloadEncodingType
- **Type**: typing.Optional[typing.Literal['binary', 'json']]

### execArgs
- **Type**: typing.Optional[typing.Sequence[str]]

### environmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### linuxProcessParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaLinuxProcessParams]


# LambdaFunctionRecipeSource

### lambdaArn
- **Type**: <class 'str'>
- **Required**: Yes

### componentName
- **Type**: typing.Optional[str]

### componentVersion
- **Type**: typing.Optional[str]

### componentPlatforms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentPlatformUnion]]

### componentDependencies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentDependencyRequirement]]

### componentLambdaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaExecutionParameters]


# LambdaLinuxProcessParams

### isolationMode
- **Type**: typing.Optional[typing.Literal['GreengrassContainer', 'NoContainer']]

### containerParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaContainerParams]


# LambdaVolumeMount

### sourcePath
- **Type**: <class 'str'>
- **Required**: Yes

### destinationPath
- **Type**: <class 'str'>
- **Required**: Yes

### permission
- **Type**: typing.Optional[typing.Literal['ro', 'rw']]

### addGroupOwner
- **Type**: typing.Optional[bool]


# ListClientDevicesAssociatedWithCoreDeviceRequest

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListClientDevicesAssociatedWithCoreDeviceRequestPaginate

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfig]


# ListClientDevicesAssociatedWithCoreDeviceResponse

### associatedClientDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.AssociatedClientDevice]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentVersionsRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentVersionsRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfig]


# ListComponentVersionsResponse

### componentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentVersionListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsRequest

### scope
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsRequestPaginate

### scope
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfig]


# ListComponentsResponse

### components
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.Component]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCoreDevicesRequest

### thingGroupArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### runtime
- **Type**: typing.Optional[str]


# ListCoreDevicesRequestPaginate

### thingGroupArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### runtime
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfig]


# ListCoreDevicesResponse

### coreDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.CoreDevice]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequest

### targetArn
- **Type**: typing.Optional[str]

### historyFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'LATEST_ONLY']]

### parentTargetArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequestPaginate

### targetArn
- **Type**: typing.Optional[str]

### historyFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'LATEST_ONLY']]

### parentTargetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfig]


# ListDeploymentsResponse

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.Deployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEffectiveDeploymentsRequest

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEffectiveDeploymentsRequestPaginate

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfig]


# ListEffectiveDeploymentsResponse

### effectiveDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.EffectiveDeployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInstalledComponentsRequest

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### topologyFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'ROOT']]


# ListInstalledComponentsRequestPaginate

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### topologyFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'ROOT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfig]


# ListInstalledComponentsResponse

### installedComponents
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.InstalledComponent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResolveComponentCandidatesRequest

### platform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentPlatformUnion]

### componentCandidates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentCandidate]]


# ResolveComponentCandidatesResponse

### resolvedComponentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ResolvedComponentVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes


# ResolvedComponentVersion

### arn
- **Type**: typing.Optional[str]

### componentName
- **Type**: typing.Optional[str]

### componentVersion
- **Type**: typing.Optional[str]

### recipe
- **Type**: typing.Optional[bytes]

### vendorGuidance
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DISCONTINUED']]

### message
- **Type**: typing.Optional[str]


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


# SystemResourceLimits

### memory
- **Type**: typing.Optional[int]

### cpus
- **Type**: typing.Optional[float]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectivityInfoRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### connectivityInfo
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.ConnectivityInfo]
- **Required**: Yes


# UpdateConnectivityInfoResponse

### version
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadata'>
- **Required**: Yes



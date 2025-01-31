# Greengrassv2 Classes

# AssociateClientDeviceWithCoreDeviceEntryTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef

### thingName
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# AssociateServiceRoleToAccountRequestRequestTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateServiceRoleToAccountResponseTypeDef

### associatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatedClientDeviceTypeDef

### thingName
- **Type**: typing.Optional[str]

### associationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.AssociateClientDeviceWithCoreDeviceEntryTypeDef]]


# BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.DisassociateClientDeviceFromCoreDeviceEntryTypeDef]]


# BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelDeploymentRequestRequestTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDeploymentResponseTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CloudComponentStatusTypeDef

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


# ComponentCandidateTypeDef

### componentName
- **Type**: typing.Optional[str]

### componentVersion
- **Type**: typing.Optional[str]

### versionRequirements
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ComponentConfigurationUpdateOutputTypeDef

### merge
- **Type**: typing.Optional[str]

### reset
- **Type**: typing.Optional[typing.List[str]]


# ComponentConfigurationUpdateTypeDef

### merge
- **Type**: typing.Optional[str]

### reset
- **Type**: typing.Optional[typing.Sequence[str]]


# ComponentDependencyRequirementTypeDef

### versionRequirement
- **Type**: typing.Optional[str]

### dependencyType
- **Type**: typing.Optional[typing.Literal['HARD', 'SOFT']]


# ComponentDeploymentSpecificationOutputTypeDef

### componentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### configurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentConfigurationUpdateOutputTypeDef]

### runWith
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentRunWithTypeDef]


# ComponentDeploymentSpecificationTypeDef

### componentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### configurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentConfigurationUpdateTypeDef]

### runWith
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentRunWithTypeDef]


# ComponentLatestVersionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentPlatformOutputTypeDef]]


# ComponentPlatformExtraOutputTypeDef

### name
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# ComponentPlatformOutputTypeDef

### name
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# ComponentPlatformTypeDef

### name
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ComponentRunWithTypeDef

### posixUser
- **Type**: typing.Optional[str]

### systemResourceLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.SystemResourceLimitsTypeDef]

### windowsUser
- **Type**: typing.Optional[str]


# ComponentTypeDef

### arn
- **Type**: typing.Optional[str]

### componentName
- **Type**: typing.Optional[str]

### latestVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentLatestVersionTypeDef]


# ComponentVersionListItemTypeDef

### componentName
- **Type**: typing.Optional[str]

### componentVersion
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# ConnectivityInfoTypeDef

### id
- **Type**: typing.Optional[str]

### hostAddress
- **Type**: typing.Optional[str]

### portNumber
- **Type**: typing.Optional[int]

### metadata
- **Type**: typing.Optional[str]


# CoreDeviceTypeDef

### coreDeviceThingName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### lastStatusUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]


# CreateComponentVersionRequestRequestTypeDef

### inlineRecipe
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### lambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaFunctionRecipeSourceTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateComponentVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.CloudComponentStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentRequestRequestTypeDef

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentName
- **Type**: typing.Optional[str]

### components
- **Type**: typing.Optional[typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentDeploymentSpecificationTypeDef, aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentDeploymentSpecificationOutputTypeDef]]]

### iotJobConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentIoTJobConfigurationTypeDef]

### deploymentPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentPoliciesTypeDef]

### parentTargetArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateDeploymentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteComponentRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCoreDeviceRequestRequestTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentRequestRequestTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeploymentComponentUpdatePolicyTypeDef

### timeoutInSeconds
- **Type**: typing.Optional[int]

### action
- **Type**: typing.Optional[typing.Literal['NOTIFY_COMPONENTS', 'SKIP_NOTIFY_COMPONENTS']]


# DeploymentConfigurationValidationPolicyTypeDef

### timeoutInSeconds
- **Type**: typing.Optional[int]


# DeploymentIoTJobConfigurationOutputTypeDef

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobExecutionsRolloutConfigTypeDef]

### abortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobAbortConfigOutputTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobTimeoutConfigTypeDef]


# DeploymentIoTJobConfigurationTypeDef

### jobExecutionsRolloutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobExecutionsRolloutConfigTypeDef]

### abortConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobAbortConfigTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobTimeoutConfigTypeDef]


# DeploymentPoliciesTypeDef

### failureHandlingPolicy
- **Type**: typing.Optional[typing.Literal['DO_NOTHING', 'ROLLBACK']]

### componentUpdatePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentComponentUpdatePolicyTypeDef]

### configurationValidationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentConfigurationValidationPolicyTypeDef]


# DeploymentTypeDef

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


# DescribeComponentRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeComponentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.CloudComponentStatusTypeDef'>
- **Required**: Yes

### platforms
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentPlatformOutputTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateClientDeviceFromCoreDeviceEntryTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef

### thingName
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# DisassociateServiceRoleFromAccountResponseTypeDef

### disassociatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EffectiveDeploymentStatusDetailsTypeDef

### errorStack
- **Type**: typing.Optional[typing.List[str]]

### errorTypes
- **Type**: typing.Optional[typing.List[str]]


# EffectiveDeploymentTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.EffectiveDeploymentStatusDetailsTypeDef]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComponentRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### recipeOutputFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]


# GetComponentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComponentVersionArtifactRequestRequestTypeDef

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


# GetComponentVersionArtifactResponseTypeDef

### preSignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectivityInfoRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectivityInfoResponseTypeDef

### connectivityInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ConnectivityInfoTypeDef]
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCoreDeviceRequestRequestTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCoreDeviceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentRequestRequestTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentResponseTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentDeploymentSpecificationOutputTypeDef]
- **Required**: Yes

### deploymentPolicies
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentPoliciesTypeDef'>
- **Required**: Yes

### iotJobConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentIoTJobConfigurationOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceRoleForAccountResponseTypeDef

### associatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstalledComponentTypeDef

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


# IoTJobAbortConfigOutputTypeDef

### criteriaList
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobAbortCriteriaTypeDef]
- **Required**: Yes


# IoTJobAbortConfigTypeDef

### criteriaList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobAbortCriteriaTypeDef]
- **Required**: Yes


# IoTJobAbortCriteriaTypeDef

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


# IoTJobExecutionsRolloutConfigTypeDef

### exponentialRate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobExponentialRolloutRateTypeDef]

### maximumPerMinute
- **Type**: typing.Optional[int]


# IoTJobExponentialRolloutRateTypeDef

### baseRatePerMinute
- **Type**: <class 'int'>
- **Required**: Yes

### incrementFactor
- **Type**: <class 'float'>
- **Required**: Yes

### rateIncreaseCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.IoTJobRateIncreaseCriteriaTypeDef'>
- **Required**: Yes


# IoTJobRateIncreaseCriteriaTypeDef

### numberOfNotifiedThings
- **Type**: typing.Optional[int]

### numberOfSucceededThings
- **Type**: typing.Optional[int]


# IoTJobTimeoutConfigTypeDef

### inProgressTimeoutInMinutes
- **Type**: typing.Optional[int]


# LambdaContainerParamsTypeDef

### memorySizeInKB
- **Type**: typing.Optional[int]

### mountROSysfs
- **Type**: typing.Optional[bool]

### volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaVolumeMountTypeDef]]

### devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaDeviceMountTypeDef]]


# LambdaDeviceMountTypeDef

### path
- **Type**: <class 'str'>
- **Required**: Yes

### permission
- **Type**: typing.Optional[typing.Literal['ro', 'rw']]

### addGroupOwner
- **Type**: typing.Optional[bool]


# LambdaEventSourceTypeDef

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['IOT_CORE', 'PUB_SUB']
- **Required**: Yes


# LambdaExecutionParametersTypeDef

### eventSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaEventSourceTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaLinuxProcessParamsTypeDef]


# LambdaFunctionRecipeSourceTypeDef

### lambdaArn
- **Type**: <class 'str'>
- **Required**: Yes

### componentName
- **Type**: typing.Optional[str]

### componentVersion
- **Type**: typing.Optional[str]

### componentPlatforms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentPlatformTypeDef]]

### componentDependencies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentDependencyRequirementTypeDef]]

### componentLambdaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaExecutionParametersTypeDef]


# LambdaLinuxProcessParamsTypeDef

### isolationMode
- **Type**: typing.Optional[typing.Literal['GreengrassContainer', 'NoContainer']]

### containerParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.LambdaContainerParamsTypeDef]


# LambdaVolumeMountTypeDef

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


# ListClientDevicesAssociatedWithCoreDeviceRequestListClientDevicesAssociatedWithCoreDevicePaginateTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfigTypeDef]


# ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef

### associatedClientDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.AssociatedClientDeviceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListComponentVersionsRequestListComponentVersionsPaginateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfigTypeDef]


# ListComponentVersionsRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentVersionsResponseTypeDef

### componentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentVersionListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListComponentsRequestListComponentsPaginateTypeDef

### scope
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfigTypeDef]


# ListComponentsRequestRequestTypeDef

### scope
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsResponseTypeDef

### components
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCoreDevicesRequestListCoreDevicesPaginateTypeDef

### thingGroupArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfigTypeDef]


# ListCoreDevicesRequestRequestTypeDef

### thingGroupArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCoreDevicesResponseTypeDef

### coreDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.CoreDeviceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeploymentsRequestListDeploymentsPaginateTypeDef

### targetArn
- **Type**: typing.Optional[str]

### historyFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'LATEST_ONLY']]

### parentTargetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfigTypeDef]


# ListDeploymentsRequestRequestTypeDef

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


# ListDeploymentsResponseTypeDef

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.DeploymentTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEffectiveDeploymentsRequestListEffectiveDeploymentsPaginateTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfigTypeDef]


# ListEffectiveDeploymentsRequestRequestTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEffectiveDeploymentsResponseTypeDef

### effectiveDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.EffectiveDeploymentTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstalledComponentsRequestListInstalledComponentsPaginateTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### topologyFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'ROOT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.PaginatorConfigTypeDef]


# ListInstalledComponentsRequestRequestTypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### topologyFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'ROOT']]


# ListInstalledComponentsResponseTypeDef

### installedComponents
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.InstalledComponentTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResolveComponentCandidatesRequestRequestTypeDef

### platform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentPlatformTypeDef]

### componentCandidates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.ComponentCandidateTypeDef]]


# ResolveComponentCandidatesResponseTypeDef

### resolvedComponentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.greengrassv2_classes.ResolvedComponentVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResolvedComponentVersionTypeDef

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


# SystemResourceLimitsTypeDef

### memory
- **Type**: typing.Optional[int]

### cpus
- **Type**: typing.Optional[float]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectivityInfoRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### connectivityInfo
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.greengrassv2_classes.ConnectivityInfoTypeDef]
- **Required**: Yes


# UpdateConnectivityInfoResponseTypeDef

### version
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.greengrassv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



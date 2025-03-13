# Robomaker Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteWorldsRequestTypeDef

### worlds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteWorldsResponseTypeDef

### unprocessedWorlds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDescribeSimulationJobRequestTypeDef

### jobs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDescribeSimulationJobResponseTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobTypeDef]
- **Required**: Yes

### unprocessedJobs
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPolicyTypeDef

### timeoutInSeconds
- **Type**: typing.Optional[int]

### maxConcurrency
- **Type**: typing.Optional[int]


# CancelDeploymentJobRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSimulationJobBatchRequestTypeDef

### batch
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSimulationJobRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# CancelWorldExportJobRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# CancelWorldGenerationJobRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# ComputeResponseTypeDef

### simulationUnitLimit
- **Type**: typing.Optional[int]

### computeType
- **Type**: typing.Optional[typing.Literal['CPU', 'GPU_AND_CPU']]

### gpuUnitLimit
- **Type**: typing.Optional[int]


# ComputeTypeDef

### simulationUnitLimit
- **Type**: typing.Optional[int]

### computeType
- **Type**: typing.Optional[typing.Literal['CPU', 'GPU_AND_CPU']]

### gpuUnitLimit
- **Type**: typing.Optional[int]


# CreateDeploymentJobRequestTypeDef

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentApplicationConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigUnionTypeDef]
- **Required**: Yes

### deploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDeploymentJobResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Failed', 'InProgress', 'Pending', 'Preparing', 'Succeeded']
- **Required**: Yes

### deploymentApplicationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigOutputTypeDef]
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['BadLambdaAssociated', 'BadPermissionError', 'DeploymentFleetDoesNotExist', 'DownloadConditionFailed', 'EnvironmentSetupError', 'EtagMismatch', 'ExtractingBundleFailure', 'FailureThresholdBreached', 'FleetDeploymentTimeout', 'GreengrassDeploymentFailed', 'GreengrassGroupVersionDoesNotExist', 'InternalServerError', 'InvalidGreengrassGroup', 'LambdaDeleted', 'MissingRobotApplicationArchitecture', 'MissingRobotArchitecture', 'MissingRobotDeploymentResource', 'PostLaunchFileFailure', 'PreLaunchFileFailure', 'ResourceNotFound', 'RobotAgentConnectionTimeout', 'RobotApplicationDoesNotExist', 'RobotDeploymentAborted', 'RobotDeploymentNoResponse']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deploymentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.DeploymentConfigTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFleetRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFleetResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRobotApplicationRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.SourceConfigTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef]


# CreateRobotApplicationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SourceTypeDef]
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRobotApplicationVersionRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### currentRevisionId
- **Type**: typing.Optional[str]

### s3Etags
- **Type**: typing.Optional[typing.Sequence[str]]

### imageDigest
- **Type**: typing.Optional[str]


# CreateRobotApplicationVersionResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SourceTypeDef]
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRobotRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### architecture
- **Type**: typing.Literal['ARM64', 'ARMHF', 'X86_64']
- **Required**: Yes

### greengrassGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRobotResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### greengrassGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### architecture
- **Type**: typing.Literal['ARM64', 'ARMHF', 'X86_64']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSimulationApplicationRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.SimulationSoftwareSuiteTypeDef'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.SourceConfigTypeDef]]

### renderingEngine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.RenderingEngineTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef]


# CreateSimulationApplicationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SourceTypeDef]
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.SimulationSoftwareSuiteTypeDef'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### renderingEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RenderingEngineTypeDef'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSimulationApplicationVersionRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### currentRevisionId
- **Type**: typing.Optional[str]

### s3Etags
- **Type**: typing.Optional[typing.Sequence[str]]

### imageDigest
- **Type**: typing.Optional[str]


# CreateSimulationApplicationVersionResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SourceTypeDef]
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.SimulationSoftwareSuiteTypeDef'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### renderingEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RenderingEngineTypeDef'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSimulationJobRequestTypeDef

### maxJobDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### outputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef]

### loggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.LoggingConfigTypeDef]

### failureBehavior
- **Type**: typing.Optional[typing.Literal['Continue', 'Fail']]

### robotApplications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigUnionTypeDef]]

### simulationApplications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigUnionTypeDef]]

### dataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.DataSourceConfigUnionTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.VPCConfigUnionTypeDef]

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.ComputeTypeDef]


# CreateSimulationJobResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Completed', 'Failed', 'Pending', 'Preparing', 'Restarting', 'Running', 'RunningFailed', 'Terminated', 'Terminating']
- **Required**: Yes

### lastStartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureBehavior
- **Type**: typing.Literal['Continue', 'Fail']
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['BadPermissionsCloudwatchLogs', 'BadPermissionsRobotApplication', 'BadPermissionsS3Object', 'BadPermissionsS3Output', 'BadPermissionsSimulationApplication', 'BadPermissionsUserCredentials', 'BatchCanceled', 'BatchTimedOut', 'ENILimitExceeded', 'InternalServiceError', 'InvalidBundleRobotApplication', 'InvalidBundleSimulationApplication', 'InvalidInput', 'InvalidS3Resource', 'LimitExceeded', 'MismatchedEtag', 'RequestThrottled', 'ResourceNotFound', 'RobotApplicationCrash', 'RobotApplicationHealthCheckFailure', 'RobotApplicationVersionMismatchedEtag', 'SimulationApplicationCrash', 'SimulationApplicationHealthCheckFailure', 'SimulationApplicationVersionMismatchedEtag', 'SubnetIpLimitExceeded', 'ThrottlingError', 'UploadContentMismatchError', 'WrongRegionRobotApplication', 'WrongRegionS3Bucket', 'WrongRegionS3Output', 'WrongRegionSimulationApplication']
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### outputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef'>
- **Required**: Yes

### loggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.LoggingConfigTypeDef'>
- **Required**: Yes

### maxJobDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### simulationTimeMillis
- **Type**: <class 'int'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### robotApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigOutputTypeDef]
- **Required**: Yes

### simulationApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigOutputTypeDef]
- **Required**: Yes

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DataSourceTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### vpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.VPCConfigResponseTypeDef'>
- **Required**: Yes

### compute
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ComputeResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorldExportJobRequestTypeDef

### worlds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### outputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateWorldExportJobResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Canceling', 'Completed', 'Failed', 'Pending', 'Running']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['AccessDenied', 'InternalServiceError', 'InvalidInput', 'LimitExceeded', 'RequestThrottled', 'ResourceNotFound']
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### outputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorldGenerationJobRequestTypeDef

### template
- **Type**: <class 'str'>
- **Required**: Yes

### worldCount
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.WorldCountTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### worldTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateWorldGenerationJobResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Canceling', 'Completed', 'Failed', 'PartialFailed', 'Pending', 'Running']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['AllWorldGenerationFailed', 'InternalServiceError', 'InvalidInput', 'LimitExceeded', 'RequestThrottled', 'ResourceNotFound']
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: <class 'str'>
- **Required**: Yes

### worldCount
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.WorldCountTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### worldTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorldTemplateRequestTypeDef

### clientRequestToken
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### templateBody
- **Type**: typing.Optional[str]

### templateLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.TemplateLocationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateWorldTemplateResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSourceConfigOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteFleetRequestTypeDef

### fleet
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRobotApplicationRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DeleteRobotRequestTypeDef

### robot
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSimulationApplicationRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DeleteWorldTemplateRequestTypeDef

### template
- **Type**: <class 'str'>
- **Required**: Yes


# DeploymentApplicationConfigOutputTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.DeploymentLaunchConfigOutputTypeDef'>
- **Required**: Yes


# DeploymentApplicationConfigTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.DeploymentLaunchConfigUnionTypeDef'>
- **Required**: Yes


# DeploymentApplicationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentConfigTypeDef

### concurrentDeploymentPercentage
- **Type**: typing.Optional[int]

### failureThresholdPercentage
- **Type**: typing.Optional[int]

### robotDeploymentTimeoutInSeconds
- **Type**: typing.Optional[int]

### downloadConditionFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.S3ObjectTypeDef]


# DeploymentJobTypeDef

### arn
- **Type**: typing.Optional[str]

### fleet
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Failed', 'InProgress', 'Pending', 'Preparing', 'Succeeded']]

### deploymentApplicationConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigOutputTypeDef]]

### deploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentConfigTypeDef]

### failureReason
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['BadLambdaAssociated', 'BadPermissionError', 'DeploymentFleetDoesNotExist', 'DownloadConditionFailed', 'EnvironmentSetupError', 'EtagMismatch', 'ExtractingBundleFailure', 'FailureThresholdBreached', 'FleetDeploymentTimeout', 'GreengrassDeploymentFailed', 'GreengrassGroupVersionDoesNotExist', 'InternalServerError', 'InvalidGreengrassGroup', 'LambdaDeleted', 'MissingRobotApplicationArchitecture', 'MissingRobotArchitecture', 'MissingRobotDeploymentResource', 'PostLaunchFileFailure', 'PreLaunchFileFailure', 'ResourceNotFound', 'RobotAgentConnectionTimeout', 'RobotApplicationDoesNotExist', 'RobotDeploymentAborted', 'RobotDeploymentNoResponse']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# DeploymentLaunchConfigOutputTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### launchFile
- **Type**: <class 'str'>
- **Required**: Yes

### preLaunchFile
- **Type**: typing.Optional[str]

### postLaunchFile
- **Type**: typing.Optional[str]

### environmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeploymentLaunchConfigTypeDef

### packageName
- **Type**: <class 'str'>
- **Required**: Yes

### launchFile
- **Type**: <class 'str'>
- **Required**: Yes

### preLaunchFile
- **Type**: typing.Optional[str]

### postLaunchFile
- **Type**: typing.Optional[str]

### environmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeploymentLaunchConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeregisterRobotRequestTypeDef

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### robot
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterRobotResponseTypeDef

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### robot
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeploymentJobRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeploymentJobResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Failed', 'InProgress', 'Pending', 'Preparing', 'Succeeded']
- **Required**: Yes

### deploymentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.DeploymentConfigTypeDef'>
- **Required**: Yes

### deploymentApplicationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigOutputTypeDef]
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['BadLambdaAssociated', 'BadPermissionError', 'DeploymentFleetDoesNotExist', 'DownloadConditionFailed', 'EnvironmentSetupError', 'EtagMismatch', 'ExtractingBundleFailure', 'FailureThresholdBreached', 'FleetDeploymentTimeout', 'GreengrassDeploymentFailed', 'GreengrassGroupVersionDoesNotExist', 'InternalServerError', 'InvalidGreengrassGroup', 'LambdaDeleted', 'MissingRobotApplicationArchitecture', 'MissingRobotArchitecture', 'MissingRobotDeploymentResource', 'PostLaunchFileFailure', 'PreLaunchFileFailure', 'ResourceNotFound', 'RobotAgentConnectionTimeout', 'RobotApplicationDoesNotExist', 'RobotDeploymentAborted', 'RobotDeploymentNoResponse']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### robotDeploymentSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotDeploymentTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFleetRequestTypeDef

### fleet
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFleetResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### robots
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastDeploymentStatus
- **Type**: typing.Literal['Canceled', 'Failed', 'InProgress', 'Pending', 'Preparing', 'Succeeded']
- **Required**: Yes

### lastDeploymentJob
- **Type**: <class 'str'>
- **Required**: Yes

### lastDeploymentTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRobotApplicationRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DescribeRobotApplicationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SourceTypeDef]
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef'>
- **Required**: Yes

### imageDigest
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRobotRequestTypeDef

### robot
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRobotResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Available', 'Deploying', 'Failed', 'InSync', 'NoResponse', 'PendingNewDeployment', 'Registered']
- **Required**: Yes

### greengrassGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### architecture
- **Type**: typing.Literal['ARM64', 'ARMHF', 'X86_64']
- **Required**: Yes

### lastDeploymentJob
- **Type**: <class 'str'>
- **Required**: Yes

### lastDeploymentTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSimulationApplicationRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DescribeSimulationApplicationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SourceTypeDef]
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.SimulationSoftwareSuiteTypeDef'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### renderingEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RenderingEngineTypeDef'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef'>
- **Required**: Yes

### imageDigest
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSimulationJobBatchRequestTypeDef

### batch
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSimulationJobBatchResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Canceling', 'Completed', 'Completing', 'Failed', 'InProgress', 'Pending', 'TimedOut', 'TimingOut']
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### batchPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.BatchPolicyTypeDef'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['InternalServiceError']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.FailedCreateSimulationJobRequestTypeDef]
- **Required**: Yes

### pendingRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobRequestOutputTypeDef]
- **Required**: Yes

### createdRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobSummaryTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSimulationJobRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSimulationJobResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Completed', 'Failed', 'Pending', 'Preparing', 'Restarting', 'Running', 'RunningFailed', 'Terminated', 'Terminating']
- **Required**: Yes

### lastStartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureBehavior
- **Type**: typing.Literal['Continue', 'Fail']
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['BadPermissionsCloudwatchLogs', 'BadPermissionsRobotApplication', 'BadPermissionsS3Object', 'BadPermissionsS3Output', 'BadPermissionsSimulationApplication', 'BadPermissionsUserCredentials', 'BatchCanceled', 'BatchTimedOut', 'ENILimitExceeded', 'InternalServiceError', 'InvalidBundleRobotApplication', 'InvalidBundleSimulationApplication', 'InvalidInput', 'InvalidS3Resource', 'LimitExceeded', 'MismatchedEtag', 'RequestThrottled', 'ResourceNotFound', 'RobotApplicationCrash', 'RobotApplicationHealthCheckFailure', 'RobotApplicationVersionMismatchedEtag', 'SimulationApplicationCrash', 'SimulationApplicationHealthCheckFailure', 'SimulationApplicationVersionMismatchedEtag', 'SubnetIpLimitExceeded', 'ThrottlingError', 'UploadContentMismatchError', 'WrongRegionRobotApplication', 'WrongRegionS3Bucket', 'WrongRegionS3Output', 'WrongRegionSimulationApplication']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### outputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef'>
- **Required**: Yes

### loggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.LoggingConfigTypeDef'>
- **Required**: Yes

### maxJobDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### simulationTimeMillis
- **Type**: <class 'int'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### robotApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigOutputTypeDef]
- **Required**: Yes

### simulationApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigOutputTypeDef]
- **Required**: Yes

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DataSourceTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### vpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.VPCConfigResponseTypeDef'>
- **Required**: Yes

### networkInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.NetworkInterfaceTypeDef'>
- **Required**: Yes

### compute
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ComputeResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorldExportJobRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorldExportJobResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Canceling', 'Completed', 'Failed', 'Pending', 'Running']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['AccessDenied', 'InternalServiceError', 'InvalidInput', 'LimitExceeded', 'RequestThrottled', 'ResourceNotFound']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### worlds
- **Type**: typing.List[str]
- **Required**: Yes

### outputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorldGenerationJobRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorldGenerationJobResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Canceling', 'Completed', 'Failed', 'PartialFailed', 'Pending', 'Running']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['AllWorldGenerationFailed', 'InternalServiceError', 'InvalidInput', 'LimitExceeded', 'RequestThrottled', 'ResourceNotFound']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: <class 'str'>
- **Required**: Yes

### worldCount
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.WorldCountTypeDef'>
- **Required**: Yes

### finishedWorldsSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.FinishedWorldsSummaryTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### worldTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorldRequestTypeDef

### world
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorldResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### generationJob
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### worldDescriptionBody
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorldTemplateRequestTypeDef

### template
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorldTemplateResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentTypeDef

### uri
- **Type**: typing.Optional[str]


# FailedCreateSimulationJobRequestTypeDef

### request
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobRequestOutputTypeDef]

### failureReason
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['BadPermissionsCloudwatchLogs', 'BadPermissionsRobotApplication', 'BadPermissionsS3Object', 'BadPermissionsS3Output', 'BadPermissionsSimulationApplication', 'BadPermissionsUserCredentials', 'BatchCanceled', 'BatchTimedOut', 'ENILimitExceeded', 'InternalServiceError', 'InvalidBundleRobotApplication', 'InvalidBundleSimulationApplication', 'InvalidInput', 'InvalidS3Resource', 'LimitExceeded', 'MismatchedEtag', 'RequestThrottled', 'ResourceNotFound', 'RobotApplicationCrash', 'RobotApplicationHealthCheckFailure', 'RobotApplicationVersionMismatchedEtag', 'SimulationApplicationCrash', 'SimulationApplicationHealthCheckFailure', 'SimulationApplicationVersionMismatchedEtag', 'SubnetIpLimitExceeded', 'ThrottlingError', 'UploadContentMismatchError', 'WrongRegionRobotApplication', 'WrongRegionS3Bucket', 'WrongRegionS3Output', 'WrongRegionSimulationApplication']]

### failedAt
- **Type**: typing.Optional[datetime.datetime]


# FailureSummaryTypeDef

### totalFailureCount
- **Type**: typing.Optional[int]

### failures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.WorldFailureTypeDef]]


# FilterTypeDef

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# FinishedWorldsSummaryTypeDef

### finishedCount
- **Type**: typing.Optional[int]

### succeededWorlds
- **Type**: typing.Optional[typing.List[str]]

### failureSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.FailureSummaryTypeDef]


# FleetTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastDeploymentStatus
- **Type**: typing.Optional[typing.Literal['Canceled', 'Failed', 'InProgress', 'Pending', 'Preparing', 'Succeeded']]

### lastDeploymentJob
- **Type**: typing.Optional[str]

### lastDeploymentTime
- **Type**: typing.Optional[datetime.datetime]


# GetWorldTemplateBodyRequestTypeDef

### template
- **Type**: typing.Optional[str]

### generationJob
- **Type**: typing.Optional[str]


# GetWorldTemplateBodyResponseTypeDef

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LaunchConfigOutputTypeDef

### packageName
- **Type**: typing.Optional[str]

### launchFile
- **Type**: typing.Optional[str]

### environmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### portForwardingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PortForwardingConfigOutputTypeDef]

### streamUI
- **Type**: typing.Optional[bool]

### command
- **Type**: typing.Optional[typing.List[str]]


# LaunchConfigTypeDef

### packageName
- **Type**: typing.Optional[str]

### launchFile
- **Type**: typing.Optional[str]

### environmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### portForwardingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PortForwardingConfigUnionTypeDef]

### streamUI
- **Type**: typing.Optional[bool]

### command
- **Type**: typing.Optional[typing.Sequence[str]]


# LaunchConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListDeploymentJobsRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListDeploymentJobsRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDeploymentJobsResponseTypeDef

### deploymentJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetsRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListFleetsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]


# ListFleetsResponseTypeDef

### fleetDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.FleetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRobotApplicationsRequestPaginateTypeDef

### versionQualifier
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListRobotApplicationsRequestTypeDef

### versionQualifier
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]


# ListRobotApplicationsResponseTypeDef

### robotApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRobotsRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListRobotsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]


# ListRobotsResponseTypeDef

### robots
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSimulationApplicationsRequestPaginateTypeDef

### versionQualifier
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListSimulationApplicationsRequestTypeDef

### versionQualifier
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]


# ListSimulationApplicationsResponseTypeDef

### simulationApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSimulationJobBatchesRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListSimulationJobBatchesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]


# ListSimulationJobBatchesResponseTypeDef

### simulationJobBatchSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobBatchSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSimulationJobsRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListSimulationJobsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]


# ListSimulationJobsResponseTypeDef

### simulationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorldExportJobsRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListWorldExportJobsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]


# ListWorldExportJobsResponseTypeDef

### worldExportJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.WorldExportJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorldGenerationJobsRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListWorldGenerationJobsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]


# ListWorldGenerationJobsResponseTypeDef

### worldGenerationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.WorldGenerationJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorldTemplatesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListWorldTemplatesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorldTemplatesResponseTypeDef

### templateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.TemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorldsRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListWorldsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]


# ListWorldsResponseTypeDef

### worldSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.WorldSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LoggingConfigTypeDef

### recordAllRosTopics
- **Type**: typing.Optional[bool]


# NetworkInterfaceTypeDef

### networkInterfaceId
- **Type**: typing.Optional[str]

### privateIpAddress
- **Type**: typing.Optional[str]

### publicIpAddress
- **Type**: typing.Optional[str]


# OutputLocationTypeDef

### s3Bucket
- **Type**: typing.Optional[str]

### s3Prefix
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortForwardingConfigOutputTypeDef

### portMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.PortMappingTypeDef]]


# PortForwardingConfigTypeDef

### portMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.PortMappingTypeDef]]


# PortForwardingConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PortMappingTypeDef

### jobPort
- **Type**: <class 'int'>
- **Required**: Yes

### applicationPort
- **Type**: <class 'int'>
- **Required**: Yes

### enableOnPublicIp
- **Type**: typing.Optional[bool]


# ProgressDetailTypeDef

### currentProgress
- **Type**: typing.Optional[typing.Literal['DownloadingExtracting', 'ExecutingDownloadCondition', 'ExecutingPostLaunch', 'ExecutingPreLaunch', 'Finished', 'Launching', 'Validating']]

### percentDone
- **Type**: typing.Optional[float]

### estimatedTimeRemainingSeconds
- **Type**: typing.Optional[int]

### targetResource
- **Type**: typing.Optional[str]


# RegisterRobotRequestTypeDef

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### robot
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterRobotResponseTypeDef

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### robot
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RenderingEngineTypeDef

### name
- **Type**: typing.Optional[typing.Literal['OGRE']]

### version
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


# RestartSimulationJobRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# RobotApplicationConfigOutputTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.LaunchConfigOutputTypeDef'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]

### uploadConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.UploadConfigurationTypeDef]]

### useDefaultUploadConfigurations
- **Type**: typing.Optional[bool]

### tools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.ToolTypeDef]]

### useDefaultTools
- **Type**: typing.Optional[bool]


# RobotApplicationConfigTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.LaunchConfigUnionTypeDef'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]

### uploadConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.UploadConfigurationTypeDef]]

### useDefaultUploadConfigurations
- **Type**: typing.Optional[bool]

### tools
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.ToolTypeDef]]

### useDefaultTools
- **Type**: typing.Optional[bool]


# RobotApplicationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RobotApplicationSummaryTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### robotSoftwareSuite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef]


# RobotDeploymentTypeDef

### arn
- **Type**: typing.Optional[str]

### deploymentStartTime
- **Type**: typing.Optional[datetime.datetime]

### deploymentFinishTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Available', 'Deploying', 'Failed', 'InSync', 'NoResponse', 'PendingNewDeployment', 'Registered']]

### progressDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.ProgressDetailTypeDef]

### failureReason
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['BadLambdaAssociated', 'BadPermissionError', 'DeploymentFleetDoesNotExist', 'DownloadConditionFailed', 'EnvironmentSetupError', 'EtagMismatch', 'ExtractingBundleFailure', 'FailureThresholdBreached', 'FleetDeploymentTimeout', 'GreengrassDeploymentFailed', 'GreengrassGroupVersionDoesNotExist', 'InternalServerError', 'InvalidGreengrassGroup', 'LambdaDeleted', 'MissingRobotApplicationArchitecture', 'MissingRobotArchitecture', 'MissingRobotDeploymentResource', 'PostLaunchFileFailure', 'PreLaunchFileFailure', 'ResourceNotFound', 'RobotAgentConnectionTimeout', 'RobotApplicationDoesNotExist', 'RobotDeploymentAborted', 'RobotDeploymentNoResponse']]


# RobotSoftwareSuiteTypeDef

### name
- **Type**: typing.Optional[typing.Literal['General', 'ROS', 'ROS2']]

### version
- **Type**: typing.Optional[typing.Literal['Dashing', 'Foxy', 'Kinetic', 'Melodic']]


# RobotTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### fleetArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Available', 'Deploying', 'Failed', 'InSync', 'NoResponse', 'PendingNewDeployment', 'Registered']]

### greenGrassGroupId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'ARMHF', 'X86_64']]

### lastDeploymentJob
- **Type**: typing.Optional[str]

### lastDeploymentTime
- **Type**: typing.Optional[datetime.datetime]


# S3KeyOutputTypeDef

### s3Key
- **Type**: typing.Optional[str]

### etag
- **Type**: typing.Optional[str]


# S3ObjectTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### etag
- **Type**: typing.Optional[str]


# SimulationApplicationConfigOutputTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.LaunchConfigOutputTypeDef'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]

### uploadConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.UploadConfigurationTypeDef]]

### worldConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.WorldConfigTypeDef]]

### useDefaultUploadConfigurations
- **Type**: typing.Optional[bool]

### tools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.ToolTypeDef]]

### useDefaultTools
- **Type**: typing.Optional[bool]


# SimulationApplicationConfigTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.LaunchConfigUnionTypeDef'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]

### uploadConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.UploadConfigurationTypeDef]]

### worldConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.WorldConfigTypeDef]]

### useDefaultUploadConfigurations
- **Type**: typing.Optional[bool]

### tools
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.ToolTypeDef]]

### useDefaultTools
- **Type**: typing.Optional[bool]


# SimulationApplicationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SimulationApplicationSummaryTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### robotSoftwareSuite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef]

### simulationSoftwareSuite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.SimulationSoftwareSuiteTypeDef]


# SimulationJobBatchSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Canceling', 'Completed', 'Completing', 'Failed', 'InProgress', 'Pending', 'TimedOut', 'TimingOut']]

### failedRequestCount
- **Type**: typing.Optional[int]

### pendingRequestCount
- **Type**: typing.Optional[int]

### createdRequestCount
- **Type**: typing.Optional[int]


# SimulationJobRequestOutputTypeDef

### maxJobDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### outputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef]

### loggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.LoggingConfigTypeDef]

### iamRole
- **Type**: typing.Optional[str]

### failureBehavior
- **Type**: typing.Optional[typing.Literal['Continue', 'Fail']]

### useDefaultApplications
- **Type**: typing.Optional[bool]

### robotApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigOutputTypeDef]]

### simulationApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigOutputTypeDef]]

### dataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DataSourceConfigOutputTypeDef]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.VPCConfigOutputTypeDef]

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.ComputeTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SimulationJobRequestTypeDef

### maxJobDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### outputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef]

### loggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.LoggingConfigTypeDef]

### iamRole
- **Type**: typing.Optional[str]

### failureBehavior
- **Type**: typing.Optional[typing.Literal['Continue', 'Fail']]

### useDefaultApplications
- **Type**: typing.Optional[bool]

### robotApplications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigUnionTypeDef]]

### simulationApplications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigUnionTypeDef]]

### dataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.DataSourceConfigUnionTypeDef]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.VPCConfigUnionTypeDef]

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.ComputeTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SimulationJobRequestUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SimulationJobSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Completed', 'Failed', 'Pending', 'Preparing', 'Restarting', 'Running', 'RunningFailed', 'Terminated', 'Terminating']]

### simulationApplicationNames
- **Type**: typing.Optional[typing.List[str]]

### robotApplicationNames
- **Type**: typing.Optional[typing.List[str]]

### dataSourceNames
- **Type**: typing.Optional[typing.List[str]]

### computeType
- **Type**: typing.Optional[typing.Literal['CPU', 'GPU_AND_CPU']]


# SimulationJobTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Completed', 'Failed', 'Pending', 'Preparing', 'Restarting', 'Running', 'RunningFailed', 'Terminated', 'Terminating']]

### lastStartedAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### failureBehavior
- **Type**: typing.Optional[typing.Literal['Continue', 'Fail']]

### failureCode
- **Type**: typing.Optional[typing.Literal['BadPermissionsCloudwatchLogs', 'BadPermissionsRobotApplication', 'BadPermissionsS3Object', 'BadPermissionsS3Output', 'BadPermissionsSimulationApplication', 'BadPermissionsUserCredentials', 'BatchCanceled', 'BatchTimedOut', 'ENILimitExceeded', 'InternalServiceError', 'InvalidBundleRobotApplication', 'InvalidBundleSimulationApplication', 'InvalidInput', 'InvalidS3Resource', 'LimitExceeded', 'MismatchedEtag', 'RequestThrottled', 'ResourceNotFound', 'RobotApplicationCrash', 'RobotApplicationHealthCheckFailure', 'RobotApplicationVersionMismatchedEtag', 'SimulationApplicationCrash', 'SimulationApplicationHealthCheckFailure', 'SimulationApplicationVersionMismatchedEtag', 'SubnetIpLimitExceeded', 'ThrottlingError', 'UploadContentMismatchError', 'WrongRegionRobotApplication', 'WrongRegionS3Bucket', 'WrongRegionS3Output', 'WrongRegionSimulationApplication']]

### failureReason
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]

### outputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef]

### loggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.LoggingConfigTypeDef]

### maxJobDurationInSeconds
- **Type**: typing.Optional[int]

### simulationTimeMillis
- **Type**: typing.Optional[int]

### iamRole
- **Type**: typing.Optional[str]

### robotApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigOutputTypeDef]]

### simulationApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigOutputTypeDef]]

### dataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DataSourceTypeDef]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.VPCConfigResponseTypeDef]

### networkInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.NetworkInterfaceTypeDef]

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.ComputeResponseTypeDef]


# SimulationSoftwareSuiteTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Gazebo', 'RosbagPlay', 'SimulationRuntime']]

### version
- **Type**: typing.Optional[str]


# SourceConfigTypeDef

### s3Bucket
- **Type**: typing.Optional[str]

### s3Key
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'ARMHF', 'X86_64']]


# SourceTypeDef

### s3Bucket
- **Type**: typing.Optional[str]

### s3Key
- **Type**: typing.Optional[str]

### etag
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'ARMHF', 'X86_64']]


# StartSimulationJobBatchRequestTypeDef

### createSimulationJobRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobRequestUnionTypeDef]
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### batchPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.BatchPolicyTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartSimulationJobBatchResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Canceling', 'Completed', 'Completing', 'Failed', 'InProgress', 'Pending', 'TimedOut', 'TimingOut']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### batchPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.BatchPolicyTypeDef'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['InternalServiceError']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.FailedCreateSimulationJobRequestTypeDef]
- **Required**: Yes

### pendingRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobRequestOutputTypeDef]
- **Required**: Yes

### createdRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobSummaryTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SyncDeploymentJobRequestTypeDef

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### fleet
- **Type**: <class 'str'>
- **Required**: Yes


# SyncDeploymentJobResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Canceled', 'Failed', 'InProgress', 'Pending', 'Preparing', 'Succeeded']
- **Required**: Yes

### deploymentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.DeploymentConfigTypeDef'>
- **Required**: Yes

### deploymentApplicationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigOutputTypeDef]
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['BadLambdaAssociated', 'BadPermissionError', 'DeploymentFleetDoesNotExist', 'DownloadConditionFailed', 'EnvironmentSetupError', 'EtagMismatch', 'ExtractingBundleFailure', 'FailureThresholdBreached', 'FleetDeploymentTimeout', 'GreengrassDeploymentFailed', 'GreengrassGroupVersionDoesNotExist', 'InternalServerError', 'InvalidGreengrassGroup', 'LambdaDeleted', 'MissingRobotApplicationArchitecture', 'MissingRobotArchitecture', 'MissingRobotDeploymentResource', 'PostLaunchFileFailure', 'PreLaunchFileFailure', 'ResourceNotFound', 'RobotAgentConnectionTimeout', 'RobotApplicationDoesNotExist', 'RobotDeploymentAborted', 'RobotDeploymentNoResponse']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateLocationTypeDef

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Key
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# ToolTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### command
- **Type**: <class 'str'>
- **Required**: Yes

### streamUI
- **Type**: typing.Optional[bool]

### streamOutputToCloudWatch
- **Type**: typing.Optional[bool]

### exitBehavior
- **Type**: typing.Optional[typing.Literal['FAIL', 'RESTART']]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateRobotApplicationRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.SourceConfigTypeDef]]

### currentRevisionId
- **Type**: typing.Optional[str]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef]


# UpdateRobotApplicationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SourceTypeDef]
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSimulationApplicationRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.SimulationSoftwareSuiteTypeDef'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.SourceConfigTypeDef]]

### renderingEngine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.RenderingEngineTypeDef]

### currentRevisionId
- **Type**: typing.Optional[str]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef]


# UpdateSimulationApplicationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SourceTypeDef]
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.SimulationSoftwareSuiteTypeDef'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RobotSoftwareSuiteTypeDef'>
- **Required**: Yes

### renderingEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.RenderingEngineTypeDef'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorldTemplateRequestTypeDef

### template
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### templateBody
- **Type**: typing.Optional[str]

### templateLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.TemplateLocationTypeDef]


# UpdateWorldTemplateResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UploadConfigurationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### path
- **Type**: <class 'str'>
- **Required**: Yes

### uploadBehavior
- **Type**: typing.Literal['UPLOAD_ON_TERMINATE', 'UPLOAD_ROLLING_AUTO_REMOVE']
- **Required**: Yes


# VPCConfigOutputTypeDef

### subnets
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### assignPublicIp
- **Type**: typing.Optional[bool]


# VPCConfigResponseTypeDef

### subnets
- **Type**: typing.Optional[typing.List[str]]

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]

### assignPublicIp
- **Type**: typing.Optional[bool]


# VPCConfigTypeDef

### subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### assignPublicIp
- **Type**: typing.Optional[bool]


# VPCConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorldConfigTypeDef

### world
- **Type**: typing.Optional[str]


# WorldCountTypeDef

### floorplanCount
- **Type**: typing.Optional[int]

### interiorCountPerFloorplan
- **Type**: typing.Optional[int]


# WorldExportJobSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Canceling', 'Completed', 'Failed', 'Pending', 'Running']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### worlds
- **Type**: typing.Optional[typing.List[str]]

### outputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.OutputLocationTypeDef]


# WorldFailureTypeDef

### failureCode
- **Type**: typing.Optional[typing.Literal['AllWorldGenerationFailed', 'InternalServiceError', 'InvalidInput', 'LimitExceeded', 'RequestThrottled', 'ResourceNotFound']]

### sampleFailureReason
- **Type**: typing.Optional[str]

### failureCount
- **Type**: typing.Optional[int]


# WorldGenerationJobSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### template
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Canceling', 'Completed', 'Failed', 'PartialFailed', 'Pending', 'Running']]

### worldCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.WorldCountTypeDef]

### succeededWorldCount
- **Type**: typing.Optional[int]

### failedWorldCount
- **Type**: typing.Optional[int]


# WorldSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### generationJob
- **Type**: typing.Optional[str]

### template
- **Type**: typing.Optional[str]



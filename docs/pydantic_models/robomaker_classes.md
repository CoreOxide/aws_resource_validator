# robomaker_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteWorldsRequestRequestTypeDef

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


# BatchDescribeSimulationJobRequestRequestTypeDef

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


# CancelDeploymentJobRequestRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSimulationJobBatchRequestRequestTypeDef

### batch
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSimulationJobRequestRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# CancelWorldExportJobRequestRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# CancelWorldGenerationJobRequestRequestTypeDef

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


# CreateDeploymentJobRequestRequestTypeDef

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentApplicationConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigTypeDef]
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


# CreateFleetRequestRequestTypeDef

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


# CreateRobotApplicationRequestRequestTypeDef

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


# CreateRobotApplicationVersionRequestRequestTypeDef

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


# CreateRobotRequestRequestTypeDef

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


# CreateSimulationApplicationRequestRequestTypeDef

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


# CreateSimulationApplicationVersionRequestRequestTypeDef

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


# CreateSimulationJobRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigTypeDef]]

### simulationApplications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigTypeDef]]

### dataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.DataSourceConfigTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.VPCConfigTypeDef]

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigTypeDef]
- **Required**: Yes

### simulationApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigTypeDef]
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


# CreateWorldExportJobRequestRequestTypeDef

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


# CreateWorldGenerationJobRequestRequestTypeDef

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


# CreateWorldTemplateRequestRequestTypeDef

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


# DataSourceConfigTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Keys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['Archive', 'File', 'Prefix']]

### destination
- **Type**: typing.Optional[str]


# DataSourceTypeDef

### name
- **Type**: typing.Optional[str]

### s3Bucket
- **Type**: typing.Optional[str]

### s3Keys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.S3KeyOutputTypeDef]]

### type
- **Type**: typing.Optional[typing.Literal['Archive', 'File', 'Prefix']]

### destination
- **Type**: typing.Optional[str]


# DeleteFleetRequestRequestTypeDef

### fleet
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRobotApplicationRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DeleteRobotRequestRequestTypeDef

### robot
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSimulationApplicationRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DeleteWorldTemplateRequestRequestTypeDef

### template
- **Type**: <class 'str'>
- **Required**: Yes


# DeploymentApplicationConfigPaginatorTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.DeploymentLaunchConfigPaginatorTypeDef'>
- **Required**: Yes


# DeploymentApplicationConfigTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.DeploymentLaunchConfigTypeDef'>
- **Required**: Yes


# DeploymentConfigTypeDef

### concurrentDeploymentPercentage
- **Type**: typing.Optional[int]

### failureThresholdPercentage
- **Type**: typing.Optional[int]

### robotDeploymentTimeoutInSeconds
- **Type**: typing.Optional[int]

### downloadConditionFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.S3ObjectTypeDef]


# DeploymentJobPaginatorTypeDef

### arn
- **Type**: typing.Optional[str]

### fleet
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Failed', 'InProgress', 'Pending', 'Preparing', 'Succeeded']]

### deploymentApplicationConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigPaginatorTypeDef]]

### deploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentConfigTypeDef]

### failureReason
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['BadLambdaAssociated', 'BadPermissionError', 'DeploymentFleetDoesNotExist', 'DownloadConditionFailed', 'EnvironmentSetupError', 'EtagMismatch', 'ExtractingBundleFailure', 'FailureThresholdBreached', 'FleetDeploymentTimeout', 'GreengrassDeploymentFailed', 'GreengrassGroupVersionDoesNotExist', 'InternalServerError', 'InvalidGreengrassGroup', 'LambdaDeleted', 'MissingRobotApplicationArchitecture', 'MissingRobotArchitecture', 'MissingRobotDeploymentResource', 'PostLaunchFileFailure', 'PreLaunchFileFailure', 'ResourceNotFound', 'RobotAgentConnectionTimeout', 'RobotApplicationDoesNotExist', 'RobotDeploymentAborted', 'RobotDeploymentNoResponse']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# DeploymentJobTypeDef

### arn
- **Type**: typing.Optional[str]

### fleet
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Failed', 'InProgress', 'Pending', 'Preparing', 'Succeeded']]

### deploymentApplicationConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigTypeDef]]

### deploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentConfigTypeDef]

### failureReason
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['BadLambdaAssociated', 'BadPermissionError', 'DeploymentFleetDoesNotExist', 'DownloadConditionFailed', 'EnvironmentSetupError', 'EtagMismatch', 'ExtractingBundleFailure', 'FailureThresholdBreached', 'FleetDeploymentTimeout', 'GreengrassDeploymentFailed', 'GreengrassGroupVersionDoesNotExist', 'InternalServerError', 'InvalidGreengrassGroup', 'LambdaDeleted', 'MissingRobotApplicationArchitecture', 'MissingRobotArchitecture', 'MissingRobotDeploymentResource', 'PostLaunchFileFailure', 'PreLaunchFileFailure', 'ResourceNotFound', 'RobotAgentConnectionTimeout', 'RobotApplicationDoesNotExist', 'RobotDeploymentAborted', 'RobotDeploymentNoResponse']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# DeploymentLaunchConfigPaginatorTypeDef

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


# DeregisterRobotRequestRequestTypeDef

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


# DescribeDeploymentJobRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigTypeDef]
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


# DescribeFleetRequestRequestTypeDef

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


# DescribeRobotApplicationRequestRequestTypeDef

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


# DescribeRobotRequestRequestTypeDef

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


# DescribeSimulationApplicationRequestRequestTypeDef

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


# DescribeSimulationJobBatchRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobRequestTypeDef]
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


# DescribeSimulationJobRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigTypeDef]
- **Required**: Yes

### simulationApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigTypeDef]
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


# DescribeWorldExportJobRequestRequestTypeDef

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


# DescribeWorldGenerationJobRequestRequestTypeDef

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


# DescribeWorldRequestRequestTypeDef

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


# DescribeWorldTemplateRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobRequestTypeDef]

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


# GetWorldTemplateBodyRequestRequestTypeDef

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


# LaunchConfigTypeDef

### packageName
- **Type**: typing.Optional[str]

### launchFile
- **Type**: typing.Optional[str]

### environmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### portForwardingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PortForwardingConfigTypeDef]

### streamUI
- **Type**: typing.Optional[bool]

### command
- **Type**: typing.Optional[typing.List[str]]


# ListDeploymentJobsRequestListDeploymentJobsPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListDeploymentJobsRequestRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDeploymentJobsResponsePaginatorTypeDef

### deploymentJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentJobPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeploymentJobsResponseTypeDef

### deploymentJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentJobTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFleetsRequestListFleetsPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListFleetsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRobotApplicationsRequestListRobotApplicationsPaginateTypeDef

### versionQualifier
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListRobotApplicationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRobotsRequestListRobotsPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListRobotsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSimulationApplicationsRequestListSimulationApplicationsPaginateTypeDef

### versionQualifier
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListSimulationApplicationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSimulationJobBatchesRequestListSimulationJobBatchesPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListSimulationJobBatchesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSimulationJobsRequestListSimulationJobsPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListSimulationJobsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorldExportJobsRequestListWorldExportJobsPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListWorldExportJobsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorldGenerationJobsRequestListWorldGenerationJobsPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListWorldGenerationJobsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorldTemplatesRequestListWorldTemplatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListWorldTemplatesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorldTemplatesResponseTypeDef

### templateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.TemplateSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorldsRequestListWorldsPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.PaginatorConfigTypeDef]


# ListWorldsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# PortForwardingConfigTypeDef

### portMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.PortMappingTypeDef]]


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


# RegisterRobotRequestRequestTypeDef

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


# RestartSimulationJobRequestRequestTypeDef

### job
- **Type**: <class 'str'>
- **Required**: Yes


# RobotApplicationConfigTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.LaunchConfigTypeDef'>
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


# SimulationApplicationConfigTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker_classes.LaunchConfigTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigTypeDef]]

### simulationApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigTypeDef]]

### dataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DataSourceConfigTypeDef]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.VPCConfigTypeDef]

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker_classes.ComputeTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.RobotApplicationConfigTypeDef]]

### simulationApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationApplicationConfigTypeDef]]

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


# StartSimulationJobBatchRequestRequestTypeDef

### createSimulationJobRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobRequestTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.SimulationJobRequestTypeDef]
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


# SyncDeploymentJobRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker_classes.DeploymentApplicationConfigTypeDef]
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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateRobotApplicationRequestRequestTypeDef

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


# UpdateSimulationApplicationRequestRequestTypeDef

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


# UpdateWorldTemplateRequestRequestTypeDef

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



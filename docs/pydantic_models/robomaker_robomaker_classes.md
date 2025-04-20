# Robomaker Robomaker Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteWorldsRequest

### worlds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteWorldsResponse

### unprocessedWorlds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDescribeSimulationJobRequest

### jobs
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDescribeSimulationJobResponse

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJob]
- **Required**: Yes

### unprocessedJobs
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPolicy

### timeoutInSeconds
- **Type**: typing.Optional[int]

### maxConcurrency
- **Type**: typing.Optional[int]


# CancelDeploymentJobRequest

### job
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSimulationJobBatchRequest

### batch
- **Type**: <class 'str'>
- **Required**: Yes


# CancelSimulationJobRequest

### job
- **Type**: <class 'str'>
- **Required**: Yes


# CancelWorldExportJobRequest

### job
- **Type**: <class 'str'>
- **Required**: Yes


# CancelWorldGenerationJobRequest

### job
- **Type**: <class 'str'>
- **Required**: Yes


# Compute

### simulationUnitLimit
- **Type**: typing.Optional[int]

### computeType
- **Type**: typing.Optional[typing.Literal['CPU', 'GPU_AND_CPU']]

### gpuUnitLimit
- **Type**: typing.Optional[int]


# ComputeResponse

### simulationUnitLimit
- **Type**: typing.Optional[int]

### computeType
- **Type**: typing.Optional[typing.Literal['CPU', 'GPU_AND_CPU']]

### gpuUnitLimit
- **Type**: typing.Optional[int]


# CreateDeploymentJobRequest

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentApplicationConfigs
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentApplicationConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentApplicationConfigOutput]]
- **Required**: Yes

### deploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentConfig]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDeploymentJobResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentApplicationConfigOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentConfig'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFleetRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateFleetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRobotApplicationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SourceConfig]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment]


# CreateRobotApplicationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Source]
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRobotApplicationVersionRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### currentRevisionId
- **Type**: typing.Optional[str]

### s3Etags
- **Type**: typing.Optional[typing.List[str]]

### imageDigest
- **Type**: typing.Optional[str]


# CreateRobotApplicationVersionResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Source]
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRobotRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRobotResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSimulationApplicationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationSoftwareSuite'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SourceConfig]]

### renderingEngine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RenderingEngine]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment]


# CreateSimulationApplicationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Source]
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationSoftwareSuite'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### renderingEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RenderingEngine'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSimulationApplicationVersionRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### currentRevisionId
- **Type**: typing.Optional[str]

### s3Etags
- **Type**: typing.Optional[typing.List[str]]

### imageDigest
- **Type**: typing.Optional[str]


# CreateSimulationApplicationVersionResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Source]
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationSoftwareSuite'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### renderingEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RenderingEngine'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSimulationJobRequest

### maxJobDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### outputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation]

### loggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LoggingConfig]

### failureBehavior
- **Type**: typing.Optional[typing.Literal['Continue', 'Fail']]

### robotApplications
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotApplicationConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotApplicationConfigOutput]]]

### simulationApplications
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationApplicationConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationApplicationConfigOutput]]]

### dataSources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DataSourceConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DataSourceConfigOutput]]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.VPCConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.VPCConfigOutput, NoneType]

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Compute]


# CreateSimulationJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation'>
- **Required**: Yes

### loggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LoggingConfig'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotApplicationConfigOutput]
- **Required**: Yes

### simulationApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationApplicationConfigOutput]
- **Required**: Yes

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DataSource]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### vpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.VPCConfigResponse'>
- **Required**: Yes

### compute
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ComputeResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorldExportJobRequest

### worlds
- **Type**: typing.List[str]
- **Required**: Yes

### outputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateWorldExportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorldGenerationJobRequest

### template
- **Type**: <class 'str'>
- **Required**: Yes

### worldCount
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldCount'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### worldTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateWorldGenerationJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldCount'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### worldTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorldTemplateRequest

### clientRequestToken
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### templateBody
- **Type**: typing.Optional[str]

### templateLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.TemplateLocation]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateWorldTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DataSource

### name
- **Type**: typing.Optional[str]

### s3Bucket
- **Type**: typing.Optional[str]

### s3Keys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.S3KeyOutput]]

### type
- **Type**: typing.Optional[typing.Literal['Archive', 'File', 'Prefix']]

### destination
- **Type**: typing.Optional[str]


# DataSourceConfig

### name
- **Type**: <class 'str'>
- **Required**: Yes

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Keys
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['Archive', 'File', 'Prefix']]

### destination
- **Type**: typing.Optional[str]


# DataSourceConfigOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Keys
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['Archive', 'File', 'Prefix']]

### destination
- **Type**: typing.Optional[str]


# DeleteFleetRequest

### fleet
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRobotApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DeleteRobotRequest

### robot
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSimulationApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DeleteWorldTemplateRequest

### template
- **Type**: <class 'str'>
- **Required**: Yes


# DeploymentApplicationConfig

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentLaunchConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentLaunchConfigOutput]
- **Required**: Yes


# DeploymentApplicationConfigOutput

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentLaunchConfigOutput'>
- **Required**: Yes


# DeploymentConfig

### concurrentDeploymentPercentage
- **Type**: typing.Optional[int]

### failureThresholdPercentage
- **Type**: typing.Optional[int]

### robotDeploymentTimeoutInSeconds
- **Type**: typing.Optional[int]

### downloadConditionFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.S3Object]


# DeploymentJob

### arn
- **Type**: typing.Optional[str]

### fleet
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Failed', 'InProgress', 'Pending', 'Preparing', 'Succeeded']]

### deploymentApplicationConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentApplicationConfigOutput]]

### deploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentConfig]

### failureReason
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['BadLambdaAssociated', 'BadPermissionError', 'DeploymentFleetDoesNotExist', 'DownloadConditionFailed', 'EnvironmentSetupError', 'EtagMismatch', 'ExtractingBundleFailure', 'FailureThresholdBreached', 'FleetDeploymentTimeout', 'GreengrassDeploymentFailed', 'GreengrassGroupVersionDoesNotExist', 'InternalServerError', 'InvalidGreengrassGroup', 'LambdaDeleted', 'MissingRobotApplicationArchitecture', 'MissingRobotArchitecture', 'MissingRobotDeploymentResource', 'PostLaunchFileFailure', 'PreLaunchFileFailure', 'ResourceNotFound', 'RobotAgentConnectionTimeout', 'RobotApplicationDoesNotExist', 'RobotDeploymentAborted', 'RobotDeploymentNoResponse']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# DeploymentLaunchConfig

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


# DeploymentLaunchConfigOutput

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


# DeregisterRobotRequest

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### robot
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterRobotResponse

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### robot
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDeploymentJobRequest

### job
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeploymentJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentConfig'>
- **Required**: Yes

### deploymentApplicationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentApplicationConfigOutput]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotDeployment]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFleetRequest

### fleet
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFleetResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### robots
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Robot]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRobotApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DescribeRobotApplicationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Source]
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment'>
- **Required**: Yes

### imageDigest
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRobotRequest

### robot
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRobotResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSimulationApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]


# DescribeSimulationApplicationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Source]
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationSoftwareSuite'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### renderingEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RenderingEngine'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment'>
- **Required**: Yes

### imageDigest
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSimulationJobBatchRequest

### batch
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSimulationJobBatchResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.BatchPolicy'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['InternalServiceError']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.FailedCreateSimulationJobRequest]
- **Required**: Yes

### pendingRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJobRequestOutput]
- **Required**: Yes

### createdRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJobSummary]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSimulationJobRequest

### job
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSimulationJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation'>
- **Required**: Yes

### loggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LoggingConfig'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotApplicationConfigOutput]
- **Required**: Yes

### simulationApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationApplicationConfigOutput]
- **Required**: Yes

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DataSource]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### vpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.VPCConfigResponse'>
- **Required**: Yes

### networkInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.NetworkInterface'>
- **Required**: Yes

### compute
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ComputeResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorldExportJobRequest

### job
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorldExportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation'>
- **Required**: Yes

### iamRole
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorldGenerationJobRequest

### job
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorldGenerationJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldCount'>
- **Required**: Yes

### finishedWorldsSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.FinishedWorldsSummary'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### worldTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorldRequest

### world
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorldResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorldTemplateRequest

### template
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorldTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# Environment

### uri
- **Type**: typing.Optional[str]


# FailedCreateSimulationJobRequest

### request
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJobRequestOutput]

### failureReason
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['BadPermissionsCloudwatchLogs', 'BadPermissionsRobotApplication', 'BadPermissionsS3Object', 'BadPermissionsS3Output', 'BadPermissionsSimulationApplication', 'BadPermissionsUserCredentials', 'BatchCanceled', 'BatchTimedOut', 'ENILimitExceeded', 'InternalServiceError', 'InvalidBundleRobotApplication', 'InvalidBundleSimulationApplication', 'InvalidInput', 'InvalidS3Resource', 'LimitExceeded', 'MismatchedEtag', 'RequestThrottled', 'ResourceNotFound', 'RobotApplicationCrash', 'RobotApplicationHealthCheckFailure', 'RobotApplicationVersionMismatchedEtag', 'SimulationApplicationCrash', 'SimulationApplicationHealthCheckFailure', 'SimulationApplicationVersionMismatchedEtag', 'SubnetIpLimitExceeded', 'ThrottlingError', 'UploadContentMismatchError', 'WrongRegionRobotApplication', 'WrongRegionS3Bucket', 'WrongRegionS3Output', 'WrongRegionSimulationApplication']]

### failedAt
- **Type**: typing.Optional[datetime.datetime]


# FailureSummary

### totalFailureCount
- **Type**: typing.Optional[int]

### failures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldFailure]]


# Filter

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# FinishedWorldsSummary

### finishedCount
- **Type**: typing.Optional[int]

### succeededWorlds
- **Type**: typing.Optional[typing.List[str]]

### failureSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.FailureSummary]


# Fleet

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


# GetWorldTemplateBodyRequest

### template
- **Type**: typing.Optional[str]

### generationJob
- **Type**: typing.Optional[str]


# GetWorldTemplateBodyResponse

### templateBody
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# LaunchConfig

### packageName
- **Type**: typing.Optional[str]

### launchFile
- **Type**: typing.Optional[str]

### environmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### portForwardingConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PortForwardingConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PortForwardingConfigOutput, NoneType]

### streamUI
- **Type**: typing.Optional[bool]

### command
- **Type**: typing.Optional[typing.List[str]]


# LaunchConfigOutput

### packageName
- **Type**: typing.Optional[str]

### launchFile
- **Type**: typing.Optional[str]

### environmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### portForwardingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PortForwardingConfigOutput]

### streamUI
- **Type**: typing.Optional[bool]

### command
- **Type**: typing.Optional[typing.List[str]]


# ListDeploymentJobsRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDeploymentJobsRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListDeploymentJobsResponse

### deploymentJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]


# ListFleetsRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListFleetsResponse

### fleetDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Fleet]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRobotApplicationsRequest

### versionQualifier
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]


# ListRobotApplicationsRequestPaginate

### versionQualifier
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListRobotApplicationsResponse

### robotApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRobotsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]


# ListRobotsRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListRobotsResponse

### robots
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Robot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSimulationApplicationsRequest

### versionQualifier
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]


# ListSimulationApplicationsRequestPaginate

### versionQualifier
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListSimulationApplicationsResponse

### simulationApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSimulationJobBatchesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]


# ListSimulationJobBatchesRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListSimulationJobBatchesResponse

### simulationJobBatchSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJobBatchSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSimulationJobsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]


# ListSimulationJobsRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListSimulationJobsResponse

### simulationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# ListWorldExportJobsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]


# ListWorldExportJobsRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListWorldExportJobsResponse

### worldExportJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldExportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorldGenerationJobsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]


# ListWorldGenerationJobsRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListWorldGenerationJobsResponse

### worldGenerationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldGenerationJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorldTemplatesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorldTemplatesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListWorldTemplatesResponse

### templateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.TemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorldsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]


# ListWorldsRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PaginatorConfig]


# ListWorldsResponse

### worldSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LoggingConfig

### recordAllRosTopics
- **Type**: typing.Optional[bool]


# NetworkInterface

### networkInterfaceId
- **Type**: typing.Optional[str]

### privateIpAddress
- **Type**: typing.Optional[str]

### publicIpAddress
- **Type**: typing.Optional[str]


# OutputLocation

### s3Bucket
- **Type**: typing.Optional[str]

### s3Prefix
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortForwardingConfig

### portMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PortMapping]]


# PortForwardingConfigOutput

### portMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.PortMapping]]


# PortMapping

### jobPort
- **Type**: <class 'int'>
- **Required**: Yes

### applicationPort
- **Type**: <class 'int'>
- **Required**: Yes

### enableOnPublicIp
- **Type**: typing.Optional[bool]


# ProgressDetail

### currentProgress
- **Type**: typing.Optional[typing.Literal['DownloadingExtracting', 'ExecutingDownloadCondition', 'ExecutingPostLaunch', 'ExecutingPreLaunch', 'Finished', 'Launching', 'Validating']]

### percentDone
- **Type**: typing.Optional[float]

### estimatedTimeRemainingSeconds
- **Type**: typing.Optional[int]

### targetResource
- **Type**: typing.Optional[str]


# RegisterRobotRequest

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### robot
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterRobotResponse

### fleet
- **Type**: <class 'str'>
- **Required**: Yes

### robot
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# RenderingEngine

### name
- **Type**: typing.Optional[typing.Literal['OGRE']]

### version
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


# RestartSimulationJobRequest

### job
- **Type**: <class 'str'>
- **Required**: Yes


# Robot

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


# RobotApplicationConfig

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LaunchConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LaunchConfigOutput]
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]

### uploadConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.UploadConfiguration]]

### useDefaultUploadConfigurations
- **Type**: typing.Optional[bool]

### tools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Tool]]

### useDefaultTools
- **Type**: typing.Optional[bool]


# RobotApplicationConfigOutput

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LaunchConfigOutput'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]

### uploadConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.UploadConfiguration]]

### useDefaultUploadConfigurations
- **Type**: typing.Optional[bool]

### tools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Tool]]

### useDefaultTools
- **Type**: typing.Optional[bool]


# RobotApplicationSummary

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### robotSoftwareSuite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite]


# RobotDeployment

### arn
- **Type**: typing.Optional[str]

### deploymentStartTime
- **Type**: typing.Optional[datetime.datetime]

### deploymentFinishTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Available', 'Deploying', 'Failed', 'InSync', 'NoResponse', 'PendingNewDeployment', 'Registered']]

### progressDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ProgressDetail]

### failureReason
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['BadLambdaAssociated', 'BadPermissionError', 'DeploymentFleetDoesNotExist', 'DownloadConditionFailed', 'EnvironmentSetupError', 'EtagMismatch', 'ExtractingBundleFailure', 'FailureThresholdBreached', 'FleetDeploymentTimeout', 'GreengrassDeploymentFailed', 'GreengrassGroupVersionDoesNotExist', 'InternalServerError', 'InvalidGreengrassGroup', 'LambdaDeleted', 'MissingRobotApplicationArchitecture', 'MissingRobotArchitecture', 'MissingRobotDeploymentResource', 'PostLaunchFileFailure', 'PreLaunchFileFailure', 'ResourceNotFound', 'RobotAgentConnectionTimeout', 'RobotApplicationDoesNotExist', 'RobotDeploymentAborted', 'RobotDeploymentNoResponse']]


# RobotSoftwareSuite

### name
- **Type**: typing.Optional[typing.Literal['General', 'ROS', 'ROS2']]

### version
- **Type**: typing.Optional[typing.Literal['Dashing', 'Foxy', 'Kinetic', 'Melodic']]


# S3KeyOutput

### s3Key
- **Type**: typing.Optional[str]

### etag
- **Type**: typing.Optional[str]


# S3Object

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### etag
- **Type**: typing.Optional[str]


# SimulationApplicationConfig

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LaunchConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LaunchConfigOutput]
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]

### uploadConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.UploadConfiguration]]

### worldConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldConfig]]

### useDefaultUploadConfigurations
- **Type**: typing.Optional[bool]

### tools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Tool]]

### useDefaultTools
- **Type**: typing.Optional[bool]


# SimulationApplicationConfigOutput

### application
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LaunchConfigOutput'>
- **Required**: Yes

### applicationVersion
- **Type**: typing.Optional[str]

### uploadConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.UploadConfiguration]]

### worldConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldConfig]]

### useDefaultUploadConfigurations
- **Type**: typing.Optional[bool]

### tools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Tool]]

### useDefaultTools
- **Type**: typing.Optional[bool]


# SimulationApplicationSummary

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### robotSoftwareSuite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite]

### simulationSoftwareSuite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationSoftwareSuite]


# SimulationJob

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation]

### loggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LoggingConfig]

### maxJobDurationInSeconds
- **Type**: typing.Optional[int]

### simulationTimeMillis
- **Type**: typing.Optional[int]

### iamRole
- **Type**: typing.Optional[str]

### robotApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotApplicationConfigOutput]]

### simulationApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationApplicationConfigOutput]]

### dataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DataSource]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.VPCConfigResponse]

### networkInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.NetworkInterface]

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ComputeResponse]


# SimulationJobBatchSummary

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


# SimulationJobRequest

### maxJobDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### outputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation]

### loggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LoggingConfig]

### iamRole
- **Type**: typing.Optional[str]

### failureBehavior
- **Type**: typing.Optional[typing.Literal['Continue', 'Fail']]

### useDefaultApplications
- **Type**: typing.Optional[bool]

### robotApplications
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotApplicationConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotApplicationConfigOutput]]]

### simulationApplications
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationApplicationConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationApplicationConfigOutput]]]

### dataSources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DataSourceConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DataSourceConfigOutput]]]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.VPCConfig, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.VPCConfigOutput, NoneType]

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Compute]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SimulationJobRequestOutput

### maxJobDurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### outputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation]

### loggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.LoggingConfig]

### iamRole
- **Type**: typing.Optional[str]

### failureBehavior
- **Type**: typing.Optional[typing.Literal['Continue', 'Fail']]

### useDefaultApplications
- **Type**: typing.Optional[bool]

### robotApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotApplicationConfigOutput]]

### simulationApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationApplicationConfigOutput]]

### dataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DataSourceConfigOutput]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.VPCConfigOutput]

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Compute]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SimulationJobSummary

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


# SimulationSoftwareSuite

### name
- **Type**: typing.Optional[typing.Literal['Gazebo', 'RosbagPlay', 'SimulationRuntime']]

### version
- **Type**: typing.Optional[str]


# Source

### s3Bucket
- **Type**: typing.Optional[str]

### s3Key
- **Type**: typing.Optional[str]

### etag
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'ARMHF', 'X86_64']]


# SourceConfig

### s3Bucket
- **Type**: typing.Optional[str]

### s3Key
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'ARMHF', 'X86_64']]


# StartSimulationJobBatchRequest

### createSimulationJobRequests
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJobRequest, aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJobRequestOutput]]
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### batchPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.BatchPolicy]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartSimulationJobBatchResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.BatchPolicy'>
- **Required**: Yes

### failureCode
- **Type**: typing.Literal['InternalServiceError']
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.FailedCreateSimulationJobRequest]
- **Required**: Yes

### pendingRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJobRequestOutput]
- **Required**: Yes

### createdRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationJobSummary]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# SyncDeploymentJobRequest

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### fleet
- **Type**: <class 'str'>
- **Required**: Yes


# SyncDeploymentJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentConfig'>
- **Required**: Yes

### deploymentApplicationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.DeploymentApplicationConfigOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TemplateLocation

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Key
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateSummary

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


# Tool

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


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateRobotApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SourceConfig]]

### currentRevisionId
- **Type**: typing.Optional[str]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment]


# UpdateRobotApplicationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Source]
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSimulationApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationSoftwareSuite'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SourceConfig]]

### renderingEngine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RenderingEngine]

### currentRevisionId
- **Type**: typing.Optional[str]

### environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment]


# UpdateSimulationApplicationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Source]
- **Required**: Yes

### simulationSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.SimulationSoftwareSuite'>
- **Required**: Yes

### robotSoftwareSuite
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RobotSoftwareSuite'>
- **Required**: Yes

### renderingEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.RenderingEngine'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### environment
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorldTemplateRequest

### template
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### templateBody
- **Type**: typing.Optional[str]

### templateLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.TemplateLocation]


# UpdateWorldTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.robomaker.robomaker_classes.ResponseMetadata'>
- **Required**: Yes


# UploadConfiguration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### path
- **Type**: <class 'str'>
- **Required**: Yes

### uploadBehavior
- **Type**: typing.Literal['UPLOAD_ON_TERMINATE', 'UPLOAD_ROLLING_AUTO_REMOVE']
- **Required**: Yes


# VPCConfig

### subnets
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### assignPublicIp
- **Type**: typing.Optional[bool]


# VPCConfigOutput

### subnets
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### assignPublicIp
- **Type**: typing.Optional[bool]


# VPCConfigResponse

### subnets
- **Type**: typing.Optional[typing.List[str]]

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]

### assignPublicIp
- **Type**: typing.Optional[bool]


# WorldConfig

### world
- **Type**: typing.Optional[str]


# WorldCount

### floorplanCount
- **Type**: typing.Optional[int]

### interiorCountPerFloorplan
- **Type**: typing.Optional[int]


# WorldExportJobSummary

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Canceling', 'Completed', 'Failed', 'Pending', 'Running']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### worlds
- **Type**: typing.Optional[typing.List[str]]

### outputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.OutputLocation]


# WorldFailure

### failureCode
- **Type**: typing.Optional[typing.Literal['AllWorldGenerationFailed', 'InternalServiceError', 'InvalidInput', 'LimitExceeded', 'RequestThrottled', 'ResourceNotFound']]

### sampleFailureReason
- **Type**: typing.Optional[str]

### failureCount
- **Type**: typing.Optional[int]


# WorldGenerationJobSummary

### arn
- **Type**: typing.Optional[str]

### template
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Canceled', 'Canceling', 'Completed', 'Failed', 'PartialFailed', 'Pending', 'Running']]

### worldCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.robomaker.robomaker_classes.WorldCount]

### succeededWorldCount
- **Type**: typing.Optional[int]

### failedWorldCount
- **Type**: typing.Optional[int]


# WorldSummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### generationJob
- **Type**: typing.Optional[str]

### template
- **Type**: typing.Optional[str]



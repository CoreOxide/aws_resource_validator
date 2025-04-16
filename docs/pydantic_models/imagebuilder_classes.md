# Imagebuilder Classes

# AccountAggregation

### accountId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SeverityCounts]


# AdditionalInstanceConfiguration

### systemsManagerAgent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SystemsManagerAgent]

### userDataOverride
- **Type**: typing.Optional[str]


# Ami

### region
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageState]

### accountId
- **Type**: typing.Optional[str]


# AmiDistributionConfiguration

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### targetAccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### amiTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyId
- **Type**: typing.Optional[str]

### launchPermission
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchPermissionConfigurationUnion]


# AmiDistributionConfigurationOutput

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### targetAccountIds
- **Type**: typing.Optional[typing.List[str]]

### amiTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyId
- **Type**: typing.Optional[str]

### launchPermission
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchPermissionConfigurationOutput]


# AmiDistributionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelImageCreationRequest

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# CancelImageCreationResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CancelLifecycleExecutionRequest

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# CancelLifecycleExecutionResponse

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# Component

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentConfiguration

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentParameterUnion]]


# ComponentConfigurationOutput

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentParameterOutput]]


# ComponentConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentParameter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ComponentParameterOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.List[str]
- **Required**: Yes


# ComponentParameterUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentState

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEPRECATED', 'DISABLED']]

### reason
- **Type**: typing.Optional[str]


# ComponentSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentVersion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Container

### region
- **Type**: typing.Optional[str]

### imageUris
- **Type**: typing.Optional[typing.List[str]]


# ContainerDistributionConfiguration

### targetRepository
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.TargetContainerRepository'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### containerTags
- **Type**: typing.Optional[typing.Sequence[str]]


# ContainerDistributionConfigurationOutput

### targetRepository
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.TargetContainerRepository'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### containerTags
- **Type**: typing.Optional[typing.List[str]]


# ContainerDistributionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerRecipe

### arn
- **Type**: typing.Optional[str]

### containerType
- **Type**: typing.Optional[typing.Literal['DOCKER']]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows', 'macOS']]

### owner
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### components
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationOutput]]

### instanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceConfigurationOutput]

### dockerfileTemplateData
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### encrypted
- **Type**: typing.Optional[bool]

### parentImage
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### workingDirectory
- **Type**: typing.Optional[str]

### targetRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.TargetContainerRepository]


# ContainerRecipeSummary

### arn
- **Type**: typing.Optional[str]

### containerType
- **Type**: typing.Optional[typing.Literal['DOCKER']]

### name
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows', 'macOS']]

### owner
- **Type**: typing.Optional[str]

### parentImage
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateComponentRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### platform
- **Type**: typing.Literal['Linux', 'Windows', 'macOS']
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### changeDescription
- **Type**: typing.Optional[str]

### supportedOsVersions
- **Type**: typing.Optional[typing.Sequence[str]]

### data
- **Type**: typing.Optional[str]

### uri
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateComponentResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### componentBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContainerRecipeRequest

### containerType
- **Type**: typing.Literal['DOCKER']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### components
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationUnion]
- **Required**: Yes

### parentImage
- **Type**: <class 'str'>
- **Required**: Yes

### targetRepository
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.TargetContainerRepository'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### instanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceConfigurationUnion]

### dockerfileTemplateData
- **Type**: typing.Optional[str]

### dockerfileTemplateUri
- **Type**: typing.Optional[str]

### platformOverride
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows', 'macOS']]

### imageOsVersionOverride
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### workingDirectory
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]


# CreateContainerRecipeResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDistributionConfigurationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### distributions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionUnion]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDistributionConfigurationResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImagePipelineRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### imageRecipeArn
- **Type**: typing.Optional[str]

### containerRecipeArn
- **Type**: typing.Optional[str]

### distributionConfigurationArn
- **Type**: typing.Optional[str]

### imageTestsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTestsConfiguration]

### enhancedImageMetadataEnabled
- **Type**: typing.Optional[bool]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Schedule]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationUnion]

### workflows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationUnion]]

### executionRole
- **Type**: typing.Optional[str]


# CreateImagePipelineResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImageRecipeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### components
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationUnion]
- **Required**: Yes

### parentImage
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### blockDeviceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceBlockDeviceMapping]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### workingDirectory
- **Type**: typing.Optional[str]

### additionalInstanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AdditionalInstanceConfiguration]


# CreateImageRecipeResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImageRequest

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipeArn
- **Type**: typing.Optional[str]

### containerRecipeArn
- **Type**: typing.Optional[str]

### distributionConfigurationArn
- **Type**: typing.Optional[str]

### imageTestsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTestsConfiguration]

### enhancedImageMetadataEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationUnion]

### workflows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationUnion]]

### executionRole
- **Type**: typing.Optional[str]


# CreateImageResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInfrastructureConfigurationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### instanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### instanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetId
- **Type**: typing.Optional[str]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Logging]

### keyPair
- **Type**: typing.Optional[str]

### terminateInstanceOnFailure
- **Type**: typing.Optional[bool]

### snsTopicArn
- **Type**: typing.Optional[str]

### resourceTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### instanceMetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceMetadataOptions]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Placement]


# CreateInfrastructureConfigurationResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLifecyclePolicyRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### executionRole
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AMI_IMAGE', 'CONTAINER_IMAGE']
- **Required**: Yes

### policyDetails
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailUnion]
- **Required**: Yes

### resourceSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionUnion'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLifecyclePolicyResponse

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkflowResponse

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CvssScore

### baseScore
- **Type**: typing.Optional[float]

### scoringVector
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]


# CvssScoreAdjustment

### metric
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# CvssScoreDetails

### scoreSource
- **Type**: typing.Optional[str]

### cvssSource
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### score
- **Type**: typing.Optional[float]

### scoringVector
- **Type**: typing.Optional[str]

### adjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.CvssScoreAdjustment]]


# DeleteComponentRequest

### componentBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComponentResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### componentBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteContainerRecipeRequest

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerRecipeResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDistributionConfigurationRequest

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDistributionConfigurationResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteImagePipelineRequest

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImagePipelineResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteImageRecipeRequest

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageRecipeResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteImageRequest

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInfrastructureConfigurationRequest

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInfrastructureConfigurationResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLifecyclePolicyRequest

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLifecyclePolicyResponse

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkflowRequest

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowResponse

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# Distribution

### region
- **Type**: <class 'str'>
- **Required**: Yes

### amiDistributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AmiDistributionConfigurationUnion]

### containerDistributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerDistributionConfigurationUnion]

### licenseConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### launchTemplateConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchTemplateConfiguration]]

### s3ExportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.S3ExportConfiguration]

### fastLaunchConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FastLaunchConfiguration]]


# DistributionConfiguration

### timeoutMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### distributions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionOutput]]

### dateCreated
- **Type**: typing.Optional[str]

### dateUpdated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DistributionConfigurationSummary

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### dateUpdated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### regions
- **Type**: typing.Optional[typing.List[str]]


# DistributionOutput

### region
- **Type**: <class 'str'>
- **Required**: Yes

### amiDistributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AmiDistributionConfigurationOutput]

### containerDistributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerDistributionConfigurationOutput]

### licenseConfigurationArns
- **Type**: typing.Optional[typing.List[str]]

### launchTemplateConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchTemplateConfiguration]]

### s3ExportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.S3ExportConfiguration]

### fastLaunchConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.FastLaunchConfiguration]]


# DistributionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EbsInstanceBlockDeviceSpecification

### encrypted
- **Type**: typing.Optional[bool]

### deleteOnTermination
- **Type**: typing.Optional[bool]

### iops
- **Type**: typing.Optional[int]

### kmsKeyId
- **Type**: typing.Optional[str]

### snapshotId
- **Type**: typing.Optional[str]

### volumeSize
- **Type**: typing.Optional[int]

### volumeType
- **Type**: typing.Optional[typing.Literal['gp2', 'gp3', 'io1', 'io2', 'sc1', 'st1', 'standard']]

### throughput
- **Type**: typing.Optional[int]


# EcrConfiguration

### repositoryName
- **Type**: typing.Optional[str]

### containerTags
- **Type**: typing.Optional[typing.Sequence[str]]


# EcrConfigurationOutput

### repositoryName
- **Type**: typing.Optional[str]

### containerTags
- **Type**: typing.Optional[typing.List[str]]


# FastLaunchConfiguration

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### snapshotConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.FastLaunchSnapshotConfiguration]

### maxParallelLaunches
- **Type**: typing.Optional[int]

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.FastLaunchLaunchTemplateSpecification]

### accountId
- **Type**: typing.Optional[str]


# FastLaunchLaunchTemplateSpecification

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### launchTemplateVersion
- **Type**: typing.Optional[str]


# FastLaunchSnapshotConfiguration

### targetResourceCount
- **Type**: typing.Optional[int]


# Filter

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetComponentPolicyRequest

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentPolicyResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetComponentRequest

### componentBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerRecipePolicyRequest

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerRecipePolicyResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerRecipeRequest

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerRecipeResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### containerRecipe
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerRecipe'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetDistributionConfigurationRequest

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDistributionConfigurationResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### distributionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetImagePipelineRequest

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImagePipelineResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ImagePipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetImagePolicyRequest

### imageArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImagePolicyResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetImageRecipePolicyRequest

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImageRecipePolicyResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetImageRecipeRequest

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImageRecipeResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipe
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ImageRecipe'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetImageRequest

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImageResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### image
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.Image'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetInfrastructureConfigurationRequest

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetInfrastructureConfigurationResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.InfrastructureConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetLifecycleExecutionRequest

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLifecycleExecutionResponse

### lifecycleExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecution'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetLifecyclePolicyRequest

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLifecyclePolicyResponse

### lifecyclePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetMarketplaceResourceRequest

### resourceType
- **Type**: typing.Literal['COMPONENT_ARTIFACT', 'COMPONENT_DATA']
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceLocation
- **Type**: typing.Optional[str]


# GetMarketplaceResourceResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowExecutionRequest

### workflowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowRequest

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowResponse

### workflow
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.Workflow'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowStepExecutionRequest

### stepExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowStepExecutionResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### stepExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SKIPPED']
- **Required**: Yes

### rollbackStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'RUNNING', 'SKIPPED']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### inputs
- **Type**: <class 'str'>
- **Required**: Yes

### outputs
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'str'>
- **Required**: Yes

### onFailure
- **Type**: <class 'str'>
- **Required**: Yes

### timeoutSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# Image

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageAggregation

### imageBuildVersionArn
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SeverityCounts]


# ImagePackage

### packageName
- **Type**: typing.Optional[str]

### packageVersion
- **Type**: typing.Optional[str]


# ImagePipeline

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows', 'macOS']]

### enhancedImageMetadataEnabled
- **Type**: typing.Optional[bool]

### imageRecipeArn
- **Type**: typing.Optional[str]

### containerRecipeArn
- **Type**: typing.Optional[str]

### infrastructureConfigurationArn
- **Type**: typing.Optional[str]

### distributionConfigurationArn
- **Type**: typing.Optional[str]

### imageTestsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTestsConfiguration]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Schedule]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### dateCreated
- **Type**: typing.Optional[str]

### dateUpdated
- **Type**: typing.Optional[str]

### dateLastRun
- **Type**: typing.Optional[str]

### dateNextRun
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationOutput]

### executionRole
- **Type**: typing.Optional[str]

### workflows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationOutput]]


# ImagePipelineAggregation

### imagePipelineArn
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SeverityCounts]


# ImageRecipe

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageRecipeSummary

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows', 'macOS']]

### owner
- **Type**: typing.Optional[str]

### parentImage
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ImageScanFinding

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageScanFindingAggregation

### accountAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AccountAggregation]

### imageAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageAggregation]

### imagePipelineAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImagePipelineAggregation]

### vulnerabilityIdAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.VulnerabilityIdAggregation]


# ImageScanFindingsFilter

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# ImageScanState

### status
- **Type**: typing.Optional[typing.Literal['ABANDONED', 'COLLECTING', 'COMPLETED', 'FAILED', 'PENDING', 'SCANNING', 'TIMED_OUT']]

### reason
- **Type**: typing.Optional[str]


# ImageScanningConfiguration

### imageScanningEnabled
- **Type**: typing.Optional[bool]

### ecrConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.EcrConfiguration]


# ImageScanningConfigurationOutput

### imageScanningEnabled
- **Type**: typing.Optional[bool]

### ecrConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.EcrConfigurationOutput]


# ImageScanningConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageState

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'BUILDING', 'CANCELLED', 'CREATING', 'DELETED', 'DEPRECATED', 'DISABLED', 'DISTRIBUTING', 'FAILED', 'INTEGRATING', 'PENDING', 'TESTING']]

### reason
- **Type**: typing.Optional[str]


# ImageSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageTestsConfiguration

### imageTestsEnabled
- **Type**: typing.Optional[bool]

### timeoutMinutes
- **Type**: typing.Optional[int]


# ImageVersion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportComponentResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### componentBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# ImportDiskImageRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### platform
- **Type**: <class 'str'>
- **Required**: Yes

### osVersion
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### executionRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ImportDiskImageResponse

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# ImportVmImageRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### platform
- **Type**: typing.Literal['Linux', 'Windows', 'macOS']
- **Required**: Yes

### vmImportTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### osVersion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ImportVmImageResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# InfrastructureConfiguration

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### instanceProfileName
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### subnetId
- **Type**: typing.Optional[str]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Logging]

### keyPair
- **Type**: typing.Optional[str]

### terminateInstanceOnFailure
- **Type**: typing.Optional[bool]

### snsTopicArn
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### dateUpdated
- **Type**: typing.Optional[str]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### instanceMetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceMetadataOptions]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Placement]


# InfrastructureConfigurationSummary

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### dateUpdated
- **Type**: typing.Optional[str]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### instanceProfileName
- **Type**: typing.Optional[str]

### placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Placement]


# InspectorScoreDetails

### adjustedCvss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.CvssScoreDetails]


# InstanceBlockDeviceMapping

### deviceName
- **Type**: typing.Optional[str]

### ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.EbsInstanceBlockDeviceSpecification]

### virtualName
- **Type**: typing.Optional[str]

### noDevice
- **Type**: typing.Optional[str]


# InstanceConfiguration

### image
- **Type**: typing.Optional[str]

### blockDeviceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceBlockDeviceMapping]]


# InstanceConfigurationOutput

### image
- **Type**: typing.Optional[str]

### blockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceBlockDeviceMapping]]


# InstanceConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InstanceMetadataOptions

### httpTokens
- **Type**: typing.Optional[str]

### httpPutResponseHopLimit
- **Type**: typing.Optional[int]


# LaunchPermissionConfiguration

### userIds
- **Type**: typing.Optional[typing.Sequence[str]]

### userGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### organizationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### organizationalUnitArns
- **Type**: typing.Optional[typing.Sequence[str]]


# LaunchPermissionConfigurationOutput

### userIds
- **Type**: typing.Optional[typing.List[str]]

### userGroups
- **Type**: typing.Optional[typing.List[str]]

### organizationArns
- **Type**: typing.Optional[typing.List[str]]

### organizationalUnitArns
- **Type**: typing.Optional[typing.List[str]]


# LaunchPermissionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LaunchTemplateConfiguration

### launchTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### setDefaultVersion
- **Type**: typing.Optional[bool]


# LifecycleExecution

### lifecycleExecutionId
- **Type**: typing.Optional[str]

### lifecyclePolicyArn
- **Type**: typing.Optional[str]

### resourcesImpactedSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResourcesImpactedSummary]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionState]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# LifecycleExecutionResource

### accountId
- **Type**: typing.Optional[str]

### resourceId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResourceState]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResourceAction]

### region
- **Type**: typing.Optional[str]

### snapshots
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionSnapshotResource]]

### imageUris
- **Type**: typing.Optional[typing.List[str]]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# LifecycleExecutionResourceAction

### name
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETE', 'DEPRECATE', 'DISABLE']]

### reason
- **Type**: typing.Optional[str]


# LifecycleExecutionResourceState

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SKIPPED', 'SUCCESS']]

### reason
- **Type**: typing.Optional[str]


# LifecycleExecutionResourcesImpactedSummary

### hasImpactedResources
- **Type**: typing.Optional[bool]


# LifecycleExecutionSnapshotResource

### snapshotId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResourceState]


# LifecycleExecutionState

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SUCCESS']]

### reason
- **Type**: typing.Optional[str]


# LifecyclePolicy

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### executionRole
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['AMI_IMAGE', 'CONTAINER_IMAGE']]

### policyDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailOutput]]

### resourceSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionOutput]

### dateCreated
- **Type**: typing.Optional[datetime.datetime]

### dateUpdated
- **Type**: typing.Optional[datetime.datetime]

### dateLastRun
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# LifecyclePolicyDetailActionIncludeResources

### amis
- **Type**: typing.Optional[bool]

### snapshots
- **Type**: typing.Optional[bool]

### containers
- **Type**: typing.Optional[bool]


# LifecyclePolicyDetailExclusionRules

### tagMap
- **Type**: typing.Optional[typing.Mapping[str, str]]

### amis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisUnion]


# LifecyclePolicyDetailExclusionRulesAmis

### isPublic
- **Type**: typing.Optional[bool]

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### sharedAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### lastLaunched
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisLastLaunched]

### tagMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# LifecyclePolicyDetailExclusionRulesAmisLastLaunched

### value
- **Type**: <class 'int'>
- **Required**: Yes

### unit
- **Type**: typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']
- **Required**: Yes


# LifecyclePolicyDetailExclusionRulesAmisOutput

### isPublic
- **Type**: typing.Optional[bool]

### regions
- **Type**: typing.Optional[typing.List[str]]

### sharedAccounts
- **Type**: typing.Optional[typing.List[str]]

### lastLaunched
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisLastLaunched]

### tagMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# LifecyclePolicyDetailExclusionRulesAmisUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyDetailExclusionRulesOutput

### tagMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### amis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisOutput]


# LifecyclePolicyDetailOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyDetailUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyResourceSelection

### recipes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionRecipe]]

### tagMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# LifecyclePolicyResourceSelectionOutput

### recipes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionRecipe]]

### tagMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# LifecyclePolicyResourceSelectionRecipe

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes


# LifecyclePolicyResourceSelectionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicySummary

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### executionRole
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['AMI_IMAGE', 'CONTAINER_IMAGE']]

### dateCreated
- **Type**: typing.Optional[datetime.datetime]

### dateUpdated
- **Type**: typing.Optional[datetime.datetime]

### dateLastRun
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListComponentBuildVersionsRequest

### componentVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentBuildVersionsResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### componentSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsRequest

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### byName
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### componentVersionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListContainerRecipesRequest

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListContainerRecipesResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### containerRecipeSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerRecipeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDistributionConfigurationsRequest

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDistributionConfigurationsResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### distributionConfigurationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImageBuildVersionsRequest

### imageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImageBuildVersionsResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImagePackagesRequest

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImagePackagesResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePackageList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImagePackage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImagePipelineImagesRequest

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImagePipelineImagesResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImagePipelinesRequest

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImagePipelinesResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePipelineList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImagePipeline]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImageRecipesRequest

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImageRecipesResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipeSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageRecipeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImageScanFindingAggregationsResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationType
- **Type**: <class 'str'>
- **Required**: Yes

### responses
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanFindingAggregation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImageScanFindingsRequest

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanFindingsFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImageScanFindingsResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanFinding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImagesRequest

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### byName
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### includeDeprecated
- **Type**: typing.Optional[bool]


# ListImagesResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageVersionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInfrastructureConfigurationsRequest

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInfrastructureConfigurationsResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfigurationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.InfrastructureConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLifecycleExecutionResourcesRequest

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### parentResourceId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLifecycleExecutionResourcesResponse

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleExecutionState
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionState'>
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLifecycleExecutionsRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLifecycleExecutionsResponse

### lifecycleExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecution]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLifecyclePoliciesRequest

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLifecyclePoliciesResponse

### lifecyclePolicySummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# ListWaitingWorkflowStepsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWaitingWorkflowStepsResponse

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowStepExecution]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowBuildVersionsRequest

### workflowVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowBuildVersionsResponse

### workflowSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowExecutionsRequest

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowExecutionsResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowExecutionMetadata]
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowStepExecutionsRequest

### workflowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowStepExecutionsResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowStepMetadata]
- **Required**: Yes

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### workflowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequest

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.Filter]]

### byName
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowsResponse

### workflowVersionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Logging

### s3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.S3Logs]


# OutputResources

### amis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.Ami]]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.Container]]


# PackageVulnerabilityDetails

### vulnerabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### vulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.VulnerablePackage]]

### source
- **Type**: typing.Optional[str]

### cvss
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.CvssScore]]

### relatedVulnerabilities
- **Type**: typing.Optional[typing.List[str]]

### sourceUrl
- **Type**: typing.Optional[str]

### vendorSeverity
- **Type**: typing.Optional[str]

### vendorCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### vendorUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### referenceUrls
- **Type**: typing.Optional[typing.List[str]]


# Placement

### availabilityZone
- **Type**: typing.Optional[str]

### tenancy
- **Type**: typing.Optional[typing.Literal['dedicated', 'default', 'host']]

### hostId
- **Type**: typing.Optional[str]

### hostResourceGroupArn
- **Type**: typing.Optional[str]


# ProductCodeListItem

### productCodeId
- **Type**: <class 'str'>
- **Required**: Yes

### productCodeType
- **Type**: typing.Literal['marketplace']
- **Required**: Yes


# PutComponentPolicyRequest

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutComponentPolicyResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# PutContainerRecipePolicyRequest

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutContainerRecipePolicyResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# PutImagePolicyRequest

### imageArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutImagePolicyResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# PutImageRecipePolicyRequest

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutImageRecipePolicyResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# Remediation

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.RemediationRecommendation]


# RemediationRecommendation

### text
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# ResourceState

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'DEPRECATED', 'DISABLED']]


# ResourceStateUpdateExclusionRules

### amis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisUnion]


# ResourceStateUpdateIncludeResources

### amis
- **Type**: typing.Optional[bool]

### snapshots
- **Type**: typing.Optional[bool]

### containers
- **Type**: typing.Optional[bool]


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


# S3ExportConfiguration

### roleName
- **Type**: <class 'str'>
- **Required**: Yes

### diskImageFormat
- **Type**: typing.Literal['RAW', 'VHD', 'VMDK']
- **Required**: Yes

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Prefix
- **Type**: typing.Optional[str]


# S3Logs

### s3BucketName
- **Type**: typing.Optional[str]

### s3KeyPrefix
- **Type**: typing.Optional[str]


# Schedule

### scheduleExpression
- **Type**: typing.Optional[str]

### timezone
- **Type**: typing.Optional[str]

### pipelineExecutionStartCondition
- **Type**: typing.Optional[typing.Literal['EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE', 'EXPRESSION_MATCH_ONLY']]


# SendWorkflowStepActionRequest

### stepExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Literal['RESUME', 'STOP']
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# SendWorkflowStepActionResponse

### stepExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# SeverityCounts

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartImagePipelineExecutionRequest

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartImagePipelineExecutionResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# StartResourceStateUpdateRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResourceState'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### executionRole
- **Type**: typing.Optional[str]

### includeResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ResourceStateUpdateIncludeResources]

### exclusionRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ResourceStateUpdateExclusionRules]

### updateAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Timestamp]


# StartResourceStateUpdateResponse

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# SystemsManagerAgent

### uninstallAfterBuild
- **Type**: typing.Optional[bool]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetContainerRepository

### service
- **Type**: typing.Literal['ECR']
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDistributionConfigurationRequest

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### distributions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionUnion]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateDistributionConfigurationResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateImagePipelineRequest

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### imageRecipeArn
- **Type**: typing.Optional[str]

### containerRecipeArn
- **Type**: typing.Optional[str]

### distributionConfigurationArn
- **Type**: typing.Optional[str]

### imageTestsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTestsConfiguration]

### enhancedImageMetadataEnabled
- **Type**: typing.Optional[bool]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Schedule]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationUnion]

### workflows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationUnion]]

### executionRole
- **Type**: typing.Optional[str]


# UpdateImagePipelineResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInfrastructureConfigurationRequest

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### instanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### instanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetId
- **Type**: typing.Optional[str]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Logging]

### keyPair
- **Type**: typing.Optional[str]

### terminateInstanceOnFailure
- **Type**: typing.Optional[bool]

### snsTopicArn
- **Type**: typing.Optional[str]

### resourceTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### instanceMetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceMetadataOptions]

### placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.Placement]


# UpdateInfrastructureConfigurationResponse

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLifecyclePolicyRequest

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionRole
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['AMI_IMAGE', 'CONTAINER_IMAGE']
- **Required**: Yes

### policyDetails
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailUnion]
- **Required**: Yes

### resourceSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionUnion'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateLifecyclePolicyResponse

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadata'>
- **Required**: Yes


# VulnerabilityIdAggregation

### vulnerabilityId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SeverityCounts]


# VulnerablePackage

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### sourceLayerHash
- **Type**: typing.Optional[str]

### epoch
- **Type**: typing.Optional[int]

### release
- **Type**: typing.Optional[str]

### arch
- **Type**: typing.Optional[str]

### packageManager
- **Type**: typing.Optional[str]

### filePath
- **Type**: typing.Optional[str]

### fixedInVersion
- **Type**: typing.Optional[str]

### remediation
- **Type**: typing.Optional[str]


# Workflow

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowConfiguration

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowParameterUnion]]

### parallelGroup
- **Type**: typing.Optional[str]

### onFailure
- **Type**: typing.Optional[typing.Literal['ABORT', 'CONTINUE']]


# WorkflowConfigurationOutput

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowParameterOutput]]

### parallelGroup
- **Type**: typing.Optional[str]

### onFailure
- **Type**: typing.Optional[typing.Literal['ABORT', 'CONTINUE']]


# WorkflowConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowExecutionMetadata

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowParameter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WorkflowParameterOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.List[str]
- **Required**: Yes


# WorkflowParameterUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowState

### status
- **Type**: typing.Optional[typing.Literal['DEPRECATED']]

### reason
- **Type**: typing.Optional[str]


# WorkflowStepExecution

### stepExecutionId
- **Type**: typing.Optional[str]

### imageBuildVersionArn
- **Type**: typing.Optional[str]

### workflowExecutionId
- **Type**: typing.Optional[str]

### workflowBuildVersionArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### action
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[str]


# WorkflowStepMetadata

### stepExecutionId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### action
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING', 'SKIPPED']]

### rollbackStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING', 'SKIPPED']]

### message
- **Type**: typing.Optional[str]

### inputs
- **Type**: typing.Optional[str]

### outputs
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]


# WorkflowSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowVersion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


# Imagebuilder Classes

# AccountAggregationTypeDef

### accountId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SeverityCountsTypeDef]


# AdditionalInstanceConfigurationTypeDef

### systemsManagerAgent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SystemsManagerAgentTypeDef]

### userDataOverride
- **Type**: typing.Optional[str]


# AmiDistributionConfigurationOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchPermissionConfigurationOutputTypeDef]


# AmiDistributionConfigurationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchPermissionConfigurationUnionTypeDef]


# AmiDistributionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AmiTypeDef

### region
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageStateTypeDef]

### accountId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelImageCreationRequestTypeDef

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# CancelImageCreationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelLifecycleExecutionRequestTypeDef

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# CancelLifecycleExecutionResponseTypeDef

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ComponentConfigurationOutputTypeDef

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentParameterOutputTypeDef]]


# ComponentConfigurationTypeDef

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentParameterUnionTypeDef]]


# ComponentConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentParameterOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.List[str]
- **Required**: Yes


# ComponentParameterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ComponentParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEPRECATED', 'DISABLED']]

### reason
- **Type**: typing.Optional[str]


# ComponentSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentVersionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerDistributionConfigurationOutputTypeDef

### targetRepository
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.TargetContainerRepositoryTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### containerTags
- **Type**: typing.Optional[typing.List[str]]


# ContainerDistributionConfigurationTypeDef

### targetRepository
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.TargetContainerRepositoryTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### containerTags
- **Type**: typing.Optional[typing.Sequence[str]]


# ContainerDistributionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerRecipeSummaryTypeDef

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


# ContainerRecipeTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationOutputTypeDef]]

### instanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceConfigurationOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.TargetContainerRepositoryTypeDef]


# ContainerTypeDef

### region
- **Type**: typing.Optional[str]

### imageUris
- **Type**: typing.Optional[typing.List[str]]


# CreateComponentRequestTypeDef

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


# CreateComponentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContainerRecipeRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationUnionTypeDef]
- **Required**: Yes

### parentImage
- **Type**: <class 'str'>
- **Required**: Yes

### targetRepository
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.TargetContainerRepositoryTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### instanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceConfigurationUnionTypeDef]

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


# CreateContainerRecipeResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDistributionConfigurationRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### distributions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionUnionTypeDef]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDistributionConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImagePipelineRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTestsConfigurationTypeDef]

### enhancedImageMetadataEnabled
- **Type**: typing.Optional[bool]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ScheduleTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationUnionTypeDef]

### workflows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationUnionTypeDef]]

### executionRole
- **Type**: typing.Optional[str]


# CreateImagePipelineResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImageRecipeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### components
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationUnionTypeDef]
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceBlockDeviceMappingTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### workingDirectory
- **Type**: typing.Optional[str]

### additionalInstanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AdditionalInstanceConfigurationTypeDef]


# CreateImageRecipeResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImageRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTestsConfigurationTypeDef]

### enhancedImageMetadataEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationUnionTypeDef]

### workflows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationUnionTypeDef]]

### executionRole
- **Type**: typing.Optional[str]


# CreateImageResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInfrastructureConfigurationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LoggingTypeDef]

### keyPair
- **Type**: typing.Optional[str]

### terminateInstanceOnFailure
- **Type**: typing.Optional[bool]

### snsTopicArn
- **Type**: typing.Optional[str]

### resourceTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### instanceMetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceMetadataOptionsTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.PlacementTypeDef]


# CreateInfrastructureConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLifecyclePolicyRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailUnionTypeDef]
- **Required**: Yes

### resourceSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionUnionTypeDef'>
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


# CreateLifecyclePolicyResponseTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkflowResponseTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CvssScoreAdjustmentTypeDef

### metric
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# CvssScoreDetailsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.CvssScoreAdjustmentTypeDef]]


# CvssScoreTypeDef

### baseScore
- **Type**: typing.Optional[float]

### scoringVector
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]


# DeleteComponentRequestTypeDef

### componentBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComponentResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### componentBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteContainerRecipeRequestTypeDef

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerRecipeResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDistributionConfigurationRequestTypeDef

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDistributionConfigurationResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteImagePipelineRequestTypeDef

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImagePipelineResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteImageRecipeRequestTypeDef

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageRecipeResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteImageRequestTypeDef

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInfrastructureConfigurationRequestTypeDef

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInfrastructureConfigurationResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLifecyclePolicyRequestTypeDef

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLifecyclePolicyResponseTypeDef

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkflowRequestTypeDef

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowResponseTypeDef

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DistributionConfigurationSummaryTypeDef

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


# DistributionConfigurationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionOutputTypeDef]]

### dateCreated
- **Type**: typing.Optional[str]

### dateUpdated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DistributionOutputTypeDef

### region
- **Type**: <class 'str'>
- **Required**: Yes

### amiDistributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AmiDistributionConfigurationOutputTypeDef]

### containerDistributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerDistributionConfigurationOutputTypeDef]

### licenseConfigurationArns
- **Type**: typing.Optional[typing.List[str]]

### launchTemplateConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchTemplateConfigurationTypeDef]]

### s3ExportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.S3ExportConfigurationTypeDef]

### fastLaunchConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.FastLaunchConfigurationTypeDef]]


# DistributionTypeDef

### region
- **Type**: <class 'str'>
- **Required**: Yes

### amiDistributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AmiDistributionConfigurationUnionTypeDef]

### containerDistributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerDistributionConfigurationUnionTypeDef]

### licenseConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### launchTemplateConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchTemplateConfigurationTypeDef]]

### s3ExportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.S3ExportConfigurationTypeDef]

### fastLaunchConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FastLaunchConfigurationTypeDef]]


# DistributionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EbsInstanceBlockDeviceSpecificationTypeDef

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


# EcrConfigurationOutputTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### containerTags
- **Type**: typing.Optional[typing.List[str]]


# EcrConfigurationTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### containerTags
- **Type**: typing.Optional[typing.Sequence[str]]


# FastLaunchConfigurationTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### snapshotConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.FastLaunchSnapshotConfigurationTypeDef]

### maxParallelLaunches
- **Type**: typing.Optional[int]

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.FastLaunchLaunchTemplateSpecificationTypeDef]

### accountId
- **Type**: typing.Optional[str]


# FastLaunchLaunchTemplateSpecificationTypeDef

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### launchTemplateVersion
- **Type**: typing.Optional[str]


# FastLaunchSnapshotConfigurationTypeDef

### targetResourceCount
- **Type**: typing.Optional[int]


# FilterTypeDef

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetComponentPolicyRequestTypeDef

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentPolicyResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComponentRequestTypeDef

### componentBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerRecipePolicyRequestTypeDef

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerRecipePolicyResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerRecipeRequestTypeDef

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerRecipeResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### containerRecipe
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerRecipeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDistributionConfigurationRequestTypeDef

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDistributionConfigurationResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### distributionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImagePipelineRequestTypeDef

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImagePipelineResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ImagePipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImagePolicyRequestTypeDef

### imageArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImagePolicyResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImageRecipePolicyRequestTypeDef

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImageRecipePolicyResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImageRecipeRequestTypeDef

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImageRecipeResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipe
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ImageRecipeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImageRequestTypeDef

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetImageResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### image
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInfrastructureConfigurationRequestTypeDef

### infrastructureConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetInfrastructureConfigurationResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.InfrastructureConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLifecycleExecutionRequestTypeDef

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLifecycleExecutionResponseTypeDef

### lifecycleExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLifecyclePolicyRequestTypeDef

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLifecyclePolicyResponseTypeDef

### lifecyclePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMarketplaceResourceRequestTypeDef

### resourceType
- **Type**: typing.Literal['COMPONENT_ARTIFACT', 'COMPONENT_DATA']
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceLocation
- **Type**: typing.Optional[str]


# GetMarketplaceResourceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowExecutionRequestTypeDef

### workflowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowRequestTypeDef

### workflowBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowResponseTypeDef

### workflow
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowStepExecutionRequestTypeDef

### stepExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowStepExecutionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImageAggregationTypeDef

### imageBuildVersionArn
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SeverityCountsTypeDef]


# ImagePackageTypeDef

### packageName
- **Type**: typing.Optional[str]

### packageVersion
- **Type**: typing.Optional[str]


# ImagePipelineAggregationTypeDef

### imagePipelineArn
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SeverityCountsTypeDef]


# ImagePipelineTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTestsConfigurationTypeDef]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ScheduleTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationOutputTypeDef]

### executionRole
- **Type**: typing.Optional[str]

### workflows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationOutputTypeDef]]


# ImageRecipeSummaryTypeDef

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


# ImageRecipeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageScanFindingAggregationTypeDef

### accountAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AccountAggregationTypeDef]

### imageAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageAggregationTypeDef]

### imagePipelineAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImagePipelineAggregationTypeDef]

### vulnerabilityIdAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.VulnerabilityIdAggregationTypeDef]


# ImageScanFindingTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageScanFindingsFilterTypeDef

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# ImageScanStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ABANDONED', 'COLLECTING', 'COMPLETED', 'FAILED', 'PENDING', 'SCANNING', 'TIMED_OUT']]

### reason
- **Type**: typing.Optional[str]


# ImageScanningConfigurationOutputTypeDef

### imageScanningEnabled
- **Type**: typing.Optional[bool]

### ecrConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.EcrConfigurationOutputTypeDef]


# ImageScanningConfigurationTypeDef

### imageScanningEnabled
- **Type**: typing.Optional[bool]

### ecrConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.EcrConfigurationTypeDef]


# ImageScanningConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'BUILDING', 'CANCELLED', 'CREATING', 'DELETED', 'DEPRECATED', 'DISABLED', 'DISTRIBUTING', 'FAILED', 'INTEGRATING', 'PENDING', 'TESTING']]

### reason
- **Type**: typing.Optional[str]


# ImageSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageTestsConfigurationTypeDef

### imageTestsEnabled
- **Type**: typing.Optional[bool]

### timeoutMinutes
- **Type**: typing.Optional[int]


# ImageTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageVersionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportComponentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportDiskImageRequestTypeDef

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


# ImportDiskImageResponseTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportVmImageRequestTypeDef

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


# ImportVmImageResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InfrastructureConfigurationSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.PlacementTypeDef]


# InfrastructureConfigurationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LoggingTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceMetadataOptionsTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.PlacementTypeDef]


# InspectorScoreDetailsTypeDef

### adjustedCvss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.CvssScoreDetailsTypeDef]


# InstanceBlockDeviceMappingTypeDef

### deviceName
- **Type**: typing.Optional[str]

### ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.EbsInstanceBlockDeviceSpecificationTypeDef]

### virtualName
- **Type**: typing.Optional[str]

### noDevice
- **Type**: typing.Optional[str]


# InstanceConfigurationOutputTypeDef

### image
- **Type**: typing.Optional[str]

### blockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceBlockDeviceMappingTypeDef]]


# InstanceConfigurationTypeDef

### image
- **Type**: typing.Optional[str]

### blockDeviceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceBlockDeviceMappingTypeDef]]


# InstanceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InstanceMetadataOptionsTypeDef

### httpTokens
- **Type**: typing.Optional[str]

### httpPutResponseHopLimit
- **Type**: typing.Optional[int]


# LaunchPermissionConfigurationOutputTypeDef

### userIds
- **Type**: typing.Optional[typing.List[str]]

### userGroups
- **Type**: typing.Optional[typing.List[str]]

### organizationArns
- **Type**: typing.Optional[typing.List[str]]

### organizationalUnitArns
- **Type**: typing.Optional[typing.List[str]]


# LaunchPermissionConfigurationTypeDef

### userIds
- **Type**: typing.Optional[typing.Sequence[str]]

### userGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### organizationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### organizationalUnitArns
- **Type**: typing.Optional[typing.Sequence[str]]


# LaunchPermissionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LaunchTemplateConfigurationTypeDef

### launchTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### setDefaultVersion
- **Type**: typing.Optional[bool]


# LifecycleExecutionResourceActionTypeDef

### name
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETE', 'DEPRECATE', 'DISABLE']]

### reason
- **Type**: typing.Optional[str]


# LifecycleExecutionResourceStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SKIPPED', 'SUCCESS']]

### reason
- **Type**: typing.Optional[str]


# LifecycleExecutionResourceTypeDef

### accountId
- **Type**: typing.Optional[str]

### resourceId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResourceStateTypeDef]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResourceActionTypeDef]

### region
- **Type**: typing.Optional[str]

### snapshots
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionSnapshotResourceTypeDef]]

### imageUris
- **Type**: typing.Optional[typing.List[str]]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# LifecycleExecutionResourcesImpactedSummaryTypeDef

### hasImpactedResources
- **Type**: typing.Optional[bool]


# LifecycleExecutionSnapshotResourceTypeDef

### snapshotId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResourceStateTypeDef]


# LifecycleExecutionStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SUCCESS']]

### reason
- **Type**: typing.Optional[str]


# LifecycleExecutionTypeDef

### lifecycleExecutionId
- **Type**: typing.Optional[str]

### lifecyclePolicyArn
- **Type**: typing.Optional[str]

### resourcesImpactedSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResourcesImpactedSummaryTypeDef]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionStateTypeDef]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# LifecyclePolicyDetailActionIncludeResourcesTypeDef

### amis
- **Type**: typing.Optional[bool]

### snapshots
- **Type**: typing.Optional[bool]

### containers
- **Type**: typing.Optional[bool]


# LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef

### value
- **Type**: <class 'int'>
- **Required**: Yes

### unit
- **Type**: typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']
- **Required**: Yes


# LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef

### isPublic
- **Type**: typing.Optional[bool]

### regions
- **Type**: typing.Optional[typing.List[str]]

### sharedAccounts
- **Type**: typing.Optional[typing.List[str]]

### lastLaunched
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef]

### tagMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# LifecyclePolicyDetailExclusionRulesAmisTypeDef

### isPublic
- **Type**: typing.Optional[bool]

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### sharedAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### lastLaunched
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef]

### tagMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyDetailExclusionRulesOutputTypeDef

### tagMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### amis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef]


# LifecyclePolicyDetailExclusionRulesTypeDef

### tagMap
- **Type**: typing.Optional[typing.Mapping[str, str]]

### amis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef]


# LifecyclePolicyDetailOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyDetailUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyResourceSelectionOutputTypeDef

### recipes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionRecipeTypeDef]]

### tagMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# LifecyclePolicyResourceSelectionRecipeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes


# LifecyclePolicyResourceSelectionTypeDef

### recipes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionRecipeTypeDef]]

### tagMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# LifecyclePolicyResourceSelectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicySummaryTypeDef

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


# LifecyclePolicyTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailOutputTypeDef]]

### resourceSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionOutputTypeDef]

### dateCreated
- **Type**: typing.Optional[datetime.datetime]

### dateUpdated
- **Type**: typing.Optional[datetime.datetime]

### dateLastRun
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListComponentBuildVersionsRequestTypeDef

### componentVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentBuildVersionsResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### componentSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### byName
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### componentVersionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListContainerRecipesRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListContainerRecipesResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### containerRecipeSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerRecipeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDistributionConfigurationsRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDistributionConfigurationsResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### distributionConfigurationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImageBuildVersionsRequestTypeDef

### imageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImageBuildVersionsResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImagePackagesRequestTypeDef

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImagePackagesResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePackageList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImagePackageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImagePipelineImagesRequestTypeDef

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImagePipelineImagesResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImagePipelinesRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImagePipelinesResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imagePipelineList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImagePipelineTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImageRecipesRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImageRecipesResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipeSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageRecipeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImageScanFindingAggregationsResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationType
- **Type**: <class 'str'>
- **Required**: Yes

### responses
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanFindingAggregationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImageScanFindingsRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanFindingsFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImageScanFindingsResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanFindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImagesRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### byName
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### includeDeprecated
- **Type**: typing.Optional[bool]


# ListImagesResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageVersionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInfrastructureConfigurationsRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInfrastructureConfigurationsResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### infrastructureConfigurationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.InfrastructureConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLifecycleExecutionResourcesRequestTypeDef

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### parentResourceId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLifecycleExecutionResourcesResponseTypeDef

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleExecutionState
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionStateTypeDef'>
- **Required**: Yes

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLifecycleExecutionsRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLifecycleExecutionsResponseTypeDef

### lifecycleExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecycleExecutionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLifecyclePoliciesRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLifecyclePoliciesResponseTypeDef

### lifecyclePolicySummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWaitingWorkflowStepsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWaitingWorkflowStepsResponseTypeDef

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowStepExecutionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowBuildVersionsRequestTypeDef

### workflowVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowBuildVersionsResponseTypeDef

### workflowSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowExecutionsRequestTypeDef

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowExecutionsResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowExecutionMetadataTypeDef]
- **Required**: Yes

### imageBuildVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowStepExecutionsRequestTypeDef

### workflowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowStepExecutionsResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowStepMetadataTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['AWSMarketplace', 'Amazon', 'Self', 'Shared', 'ThirdParty']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]]

### byName
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowsResponseTypeDef

### workflowVersionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LoggingTypeDef

### s3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.S3LogsTypeDef]


# OutputResourcesTypeDef

### amis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.AmiTypeDef]]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerTypeDef]]


# PackageVulnerabilityDetailsTypeDef

### vulnerabilityId
- **Type**: <class 'str'>
- **Required**: Yes

### vulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.VulnerablePackageTypeDef]]

### source
- **Type**: typing.Optional[str]

### cvss
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.CvssScoreTypeDef]]

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


# PlacementTypeDef

### availabilityZone
- **Type**: typing.Optional[str]

### tenancy
- **Type**: typing.Optional[typing.Literal['dedicated', 'default', 'host']]

### hostId
- **Type**: typing.Optional[str]

### hostResourceGroupArn
- **Type**: typing.Optional[str]


# ProductCodeListItemTypeDef

### productCodeId
- **Type**: <class 'str'>
- **Required**: Yes

### productCodeType
- **Type**: typing.Literal['marketplace']
- **Required**: Yes


# PutComponentPolicyRequestTypeDef

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutComponentPolicyResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### componentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutContainerRecipePolicyRequestTypeDef

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutContainerRecipePolicyResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### containerRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutImagePolicyRequestTypeDef

### imageArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutImagePolicyResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutImageRecipePolicyRequestTypeDef

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutImageRecipePolicyResponseTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### imageRecipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemediationRecommendationTypeDef

### text
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# RemediationTypeDef

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.RemediationRecommendationTypeDef]


# ResourceStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'DEPRECATED', 'DISABLED']]


# ResourceStateUpdateExclusionRulesTypeDef

### amis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef]


# ResourceStateUpdateIncludeResourcesTypeDef

### amis
- **Type**: typing.Optional[bool]

### snapshots
- **Type**: typing.Optional[bool]

### containers
- **Type**: typing.Optional[bool]


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


# S3ExportConfigurationTypeDef

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


# S3LogsTypeDef

### s3BucketName
- **Type**: typing.Optional[str]

### s3KeyPrefix
- **Type**: typing.Optional[str]


# ScheduleTypeDef

### scheduleExpression
- **Type**: typing.Optional[str]

### timezone
- **Type**: typing.Optional[str]

### pipelineExecutionStartCondition
- **Type**: typing.Optional[typing.Literal['EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE', 'EXPRESSION_MATCH_ONLY']]


# SendWorkflowStepActionRequestTypeDef

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


# SendWorkflowStepActionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SeverityCountsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartImagePipelineExecutionRequestTypeDef

### imagePipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartImagePipelineExecutionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartResourceStateUpdateRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResourceStateTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### executionRole
- **Type**: typing.Optional[str]

### includeResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ResourceStateUpdateIncludeResourcesTypeDef]

### exclusionRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ResourceStateUpdateExclusionRulesTypeDef]

### updateAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.TimestampTypeDef]


# StartResourceStateUpdateResponseTypeDef

### lifecycleExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SystemsManagerAgentTypeDef

### uninstallAfterBuild
- **Type**: typing.Optional[bool]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetContainerRepositoryTypeDef

### service
- **Type**: typing.Literal['ECR']
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDistributionConfigurationRequestTypeDef

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### distributions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionUnionTypeDef]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateDistributionConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateImagePipelineRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTestsConfigurationTypeDef]

### enhancedImageMetadataEnabled
- **Type**: typing.Optional[bool]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ScheduleTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationUnionTypeDef]

### workflows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationUnionTypeDef]]

### executionRole
- **Type**: typing.Optional[str]


# UpdateImagePipelineResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInfrastructureConfigurationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LoggingTypeDef]

### keyPair
- **Type**: typing.Optional[str]

### terminateInstanceOnFailure
- **Type**: typing.Optional[bool]

### snsTopicArn
- **Type**: typing.Optional[str]

### resourceTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### instanceMetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceMetadataOptionsTypeDef]

### placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.PlacementTypeDef]


# UpdateInfrastructureConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLifecyclePolicyRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailUnionTypeDef]
- **Required**: Yes

### resourceSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionUnionTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateLifecyclePolicyResponseTypeDef

### lifecyclePolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VulnerabilityIdAggregationTypeDef

### vulnerabilityId
- **Type**: typing.Optional[str]

### severityCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.SeverityCountsTypeDef]


# VulnerablePackageTypeDef

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


# WorkflowConfigurationOutputTypeDef

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowParameterOutputTypeDef]]

### parallelGroup
- **Type**: typing.Optional[str]

### onFailure
- **Type**: typing.Optional[typing.Literal['ABORT', 'CONTINUE']]


# WorkflowConfigurationTypeDef

### workflowArn
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowParameterUnionTypeDef]]

### parallelGroup
- **Type**: typing.Optional[str]

### onFailure
- **Type**: typing.Optional[typing.Literal['ABORT', 'CONTINUE']]


# WorkflowConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowExecutionMetadataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowParameterOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.List[str]
- **Required**: Yes


# WorkflowParameterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WorkflowParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['DEPRECATED']]

### reason
- **Type**: typing.Optional[str]


# WorkflowStepExecutionTypeDef

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


# WorkflowStepMetadataTypeDef

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


# WorkflowSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowVersionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


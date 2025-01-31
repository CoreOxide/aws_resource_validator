# imagebuilder_classes

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchPermissionConfigurationTypeDef]


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

# CancelImageCreationRequestRequestTypeDef

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


# CancelLifecycleExecutionRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentParameterTypeDef]]


# ComponentParameterDetailTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]


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


# ComponentStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['DEPRECATED']]

### reason
- **Type**: typing.Optional[str]


# ComponentSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

### supportedOsVersions
- **Type**: typing.Optional[typing.List[str]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentStateTypeDef]

### type
- **Type**: typing.Optional[typing.Literal['BUILD', 'TEST']]

### owner
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### changeDescription
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### publisher
- **Type**: typing.Optional[str]

### obfuscate
- **Type**: typing.Optional[bool]


# ComponentTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### changeDescription
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['BUILD', 'TEST']]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

### supportedOsVersions
- **Type**: typing.Optional[typing.List[str]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentStateTypeDef]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentParameterDetailTypeDef]]

### owner
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### encrypted
- **Type**: typing.Optional[bool]

### dateCreated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### publisher
- **Type**: typing.Optional[str]

### obfuscate
- **Type**: typing.Optional[bool]


# ComponentVersionTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

### supportedOsVersions
- **Type**: typing.Optional[typing.List[str]]

### type
- **Type**: typing.Optional[typing.Literal['BUILD', 'TEST']]

### owner
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]


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


# ContainerRecipeSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### containerType
- **Type**: typing.Optional[typing.Literal['DOCKER']]

### name
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

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
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

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


# CreateComponentRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### platform
- **Type**: typing.Literal['Linux', 'Windows']
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


# CreateContainerRecipeRequestRequestTypeDef

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
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationTypeDef, aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationOutputTypeDef]]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceConfigurationTypeDef]

### dockerfileTemplateData
- **Type**: typing.Optional[str]

### dockerfileTemplateUri
- **Type**: typing.Optional[str]

### platformOverride
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

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


# CreateDistributionConfigurationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### distributions
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionTypeDef, aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionOutputTypeDef]]
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


# CreateImagePipelineRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationTypeDef]

### workflows
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationTypeDef, aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationOutputTypeDef]]]

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


# CreateImageRecipeRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### components
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationTypeDef, aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationOutputTypeDef]]
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


# CreateImageRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationTypeDef]

### workflows
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationTypeDef, aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationOutputTypeDef]]]

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


# CreateInfrastructureConfigurationRequestRequestTypeDef

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


# CreateLifecyclePolicyRequestRequestTypeDef

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
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailTypeDef, aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailOutputTypeDef]]
- **Required**: Yes

### resourceSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionTypeDef'>
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


# CreateWorkflowRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BUILD', 'DISTRIBUTION', 'TEST']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### changeDescription
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[str]

### uri
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


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


# DeleteComponentRequestRequestTypeDef

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


# DeleteContainerRecipeRequestRequestTypeDef

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


# DeleteDistributionConfigurationRequestRequestTypeDef

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


# DeleteImagePipelineRequestRequestTypeDef

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


# DeleteImageRecipeRequestRequestTypeDef

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


# DeleteImageRequestRequestTypeDef

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


# DeleteInfrastructureConfigurationRequestRequestTypeDef

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


# DeleteLifecyclePolicyRequestRequestTypeDef

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


# DeleteWorkflowRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AmiDistributionConfigurationTypeDef]

### containerDistributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerDistributionConfigurationTypeDef]

### licenseConfigurationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### launchTemplateConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.LaunchTemplateConfigurationTypeDef]]

### s3ExportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.S3ExportConfigurationTypeDef]

### fastLaunchConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.FastLaunchConfigurationTypeDef]]


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


# GetComponentPolicyRequestRequestTypeDef

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


# GetComponentRequestRequestTypeDef

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


# GetContainerRecipePolicyRequestRequestTypeDef

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


# GetContainerRecipeRequestRequestTypeDef

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


# GetDistributionConfigurationRequestRequestTypeDef

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


# GetImagePipelineRequestRequestTypeDef

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


# GetImagePolicyRequestRequestTypeDef

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


# GetImageRecipePolicyRequestRequestTypeDef

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


# GetImageRecipeRequestRequestTypeDef

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


# GetImageRequestRequestTypeDef

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


# GetInfrastructureConfigurationRequestRequestTypeDef

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


# GetLifecycleExecutionRequestRequestTypeDef

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


# GetLifecyclePolicyRequestRequestTypeDef

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


# GetWorkflowExecutionRequestRequestTypeDef

### workflowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowExecutionResponseTypeDef

### requestId
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

### type
- **Type**: typing.Literal['BUILD', 'DISTRIBUTION', 'TEST']
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'ROLLBACK_COMPLETED', 'ROLLBACK_IN_PROGRESS', 'RUNNING', 'SKIPPED']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### totalStepCount
- **Type**: <class 'int'>
- **Required**: Yes

### totalStepsSucceeded
- **Type**: <class 'int'>
- **Required**: Yes

### totalStepsFailed
- **Type**: <class 'int'>
- **Required**: Yes

### totalStepsSkipped
- **Type**: <class 'int'>
- **Required**: Yes

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'str'>
- **Required**: Yes

### parallelGroup
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowRequestRequestTypeDef

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


# GetWorkflowStepExecutionRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

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
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

### owner
- **Type**: typing.Optional[str]

### parentImage
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ImageRecipeTypeDef

### arn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['AMI', 'DOCKER']]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

### owner
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### components
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.ComponentConfigurationOutputTypeDef]]

### parentImage
- **Type**: typing.Optional[str]

### blockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.InstanceBlockDeviceMappingTypeDef]]

### dateCreated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### workingDirectory
- **Type**: typing.Optional[str]

### additionalInstanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.AdditionalInstanceConfigurationTypeDef]


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

### awsAccountId
- **Type**: typing.Optional[str]

### imageBuildVersionArn
- **Type**: typing.Optional[str]

### imagePipelineArn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### remediation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.RemediationTypeDef]

### severity
- **Type**: typing.Optional[str]

### firstObservedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### inspectorScore
- **Type**: typing.Optional[float]

### inspectorScoreDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InspectorScoreDetailsTypeDef]

### packageVulnerabilityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.PackageVulnerabilityDetailsTypeDef]

### fixAvailable
- **Type**: typing.Optional[str]


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


# ImageStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'BUILDING', 'CANCELLED', 'CREATING', 'DELETED', 'DEPRECATED', 'DISABLED', 'DISTRIBUTING', 'FAILED', 'INTEGRATING', 'PENDING', 'TESTING']]

### reason
- **Type**: typing.Optional[str]


# ImageSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['AMI', 'DOCKER']]

### version
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

### osVersion
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageStateTypeDef]

### owner
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### outputResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.OutputResourcesTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### buildType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'SCHEDULED', 'USER_INITIATED']]

### imageSource
- **Type**: typing.Optional[typing.Literal['AMAZON_MANAGED', 'AWS_MARKETPLACE', 'CUSTOM', 'IMPORTED']]

### deprecationTime
- **Type**: typing.Optional[datetime.datetime]

### lifecycleExecutionId
- **Type**: typing.Optional[str]


# ImageTestsConfigurationTypeDef

### imageTestsEnabled
- **Type**: typing.Optional[bool]

### timeoutMinutes
- **Type**: typing.Optional[int]


# ImageTypeDef

### arn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['AMI', 'DOCKER']]

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

### enhancedImageMetadataEnabled
- **Type**: typing.Optional[bool]

### osVersion
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageStateTypeDef]

### imageRecipe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageRecipeTypeDef]

### containerRecipe
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ContainerRecipeTypeDef]

### sourcePipelineName
- **Type**: typing.Optional[str]

### sourcePipelineArn
- **Type**: typing.Optional[str]

### infrastructureConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.InfrastructureConfigurationTypeDef]

### distributionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionConfigurationTypeDef]

### imageTestsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageTestsConfigurationTypeDef]

### dateCreated
- **Type**: typing.Optional[str]

### outputResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.OutputResourcesTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### buildType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'SCHEDULED', 'USER_INITIATED']]

### imageSource
- **Type**: typing.Optional[typing.Literal['AMAZON_MANAGED', 'AWS_MARKETPLACE', 'CUSTOM', 'IMPORTED']]

### scanState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanStateTypeDef]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationOutputTypeDef]

### deprecationTime
- **Type**: typing.Optional[datetime.datetime]

### lifecycleExecutionId
- **Type**: typing.Optional[str]

### executionRole
- **Type**: typing.Optional[str]

### workflows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationOutputTypeDef]]


# ImageVersionTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['AMI', 'DOCKER']]

### version
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['Linux', 'Windows']]

### osVersion
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### buildType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'SCHEDULED', 'USER_INITIATED']]

### imageSource
- **Type**: typing.Optional[typing.Literal['AMAZON_MANAGED', 'AWS_MARKETPLACE', 'CUSTOM', 'IMPORTED']]


# ImportComponentRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BUILD', 'TEST']
- **Required**: Yes

### format
- **Type**: typing.Literal['SHELL']
- **Required**: Yes

### platform
- **Type**: typing.Literal['Linux', 'Windows']
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### changeDescription
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[str]

### uri
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


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


# ImportVmImageRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### semanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### platform
- **Type**: typing.Literal['Linux', 'Windows']
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


# LifecyclePolicyDetailActionTypeDef

### type
- **Type**: typing.Literal['DELETE', 'DEPRECATE', 'DISABLE']
- **Required**: Yes

### includeResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailActionIncludeResourcesTypeDef]


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


# LifecyclePolicyDetailExclusionRulesOutputTypeDef

### tagMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### amis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef]


# LifecyclePolicyDetailExclusionRulesTypeDef

### tagMap
- **Type**: typing.Optional[typing.Mapping[str, str]]

### amis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisTypeDef]


# LifecyclePolicyDetailFilterTypeDef

### type
- **Type**: typing.Literal['AGE', 'COUNT']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes

### unit
- **Type**: typing.Optional[typing.Literal['DAYS', 'MONTHS', 'WEEKS', 'YEARS']]

### retainAtLeast
- **Type**: typing.Optional[int]


# LifecyclePolicyDetailOutputTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailActionTypeDef'>
- **Required**: Yes

### filter
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailFilterTypeDef'>
- **Required**: Yes

### exclusionRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesOutputTypeDef]


# LifecyclePolicyDetailTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailActionTypeDef'>
- **Required**: Yes

### filter
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailFilterTypeDef'>
- **Required**: Yes

### exclusionRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesTypeDef]


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


# ListComponentBuildVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListComponentsRequestRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['Amazon', 'Self', 'Shared', 'ThirdParty']]

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContainerRecipesRequestRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['Amazon', 'Self', 'Shared', 'ThirdParty']]

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionConfigurationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImageBuildVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImagePackagesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImagePipelineImagesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImagePipelinesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImageRecipesRequestRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['Amazon', 'Self', 'Shared', 'ThirdParty']]

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImageScanFindingAggregationsRequestRequestTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.FilterTypeDef]

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImageScanFindingsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImagesRequestRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['Amazon', 'Self', 'Shared', 'ThirdParty']]

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInfrastructureConfigurationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLifecycleExecutionResourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLifecycleExecutionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLifecyclePoliciesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWaitingWorkflowStepsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWaitingWorkflowStepsResponseTypeDef

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowStepExecutionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowBuildVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowExecutionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowStepExecutionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowsRequestRequestTypeDef

### owner
- **Type**: typing.Optional[typing.Literal['Amazon', 'Self', 'Shared', 'ThirdParty']]

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# PutComponentPolicyRequestRequestTypeDef

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


# PutContainerRecipePolicyRequestRequestTypeDef

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


# PutImagePolicyRequestRequestTypeDef

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


# PutImageRecipePolicyRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailExclusionRulesAmisTypeDef]


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


# SendWorkflowStepActionRequestRequestTypeDef

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

### all
- **Type**: typing.Optional[int]

### critical
- **Type**: typing.Optional[int]

### high
- **Type**: typing.Optional[int]

### medium
- **Type**: typing.Optional[int]


# StartImagePipelineExecutionRequestRequestTypeDef

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


# StartResourceStateUpdateRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDistributionConfigurationRequestRequestTypeDef

### distributionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### distributions
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionTypeDef, aws_resource_validator.pydantic_models.imagebuilder_classes.DistributionOutputTypeDef]]
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


# UpdateImagePipelineRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.ImageScanningConfigurationTypeDef]

### workflows
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationTypeDef, aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowConfigurationOutputTypeDef]]]

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


# UpdateInfrastructureConfigurationRequestRequestTypeDef

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


# UpdateLifecyclePolicyRequestRequestTypeDef

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
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailTypeDef, aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyDetailOutputTypeDef]]
- **Required**: Yes

### resourceSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.imagebuilder_classes.LifecyclePolicyResourceSelectionTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowParameterTypeDef]]

### parallelGroup
- **Type**: typing.Optional[str]

### onFailure
- **Type**: typing.Optional[typing.Literal['ABORT', 'CONTINUE']]


# WorkflowExecutionMetadataTypeDef

### workflowBuildVersionArn
- **Type**: typing.Optional[str]

### workflowExecutionId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['BUILD', 'DISTRIBUTION', 'TEST']]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'ROLLBACK_COMPLETED', 'ROLLBACK_IN_PROGRESS', 'RUNNING', 'SKIPPED']]

### message
- **Type**: typing.Optional[str]

### totalStepCount
- **Type**: typing.Optional[int]

### totalStepsSucceeded
- **Type**: typing.Optional[int]

### totalStepsFailed
- **Type**: typing.Optional[int]

### totalStepsSkipped
- **Type**: typing.Optional[int]

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]

### parallelGroup
- **Type**: typing.Optional[str]


# WorkflowParameterDetailTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]


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

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### changeDescription
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['BUILD', 'DISTRIBUTION', 'TEST']]

### owner
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowStateTypeDef]

### dateCreated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# WorkflowTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### changeDescription
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['BUILD', 'DISTRIBUTION', 'TEST']]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowStateTypeDef]

### owner
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.imagebuilder_classes.WorkflowParameterDetailTypeDef]]


# WorkflowVersionTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['BUILD', 'DISTRIBUTION', 'TEST']]

### owner
- **Type**: typing.Optional[str]

### dateCreated
- **Type**: typing.Optional[str]



# Bedrock Classes

# AutomatedEvaluationConfigOutputTypeDef

### datasetMetricConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationDatasetMetricConfigOutputTypeDef]
- **Required**: Yes

### evaluatorModelConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.EvaluatorModelConfigOutputTypeDef]


# AutomatedEvaluationConfigTypeDef

### datasetMetricConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationDatasetMetricConfigTypeDef]
- **Required**: Yes

### evaluatorModelConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.EvaluatorModelConfigTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteEvaluationJobErrorTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: typing.Optional[str]


# BatchDeleteEvaluationJobItemTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes


# BatchDeleteEvaluationJobRequestTypeDef

### jobIdentifiers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteEvaluationJobResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.BatchDeleteEvaluationJobErrorTypeDef]
- **Required**: Yes

### evaluationJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.BatchDeleteEvaluationJobItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BedrockEvaluatorModelTypeDef

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByteContentDocOutputTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: <class 'bytes'>
- **Required**: Yes


# ByteContentDocTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.BlobTypeDef'>
- **Required**: Yes


# CloudWatchConfigTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### largeDataDeliveryS3Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.S3ConfigTypeDef]


# CreateEvaluationJobRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### evaluationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationConfigUnionTypeDef'>
- **Required**: Yes

### inferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationInferenceConfigUnionTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationOutputDataConfigTypeDef'>
- **Required**: Yes

### jobDescription
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]

### customerEncryptionKeyId
- **Type**: typing.Optional[str]

### jobTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### applicationType
- **Type**: typing.Optional[typing.Literal['ModelEvaluation', 'RagEvaluation']]


# CreateEvaluationJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGuardrailRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### blockedInputMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### blockedOutputsMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### topicPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailTopicPolicyConfigTypeDef]

### contentPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContentPolicyConfigTypeDef]

### wordPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailWordPolicyConfigTypeDef]

### sensitiveInformationPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailSensitiveInformationPolicyConfigTypeDef]

### contextualGroundingPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContextualGroundingPolicyConfigTypeDef]

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### clientRequestToken
- **Type**: typing.Optional[str]


# CreateGuardrailResponseTypeDef

### guardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailArn
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGuardrailVersionRequestTypeDef

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]


# CreateGuardrailVersionResponseTypeDef

### guardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInferenceProfileRequestTypeDef

### inferenceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### modelSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.InferenceProfileModelSourceTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]


# CreateInferenceProfileResponseTypeDef

### inferenceProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMarketplaceModelEndpointRequestTypeDef

### modelSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### endpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EndpointConfigUnionTypeDef'>
- **Required**: Yes

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes

### acceptEula
- **Type**: typing.Optional[bool]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]


# CreateMarketplaceModelEndpointResponseTypeDef

### marketplaceModelEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.MarketplaceModelEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelCopyJobRequestTypeDef

### sourceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetModelName
- **Type**: <class 'str'>
- **Required**: Yes

### modelKmsKeyId
- **Type**: typing.Optional[str]

### targetModelTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### clientRequestToken
- **Type**: typing.Optional[str]


# CreateModelCopyJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelCustomizationJobRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### customModelName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### baseModelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.TrainingDataConfigUnionTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### customizationType
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']]

### customModelKmsKeyId
- **Type**: typing.Optional[str]

### jobTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### customModelTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### validationDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.ValidationDataConfigUnionTypeDef]

### hyperParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigUnionTypeDef]

### customizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.CustomizationConfigTypeDef]


# CreateModelCustomizationJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelImportJobRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### importedModelName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ModelDataSourceTypeDef'>
- **Required**: Yes

### jobTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### importedModelTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### clientRequestToken
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigUnionTypeDef]

### importedModelKmsKeyId
- **Type**: typing.Optional[str]


# CreateModelImportJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelInvocationJobRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### inputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ModelInvocationJobInputDataConfigTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ModelInvocationJobOutputDataConfigTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigUnionTypeDef]

### timeoutDurationInHours
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]


# CreateModelInvocationJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePromptRouterRequestTypeDef

### promptRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### models
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.PromptRouterTargetModelTypeDef]
- **Required**: Yes

### routingCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.RoutingCriteriaTypeDef'>
- **Required**: Yes

### fallbackModel
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.PromptRouterTargetModelTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]


# CreatePromptRouterResponseTypeDef

### promptRouterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProvisionedModelThroughputRequestTypeDef

### modelUnits
- **Type**: <class 'int'>
- **Required**: Yes

### provisionedModelName
- **Type**: <class 'str'>
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### commitmentDuration
- **Type**: typing.Optional[typing.Literal['OneMonth', 'SixMonths']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]


# CreateProvisionedModelThroughputResponseTypeDef

### provisionedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomModelSummaryTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### baseModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### baseModelName
- **Type**: <class 'str'>
- **Required**: Yes

### customizationType
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']]

### ownerAccountId
- **Type**: typing.Optional[str]


# CustomizationConfigTypeDef

### distillationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.DistillationConfigTypeDef]


# DeleteCustomModelRequestTypeDef

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGuardrailRequestTypeDef

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: typing.Optional[str]


# DeleteImportedModelRequestTypeDef

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInferenceProfileRequestTypeDef

### inferenceProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMarketplaceModelEndpointRequestTypeDef

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePromptRouterRequestTypeDef

### promptRouterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProvisionedModelThroughputRequestTypeDef

### provisionedModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterMarketplaceModelEndpointRequestTypeDef

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DistillationConfigTypeDef

### teacherModelConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.TeacherModelConfigTypeDef'>
- **Required**: Yes


# EndpointConfigOutputTypeDef

### sageMaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.SageMakerEndpointOutputTypeDef]


# EndpointConfigTypeDef

### sageMaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.SageMakerEndpointTypeDef]


# EndpointConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationBedrockModelTypeDef

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inferenceParams
- **Type**: typing.Optional[str]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PerformanceConfigurationTypeDef]


# EvaluationConfigOutputTypeDef

### automated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.AutomatedEvaluationConfigOutputTypeDef]

### human
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.HumanEvaluationConfigOutputTypeDef]


# EvaluationConfigTypeDef

### automated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.AutomatedEvaluationConfigTypeDef]

### human
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.HumanEvaluationConfigTypeDef]


# EvaluationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationDatasetLocationTypeDef

### s3Uri
- **Type**: typing.Optional[str]


# EvaluationDatasetMetricConfigOutputTypeDef

### taskType
- **Type**: typing.Literal['Classification', 'Custom', 'Generation', 'QuestionAndAnswer', 'Summarization']
- **Required**: Yes

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationDatasetTypeDef'>
- **Required**: Yes

### metricNames
- **Type**: typing.List[str]
- **Required**: Yes


# EvaluationDatasetMetricConfigTypeDef

### taskType
- **Type**: typing.Literal['Classification', 'Custom', 'Generation', 'QuestionAndAnswer', 'Summarization']
- **Required**: Yes

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationDatasetTypeDef'>
- **Required**: Yes

### metricNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# EvaluationDatasetTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datasetLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationDatasetLocationTypeDef]


# EvaluationInferenceConfigOutputTypeDef

### models
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationModelConfigTypeDef]]

### ragConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.RAGConfigOutputTypeDef]]


# EvaluationInferenceConfigTypeDef

### models
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationModelConfigTypeDef]]

### ragConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.RAGConfigTypeDef]]


# EvaluationInferenceConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationModelConfigTypeDef

### bedrockModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationBedrockModelTypeDef]


# EvaluationOutputDataConfigTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluationSummaryTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### jobType
- **Type**: typing.Literal['Automated', 'Human']
- **Required**: Yes

### evaluationTaskTypes
- **Type**: typing.List[typing.Literal['Classification', 'Custom', 'Generation', 'QuestionAndAnswer', 'Summarization']]
- **Required**: Yes

### modelIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### ragIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### evaluatorModelIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### applicationType
- **Type**: typing.Optional[typing.Literal['ModelEvaluation', 'RagEvaluation']]


# EvaluatorModelConfigOutputTypeDef

### bedrockEvaluatorModels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.BedrockEvaluatorModelTypeDef]]


# EvaluatorModelConfigTypeDef

### bedrockEvaluatorModels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.BedrockEvaluatorModelTypeDef]]


# ExternalSourceOutputTypeDef

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.S3ObjectDocTypeDef]

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.ByteContentDocOutputTypeDef]


# ExternalSourceTypeDef

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.S3ObjectDocTypeDef]

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.ByteContentDocTypeDef]


# ExternalSourcesGenerationConfigurationOutputTypeDef

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PromptTemplateTypeDef]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailConfigurationTypeDef]

### kbInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.KbInferenceConfigOutputTypeDef]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# ExternalSourcesGenerationConfigurationTypeDef

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PromptTemplateTypeDef]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailConfigurationTypeDef]

### kbInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.KbInferenceConfigTypeDef]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


# ExternalSourcesRetrieveAndGenerateConfigurationOutputTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ExternalSourceOutputTypeDef]
- **Required**: Yes

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.ExternalSourcesGenerationConfigurationOutputTypeDef]


# ExternalSourcesRetrieveAndGenerateConfigurationTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.ExternalSourceTypeDef]
- **Required**: Yes

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.ExternalSourcesGenerationConfigurationTypeDef]


# FilterAttributeOutputTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# FilterAttributeTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# FoundationModelDetailsTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: typing.Optional[str]

### providerName
- **Type**: typing.Optional[str]

### inputModalities
- **Type**: typing.Optional[typing.List[typing.Literal['EMBEDDING', 'IMAGE', 'TEXT']]]

### outputModalities
- **Type**: typing.Optional[typing.List[typing.Literal['EMBEDDING', 'IMAGE', 'TEXT']]]

### responseStreamingSupported
- **Type**: typing.Optional[bool]

### customizationsSupported
- **Type**: typing.Optional[typing.List[typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']]]

### inferenceTypesSupported
- **Type**: typing.Optional[typing.List[typing.Literal['ON_DEMAND', 'PROVISIONED']]]

### modelLifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.FoundationModelLifecycleTypeDef]


# FoundationModelLifecycleTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'LEGACY']
- **Required**: Yes


# FoundationModelSummaryTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: typing.Optional[str]

### providerName
- **Type**: typing.Optional[str]

### inputModalities
- **Type**: typing.Optional[typing.List[typing.Literal['EMBEDDING', 'IMAGE', 'TEXT']]]

### outputModalities
- **Type**: typing.Optional[typing.List[typing.Literal['EMBEDDING', 'IMAGE', 'TEXT']]]

### responseStreamingSupported
- **Type**: typing.Optional[bool]

### customizationsSupported
- **Type**: typing.Optional[typing.List[typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']]]

### inferenceTypesSupported
- **Type**: typing.Optional[typing.List[typing.Literal['ON_DEMAND', 'PROVISIONED']]]

### modelLifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.FoundationModelLifecycleTypeDef]


# GenerationConfigurationOutputTypeDef

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PromptTemplateTypeDef]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailConfigurationTypeDef]

### kbInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.KbInferenceConfigOutputTypeDef]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# GenerationConfigurationTypeDef

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PromptTemplateTypeDef]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailConfigurationTypeDef]

### kbInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.KbInferenceConfigTypeDef]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


# GetCustomModelRequestTypeDef

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomModelResponseTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### baseModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### customizationType
- **Type**: typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']
- **Required**: Yes

### modelKmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### hyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### trainingDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.TrainingDataConfigOutputTypeDef'>
- **Required**: Yes

### validationDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ValidationDataConfigOutputTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### trainingMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.TrainingMetricsTypeDef'>
- **Required**: Yes

### validationMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ValidatorMetricTypeDef]
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.CustomizationConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEvaluationJobRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvaluationJobResponseTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobDescription
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### customerEncryptionKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### jobType
- **Type**: typing.Literal['Automated', 'Human']
- **Required**: Yes

### applicationType
- **Type**: typing.Literal['ModelEvaluation', 'RagEvaluation']
- **Required**: Yes

### evaluationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationConfigOutputTypeDef'>
- **Required**: Yes

### inferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationInferenceConfigOutputTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationOutputDataConfigTypeDef'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureMessages
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFoundationModelRequestTypeDef

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFoundationModelResponseTypeDef

### modelDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.FoundationModelDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGuardrailRequestTypeDef

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: typing.Optional[str]


# GetGuardrailResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailArn
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'READY', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### topicPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.GuardrailTopicPolicyTypeDef'>
- **Required**: Yes

### contentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContentPolicyTypeDef'>
- **Required**: Yes

### wordPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.GuardrailWordPolicyTypeDef'>
- **Required**: Yes

### sensitiveInformationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.GuardrailSensitiveInformationPolicyTypeDef'>
- **Required**: Yes

### contextualGroundingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContextualGroundingPolicyTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusReasons
- **Type**: typing.List[str]
- **Required**: Yes

### failureRecommendations
- **Type**: typing.List[str]
- **Required**: Yes

### blockedInputMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### blockedOutputsMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImportedModelRequestTypeDef

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportedModelResponseTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ModelDataSourceTypeDef'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modelArchitecture
- **Type**: <class 'str'>
- **Required**: Yes

### modelKmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### instructSupported
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInferenceProfileRequestTypeDef

### inferenceProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMarketplaceModelEndpointRequestTypeDef

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetMarketplaceModelEndpointResponseTypeDef

### marketplaceModelEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.MarketplaceModelEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelCopyJobRequestTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelCopyJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### targetModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetModelName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetModelKmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetModelTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### sourceModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelCustomizationJobRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelCustomizationJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### outputModelName
- **Type**: <class 'str'>
- **Required**: Yes

### outputModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### baseModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### hyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### trainingDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.TrainingDataConfigOutputTypeDef'>
- **Required**: Yes

### validationDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ValidationDataConfigOutputTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### customizationType
- **Type**: typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']
- **Required**: Yes

### outputModelKmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### trainingMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.TrainingMetricsTypeDef'>
- **Required**: Yes

### validationMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ValidatorMetricTypeDef]
- **Required**: Yes

### vpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigOutputTypeDef'>
- **Required**: Yes

### customizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.CustomizationConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelImportJobRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelImportJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### importedModelName
- **Type**: <class 'str'>
- **Required**: Yes

### importedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ModelDataSourceTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### vpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigOutputTypeDef'>
- **Required**: Yes

### importedModelKmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelInvocationJobRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelInvocationJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Expired', 'Failed', 'InProgress', 'PartiallyCompleted', 'Scheduled', 'Stopped', 'Stopping', 'Submitted', 'Validating']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### submitTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### inputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ModelInvocationJobInputDataConfigTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ModelInvocationJobOutputDataConfigTypeDef'>
- **Required**: Yes

### vpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigOutputTypeDef'>
- **Required**: Yes

### timeoutDurationInHours
- **Type**: <class 'int'>
- **Required**: Yes

### jobExpirationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelInvocationLoggingConfigurationResponseTypeDef

### loggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.LoggingConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPromptRouterRequestTypeDef

### promptRouterArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetProvisionedModelThroughputRequestTypeDef

### provisionedModelId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProvisionedModelThroughputResponseTypeDef

### modelUnits
- **Type**: <class 'int'>
- **Required**: Yes

### desiredModelUnits
- **Type**: <class 'int'>
- **Required**: Yes

### provisionedModelName
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### desiredModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### foundationModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Creating', 'Failed', 'InService', 'Updating']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### commitmentDuration
- **Type**: typing.Literal['OneMonth', 'SixMonths']
- **Required**: Yes

### commitmentExpirationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GuardrailConfigurationTypeDef

### guardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GuardrailContentFilterConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContentFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContentPolicyConfigTypeDef

### filtersConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContentFilterConfigTypeDef]
- **Required**: Yes


# GuardrailContentPolicyTypeDef

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContentFilterTypeDef]]


# GuardrailContextualGroundingFilterConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContextualGroundingFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContextualGroundingPolicyConfigTypeDef

### filtersConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContextualGroundingFilterConfigTypeDef]
- **Required**: Yes


# GuardrailContextualGroundingPolicyTypeDef

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContextualGroundingFilterTypeDef]
- **Required**: Yes


# GuardrailManagedWordsConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailManagedWordsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailPiiEntityConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailPiiEntityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailRegexConfigTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Literal['ANONYMIZE', 'BLOCK']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# GuardrailRegexTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Literal['ANONYMIZE', 'BLOCK']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# GuardrailSensitiveInformationPolicyConfigTypeDef

### piiEntitiesConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailPiiEntityConfigTypeDef]]

### regexesConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailRegexConfigTypeDef]]


# GuardrailSensitiveInformationPolicyTypeDef

### piiEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailPiiEntityTypeDef]]

### regexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailRegexTypeDef]]


# GuardrailSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailTopicConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailTopicPolicyConfigTypeDef

### topicsConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailTopicConfigTypeDef]
- **Required**: Yes


# GuardrailTopicPolicyTypeDef

### topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailTopicTypeDef]
- **Required**: Yes


# GuardrailTopicTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailWordConfigTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# GuardrailWordPolicyConfigTypeDef

### wordsConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailWordConfigTypeDef]]

### managedWordListsConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailManagedWordsConfigTypeDef]]


# GuardrailWordPolicyTypeDef

### words
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailWordTypeDef]]

### managedWordLists
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailManagedWordsTypeDef]]


# GuardrailWordTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# HumanEvaluationConfigOutputTypeDef

### datasetMetricConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationDatasetMetricConfigOutputTypeDef]
- **Required**: Yes

### humanWorkflowConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.HumanWorkflowConfigTypeDef]

### customMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.HumanEvaluationCustomMetricTypeDef]]


# HumanEvaluationConfigTypeDef

### datasetMetricConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationDatasetMetricConfigTypeDef]
- **Required**: Yes

### humanWorkflowConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.HumanWorkflowConfigTypeDef]

### customMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.HumanEvaluationCustomMetricTypeDef]]


# HumanEvaluationCustomMetricTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ratingMethod
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# HumanWorkflowConfigTypeDef

### flowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### instructions
- **Type**: typing.Optional[str]


# ImportedModelSummaryTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### instructSupported
- **Type**: typing.Optional[bool]

### modelArchitecture
- **Type**: typing.Optional[str]


# InferenceProfileModelSourceTypeDef

### copyFrom
- **Type**: typing.Optional[str]


# InferenceProfileModelTypeDef

### modelArn
- **Type**: typing.Optional[str]


# InferenceProfileSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InvocationLogSourceTypeDef

### s3Uri
- **Type**: typing.Optional[str]


# InvocationLogsConfigOutputTypeDef

### invocationLogSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.InvocationLogSourceTypeDef'>
- **Required**: Yes

### usePromptResponse
- **Type**: typing.Optional[bool]

### requestMetadataFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.RequestMetadataFiltersOutputTypeDef]


# InvocationLogsConfigTypeDef

### invocationLogSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.InvocationLogSourceTypeDef'>
- **Required**: Yes

### usePromptResponse
- **Type**: typing.Optional[bool]

### requestMetadataFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.RequestMetadataFiltersTypeDef]


# KbInferenceConfigOutputTypeDef

### textInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TextInferenceConfigOutputTypeDef]


# KbInferenceConfigTypeDef

### textInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TextInferenceConfigTypeDef]


# KnowledgeBaseConfigOutputTypeDef

### retrieveConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.RetrieveConfigOutputTypeDef]

### retrieveAndGenerateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.RetrieveAndGenerateConfigurationOutputTypeDef]


# KnowledgeBaseConfigTypeDef

### retrieveConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.RetrieveConfigTypeDef]

### retrieveAndGenerateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.RetrieveAndGenerateConfigurationTypeDef]


# KnowledgeBaseRetrievalConfigurationOutputTypeDef

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.KnowledgeBaseVectorSearchConfigurationOutputTypeDef'>
- **Required**: Yes


# KnowledgeBaseRetrievalConfigurationTypeDef

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.KnowledgeBaseVectorSearchConfigurationTypeDef'>
- **Required**: Yes


# KnowledgeBaseRetrieveAndGenerateConfigurationOutputTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.KnowledgeBaseRetrievalConfigurationOutputTypeDef]

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GenerationConfigurationOutputTypeDef]

### orchestrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.OrchestrationConfigurationTypeDef]


# KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.KnowledgeBaseRetrievalConfigurationTypeDef]

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GenerationConfigurationTypeDef]

### orchestrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.OrchestrationConfigurationTypeDef]


# KnowledgeBaseVectorSearchConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KnowledgeBaseVectorSearchConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListCustomModelsRequestPaginateTypeDef

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### nameContains
- **Type**: typing.Optional[str]

### baseModelArnEquals
- **Type**: typing.Optional[str]

### foundationModelArnEquals
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### isOwned
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListCustomModelsRequestTypeDef

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### nameContains
- **Type**: typing.Optional[str]

### baseModelArnEquals
- **Type**: typing.Optional[str]

### foundationModelArnEquals
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### isOwned
- **Type**: typing.Optional[bool]


# ListCustomModelsResponseTypeDef

### modelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.CustomModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEvaluationJobsRequestPaginateTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### applicationTypeEquals
- **Type**: typing.Optional[typing.Literal['ModelEvaluation', 'RagEvaluation']]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListEvaluationJobsRequestTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### applicationTypeEquals
- **Type**: typing.Optional[typing.Literal['ModelEvaluation', 'RagEvaluation']]

### nameContains
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListEvaluationJobsResponseTypeDef

### jobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFoundationModelsRequestTypeDef

### byProvider
- **Type**: typing.Optional[str]

### byCustomizationType
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']]

### byOutputModality
- **Type**: typing.Optional[typing.Literal['EMBEDDING', 'IMAGE', 'TEXT']]

### byInferenceType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'PROVISIONED']]


# ListFoundationModelsResponseTypeDef

### modelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.FoundationModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGuardrailsRequestPaginateTypeDef

### guardrailIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListGuardrailsRequestTypeDef

### guardrailIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListGuardrailsResponseTypeDef

### guardrails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportedModelsRequestPaginateTypeDef

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListImportedModelsRequestTypeDef

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### nameContains
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListImportedModelsResponseTypeDef

### modelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ImportedModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInferenceProfilesRequestPaginateTypeDef

### typeEquals
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'SYSTEM_DEFINED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListInferenceProfilesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### typeEquals
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'SYSTEM_DEFINED']]


# ListInferenceProfilesResponseTypeDef

### inferenceProfileSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.InferenceProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMarketplaceModelEndpointsRequestPaginateTypeDef

### modelSourceEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListMarketplaceModelEndpointsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### modelSourceEquals
- **Type**: typing.Optional[str]


# ListMarketplaceModelEndpointsResponseTypeDef

### marketplaceModelEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.MarketplaceModelEndpointSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelCopyJobsRequestPaginateTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### sourceAccountEquals
- **Type**: typing.Optional[str]

### sourceModelArnEquals
- **Type**: typing.Optional[str]

### targetModelNameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListModelCopyJobsRequestTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### sourceAccountEquals
- **Type**: typing.Optional[str]

### sourceModelArnEquals
- **Type**: typing.Optional[str]

### targetModelNameContains
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelCopyJobsResponseTypeDef

### modelCopyJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ModelCopyJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelCustomizationJobsRequestPaginateTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListModelCustomizationJobsRequestTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### nameContains
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelCustomizationJobsResponseTypeDef

### modelCustomizationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ModelCustomizationJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelImportJobsRequestPaginateTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListModelImportJobsRequestTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### nameContains
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelImportJobsResponseTypeDef

### modelImportJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ModelImportJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelInvocationJobsRequestPaginateTypeDef

### submitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### submitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Expired', 'Failed', 'InProgress', 'PartiallyCompleted', 'Scheduled', 'Stopped', 'Stopping', 'Submitted', 'Validating']]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListModelInvocationJobsRequestTypeDef

### submitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### submitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Expired', 'Failed', 'InProgress', 'PartiallyCompleted', 'Scheduled', 'Stopped', 'Stopping', 'Submitted', 'Validating']]

### nameContains
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelInvocationJobsResponseTypeDef

### invocationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ModelInvocationJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPromptRoutersResponseTypeDef

### promptRouterSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.PromptRouterSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProvisionedModelThroughputsRequestPaginateTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Failed', 'InService', 'Updating']]

### modelArnEquals
- **Type**: typing.Optional[str]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListProvisionedModelThroughputsRequestTypeDef

### creationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### creationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Failed', 'InService', 'Updating']]

### modelArnEquals
- **Type**: typing.Optional[str]

### nameContains
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListProvisionedModelThroughputsResponseTypeDef

### provisionedModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ProvisionedModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingConfigTypeDef

### cloudWatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.CloudWatchConfigTypeDef]

### s3Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.S3ConfigTypeDef]

### textDataDeliveryEnabled
- **Type**: typing.Optional[bool]

### imageDataDeliveryEnabled
- **Type**: typing.Optional[bool]

### embeddingDataDeliveryEnabled
- **Type**: typing.Optional[bool]

### videoDataDeliveryEnabled
- **Type**: typing.Optional[bool]


# MarketplaceModelEndpointSummaryTypeDef

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['INCOMPATIBLE_ENDPOINT', 'REGISTERED']]

### statusMessage
- **Type**: typing.Optional[str]


# MarketplaceModelEndpointTypeDef

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EndpointConfigOutputTypeDef'>
- **Required**: Yes

### endpointStatus
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['INCOMPATIBLE_ENDPOINT', 'REGISTERED']]

### statusMessage
- **Type**: typing.Optional[str]

### endpointStatusMessage
- **Type**: typing.Optional[str]


# ModelCopyJobSummaryTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### targetModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetModelName
- **Type**: typing.Optional[str]

### targetModelKmsKeyArn
- **Type**: typing.Optional[str]

### targetModelTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### failureMessage
- **Type**: typing.Optional[str]

### sourceModelName
- **Type**: typing.Optional[str]


# ModelCustomizationJobSummaryTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### baseModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### customModelArn
- **Type**: typing.Optional[str]

### customModelName
- **Type**: typing.Optional[str]

### customizationType
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']]


# ModelDataSourceTypeDef

### s3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.S3DataSourceTypeDef]


# ModelImportJobSummaryTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### importedModelArn
- **Type**: typing.Optional[str]

### importedModelName
- **Type**: typing.Optional[str]


# ModelInvocationJobInputDataConfigTypeDef

### s3InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.ModelInvocationJobS3InputDataConfigTypeDef]


# ModelInvocationJobOutputDataConfigTypeDef

### s3OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.ModelInvocationJobS3OutputDataConfigTypeDef]


# ModelInvocationJobS3InputDataConfigTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### s3InputFormat
- **Type**: typing.Optional[typing.Literal['JSONL']]

### s3BucketOwner
- **Type**: typing.Optional[str]


# ModelInvocationJobS3OutputDataConfigTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### s3EncryptionKeyId
- **Type**: typing.Optional[str]

### s3BucketOwner
- **Type**: typing.Optional[str]


# ModelInvocationJobSummaryTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### submitTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### inputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ModelInvocationJobInputDataConfigTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ModelInvocationJobOutputDataConfigTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Completed', 'Expired', 'Failed', 'InProgress', 'PartiallyCompleted', 'Scheduled', 'Stopped', 'Stopping', 'Submitted', 'Validating']]

### message
- **Type**: typing.Optional[str]

### lastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigOutputTypeDef]

### timeoutDurationInHours
- **Type**: typing.Optional[int]

### jobExpirationTime
- **Type**: typing.Optional[datetime.datetime]


# OrchestrationConfigurationTypeDef

### queryTransformationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.QueryTransformationConfigurationTypeDef'>
- **Required**: Yes


# OutputDataConfigTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceConfigurationTypeDef

### latency
- **Type**: typing.Optional[typing.Literal['optimized', 'standard']]


# PromptRouterSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptRouterTargetModelTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes


# PromptTemplateTypeDef

### textPromptTemplate
- **Type**: typing.Optional[str]


# ProvisionedModelSummaryTypeDef

### provisionedModelName
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### desiredModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### foundationModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelUnits
- **Type**: <class 'int'>
- **Required**: Yes

### desiredModelUnits
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Creating', 'Failed', 'InService', 'Updating']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### commitmentDuration
- **Type**: typing.Optional[typing.Literal['OneMonth', 'SixMonths']]

### commitmentExpirationTime
- **Type**: typing.Optional[datetime.datetime]


# PutModelInvocationLoggingConfigurationRequestTypeDef

### loggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.LoggingConfigTypeDef'>
- **Required**: Yes


# QueryTransformationConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RAGConfigOutputTypeDef

### knowledgeBaseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.KnowledgeBaseConfigOutputTypeDef]


# RAGConfigTypeDef

### knowledgeBaseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.KnowledgeBaseConfigTypeDef]


# RegisterMarketplaceModelEndpointRequestTypeDef

### endpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### modelSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterMarketplaceModelEndpointResponseTypeDef

### marketplaceModelEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.MarketplaceModelEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RequestMetadataBaseFiltersOutputTypeDef

### equals
- **Type**: typing.Optional[typing.Dict[str, str]]

### notEquals
- **Type**: typing.Optional[typing.Dict[str, str]]


# RequestMetadataBaseFiltersTypeDef

### equals
- **Type**: typing.Optional[typing.Mapping[str, str]]

### notEquals
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RequestMetadataFiltersOutputTypeDef

### equals
- **Type**: typing.Optional[typing.Dict[str, str]]

### notEquals
- **Type**: typing.Optional[typing.Dict[str, str]]

### andAll
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.RequestMetadataBaseFiltersOutputTypeDef]]

### orAll
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.RequestMetadataBaseFiltersOutputTypeDef]]


# RequestMetadataFiltersTypeDef

### equals
- **Type**: typing.Optional[typing.Mapping[str, str]]

### notEquals
- **Type**: typing.Optional[typing.Mapping[str, str]]

### andAll
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.RequestMetadataBaseFiltersTypeDef]]

### orAll
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.RequestMetadataBaseFiltersTypeDef]]


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


# RetrieveAndGenerateConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RetrieveAndGenerateConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RetrieveConfigOutputTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseRetrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.KnowledgeBaseRetrievalConfigurationOutputTypeDef'>
- **Required**: Yes


# RetrieveConfigTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseRetrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.KnowledgeBaseRetrievalConfigurationTypeDef'>
- **Required**: Yes


# RoutingCriteriaTypeDef

### responseQualityDifference
- **Type**: <class 'float'>
- **Required**: Yes


# S3ConfigTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# S3DataSourceTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# S3ObjectDocTypeDef

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# SageMakerEndpointOutputTypeDef

### initialInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### executionRole
- **Type**: <class 'str'>
- **Required**: Yes

### kmsEncryptionKey
- **Type**: typing.Optional[str]

### vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigOutputTypeDef]


# SageMakerEndpointTypeDef

### initialInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### executionRole
- **Type**: <class 'str'>
- **Required**: Yes

### kmsEncryptionKey
- **Type**: typing.Optional[str]

### vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigTypeDef]


# StopEvaluationJobRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopModelCustomizationJobRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopModelInvocationJobRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TeacherModelConfigTypeDef

### teacherModelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResponseLengthForInference
- **Type**: typing.Optional[int]


# TextInferenceConfigOutputTypeDef

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.List[str]]


# TextInferenceConfigTypeDef

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.Sequence[str]]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrainingDataConfigOutputTypeDef

### s3Uri
- **Type**: typing.Optional[str]

### invocationLogsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.InvocationLogsConfigOutputTypeDef]


# TrainingDataConfigTypeDef

### s3Uri
- **Type**: typing.Optional[str]

### invocationLogsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.InvocationLogsConfigTypeDef]


# TrainingDataConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrainingMetricsTypeDef

### trainingLoss
- **Type**: typing.Optional[float]


# UntagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGuardrailRequestTypeDef

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### blockedInputMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### blockedOutputsMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### topicPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailTopicPolicyConfigTypeDef]

### contentPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContentPolicyConfigTypeDef]

### wordPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailWordPolicyConfigTypeDef]

### sensitiveInformationPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailSensitiveInformationPolicyConfigTypeDef]

### contextualGroundingPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContextualGroundingPolicyConfigTypeDef]

### kmsKeyId
- **Type**: typing.Optional[str]


# UpdateGuardrailResponseTypeDef

### guardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailArn
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMarketplaceModelEndpointRequestTypeDef

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### endpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EndpointConfigUnionTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdateMarketplaceModelEndpointResponseTypeDef

### marketplaceModelEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.MarketplaceModelEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProvisionedModelThroughputRequestTypeDef

### provisionedModelId
- **Type**: <class 'str'>
- **Required**: Yes

### desiredProvisionedModelName
- **Type**: typing.Optional[str]

### desiredModelId
- **Type**: typing.Optional[str]


# ValidationDataConfigOutputTypeDef

### validators
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ValidatorTypeDef]
- **Required**: Yes


# ValidationDataConfigTypeDef

### validators
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.ValidatorTypeDef]
- **Required**: Yes


# ValidationDataConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ValidatorMetricTypeDef

### validationLoss
- **Type**: typing.Optional[float]


# ValidatorTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# VpcConfigOutputTypeDef

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigTypeDef

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


# Bedrock Classes

# AutomatedEvaluationConfig

### datasetMetricConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationDatasetMetricConfig]
- **Required**: Yes

### evaluatorModelConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluatorModelConfig]


# AutomatedEvaluationConfigOutput

### datasetMetricConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationDatasetMetricConfigOutput]
- **Required**: Yes

### evaluatorModelConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluatorModelConfigOutput]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteEvaluationJobError

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: typing.Optional[str]


# BatchDeleteEvaluationJobItem

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes


# BatchDeleteEvaluationJobRequest

### jobIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteEvaluationJobResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.BatchDeleteEvaluationJobError]
- **Required**: Yes

### evaluationJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.BatchDeleteEvaluationJobItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# BedrockEvaluatorModel

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ByteContentDoc

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes


# ByteContentDocOutput

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: <class 'bytes'>
- **Required**: Yes


# CloudWatchConfig

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### largeDataDeliveryS3Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.S3Config]


# CreateEvaluationJobRequest

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### evaluationConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationConfig, aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationConfigOutput]
- **Required**: Yes

### inferenceConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationInferenceConfig, aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationInferenceConfigOutput]
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationOutputDataConfig'>
- **Required**: Yes

### jobDescription
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]

### customerEncryptionKeyId
- **Type**: typing.Optional[str]

### jobTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]

### applicationType
- **Type**: typing.Optional[typing.Literal['ModelEvaluation', 'RagEvaluation']]


# CreateEvaluationJobResponse

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGuardrailRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailTopicPolicyConfig]

### contentPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContentPolicyConfig]

### wordPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailWordPolicyConfig]

### sensitiveInformationPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailSensitiveInformationPolicyConfig]

### contextualGroundingPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContextualGroundingPolicyConfig]

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]

### clientRequestToken
- **Type**: typing.Optional[str]


# CreateGuardrailResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGuardrailVersionRequest

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]


# CreateGuardrailVersionResponse

### guardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInferenceProfileRequest

### inferenceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### modelSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.InferenceProfileModelSource'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]


# CreateInferenceProfileResponse

### inferenceProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMarketplaceModelEndpointRequest

### modelSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### endpointConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EndpointConfig, aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EndpointConfigOutput]
- **Required**: Yes

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes

### acceptEula
- **Type**: typing.Optional[bool]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]


# CreateMarketplaceModelEndpointResponse

### marketplaceModelEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.MarketplaceModelEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelCopyJobRequest

### sourceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetModelName
- **Type**: <class 'str'>
- **Required**: Yes

### modelKmsKeyId
- **Type**: typing.Optional[str]

### targetModelTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]

### clientRequestToken
- **Type**: typing.Optional[str]


# CreateModelCopyJobResponse

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelCustomizationJobRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.TrainingDataConfig, aws_resource_validator.pydantic_models.bedrock.bedrock_classes.TrainingDataConfigOutput]
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.OutputDataConfig'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### customizationType
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']]

### customModelKmsKeyId
- **Type**: typing.Optional[str]

### jobTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]

### customModelTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]

### validationDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ValidationDataConfig, aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ValidationDataConfigOutput, NoneType]

### hyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfig, aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfigOutput, NoneType]

### customizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.CustomizationConfig]


# CreateModelCustomizationJobResponse

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelImportJobRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelDataSource'>
- **Required**: Yes

### jobTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]

### importedModelTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]

### clientRequestToken
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfig, aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfigOutput, NoneType]

### importedModelKmsKeyId
- **Type**: typing.Optional[str]


# CreateModelImportJobResponse

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelInvocationJobRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelInvocationJobInputDataConfig'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelInvocationJobOutputDataConfig'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### vpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfig, aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfigOutput, NoneType]

### timeoutDurationInHours
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]


# CreateModelInvocationJobResponse

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePromptRouterRequest

### promptRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptRouterTargetModel]
- **Required**: Yes

### routingCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RoutingCriteria'>
- **Required**: Yes

### fallbackModel
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptRouterTargetModel'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]


# CreatePromptRouterResponse

### promptRouterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProvisionedModelThroughputRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]


# CreateProvisionedModelThroughputResponse

### provisionedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# CustomModelSummary

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


# CustomizationConfig

### distillationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.DistillationConfig]


# DeleteCustomModelRequest

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGuardrailRequest

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: typing.Optional[str]


# DeleteImportedModelRequest

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInferenceProfileRequest

### inferenceProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMarketplaceModelEndpointRequest

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePromptRouterRequest

### promptRouterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProvisionedModelThroughputRequest

### provisionedModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterMarketplaceModelEndpointRequest

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DistillationConfig

### teacherModelConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.TeacherModelConfig'>
- **Required**: Yes


# EndpointConfig

### sageMaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.SageMakerEndpoint]


# EndpointConfigOutput

### sageMaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.SageMakerEndpointOutput]


# EvaluationBedrockModel

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inferenceParams
- **Type**: typing.Optional[str]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PerformanceConfiguration]


# EvaluationConfig

### automated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.AutomatedEvaluationConfig]

### human
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.HumanEvaluationConfig]


# EvaluationConfigOutput

### automated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.AutomatedEvaluationConfigOutput]

### human
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.HumanEvaluationConfigOutput]


# EvaluationDataset

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datasetLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationDatasetLocation]


# EvaluationDatasetLocation

### s3Uri
- **Type**: typing.Optional[str]


# EvaluationDatasetMetricConfig

### taskType
- **Type**: typing.Literal['Classification', 'Custom', 'Generation', 'QuestionAndAnswer', 'Summarization']
- **Required**: Yes

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationDataset'>
- **Required**: Yes

### metricNames
- **Type**: typing.List[str]
- **Required**: Yes


# EvaluationDatasetMetricConfigOutput

### taskType
- **Type**: typing.Literal['Classification', 'Custom', 'Generation', 'QuestionAndAnswer', 'Summarization']
- **Required**: Yes

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationDataset'>
- **Required**: Yes

### metricNames
- **Type**: typing.List[str]
- **Required**: Yes


# EvaluationInferenceConfig

### models
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationModelConfig]]

### ragConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RAGConfig]]


# EvaluationInferenceConfigOutput

### models
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationModelConfig]]

### ragConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RAGConfigOutput]]


# EvaluationModelConfig

### bedrockModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationBedrockModel]


# EvaluationOutputDataConfig

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluationSummary

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


# EvaluatorModelConfig

### bedrockEvaluatorModels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.BedrockEvaluatorModel]]


# EvaluatorModelConfigOutput

### bedrockEvaluatorModels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.BedrockEvaluatorModel]]


# ExternalSource

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.S3ObjectDoc]

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ByteContentDoc]


# ExternalSourceOutput

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.S3ObjectDoc]

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ByteContentDocOutput]


# ExternalSourcesGenerationConfiguration

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptTemplate]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailConfiguration]

### kbInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KbInferenceConfig]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# ExternalSourcesGenerationConfigurationOutput

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptTemplate]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailConfiguration]

### kbInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KbInferenceConfigOutput]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# ExternalSourcesRetrieveAndGenerateConfiguration

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ExternalSource]
- **Required**: Yes

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ExternalSourcesGenerationConfiguration]


# ExternalSourcesRetrieveAndGenerateConfigurationOutput

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ExternalSourceOutput]
- **Required**: Yes

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ExternalSourcesGenerationConfigurationOutput]


# FilterAttribute

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# FilterAttributeOutput

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# FoundationModelDetails

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FoundationModelLifecycle]


# FoundationModelLifecycle

### status
- **Type**: typing.Literal['ACTIVE', 'LEGACY']
- **Required**: Yes


# FoundationModelSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FoundationModelLifecycle]


# GenerationConfiguration

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptTemplate]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailConfiguration]

### kbInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KbInferenceConfig]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# GenerationConfigurationOutput

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptTemplate]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailConfiguration]

### kbInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KbInferenceConfigOutput]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# GetCustomModelRequest

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.TrainingDataConfigOutput'>
- **Required**: Yes

### validationDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ValidationDataConfigOutput'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.OutputDataConfig'>
- **Required**: Yes

### trainingMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.TrainingMetrics'>
- **Required**: Yes

### validationMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ValidatorMetric]
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.CustomizationConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetEvaluationJobRequest

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvaluationJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationConfigOutput'>
- **Required**: Yes

### inferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationInferenceConfigOutput'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationOutputDataConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetFoundationModelRequest

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFoundationModelResponse

### modelDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FoundationModelDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetGuardrailRequest

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: typing.Optional[str]


# GetGuardrailResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailTopicPolicy'>
- **Required**: Yes

### contentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContentPolicy'>
- **Required**: Yes

### wordPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailWordPolicy'>
- **Required**: Yes

### sensitiveInformationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailSensitiveInformationPolicy'>
- **Required**: Yes

### contextualGroundingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContextualGroundingPolicy'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetImportedModelRequest

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportedModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelDataSource'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetInferenceProfileRequest

### inferenceProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetInferenceProfileResponse

### inferenceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### inferenceProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.InferenceProfileModel]
- **Required**: Yes

### inferenceProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### type
- **Type**: typing.Literal['APPLICATION', 'SYSTEM_DEFINED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetMarketplaceModelEndpointRequest

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetMarketplaceModelEndpointResponse

### marketplaceModelEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.MarketplaceModelEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelCopyJobRequest

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelCopyJobResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### sourceModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelCustomizationJobRequest

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelCustomizationJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.TrainingDataConfigOutput'>
- **Required**: Yes

### validationDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ValidationDataConfigOutput'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.OutputDataConfig'>
- **Required**: Yes

### customizationType
- **Type**: typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']
- **Required**: Yes

### outputModelKmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### trainingMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.TrainingMetrics'>
- **Required**: Yes

### validationMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ValidatorMetric]
- **Required**: Yes

### vpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfigOutput'>
- **Required**: Yes

### customizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.CustomizationConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelImportJobRequest

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelImportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelDataSource'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfigOutput'>
- **Required**: Yes

### importedModelKmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelInvocationJobRequest

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelInvocationJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelInvocationJobInputDataConfig'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelInvocationJobOutputDataConfig'>
- **Required**: Yes

### vpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfigOutput'>
- **Required**: Yes

### timeoutDurationInHours
- **Type**: <class 'int'>
- **Required**: Yes

### jobExpirationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelInvocationLoggingConfigurationResponse

### loggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.LoggingConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetPromptRouterRequest

### promptRouterArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPromptRouterResponse

### promptRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### routingCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RoutingCriteria'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### promptRouterArn
- **Type**: <class 'str'>
- **Required**: Yes

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptRouterTargetModel]
- **Required**: Yes

### fallbackModel
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptRouterTargetModel'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE']
- **Required**: Yes

### type
- **Type**: typing.Literal['custom', 'default']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GetProvisionedModelThroughputRequest

### provisionedModelId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProvisionedModelThroughputResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# GuardrailConfiguration

### guardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GuardrailContentFilter

### type
- **Type**: typing.Literal['HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK', 'SEXUAL', 'VIOLENCE']
- **Required**: Yes

### inputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### outputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### inputModalities
- **Type**: typing.Optional[typing.List[typing.Literal['IMAGE', 'TEXT']]]

### outputModalities
- **Type**: typing.Optional[typing.List[typing.Literal['IMAGE', 'TEXT']]]


# GuardrailContentFilterConfig

### type
- **Type**: typing.Literal['HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK', 'SEXUAL', 'VIOLENCE']
- **Required**: Yes

### inputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### outputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### inputModalities
- **Type**: typing.Optional[typing.List[typing.Literal['IMAGE', 'TEXT']]]

### outputModalities
- **Type**: typing.Optional[typing.List[typing.Literal['IMAGE', 'TEXT']]]


# GuardrailContentPolicy

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContentFilter]]


# GuardrailContentPolicyConfig

### filtersConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContentFilterConfig]
- **Required**: Yes


# GuardrailContextualGroundingFilter

### type
- **Type**: typing.Literal['GROUNDING', 'RELEVANCE']
- **Required**: Yes

### threshold
- **Type**: <class 'float'>
- **Required**: Yes


# GuardrailContextualGroundingFilterConfig

### type
- **Type**: typing.Literal['GROUNDING', 'RELEVANCE']
- **Required**: Yes

### threshold
- **Type**: <class 'float'>
- **Required**: Yes


# GuardrailContextualGroundingPolicy

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContextualGroundingFilter]
- **Required**: Yes


# GuardrailContextualGroundingPolicyConfig

### filtersConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContextualGroundingFilterConfig]
- **Required**: Yes


# GuardrailManagedWords

### type
- **Type**: typing.Literal['PROFANITY']
- **Required**: Yes


# GuardrailManagedWordsConfig

### type
- **Type**: typing.Literal['PROFANITY']
- **Required**: Yes


# GuardrailPiiEntity

### type
- **Type**: typing.Literal['ADDRESS', 'AGE', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CARD_CVV', 'CREDIT_DEBIT_CARD_EXPIRY', 'CREDIT_DEBIT_CARD_NUMBER', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSWORD', 'PHONE', 'PIN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_BANK_ACCOUNT_NUMBER', 'US_BANK_ROUTING_NUMBER', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'US_PASSPORT_NUMBER', 'US_SOCIAL_SECURITY_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']
- **Required**: Yes

### action
- **Type**: typing.Literal['ANONYMIZE', 'BLOCK']
- **Required**: Yes


# GuardrailPiiEntityConfig

### type
- **Type**: typing.Literal['ADDRESS', 'AGE', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CARD_CVV', 'CREDIT_DEBIT_CARD_EXPIRY', 'CREDIT_DEBIT_CARD_NUMBER', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSWORD', 'PHONE', 'PIN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_BANK_ACCOUNT_NUMBER', 'US_BANK_ROUTING_NUMBER', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'US_PASSPORT_NUMBER', 'US_SOCIAL_SECURITY_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']
- **Required**: Yes

### action
- **Type**: typing.Literal['ANONYMIZE', 'BLOCK']
- **Required**: Yes


# GuardrailRegex

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


# GuardrailRegexConfig

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


# GuardrailSensitiveInformationPolicy

### piiEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailPiiEntity]]

### regexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailRegex]]


# GuardrailSensitiveInformationPolicyConfig

### piiEntitiesConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailPiiEntityConfig]]

### regexesConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailRegexConfig]]


# GuardrailSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'READY', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# GuardrailTopic

### name
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### examples
- **Type**: typing.Optional[typing.List[str]]

### type
- **Type**: typing.Optional[typing.Literal['DENY']]


# GuardrailTopicConfig

### name
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DENY']
- **Required**: Yes

### examples
- **Type**: typing.Optional[typing.List[str]]


# GuardrailTopicPolicy

### topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailTopic]
- **Required**: Yes


# GuardrailTopicPolicyConfig

### topicsConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailTopicConfig]
- **Required**: Yes


# GuardrailWord

### text
- **Type**: <class 'str'>
- **Required**: Yes


# GuardrailWordConfig

### text
- **Type**: <class 'str'>
- **Required**: Yes


# GuardrailWordPolicy

### words
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailWord]]

### managedWordLists
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailManagedWords]]


# GuardrailWordPolicyConfig

### wordsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailWordConfig]]

### managedWordListsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailManagedWordsConfig]]


# HumanEvaluationConfig

### datasetMetricConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationDatasetMetricConfig]
- **Required**: Yes

### humanWorkflowConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.HumanWorkflowConfig]

### customMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.HumanEvaluationCustomMetric]]


# HumanEvaluationConfigOutput

### datasetMetricConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationDatasetMetricConfigOutput]
- **Required**: Yes

### humanWorkflowConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.HumanWorkflowConfig]

### customMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.HumanEvaluationCustomMetric]]


# HumanEvaluationCustomMetric

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ratingMethod
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# HumanWorkflowConfig

### flowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### instructions
- **Type**: typing.Optional[str]


# ImportedModelSummary

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


# InferenceProfileModel

### modelArn
- **Type**: typing.Optional[str]


# InferenceProfileModelSource

### copyFrom
- **Type**: typing.Optional[str]


# InferenceProfileSummary

### inferenceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### inferenceProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.InferenceProfileModel]
- **Required**: Yes

### inferenceProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### type
- **Type**: typing.Literal['APPLICATION', 'SYSTEM_DEFINED']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# InvocationLogSource

### s3Uri
- **Type**: typing.Optional[str]


# InvocationLogsConfig

### invocationLogSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.InvocationLogSource'>
- **Required**: Yes

### usePromptResponse
- **Type**: typing.Optional[bool]

### requestMetadataFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RequestMetadataFilters]


# InvocationLogsConfigOutput

### invocationLogSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.InvocationLogSource'>
- **Required**: Yes

### usePromptResponse
- **Type**: typing.Optional[bool]

### requestMetadataFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RequestMetadataFiltersOutput]


# KbInferenceConfig

### textInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.TextInferenceConfig]


# KbInferenceConfigOutput

### textInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.TextInferenceConfigOutput]


# KnowledgeBaseConfig

### retrieveConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RetrieveConfig]

### retrieveAndGenerateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RetrieveAndGenerateConfiguration]


# KnowledgeBaseConfigOutput

### retrieveConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RetrieveConfigOutput]

### retrieveAndGenerateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RetrieveAndGenerateConfigurationOutput]


# KnowledgeBaseRetrievalConfiguration

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseVectorSearchConfiguration'>
- **Required**: Yes


# KnowledgeBaseRetrievalConfigurationOutput

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseVectorSearchConfigurationOutput'>
- **Required**: Yes


# KnowledgeBaseRetrieveAndGenerateConfiguration

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseRetrievalConfiguration]

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GenerationConfiguration]

### orchestrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.OrchestrationConfiguration]


# KnowledgeBaseRetrieveAndGenerateConfigurationOutput

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseRetrievalConfigurationOutput]

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GenerationConfigurationOutput]

### orchestrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.OrchestrationConfiguration]


# KnowledgeBaseVectorSearchConfiguration

### numberOfResults
- **Type**: typing.Optional[int]

### overrideSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RetrievalFilter]


# KnowledgeBaseVectorSearchConfigurationOutput

### numberOfResults
- **Type**: typing.Optional[int]

### overrideSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RetrievalFilterOutput]


# ListCustomModelsRequest

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ListCustomModelsRequestPaginate

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListCustomModelsResponse

### modelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.CustomModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEvaluationJobsRequest

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ListEvaluationJobsRequestPaginate

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListEvaluationJobsResponse

### jobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EvaluationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFoundationModelsRequest

### byProvider
- **Type**: typing.Optional[str]

### byCustomizationType
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'DISTILLATION', 'FINE_TUNING']]

### byOutputModality
- **Type**: typing.Optional[typing.Literal['EMBEDDING', 'IMAGE', 'TEXT']]

### byInferenceType
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'PROVISIONED']]


# ListFoundationModelsResponse

### modelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FoundationModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# ListGuardrailsRequest

### guardrailIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListGuardrailsRequestPaginate

### guardrailIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListGuardrailsResponse

### guardrails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportedModelsRequest

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ListImportedModelsRequestPaginate

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListImportedModelsResponse

### modelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ImportedModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInferenceProfilesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### typeEquals
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'SYSTEM_DEFINED']]


# ListInferenceProfilesRequestPaginate

### typeEquals
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'SYSTEM_DEFINED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListInferenceProfilesResponse

### inferenceProfileSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.InferenceProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMarketplaceModelEndpointsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### modelSourceEquals
- **Type**: typing.Optional[str]


# ListMarketplaceModelEndpointsRequestPaginate

### modelSourceEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListMarketplaceModelEndpointsResponse

### marketplaceModelEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.MarketplaceModelEndpointSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelCopyJobsRequest

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ListModelCopyJobsRequestPaginate

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListModelCopyJobsResponse

### modelCopyJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelCopyJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelCustomizationJobsRequest

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ListModelCustomizationJobsRequestPaginate

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListModelCustomizationJobsResponse

### modelCustomizationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelCustomizationJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelImportJobsRequest

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ListModelImportJobsRequestPaginate

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListModelImportJobsResponse

### modelImportJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelImportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListModelInvocationJobsRequest

### submitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### submitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ListModelInvocationJobsRequestPaginate

### submitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### submitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Expired', 'Failed', 'InProgress', 'PartiallyCompleted', 'Scheduled', 'Stopped', 'Stopping', 'Submitted', 'Validating']]

### nameContains
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListModelInvocationJobsResponse

### invocationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelInvocationJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPromptRoutersRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['custom', 'default']]


# ListPromptRoutersRequestPaginate

### type
- **Type**: typing.Optional[typing.Literal['custom', 'default']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListPromptRoutersResponse

### promptRouterSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptRouterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProvisionedModelThroughputsRequest

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ListProvisionedModelThroughputsRequestPaginate

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PaginatorConfig]


# ListProvisionedModelThroughputsResponse

### provisionedModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ProvisionedModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingConfig

### cloudWatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.CloudWatchConfig]

### s3Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.S3Config]

### textDataDeliveryEnabled
- **Type**: typing.Optional[bool]

### imageDataDeliveryEnabled
- **Type**: typing.Optional[bool]

### embeddingDataDeliveryEnabled
- **Type**: typing.Optional[bool]

### videoDataDeliveryEnabled
- **Type**: typing.Optional[bool]


# MarketplaceModelEndpoint

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EndpointConfigOutput'>
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


# MarketplaceModelEndpointSummary

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


# ModelCopyJobSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]]

### failureMessage
- **Type**: typing.Optional[str]

### sourceModelName
- **Type**: typing.Optional[str]


# ModelCustomizationJobSummary

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


# ModelDataSource

### s3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.S3DataSource]


# ModelImportJobSummary

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


# ModelInvocationJobInputDataConfig

### s3InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelInvocationJobS3InputDataConfig]


# ModelInvocationJobOutputDataConfig

### s3OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelInvocationJobS3OutputDataConfig]


# ModelInvocationJobS3InputDataConfig

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### s3InputFormat
- **Type**: typing.Optional[typing.Literal['JSONL']]

### s3BucketOwner
- **Type**: typing.Optional[str]


# ModelInvocationJobS3OutputDataConfig

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### s3EncryptionKeyId
- **Type**: typing.Optional[str]

### s3BucketOwner
- **Type**: typing.Optional[str]


# ModelInvocationJobSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelInvocationJobInputDataConfig'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ModelInvocationJobOutputDataConfig'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfigOutput]

### timeoutDurationInHours
- **Type**: typing.Optional[int]

### jobExpirationTime
- **Type**: typing.Optional[datetime.datetime]


# OrchestrationConfiguration

### queryTransformationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.QueryTransformationConfiguration'>
- **Required**: Yes


# OutputDataConfig

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceConfiguration

### latency
- **Type**: typing.Optional[typing.Literal['optimized', 'standard']]


# PromptRouterSummary

### promptRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### routingCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RoutingCriteria'>
- **Required**: Yes

### promptRouterArn
- **Type**: <class 'str'>
- **Required**: Yes

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptRouterTargetModel]
- **Required**: Yes

### fallbackModel
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.PromptRouterTargetModel'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE']
- **Required**: Yes

### type
- **Type**: typing.Literal['custom', 'default']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# PromptRouterTargetModel

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes


# PromptTemplate

### textPromptTemplate
- **Type**: typing.Optional[str]


# ProvisionedModelSummary

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


# PutModelInvocationLoggingConfigurationRequest

### loggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.LoggingConfig'>
- **Required**: Yes


# QueryTransformationConfiguration

### type
- **Type**: typing.Literal['QUERY_DECOMPOSITION']
- **Required**: Yes


# RAGConfig

### knowledgeBaseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseConfig]


# RAGConfigOutput

### knowledgeBaseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseConfigOutput]


# RegisterMarketplaceModelEndpointRequest

### endpointIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### modelSourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterMarketplaceModelEndpointResponse

### marketplaceModelEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.MarketplaceModelEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# RequestMetadataBaseFilters

### equals
- **Type**: typing.Optional[typing.Dict[str, str]]

### notEquals
- **Type**: typing.Optional[typing.Dict[str, str]]


# RequestMetadataBaseFiltersOutput

### equals
- **Type**: typing.Optional[typing.Dict[str, str]]

### notEquals
- **Type**: typing.Optional[typing.Dict[str, str]]


# RequestMetadataFilters

### equals
- **Type**: typing.Optional[typing.Dict[str, str]]

### notEquals
- **Type**: typing.Optional[typing.Dict[str, str]]

### andAll
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RequestMetadataBaseFilters]]

### orAll
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RequestMetadataBaseFilters]]


# RequestMetadataFiltersOutput

### equals
- **Type**: typing.Optional[typing.Dict[str, str]]

### notEquals
- **Type**: typing.Optional[typing.Dict[str, str]]

### andAll
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RequestMetadataBaseFiltersOutput]]

### orAll
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.RequestMetadataBaseFiltersOutput]]


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


# RetrievalFilter

### equals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### notEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### in_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### notIn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### startsWith
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### listContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### stringContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttribute]

### andAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### orAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# RetrievalFilterOutput

### equals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### notEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### in_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### notIn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### startsWith
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### listContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### stringContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.FilterAttributeOutput]

### andAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### orAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# RetrieveAndGenerateConfiguration

### type
- **Type**: typing.Literal['EXTERNAL_SOURCES', 'KNOWLEDGE_BASE']
- **Required**: Yes

### knowledgeBaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseRetrieveAndGenerateConfiguration]

### externalSourcesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ExternalSourcesRetrieveAndGenerateConfiguration]


# RetrieveAndGenerateConfigurationOutput

### type
- **Type**: typing.Literal['EXTERNAL_SOURCES', 'KNOWLEDGE_BASE']
- **Required**: Yes

### knowledgeBaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseRetrieveAndGenerateConfigurationOutput]

### externalSourcesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ExternalSourcesRetrieveAndGenerateConfigurationOutput]


# RetrieveConfig

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseRetrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseRetrievalConfiguration'>
- **Required**: Yes


# RetrieveConfigOutput

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseRetrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.KnowledgeBaseRetrievalConfigurationOutput'>
- **Required**: Yes


# RoutingCriteria

### responseQualityDifference
- **Type**: <class 'float'>
- **Required**: Yes


# S3Config

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# S3DataSource

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# S3ObjectDoc

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# SageMakerEndpoint

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfig]


# SageMakerEndpointOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.VpcConfigOutput]


# StopEvaluationJobRequest

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopModelCustomizationJobRequest

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopModelInvocationJobRequest

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Tag]
- **Required**: Yes


# TeacherModelConfig

### teacherModelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResponseLengthForInference
- **Type**: typing.Optional[int]


# TextInferenceConfig

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.List[str]]


# TextInferenceConfigOutput

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.List[str]]


# TrainingDataConfig

### s3Uri
- **Type**: typing.Optional[str]

### invocationLogsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.InvocationLogsConfig]


# TrainingDataConfigOutput

### s3Uri
- **Type**: typing.Optional[str]

### invocationLogsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.InvocationLogsConfigOutput]


# TrainingMetrics

### trainingLoss
- **Type**: typing.Optional[float]


# UntagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateGuardrailRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailTopicPolicyConfig]

### contentPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContentPolicyConfig]

### wordPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailWordPolicyConfig]

### sensitiveInformationPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailSensitiveInformationPolicyConfig]

### contextualGroundingPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.GuardrailContextualGroundingPolicyConfig]

### kmsKeyId
- **Type**: typing.Optional[str]


# UpdateGuardrailResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMarketplaceModelEndpointRequest

### endpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### endpointConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EndpointConfig, aws_resource_validator.pydantic_models.bedrock.bedrock_classes.EndpointConfigOutput]
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdateMarketplaceModelEndpointResponse

### marketplaceModelEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.MarketplaceModelEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock.bedrock_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProvisionedModelThroughputRequest

### provisionedModelId
- **Type**: <class 'str'>
- **Required**: Yes

### desiredProvisionedModelName
- **Type**: typing.Optional[str]

### desiredModelId
- **Type**: typing.Optional[str]


# ValidationDataConfig

### validators
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Validator]
- **Required**: Yes


# ValidationDataConfigOutput

### validators
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock.bedrock_classes.Validator]
- **Required**: Yes


# Validator

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# ValidatorMetric

### validationLoss
- **Type**: typing.Optional[float]


# VpcConfig

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigOutput

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes



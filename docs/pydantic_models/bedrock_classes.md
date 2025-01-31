# Bedrock Classes

# AutomatedEvaluationConfigOutputTypeDef

### datasetMetricConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationDatasetMetricConfigOutputTypeDef]
- **Required**: Yes


# AutomatedEvaluationConfigTypeDef

### datasetMetricConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationDatasetMetricConfigTypeDef]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchConfigTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### largeDataDeliveryS3Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.S3ConfigTypeDef]


# CreateEvaluationJobRequestRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### evaluationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationConfigTypeDef'>
- **Required**: Yes

### inferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.EvaluationInferenceConfigTypeDef'>
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


# CreateEvaluationJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGuardrailRequestRequestTypeDef

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


# CreateGuardrailVersionRequestRequestTypeDef

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


# CreateModelCustomizationJobRequestRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### customModelName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BaseValidatorModelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.TrainingDataConfigTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### hyperParameters
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### customizationType
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'FINE_TUNING']]

### customModelKmsKeyId
- **Type**: typing.Optional[str]

### jobTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### customModelTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.TagTypeDef]]

### validationDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.ValidationDataConfigTypeDef]

### vpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.VpcConfigTypeDef]


# CreateModelCustomizationJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProvisionedModelThroughputRequestRequestTypeDef

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

### BaseValidatorModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### BaseValidatorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### customizationType
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'FINE_TUNING']]


# DeleteCustomModelRequestRequestTypeDef

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGuardrailRequestRequestTypeDef

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: typing.Optional[str]


# DeleteProvisionedModelThroughputRequestRequestTypeDef

### provisionedModelId
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluationBedrockModelTypeDef

### modelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inferenceParams
- **Type**: <class 'str'>
- **Required**: Yes


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


# EvaluationInferenceConfigTypeDef

### models
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationModelConfigTypeDef]]


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
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
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
- **Type**: typing.List[str]
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
- **Type**: typing.Optional[typing.List[typing.Literal['CONTINUED_PRE_TRAINING', 'FINE_TUNING']]]

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
- **Type**: typing.Optional[typing.List[typing.Literal['CONTINUED_PRE_TRAINING', 'FINE_TUNING']]]

### inferenceTypesSupported
- **Type**: typing.Optional[typing.List[typing.Literal['ON_DEMAND', 'PROVISIONED']]]

### modelLifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.FoundationModelLifecycleTypeDef]


# GetCustomModelRequestRequestTypeDef

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

### BaseValidatorModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### customizationType
- **Type**: typing.Literal['CONTINUED_PRE_TRAINING', 'FINE_TUNING']
- **Required**: Yes

### modelKmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### hyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### trainingDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.TrainingDataConfigTypeDef'>
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEvaluationJobRequestRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEvaluationJobResponseTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
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


# GetFoundationModelRequestRequestTypeDef

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


# GetGuardrailRequestRequestTypeDef

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


# GetModelCustomizationJobRequestRequestTypeDef

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

### BaseValidatorModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### hyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### trainingDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.TrainingDataConfigTypeDef'>
- **Required**: Yes

### validationDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ValidationDataConfigOutputTypeDef'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### customizationType
- **Type**: typing.Literal['CONTINUED_PRE_TRAINING', 'FINE_TUNING']
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


# GetProvisionedModelThroughputRequestRequestTypeDef

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


# GuardrailContentFilterConfigTypeDef

### type
- **Type**: typing.Literal['HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK', 'SEXUAL', 'VIOLENCE']
- **Required**: Yes

### inputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### outputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes


# GuardrailContentFilterTypeDef

### type
- **Type**: typing.Literal['HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK', 'SEXUAL', 'VIOLENCE']
- **Required**: Yes

### inputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### outputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes


# GuardrailContentPolicyConfigTypeDef

### filtersConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContentFilterConfigTypeDef]
- **Required**: Yes


# GuardrailContentPolicyTypeDef

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContentFilterTypeDef]]


# GuardrailContextualGroundingFilterConfigTypeDef

### type
- **Type**: typing.Literal['GROUNDING', 'RELEVANCE']
- **Required**: Yes

### threshold
- **Type**: <class 'float'>
- **Required**: Yes


# GuardrailContextualGroundingFilterTypeDef

### type
- **Type**: typing.Literal['GROUNDING', 'RELEVANCE']
- **Required**: Yes

### threshold
- **Type**: <class 'float'>
- **Required**: Yes


# GuardrailContextualGroundingPolicyConfigTypeDef

### filtersConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContextualGroundingFilterConfigTypeDef]
- **Required**: Yes


# GuardrailContextualGroundingPolicyTypeDef

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailContextualGroundingFilterTypeDef]
- **Required**: Yes


# GuardrailManagedWordsConfigTypeDef

### type
- **Type**: typing.Literal['PROFANITY']
- **Required**: Yes


# GuardrailManagedWordsTypeDef

### type
- **Type**: typing.Literal['PROFANITY']
- **Required**: Yes


# GuardrailPiiEntityConfigTypeDef

### type
- **Type**: typing.Literal['ADDRESS', 'AGE', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CARD_CVV', 'CREDIT_DEBIT_CARD_EXPIRY', 'CREDIT_DEBIT_CARD_NUMBER', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSWORD', 'PHONE', 'PIN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_BANK_ACCOUNT_NUMBER', 'US_BANK_ROUTING_NUMBER', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'US_PASSPORT_NUMBER', 'US_SOCIAL_SECURITY_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']
- **Required**: Yes

### action
- **Type**: typing.Literal['ANONYMIZE', 'BLOCK']
- **Required**: Yes


# GuardrailPiiEntityTypeDef

### type
- **Type**: typing.Literal['ADDRESS', 'AGE', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CARD_CVV', 'CREDIT_DEBIT_CARD_EXPIRY', 'CREDIT_DEBIT_CARD_NUMBER', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSWORD', 'PHONE', 'PIN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_BANK_ACCOUNT_NUMBER', 'US_BANK_ROUTING_NUMBER', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'US_PASSPORT_NUMBER', 'US_SOCIAL_SECURITY_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']
- **Required**: Yes

### action
- **Type**: typing.Literal['ANONYMIZE', 'BLOCK']
- **Required**: Yes


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


# GuardrailTopicConfigTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]


# GuardrailTopicPolicyConfigTypeDef

### topicsConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailTopicConfigTypeDef]
- **Required**: Yes


# GuardrailTopicPolicyTypeDef

### topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.GuardrailTopicTypeDef]
- **Required**: Yes


# GuardrailTopicTypeDef

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


# ListCustomModelsRequestListCustomModelsPaginateTypeDef

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### nameContains
- **Type**: typing.Optional[str]

### BaseValidatorModelArnEquals
- **Type**: typing.Optional[str]

### foundationModelArnEquals
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListCustomModelsRequestRequestTypeDef

### creationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### creationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### nameContains
- **Type**: typing.Optional[str]

### BaseValidatorModelArnEquals
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


# ListCustomModelsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### modelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.CustomModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEvaluationJobsRequestListEvaluationJobsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListEvaluationJobsRequestRequestTypeDef

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


# ListEvaluationJobsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### jobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.EvaluationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFoundationModelsRequestRequestTypeDef

### byProvider
- **Type**: typing.Optional[str]

### byCustomizationType
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'FINE_TUNING']]

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


# ListGuardrailsRequestListGuardrailsPaginateTypeDef

### guardrailIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListGuardrailsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListModelCustomizationJobsRequestListModelCustomizationJobsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListModelCustomizationJobsRequestRequestTypeDef

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


# ListModelCustomizationJobsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### modelCustomizationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ModelCustomizationJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProvisionedModelThroughputsRequestListProvisionedModelThroughputsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_classes.PaginatorConfigTypeDef]


# ListProvisionedModelThroughputsRequestRequestTypeDef

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


# ListProvisionedModelThroughputsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_classes.ProvisionedModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ModelCustomizationJobSummaryTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### BaseValidatorModelArn
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
- **Type**: typing.Optional[typing.Literal['CONTINUED_PRE_TRAINING', 'FINE_TUNING']]


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


# PutModelInvocationLoggingConfigurationRequestRequestTypeDef

### loggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_classes.LoggingConfigTypeDef'>
- **Required**: Yes


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


# S3ConfigTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# StopEvaluationJobRequestRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopModelCustomizationJobRequestRequestTypeDef

### jobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

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


# TrainingDataConfigTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# TrainingMetricsTypeDef

### trainingLoss
- **Type**: typing.Optional[float]


# UntagResourceRequestRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGuardrailRequestRequestTypeDef

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


# UpdateProvisionedModelThroughputRequestRequestTypeDef

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



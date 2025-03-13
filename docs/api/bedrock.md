# Bedrock Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### BaseModelIdentifier
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)`
- **Min Length**: 1
- **Max Length**: 2048

### BedrockModelArn
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))))|(arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{1,20}):(|[0-9]{12}):inference-profile/[a-zA-Z0-9-:.]+)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|(([0-9a-zA-Z][_-]?)+)`
- **Min Length**: 1
- **Max Length**: 2048

### BedrockModelId
- **Type**: string
- **Pattern**: `[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`
- **Min Length**: 0
- **Max Length**: 140

### BrandedName
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 20

### ContentType
- **Type**: string
- **Pattern**: `.*[a-z]{1,20}/.{1,20}.*`

### CustomModelArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}/[a-z0-9]{12}`
- **Min Length**: 20
- **Max Length**: 1011

### CustomModelName
- **Type**: string
- **Pattern**: `([0-9a-zA-Z][_-]?){1,63}`
- **Min Length**: 1
- **Max Length**: 63

### EvaluationDatasetName
- **Type**: string
- **Pattern**: `[0-9a-zA-Z-_.]+`
- **Min Length**: 1
- **Max Length**: 63

### EvaluationJobArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:evaluation-job/[a-z0-9]{12}`
- **Min Length**: 0
- **Max Length**: 1011

### EvaluationJobDescription
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 200

### EvaluationJobIdentifier
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:evaluation-job/[a-z0-9]{12})`
- **Min Length**: 0
- **Max Length**: 1011

### EvaluationJobName
- **Type**: string
- **Pattern**: `[a-z0-9](-*[a-z0-9]){0,62}`
- **Min Length**: 1
- **Max Length**: 63

### EvaluationMetricDescription
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 63

### EvaluationMetricName
- **Type**: string
- **Pattern**: `[0-9a-zA-Z-_.]+`
- **Min Length**: 1
- **Max Length**: 63

### EvaluationModelIdentifier
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:((:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:provisioned-model/[a-z0-9]{12})|([0-9]{12}:imported-model/[a-z0-9]{12})|([0-9]{12}:application-inference-profile/[a-z0-9]{12})|([0-9]{12}:inference-profile/(([a-z-]{2,8}.)[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))|([0-9]{12}:default-prompt-router/[a-zA-Z0-9-:.]+)))|(([a-z]{2}[.]{1})([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|arn:aws(-[^:]+)?:sagemaker:[a-z0-9-]{1,20}:[0-9]{12}:endpoint/[a-z0-9-]{1,63}`
- **Min Length**: 1
- **Max Length**: 2048

### EvaluationRatingMethod
- **Type**: string
- **Pattern**: `[0-9a-zA-Z-_]+`
- **Min Length**: 1
- **Max Length**: 100

### EvaluationTaskType
- **Type**: string
- **Pattern**: `[A-Za-z0-9]+`
- **Min Length**: 1
- **Max Length**: 63

### EvaluatorModelIdentifier
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}$|(^[a-z0-9-]+[.][a-z0-9-]+([.][a-z0-9-]+)*(:[a-z0-9-]+)?$)|^[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`
- **Min Length**: 1
- **Max Length**: 2048

### FoundationModelArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}`

### GuardrailArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+`
- **Min Length**: 0
- **Max Length**: 2048

### GuardrailConfigurationGuardrailIdString
- **Type**: string
- **Pattern**: `[a-z0-9]+`
- **Min Length**: 0
- **Max Length**: 64

### GuardrailConfigurationGuardrailVersionString
- **Type**: string
- **Pattern**: `(([1-9][0-9]{0,7})|(DRAFT))`
- **Min Length**: 1
- **Max Length**: 5

### GuardrailDraftVersion
- **Type**: string
- **Pattern**: `DRAFT`
- **Min Length**: 5
- **Max Length**: 5

### GuardrailId
- **Type**: string
- **Pattern**: `[a-z0-9]+`
- **Min Length**: 0
- **Max Length**: 64

### GuardrailIdentifier
- **Type**: string
- **Pattern**: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`
- **Min Length**: 0
- **Max Length**: 2048

### GuardrailName
- **Type**: string
- **Pattern**: `[0-9a-zA-Z-_]+`
- **Min Length**: 1
- **Max Length**: 50

### GuardrailNumericalVersion
- **Type**: string
- **Pattern**: `[1-9][0-9]{0,7}`

### GuardrailTopicName
- **Type**: string
- **Pattern**: `[0-9a-zA-Z-_ !?.]+`
- **Min Length**: 1
- **Max Length**: 100

### GuardrailVersion
- **Type**: string
- **Pattern**: `(([1-9][0-9]{0,7})|(DRAFT))`

### HumanTaskInstructions
- **Type**: string
- **Pattern**: `[\S\s]+`
- **Min Length**: 1
- **Max Length**: 5000

### IdempotencyToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Min Length**: 1
- **Max Length**: 256

### ImportedModelArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:imported-model/[a-z0-9]{12}`
- **Min Length**: 20
- **Max Length**: 1011

### ImportedModelIdentifier
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:imported-model/[a-z0-9]{12})|(([0-9a-zA-Z][_-]?)+)`
- **Min Length**: 1
- **Max Length**: 1011

### ImportedModelName
- **Type**: string
- **Pattern**: `([0-9a-zA-Z][_-]?)+`
- **Min Length**: 1
- **Max Length**: 63

### InferenceProfileArn
- **Type**: string
- **Pattern**: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+`
- **Min Length**: 1
- **Max Length**: 2048

### InferenceProfileDescription
- **Type**: string
- **Pattern**: `([0-9a-zA-Z:.][ _-]?)+`
- **Min Length**: 1
- **Max Length**: 200

### InferenceProfileId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-:.]+`
- **Min Length**: 1
- **Max Length**: 64

### InferenceProfileIdentifier
- **Type**: string
- **Pattern**: `(arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|application-inference-profile)/)?[a-zA-Z0-9-:.]+`
- **Min Length**: 1
- **Max Length**: 2048

### InferenceProfileModelSourceArn
- **Type**: string
- **Pattern**: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|foundation-model)/[a-zA-Z0-9-:.]+`
- **Min Length**: 1
- **Max Length**: 2048

### InferenceProfileName
- **Type**: string
- **Pattern**: `([0-9a-zA-Z][ _-]?)+`
- **Min Length**: 1
- **Max Length**: 64

### JobName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*`
- **Min Length**: 1
- **Max Length**: 63

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
- **Min Length**: 1
- **Max Length**: 2048

### KmsKeyId
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`
- **Min Length**: 1
- **Max Length**: 2048

### KnowledgeBaseId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z]+`
- **Min Length**: 0
- **Max Length**: 10

### ModelArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))`
- **Min Length**: 20
- **Max Length**: 1011

### ModelCopyJobArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-copy-job/[a-z0-9]{12}`
- **Min Length**: 0
- **Max Length**: 1011

### ModelCustomizationJobArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-customization-job/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}/[a-z0-9]{12}`
- **Min Length**: 0
- **Max Length**: 1011

### ModelCustomizationJobIdentifier
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-customization-job/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*)`
- **Min Length**: 0
- **Max Length**: 1011

### ModelId
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-:]{1,63}/[a-z0-9]{12}$)|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}$)))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)`
- **Min Length**: 1
- **Max Length**: 2048

### ModelIdentifier
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+)`
- **Min Length**: 1
- **Max Length**: 2048

### ModelImportJobArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-import-job/[a-z0-9]{12}`
- **Min Length**: 0
- **Max Length**: 1011

### ModelImportJobIdentifier
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-import-job/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*)`
- **Min Length**: 0
- **Max Length**: 1011

### ModelInvocationIdempotencyToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]{1,256}(-*[a-zA-Z0-9]){0,256}`
- **Min Length**: 1
- **Max Length**: 256

### ModelInvocationJobArn
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-invocation-job/[a-z0-9]{12})`
- **Min Length**: 0
- **Max Length**: 1011

### ModelInvocationJobIdentifier
- **Type**: string
- **Pattern**: `((arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-invocation-job/)?[a-z0-9]{12})`
- **Min Length**: 0
- **Max Length**: 1011

### ModelInvocationJobName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]{1,63}(-*[a-zA-Z0-9\+\-\.]){0,63}`
- **Min Length**: 1
- **Max Length**: 63

### ModelName
- **Type**: string
- **Pattern**: `([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63})`
- **Min Length**: 1
- **Max Length**: 63

### ModelSourceIdentifier
- **Type**: string
- **Pattern**: `.*arn:aws:sagemaker:.*:hub-content/SageMakerPublicHub/Model/.*`
- **Min Length**: 0
- **Max Length**: 2048

### NonBlankString
- **Type**: string
- **Pattern**: `[\s\S]*`

### PaginationToken
- **Type**: string
- **Pattern**: `\S*`
- **Min Length**: 1
- **Max Length**: 2048

### PromptRouterArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:default-prompt-router/[a-zA-Z0-9-:.]+`
- **Min Length**: 1
- **Max Length**: 2048

### PromptRouterDescription
- **Type**: string
- **Pattern**: `([0-9a-zA-Z:.][ _-]?)+`
- **Min Length**: 1
- **Max Length**: 200

### PromptRouterName
- **Type**: string
- **Pattern**: `([0-9a-zA-Z][ _-]?)+`
- **Min Length**: 1
- **Max Length**: 64

### PromptRouterTargetModelArn
- **Type**: string
- **Pattern**: `.*(^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})|(^arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+)`
- **Min Length**: 1
- **Max Length**: 2048

### Provider
- **Type**: string
- **Pattern**: `[A-Za-z0-9- ]{1,63}`

### ProvisionedModelArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}`

### ProvisionedModelId
- **Type**: string
- **Pattern**: `((([0-9a-zA-Z][_-]?)+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}))`

### ProvisionedModelName
- **Type**: string
- **Pattern**: `([0-9a-zA-Z][_-]?)+`
- **Min Length**: 1
- **Max Length**: 63

### RequestMetadataMapKeyString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\s._:/=+$@-]{1,256}`
- **Min Length**: 1
- **Max Length**: 256

### RequestMetadataMapValueString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\s._:/=+$@-]{0,256}`
- **Min Length**: 0
- **Max Length**: 256

### RoleArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`
- **Min Length**: 0
- **Max Length**: 2048

### S3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][-.a-z0-9]{1,61}(?:/[-!_*\'().a-z0-9A-Z]+(?:/[-!_*\'().a-z0-9A-Z]+)*)?/?`
- **Min Length**: 1
- **Max Length**: 1024

### SageMakerFlowDefinitionArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:sagemaker:[a-z0-9-]{1,20}:[0-9]{12}:flow-definition/.*`
- **Min Length**: 0
- **Max Length**: 1024

### SecurityGroupId
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+`
- **Min Length**: 0
- **Max Length**: 32

### SubnetId
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+`
- **Min Length**: 0
- **Max Length**: 32

### TagKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\s._:/=+@-]*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\s._:/=+@-]*`
- **Min Length**: 0
- **Max Length**: 256

### TaggableResourcesArn
- **Type**: string
- **Pattern**: `.*(^[a-zA-Z0-9][a-zA-Z0-9\-]*$)|(^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:([0-9]{12}|)((:(fine-tuning-job|model-customization-job|custom-model)/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12})$)|(:guardrail/[a-z0-9]+$)|(:automated-reasoning-policy/[a-zA-Z0-9]+(:[a-zA-Z0-9]+)?$)|(:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+$)|(:(provisioned-model|model-invocation-job|model-evaluation-job|evaluation-job|model-import-job|imported-model|async-invoke|provisioned-model-v2|provisioned-model-reservation|prompt-router)/[a-z0-9]{12}$))).*`
- **Min Length**: 20
- **Max Length**: 1011

### TeacherModelIdentifier
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)`

### kBS3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.{1,1024}`
- **Min Length**: 1
- **Max Length**: 1024


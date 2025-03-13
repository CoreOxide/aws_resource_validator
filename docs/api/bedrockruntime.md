# Bedrockruntime Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9]{12}`

### AsyncInvokeArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9\-]+:bedrock:[a-z0-9\-]*:[0-9]*:(provisioned-model|foundation-model)/.+`
- **Min Length**: 1
- **Max Length**: 2048

### AsyncInvokeIdempotencyToken
- **Type**: string
- **Pattern**: `[!-~]*`
- **Min Length**: 1
- **Max Length**: 256

### AsyncInvokeIdentifier
- **Type**: string
- **Pattern**: `[a-zA-Z_\.\-/0-9:]+`
- **Min Length**: 1
- **Max Length**: 256

### ConversationalModelId
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:imported-model/[a-z0-9]{12})|([0-9]{12}:provisioned-model/[a-z0-9]{12})|([0-9]{12}:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+)))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|(([0-9a-zA-Z][_-]?)+)|([a-zA-Z0-9-:.]+)|(^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?))$|(^arn:aws:sagemaker:[a-z0-9-]+:[0-9]{12}:endpoint/[a-zA-Z0-9-]+$)|(^arn:aws(-[^:]+)?:bedrock:([0-9a-z-]{1,20}):([0-9]{12}):(default-)?prompt-router/[a-zA-Z0-9-:.]+$)`
- **Min Length**: 1
- **Max Length**: 2048

### GuardrailIdentifier
- **Type**: string
- **Pattern**: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`
- **Min Length**: 0
- **Max Length**: 2048

### GuardrailVersion
- **Type**: string
- **Pattern**: `(([1-9][0-9]{0,7})|(DRAFT))`

### InvocationArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:async-invoke/[a-z0-9]{12}`
- **Min Length**: 1
- **Max Length**: 2048

### InvokeModelIdentifier
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:imported-model/[a-z0-9]{12})|([0-9]{12}:provisioned-model/[a-z0-9]{12})|([0-9]{12}:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+)))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|(([0-9a-zA-Z][_-]?)+)|([a-zA-Z0-9-:.]+)$|(^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?))$|(^arn:aws:sagemaker:[a-z0-9-]+:[0-9]{12}:endpoint/[a-zA-Z0-9-]+$)|(^arn:aws(-[^:]+)?:bedrock:([0-9a-z-]{1,20}):([0-9]{12}):(default-)?prompt-router/[a-zA-Z0-9-:.]+$)`
- **Min Length**: 1
- **Max Length**: 2048

### InvokedModelId
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})|(arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{1,20}):(|[0-9]{12}):inference-profile/[a-zA-Z0-9-:.]+)`

### KmsKeyId
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+))`
- **Min Length**: 1
- **Max Length**: 2048

### NonBlankString
- **Type**: string
- **Pattern**: `[\s\S]*`

### PaginationToken
- **Type**: string
- **Pattern**: `\S*`
- **Min Length**: 1
- **Max Length**: 2048

### RequestMetadataKeyString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\s:_@$#=/+,-.]{1,256}`
- **Min Length**: 1
- **Max Length**: 256

### RequestMetadataValueString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\s:_@$#=/+,-.]{0,256}`
- **Min Length**: 0
- **Max Length**: 256

### S3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
- **Min Length**: 1
- **Max Length**: 1024

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

### ToolName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### ToolUseId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64


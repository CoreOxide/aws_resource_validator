# Bedrockruntime Service

### GuardrailIdentifier
- **Type**: string
- **Pattern**: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`
- **Min Length**: 0
- **Max Length**: 2048

### GuardrailVersion
- **Type**: string
- **Pattern**: `(([1-9][0-9]{0,7})|(DRAFT))`

### InvokeModelIdentifier
- **Type**: string
- **Pattern**: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:provisioned-model/[a-z0-9]{12})))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|(([0-9a-zA-Z][_-]?)+)`
- **Min Length**: 1
- **Max Length**: 2048

### NonBlankString
- **Type**: string
- **Pattern**: `[\s\S]*`


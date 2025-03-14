# Bedrockagentruntime Service

### AWSResourceARN
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent/[0-9a-zA-Z]{10}$`
- **Min Length**: 0
- **Max Length**: 2048

### AgentAliasArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}$`
- **Min Length**: 0
- **Max Length**: 2048

### AgentAliasId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]+$`
- **Min Length**: 0
- **Max Length**: 10

### AgentId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]+$`
- **Min Length**: 0
- **Max Length**: 10

### AgentVersion
- **Type**: string
- **Pattern**: `^(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})$`
- **Min Length**: 1
- **Max Length**: 5

### BedrockModelArn
- **Type**: string
- **Pattern**: `^(arn:aws(-[^:]+)?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
- **Min Length**: 1
- **Max Length**: 2048

### BedrockRerankingModelArn
- **Type**: string
- **Pattern**: `^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/(.*))?$`
- **Min Length**: 1
- **Max Length**: 2048

### ContentType
- **Type**: string
- **Pattern**: `[a-z]{1,20}/.{1,20}`

### FlowAliasIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
- **Min Length**: 0
- **Max Length**: 2048

### FlowExecutionId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._:-]+$`
- **Min Length**: 2
- **Max Length**: 100

### FlowIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})$`
- **Min Length**: 0
- **Max Length**: 2048

### GuardrailConfigurationGuardrailIdString
- **Type**: string
- **Pattern**: `^[a-z0-9]+$`
- **Min Length**: 0
- **Max Length**: 64

### GuardrailConfigurationGuardrailVersionString
- **Type**: string
- **Pattern**: `^(([1-9][0-9]{0,7})|(DRAFT))$`
- **Min Length**: 1
- **Max Length**: 5

### GuardrailIdentifierWithArn
- **Type**: string
- **Pattern**: `^(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))$`
- **Min Length**: 0
- **Max Length**: 2048

### GuardrailVersion
- **Type**: string
- **Pattern**: `^(([1-9][0-9]{0,7})|(DRAFT))$`
- **Min Length**: 1
- **Max Length**: 5

### InvocationIdentifier
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
- **Min Length**: 1
- **Max Length**: 2048

### KnowledgeBaseArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:knowledge-base/[0-9a-zA-Z]+$`
- **Min Length**: 0
- **Max Length**: 128

### KnowledgeBaseId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]+$`
- **Min Length**: 0
- **Max Length**: 10

### LambdaResourceArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
- **Min Length**: 0
- **Max Length**: 2048

### MemoryId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._:-]+$`
- **Min Length**: 2
- **Max Length**: 100

### MetadataAttributeSchemaDescriptionString
- **Type**: string
- **Pattern**: `^[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 1024

### MetadataAttributeSchemaKeyString
- **Type**: string
- **Pattern**: `^[\s\S]+$`
- **Min Length**: 1
- **Max Length**: 256

### ModelIdentifier
- **Type**: string
- **Pattern**: `(^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+))$|(^arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{1,20}):(|[0-9]{12}):inference-profile/[a-zA-Z0-9-:.]+)$`
- **Min Length**: 1
- **Max Length**: 2048

### Name
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?){1,100}$`

### NextToken
- **Type**: string
- **Pattern**: `^\S*$`
- **Min Length**: 1
- **Max Length**: 2048

### NodeInputName
- **Type**: string
- **Pattern**: `^[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}$`

### NodeName
- **Type**: string
- **Pattern**: `^[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}$`

### NodeOutputName
- **Type**: string
- **Pattern**: `^[a-zA-Z]([_]?[0-9a-zA-Z]){0,99}$`

### NonBlankString
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### OptimizePromptRequestTargetModelIdString
- **Type**: string
- **Pattern**: `^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:provisioned-model/[a-z0-9]{12})))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|(([0-9a-zA-Z][_-]?)+)$`
- **Min Length**: 1
- **Max Length**: 2048

### ParameterName
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?){1,100}$`

### ResourceName
- **Type**: string
- **Pattern**: `^([0-9a-zA-Z][_-]?){1,100}$`

### S3BucketName
- **Type**: string
- **Pattern**: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### S3ObjectKey
- **Type**: string
- **Pattern**: `^[.!*\'()_\-a-zA-Z0-9][.!*\'()_\-\/a-zA-Z0-9]*$`
- **Min Length**: 1
- **Max Length**: 1024

### S3Uri
- **Type**: string
- **Pattern**: `^s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.{1,1024}$`
- **Min Length**: 1
- **Max Length**: 1024

### SessionArn
- **Type**: string
- **Pattern**: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

### SessionId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._:-]+$`
- **Min Length**: 2
- **Max Length**: 100

### SessionIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})|([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})$`

### TagKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s._:/=+@-]*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s._:/=+@-]*$`
- **Min Length**: 0
- **Max Length**: 256

### TaggableResourcesArn
- **Type**: string
- **Pattern**: `(^arn:aws(-[^:]+)?:bedrock:[a-zA-Z0-9-]+:[0-9]{12}:(session)/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$)`
- **Min Length**: 20
- **Max Length**: 1011

### Uuid
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`


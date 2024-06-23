# Bedrockagentruntime Service

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
- **Pattern**: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))$`
- **Min Length**: 20
- **Max Length**: 1011

### ContentType
- **Type**: string
- **Pattern**: `[a-z]{1,20}/.{1,20}`

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

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
- **Min Length**: 1
- **Max Length**: 2048

### KnowledgeBaseId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z]+$`
- **Min Length**: 0
- **Max Length**: 10

### NextToken
- **Type**: string
- **Pattern**: `^\S*$`
- **Min Length**: 1
- **Max Length**: 2048

### NonBlankString
- **Type**: string
- **Pattern**: `^[\s\S]*$`

### S3Uri
- **Type**: string
- **Pattern**: `^s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.{1,1024}$`
- **Min Length**: 1
- **Max Length**: 1024

### SessionId
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._:-]+$`
- **Min Length**: 2
- **Max Length**: 100


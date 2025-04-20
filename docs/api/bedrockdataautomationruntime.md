# Bedrockdataautomationruntime Service

### BlueprintArn
- **Type**: string
- **Pattern**: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-insights-public-[a-zA-Z0-9-_]{1,30}|bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`
- **Min Length**: 0
- **Max Length**: 128

### BlueprintVersion
- **Type**: string
- **Pattern**: `[0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### DataAutomationArn
- **Type**: string
- **Pattern**: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-_]+`
- **Min Length**: 1
- **Max Length**: 128

### DataAutomationProfileArn
- **Type**: string
- **Pattern**: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-profile/[a-zA-Z0-9-_.]+`
- **Min Length**: 1
- **Max Length**: 128

### EncryptionContextKey
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2000

### EncryptionContextValue
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2000

### IdempotencyToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Min Length**: 1
- **Max Length**: 256

### InvocationArn
- **Type**: string
- **Pattern**: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:(insights-invocation|data-automation-invocation)/[a-zA-Z0-9-_]+`
- **Min Length**: 1
- **Max Length**: 128

### KMSKeyId
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]+`
- **Min Length**: 1
- **Max Length**: 2048

### NonBlankString
- **Type**: string
- **Pattern**: `[\s\S]*`

### S3Uri
- **Type**: string
- **Pattern**: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/[^\x00-\x1F\x7F\{^}%`\]">\[~<#|]*)?`
- **Min Length**: 1
- **Max Length**: 1024

### TagKey
- **Type**: string
- **Pattern**: `(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
- **Min Length**: 0
- **Max Length**: 256

### TaggableResourceArn
- **Type**: string
- **Pattern**: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-invocation/[a-zA-Z0-9-_]+`
- **Min Length**: 20
- **Max Length**: 1011


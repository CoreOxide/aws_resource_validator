# Bedrockdataautomation Service

### BlueprintArn
- **Type**: string
- **Pattern**: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`
- **Min Length**: 0
- **Max Length**: 128

### BlueprintName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]+`
- **Min Length**: 1
- **Max Length**: 128

### BlueprintVersion
- **Type**: string
- **Pattern**: `[0-9]*`
- **Min Length**: 1
- **Max Length**: 128

### ClientToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
- **Min Length**: 33
- **Max Length**: 256

### DataAutomationProjectArn
- **Type**: string
- **Pattern**: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-]{12,36}`
- **Min Length**: 0
- **Max Length**: 128

### DataAutomationProjectName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]+`
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

### KmsKeyId
- **Type**: string
- **Pattern**: `[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]+`
- **Min Length**: 1
- **Max Length**: 2048

### NextToken
- **Type**: string
- **Pattern**: `\S*`
- **Min Length**: 1
- **Max Length**: 2048

### NonBlankString
- **Type**: string
- **Pattern**: `[\s\S]+`

### TaggableResourceArn
- **Type**: string
- **Pattern**: `arn:aws(|-cn|-us-gov):bedrock:[a-z0-9-]*:[0-9]{12}:(blueprint|data-automation-project)/[a-zA-Z0-9-]{12,36}`
- **Min Length**: 20
- **Max Length**: 1011


# Cloudcontrol Service

### ClientToken
- **Type**: string
- **Pattern**: `[-A-Za-z0-9+/=]+`
- **Min Length**: 1
- **Max Length**: 128

### ErrorMessage
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 1024

### HandlerNextToken
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 2048

### Identifier
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 1024

### NextToken
- **Type**: string
- **Pattern**: `[-A-Za-z0-9+/=]+`
- **Min Length**: 1
- **Max Length**: 2048

### PatchDocument
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 65536

### Properties
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 65536

### RequestToken
- **Type**: string
- **Pattern**: `[-A-Za-z0-9+/=]+`
- **Min Length**: 1
- **Max Length**: 128

### RoleArn
- **Type**: string
- **Pattern**: `arn:.+:iam::[0-9]{12}:role/.+`
- **Min Length**: 20
- **Max Length**: 2048

### StatusMessage
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 1024

### TypeName
- **Type**: string
- **Pattern**: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}`
- **Min Length**: 10
- **Max Length**: 196

### TypeVersionId
- **Type**: string
- **Pattern**: `[A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128


# Cognitosync Service

### ApplicationArn
- **Type**: string
- **Pattern**: `arn:aws:sns:[-0-9a-z]+:\d+:app/[A-Z_]+/[a-zA-Z0-9_.-]+`

### AssumeRoleArn
- **Type**: string
- **Pattern**: `arn:aws:iam::\d+:role/.*`
- **Min Length**: 20
- **Max Length**: 2048

### DatasetName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.:-]+`
- **Min Length**: 1
- **Max Length**: 128

### IdentityId
- **Type**: string
- **Pattern**: `[\w-]+:[0-9a-f-]+`
- **Min Length**: 1
- **Max Length**: 55

### IdentityPoolId
- **Type**: string
- **Pattern**: `[\w-]+:[0-9a-f-]+`
- **Min Length**: 1
- **Max Length**: 55


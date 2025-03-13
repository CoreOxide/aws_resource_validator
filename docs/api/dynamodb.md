# Dynamodb Service

### Arn
- **Type**: string
- **Pattern**: `arn:.+`
- **Min Length**: 1
- **Max Length**: 1011

### ClientToken
- **Type**: string
- **Pattern**: `[!-~]+`
- **Min Length**: 1
- **Max Length**: 128

### TagKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.:/=+\-@ ]*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.:/=+\-@ ]*`
- **Min Length**: 0
- **Max Length**: 256


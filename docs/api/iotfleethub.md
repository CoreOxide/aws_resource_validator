# Iotfleethub Service

### Arn
- **Type**: string
- **Pattern**: `^arn:[!-~]+$`
- **Min Length**: 1
- **Max Length**: 1600

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### Description
- **Type**: string
- **Pattern**: `^[ -~]*$`
- **Min Length**: 1
- **Max Length**: 2048

### Id
- **Type**: string
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### Name
- **Type**: string
- **Pattern**: `^[ -~]*$`
- **Min Length**: 1
- **Max Length**: 100

### NextToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+/=]+$`
- **Min Length**: 1
- **Max Length**: 2048

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### Url
- **Type**: string
- **Pattern**: `^https\://\S+$`
- **Min Length**: 1
- **Max Length**: 256


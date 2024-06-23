# Mediastore Service

### ContainerARN
- **Type**: string
- **Pattern**: `arn:aws:mediastore:[a-z]+-[a-z]+-\d:\d{12}:container/[\w-]{1,255}`
- **Min Length**: 1
- **Max Length**: 1024

### ContainerName
- **Type**: string
- **Pattern**: `[\w-]+`
- **Min Length**: 1
- **Max Length**: 255

### ContainerPolicy
- **Type**: string
- **Pattern**: `[\x00-\x7F]+`
- **Min Length**: 1
- **Max Length**: 8192

### Endpoint
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 255

### ErrorMessage
- **Type**: string
- **Pattern**: `[ \w:\.\?-]+`
- **Min Length**: 1
- **Max Length**: 255

### Header
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 8192

### LifecyclePolicy
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 0
- **Max Length**: 8192

### ObjectGroup
- **Type**: string
- **Pattern**: `/?(?:[A-Za-z0-9_=:\.\-\~\*]+/){0,10}(?:[A-Za-z0-9_=:\.\-\~\*]+)?/?`
- **Min Length**: 1
- **Max Length**: 900

### ObjectGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_]+`
- **Min Length**: 1
- **Max Length**: 30

### Origin
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 2048

### PaginationToken
- **Type**: string
- **Pattern**: `[0-9A-Za-z=/+]+`
- **Min Length**: 1
- **Max Length**: 1024

### TagKey
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
- **Min Length**: 0
- **Max Length**: 256


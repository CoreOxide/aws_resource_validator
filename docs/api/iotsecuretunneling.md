# Iotsecuretunneling Service

### Description
- **Type**: string
- **Pattern**: `[^\p{C}]{1,2048}`

### NextToken
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_=-]{1,4096}`

### Service
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### ThingName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### TunnelId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-+=:]{1,128}`


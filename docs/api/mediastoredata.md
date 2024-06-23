# Mediastoredata Service

### ContentRangePattern
- **Type**: string
- **Pattern**: `^bytes=\d+\-\d+/\d+$`

### ContentType
- **Type**: string
- **Pattern**: `^[\w\-\/\.\+]{1,255}$`

### ETag
- **Type**: string
- **Pattern**: `[0-9A-Fa-f]+`
- **Min Length**: 1
- **Max Length**: 64

### ErrorMessage
- **Type**: string
- **Pattern**: `[ \w:\.\?-]+`
- **Min Length**: 1
- **Max Length**: 255

### ItemName
- **Type**: string
- **Pattern**: `[A-Za-z0-9_\.\-\~]+`

### ListPathNaming
- **Type**: string
- **Pattern**: `/?(?:[A-Za-z0-9_\.\-\~]+/){0,10}(?:[A-Za-z0-9_\.\-\~]+)?/?`
- **Min Length**: 0
- **Max Length**: 900

### PathNaming
- **Type**: string
- **Pattern**: `(?:[A-Za-z0-9_\.\-\~]+/){0,10}[A-Za-z0-9_\.\-\~]+`
- **Min Length**: 1
- **Max Length**: 900

### RangePattern
- **Type**: string
- **Pattern**: `^bytes=(?:\d+\-\d*|\d*\-\d+)$`

### SHA256Hash
- **Type**: string
- **Pattern**: `[0-9A-Fa-f]{64}`
- **Min Length**: 64
- **Max Length**: 64


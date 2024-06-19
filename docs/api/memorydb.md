# Memorydb Service

### ACLName
- **Type**: string
- **Pattern**: `[a-zA-Z][a-zA-Z0-9\-]*`
- **Min Length**: 1

### AccessString
- **Type**: string
- **Pattern**: `.*\S.*`

### FilterName
- **Type**: string
- **Pattern**: `.*\S.*`

### FilterValue
- **Type**: string
- **Pattern**: `.*\S.*`

### TargetBucket
- **Type**: string
- **Pattern**: `^[A-Za-z0-9._-]+$`
- **Max Length**: 255

### UserName
- **Type**: string
- **Pattern**: `[a-zA-Z][a-zA-Z0-9\-]*`
- **Min Length**: 1


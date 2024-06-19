# Honeycode Service

### BatchErrorMessage
- **Type**: string
- **Pattern**: `^(?!\s*$).+`

### BatchItemId
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 64

### ClientRequestToken
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 32
- **Max Length**: 64

### DelimitedTextDelimiter
- **Type**: string
- **Pattern**: `^[^\n\r\x00\x08\x0B\x0C\x0E\x1F]?$`
- **Min Length**: 1
- **Max Length**: 1

### Email
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$`
- **Min Length**: 3
- **Max Length**: 254

### Fact
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 8192

### FormattedValue
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 8192

### Formula
- **Type**: string
- **Pattern**: `^=.*`
- **Min Length**: 0
- **Max Length**: 8192

### JobId
- **Type**: string
- **Pattern**: `^[^\n\r\x00\x08\x0B\x0C\x0E\x1F]*$`
- **Min Length**: 1
- **Max Length**: 100

### PaginationToken
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 1024

### RawValue
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 32767

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:aws:honeycode:.+:[0-9]{12}:.+:.+$`
- **Min Length**: 1
- **Max Length**: 256

### ResourceId
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
- **Min Length**: 36
- **Max Length**: 36

### RowId
- **Type**: string
- **Pattern**: `row:[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
- **Min Length**: 77
- **Max Length**: 77

### SecureURL
- **Type**: string
- **Pattern**: `^https:\/\/[^\n\r\x00\x08\x0B\x0C\x0E\x1F]*$`
- **Min Length**: 1
- **Max Length**: 8000

### TagKey
- **Type**: string
- **Pattern**: `^[^\n\r\x00\x08\x0B\x0C\x0E\x1F]*$`
- **Min Length**: 1
- **Max Length**: 100

### TagValue
- **Type**: string
- **Pattern**: `^[^\n\r\x00\x08\x0B\x0C\x0E\x1F]*$`
- **Min Length**: 1
- **Max Length**: 100

### VariableName
- **Type**: string
- **Pattern**: `^(?!\s*$).+`
- **Min Length**: 1
- **Max Length**: 255


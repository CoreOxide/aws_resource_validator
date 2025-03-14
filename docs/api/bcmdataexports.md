# Bcmdataexports Service

### Arn
- **Type**: string
- **Pattern**: `^arn:aws[-a-z0-9]*:[-a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+$`
- **Min Length**: 20
- **Max Length**: 2048

### ExportName
- **Type**: string
- **Pattern**: `^[0-9A-Za-z!\-_.*\'()]+$`
- **Min Length**: 1
- **Max Length**: 128

### GenericString
- **Type**: string
- **Pattern**: `^[\S\s]*$`
- **Min Length**: 0
- **Max Length**: 1024

### NextPageToken
- **Type**: string
- **Pattern**: `^[\S\s]*$`
- **Min Length**: 0
- **Max Length**: 8192

### QueryStatement
- **Type**: string
- **Pattern**: `^[\S\s]*$`
- **Min Length**: 1
- **Max Length**: 36000

### TableName
- **Type**: string
- **Pattern**: `^[\S\s]*$`
- **Min Length**: 0
- **Max Length**: 1024

### TableProperty
- **Type**: string
- **Pattern**: `^[\S\s]*$`
- **Min Length**: 0
- **Max Length**: 1024


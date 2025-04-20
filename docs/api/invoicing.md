# Invoicing Service

### AccountIdString
- **Type**: string
- **Pattern**: `\d{12}`

### BasicString
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 0
- **Max Length**: 1024

### DescriptionString
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 0
- **Max Length**: 500

### InvoiceUnitArnString
- **Type**: string
- **Pattern**: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
- **Min Length**: 1
- **Max Length**: 256

### InvoiceUnitName
- **Type**: string
- **Pattern**: `(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )`
- **Min Length**: 1
- **Max Length**: 50

### NextTokenString
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 1
- **Max Length**: 2048

### SensitiveBasicString
- **Type**: string
- **Pattern**: `\S+`
- **Min Length**: 0
- **Max Length**: 1024

### TagrisArn
- **Type**: string
- **Pattern**: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
- **Min Length**: 20
- **Max Length**: 2048


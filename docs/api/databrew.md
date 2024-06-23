# Databrew Service

### BucketOwner
- **Type**: string
- **Pattern**: `^[0-9]{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ClientSessionId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9-]*$`
- **Min Length**: 1
- **Max Length**: 255

### Condition
- **Type**: string
- **Pattern**: `^[A-Z\_]+$`
- **Min Length**: 1
- **Max Length**: 128

### EntityType
- **Type**: string
- **Pattern**: `^[A-Z_][A-Z\\d_]*$`
- **Min Length**: 1
- **Max Length**: 128

### ErrorCode
- **Type**: string
- **Pattern**: `^[1-5][0-9][0-9]$`

### Expression
- **Type**: string
- **Pattern**: `^[<>0-9A-Za-z_.,:)(!= ]+$`
- **Min Length**: 4
- **Max Length**: 1024

### LocaleCode
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_\.#@\-]+$`
- **Min Length**: 2
- **Max Length**: 100

### Operation
- **Type**: string
- **Pattern**: `^[A-Z\_]+$`
- **Min Length**: 1
- **Max Length**: 128

### ParameterName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9]+$`
- **Min Length**: 1
- **Max Length**: 128

### Statistic
- **Type**: string
- **Pattern**: `^[A-Z\_]+$`
- **Min Length**: 1
- **Max Length**: 128

### TimezoneOffset
- **Type**: string
- **Pattern**: `^(Z|[-+](\d|\d{2}|\d{2}:?\d{2}))$`
- **Min Length**: 1
- **Max Length**: 6

### ValueReference
- **Type**: string
- **Pattern**: `^:[A-Za-z0-9_]+$`
- **Min Length**: 2
- **Max Length**: 128


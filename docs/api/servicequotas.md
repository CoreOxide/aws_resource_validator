# Servicequotas Service

### AmazonResourceName
- **Type**: string
- **Pattern**: `arn:aws(-[\w]+)*:*:.+:[0-9]{12}:.+`
- **Min Length**: 1
- **Max Length**: 1011

### AwsRegion
- **Type**: string
- **Pattern**: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
- **Min Length**: 1
- **Max Length**: 64

### NextToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/+]*={0,2}$`
- **Max Length**: 2048

### QuotaCode
- **Type**: string
- **Pattern**: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
- **Min Length**: 1
- **Max Length**: 128

### RequestId
- **Type**: string
- **Pattern**: `[0-9a-zA-Z][a-zA-Z0-9-]{1,128}`
- **Min Length**: 1
- **Max Length**: 128

### ServiceCode
- **Type**: string
- **Pattern**: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
- **Min Length**: 1
- **Max Length**: 63

### Statistic
- **Type**: string
- **Pattern**: `(Sum|Maximum)`
- **Min Length**: 1
- **Max Length**: 256

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


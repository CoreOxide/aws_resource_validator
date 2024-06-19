# Personalize Service

### Arn
- **Type**: string
- **Pattern**: `arn:([a-z\d-]+):personalize:.*:.*:.+`
- **Max Length**: 256

### KmsKeyArn
- **Type**: string
- **Pattern**: `arn:aws.*:kms:.*:[0-9]{12}:key/.*`
- **Max Length**: 2048

### Name
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
- **Min Length**: 1
- **Max Length**: 63

### NextToken
- **Type**: string
- **Pattern**: `\p{ASCII}{0,1500}`
- **Max Length**: 1500

### RoleArn
- **Type**: string
- **Pattern**: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
- **Max Length**: 256

### S3Location
- **Type**: string
- **Pattern**: `(s3|http|https)://.+`
- **Max Length**: 256

### SchedulingExpression
- **Type**: string
- **Pattern**: `rate\(\d+ days?\)`
- **Min Length**: 1
- **Max Length**: 16

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


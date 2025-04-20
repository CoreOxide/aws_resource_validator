# S3tables Service

### AccountId
- **Type**: string
- **Pattern**: `[0-9].*`
- **Min Length**: 12
- **Max Length**: 12

### NamespaceName
- **Type**: string
- **Pattern**: `[0-9a-z_]*`
- **Min Length**: 1
- **Max Length**: 255

### TableARN
- **Type**: string
- **Pattern**: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
- **Min Length**: 1
- **Max Length**: 2048

### TableBucketARN
- **Type**: string
- **Pattern**: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`

### TableBucketName
- **Type**: string
- **Pattern**: `[0-9a-z-]*`
- **Min Length**: 3
- **Max Length**: 63

### TableName
- **Type**: string
- **Pattern**: `[0-9a-z_]*`
- **Min Length**: 1
- **Max Length**: 255


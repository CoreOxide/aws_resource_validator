# Timestreamwrite Service

### BatchLoadTaskId
- **Type**: string
- **Pattern**: `[A-Z0-9]+`
- **Min Length**: 3
- **Max Length**: 32

### ResourceCreateAPIName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]+`

### S3BucketName
- **Type**: string
- **Pattern**: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
- **Min Length**: 3
- **Max Length**: 63

### S3ObjectKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9|!\-_*\'\(\)]([a-zA-Z0-9]|[!\-_*\'\(\)\/.])+`
- **Min Length**: 1
- **Max Length**: 1024

### S3ObjectKeyPrefix
- **Type**: string
- **Pattern**: `[a-zA-Z0-9|!\-_*\'\(\)]([a-zA-Z0-9]|[!\-_*\'\(\)\/.])+`
- **Min Length**: 1
- **Max Length**: 928


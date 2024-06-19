# Timestreamquery Service

### QueryId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 64

### S3BucketName
- **Type**: string
- **Pattern**: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
- **Min Length**: 3
- **Max Length**: 63

### S3ObjectKeyPrefix
- **Type**: string
- **Pattern**: `[a-zA-Z0-9|!\-_*\'\(\)]([a-zA-Z0-9]|[!\-_*\'\(\)\/.])+`
- **Min Length**: 1
- **Max Length**: 896

### ScheduledQueryName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9|!\-_*\'\(\)]([a-zA-Z0-9]|[!\-_*\'\(\)\/.])+`
- **Min Length**: 1
- **Max Length**: 64


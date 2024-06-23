# Workmailmessageflow Service

### messageIdType
- **Type**: string
- **Pattern**: `[a-z0-9\-]*`
- **Min Length**: 1
- **Max Length**: 120

### s3BucketIdType
- **Type**: string
- **Pattern**: `^[a-z0-9][a-z0-9\-]*`
- **Min Length**: 3
- **Max Length**: 63

### s3KeyIdType
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-/]*`
- **Min Length**: 1
- **Max Length**: 1024

### s3VersionType
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 1
- **Max Length**: 1024


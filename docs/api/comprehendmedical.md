# Comprehendmedical Service

### ClientRequestTokenString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 64

### IamRoleArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
- **Min Length**: 20
- **Max Length**: 2048

### JobId
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 32

### JobName
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
- **Min Length**: 1
- **Max Length**: 256

### KMSKey
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 2048

### S3Bucket
- **Type**: string
- **Pattern**: `^[0-9a-z\.\-_]*(?!\.)$`
- **Min Length**: 3
- **Max Length**: 63

### S3Key
- **Type**: string
- **Pattern**: `.*`
- **Max Length**: 1024


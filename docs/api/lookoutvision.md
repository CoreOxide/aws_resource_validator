# Lookoutvision Service

### AnomalyClassFilter
- **Type**: string
- **Pattern**: `(normal|anomaly)`
- **Min Length**: 1
- **Max Length**: 10

### AnomalyName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 256

### ClientToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 64

### Color
- **Type**: string
- **Pattern**: `\#[a-zA-Z0-9]{6}`
- **Min Length**: 7
- **Max Length**: 7

### CompilerOptions
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 3
- **Max Length**: 1024

### ComponentDescription
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_. ()\':,;?]+`
- **Min Length**: 1
- **Max Length**: 256

### ComponentName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_.]+`
- **Min Length**: 1
- **Max Length**: 128

### ComponentVersion
- **Type**: string
- **Pattern**: `^([0-9]{1,6})\.([0-9]{1,6})\.([0-9]{1,6})$`
- **Min Length**: 1
- **Max Length**: 64

### ComponentVersionArn
- **Type**: string
- **Pattern**: `arn:[^:]*:greengrass:[^:]*:aws:components:[^:]+`

### ContentType
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 255

### DatasetEntry
- **Type**: string
- **Pattern**: `^\{.*\}$`
- **Min Length**: 2
- **Max Length**: 8192

### DatasetType
- **Type**: string
- **Pattern**: `train|test`
- **Min Length**: 1
- **Max Length**: 10

### ImageSourceType
- **Type**: string
- **Pattern**: `direct`

### KmsKeyId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
- **Min Length**: 1
- **Max Length**: 2048

### ModelDescriptionMessage
- **Type**: string
- **Pattern**: `[0-9A-Za-z\.\-_]*`
- **Min Length**: 1
- **Max Length**: 500

### ModelPackagingJobDescription
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_. ()\':,;?]+`
- **Min Length**: 1
- **Max Length**: 256

### ModelPackagingJobName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 64

### ModelPackagingMethod
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 32

### ModelVersion
- **Type**: string
- **Pattern**: `([1-9][0-9]*|latest)`
- **Min Length**: 1
- **Max Length**: 10

### ModelVersionNoLatest
- **Type**: string
- **Pattern**: `([1-9][0-9]*)`
- **Min Length**: 1
- **Max Length**: 10

### PaginationToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\+\=]{0,2048}$`
- **Max Length**: 2048

### ProjectName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_\-]*`
- **Min Length**: 1
- **Max Length**: 255

### QueryString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2048

### S3BucketName
- **Type**: string
- **Pattern**: `[0-9A-Za-z\.\-_]*`
- **Min Length**: 3
- **Max Length**: 63

### S3KeyPrefix
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9!_.*\'()-][/a-zA-Z0-9!_.*\'()-]*)?$`
- **Max Length**: 1024

### S3ObjectKey
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9!_.*\'()-][/a-zA-Z0-9!_.*\'()-]*)?$`
- **Min Length**: 1
- **Max Length**: 1024

### S3ObjectVersion
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1024

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


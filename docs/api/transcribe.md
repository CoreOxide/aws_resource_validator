# Transcribe Service

### CallAnalyticsJobName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### CategoryName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### DataAccessRoleArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`
- **Min Length**: 20
- **Max Length**: 2048

### KMSKeyId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
- **Min Length**: 1
- **Max Length**: 2048

### ModelName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### NextToken
- **Type**: string
- **Pattern**: `.+`
- **Max Length**: 8192

### NonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 2000

### OutputBucketName
- **Type**: string
- **Pattern**: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
- **Max Length**: 64

### OutputKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_.!*\'()/]{1,1024}$`
- **Min Length**: 1
- **Max Length**: 1024

### Phrase
- **Type**: string
- **Pattern**: `.+`
- **Min Length**: 0
- **Max Length**: 256

### TranscribeArn
- **Type**: string
- **Pattern**: `arn:aws(-[^:]+)?:transcribe:[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z-]*/[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 1011

### TranscriptionJobName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### Uri
- **Type**: string
- **Pattern**: `(s3://|http(s*)://).+`
- **Min Length**: 1
- **Max Length**: 2000

### VocabularyFilterName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200

### VocabularyName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z._-]+`
- **Min Length**: 1
- **Max Length**: 200


# Textract Service

### AdapterDescription
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s!"\#\$%\'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`
- **Min Length**: 1
- **Max Length**: 256

### AdapterName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_]+`
- **Min Length**: 1
- **Max Length**: 128

### AdapterPage
- **Type**: string
- **Pattern**: `^[0-9\*\-]+$`
- **Min Length**: 1
- **Max Length**: 9

### AdapterVersionStatusMessage
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s!"\#\$%\'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`
- **Min Length**: 1
- **Max Length**: 256

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### HumanLoopName
- **Type**: string
- **Pattern**: `^[a-z0-9](-*[a-z0-9])*`
- **Min Length**: 1
- **Max Length**: 63

### JobId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### JobTag
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.\-:]+`
- **Min Length**: 1
- **Max Length**: 64

### KMSKeyId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
- **Min Length**: 1
- **Max Length**: 2048

### NonEmptyString
- **Type**: string
- **Pattern**: `.*\S.*`

### PaginationToken
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### QueryInput
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\s!"\#\$%\'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`
- **Min Length**: 1
- **Max Length**: 200

### QueryPage
- **Type**: string
- **Pattern**: `^[0-9\*\-]+$`
- **Min Length**: 1
- **Max Length**: 9

### RoleArn
- **Type**: string
- **Pattern**: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
- **Min Length**: 20
- **Max Length**: 2048

### S3Bucket
- **Type**: string
- **Pattern**: `[0-9A-Za-z\.\-_]*`
- **Min Length**: 3
- **Max Length**: 255

### S3ObjectName
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### S3ObjectVersion
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### SNSTopicArn
- **Type**: string
- **Pattern**: `(^arn:([a-z\d-]+):sns:[a-zA-Z\d-]{1,20}:\w{12}:.+$)`
- **Min Length**: 20
- **Max Length**: 1024

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

